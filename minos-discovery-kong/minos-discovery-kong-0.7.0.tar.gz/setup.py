# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['minos', 'minos.plugins.kong']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=2.3.0,<3.0.0',
 'httpx>=0.22.0,<0.23.0',
 'minos-microservice-common>=0.7.0,<0.8.0',
 'minos-microservice-networks>=0.7.0,<0.8.0',
 'pytz>=2022.1,<2023.0']

setup_kwargs = {
    'name': 'minos-discovery-kong',
    'version': '0.7.0',
    'description': 'The minos-kong plugin offer an interface that permit integrate Minos Microservice with Kong API Gateway',
    'long_description': '<p align="center">\n  <a href="https://minos.run" target="_blank"><img src="https://raw.githubusercontent.com/minos-framework/.github/main/images/logo.png" alt="Minos logo"></a>\n</p>\n\n## minos-kong\n\n[![PyPI Latest Release](https://img.shields.io/pypi/v/minos-kong.svg)](https://pypi.org/project/minos-kong/)\n[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/minos-framework/minos-python/pages%20build%20and%20deployment?label=docs)](https://minos-framework.github.io/minos-python)\n[![License](https://img.shields.io/github/license/minos-framework/minos-python.svg)](https://github.com/minos-framework/minos-python/blob/main/LICENSE)\n[![Coverage](https://codecov.io/github/minos-framework/minos-python/coverage.svg?branch=main)](https://codecov.io/gh/minos-framework/minos-python)\n[![Stack Overflow](https://img.shields.io/badge/Stack%20Overflow-Ask%20a%20question-green)](https://stackoverflow.com/questions/tagged/minos)\n\n## Summary\nPre-Alpha release, use at your own risk\nMinos Kong is a plugin that integrate minos micorservices with Kong API Gateway\n\n## Installation\n\nInstall the dependency:\n\n```shell\npip install minos-discovery-kong\n```\n\nModify `config.yml` file:\n\n```yaml\n...\ndiscovery:\n  client: minos.plugins.kong.KongDiscoveryClient\n  host: localhost\n  port: 8001\n...\n```\n\n## How to\nThe above configuration is sufficient for the microservice to subscribe on startup and unsubscribe on shutdown.\nTherefore, all you would have to do would be to make your requests against:\n\n`http://localhost:8000/your_endpoint`\n\n## Kong official documentation\n### Official docs\nYou can get read the official docs [here](https://docs.konghq.com/gateway/2.8.x/admin-api/).\n\n### Postman\n\nYou can get the official postman collection for postman [here](https://documenter.getpostman.com/view/10587735/SzS7QS2c#intro).\n\n## Konga - Administrative interface\nFor development purposes you can add open-source administrative section by using next docker service:\n```yaml\nservices:\n  ...\n  konga:\n      image: pantsel/konga\n      ports:\n          - 1337:1337\n      links:\n          - kong:kong\n      container_name: konga\n      environment:\n          - NODE_ENV=production\n```\n\n## Decorators\nDecorator `@enroute` can support next params:\n - `path` - route url path.\n - `method` - HTTP method.\n - `authenticated` (Optional) - True if route need authentication.\n - `authorized_groups` (Optional) - Groups which can access to specified route (they must exist in Kong).\n - `regex_priority` (Optional) - A number used to choose which route resolves a given request when several routes match it using regexes simultaneously. When two routes match the path and have the same regex_priority, the older one (lowest created_at) is used. Note that the priority for non-regex routes is different (longer non-regex routes are matched before shorter ones). Defaults to 0.\n\nExample:\n```python\n    @enroute.rest.command(f"/users/{{uuid:{UUID_REGEX.pattern}}}/jwt", "POST", authenticated=True, authorized_groups=["admin"], regex_priority=2)\n    @enroute.broker.command("GetUserJWT")\n    async def foo(self, request: Request) -> Response:\n       ...\n```\n## Route path\nIt is important to know that it is best to define routes with a regular expression when it is an id, uuid or similar. This is to avoid collisions with similar routes.\nInstead of using:\n```python\n@enroute.rest.command("/users/{uuid}", "POST")\n```\nUse:\n```python\nimport re\nUUID_REGEX = re.compile(r"\\w{8}-\\w{4}-\\w{4}-\\w{4}-\\w{12}")\n@enroute.rest.command(f"/users/{{uuid:{UUID_REGEX.pattern}}}", "POST")\n```\n\n## Authentication\n\nModify `config.yml` file. Add new middleware and modify discovery section:\n```yaml\n...\nmiddleware:\n  ...\n  - minos.plugins.kong.middleware\n\ndiscovery:\n  connector: minos.networks.DiscoveryConnector\n  client: minos.plugins.kong.KongDiscoveryClient\n  host: localhost\n  auth-type: basic-auth\n  port: 8001\n...\n```\n\nCurrently, there are 2 possible types of authentication:\n- `basic-auth`\n- `jwt`\n\nFor jwt auth type you can specify default token expiration. Example:\n```yaml\n...\nmiddleware:\n  ...\n  - minos.plugins.kong.middleware\n\ndiscovery:\n  connector: minos.networks.DiscoveryConnector\n  client: minos.plugins.kong.KongDiscoveryClient\n  host: localhost\n  auth-type: jwt\n  token-exp: 60 # seconds\n  port: 8001\n...\n```\n\n### JWT Token creation & refresh\nExample on how to create and refresh token. You need to store in database or similar the secret and key returned form kong in order to refresh existing token.\n```python\nfrom minos.common import (\n    UUID_REGEX,\n    NotProvidedException,\n    Config,\n    Inject,\n)\nfrom minos.cqrs import (\n    CommandService,\n)\nfrom minos.networks import (\n    Request,\n    Response,\n    enroute,\n)\n\nfrom ..aggregates import (\n    User,\n)\nfrom minos.plugins.kong import KongClient\n\nclass UserCommandService(CommandService):\n    """UserCommandService class."""\n\n    def __init__(self, *args, **kwargs):\n        super().__init__(*args, **kwargs)\n        self.kong = self._get_kong_client()\n\n    @staticmethod\n    @Inject()\n    def _get_kong_client(config: Config) -> KongClient:\n        """Get the service name."""\n        if config is None:\n            raise NotProvidedException("The config object must be provided.")\n        return KongClient.from_config(config)\n\n    @enroute.rest.command(f"/users/{{uuid:{UUID_REGEX.pattern}}}/jwt", "POST", authenticated=True,\n                          authorized_groups=["admin"], regex_priority=3)\n    @enroute.broker.command("GetUserJWT")\n    async def create_user_jwt(self, request: Request) -> Response:\n        params = await request.params()\n        uuid = params["uuid"]\n        user = await User.get(uuid)\n\n        if user.uuid == request.user:\n            token = await self.add_jwt_to_consumer(request.headers.get("X-Consumer-ID"))\n            return Response({"token": token})\n        else:\n            return Response(status=404)\n\n    async def add_jwt_to_consumer(self, consumer: str):\n        resp = await self.kong.add_jwt_to_consumer(consumer=consumer)\n        res = resp.json()\n        self.key = res[\'key\']\n        self.secret = res[\'secret\']\n        token = await self.kong.generate_jwt_token(key=self.key, secret=self.secret)\n        return token\n\n    @enroute.rest.command(f"/users/{{uuid:{UUID_REGEX.pattern}}}/refresh-jwt", "POST", authenticated=True,\n                          authorized_groups=["admin"], regex_priority=3)\n    @enroute.broker.command("RefreshJWT")\n    async def refresh_jwt(self, request: Request) -> Response:\n        token = await self.kong.generate_jwt_token(key=self.key, secret=self.secret)\n        return Response({"token": token})\n```\n\nFor the route to be authenticated with the method specified above, a parameter called `authenticated` must be passed:\n```python\nclass CategoryCommandService(CommandService):\n    @enroute.rest.command("/categories", "POST", authenticated=True, authorized_groups=["super_admin", "admin"])\n    @enroute.broker.command("CreateCategory")\n    async def create_category(self, request: Request) -> Response:\n        try:\n            content = await request.content()\n            category = await Category.create(**content)\n            return Response(category)\n        except Exception:\n            raise ResponseException("An error occurred during category creation.")\n```\n\nIf `authorized_groups` is also specified, this means that ACL will be enabled for that path and only users in the specified group will be allowed access.\n\nExample of how to create a user and add them to a group:\n\n```python\nfrom minos.common import (\n    NotProvidedException,\n    Config,\n    Inject,\n)\nfrom minos.cqrs import (\n    CommandService,\n)\nfrom minos.networks import (\n    Request,\n    Response,\n    enroute,\n)\nfrom ..aggregates import (\n    Role,\n    User,\n)\nfrom minos.plugins.kong import KongClient\n\n\nclass UserCommandService(CommandService):\n    """UserCommandService class."""\n\n\n    @enroute.rest.command("/users", "POST")\n    @enroute.broker.command("CreateUser")\n    async def create_user(self, request: Request) -> Response:\n        """Create a new ``User`` instance.\n\n        :param request: The ``Request`` instance.\n        :return: A ``Response`` instance.\n        """\n        content = await request.content()\n\n        active = True\n        if "active" in content:\n            active = content["active"]\n\n        user = User(\n            name=content["name"],\n            surname=content["surname"],\n            email=content["email"],\n            telephone=content["telephone"],\n            role=content["role"],\n            active=active,\n        )\n        await user.save()\n\n        kong = KongClient(self._get_kong_url())\n\n        consumer_raw = await kong.create_consumer(username=f"{user.name} {user.surname}", user=user.uuid, tags=[])\n        consumer = consumer_raw.json()\n\n        basic_auth = await kong.add_basic_auth_to_consumer(username=f"{user.name.lower()}_{user.surname.lower()}",\n                                                      password=content["password"], consumer=consumer["id"])\n\n        acl = await kong.add_acl_to_consumer(role=user.role.name.lower(), consumer=consumer["id"])\n\n        return Response(user)\n\n    @staticmethod\n    @Inject()\n    def _get_kong_url(config: Config) -> str:\n        """Get the service name."""\n        if config is None:\n            raise NotProvidedException("The config object must be provided.")\n        return f"http://{config.get_by_key(\'discovery.host\')}:{config.get_by_key(\'discovery.port\')}"\n```\n\nGenerate JWT example:\n```python\nfrom minos.common import (\n    UUID_REGEX,\n    NotProvidedException,\n    Config,\n    Inject,\n)\nfrom minos.cqrs import (\n    CommandService,\n)\nfrom minos.networks import (\n    Request,\n    Response,\n    enroute,\n)\nfrom ..aggregates import (\n    Role,\n    User,\n)\nfrom minos.plugins.kong import KongClient\n\nclass UserCommandService(CommandService):\n    """UserCommandService class."""\n\n    @enroute.rest.command(f"/users/{{uuid:{UUID_REGEX.pattern}}}/jwt", "POST", authenticated=True, authorized_groups=["admin"])\n    @enroute.broker.command("GetUserJWT")\n    async def create_user_jwt(self, request: Request) -> Response:\n        params = await request.params()\n        uuid = params["uuid"]\n        user = await User.get(uuid)\n\n        if user.uuid == request.user:\n            kong = KongClient(self._get_kong_url())\n            jwt = await kong.add_jwt_to_consumer(request.headers.get("X-Consumer-ID"))\n            return Response(jwt.json())\n        else:\n            return Response(status=404)\n\n    @staticmethod\n    @Inject()\n    def _get_kong_url(config: Config) -> str:\n        """Get the service name."""\n        if config is None:\n            raise NotProvidedException("The config object must be provided.")\n        return f"http://{config.get_by_key(\'discovery.host\')}:{config.get_by_key(\'discovery.port\')}"\n```\n\nYou can get read the official docs [here](https://pantsel.github.io/konga/).\n\n\n## Documentation\n\nThe official API Reference is publicly available at the [GitHub Pages](https://minos-framework.github.io/minos-python).\n\n## Source Code\n\nThe source code of this project is hosted at the [GitHub Repository](https://github.com/minos-framework/minos-python).\n\n## Getting Help\n\nFor usage questions, the best place to go to is [StackOverflow](https://stackoverflow.com/questions/tagged/minos).\n\n## Discussion and Development\n\nMost development discussions take place over the [GitHub Issues](https://github.com/minos-framework/minos-python/issues). In addition, a [Gitter channel](https://gitter.im/minos-framework/community) is available for development-related questions.\n\n## License\n\nThis project is distributed under the [MIT](https://raw.githubusercontent.com/minos-framework/minos-python/main/LICENSE) license.\n',
    'author': 'Minos Framework Devs',
    'author_email': 'hey@minos.run',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://www.minos.run/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
