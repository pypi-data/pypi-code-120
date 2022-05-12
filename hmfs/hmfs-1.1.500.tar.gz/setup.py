from setuptools import setup, find_packages

setup(
    name='hmfs',
    version='1.1.500',
    packages=find_packages(),
    license="MIT",
    description='Distributed filesystem for Hamuna AI',
    long_description='Distributed filesystem for Hamuna AI with multiple third party middleware transfer points',
    long_description_content_type="text/plain",
    author='O.Push',
    author_email='opush.developer@outlook.com',
    url='https://www.hamuna.club',
    package_dir={'': '.'},
    install_requires=['minio', 'redis', 'paho-mqtt', 'gnsq', 'aonsq', 'qiniu', 'boto', 'diskcache',
                      'httpx', 'aiofile', 'aiohttp', 'aiohttp_retry', 'coredis']
)
