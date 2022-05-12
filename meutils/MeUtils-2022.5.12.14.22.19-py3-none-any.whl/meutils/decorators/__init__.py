#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : DeepNN.
# @File         : decorator_utils
# @Time         : 2020/4/30 10:46 上午
# @Author       : yuanjie
# @Email        : meutils@qq.com
# @Software     : PyCharm
# @Description  : 可以看到，当多个装饰器装饰同一个函数时，会是一个嵌套的装饰结果，也就是说，先执行完离函数近的一个装饰器，然后再用离函数远的装饰器来装饰执行结果。
"""
@wrapt.decorator
def noargs(wrapped, instance, args, kwargs):
    logger.info(f'noargs decorator')

    return wrapped(*args, **kwargs)


def withargs(myarg1, myarg2):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        logger.info(f'withargs decorator: {myarg1}, {myarg2}')
        return wrapped(*args, **kwargs)

    return wrapper
"""
import inspect

import wrapt
from loguru import logger

# me
from meutils.decorators.common import *
from meutils.decorators.decorator import decorator


class singleton:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance


@wrapt.decorator
def opener(wrapped, instance, args, kwargs):
    """
    opener(yaml.load)("conf.yaml")
    opener(json.load)("conf.json")

    """
    path = args[0]
    with open(path) as f:
        return wrapped(f)


@wrapt.decorator
def args(wrapped, instance, args, kwargs):
    func_name = wrapped.__name__
    logger.debug(f'FUNC-{func_name} ARGS: {args}')
    logger.debug(f'FUNC-{func_name} KWARGS: {kwargs}')
    logger.debug(f'FUNC-{func_name} DEFINED ARGS: {inspect.getfullargspec(wrapped).args}')  # .varargs

    return wrapped(*args, **kwargs)


@wrapt.decorator
def deprecated(wrapped, instance, args, kwargs):
    func_name = wrapped.__name__
    logger.warning(f"{func_name} deprecated")
    return wrapped(*args, **kwargs)


@wrapt.decorator
def func(wrapped, instance, args, kwargs):  # TODO有bug待修复 dill可序列化lambda
    """包装lambda"""
    return wrapped(*args, **kwargs)


def hdfs_flag(check_dir):  # TODO: zk check
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        from meutils.aizoo import tf_io
        # 不执行
        if tf_io.check_path(f"{check_dir}/_FLAG") or tf_io.check_path(f"{check_dir}/_SUCCESS"):
            logger.info("任务正在执行或者已经执行成功")
            return

        tf_io.make_flag(check_dir)  # 执行中：生成 _FLAG
        _ = wrapped(*args, **kwargs)
        tf_io.rm(f"{check_dir}/_FLAG")  # 执行成功: 删除 _FLAG

        return _

    return wrapper


if __name__ == '__main__':
    class A:

        def __init__(self, ):
            print('A实例化')


    @singleton
    class B:
        def __init__(self, ):
            print('B实例化')


    for _ in range(3):
        print('\n', _)
        A()
        B()
