import os
import re
import time

import psutil as psutil
import pytest
import requests
from process_tests import TestProcess
from process_tests import dump_on_error
from process_tests import wait_for_strings

from redisboard.models import RedisServer

TIMEOUT = int(os.getenv('TEST_TIMEOUT', 10))


@pytest.fixture
def redis_model(redis_server, db):
    server = RedisServer.objects.create(
        url=f'unix:///{redis_server}',
    )
    c = server.connection
    c.set('str', 'bar')
    c.sadd('set', 'bar')
    c.sadd('set', 'foo')
    c.hset('hash', 'key', 'val')
    c.hset('hash', 'foo', 'bar')
    c.lpush('list', 'foo', 'bar', 'foobar')
    c.zadd('sorted-set', {'foo': 1, 'b': 2})
    c.eval(
        """
        local c = 0
        while c < 1000000 do
            redis.call('get', 'str')
            c = c + 1
        end
    """,
        0,
    )
    yield server


@pytest.fixture
def empty_redis_model(redis_server, db):
    return RedisServer.objects.create(
        url=f'unix:///{redis_server}?db=1',
    )


@pytest.mark.django_db
def test_changelist(admin_client, redis_model):
    response = admin_client.get('/redisboard/redisserver/')
    print(response)
    content = response.content.decode('utf-8')
    assert '>UP</' in content
    assert '>redis version</' in content
    assert '<a href="/redisboard/redisserver/{:d}/inspect/">Inspect</a>'.format(redis_model.pk) in content


@pytest.mark.django_db
def test_inspect(admin_client, redis_model):
    response = admin_client.get('/redisboard/redisserver/{:d}/inspect/'.format(redis_model.pk))
    print(response)
    content = response.content.decode('utf-8')
    assert 'Database 0:' in content
    assert '5 keys' in content
    assert '>UP</' in content
    assert '>redis version</' in content

    assert '<a href="/redisboard/redisserver/{:d}/inspect/?key=set&db=0">set</a>'.format(redis_model.pk) in content
    assert '<a href="/redisboard/redisserver/{:d}/inspect/?key=str&db=0">str</a>'.format(redis_model.pk) in content
    assert '<a href="/redisboard/redisserver/{:d}/inspect/?key=hash&db=0">hash</a>'.format(redis_model.pk) in content
    assert '<a href="/redisboard/redisserver/{:d}/inspect/?key=list&db=0">list</a>'.format(redis_model.pk) in content
    assert '<a href="/redisboard/redisserver/{:d}/inspect/?key=sorted-set&db=0">sorted-set</a>'.format(redis_model.pk) in content


@pytest.mark.django_db
def test_inspect_empty(admin_client, empty_redis_model):
    response = admin_client.get('/redisboard/redisserver/{:d}/inspect/'.format(empty_redis_model.pk))
    print(response)
    content = response.content.decode('utf-8')
    assert 'No databases found' in content
    assert '>UP</' in content
    assert '>redis version</' in content


@pytest.mark.django_db
@pytest.mark.parametrize("key", ["set", "str", "hash", "list", "sorted-set"])
def test_key_details(admin_client, redis_model, key):
    response = admin_client.get('/redisboard/redisserver/{:d}/inspect/?key={}'.format(redis_model.pk, key))
    print(response)
    content = response.content.decode('utf-8')
    assert '<h2>Key data: {}</h2>'.format(key) in content


@pytest.mark.parametrize('entrypoint', ['redisboard', 'python -mredisboard'])
def test_cli(entrypoint, tmpdir):
    args = ['127.0.0.1:0', '--password', 'foobar', '--storage', str(tmpdir)]
    with TestProcess(*entrypoint.split() + args) as process:
        with dump_on_error(process.read):
            wait_for_strings(process.read, TIMEOUT, "server at http://")
            t = time.time()
            port = None
            while time.time() - t < TIMEOUT and port is None:
                for conn in psutil.Process(process.proc.pid).connections('all'):
                    print(conn)
                    if conn.status == psutil.CONN_LISTEN and conn.laddr[0] == '127.0.0.1':
                        port = conn.laddr[1]
                        break
            assert port
            with requests.Session() as session:
                resp = session.get('http://127.0.0.1:%s/' % port)
                (csrftoken,) = re.findall('name=[\'"]csrfmiddlewaretoken[\'"] value=[\'"](.*?)[\'"]', resp.text)
                resp = session.post(
                    'http://127.0.0.1:%s/login/?next=/redisboard/redisserver/' % port,
                    data={
                        'csrfmiddlewaretoken': csrftoken,
                        'username': 'redisboard',
                        'password': 'foobar',
                    },
                )
                assert '<a href="/redisboard/redisserver/1/inspect/"' in resp.text
