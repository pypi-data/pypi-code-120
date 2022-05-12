'''
<p align="center">
  <a href="https://projen.io">
    <img src="https://raw.githubusercontent.com/projen/projen/main/logo/projen.svg">
    <h3 align="center">projen</h3>
  </a>
</p><p align="center">
  Define and maintain complex project configuration through code.
</p><p align="center">
  <a href="https://projen.io/"><strong>Documentation</strong></a> ·
  <a href="https://github.com/projen/projen/releases"><strong>Changelog</strong></a> ·
  <a href="#project-types"><strong>Project types</strong></a> ·
  <a href="#community"><strong>Join the community</strong></a>
</p><p align="center">
  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg" alt="Apache 2.0 License"></a>
  <a href="https://gitpod.io/#https://github.com/projen/projen"><img src="https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod" alt="Gitpod ready-to-code"></a>
  <a href="https://github.com/projen/projen/actions/workflows/build.yml"><img src="https://github.com/projen/projen/workflows/Build/badge.svg" alt="Build badge"></a>
  <a href="https://github.com/projen/projen/actions/workflows/release.yml"><img src="https://github.com/projen/projen/workflows/Release/badge.svg" alt="Release badge"></a>
  <a href="https://github.com/projen/projen/commits/main"><img src="https://img.shields.io/github/commit-activity/w/projen/projen" alt="Commit activity"></a>
</p><br/>

*projen* synthesizes project configuration files such as `package.json`,
`tsconfig.json`, `.gitignore`, GitHub Workflows, eslint, jest, etc from a
well-typed definition written in JavaScript.

As opposed to existing templating/scaffolding tools, *projen* is not a one-off
generator. Synthesized files should never be manually edited (in fact, projen
enforces that). To modify your project setup, users interact with rich
strongly-typed class and execute `projen` to update their project configuration
files.

By defining a custom project type and using projen in multiple repositories, it's
possible to update configuration files and CI/CD workflows across dozens (or
hundreds!?) of projects.

Check out [this talk](https://youtu.be/SOWMPzXtTCw) about projen from its creator.

## Getting Started

To create a new project, run the following command and follow the instructions:

```console
$ mkdir my-project
$ cd my-project
$ git init
$ npx projen new PROJECT-TYPE
🤖 Synthesizing project...
...
```

### Project types

Currently supported project types (use `npx projen new` without a type for a
full list):

**Built-in:** (run `npx projen <type>`)

<!-- <macro exec="node ./scripts/readme-projects.js"> -->

* [awscdk-app-java](https://projen.io/api/API.html#projen-awscdk-awscdkjavaapp) - AWS CDK app in Java.
* [awscdk-app-py](https://projen.io/api/API.html#projen-awscdk-awscdkpythonapp) - AWS CDK app in Python.
* [awscdk-app-ts](https://projen.io/api/API.html#projen-awscdk-awscdktypescriptapp) - AWS CDK app in TypeScript.
* [awscdk-construct](https://projen.io/api/API.html#projen-awscdk-awscdkconstructlibrary) - AWS CDK construct library project.
* [cdk8s-app-ts](https://projen.io/api/API.html#projen-cdk8s-cdk8stypescriptapp) - CDK8s app in TypeScript.
* [cdk8s-construct](https://projen.io/api/API.html#projen-cdk8s-constructlibrarycdk8s) - CDK8s construct library project.
* [cdktf-construct](https://projen.io/api/API.html#projen-cdktf-constructlibrarycdktf) - CDKTF construct library project.
* [java](https://projen.io/api/API.html#projen-java-javaproject) - Java project.
* [jsii](https://projen.io/api/API.html#projen-cdk-jsiiproject) - Multi-language jsii library project.
* [nextjs](https://projen.io/api/API.html#projen-web-nextjsproject) - Next.js project without TypeScript.
* [nextjs-ts](https://projen.io/api/API.html#projen-web-nextjstypescriptproject) - Next.js project with TypeScript.
* [node](https://projen.io/api/API.html#projen-javascript-nodeproject) - Node.js project.
* [project](https://projen.io/api/API.html#projen-project) - Base project.
* [python](https://projen.io/api/API.html#projen-python-pythonproject) - Python project.
* [react](https://projen.io/api/API.html#projen-web-reactproject) - React project without TypeScript.
* [react-ts](https://projen.io/api/API.html#projen-web-reacttypescriptproject) - React project with TypeScript.
* [typescript](https://projen.io/api/API.html#projen-typescript-typescriptproject) - TypeScript project.
* [typescript-app](https://projen.io/api/API.html#projen-typescript-typescriptappproject) - TypeScript app.

<!-- </macro> -->

**External:** (run `npx projen --from <type>`)

* [projen-github-action-typescript](https://github.com/projen/projen-github-action-typescript/blob/main/API.md) - GitHub Action in TypeScript project.

> Use `npx projen new PROJECT-TYPE --help` to view a list of command line
> switches that allows you to specify most project options during bootstrapping.
> For example: `npx projen new jsii --author-name "Jerry Berry"`.

The `new` command will create a `.projenrc.js` file which looks like this for
`jsii` projects:

```js
const { JsiiProject } = require('projen');

const project = new JsiiProject({
  authorAddress: "elad.benisrael@gmail.com",
  authorName: "Elad Ben-Israel",
  name: "foobar",
  repository: "https://github.com/eladn/foobar.git",
});

project.synth();
```

This program instantiates the project type with minimal setup, and then calls
`synth()` to synthesize the project files. By default, the `new` command will
also execute this program, which will result in a fully working project.

Once your project is created, you can configure your project by editing
`.projenrc.js` and re-running `npx projen` to synthesize again.

> The files generated by *projen* are considered an "implementation detail" and
> *projen* protects them from being manually edited (most files are marked
> read-only, and an "anti tamper" check is configured in the CI build workflow
> to ensure that files are not updated during build).

For example, to setup PyPI publishing in `jsii` projects, you can use
[`python option`](https://github.com/eladb/projen/blob/master/API.md#projen-jsiipythontarget):

```js
const project = new JsiiProject({
  // ...
  python: {
    distName: "mydist",
    module: "my_module",
  }
});
```

Run:

```shell
npx projen
```

And you'll notice that your `package.json` file now contains a `python` section in
its `jsii` config and the GitHub `release.yml` workflow includes a PyPI
publishing step.

We recommend to put this in your shell profile, so you can simply run `pj` every
time you update `.projenrc.js`:

```bash
alias pj='npx projen'
```

Most projects come with an assortment of **tasks** that handle various
development activities, from compiling to publishing. Tasks can be and composed
together, and can be run as local commands or turned into GitHub workflows. You
can list all tasks with `npx projen --help`:

```shell
$ npx projen --help
projen [command]

Commands:
  projen new [PROJECT-TYPE-NAME] [OPTIONS]  Creates a new projen project
  projen clobber                            hard resets to HEAD of origin and cleans the local repo
  projen compile                            Only compile
  projen test:compile                       compiles the test code
  projen test                               Run tests
  projen build                              Full release build (test+compile)
  projen upgrade-dependencies               upgrade dependencies
  projen upgrade-projen                     upgrade projen
...
```

The `build` task is the same task that's executed in your CI builds. It
typically compiles, lints, tests and packages your module for distribution.

### Shell Completions

If installed as a global package, `projen` includes rich shell tab-completion support. To enable this in your shell, run:

```shell
# Bash
projen completion >> ~/.bashrc

# ZSH
projen completion >> ~/.zshrc
```

## Features

Some examples for features built-in to project types:

* Fully synthesize `package.json`
* Standard npm scripts like `compile`, `build`, `test`, `package`
* eslint
* Jest
* jsii: compile, package, api compatibility checks, API.md
* Bump & release scripts with CHANGELOG generation based on conventional commits
* Automated PR builds
* Automated releases to npm, maven, NuGet and PyPI
* Automated dependency upgrades
* Mergify configuration
* LICENSE file generation
* gitignore + npmignore management
* Node "engines" support with coupling to CI build environment and @types/node
* Anti-tamper: CI builds will fail if a synthesized file is modified manually

## Documentation

For documentation including examples and a full API reference, visit [https://projen.io/](https://projen.io/).

## Ecosystem

*projen* takes a "batteries included" approach and aims to offer dozens of different project types out of
the box (we are just getting started). Think `projen new react`, `projen new angular`, `projen new java-maven`,
`projen new awscdk-typescript`, `projen new cdk8s-python` (nothing in projen is tied to javascript or npm!)...

Adding new project types is as simple as submitting a pull request to this repo and exporting a class that
extends `projen.Project` (or one of its derivatives). Projen automatically discovers project types so your
type will immediately be available in `projen new`.

### Projects in external modules

*projen* is bundled with many project types out of the box, but it can also work
with project types and components defined in external jsii modules (the reason
we need jsii is because projen uses the jsii metadata to discover project types
& options in projen new).

Say we have a module in npm called `projen-vuejs` which includes a single project
type for vue.js:

```bash
$ npx projen new --from projen-vuejs
```

If the referenced module includes multiple project types, the type is required.
Switches can also be used to specify initial values based on the project type
APIs. You can also use any package syntax supported by [yarn
add](https://classic.yarnpkg.com/en/docs/cli/add#toc-adding-dependencies) like
`projen-vuejs@1.2.3`, `file:/path/to/local/folder`,
`git@github.com/awesome/projen-vuejs#1.2.3`, etc.

```bash
$ npx projen new --from projen-vuejs@^2 vuejs-ts --description "my awesome vue project"
```

Under the hood, `projen new` will install the `projen-vuejs` module from npm
(version 2.0.0 and above), discover the project types in it and bootstrap the
`vuejs-ts` project type. It will assign the value `"my awesome vue project"` to
the `description` field. If you examine your `.projenrc.js` file, you'll see
that `projen-vuejs` is defined as a dev dependency:

```javascript
const { VueJsProject } = require('projen-vuejs');

const project = new VueJsProject({
  name: 'my-vuejs-sample',
  description: "my awesome vue project",
  // ...
  devDeps: [
    'projen-vuejs'
  ]
});

project.synth();
```

## Roadmap

See [Vision](./VISION.md).

## FAQ

### Do I have to write my configuration in JavaScript?

Not at all! JavaScript is the default, but it's also possible to write it in
Java, TypeScript, or even JSON. Python support is also planned. This is made
possible by the [jsii](https://github.com/aws/jsii) library which allows us
to write APIs once and generate libraries in several languages. You can choose
a different language by passing the `--projenrc-ts`, `--projenrc-java`, or
`--projenrc-json` flags when running `projen new`.

Note: using a `.projenrc.json` file to specify configuration only allows
accessing a subset of the entire API - the options which are passed to the
constructor of each project type.

### How does projen work with my IDE?

projen has an unofficial [VS Code extension](https://marketplace.visualstudio.com/items?itemName=MarkMcCulloh.vscode-projen). Check it out!

## Community

The projen community can be found within the #projen channel in the [cdk.dev](https://cdk.dev/)
community Slack workspace.

### Virtual Meetup

* Thursday June 30, 2022
* 1-2pm America/New_York (EDT)
* [CFP](https://bit.ly/3NEc0UQ) a Google Form
* CFP Closes Saturday April 30, 2022
* Hosted on [Zoom](https://zoom.us/j/92399854777?pwd=OUZybHlobHNoZUs1VVordWhaRTVGdz09#success)

## Contributions

Contributions of all kinds are welcome! Check out our [contributor's
guide](./CONTRIBUTING.md) and our [code of conduct](./CODE_OF_CONDUCT.md).

For a quick start, check out a development environment:

```bash
$ git clone git@github.com:projen/projen
$ cd projen
$ yarn
$ yarn watch # compile in the background
```

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-67-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END --><!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section --><!-- prettier-ignore-start --><!-- markdownlint-disable --><table>
  <tr>
    <td align="center"><a href="http://eladb.github.com/"><img src="https://avatars3.githubusercontent.com/u/598796?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Elad Ben-Israel</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=eladb" title="Code">💻</a></td>
    <td align="center"><a href="https://rybicki.io/"><img src="https://avatars2.githubusercontent.com/u/5008987?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Christopher Rybicki</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=Chriscbr" title="Code">💻</a></td>
    <td align="center"><a href="http://p6m7g8.github.io/"><img src="https://avatars0.githubusercontent.com/u/34295?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Philip M. Gollucci</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=pgollucci" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/hoegertn"><img src="https://avatars2.githubusercontent.com/u/1287829?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Thorsten Hoeger</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=hoegertn" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/kcwinner"><img src="https://avatars3.githubusercontent.com/u/2728868?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Kenneth Winner</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=kcwinner" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/JordanSinko"><img src="https://avatars2.githubusercontent.com/u/10212966?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jordan Sinko</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=JordanSinko" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/misterjoshua"><img src="https://avatars2.githubusercontent.com/u/644092?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Josh Kellendonk</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=misterjoshua" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/andrestone"><img src="https://avatars1.githubusercontent.com/u/7958086?v=4?s=100" width="100px;" alt=""/><br /><sub><b>andrestone</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=andrestone" title="Code">💻</a></td>
    <td align="center"><a href="https://pallares.io/"><img src="https://avatars3.githubusercontent.com/u/1077520?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Cristian Pallarés</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=skyrpex" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/jogold"><img src="https://avatars2.githubusercontent.com/u/12623249?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jonathan Goldwasser</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=jogold" title="Code">💻</a></td>
    <td align="center"><a href="http://www.matthewbonig.com/"><img src="https://avatars2.githubusercontent.com/u/1559437?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Matthew Bonig</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=mbonig" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/pahud"><img src="https://avatars3.githubusercontent.com/u/278432?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Pahud Hsieh</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=pahud" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/adamelmore"><img src="https://avatars2.githubusercontent.com/u/2363879?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Adam Elmore</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=adamelmore" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/abelmokadem"><img src="https://avatars0.githubusercontent.com/u/9717944?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ash</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=abelmokadem" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/jmourelos"><img src="https://avatars3.githubusercontent.com/u/3878434?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jacob</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=jmourelos" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/bigkraig"><img src="https://avatars1.githubusercontent.com/u/508403?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Kraig Amador</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=bigkraig" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/mmuller88"><img src="https://avatars0.githubusercontent.com/u/18393842?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Martin Muller</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=mmuller88" title="Code">💻</a></td>
    <td align="center"><a href="https://tlakomy.com/"><img src="https://avatars2.githubusercontent.com/u/16646517?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tomasz Łakomy</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=tlakomy" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/john-tipper"><img src="https://avatars2.githubusercontent.com/u/9730398?v=4?s=100" width="100px;" alt=""/><br /><sub><b>john-tipper</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=john-tipper" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/henrysachs"><img src="https://avatars0.githubusercontent.com/u/17173951?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Henry Sachs</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=henrysachs" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/eganjs"><img src="https://avatars3.githubusercontent.com/u/6639482?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Joseph Egan</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=eganjs" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://skorfmann.com/"><img src="https://avatars1.githubusercontent.com/u/136789?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sebastian Korfmann</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=skorfmann" title="Code">💻</a></td>
    <td align="center"><a href="http://www.callant.net/"><img src="https://avatars1.githubusercontent.com/u/5915843?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Bart Callant</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=bartcallant" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/campionfellin"><img src="https://avatars3.githubusercontent.com/u/11984923?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Campion Fellin</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=campionfellin" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/gradybarrett"><img src="https://avatars1.githubusercontent.com/u/1140074?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Grady Barrett</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=gradybarrett" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/HassanMahmud"><img src="https://avatars3.githubusercontent.com/u/58504381?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Hassan Mahmud</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=HassanMahmud" title="Code">💻</a></td>
    <td align="center"><a href="https://dk.linkedin.com/in/hassanmahmud93"><img src="https://avatars1.githubusercontent.com/u/7426703?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Hassan Mahmud</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=hass123uk" title="Code">💻</a></td>
    <td align="center"><a href="http://joapy.com/"><img src="https://avatars3.githubusercontent.com/u/325306?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jake Pearson</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=jakepearson" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/JeremyJonas"><img src="https://avatars1.githubusercontent.com/u/464119?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jeremy Jonas</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=JeremyJonas" title="Code">💻</a></td>
    <td align="center"><a href="https://dev.to/martzcodes"><img src="https://avatars1.githubusercontent.com/u/978362?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Matt Martz</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=martzcodes" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/fongie"><img src="https://avatars1.githubusercontent.com/u/19932622?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Max Körlinge</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=fongie" title="Code">💻</a></td>
    <td align="center"><a href="https://blog.neilkuan.dev/"><img src="https://avatars2.githubusercontent.com/u/46012524?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Neil Kuan</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=guan840912" title="Code">💻</a></td>
    <td align="center"><a href="https://dynobase.dev/"><img src="https://avatars3.githubusercontent.com/u/3391616?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Rafal Wilinski</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=RafalWilinski" title="Code">💻</a></td>
    <td align="center"><a href="https://keybase.io/romainmuller"><img src="https://avatars2.githubusercontent.com/u/411689?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Romain Marcadier</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=RomainMuller" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/thomasklinger1234"><img src="https://avatars1.githubusercontent.com/u/39558817?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Thomas Klinger</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=thomasklinger1234" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/gwriss"><img src="https://avatars2.githubusercontent.com/u/1842089?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tobias</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=gwriss" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/flyingImer"><img src="https://avatars0.githubusercontent.com/u/1973868?v=4?s=100" width="100px;" alt=""/><br /><sub><b>flyingImer</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=flyingImer" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Hunter-Thompson"><img src="https://avatars.githubusercontent.com/u/20844961?v=4?s=100" width="100px;" alt=""/><br /><sub><b> Aatman </b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=Hunter-Thompson" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/mmcculloh-dms"><img src="https://avatars.githubusercontent.com/u/68597641?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mark McCulloh</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=mmcculloh-dms" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/aisamu"><img src="https://avatars.githubusercontent.com/u/431708?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Samuel Tschiedel</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=aisamu" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/iliapolo"><img src="https://avatars.githubusercontent.com/u/1428812?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Eli Polonsky</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=iliapolo" title="Code">💻</a></td>
    <td align="center"><a href="https://unsubstantiated.blog/"><img src="https://avatars.githubusercontent.com/u/1308885?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alexander Steppke</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=Miradorn" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/kanatti"><img src="https://avatars.githubusercontent.com/u/8623654?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Balagopal Kanattil</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=kanatti" title="Code">💻</a></td>
    <td align="center"><a href="http://twitter.com/bracki"><img src="https://avatars.githubusercontent.com/u/49786?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jan Brauer</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=bracki" title="Code">💻</a></td>
    <td align="center"><a href="https://polothy.github.io/"><img src="https://avatars.githubusercontent.com/u/634657?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mark Nielsen</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=polothy" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/MrArnoldPalmer"><img src="https://avatars.githubusercontent.com/u/7221111?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mitchell Valine</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=MrArnoldPalmer" title="Code">💻</a></td>
    <td align="center"><a href="https://blog.neilkuan.net/"><img src="https://avatars.githubusercontent.com/u/46012524?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Neil Kuan</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=neilkuan" title="Code">💻</a></td>
    <td align="center"><a href="https://garbe.io/"><img src="https://avatars.githubusercontent.com/u/721899?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Philipp Garbe</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=pgarbe" title="Code">💻</a></td>
    <td align="center"><a href="https://selfstructured.com/"><img src="https://avatars.githubusercontent.com/u/361689?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Shawn MacIntyre</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=smacintyre" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/tobias-bardino"><img src="https://avatars.githubusercontent.com/u/1842089?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tobias</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=tobias-bardino" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/yglcode"><img src="https://avatars.githubusercontent.com/u/11893614?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Yigong Liu</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=yglcode" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/eduardomourar"><img src="https://avatars.githubusercontent.com/u/16357187?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Eduardo Rodrigues</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=eduardomourar" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/hassanazharkhan"><img src="https://avatars.githubusercontent.com/u/57677979?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Hassan Azhar</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=hassanazharkhan" title="Code">💻</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/julian-michel-812a223a/"><img src="https://avatars.githubusercontent.com/u/15660169?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Julian Michel</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=jumic" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/lmarsden"><img src="https://avatars.githubusercontent.com/u/51232932?v=4?s=100" width="100px;" alt=""/><br /><sub><b>lmarsden</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=lmarsden" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/adrianmace"><img src="https://avatars.githubusercontent.com/u/5071859?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Adrian Mace</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=adrianmace" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/mKeRix"><img src="https://avatars.githubusercontent.com/u/770596?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Heiko Rothe</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=mKeRix" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/hyandell"><img src="https://avatars.githubusercontent.com/u/477715?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Henri Yandell</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=hyandell" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/mwg-rea"><img src="https://avatars.githubusercontent.com/u/82480228?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Matthew Gamble</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=mwg-rea" title="Code">💻</a></td>
    <td align="center"><a href="https://willdady.com/"><img src="https://avatars.githubusercontent.com/u/204259?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Will Dady</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=willdady" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/msessa"><img src="https://avatars.githubusercontent.com/u/1912143?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Matteo Sessa</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=msessa" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Hi-Fi"><img src="https://avatars.githubusercontent.com/u/1499780?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Juho Saarinen</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=Hi-Fi" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/njlynch"><img src="https://avatars.githubusercontent.com/u/1376292?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nick Lynch</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=njlynch" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://amani.kilumanga.com/"><img src="https://avatars.githubusercontent.com/u/8690282?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Amani Kilumanga</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=dkaksl" title="Code">💻</a></td>
    <td align="center"><a href="http://blog.herlein.com/"><img src="https://avatars.githubusercontent.com/u/173428?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Greg Herlein</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=gherlein" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/kaizen3031593"><img src="https://avatars.githubusercontent.com/u/36202692?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Kaizen Conroy</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=kaizen3031593" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/saudkhanzada"><img src="https://avatars.githubusercontent.com/u/30137907?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Saud Khanzada</b></sub></a><br /><a href="https://github.com/projen/projen/commits?author=saudkhanzada" title="Code">💻</a></td>
  </tr>
</table><!-- markdownlint-restore --><!-- prettier-ignore-end --><!-- ALL-CONTRIBUTORS-LIST:END -->

## License

Distributed under the [Apache-2.0](./LICENSE) license.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *


class Component(metaclass=jsii.JSIIMeta, jsii_type="projen.Component"):
    '''(experimental) Represents a project component.

    :stability: experimental
    '''

    def __init__(self, project: "Project") -> None:
        '''
        :param project: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [project])

    @jsii.member(jsii_name="postSynthesize")
    def post_synthesize(self) -> None:
        '''(experimental) Called after synthesis.

        Order is *not* guaranteed.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "postSynthesize", []))

    @jsii.member(jsii_name="preSynthesize")
    def pre_synthesize(self) -> None:
        '''(experimental) Called before synthesis.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "preSynthesize", []))

    @jsii.member(jsii_name="synthesize")
    def synthesize(self) -> None:
        '''(experimental) Synthesizes files to the project output directory.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "synthesize", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="project")
    def project(self) -> "Project":
        '''
        :stability: experimental
        '''
        return typing.cast("Project", jsii.get(self, "project"))


@jsii.data_type(
    jsii_type="projen.CreateProjectOptions",
    jsii_struct_bases=[],
    name_mapping={
        "dir": "dir",
        "project_fqn": "projectFqn",
        "project_options": "projectOptions",
        "option_hints": "optionHints",
        "post": "post",
        "synth": "synth",
    },
)
class CreateProjectOptions:
    def __init__(
        self,
        *,
        dir: builtins.str,
        project_fqn: builtins.str,
        project_options: typing.Mapping[builtins.str, typing.Any],
        option_hints: typing.Optional["InitProjectOptionHints"] = None,
        post: typing.Optional[builtins.bool] = None,
        synth: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param dir: (experimental) Directory that the project will be generated in.
        :param project_fqn: (experimental) Fully-qualified name of the project type (usually formatted as ``module.ProjectType``).
        :param project_options: (experimental) Project options. Only JSON-like values can be passed in (strings, booleans, numbers, enums, arrays, and objects that are not derived from classes). Consult the API reference of the project type you are generating for information about what fields and types are available.
        :param option_hints: (experimental) Should we render commented-out default options in the projenrc file? Does not apply to projenrc.json files. Default: InitProjectOptionHints.FEATURED
        :param post: (experimental) Should we execute post synthesis hooks? (usually package manager install). Default: true
        :param synth: (experimental) Should we call ``project.synth()`` or instantiate the project (could still have side-effects) and render the .projenrc file. Default: true

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "dir": dir,
            "project_fqn": project_fqn,
            "project_options": project_options,
        }
        if option_hints is not None:
            self._values["option_hints"] = option_hints
        if post is not None:
            self._values["post"] = post
        if synth is not None:
            self._values["synth"] = synth

    @builtins.property
    def dir(self) -> builtins.str:
        '''(experimental) Directory that the project will be generated in.

        :stability: experimental
        '''
        result = self._values.get("dir")
        assert result is not None, "Required property 'dir' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_fqn(self) -> builtins.str:
        '''(experimental) Fully-qualified name of the project type (usually formatted as ``module.ProjectType``).

        :stability: experimental

        Example::

            `projen.TypescriptProject`
        '''
        result = self._values.get("project_fqn")
        assert result is not None, "Required property 'project_fqn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_options(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''(experimental) Project options.

        Only JSON-like values can be passed in (strings,
        booleans, numbers, enums, arrays, and objects that are not
        derived from classes).

        Consult the API reference of the project type you are generating for
        information about what fields and types are available.

        :stability: experimental
        '''
        result = self._values.get("project_options")
        assert result is not None, "Required property 'project_options' is missing"
        return typing.cast(typing.Mapping[builtins.str, typing.Any], result)

    @builtins.property
    def option_hints(self) -> typing.Optional["InitProjectOptionHints"]:
        '''(experimental) Should we render commented-out default options in the projenrc file?

        Does not apply to projenrc.json files.

        :default: InitProjectOptionHints.FEATURED

        :stability: experimental
        '''
        result = self._values.get("option_hints")
        return typing.cast(typing.Optional["InitProjectOptionHints"], result)

    @builtins.property
    def post(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Should we execute post synthesis hooks?

        (usually package manager install).

        :default: true

        :stability: experimental
        '''
        result = self._values.get("post")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def synth(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Should we call ``project.synth()`` or instantiate the project (could still have side-effects) and render the .projenrc file.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("synth")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateProjectOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Dependencies(Component, metaclass=jsii.JSIIMeta, jsii_type="projen.Dependencies"):
    '''(experimental) The ``Dependencies`` component is responsible to track the list of dependencies a project has, and then used by project types as the model for rendering project-specific dependency manifests such as the dependencies section ``package.json`` files.

    To add a dependency you can use a project-type specific API such as
    ``nodeProject.addDeps()`` or use the generic API of ``project.deps``:

    :stability: experimental
    '''

    def __init__(self, project: "Project") -> None:
        '''(experimental) Adds a dependencies component to the project.

        :param project: The parent project.

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [project])

    @jsii.member(jsii_name="parseDependency") # type: ignore[misc]
    @builtins.classmethod
    def parse_dependency(cls, spec: builtins.str) -> "DependencyCoordinates":
        '''(experimental) Returns the coordinates of a dependency spec.

        Given ``foo@^3.4.0`` returns ``{ name: "foo", version: "^3.4.0" }``.
        Given ``bar@npm:@bar/legacy`` returns ``{ name: "bar", version: "npm:@bar/legacy" }``.

        :param spec: -

        :stability: experimental
        '''
        return typing.cast("DependencyCoordinates", jsii.sinvoke(cls, "parseDependency", [spec]))

    @jsii.member(jsii_name="addDependency")
    def add_dependency(
        self,
        spec: builtins.str,
        type: "DependencyType",
        metadata: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> "Dependency":
        '''(experimental) Adds a dependency to this project.

        :param spec: The dependency spec in the format ``MODULE[@VERSION]`` where ``MODULE`` is the package-manager-specific module name and ``VERSION`` is an optional semantic version requirement (e.g. ``^3.4.0``).
        :param type: The type of the dependency.
        :param metadata: -

        :stability: experimental
        '''
        return typing.cast("Dependency", jsii.invoke(self, "addDependency", [spec, type, metadata]))

    @jsii.member(jsii_name="getDependency")
    def get_dependency(
        self,
        name: builtins.str,
        type: typing.Optional["DependencyType"] = None,
    ) -> "Dependency":
        '''(experimental) Returns a dependency by name.

        Fails if there is no dependency defined by that name or if ``type`` is not
        provided and there is more then one dependency type for this dependency.

        :param name: The name of the dependency.
        :param type: The dependency type. If this dependency is defined only for a single type, this argument can be omitted.

        :return: a copy (cannot be modified)

        :stability: experimental
        '''
        return typing.cast("Dependency", jsii.invoke(self, "getDependency", [name, type]))

    @jsii.member(jsii_name="removeDependency")
    def remove_dependency(
        self,
        name: builtins.str,
        type: typing.Optional["DependencyType"] = None,
    ) -> None:
        '''(experimental) Removes a dependency.

        :param name: The name of the module to remove (without the version).
        :param type: The dependency type. This is only required if there the dependency is defined for multiple types.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "removeDependency", [name, type]))

    @jsii.member(jsii_name="tryGetDependency")
    def try_get_dependency(
        self,
        name: builtins.str,
        type: typing.Optional["DependencyType"] = None,
    ) -> typing.Optional["Dependency"]:
        '''(experimental) Returns a dependency by name.

        Returns ``undefined`` if there is no dependency defined by that name or if
        ``type`` is not provided and there is more then one dependency type for this
        dependency.

        :param name: The name of the dependency.
        :param type: The dependency type. If this dependency is defined only for a single type, this argument can be omitted.

        :return: a copy (cannot be modified) or undefined if there is no match

        :stability: experimental
        '''
        return typing.cast(typing.Optional["Dependency"], jsii.invoke(self, "tryGetDependency", [name, type]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="MANIFEST_FILE")
    def MANIFEST_FILE(cls) -> builtins.str:
        '''(experimental) The project-relative path of the deps manifest file.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "MANIFEST_FILE"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="all")
    def all(self) -> typing.List["Dependency"]:
        '''(experimental) A copy of all dependencies recorded for this project.

        The list is sorted by type->name->version

        :stability: experimental
        '''
        return typing.cast(typing.List["Dependency"], jsii.get(self, "all"))


@jsii.data_type(
    jsii_type="projen.DependencyCoordinates",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "version": "version"},
)
class DependencyCoordinates:
    def __init__(
        self,
        *,
        name: builtins.str,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Coordinates of the dependency (name and version).

        :param name: (experimental) The package manager name of the dependency (e.g. ``leftpad`` for npm). NOTE: For package managers that use complex coordinates (like Maven), we will codify it into a string somehow.
        :param version: (experimental) Semantic version version requirement. Default: - requirement is managed by the package manager (e.g. npm/yarn).

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) The package manager name of the dependency (e.g. ``leftpad`` for npm).

        NOTE: For package managers that use complex coordinates (like Maven), we
        will codify it into a string somehow.

        :stability: experimental
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''(experimental) Semantic version version requirement.

        :default: - requirement is managed by the package manager (e.g. npm/yarn).

        :stability: experimental
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DependencyCoordinates(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="projen.DependencyType")
class DependencyType(enum.Enum):
    '''(experimental) Type of dependency.

    :stability: experimental
    '''

    RUNTIME = "RUNTIME"
    '''(experimental) The dependency is required for the program/library during runtime.

    :stability: experimental
    '''
    PEER = "PEER"
    '''(experimental) The dependency is required at runtime but expected to be installed by the consumer.

    :stability: experimental
    '''
    BUNDLED = "BUNDLED"
    '''(experimental) The dependency is bundled and shipped with the module, so consumers are not required to install it.

    :stability: experimental
    '''
    BUILD = "BUILD"
    '''(experimental) The dependency is required to run the ``build`` task.

    :stability: experimental
    '''
    TEST = "TEST"
    '''(experimental) The dependency is required to run the ``test`` task.

    :stability: experimental
    '''
    DEVENV = "DEVENV"
    '''(experimental) The dependency is required for development (e.g. IDE plugins).

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="projen.DepsManifest",
    jsii_struct_bases=[],
    name_mapping={"dependencies": "dependencies"},
)
class DepsManifest:
    def __init__(self, *, dependencies: typing.Sequence["Dependency"]) -> None:
        '''
        :param dependencies: (experimental) All dependencies of this module.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "dependencies": dependencies,
        }

    @builtins.property
    def dependencies(self) -> typing.List["Dependency"]:
        '''(experimental) All dependencies of this module.

        :stability: experimental
        '''
        result = self._values.get("dependencies")
        assert result is not None, "Required property 'dependencies' is missing"
        return typing.cast(typing.List["Dependency"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DepsManifest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DevEnvironmentDockerImage(
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.DevEnvironmentDockerImage",
):
    '''(experimental) Options for specifying the Docker image of the container.

    :stability: experimental
    '''

    @jsii.member(jsii_name="fromFile") # type: ignore[misc]
    @builtins.classmethod
    def from_file(cls, docker_file: builtins.str) -> "DevEnvironmentDockerImage":
        '''(experimental) The relative path of a Dockerfile that defines the container contents.

        :param docker_file: a relative path.

        :stability: experimental

        Example::

            '.gitpod.Docker'
        '''
        return typing.cast("DevEnvironmentDockerImage", jsii.sinvoke(cls, "fromFile", [docker_file]))

    @jsii.member(jsii_name="fromImage") # type: ignore[misc]
    @builtins.classmethod
    def from_image(cls, image: builtins.str) -> "DevEnvironmentDockerImage":
        '''(experimental) A publicly available Docker image.

        :param image: a Docker image.

        :stability: experimental

        Example::

            'ubuntu:latest'
        '''
        return typing.cast("DevEnvironmentDockerImage", jsii.sinvoke(cls, "fromImage", [image]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dockerFile")
    def docker_file(self) -> typing.Optional[builtins.str]:
        '''(experimental) The relative path of a Dockerfile that defines the container contents.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerFile"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="image")
    def image(self) -> typing.Optional[builtins.str]:
        '''(experimental) A publicly available Docker image.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "image"))


@jsii.data_type(
    jsii_type="projen.DevEnvironmentOptions",
    jsii_struct_bases=[],
    name_mapping={
        "docker_image": "dockerImage",
        "ports": "ports",
        "tasks": "tasks",
        "vscode_extensions": "vscodeExtensions",
    },
)
class DevEnvironmentOptions:
    def __init__(
        self,
        *,
        docker_image: typing.Optional[DevEnvironmentDockerImage] = None,
        ports: typing.Optional[typing.Sequence[builtins.str]] = None,
        tasks: typing.Optional[typing.Sequence["Task"]] = None,
        vscode_extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) Base options for configuring a container-based development environment.

        :param docker_image: (experimental) A Docker image or Dockerfile for the container.
        :param ports: (experimental) An array of ports that should be exposed from the container.
        :param tasks: (experimental) An array of tasks that should be run when the container starts.
        :param vscode_extensions: (experimental) An array of extension IDs that specify the extensions that should be installed inside the container when it is created.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if docker_image is not None:
            self._values["docker_image"] = docker_image
        if ports is not None:
            self._values["ports"] = ports
        if tasks is not None:
            self._values["tasks"] = tasks
        if vscode_extensions is not None:
            self._values["vscode_extensions"] = vscode_extensions

    @builtins.property
    def docker_image(self) -> typing.Optional[DevEnvironmentDockerImage]:
        '''(experimental) A Docker image or Dockerfile for the container.

        :stability: experimental
        '''
        result = self._values.get("docker_image")
        return typing.cast(typing.Optional[DevEnvironmentDockerImage], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) An array of ports that should be exposed from the container.

        :stability: experimental
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tasks(self) -> typing.Optional[typing.List["Task"]]:
        '''(experimental) An array of tasks that should be run when the container starts.

        :stability: experimental
        '''
        result = self._values.get("tasks")
        return typing.cast(typing.Optional[typing.List["Task"]], result)

    @builtins.property
    def vscode_extensions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) An array of extension IDs that specify the extensions that should be installed inside the container when it is created.

        :stability: experimental
        '''
        result = self._values.get("vscode_extensions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DevEnvironmentOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DockerCompose(
    Component,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.DockerCompose",
):
    '''(experimental) Create a docker-compose YAML file.

    :stability: experimental
    '''

    def __init__(
        self,
        project: "Project",
        *,
        name_suffix: typing.Optional[builtins.str] = None,
        schema_version: typing.Optional[builtins.str] = None,
        services: typing.Optional[typing.Mapping[builtins.str, "DockerComposeServiceDescription"]] = None,
    ) -> None:
        '''
        :param project: -
        :param name_suffix: (experimental) A name to add to the docker-compose.yml filename. Default: - no name is added
        :param schema_version: (experimental) Docker Compose schema version do be used. Default: 3.3
        :param services: (experimental) Service descriptions.

        :stability: experimental
        '''
        props = DockerComposeProps(
            name_suffix=name_suffix, schema_version=schema_version, services=services
        )

        jsii.create(self.__class__, self, [project, props])

    @jsii.member(jsii_name="bindVolume") # type: ignore[misc]
    @builtins.classmethod
    def bind_volume(
        cls,
        source_path: builtins.str,
        target_path: builtins.str,
    ) -> "IDockerComposeVolumeBinding":
        '''(experimental) Create a bind volume that binds a host path to the target path in the container.

        :param source_path: Host path name.
        :param target_path: Target path name.

        :stability: experimental
        '''
        return typing.cast("IDockerComposeVolumeBinding", jsii.sinvoke(cls, "bindVolume", [source_path, target_path]))

    @jsii.member(jsii_name="namedVolume") # type: ignore[misc]
    @builtins.classmethod
    def named_volume(
        cls,
        volume_name: builtins.str,
        target_path: builtins.str,
        *,
        driver: typing.Optional[builtins.str] = None,
        driver_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        external: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "IDockerComposeVolumeBinding":
        '''(experimental) Create a named volume and mount it to the target path.

        If you use this
        named volume in several services, the volume will be shared. In this
        case, the volume configuration of the first-provided options are used.

        :param volume_name: Name of the volume.
        :param target_path: Target path.
        :param driver: (experimental) Driver to use for the volume. Default: - value is not provided
        :param driver_opts: (experimental) Options to provide to the driver.
        :param external: (experimental) Set to true to indicate that the volume is externally created. Default: - unset, indicating that docker-compose creates the volume
        :param name: (experimental) Name of the volume for when the volume name isn't going to work in YAML. Default: - unset, indicating that docker-compose creates volumes as usual

        :stability: experimental
        '''
        options = DockerComposeVolumeConfig(
            driver=driver, driver_opts=driver_opts, external=external, name=name
        )

        return typing.cast("IDockerComposeVolumeBinding", jsii.sinvoke(cls, "namedVolume", [volume_name, target_path, options]))

    @jsii.member(jsii_name="portMapping") # type: ignore[misc]
    @builtins.classmethod
    def port_mapping(
        cls,
        published_port: jsii.Number,
        target_port: jsii.Number,
        *,
        protocol: typing.Optional["DockerComposeProtocol"] = None,
    ) -> "DockerComposeServicePort":
        '''(experimental) Create a port mapping.

        :param published_port: Published port number.
        :param target_port: Container's port number.
        :param protocol: (experimental) Port mapping protocol. Default: DockerComposeProtocol.TCP

        :stability: experimental
        '''
        options = DockerComposePortMappingOptions(protocol=protocol)

        return typing.cast("DockerComposeServicePort", jsii.sinvoke(cls, "portMapping", [published_port, target_port, options]))

    @jsii.member(jsii_name="serviceName") # type: ignore[misc]
    @builtins.classmethod
    def service_name(cls, service_name: builtins.str) -> "IDockerComposeServiceName":
        '''(experimental) Depends on a service name.

        :param service_name: -

        :stability: experimental
        '''
        return typing.cast("IDockerComposeServiceName", jsii.sinvoke(cls, "serviceName", [service_name]))

    @jsii.member(jsii_name="addService")
    def add_service(
        self,
        service_name: builtins.str,
        *,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        depends_on: typing.Optional[typing.Sequence["IDockerComposeServiceName"]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        image: typing.Optional[builtins.str] = None,
        image_build: typing.Optional["DockerComposeBuild"] = None,
        ports: typing.Optional[typing.Sequence["DockerComposeServicePort"]] = None,
        volumes: typing.Optional[typing.Sequence["IDockerComposeVolumeBinding"]] = None,
    ) -> "DockerComposeService":
        '''(experimental) Add a service to the docker-compose file.

        :param service_name: name of the service.
        :param command: (experimental) Provide a command to the docker container. Default: - use the container's default command
        :param depends_on: (experimental) Names of other services this service depends on. Default: - no dependencies
        :param environment: (experimental) Add environment variables. Default: - no environment variables are provided
        :param image: (experimental) Use a docker image. Note: You must specify either ``build`` or ``image`` key.
        :param image_build: (experimental) Build a docker image. Note: You must specify either ``imageBuild`` or ``image`` key.
        :param ports: (experimental) Map some ports. Default: - no ports are mapped
        :param volumes: (experimental) Mount some volumes into the service. Use one of the following to create volumes:

        :stability: experimental
        '''
        description = DockerComposeServiceDescription(
            command=command,
            depends_on=depends_on,
            environment=environment,
            image=image,
            image_build=image_build,
            ports=ports,
            volumes=volumes,
        )

        return typing.cast("DockerComposeService", jsii.invoke(self, "addService", [service_name, description]))


@jsii.data_type(
    jsii_type="projen.DockerComposeBuild",
    jsii_struct_bases=[],
    name_mapping={"context": "context", "args": "args", "dockerfile": "dockerfile"},
)
class DockerComposeBuild:
    def __init__(
        self,
        *,
        context: builtins.str,
        args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        dockerfile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Build arguments for creating a docker image.

        :param context: (experimental) Docker build context directory.
        :param args: (experimental) Build args. Default: - none are provided
        :param dockerfile: (experimental) A dockerfile to build from. Default: "Dockerfile"

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "context": context,
        }
        if args is not None:
            self._values["args"] = args
        if dockerfile is not None:
            self._values["dockerfile"] = dockerfile

    @builtins.property
    def context(self) -> builtins.str:
        '''(experimental) Docker build context directory.

        :stability: experimental
        '''
        result = self._values.get("context")
        assert result is not None, "Required property 'context' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def args(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) Build args.

        :default: - none are provided

        :stability: experimental
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def dockerfile(self) -> typing.Optional[builtins.str]:
        '''(experimental) A dockerfile to build from.

        :default: "Dockerfile"

        :stability: experimental
        '''
        result = self._values.get("dockerfile")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerComposeBuild(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.DockerComposePortMappingOptions",
    jsii_struct_bases=[],
    name_mapping={"protocol": "protocol"},
)
class DockerComposePortMappingOptions:
    def __init__(
        self,
        *,
        protocol: typing.Optional["DockerComposeProtocol"] = None,
    ) -> None:
        '''(experimental) Options for port mappings.

        :param protocol: (experimental) Port mapping protocol. Default: DockerComposeProtocol.TCP

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if protocol is not None:
            self._values["protocol"] = protocol

    @builtins.property
    def protocol(self) -> typing.Optional["DockerComposeProtocol"]:
        '''(experimental) Port mapping protocol.

        :default: DockerComposeProtocol.TCP

        :stability: experimental
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional["DockerComposeProtocol"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerComposePortMappingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.DockerComposeProps",
    jsii_struct_bases=[],
    name_mapping={
        "name_suffix": "nameSuffix",
        "schema_version": "schemaVersion",
        "services": "services",
    },
)
class DockerComposeProps:
    def __init__(
        self,
        *,
        name_suffix: typing.Optional[builtins.str] = None,
        schema_version: typing.Optional[builtins.str] = None,
        services: typing.Optional[typing.Mapping[builtins.str, "DockerComposeServiceDescription"]] = None,
    ) -> None:
        '''(experimental) Props for DockerCompose.

        :param name_suffix: (experimental) A name to add to the docker-compose.yml filename. Default: - no name is added
        :param schema_version: (experimental) Docker Compose schema version do be used. Default: 3.3
        :param services: (experimental) Service descriptions.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name_suffix is not None:
            self._values["name_suffix"] = name_suffix
        if schema_version is not None:
            self._values["schema_version"] = schema_version
        if services is not None:
            self._values["services"] = services

    @builtins.property
    def name_suffix(self) -> typing.Optional[builtins.str]:
        '''(experimental) A name to add to the docker-compose.yml filename.

        :default: - no name is added

        :stability: experimental

        Example::

            'myname' yields 'docker-compose.myname.yml'
        '''
        result = self._values.get("name_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_version(self) -> typing.Optional[builtins.str]:
        '''(experimental) Docker Compose schema version do be used.

        :default: 3.3

        :stability: experimental
        '''
        result = self._values.get("schema_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def services(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "DockerComposeServiceDescription"]]:
        '''(experimental) Service descriptions.

        :stability: experimental
        '''
        result = self._values.get("services")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "DockerComposeServiceDescription"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerComposeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="projen.DockerComposeProtocol")
class DockerComposeProtocol(enum.Enum):
    '''(experimental) Network protocol for port mapping.

    :stability: experimental
    '''

    TCP = "TCP"
    '''(experimental) TCP protocol.

    :stability: experimental
    '''
    UDP = "UDP"
    '''(experimental) UDP protocol.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="projen.DockerComposeServiceDescription",
    jsii_struct_bases=[],
    name_mapping={
        "command": "command",
        "depends_on": "dependsOn",
        "environment": "environment",
        "image": "image",
        "image_build": "imageBuild",
        "ports": "ports",
        "volumes": "volumes",
    },
)
class DockerComposeServiceDescription:
    def __init__(
        self,
        *,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        depends_on: typing.Optional[typing.Sequence["IDockerComposeServiceName"]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        image: typing.Optional[builtins.str] = None,
        image_build: typing.Optional[DockerComposeBuild] = None,
        ports: typing.Optional[typing.Sequence["DockerComposeServicePort"]] = None,
        volumes: typing.Optional[typing.Sequence["IDockerComposeVolumeBinding"]] = None,
    ) -> None:
        '''(experimental) Description of a docker-compose.yml service.

        :param command: (experimental) Provide a command to the docker container. Default: - use the container's default command
        :param depends_on: (experimental) Names of other services this service depends on. Default: - no dependencies
        :param environment: (experimental) Add environment variables. Default: - no environment variables are provided
        :param image: (experimental) Use a docker image. Note: You must specify either ``build`` or ``image`` key.
        :param image_build: (experimental) Build a docker image. Note: You must specify either ``imageBuild`` or ``image`` key.
        :param ports: (experimental) Map some ports. Default: - no ports are mapped
        :param volumes: (experimental) Mount some volumes into the service. Use one of the following to create volumes:

        :stability: experimental
        '''
        if isinstance(image_build, dict):
            image_build = DockerComposeBuild(**image_build)
        self._values: typing.Dict[str, typing.Any] = {}
        if command is not None:
            self._values["command"] = command
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if environment is not None:
            self._values["environment"] = environment
        if image is not None:
            self._values["image"] = image
        if image_build is not None:
            self._values["image_build"] = image_build
        if ports is not None:
            self._values["ports"] = ports
        if volumes is not None:
            self._values["volumes"] = volumes

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Provide a command to the docker container.

        :default: - use the container's default command

        :stability: experimental
        '''
        result = self._values.get("command")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List["IDockerComposeServiceName"]]:
        '''(experimental) Names of other services this service depends on.

        :default: - no dependencies

        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List["IDockerComposeServiceName"]], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) Add environment variables.

        :default: - no environment variables are provided

        :stability: experimental
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def image(self) -> typing.Optional[builtins.str]:
        '''(experimental) Use a docker image.

        Note: You must specify either ``build`` or ``image`` key.

        :see: imageBuild
        :stability: experimental
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_build(self) -> typing.Optional[DockerComposeBuild]:
        '''(experimental) Build a docker image.

        Note: You must specify either ``imageBuild`` or ``image`` key.

        :see: image
        :stability: experimental
        '''
        result = self._values.get("image_build")
        return typing.cast(typing.Optional[DockerComposeBuild], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List["DockerComposeServicePort"]]:
        '''(experimental) Map some ports.

        :default: - no ports are mapped

        :stability: experimental
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List["DockerComposeServicePort"]], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List["IDockerComposeVolumeBinding"]]:
        '''(experimental) Mount some volumes into the service.

        Use one of the following to create volumes:

        :see: DockerCompose.namedVolume() to create & mount a named volume
        :stability: experimental
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List["IDockerComposeVolumeBinding"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerComposeServiceDescription(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.DockerComposeServicePort",
    jsii_struct_bases=[],
    name_mapping={
        "mode": "mode",
        "protocol": "protocol",
        "published": "published",
        "target": "target",
    },
)
class DockerComposeServicePort:
    def __init__(
        self,
        *,
        mode: builtins.str,
        protocol: DockerComposeProtocol,
        published: jsii.Number,
        target: jsii.Number,
    ) -> None:
        '''(experimental) A service port mapping.

        :param mode: (experimental) Port mapping mode.
        :param protocol: (experimental) Network protocol.
        :param published: (experimental) Published port number.
        :param target: (experimental) Target port number.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "protocol": protocol,
            "published": published,
            "target": target,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''(experimental) Port mapping mode.

        :stability: experimental
        '''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> DockerComposeProtocol:
        '''(experimental) Network protocol.

        :stability: experimental
        '''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(DockerComposeProtocol, result)

    @builtins.property
    def published(self) -> jsii.Number:
        '''(experimental) Published port number.

        :stability: experimental
        '''
        result = self._values.get("published")
        assert result is not None, "Required property 'published' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def target(self) -> jsii.Number:
        '''(experimental) Target port number.

        :stability: experimental
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerComposeServicePort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.DockerComposeVolumeConfig",
    jsii_struct_bases=[],
    name_mapping={
        "driver": "driver",
        "driver_opts": "driverOpts",
        "external": "external",
        "name": "name",
    },
)
class DockerComposeVolumeConfig:
    def __init__(
        self,
        *,
        driver: typing.Optional[builtins.str] = None,
        driver_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        external: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Volume configuration.

        :param driver: (experimental) Driver to use for the volume. Default: - value is not provided
        :param driver_opts: (experimental) Options to provide to the driver.
        :param external: (experimental) Set to true to indicate that the volume is externally created. Default: - unset, indicating that docker-compose creates the volume
        :param name: (experimental) Name of the volume for when the volume name isn't going to work in YAML. Default: - unset, indicating that docker-compose creates volumes as usual

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if driver is not None:
            self._values["driver"] = driver
        if driver_opts is not None:
            self._values["driver_opts"] = driver_opts
        if external is not None:
            self._values["external"] = external
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def driver(self) -> typing.Optional[builtins.str]:
        '''(experimental) Driver to use for the volume.

        :default: - value is not provided

        :stability: experimental
        '''
        result = self._values.get("driver")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def driver_opts(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) Options to provide to the driver.

        :stability: experimental
        '''
        result = self._values.get("driver_opts")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def external(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Set to true to indicate that the volume is externally created.

        :default: - unset, indicating that docker-compose creates the volume

        :stability: experimental
        '''
        result = self._values.get("external")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Name of the volume for when the volume name isn't going to work in YAML.

        :default: - unset, indicating that docker-compose creates volumes as usual

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerComposeVolumeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.DockerComposeVolumeMount",
    jsii_struct_bases=[],
    name_mapping={"source": "source", "target": "target", "type": "type"},
)
class DockerComposeVolumeMount:
    def __init__(
        self,
        *,
        source: builtins.str,
        target: builtins.str,
        type: builtins.str,
    ) -> None:
        '''(experimental) Service volume mounting information.

        :param source: (experimental) Volume source.
        :param target: (experimental) Volume target.
        :param type: (experimental) Type of volume.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "source": source,
            "target": target,
            "type": type,
        }

    @builtins.property
    def source(self) -> builtins.str:
        '''(experimental) Volume source.

        :stability: experimental
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''(experimental) Volume target.

        :stability: experimental
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''(experimental) Type of volume.

        :stability: experimental
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerComposeVolumeMount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FileBase(
    Component,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="projen.FileBase",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        project: "Project",
        file_path: builtins.str,
        *,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param project: -
        :param file_path: -
        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true

        :stability: experimental
        '''
        options = FileBaseOptions(
            committed=committed,
            edit_gitignore=edit_gitignore,
            executable=executable,
            marker=marker,
            readonly=readonly,
        )

        jsii.create(self.__class__, self, [project, file_path, options])

    @jsii.member(jsii_name="synthesize")
    def synthesize(self) -> None:
        '''(experimental) Writes the file to the project's output directory.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "synthesize", []))

    @jsii.member(jsii_name="synthesizeContent") # type: ignore[misc]
    @abc.abstractmethod
    def _synthesize_content(
        self,
        resolver: "IResolver",
    ) -> typing.Optional[builtins.str]:
        '''(experimental) Implemented by derived classes and returns the contents of the file to emit.

        :param resolver: Call ``resolver.resolve(obj)`` on any objects in order to resolve token functions.

        :return: the content to synthesize or undefined to skip the file

        :stability: experimental
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="absolutePath")
    def absolute_path(self) -> builtins.str:
        '''(experimental) The absolute path of this file.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "absolutePath"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        '''(experimental) The file path, relative to the project root.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="changed")
    def changed(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates if the file has been changed during synthesis.

        This property is
        only available in ``postSynthesize()`` hooks. If this is ``undefined``, the
        file has not been synthesized yet.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "changed"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="marker")
    def marker(self) -> typing.Optional[builtins.str]:
        '''(experimental) The projen marker, used to identify files as projen-generated.

        Value is undefined if the project is being ejected.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "marker"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="executable")
    def executable(self) -> builtins.bool:
        '''(experimental) Indicates if the file should be marked as executable.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "executable"))

    @executable.setter
    def executable(self, value: builtins.bool) -> None:
        jsii.set(self, "executable", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="readonly")
    def readonly(self) -> builtins.bool:
        '''(experimental) Indicates if the file should be read-only or read-write.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "readonly"))

    @readonly.setter
    def readonly(self, value: builtins.bool) -> None:
        jsii.set(self, "readonly", value)


class _FileBaseProxy(FileBase):
    @jsii.member(jsii_name="synthesizeContent")
    def _synthesize_content(
        self,
        resolver: "IResolver",
    ) -> typing.Optional[builtins.str]:
        '''(experimental) Implemented by derived classes and returns the contents of the file to emit.

        :param resolver: Call ``resolver.resolve(obj)`` on any objects in order to resolve token functions.

        :return: the content to synthesize or undefined to skip the file

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "synthesizeContent", [resolver]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, FileBase).__jsii_proxy_class__ = lambda : _FileBaseProxy


@jsii.data_type(
    jsii_type="projen.FileBaseOptions",
    jsii_struct_bases=[],
    name_mapping={
        "committed": "committed",
        "edit_gitignore": "editGitignore",
        "executable": "executable",
        "marker": "marker",
        "readonly": "readonly",
    },
)
class FileBaseOptions:
    def __init__(
        self,
        *,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if committed is not None:
            self._values["committed"] = committed
        if edit_gitignore is not None:
            self._values["edit_gitignore"] = edit_gitignore
        if executable is not None:
            self._values["executable"] = executable
        if marker is not None:
            self._values["marker"] = marker
        if readonly is not None:
            self._values["readonly"] = readonly

    @builtins.property
    def committed(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether this file should be committed to git or ignored.

        By
        default, all generated files are committed and anti-tamper is used to
        protect against manual modifications.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("committed")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def edit_gitignore(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Update the project's .gitignore file.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("edit_gitignore")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def executable(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be marked as executable.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("executable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def marker(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Adds the projen marker to the file.

        :default: - marker will be included as long as the project is not ejected

        :stability: experimental
        '''
        result = self._values.get("marker")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def readonly(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be readonly.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("readonly")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileBaseOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GitAttributesFile(
    FileBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.GitAttributesFile",
):
    '''(experimental) Assign attributes to file names in a git repository.

    :see: https://git-scm.com/docs/gitattributes
    :stability: experimental
    '''

    def __init__(self, project: "Project") -> None:
        '''
        :param project: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [project])

    @jsii.member(jsii_name="addAttributes")
    def add_attributes(self, glob: builtins.str, *attributes: builtins.str) -> None:
        '''(experimental) Maps a set of attributes to a set of files.

        :param glob: Glob pattern to match files in the repo.
        :param attributes: Attributes to assign to these files.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addAttributes", [glob, *attributes]))

    @jsii.member(jsii_name="synthesizeContent")
    def _synthesize_content(self, _: "IResolver") -> typing.Optional[builtins.str]:
        '''(experimental) Implemented by derived classes and returns the contents of the file to emit.

        :param _: -

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "synthesizeContent", [_]))


@jsii.enum(jsii_type="projen.GitpodOnOpen")
class GitpodOnOpen(enum.Enum):
    '''(experimental) What to do when a service on a port is detected.

    :stability: experimental
    '''

    OPEN_BROWSER = "OPEN_BROWSER"
    '''(experimental) Open a new browser tab.

    :stability: experimental
    '''
    OPEN_PREVIEW = "OPEN_PREVIEW"
    '''(experimental) Open a preview on the right side of the IDE.

    :stability: experimental
    '''
    NOTIFY = "NOTIFY"
    '''(experimental) Show a notification asking the user what to do (default).

    :stability: experimental
    '''
    IGNORE = "IGNORE"
    '''(experimental) Do nothing.

    :stability: experimental
    '''


@jsii.enum(jsii_type="projen.GitpodOpenIn")
class GitpodOpenIn(enum.Enum):
    '''(experimental) Configure where in the IDE the terminal should be opened.

    :stability: experimental
    '''

    BOTTOM = "BOTTOM"
    '''(experimental) the bottom panel (default).

    :stability: experimental
    '''
    LEFT = "LEFT"
    '''(experimental) the left panel.

    :stability: experimental
    '''
    RIGHT = "RIGHT"
    '''(experimental) the right panel.

    :stability: experimental
    '''
    MAIN = "MAIN"
    '''(experimental) the main editor area.

    :stability: experimental
    '''


@jsii.enum(jsii_type="projen.GitpodOpenMode")
class GitpodOpenMode(enum.Enum):
    '''(experimental) Configure how the terminal should be opened relative to the previous task.

    :stability: experimental
    '''

    TAB_AFTER = "TAB_AFTER"
    '''(experimental) Opens in the same tab group right after the previous tab.

    :stability: experimental
    '''
    TAB_BEFORE = "TAB_BEFORE"
    '''(experimental) Opens in the same tab group left before the previous tab.

    :stability: experimental
    '''
    SPLIT_RIGHT = "SPLIT_RIGHT"
    '''(experimental) Splits and adds the terminal to the right.

    :stability: experimental
    '''
    SPLIT_LEFT = "SPLIT_LEFT"
    '''(experimental) Splits and adds the terminal to the left.

    :stability: experimental
    '''
    SPLIT_TOP = "SPLIT_TOP"
    '''(experimental) Splits and adds the terminal to the top.

    :stability: experimental
    '''
    SPLIT_BOTTOM = "SPLIT_BOTTOM"
    '''(experimental) Splits and adds the terminal to the bottom.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="projen.GitpodOptions",
    jsii_struct_bases=[DevEnvironmentOptions],
    name_mapping={
        "docker_image": "dockerImage",
        "ports": "ports",
        "tasks": "tasks",
        "vscode_extensions": "vscodeExtensions",
        "prebuilds": "prebuilds",
    },
)
class GitpodOptions(DevEnvironmentOptions):
    def __init__(
        self,
        *,
        docker_image: typing.Optional[DevEnvironmentDockerImage] = None,
        ports: typing.Optional[typing.Sequence[builtins.str]] = None,
        tasks: typing.Optional[typing.Sequence["Task"]] = None,
        vscode_extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
        prebuilds: typing.Optional["GitpodPrebuilds"] = None,
    ) -> None:
        '''(experimental) Constructor options for the Gitpod component.

        By default, Gitpod uses the 'gitpod/workspace-full' docker image.

        :param docker_image: (experimental) A Docker image or Dockerfile for the container.
        :param ports: (experimental) An array of ports that should be exposed from the container.
        :param tasks: (experimental) An array of tasks that should be run when the container starts.
        :param vscode_extensions: (experimental) An array of extension IDs that specify the extensions that should be installed inside the container when it is created.
        :param prebuilds: (experimental) Optional Gitpod's Github App integration for prebuilds If this is not set and Gitpod's Github App is installed, then Gitpod will apply these defaults: https://www.gitpod.io/docs/prebuilds/#configure-the-github-app. Default: undefined

        :see:

        https://github.com/gitpod-io/workspace-images/blob/master/full/Dockerfile

        By default, all tasks will be run in parallel. To run the tasks in sequence,
        create a new task and specify the other tasks as subtasks.
        :stability: experimental
        '''
        if isinstance(prebuilds, dict):
            prebuilds = GitpodPrebuilds(**prebuilds)
        self._values: typing.Dict[str, typing.Any] = {}
        if docker_image is not None:
            self._values["docker_image"] = docker_image
        if ports is not None:
            self._values["ports"] = ports
        if tasks is not None:
            self._values["tasks"] = tasks
        if vscode_extensions is not None:
            self._values["vscode_extensions"] = vscode_extensions
        if prebuilds is not None:
            self._values["prebuilds"] = prebuilds

    @builtins.property
    def docker_image(self) -> typing.Optional[DevEnvironmentDockerImage]:
        '''(experimental) A Docker image or Dockerfile for the container.

        :stability: experimental
        '''
        result = self._values.get("docker_image")
        return typing.cast(typing.Optional[DevEnvironmentDockerImage], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) An array of ports that should be exposed from the container.

        :stability: experimental
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tasks(self) -> typing.Optional[typing.List["Task"]]:
        '''(experimental) An array of tasks that should be run when the container starts.

        :stability: experimental
        '''
        result = self._values.get("tasks")
        return typing.cast(typing.Optional[typing.List["Task"]], result)

    @builtins.property
    def vscode_extensions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) An array of extension IDs that specify the extensions that should be installed inside the container when it is created.

        :stability: experimental
        '''
        result = self._values.get("vscode_extensions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def prebuilds(self) -> typing.Optional["GitpodPrebuilds"]:
        '''(experimental) Optional Gitpod's Github App integration for prebuilds If this is not set and Gitpod's Github App is installed, then Gitpod will apply these defaults: https://www.gitpod.io/docs/prebuilds/#configure-the-github-app.

        :default: undefined

        :stability: experimental
        '''
        result = self._values.get("prebuilds")
        return typing.cast(typing.Optional["GitpodPrebuilds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitpodOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.GitpodPort",
    jsii_struct_bases=[],
    name_mapping={"on_open": "onOpen", "port": "port", "visibility": "visibility"},
)
class GitpodPort:
    def __init__(
        self,
        *,
        on_open: typing.Optional[GitpodOnOpen] = None,
        port: typing.Optional[builtins.str] = None,
        visibility: typing.Optional["GitpodPortVisibility"] = None,
    ) -> None:
        '''(experimental) Options for an exposed port on Gitpod.

        :param on_open: (experimental) What to do when a service on a port is detected. Default: GitpodOnOpen.NOTIFY
        :param port: (experimental) A port that should be exposed (forwarded) from the container.
        :param visibility: (experimental) Whether the port visibility should be private or public. Default: GitpodPortVisibility.PUBLIC

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if on_open is not None:
            self._values["on_open"] = on_open
        if port is not None:
            self._values["port"] = port
        if visibility is not None:
            self._values["visibility"] = visibility

    @builtins.property
    def on_open(self) -> typing.Optional[GitpodOnOpen]:
        '''(experimental) What to do when a service on a port is detected.

        :default: GitpodOnOpen.NOTIFY

        :stability: experimental
        '''
        result = self._values.get("on_open")
        return typing.cast(typing.Optional[GitpodOnOpen], result)

    @builtins.property
    def port(self) -> typing.Optional[builtins.str]:
        '''(experimental) A port that should be exposed (forwarded) from the container.

        :stability: experimental

        Example::

            "8080"
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def visibility(self) -> typing.Optional["GitpodPortVisibility"]:
        '''(experimental) Whether the port visibility should be private or public.

        :default: GitpodPortVisibility.PUBLIC

        :stability: experimental
        '''
        result = self._values.get("visibility")
        return typing.cast(typing.Optional["GitpodPortVisibility"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitpodPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="projen.GitpodPortVisibility")
class GitpodPortVisibility(enum.Enum):
    '''(experimental) Whether the port visibility should be private or public.

    :stability: experimental
    '''

    PUBLIC = "PUBLIC"
    '''(experimental) Allows everyone with the port URL to access the port (default).

    :stability: experimental
    '''
    PRIVATE = "PRIVATE"
    '''(experimental) Only allows users with workspace access to access the port.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="projen.GitpodPrebuilds",
    jsii_struct_bases=[],
    name_mapping={
        "add_badge": "addBadge",
        "add_check": "addCheck",
        "add_comment": "addComment",
        "add_label": "addLabel",
        "branches": "branches",
        "master": "master",
        "pull_requests": "pullRequests",
        "pull_requests_from_forks": "pullRequestsFromForks",
    },
)
class GitpodPrebuilds:
    def __init__(
        self,
        *,
        add_badge: typing.Optional[builtins.bool] = None,
        add_check: typing.Optional[builtins.bool] = None,
        add_comment: typing.Optional[builtins.bool] = None,
        add_label: typing.Optional[builtins.bool] = None,
        branches: typing.Optional[builtins.bool] = None,
        master: typing.Optional[builtins.bool] = None,
        pull_requests: typing.Optional[builtins.bool] = None,
        pull_requests_from_forks: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Configure the Gitpod App for prebuilds.

        Currently only GitHub is supported.

        :param add_badge: (experimental) Add a "Review in Gitpod" button to the pull request's description. Default: false
        :param add_check: (experimental) Add a check to pull requests. Default: true
        :param add_comment: (experimental) Add a "Review in Gitpod" button as a comment to pull requests. Default: false
        :param add_label: (experimental) Add a label once the prebuild is ready to pull requests. Default: false
        :param branches: (experimental) Enable for all branches in this repo. Default: false
        :param master: (experimental) Enable for the master/default branch. Default: true
        :param pull_requests: (experimental) Enable for pull requests coming from this repo. Default: true
        :param pull_requests_from_forks: (experimental) Enable for pull requests coming from forks. Default: false

        :see: https://www.gitpod.io/docs/prebuilds/
        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if add_badge is not None:
            self._values["add_badge"] = add_badge
        if add_check is not None:
            self._values["add_check"] = add_check
        if add_comment is not None:
            self._values["add_comment"] = add_comment
        if add_label is not None:
            self._values["add_label"] = add_label
        if branches is not None:
            self._values["branches"] = branches
        if master is not None:
            self._values["master"] = master
        if pull_requests is not None:
            self._values["pull_requests"] = pull_requests
        if pull_requests_from_forks is not None:
            self._values["pull_requests_from_forks"] = pull_requests_from_forks

    @builtins.property
    def add_badge(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Add a "Review in Gitpod" button to the pull request's description.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("add_badge")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def add_check(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Add a check to pull requests.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("add_check")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def add_comment(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Add a "Review in Gitpod" button as a comment to pull requests.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("add_comment")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def add_label(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Add a label once the prebuild is ready to pull requests.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("add_label")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def branches(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Enable for all branches in this repo.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("branches")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def master(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Enable for the master/default branch.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("master")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def pull_requests(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Enable for pull requests coming from this repo.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("pull_requests")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def pull_requests_from_forks(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Enable for pull requests coming from forks.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("pull_requests_from_forks")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitpodPrebuilds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.GitpodTask",
    jsii_struct_bases=[],
    name_mapping={
        "command": "command",
        "before": "before",
        "init": "init",
        "name": "name",
        "open_in": "openIn",
        "open_mode": "openMode",
        "prebuild": "prebuild",
    },
)
class GitpodTask:
    def __init__(
        self,
        *,
        command: builtins.str,
        before: typing.Optional[builtins.str] = None,
        init: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        open_in: typing.Optional[GitpodOpenIn] = None,
        open_mode: typing.Optional[GitpodOpenMode] = None,
        prebuild: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Configure options for a task to be run when opening a Gitpod workspace (e.g. running tests, or starting a dev server).

        Start Mode         | Execution
        Fresh Workspace    | before && init && command
        Restart Workspace  | before && command
        Snapshot           | before && command
        Prebuild           | before && init && prebuild

        :param command: (experimental) Required. The shell command to run
        :param before: (experimental) In case you need to run something even before init, that is a requirement for both init and command, you can use the before property.
        :param init: (experimental) The init property can be used to specify shell commands that should only be executed after a workspace was freshly cloned and needs to be initialized somehow. Such tasks are usually builds or downloading dependencies. Anything you only want to do once but not when you restart a workspace or start a snapshot.
        :param name: (experimental) A name for this task. Default: - task names are omitted when blank
        :param open_in: (experimental) You can configure where in the IDE the terminal should be opened. Default: GitpodOpenIn.BOTTOM
        :param open_mode: (experimental) You can configure how the terminal should be opened relative to the previous task. Default: GitpodOpenMode.TAB_AFTER
        :param prebuild: (experimental) The optional prebuild command will be executed during prebuilds. It is meant to run additional long running processes that could be useful, e.g. running test suites.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "command": command,
        }
        if before is not None:
            self._values["before"] = before
        if init is not None:
            self._values["init"] = init
        if name is not None:
            self._values["name"] = name
        if open_in is not None:
            self._values["open_in"] = open_in
        if open_mode is not None:
            self._values["open_mode"] = open_mode
        if prebuild is not None:
            self._values["prebuild"] = prebuild

    @builtins.property
    def command(self) -> builtins.str:
        '''(experimental) Required.

        The shell command to run

        :stability: experimental
        '''
        result = self._values.get("command")
        assert result is not None, "Required property 'command' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def before(self) -> typing.Optional[builtins.str]:
        '''(experimental) In case you need to run something even before init, that is a requirement for both init and command, you can use the before property.

        :stability: experimental
        '''
        result = self._values.get("before")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def init(self) -> typing.Optional[builtins.str]:
        '''(experimental) The init property can be used to specify shell commands that should only be executed after a workspace was freshly cloned and needs to be initialized somehow.

        Such tasks are usually builds or downloading
        dependencies. Anything you only want to do once but not when you restart a workspace or start a snapshot.

        :stability: experimental
        '''
        result = self._values.get("init")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) A name for this task.

        :default: - task names are omitted when blank

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def open_in(self) -> typing.Optional[GitpodOpenIn]:
        '''(experimental) You can configure where in the IDE the terminal should be opened.

        :default: GitpodOpenIn.BOTTOM

        :stability: experimental
        '''
        result = self._values.get("open_in")
        return typing.cast(typing.Optional[GitpodOpenIn], result)

    @builtins.property
    def open_mode(self) -> typing.Optional[GitpodOpenMode]:
        '''(experimental) You can configure how the terminal should be opened relative to the previous task.

        :default: GitpodOpenMode.TAB_AFTER

        :stability: experimental
        '''
        result = self._values.get("open_mode")
        return typing.cast(typing.Optional[GitpodOpenMode], result)

    @builtins.property
    def prebuild(self) -> typing.Optional[builtins.str]:
        '''(experimental) The optional prebuild command will be executed during prebuilds.

        It is meant to run additional long running
        processes that could be useful, e.g. running test suites.

        :stability: experimental
        '''
        result = self._values.get("prebuild")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitpodTask(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="projen.IDevEnvironment")
class IDevEnvironment(typing_extensions.Protocol):
    '''(experimental) Abstract interface for container-based development environments, such as Gitpod and GitHub Codespaces.

    :stability: experimental
    '''

    @jsii.member(jsii_name="addDockerImage")
    def add_docker_image(self, image: DevEnvironmentDockerImage) -> None:
        '''(experimental) Add a custom Docker image or Dockerfile for the container.

        :param image: The Docker image.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="addPorts")
    def add_ports(self, *ports: builtins.str) -> None:
        '''(experimental) Adds ports that should be exposed (forwarded) from the container.

        :param ports: The new ports.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="addTasks")
    def add_tasks(self, *tasks: "Task") -> None:
        '''(experimental) Adds tasks to run when the container starts.

        :param tasks: The new tasks.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="addVscodeExtensions")
    def add_vscode_extensions(self, *extensions: builtins.str) -> None:
        '''(experimental) Adds a list of VSCode extensions that should be automatically installed in the container.

        :param extensions: The extension IDs.

        :stability: experimental
        '''
        ...


class _IDevEnvironmentProxy:
    '''(experimental) Abstract interface for container-based development environments, such as Gitpod and GitHub Codespaces.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "projen.IDevEnvironment"

    @jsii.member(jsii_name="addDockerImage")
    def add_docker_image(self, image: DevEnvironmentDockerImage) -> None:
        '''(experimental) Add a custom Docker image or Dockerfile for the container.

        :param image: The Docker image.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addDockerImage", [image]))

    @jsii.member(jsii_name="addPorts")
    def add_ports(self, *ports: builtins.str) -> None:
        '''(experimental) Adds ports that should be exposed (forwarded) from the container.

        :param ports: The new ports.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addPorts", [*ports]))

    @jsii.member(jsii_name="addTasks")
    def add_tasks(self, *tasks: "Task") -> None:
        '''(experimental) Adds tasks to run when the container starts.

        :param tasks: The new tasks.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addTasks", [*tasks]))

    @jsii.member(jsii_name="addVscodeExtensions")
    def add_vscode_extensions(self, *extensions: builtins.str) -> None:
        '''(experimental) Adds a list of VSCode extensions that should be automatically installed in the container.

        :param extensions: The extension IDs.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addVscodeExtensions", [*extensions]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDevEnvironment).__jsii_proxy_class__ = lambda : _IDevEnvironmentProxy


@jsii.interface(jsii_type="projen.IDockerComposeServiceName")
class IDockerComposeServiceName(typing_extensions.Protocol):
    '''(experimental) An interface providing the name of a docker compose service.

    :stability: experimental
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        '''(experimental) The name of the docker compose service.

        :stability: experimental
        '''
        ...


class _IDockerComposeServiceNameProxy:
    '''(experimental) An interface providing the name of a docker compose service.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "projen.IDockerComposeServiceName"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        '''(experimental) The name of the docker compose service.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDockerComposeServiceName).__jsii_proxy_class__ = lambda : _IDockerComposeServiceNameProxy


@jsii.interface(jsii_type="projen.IDockerComposeVolumeBinding")
class IDockerComposeVolumeBinding(typing_extensions.Protocol):
    '''(experimental) Volume binding information.

    :stability: experimental
    '''

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        volume_config: "IDockerComposeVolumeConfig",
    ) -> DockerComposeVolumeMount:
        '''(experimental) Binds the requested volume to the docker-compose volume configuration and provide mounting instructions for synthesis.

        :param volume_config: the volume configuration.

        :return: mounting instructions for the service.

        :stability: experimental
        '''
        ...


class _IDockerComposeVolumeBindingProxy:
    '''(experimental) Volume binding information.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "projen.IDockerComposeVolumeBinding"

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        volume_config: "IDockerComposeVolumeConfig",
    ) -> DockerComposeVolumeMount:
        '''(experimental) Binds the requested volume to the docker-compose volume configuration and provide mounting instructions for synthesis.

        :param volume_config: the volume configuration.

        :return: mounting instructions for the service.

        :stability: experimental
        '''
        return typing.cast(DockerComposeVolumeMount, jsii.invoke(self, "bind", [volume_config]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDockerComposeVolumeBinding).__jsii_proxy_class__ = lambda : _IDockerComposeVolumeBindingProxy


@jsii.interface(jsii_type="projen.IDockerComposeVolumeConfig")
class IDockerComposeVolumeConfig(typing_extensions.Protocol):
    '''(experimental) Storage for volume configuration.

    :stability: experimental
    '''

    @jsii.member(jsii_name="addVolumeConfiguration")
    def add_volume_configuration(
        self,
        volume_name: builtins.str,
        *,
        driver: typing.Optional[builtins.str] = None,
        driver_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        external: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Add volume configuration to the repository.

        :param volume_name: -
        :param driver: (experimental) Driver to use for the volume. Default: - value is not provided
        :param driver_opts: (experimental) Options to provide to the driver.
        :param external: (experimental) Set to true to indicate that the volume is externally created. Default: - unset, indicating that docker-compose creates the volume
        :param name: (experimental) Name of the volume for when the volume name isn't going to work in YAML. Default: - unset, indicating that docker-compose creates volumes as usual

        :stability: experimental
        '''
        ...


class _IDockerComposeVolumeConfigProxy:
    '''(experimental) Storage for volume configuration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "projen.IDockerComposeVolumeConfig"

    @jsii.member(jsii_name="addVolumeConfiguration")
    def add_volume_configuration(
        self,
        volume_name: builtins.str,
        *,
        driver: typing.Optional[builtins.str] = None,
        driver_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        external: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Add volume configuration to the repository.

        :param volume_name: -
        :param driver: (experimental) Driver to use for the volume. Default: - value is not provided
        :param driver_opts: (experimental) Options to provide to the driver.
        :param external: (experimental) Set to true to indicate that the volume is externally created. Default: - unset, indicating that docker-compose creates the volume
        :param name: (experimental) Name of the volume for when the volume name isn't going to work in YAML. Default: - unset, indicating that docker-compose creates volumes as usual

        :stability: experimental
        '''
        configuration = DockerComposeVolumeConfig(
            driver=driver, driver_opts=driver_opts, external=external, name=name
        )

        return typing.cast(None, jsii.invoke(self, "addVolumeConfiguration", [volume_name, configuration]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDockerComposeVolumeConfig).__jsii_proxy_class__ = lambda : _IDockerComposeVolumeConfigProxy


@jsii.interface(jsii_type="projen.IResolvable")
class IResolvable(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> typing.Any:
        '''(experimental) Resolves and returns content.

        :stability: experimental
        '''
        ...


class _IResolvableProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "projen.IResolvable"

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> typing.Any:
        '''(experimental) Resolves and returns content.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "toJSON", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResolvable).__jsii_proxy_class__ = lambda : _IResolvableProxy


@jsii.interface(jsii_type="projen.IResolver")
class IResolver(typing_extensions.Protocol):
    '''(experimental) API for resolving tokens when synthesizing file content.

    :stability: experimental
    '''

    @jsii.member(jsii_name="resolve")
    def resolve(
        self,
        value: typing.Any,
        *,
        args: typing.Optional[typing.Sequence[typing.Any]] = None,
        omit_empty: typing.Optional[builtins.bool] = None,
    ) -> typing.Any:
        '''(experimental) Given a value (object/string/array/whatever, looks up any functions inside the object and returns an object where all functions are called.

        :param value: The value to resolve.
        :param args: (experimental) Context arguments. Default: []
        :param omit_empty: (experimental) Omits empty arrays and objects. Default: false

        :stability: experimental
        :package: options Resolve options
        '''
        ...


class _IResolverProxy:
    '''(experimental) API for resolving tokens when synthesizing file content.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "projen.IResolver"

    @jsii.member(jsii_name="resolve")
    def resolve(
        self,
        value: typing.Any,
        *,
        args: typing.Optional[typing.Sequence[typing.Any]] = None,
        omit_empty: typing.Optional[builtins.bool] = None,
    ) -> typing.Any:
        '''(experimental) Given a value (object/string/array/whatever, looks up any functions inside the object and returns an object where all functions are called.

        :param value: The value to resolve.
        :param args: (experimental) Context arguments. Default: []
        :param omit_empty: (experimental) Omits empty arrays and objects. Default: false

        :stability: experimental
        :package: options Resolve options
        '''
        options = ResolveOptions(args=args, omit_empty=omit_empty)

        return typing.cast(typing.Any, jsii.invoke(self, "resolve", [value, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResolver).__jsii_proxy_class__ = lambda : _IResolverProxy


class IgnoreFile(FileBase, metaclass=jsii.JSIIMeta, jsii_type="projen.IgnoreFile"):
    '''
    :stability: experimental
    '''

    def __init__(self, project: "Project", file_path: builtins.str) -> None:
        '''
        :param project: -
        :param file_path: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [project, file_path])

    @jsii.member(jsii_name="addPatterns")
    def add_patterns(self, *patterns: builtins.str) -> None:
        '''(experimental) Add ignore patterns.

        Files that match this pattern will be ignored. If the
        pattern starts with a negation mark ``!``, files that match will *not* be
        ignored.

        Comment lines (start with ``#``) are ignored.

        :param patterns: Ignore patterns.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addPatterns", [*patterns]))

    @jsii.member(jsii_name="exclude")
    def exclude(self, *patterns: builtins.str) -> None:
        '''(experimental) Ignore the files that match these patterns.

        :param patterns: The patterns to match.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "exclude", [*patterns]))

    @jsii.member(jsii_name="include")
    def include(self, *patterns: builtins.str) -> None:
        '''(experimental) Always include the specified file patterns.

        :param patterns: Patterns to include in git commits.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "include", [*patterns]))

    @jsii.member(jsii_name="removePatterns")
    def remove_patterns(self, *patterns: builtins.str) -> None:
        '''(experimental) Removes patterns previously added from the ignore file.

        If ``addPattern()`` is called after this, the pattern will be added again.

        :param patterns: patters to remove.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "removePatterns", [*patterns]))

    @jsii.member(jsii_name="synthesizeContent")
    def _synthesize_content(self, resolver: IResolver) -> typing.Optional[builtins.str]:
        '''(experimental) Implemented by derived classes and returns the contents of the file to emit.

        :param resolver: -

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "synthesizeContent", [resolver]))


@jsii.data_type(
    jsii_type="projen.InitProject",
    jsii_struct_bases=[],
    name_mapping={
        "args": "args",
        "comments": "comments",
        "fqn": "fqn",
        "type": "type",
    },
)
class InitProject:
    def __init__(
        self,
        *,
        args: typing.Mapping[builtins.str, typing.Any],
        comments: "InitProjectOptionHints",
        fqn: builtins.str,
        type: "ProjectType",
    ) -> None:
        '''(experimental) Information passed from ``projen new`` to the project object when the project is first created.

        It is used to generate projenrc files in various languages.

        :param args: (experimental) Initial arguments passed to ``projen new``.
        :param comments: (experimental) Include commented out options. Does not apply to projenrc.json files. Default: InitProjectOptionHints.FEATURED
        :param fqn: (experimental) The JSII FQN of the project type.
        :param type: (experimental) Project metadata.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "args": args,
            "comments": comments,
            "fqn": fqn,
            "type": type,
        }

    @builtins.property
    def args(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''(experimental) Initial arguments passed to ``projen new``.

        :stability: experimental
        '''
        result = self._values.get("args")
        assert result is not None, "Required property 'args' is missing"
        return typing.cast(typing.Mapping[builtins.str, typing.Any], result)

    @builtins.property
    def comments(self) -> "InitProjectOptionHints":
        '''(experimental) Include commented out options.

        Does not apply to projenrc.json files.

        :default: InitProjectOptionHints.FEATURED

        :stability: experimental
        '''
        result = self._values.get("comments")
        assert result is not None, "Required property 'comments' is missing"
        return typing.cast("InitProjectOptionHints", result)

    @builtins.property
    def fqn(self) -> builtins.str:
        '''(experimental) The JSII FQN of the project type.

        :stability: experimental
        '''
        result = self._values.get("fqn")
        assert result is not None, "Required property 'fqn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> "ProjectType":
        '''(experimental) Project metadata.

        :stability: experimental
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("ProjectType", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InitProject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="projen.InitProjectOptionHints")
class InitProjectOptionHints(enum.Enum):
    '''(experimental) Choices for how to display commented out options in projenrc files.

    Does not apply to projenrc.json files.

    :stability: experimental
    '''

    ALL = "ALL"
    '''(experimental) Display all possible options (grouped by which interface they belong to).

    :stability: experimental
    '''
    FEATURED = "FEATURED"
    '''(experimental) Display only featured options, in alphabetical order.

    :stability: experimental
    '''
    NONE = "NONE"
    '''(experimental) Display no extra options.

    :stability: experimental
    '''


class License(FileBase, metaclass=jsii.JSIIMeta, jsii_type="projen.License"):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        project: "Project",
        *,
        spdx: builtins.str,
        copyright_owner: typing.Optional[builtins.str] = None,
        copyright_period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param project: -
        :param spdx: (experimental) License type (SPDX).
        :param copyright_owner: (experimental) Copyright owner. If the license text has $copyright_owner, this option must be specified. Default: -
        :param copyright_period: (experimental) Period of license (e.g. "1998-2023"). The string ``$copyright_period`` will be substituted with this string. Default: - current year (e.g. "2020")

        :stability: experimental
        '''
        options = LicenseOptions(
            spdx=spdx,
            copyright_owner=copyright_owner,
            copyright_period=copyright_period,
        )

        jsii.create(self.__class__, self, [project, options])

    @jsii.member(jsii_name="synthesizeContent")
    def _synthesize_content(self, _: IResolver) -> typing.Optional[builtins.str]:
        '''(experimental) Implemented by derived classes and returns the contents of the file to emit.

        :param _: -

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "synthesizeContent", [_]))


@jsii.data_type(
    jsii_type="projen.LicenseOptions",
    jsii_struct_bases=[],
    name_mapping={
        "spdx": "spdx",
        "copyright_owner": "copyrightOwner",
        "copyright_period": "copyrightPeriod",
    },
)
class LicenseOptions:
    def __init__(
        self,
        *,
        spdx: builtins.str,
        copyright_owner: typing.Optional[builtins.str] = None,
        copyright_period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param spdx: (experimental) License type (SPDX).
        :param copyright_owner: (experimental) Copyright owner. If the license text has $copyright_owner, this option must be specified. Default: -
        :param copyright_period: (experimental) Period of license (e.g. "1998-2023"). The string ``$copyright_period`` will be substituted with this string. Default: - current year (e.g. "2020")

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "spdx": spdx,
        }
        if copyright_owner is not None:
            self._values["copyright_owner"] = copyright_owner
        if copyright_period is not None:
            self._values["copyright_period"] = copyright_period

    @builtins.property
    def spdx(self) -> builtins.str:
        '''(experimental) License type (SPDX).

        :see: https://github.com/projen/projen/tree/main/license-text for list of supported licenses
        :stability: experimental
        '''
        result = self._values.get("spdx")
        assert result is not None, "Required property 'spdx' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def copyright_owner(self) -> typing.Optional[builtins.str]:
        '''(experimental) Copyright owner.

        If the license text has $copyright_owner, this option must be specified.

        :default: -

        :stability: experimental
        '''
        result = self._values.get("copyright_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def copyright_period(self) -> typing.Optional[builtins.str]:
        '''(experimental) Period of license (e.g. "1998-2023").

        The string ``$copyright_period`` will be substituted with this string.

        :default: - current year (e.g. "2020")

        :stability: experimental
        '''
        result = self._values.get("copyright_period")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LicenseOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="projen.LogLevel")
class LogLevel(enum.Enum):
    '''(experimental) Logging verbosity.

    :stability: experimental
    '''

    OFF = "OFF"
    '''
    :stability: experimental
    '''
    ERROR = "ERROR"
    '''
    :stability: experimental
    '''
    WARN = "WARN"
    '''
    :stability: experimental
    '''
    INFO = "INFO"
    '''
    :stability: experimental
    '''
    DEBUG = "DEBUG"
    '''
    :stability: experimental
    '''
    VERBOSE = "VERBOSE"
    '''
    :stability: experimental
    '''


class Logger(Component, metaclass=jsii.JSIIMeta, jsii_type="projen.Logger"):
    '''(experimental) Project-level logging utilities.

    :stability: experimental
    '''

    def __init__(
        self,
        project: "Project",
        *,
        level: typing.Optional[LogLevel] = None,
        use_prefix: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param project: -
        :param level: (experimental) The logging verbosity. The levels available (in increasing verbosity) are OFF, ERROR, WARN, INFO, DEBUG, and VERBOSE. Default: LogLevel.INFO
        :param use_prefix: (experimental) Include a prefix for all logging messages with the project name. Default: false

        :stability: experimental
        '''
        options = LoggerOptions(level=level, use_prefix=use_prefix)

        jsii.create(self.__class__, self, [project, options])

    @jsii.member(jsii_name="debug")
    def debug(self, *text: typing.Any) -> None:
        '''(experimental) Log a message to stderr with DEBUG severity.

        :param text: strings or objects to print.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "debug", [*text]))

    @jsii.member(jsii_name="error")
    def error(self, *text: typing.Any) -> None:
        '''(experimental) Log a message to stderr with ERROR severity.

        :param text: strings or objects to print.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "error", [*text]))

    @jsii.member(jsii_name="info")
    def info(self, *text: typing.Any) -> None:
        '''(experimental) Log a message to stderr with INFO severity.

        :param text: strings or objects to print.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "info", [*text]))

    @jsii.member(jsii_name="log")
    def log(self, level: LogLevel, *text: typing.Any) -> None:
        '''(experimental) Log a message to stderr with a given logging level.

        The message will be
        printed as long as ``logger.level`` is set to the message's severity or higher.

        :param level: Logging verbosity.
        :param text: strings or objects to print.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "log", [level, *text]))

    @jsii.member(jsii_name="verbose")
    def verbose(self, *text: typing.Any) -> None:
        '''(experimental) Log a message to stderr with VERBOSE severity.

        :param text: strings or objects to print.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "verbose", [*text]))

    @jsii.member(jsii_name="warn")
    def warn(self, *text: typing.Any) -> None:
        '''(experimental) Log a message to stderr with WARN severity.

        :param text: strings or objects to print.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "warn", [*text]))


@jsii.data_type(
    jsii_type="projen.LoggerOptions",
    jsii_struct_bases=[],
    name_mapping={"level": "level", "use_prefix": "usePrefix"},
)
class LoggerOptions:
    def __init__(
        self,
        *,
        level: typing.Optional[LogLevel] = None,
        use_prefix: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Options for logging utilities.

        :param level: (experimental) The logging verbosity. The levels available (in increasing verbosity) are OFF, ERROR, WARN, INFO, DEBUG, and VERBOSE. Default: LogLevel.INFO
        :param use_prefix: (experimental) Include a prefix for all logging messages with the project name. Default: false

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if level is not None:
            self._values["level"] = level
        if use_prefix is not None:
            self._values["use_prefix"] = use_prefix

    @builtins.property
    def level(self) -> typing.Optional[LogLevel]:
        '''(experimental) The logging verbosity.

        The levels available (in increasing verbosity) are
        OFF, ERROR, WARN, INFO, DEBUG, and VERBOSE.

        :default: LogLevel.INFO

        :stability: experimental
        '''
        result = self._values.get("level")
        return typing.cast(typing.Optional[LogLevel], result)

    @builtins.property
    def use_prefix(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Include a prefix for all logging messages with the project name.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("use_prefix")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Makefile(FileBase, metaclass=jsii.JSIIMeta, jsii_type="projen.Makefile"):
    '''(experimental) Minimal Makefile.

    :stability: experimental
    '''

    def __init__(
        self,
        project: "Project",
        file_path: builtins.str,
        *,
        all: typing.Optional[typing.Sequence[builtins.str]] = None,
        rules: typing.Optional[typing.Sequence["Rule"]] = None,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param project: -
        :param file_path: -
        :param all: (experimental) List of targets to build when Make is invoked without specifying any targets. Default: []
        :param rules: (experimental) Rules to include in the Makefile. Default: []
        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true

        :stability: experimental
        '''
        options = MakefileOptions(
            all=all,
            rules=rules,
            committed=committed,
            edit_gitignore=edit_gitignore,
            executable=executable,
            marker=marker,
            readonly=readonly,
        )

        jsii.create(self.__class__, self, [project, file_path, options])

    @jsii.member(jsii_name="addAll")
    def add_all(self, target: builtins.str) -> "Makefile":
        '''(experimental) Add a target to all.

        :param target: -

        :stability: experimental
        '''
        return typing.cast("Makefile", jsii.invoke(self, "addAll", [target]))

    @jsii.member(jsii_name="addAlls")
    def add_alls(self, *targets: builtins.str) -> "Makefile":
        '''(experimental) Add multiple targets to all.

        :param targets: -

        :stability: experimental
        '''
        return typing.cast("Makefile", jsii.invoke(self, "addAlls", [*targets]))

    @jsii.member(jsii_name="addRule")
    def add_rule(
        self,
        *,
        targets: typing.Sequence[builtins.str],
        phony: typing.Optional[builtins.bool] = None,
        prerequisites: typing.Optional[typing.Sequence[builtins.str]] = None,
        recipe: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> "Makefile":
        '''(experimental) Add a rule to the Makefile.

        :param targets: (experimental) Files to be created or updated by this rule. If the rule is phony then instead this represents the command's name(s).
        :param phony: (experimental) Marks whether the target is phony. Default: false
        :param prerequisites: (experimental) Files that are used as inputs to create a target. Default: []
        :param recipe: (experimental) Commands that are run (using prerequisites as inputs) to create a target. Default: []

        :stability: experimental
        '''
        rule = Rule(
            targets=targets, phony=phony, prerequisites=prerequisites, recipe=recipe
        )

        return typing.cast("Makefile", jsii.invoke(self, "addRule", [rule]))

    @jsii.member(jsii_name="addRules")
    def add_rules(self, *rules: "Rule") -> "Makefile":
        '''(experimental) Add multiple rules to the Makefile.

        :param rules: -

        :stability: experimental
        '''
        return typing.cast("Makefile", jsii.invoke(self, "addRules", [*rules]))

    @jsii.member(jsii_name="synthesizeContent")
    def _synthesize_content(self, resolver: IResolver) -> typing.Optional[builtins.str]:
        '''(experimental) Implemented by derived classes and returns the contents of the file to emit.

        :param resolver: -

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "synthesizeContent", [resolver]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rules")
    def rules(self) -> typing.List["Rule"]:
        '''(experimental) List of rule definitions.

        :stability: experimental
        '''
        return typing.cast(typing.List["Rule"], jsii.get(self, "rules"))


@jsii.data_type(
    jsii_type="projen.MakefileOptions",
    jsii_struct_bases=[FileBaseOptions],
    name_mapping={
        "committed": "committed",
        "edit_gitignore": "editGitignore",
        "executable": "executable",
        "marker": "marker",
        "readonly": "readonly",
        "all": "all",
        "rules": "rules",
    },
)
class MakefileOptions(FileBaseOptions):
    def __init__(
        self,
        *,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
        all: typing.Optional[typing.Sequence[builtins.str]] = None,
        rules: typing.Optional[typing.Sequence["Rule"]] = None,
    ) -> None:
        '''(experimental) Options for Makefiles.

        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true
        :param all: (experimental) List of targets to build when Make is invoked without specifying any targets. Default: []
        :param rules: (experimental) Rules to include in the Makefile. Default: []

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if committed is not None:
            self._values["committed"] = committed
        if edit_gitignore is not None:
            self._values["edit_gitignore"] = edit_gitignore
        if executable is not None:
            self._values["executable"] = executable
        if marker is not None:
            self._values["marker"] = marker
        if readonly is not None:
            self._values["readonly"] = readonly
        if all is not None:
            self._values["all"] = all
        if rules is not None:
            self._values["rules"] = rules

    @builtins.property
    def committed(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether this file should be committed to git or ignored.

        By
        default, all generated files are committed and anti-tamper is used to
        protect against manual modifications.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("committed")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def edit_gitignore(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Update the project's .gitignore file.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("edit_gitignore")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def executable(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be marked as executable.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("executable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def marker(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Adds the projen marker to the file.

        :default: - marker will be included as long as the project is not ejected

        :stability: experimental
        '''
        result = self._values.get("marker")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def readonly(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be readonly.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("readonly")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def all(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) List of targets to build when Make is invoked without specifying any targets.

        :default: []

        :stability: experimental
        '''
        result = self._values.get("all")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.List["Rule"]]:
        '''(experimental) Rules to include in the Makefile.

        :default: []

        :stability: experimental
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.List["Rule"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MakefileOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ObjectFile(
    FileBase,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="projen.ObjectFile",
):
    '''(experimental) Represents an Object file.

    :stability: experimental
    '''

    def __init__(
        self,
        project: "Project",
        file_path: builtins.str,
        *,
        obj: typing.Any = None,
        omit_empty: typing.Optional[builtins.bool] = None,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param project: -
        :param file_path: -
        :param obj: (experimental) The object that will be serialized. You can modify the object's contents before synthesis. Default: {} an empty object (use ``file.obj`` to mutate).
        :param omit_empty: (experimental) Omits empty objects and arrays. Default: false
        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true

        :stability: experimental
        '''
        options = ObjectFileOptions(
            obj=obj,
            omit_empty=omit_empty,
            committed=committed,
            edit_gitignore=edit_gitignore,
            executable=executable,
            marker=marker,
            readonly=readonly,
        )

        jsii.create(self.__class__, self, [project, file_path, options])

    @jsii.member(jsii_name="addDeletionOverride")
    def add_deletion_override(self, path: builtins.str) -> None:
        '''(experimental) Syntactic sugar for ``addOverride(path, undefined)``.

        :param path: The path of the value to delete.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addDeletionOverride", [path]))

    @jsii.member(jsii_name="addOverride")
    def add_override(self, path: builtins.str, value: typing.Any) -> None:
        '''(experimental) Adds an override to the synthesized object file.

        If the override is nested, separate each nested level using a dot (.) in the path parameter.
        If there is an array as part of the nesting, specify the index in the path.

        To include a literal ``.`` in the property name, prefix with a ``\\``. In most
        programming languages you will need to write this as ``"\\\\."`` because the
        ``\\`` itself will need to be escaped.

        For example::

           project.tsconfig.file.addOverride('compilerOptions.alwaysStrict', true);
           project.tsconfig.file.addOverride('compilerOptions.lib', ['dom', 'dom.iterable', 'esnext']);

        would add the overrides Example::

           "compilerOptions": {
              "alwaysStrict": true,
              "lib": [
                "dom",
                "dom.iterable",
                "esnext"
              ]
              ...
           }
           ...

        :param path: - The path of the property, you can use dot notation to override values in complex types. Any intermediate keys will be created as needed.
        :param value: - The value. Could be primitive or complex.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addOverride", [path, value]))

    @jsii.member(jsii_name="synthesizeContent")
    def _synthesize_content(self, resolver: IResolver) -> typing.Optional[builtins.str]:
        '''(experimental) Implemented by derived classes and returns the contents of the file to emit.

        :param resolver: -

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "synthesizeContent", [resolver]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="omitEmpty")
    def omit_empty(self) -> builtins.bool:
        '''(experimental) Indicates if empty objects and arrays are omitted from the output object.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "omitEmpty"))


class _ObjectFileProxy(
    ObjectFile, jsii.proxy_for(FileBase) # type: ignore[misc]
):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, ObjectFile).__jsii_proxy_class__ = lambda : _ObjectFileProxy


@jsii.data_type(
    jsii_type="projen.ObjectFileOptions",
    jsii_struct_bases=[FileBaseOptions],
    name_mapping={
        "committed": "committed",
        "edit_gitignore": "editGitignore",
        "executable": "executable",
        "marker": "marker",
        "readonly": "readonly",
        "obj": "obj",
        "omit_empty": "omitEmpty",
    },
)
class ObjectFileOptions(FileBaseOptions):
    def __init__(
        self,
        *,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
        obj: typing.Any = None,
        omit_empty: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Options for ``ObjectFile``.

        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true
        :param obj: (experimental) The object that will be serialized. You can modify the object's contents before synthesis. Default: {} an empty object (use ``file.obj`` to mutate).
        :param omit_empty: (experimental) Omits empty objects and arrays. Default: false

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if committed is not None:
            self._values["committed"] = committed
        if edit_gitignore is not None:
            self._values["edit_gitignore"] = edit_gitignore
        if executable is not None:
            self._values["executable"] = executable
        if marker is not None:
            self._values["marker"] = marker
        if readonly is not None:
            self._values["readonly"] = readonly
        if obj is not None:
            self._values["obj"] = obj
        if omit_empty is not None:
            self._values["omit_empty"] = omit_empty

    @builtins.property
    def committed(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether this file should be committed to git or ignored.

        By
        default, all generated files are committed and anti-tamper is used to
        protect against manual modifications.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("committed")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def edit_gitignore(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Update the project's .gitignore file.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("edit_gitignore")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def executable(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be marked as executable.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("executable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def marker(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Adds the projen marker to the file.

        :default: - marker will be included as long as the project is not ejected

        :stability: experimental
        '''
        result = self._values.get("marker")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def readonly(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be readonly.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("readonly")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def obj(self) -> typing.Any:
        '''(experimental) The object that will be serialized.

        You can modify the object's contents
        before synthesis.

        :default: {} an empty object (use ``file.obj`` to mutate).

        :stability: experimental
        '''
        result = self._values.get("obj")
        return typing.cast(typing.Any, result)

    @builtins.property
    def omit_empty(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Omits empty objects and arrays.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("omit_empty")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ObjectFileOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Project(metaclass=jsii.JSIIMeta, jsii_type="projen.Project"):
    '''(experimental) Base project.

    :stability: experimental
    '''

    def __init__(
        self,
        *,
        name: builtins.str,
        logging: typing.Optional[LoggerOptions] = None,
        outdir: typing.Optional[builtins.str] = None,
        parent: typing.Optional["Project"] = None,
        projen_command: typing.Optional[builtins.str] = None,
        projenrc_json: typing.Optional[builtins.bool] = None,
        projenrc_json_options: typing.Optional["ProjenrcOptions"] = None,
        renovatebot: typing.Optional[builtins.bool] = None,
        renovatebot_options: typing.Optional["RenovatebotOptions"] = None,
    ) -> None:
        '''
        :param name: (experimental) This is the name of your project. Default: $BASEDIR
        :param logging: (experimental) Configure logging options such as verbosity. Default: {}
        :param outdir: (experimental) The root directory of the project. Relative to this directory, all files are synthesized. If this project has a parent, this directory is relative to the parent directory and it cannot be the same as the parent or any of it's other sub-projects. Default: "."
        :param parent: (experimental) The parent project, if this project is part of a bigger project.
        :param projen_command: (experimental) The shell command to use in order to run the projen CLI. Can be used to customize in special environments. Default: "npx projen"
        :param projenrc_json: (experimental) Generate (once) .projenrc.json (in JSON). Set to ``false`` in order to disable .projenrc.json generation. Default: false
        :param projenrc_json_options: (experimental) Options for .projenrc.json. Default: - default options
        :param renovatebot: (experimental) Use renovatebot to handle dependency upgrades. Default: false
        :param renovatebot_options: (experimental) Options for renovatebot. Default: - default options

        :stability: experimental
        '''
        options = ProjectOptions(
            name=name,
            logging=logging,
            outdir=outdir,
            parent=parent,
            projen_command=projen_command,
            projenrc_json=projenrc_json,
            projenrc_json_options=projenrc_json_options,
            renovatebot=renovatebot,
            renovatebot_options=renovatebot_options,
        )

        jsii.create(self.__class__, self, [options])

    @jsii.member(jsii_name="addExcludeFromCleanup")
    def add_exclude_from_cleanup(self, *globs: builtins.str) -> None:
        '''(experimental) Exclude the matching files from pre-synth cleanup.

        Can be used when, for example, some
        source files include the projen marker and we don't want them to be erased during synth.

        :param globs: The glob patterns to match.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addExcludeFromCleanup", [*globs]))

    @jsii.member(jsii_name="addGitIgnore")
    def add_git_ignore(self, pattern: builtins.str) -> None:
        '''(experimental) Adds a .gitignore pattern.

        :param pattern: The glob pattern to ignore.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addGitIgnore", [pattern]))

    @jsii.member(jsii_name="addPackageIgnore")
    def add_package_ignore(self, _pattern: builtins.str) -> None:
        '''(experimental) Exclude these files from the bundled package.

        Implemented by project types based on the
        packaging mechanism. For example, ``NodeProject`` delegates this to ``.npmignore``.

        :param _pattern: The glob pattern to exclude.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addPackageIgnore", [_pattern]))

    @jsii.member(jsii_name="addTask")
    def add_task(
        self,
        name: builtins.str,
        *,
        exec: typing.Optional[builtins.str] = None,
        steps: typing.Optional[typing.Sequence["TaskStep"]] = None,
        condition: typing.Optional[builtins.str] = None,
        cwd: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        required_env: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> "Task":
        '''(experimental) Adds a new task to this project.

        This will fail if the project already has
        a task with this name.

        :param name: The task name to add.
        :param exec: (experimental) Shell command to execute as the first command of the task. Default: - add steps using ``task.exec(command)`` or ``task.spawn(subtask)``
        :param steps: (experimental) List of task steps to run.
        :param condition: (experimental) A shell command which determines if the this task should be executed. If the program exits with a zero exit code, steps will be executed. A non-zero code means that task will be skipped.
        :param cwd: (experimental) The working directory for all steps in this task (unless overridden by the step). Default: - process.cwd()
        :param description: (experimental) The description of this build command. Default: - the task name
        :param env: (experimental) Defines environment variables for the execution of this task. Values in this map will be evaluated in a shell, so you can do stuff like ``$(echo "foo")``. Default: {}
        :param required_env: (experimental) A set of environment variables that must be defined in order to execute this task. Task execution will fail if one of these is not defined.

        :stability: experimental
        '''
        props = TaskOptions(
            exec=exec,
            steps=steps,
            condition=condition,
            cwd=cwd,
            description=description,
            env=env,
            required_env=required_env,
        )

        return typing.cast("Task", jsii.invoke(self, "addTask", [name, props]))

    @jsii.member(jsii_name="addTip")
    def add_tip(self, message: builtins.str) -> None:
        '''(deprecated) Prints a "tip" message during synthesis.

        :param message: The message.

        :deprecated: - use ``project.logger.info(message)`` to show messages during synthesis

        :stability: deprecated
        '''
        return typing.cast(None, jsii.invoke(self, "addTip", [message]))

    @jsii.member(jsii_name="annotateGenerated")
    def annotate_generated(self, _glob: builtins.str) -> None:
        '''(experimental) Consider a set of files as "generated".

        This method is implemented by
        derived classes and used for example, to add git attributes to tell GitHub
        that certain files are generated.

        :param _glob: the glob pattern to match (could be a file path).

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "annotateGenerated", [_glob]))

    @jsii.member(jsii_name="postSynthesize")
    def post_synthesize(self) -> None:
        '''(experimental) Called after all components are synthesized.

        Order is *not* guaranteed.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "postSynthesize", []))

    @jsii.member(jsii_name="preSynthesize")
    def pre_synthesize(self) -> None:
        '''(experimental) Called before all components are synthesized.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "preSynthesize", []))

    @jsii.member(jsii_name="removeTask")
    def remove_task(self, name: builtins.str) -> typing.Optional["Task"]:
        '''(experimental) Removes a task from a project.

        :param name: The name of the task to remove.

        :return: The ``Task`` that was removed, otherwise ``undefined``.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["Task"], jsii.invoke(self, "removeTask", [name]))

    @jsii.member(jsii_name="runTaskCommand")
    def run_task_command(self, task: "Task") -> builtins.str:
        '''(experimental) Returns the shell command to execute in order to run a task.

        By default, this is ``npx projen@<version> <task>``

        :param task: The task for which the command is required.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "runTaskCommand", [task]))

    @jsii.member(jsii_name="synth")
    def synth(self) -> None:
        '''(experimental) Synthesize all project files into ``outdir``.

        1. Call "this.preSynthesize()"
        2. Delete all generated files
        3. Synthesize all sub-projects
        4. Synthesize all components of this project
        5. Call "postSynthesize()" for all components of this project
        6. Call "this.postSynthesize()"

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "synth", []))

    @jsii.member(jsii_name="tryFindFile")
    def try_find_file(self, file_path: builtins.str) -> typing.Optional[FileBase]:
        '''(experimental) Finds a file at the specified relative path within this project and all its subprojects.

        :param file_path: The file path. If this path is relative, it will be resolved from the root of *this* project.

        :return: a ``FileBase`` or undefined if there is no file in that path

        :stability: experimental
        '''
        return typing.cast(typing.Optional[FileBase], jsii.invoke(self, "tryFindFile", [file_path]))

    @jsii.member(jsii_name="tryFindJsonFile")
    def try_find_json_file(
        self,
        file_path: builtins.str,
    ) -> typing.Optional["JsonFile"]:
        '''(deprecated) Finds a json file by name.

        :param file_path: The file path.

        :deprecated: use ``tryFindObjectFile``

        :stability: deprecated
        '''
        return typing.cast(typing.Optional["JsonFile"], jsii.invoke(self, "tryFindJsonFile", [file_path]))

    @jsii.member(jsii_name="tryFindObjectFile")
    def try_find_object_file(
        self,
        file_path: builtins.str,
    ) -> typing.Optional[ObjectFile]:
        '''(experimental) Finds an object file (like JsonFile, YamlFile, etc.) by name.

        :param file_path: The file path.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[ObjectFile], jsii.invoke(self, "tryFindObjectFile", [file_path]))

    @jsii.member(jsii_name="tryRemoveFile")
    def try_remove_file(self, file_path: builtins.str) -> typing.Optional[FileBase]:
        '''(experimental) Finds a file at the specified relative path within this project and removes it.

        :param file_path: The file path. If this path is relative, it will be resolved from the root of *this* project.

        :return:

        a ``FileBase`` if the file was found and removed, or undefined if
        the file was not found.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[FileBase], jsii.invoke(self, "tryRemoveFile", [file_path]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="DEFAULT_TASK")
    def DEFAULT_TASK(cls) -> builtins.str:
        '''(experimental) The name of the default task (the task executed when ``projen`` is run without arguments).

        Normally
        this task should synthesize the project files.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DEFAULT_TASK"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="buildTask")
    def build_task(self) -> "Task":
        '''
        :stability: experimental
        '''
        return typing.cast("Task", jsii.get(self, "buildTask"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="compileTask")
    def compile_task(self) -> "Task":
        '''
        :stability: experimental
        '''
        return typing.cast("Task", jsii.get(self, "compileTask"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="components")
    def components(self) -> typing.List[Component]:
        '''(experimental) Returns all the components within this project.

        :stability: experimental
        '''
        return typing.cast(typing.List[Component], jsii.get(self, "components"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deps")
    def deps(self) -> Dependencies:
        '''(experimental) Project dependencies.

        :stability: experimental
        '''
        return typing.cast(Dependencies, jsii.get(self, "deps"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ejected")
    def ejected(self) -> builtins.bool:
        '''(experimental) Whether or not the project is being ejected.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "ejected"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="files")
    def files(self) -> typing.List[FileBase]:
        '''(experimental) All files in this project.

        :stability: experimental
        '''
        return typing.cast(typing.List[FileBase], jsii.get(self, "files"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="gitattributes")
    def gitattributes(self) -> GitAttributesFile:
        '''(experimental) The .gitattributes file for this repository.

        :stability: experimental
        '''
        return typing.cast(GitAttributesFile, jsii.get(self, "gitattributes"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="gitignore")
    def gitignore(self) -> IgnoreFile:
        '''(experimental) .gitignore.

        :stability: experimental
        '''
        return typing.cast(IgnoreFile, jsii.get(self, "gitignore"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logger")
    def logger(self) -> Logger:
        '''(experimental) Logging utilities.

        :stability: experimental
        '''
        return typing.cast(Logger, jsii.get(self, "logger"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''(experimental) Project name.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outdir")
    def outdir(self) -> builtins.str:
        '''(experimental) Absolute output directory of this project.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "outdir"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="packageTask")
    def package_task(self) -> "Task":
        '''
        :stability: experimental
        '''
        return typing.cast("Task", jsii.get(self, "packageTask"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="postCompileTask")
    def post_compile_task(self) -> "Task":
        '''
        :stability: experimental
        '''
        return typing.cast("Task", jsii.get(self, "postCompileTask"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="preCompileTask")
    def pre_compile_task(self) -> "Task":
        '''
        :stability: experimental
        '''
        return typing.cast("Task", jsii.get(self, "preCompileTask"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="projectBuild")
    def project_build(self) -> "ProjectBuild":
        '''(experimental) Manages the build process of the project.

        :stability: experimental
        '''
        return typing.cast("ProjectBuild", jsii.get(self, "projectBuild"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="projenCommand")
    def projen_command(self) -> builtins.str:
        '''(experimental) The command to use in order to run the projen CLI.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "projenCommand"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="root")
    def root(self) -> "Project":
        '''(experimental) The root project.

        :stability: experimental
        '''
        return typing.cast("Project", jsii.get(self, "root"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tasks")
    def tasks(self) -> "Tasks":
        '''(experimental) Project tasks.

        :stability: experimental
        '''
        return typing.cast("Tasks", jsii.get(self, "tasks"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="testTask")
    def test_task(self) -> "Task":
        '''
        :stability: experimental
        '''
        return typing.cast("Task", jsii.get(self, "testTask"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultTask")
    def default_task(self) -> typing.Optional["Task"]:
        '''(experimental) This is the "default" task, the one that executes "projen".

        Undefined if
        the project is being ejected.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["Task"], jsii.get(self, "defaultTask"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="initProject")
    def init_project(self) -> typing.Optional[InitProject]:
        '''(experimental) The options used when this project is bootstrapped via ``projen new``.

        It
        includes the original set of options passed to the CLI and also the JSII
        FQN of the project type.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[InitProject], jsii.get(self, "initProject"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parent")
    def parent(self) -> typing.Optional["Project"]:
        '''(experimental) A parent project.

        If undefined, this is the root project.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["Project"], jsii.get(self, "parent"))


class ProjectBuild(Component, metaclass=jsii.JSIIMeta, jsii_type="projen.ProjectBuild"):
    '''(experimental) Manages a standard build process for all projects.

    Build spawns these tasks in order:

    1. default
    2. pre-compile
    3. compile
    4. post-compile
    5. test
    6. package

    :stability: experimental
    '''

    def __init__(self, project: Project) -> None:
        '''
        :param project: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [project])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="buildTask")
    def build_task(self) -> "Task":
        '''(experimental) The task responsible for a full release build.

        :stability: experimental
        '''
        return typing.cast("Task", jsii.get(self, "buildTask"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="compileTask")
    def compile_task(self) -> "Task":
        '''(experimental) Compiles the code.

        By default for node.js projects this task is empty.

        :stability: experimental
        '''
        return typing.cast("Task", jsii.get(self, "compileTask"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="packageTask")
    def package_task(self) -> "Task":
        '''(experimental) The "package" task.

        :stability: experimental
        '''
        return typing.cast("Task", jsii.get(self, "packageTask"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="postCompileTask")
    def post_compile_task(self) -> "Task":
        '''(experimental) Post-compile task.

        :stability: experimental
        '''
        return typing.cast("Task", jsii.get(self, "postCompileTask"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="preCompileTask")
    def pre_compile_task(self) -> "Task":
        '''(experimental) Pre-compile task.

        :stability: experimental
        '''
        return typing.cast("Task", jsii.get(self, "preCompileTask"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="testTask")
    def test_task(self) -> "Task":
        '''(experimental) Tests the code.

        :stability: experimental
        '''
        return typing.cast("Task", jsii.get(self, "testTask"))


@jsii.data_type(
    jsii_type="projen.ProjectOptions",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "logging": "logging",
        "outdir": "outdir",
        "parent": "parent",
        "projen_command": "projenCommand",
        "projenrc_json": "projenrcJson",
        "projenrc_json_options": "projenrcJsonOptions",
        "renovatebot": "renovatebot",
        "renovatebot_options": "renovatebotOptions",
    },
)
class ProjectOptions:
    def __init__(
        self,
        *,
        name: builtins.str,
        logging: typing.Optional[LoggerOptions] = None,
        outdir: typing.Optional[builtins.str] = None,
        parent: typing.Optional[Project] = None,
        projen_command: typing.Optional[builtins.str] = None,
        projenrc_json: typing.Optional[builtins.bool] = None,
        projenrc_json_options: typing.Optional["ProjenrcOptions"] = None,
        renovatebot: typing.Optional[builtins.bool] = None,
        renovatebot_options: typing.Optional["RenovatebotOptions"] = None,
    ) -> None:
        '''(experimental) Options for ``Project``.

        :param name: (experimental) This is the name of your project. Default: $BASEDIR
        :param logging: (experimental) Configure logging options such as verbosity. Default: {}
        :param outdir: (experimental) The root directory of the project. Relative to this directory, all files are synthesized. If this project has a parent, this directory is relative to the parent directory and it cannot be the same as the parent or any of it's other sub-projects. Default: "."
        :param parent: (experimental) The parent project, if this project is part of a bigger project.
        :param projen_command: (experimental) The shell command to use in order to run the projen CLI. Can be used to customize in special environments. Default: "npx projen"
        :param projenrc_json: (experimental) Generate (once) .projenrc.json (in JSON). Set to ``false`` in order to disable .projenrc.json generation. Default: false
        :param projenrc_json_options: (experimental) Options for .projenrc.json. Default: - default options
        :param renovatebot: (experimental) Use renovatebot to handle dependency upgrades. Default: false
        :param renovatebot_options: (experimental) Options for renovatebot. Default: - default options

        :stability: experimental
        '''
        if isinstance(logging, dict):
            logging = LoggerOptions(**logging)
        if isinstance(projenrc_json_options, dict):
            projenrc_json_options = ProjenrcOptions(**projenrc_json_options)
        if isinstance(renovatebot_options, dict):
            renovatebot_options = RenovatebotOptions(**renovatebot_options)
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if logging is not None:
            self._values["logging"] = logging
        if outdir is not None:
            self._values["outdir"] = outdir
        if parent is not None:
            self._values["parent"] = parent
        if projen_command is not None:
            self._values["projen_command"] = projen_command
        if projenrc_json is not None:
            self._values["projenrc_json"] = projenrc_json
        if projenrc_json_options is not None:
            self._values["projenrc_json_options"] = projenrc_json_options
        if renovatebot is not None:
            self._values["renovatebot"] = renovatebot
        if renovatebot_options is not None:
            self._values["renovatebot_options"] = renovatebot_options

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) This is the name of your project.

        :default: $BASEDIR

        :stability: experimental
        :featured: true
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def logging(self) -> typing.Optional[LoggerOptions]:
        '''(experimental) Configure logging options such as verbosity.

        :default: {}

        :stability: experimental
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional[LoggerOptions], result)

    @builtins.property
    def outdir(self) -> typing.Optional[builtins.str]:
        '''(experimental) The root directory of the project.

        Relative to this directory, all files are synthesized.

        If this project has a parent, this directory is relative to the parent
        directory and it cannot be the same as the parent or any of it's other
        sub-projects.

        :default: "."

        :stability: experimental
        '''
        result = self._values.get("outdir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent(self) -> typing.Optional[Project]:
        '''(experimental) The parent project, if this project is part of a bigger project.

        :stability: experimental
        '''
        result = self._values.get("parent")
        return typing.cast(typing.Optional[Project], result)

    @builtins.property
    def projen_command(self) -> typing.Optional[builtins.str]:
        '''(experimental) The shell command to use in order to run the projen CLI.

        Can be used to customize in special environments.

        :default: "npx projen"

        :stability: experimental
        '''
        result = self._values.get("projen_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def projenrc_json(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Generate (once) .projenrc.json (in JSON). Set to ``false`` in order to disable .projenrc.json generation.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("projenrc_json")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def projenrc_json_options(self) -> typing.Optional["ProjenrcOptions"]:
        '''(experimental) Options for .projenrc.json.

        :default: - default options

        :stability: experimental
        '''
        result = self._values.get("projenrc_json_options")
        return typing.cast(typing.Optional["ProjenrcOptions"], result)

    @builtins.property
    def renovatebot(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Use renovatebot to handle dependency upgrades.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("renovatebot")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def renovatebot_options(self) -> typing.Optional["RenovatebotOptions"]:
        '''(experimental) Options for renovatebot.

        :default: - default options

        :stability: experimental
        '''
        result = self._values.get("renovatebot_options")
        return typing.cast(typing.Optional["RenovatebotOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="projen.ProjectType")
class ProjectType(enum.Enum):
    '''(deprecated) Which type of project this is.

    :deprecated: no longer supported at the base project level

    :stability: deprecated
    '''

    UNKNOWN = "UNKNOWN"
    '''(deprecated) This module may be a either a library or an app.

    :stability: deprecated
    '''
    LIB = "LIB"
    '''(deprecated) This is a library, intended to be published to a package manager and consumed by other projects.

    :stability: deprecated
    '''
    APP = "APP"
    '''(deprecated) This is an app (service, tool, website, etc).

    Its artifacts are intended to
    be deployed or published for end-user consumption.

    :stability: deprecated
    '''


class Projects(metaclass=jsii.JSIIMeta, jsii_type="projen.Projects"):
    '''(experimental) Programmatic API for projen.

    :stability: experimental
    '''

    @jsii.member(jsii_name="createProject") # type: ignore[misc]
    @builtins.classmethod
    def create_project(
        cls,
        *,
        dir: builtins.str,
        project_fqn: builtins.str,
        project_options: typing.Mapping[builtins.str, typing.Any],
        option_hints: typing.Optional[InitProjectOptionHints] = None,
        post: typing.Optional[builtins.bool] = None,
        synth: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Creates a new project with defaults.

        This function creates the project type in-process (with in VM) and calls
        ``.synth()`` on it (if ``options.synth`` is not ``false``).

        At the moment, it also generates a ``.projenrc.js`` file with the same code
        that was just executed. In the future, this will also be done by the project
        type, so we can easily support multiple languages of projenrc.

        :param dir: (experimental) Directory that the project will be generated in.
        :param project_fqn: (experimental) Fully-qualified name of the project type (usually formatted as ``module.ProjectType``).
        :param project_options: (experimental) Project options. Only JSON-like values can be passed in (strings, booleans, numbers, enums, arrays, and objects that are not derived from classes). Consult the API reference of the project type you are generating for information about what fields and types are available.
        :param option_hints: (experimental) Should we render commented-out default options in the projenrc file? Does not apply to projenrc.json files. Default: InitProjectOptionHints.FEATURED
        :param post: (experimental) Should we execute post synthesis hooks? (usually package manager install). Default: true
        :param synth: (experimental) Should we call ``project.synth()`` or instantiate the project (could still have side-effects) and render the .projenrc file. Default: true

        :stability: experimental
        '''
        options = CreateProjectOptions(
            dir=dir,
            project_fqn=project_fqn,
            project_options=project_options,
            option_hints=option_hints,
            post=post,
            synth=synth,
        )

        return typing.cast(None, jsii.sinvoke(cls, "createProject", [options]))


class Projenrc(Component, metaclass=jsii.JSIIMeta, jsii_type="projen.Projenrc"):
    '''(experimental) Sets up a project to use JSON for projenrc.

    :stability: experimental
    '''

    def __init__(
        self,
        project: Project,
        *,
        filename: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param project: -
        :param filename: (experimental) The name of the projenrc file. Default: ".projenrc.json"

        :stability: experimental
        '''
        options = ProjenrcOptions(filename=filename)

        jsii.create(self.__class__, self, [project, options])


@jsii.data_type(
    jsii_type="projen.ProjenrcOptions",
    jsii_struct_bases=[],
    name_mapping={"filename": "filename"},
)
class ProjenrcOptions:
    def __init__(self, *, filename: typing.Optional[builtins.str] = None) -> None:
        '''
        :param filename: (experimental) The name of the projenrc file. Default: ".projenrc.json"

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if filename is not None:
            self._values["filename"] = filename

    @builtins.property
    def filename(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the projenrc file.

        :default: ".projenrc.json"

        :stability: experimental
        '''
        result = self._values.get("filename")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjenrcOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Renovatebot(Component, metaclass=jsii.JSIIMeta, jsii_type="projen.Renovatebot"):
    '''(experimental) Defines renovatebot configuration for projen project.

    Ignores the versions controlled by Projen.

    :stability: experimental
    '''

    def __init__(
        self,
        project: Project,
        *,
        ignore: typing.Optional[typing.Sequence[builtins.str]] = None,
        ignore_projen: typing.Optional[builtins.bool] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        schedule_interval: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param project: -
        :param ignore: (experimental) You can use the ``ignore`` option to customize which dependencies are updated. The ignore option supports just package name. Default: []
        :param ignore_projen: (experimental) Ignores updates to ``projen``. This is required since projen updates may cause changes in committed files and anti-tamper checks will fail. Projen upgrades are covered through the ``ProjenUpgrade`` class. Default: true
        :param labels: (experimental) List of labels to apply to the created PR's.
        :param schedule_interval: (experimental) How often to check for new versions and raise pull requests. Can be given in CRON or LATER format, and use multiple schedules (e.g. different for weekdays and weekends). Multiple rules are handles as OR. Some normal scheduling values defined in enum ``RenovatebotScheduleInterval``. Default: ["at any time"]

        :stability: experimental
        '''
        options = RenovatebotOptions(
            ignore=ignore,
            ignore_projen=ignore_projen,
            labels=labels,
            schedule_interval=schedule_interval,
        )

        jsii.create(self.__class__, self, [project, options])

    @jsii.member(jsii_name="preSynthesize")
    def pre_synthesize(self) -> None:
        '''(experimental) Called before synthesis.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "preSynthesize", []))


@jsii.data_type(
    jsii_type="projen.RenovatebotOptions",
    jsii_struct_bases=[],
    name_mapping={
        "ignore": "ignore",
        "ignore_projen": "ignoreProjen",
        "labels": "labels",
        "schedule_interval": "scheduleInterval",
    },
)
class RenovatebotOptions:
    def __init__(
        self,
        *,
        ignore: typing.Optional[typing.Sequence[builtins.str]] = None,
        ignore_projen: typing.Optional[builtins.bool] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        schedule_interval: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) Options for Renovatebot.

        :param ignore: (experimental) You can use the ``ignore`` option to customize which dependencies are updated. The ignore option supports just package name. Default: []
        :param ignore_projen: (experimental) Ignores updates to ``projen``. This is required since projen updates may cause changes in committed files and anti-tamper checks will fail. Projen upgrades are covered through the ``ProjenUpgrade`` class. Default: true
        :param labels: (experimental) List of labels to apply to the created PR's.
        :param schedule_interval: (experimental) How often to check for new versions and raise pull requests. Can be given in CRON or LATER format, and use multiple schedules (e.g. different for weekdays and weekends). Multiple rules are handles as OR. Some normal scheduling values defined in enum ``RenovatebotScheduleInterval``. Default: ["at any time"]

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if ignore is not None:
            self._values["ignore"] = ignore
        if ignore_projen is not None:
            self._values["ignore_projen"] = ignore_projen
        if labels is not None:
            self._values["labels"] = labels
        if schedule_interval is not None:
            self._values["schedule_interval"] = schedule_interval

    @builtins.property
    def ignore(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) You can use the ``ignore`` option to customize which dependencies are updated.

        The ignore option supports just package name.

        :default: []

        :stability: experimental
        '''
        result = self._values.get("ignore")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ignore_projen(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Ignores updates to ``projen``.

        This is required since projen updates may cause changes in committed files
        and anti-tamper checks will fail.

        Projen upgrades are covered through the ``ProjenUpgrade`` class.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("ignore_projen")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) List of labels to apply to the created PR's.

        :stability: experimental
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def schedule_interval(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) How often to check for new versions and raise pull requests.

        Can be given in CRON or LATER format, and use multiple schedules
        (e.g. different for weekdays and weekends). Multiple rules are
        handles as OR.

        Some normal scheduling values defined in enum ``RenovatebotScheduleInterval``.

        :default: ["at any time"]

        :see: https://docs.renovatebot.com/configuration-options/#schedule
        :stability: experimental
        '''
        result = self._values.get("schedule_interval")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RenovatebotOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="projen.RenovatebotScheduleInterval")
class RenovatebotScheduleInterval(enum.Enum):
    '''(experimental) How often to check for new versions and raise pull requests for version updates.

    :see: https://docs.renovatebot.com/presets-schedule/
    :stability: experimental
    '''

    ANY_TIME = "ANY_TIME"
    '''(experimental) Run at any time.

    :stability: experimental
    '''
    EARLY_MONDAYS = "EARLY_MONDAYS"
    '''(experimental) Weekly schedule on early monday mornings.

    :stability: experimental
    '''
    DAILY = "DAILY"
    '''(experimental) Schedule daily.

    :stability: experimental
    '''
    MONTHLY = "MONTHLY"
    '''(experimental) Schedule monthly.

    :stability: experimental
    '''
    QUARTERLY = "QUARTERLY"
    '''(experimental) Schedule quarterly.

    :stability: experimental
    '''
    WEEKENDS = "WEEKENDS"
    '''(experimental) Schedule for weekends.

    :stability: experimental
    '''
    WEEKDAYS = "WEEKDAYS"
    '''(experimental) Schedule for weekdays.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="projen.ResolveOptions",
    jsii_struct_bases=[],
    name_mapping={"args": "args", "omit_empty": "omitEmpty"},
)
class ResolveOptions:
    def __init__(
        self,
        *,
        args: typing.Optional[typing.Sequence[typing.Any]] = None,
        omit_empty: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Resolve options.

        :param args: (experimental) Context arguments. Default: []
        :param omit_empty: (experimental) Omits empty arrays and objects. Default: false

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if args is not None:
            self._values["args"] = args
        if omit_empty is not None:
            self._values["omit_empty"] = omit_empty

    @builtins.property
    def args(self) -> typing.Optional[typing.List[typing.Any]]:
        '''(experimental) Context arguments.

        :default: []

        :stability: experimental
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def omit_empty(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Omits empty arrays and objects.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("omit_empty")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResolveOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.Rule",
    jsii_struct_bases=[],
    name_mapping={
        "targets": "targets",
        "phony": "phony",
        "prerequisites": "prerequisites",
        "recipe": "recipe",
    },
)
class Rule:
    def __init__(
        self,
        *,
        targets: typing.Sequence[builtins.str],
        phony: typing.Optional[builtins.bool] = None,
        prerequisites: typing.Optional[typing.Sequence[builtins.str]] = None,
        recipe: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) A Make rule.

        :param targets: (experimental) Files to be created or updated by this rule. If the rule is phony then instead this represents the command's name(s).
        :param phony: (experimental) Marks whether the target is phony. Default: false
        :param prerequisites: (experimental) Files that are used as inputs to create a target. Default: []
        :param recipe: (experimental) Commands that are run (using prerequisites as inputs) to create a target. Default: []

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "targets": targets,
        }
        if phony is not None:
            self._values["phony"] = phony
        if prerequisites is not None:
            self._values["prerequisites"] = prerequisites
        if recipe is not None:
            self._values["recipe"] = recipe

    @builtins.property
    def targets(self) -> typing.List[builtins.str]:
        '''(experimental) Files to be created or updated by this rule.

        If the rule is phony then instead this represents the command's name(s).

        :stability: experimental
        '''
        result = self._values.get("targets")
        assert result is not None, "Required property 'targets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def phony(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Marks whether the target is phony.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("phony")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def prerequisites(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Files that are used as inputs to create a target.

        :default: []

        :stability: experimental
        '''
        result = self._values.get("prerequisites")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def recipe(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Commands that are run (using prerequisites as inputs) to create a target.

        :default: []

        :stability: experimental
        '''
        result = self._values.get("recipe")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Rule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SampleDir(Component, metaclass=jsii.JSIIMeta, jsii_type="projen.SampleDir"):
    '''(experimental) Renders the given files into the directory if the directory does not exist.

    Use this to create sample code files

    :stability: experimental
    '''

    def __init__(
        self,
        project: Project,
        dir: builtins.str,
        *,
        files: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        source_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Create sample files in the given directory if the given directory does not exist.

        :param project: Parent project to add files to.
        :param dir: directory to add files to. If directory already exists, nothing is added.
        :param files: (experimental) The files to render into the directory. These files get added after any files from ``source`` if that option is specified (replacing if names overlap).
        :param source_dir: (experimental) Absolute path to a directory to copy files from (does not need to be text files). If your project is typescript-based and has configured ``testdir`` to be a subdirectory of ``src``, sample files should outside of the ``src`` directory otherwise they may not be copied. For example:: new SampleDir(this, 'public', { source: path.join(__dirname, '..', 'sample-assets') });

        :stability: experimental
        '''
        options = SampleDirOptions(files=files, source_dir=source_dir)

        jsii.create(self.__class__, self, [project, dir, options])

    @jsii.member(jsii_name="synthesize")
    def synthesize(self) -> None:
        '''(experimental) Synthesizes files to the project output directory.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "synthesize", []))


@jsii.data_type(
    jsii_type="projen.SampleDirOptions",
    jsii_struct_bases=[],
    name_mapping={"files": "files", "source_dir": "sourceDir"},
)
class SampleDirOptions:
    def __init__(
        self,
        *,
        files: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        source_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) SampleDir options.

        :param files: (experimental) The files to render into the directory. These files get added after any files from ``source`` if that option is specified (replacing if names overlap).
        :param source_dir: (experimental) Absolute path to a directory to copy files from (does not need to be text files). If your project is typescript-based and has configured ``testdir`` to be a subdirectory of ``src``, sample files should outside of the ``src`` directory otherwise they may not be copied. For example:: new SampleDir(this, 'public', { source: path.join(__dirname, '..', 'sample-assets') });

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if files is not None:
            self._values["files"] = files
        if source_dir is not None:
            self._values["source_dir"] = source_dir

    @builtins.property
    def files(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) The files to render into the directory.

        These files get added after
        any files from ``source`` if that option is specified (replacing if names
        overlap).

        :stability: experimental
        '''
        result = self._values.get("files")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def source_dir(self) -> typing.Optional[builtins.str]:
        '''(experimental) Absolute path to a directory to copy files from (does not need to be text files).

        If your project is typescript-based and has configured ``testdir`` to be a
        subdirectory of ``src``, sample files should outside of the ``src`` directory
        otherwise they may not be copied. For example::

           new SampleDir(this, 'public', { source: path.join(__dirname, '..', 'sample-assets') });

        :stability: experimental
        '''
        result = self._values.get("source_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SampleDirOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SampleFile(Component, metaclass=jsii.JSIIMeta, jsii_type="projen.SampleFile"):
    '''(experimental) Produces a file with the given contents but only once, if the file doesn't already exist.

    Use this for creating example code files or other resources.

    :stability: experimental
    '''

    def __init__(
        self,
        project: Project,
        file_path: builtins.str,
        *,
        contents: typing.Optional[builtins.str] = None,
        source_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Creates a new SampleFile object.

        :param project: - the project to tie this file to.
        :param file_path: - the relative path in the project to put the file.
        :param contents: (experimental) The contents of the file to write.
        :param source_path: (experimental) Absolute path to a file to copy the contents from (does not need to be a text file). If your project is Typescript-based and has configured ``testdir`` to be a subdirectory of ``src``, sample files should outside of the ``src`` directory, otherwise they may not be copied. For example:: new SampleFile(this, 'assets/icon.png', { source: path.join(__dirname, '..', 'sample-assets', 'icon.png') });

        :stability: experimental
        '''
        options = SampleFileOptions(contents=contents, source_path=source_path)

        jsii.create(self.__class__, self, [project, file_path, options])

    @jsii.member(jsii_name="synthesize")
    def synthesize(self) -> None:
        '''(experimental) Synthesizes files to the project output directory.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "synthesize", []))


@jsii.data_type(
    jsii_type="projen.SampleFileOptions",
    jsii_struct_bases=[],
    name_mapping={"contents": "contents", "source_path": "sourcePath"},
)
class SampleFileOptions:
    def __init__(
        self,
        *,
        contents: typing.Optional[builtins.str] = None,
        source_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Options for the SampleFile object.

        :param contents: (experimental) The contents of the file to write.
        :param source_path: (experimental) Absolute path to a file to copy the contents from (does not need to be a text file). If your project is Typescript-based and has configured ``testdir`` to be a subdirectory of ``src``, sample files should outside of the ``src`` directory, otherwise they may not be copied. For example:: new SampleFile(this, 'assets/icon.png', { source: path.join(__dirname, '..', 'sample-assets', 'icon.png') });

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if contents is not None:
            self._values["contents"] = contents
        if source_path is not None:
            self._values["source_path"] = source_path

    @builtins.property
    def contents(self) -> typing.Optional[builtins.str]:
        '''(experimental) The contents of the file to write.

        :stability: experimental
        '''
        result = self._values.get("contents")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_path(self) -> typing.Optional[builtins.str]:
        '''(experimental) Absolute path to a file to copy the contents from (does not need to be a text file).

        If your project is Typescript-based and has configured ``testdir`` to be a
        subdirectory of ``src``, sample files should outside of the ``src`` directory,
        otherwise they may not be copied. For example::

           new SampleFile(this, 'assets/icon.png', { source: path.join(__dirname, '..', 'sample-assets', 'icon.png') });

        :stability: experimental
        '''
        result = self._values.get("source_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SampleFileOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SampleReadme(
    SampleFile,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.SampleReadme",
):
    '''(experimental) Represents a README.md sample file. You are expected to manage this file after creation.

    :stability: experimental
    '''

    def __init__(
        self,
        project: Project,
        *,
        contents: typing.Optional[builtins.str] = None,
        filename: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param project: -
        :param contents: (experimental) The contents. Default: "# replace this"
        :param filename: (experimental) The name of the README.md file. Default: "README.md"

        :stability: experimental
        '''
        props = SampleReadmeProps(contents=contents, filename=filename)

        jsii.create(self.__class__, self, [project, props])


@jsii.data_type(
    jsii_type="projen.SampleReadmeProps",
    jsii_struct_bases=[],
    name_mapping={"contents": "contents", "filename": "filename"},
)
class SampleReadmeProps:
    def __init__(
        self,
        *,
        contents: typing.Optional[builtins.str] = None,
        filename: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) SampleReadme Properties.

        :param contents: (experimental) The contents. Default: "# replace this"
        :param filename: (experimental) The name of the README.md file. Default: "README.md"

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if contents is not None:
            self._values["contents"] = contents
        if filename is not None:
            self._values["filename"] = filename

    @builtins.property
    def contents(self) -> typing.Optional[builtins.str]:
        '''(experimental) The contents.

        :default: "# replace this"

        :stability: experimental
        '''
        result = self._values.get("contents")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filename(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the README.md file.

        :default: "README.md"

        :stability: experimental

        Example::

            "readme.md"
        '''
        result = self._values.get("filename")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SampleReadmeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Semver(metaclass=jsii.JSIIMeta, jsii_type="projen.Semver"):
    '''
    :deprecated:

    This class will be removed in upcoming releases. if you wish to
    specify semver requirements in ``deps``, ``devDeps``, etc, specify them like so
    ``express@^2.1``.

    :stability: deprecated
    '''

    @jsii.member(jsii_name="caret") # type: ignore[misc]
    @builtins.classmethod
    def caret(cls, version: builtins.str) -> "Semver":
        '''(deprecated) Accept any minor version.

        .. epigraph::

           = version
           < next major version

        :param version: -

        :stability: deprecated
        '''
        return typing.cast("Semver", jsii.sinvoke(cls, "caret", [version]))

    @jsii.member(jsii_name="latest") # type: ignore[misc]
    @builtins.classmethod
    def latest(cls) -> "Semver":
        '''(deprecated) Latest version.

        :stability: deprecated
        '''
        return typing.cast("Semver", jsii.sinvoke(cls, "latest", []))

    @jsii.member(jsii_name="of") # type: ignore[misc]
    @builtins.classmethod
    def of(cls, spec: builtins.str) -> "Semver":
        '''
        :param spec: -

        :stability: deprecated
        '''
        return typing.cast("Semver", jsii.sinvoke(cls, "of", [spec]))

    @jsii.member(jsii_name="pinned") # type: ignore[misc]
    @builtins.classmethod
    def pinned(cls, version: builtins.str) -> "Semver":
        '''(deprecated) Accept only an exact version.

        :param version: -

        :stability: deprecated
        '''
        return typing.cast("Semver", jsii.sinvoke(cls, "pinned", [version]))

    @jsii.member(jsii_name="tilde") # type: ignore[misc]
    @builtins.classmethod
    def tilde(cls, version: builtins.str) -> "Semver":
        '''(deprecated) Accept patches.

        .. epigraph::

           = version
           < next minor version

        :param version: -

        :stability: deprecated
        '''
        return typing.cast("Semver", jsii.sinvoke(cls, "tilde", [version]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="spec")
    def spec(self) -> builtins.str:
        '''
        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.get(self, "spec"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mode")
    def mode(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mode"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "version"))


class SourceCode(Component, metaclass=jsii.JSIIMeta, jsii_type="projen.SourceCode"):
    '''(experimental) Represents a source file.

    :stability: experimental
    '''

    def __init__(
        self,
        project: Project,
        file_path: builtins.str,
        *,
        indent: typing.Optional[jsii.Number] = None,
        readonly: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param project: -
        :param file_path: -
        :param indent: (experimental) Indentation size. Default: 2
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true

        :stability: experimental
        '''
        options = SourceCodeOptions(indent=indent, readonly=readonly)

        jsii.create(self.__class__, self, [project, file_path, options])

    @jsii.member(jsii_name="close")
    def close(self, code: typing.Optional[builtins.str] = None) -> None:
        '''(experimental) Decreases the indentation level and closes a code block.

        :param code: The code after the block is closed (e.g. ``}``).

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "close", [code]))

    @jsii.member(jsii_name="line")
    def line(self, code: typing.Optional[builtins.str] = None) -> None:
        '''(experimental) Emit a line of code.

        :param code: The contents, if not specified, just adds a newline.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "line", [code]))

    @jsii.member(jsii_name="open")
    def open(self, code: typing.Optional[builtins.str] = None) -> None:
        '''(experimental) Opens a code block and increases the indentation level.

        :param code: The code before the block starts (e.g. ``export class {``).

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "open", [code]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="filePath")
    def file_path(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "filePath"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="marker")
    def marker(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "marker"))


@jsii.data_type(
    jsii_type="projen.SourceCodeOptions",
    jsii_struct_bases=[],
    name_mapping={"indent": "indent", "readonly": "readonly"},
)
class SourceCodeOptions:
    def __init__(
        self,
        *,
        indent: typing.Optional[jsii.Number] = None,
        readonly: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Options for ``SourceCodeFile``.

        :param indent: (experimental) Indentation size. Default: 2
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if indent is not None:
            self._values["indent"] = indent
        if readonly is not None:
            self._values["readonly"] = readonly

    @builtins.property
    def indent(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Indentation size.

        :default: 2

        :stability: experimental
        '''
        result = self._values.get("indent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def readonly(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be readonly.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("readonly")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SourceCodeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Task(metaclass=jsii.JSIIMeta, jsii_type="projen.Task"):
    '''(experimental) A task that can be performed on the project.

    Modeled as a series of shell
    commands and subtasks.

    :stability: experimental
    '''

    def __init__(
        self,
        name: builtins.str,
        *,
        exec: typing.Optional[builtins.str] = None,
        steps: typing.Optional[typing.Sequence["TaskStep"]] = None,
        condition: typing.Optional[builtins.str] = None,
        cwd: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        required_env: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: -
        :param exec: (experimental) Shell command to execute as the first command of the task. Default: - add steps using ``task.exec(command)`` or ``task.spawn(subtask)``
        :param steps: (experimental) List of task steps to run.
        :param condition: (experimental) A shell command which determines if the this task should be executed. If the program exits with a zero exit code, steps will be executed. A non-zero code means that task will be skipped.
        :param cwd: (experimental) The working directory for all steps in this task (unless overridden by the step). Default: - process.cwd()
        :param description: (experimental) The description of this build command. Default: - the task name
        :param env: (experimental) Defines environment variables for the execution of this task. Values in this map will be evaluated in a shell, so you can do stuff like ``$(echo "foo")``. Default: {}
        :param required_env: (experimental) A set of environment variables that must be defined in order to execute this task. Task execution will fail if one of these is not defined.

        :stability: experimental
        '''
        props = TaskOptions(
            exec=exec,
            steps=steps,
            condition=condition,
            cwd=cwd,
            description=description,
            env=env,
            required_env=required_env,
        )

        jsii.create(self.__class__, self, [name, props])

    @jsii.member(jsii_name="builtin")
    def builtin(self, name: builtins.str) -> None:
        '''(experimental) Execute a builtin task.

        Builtin tasks are programs bundled as part of projen itself and used as
        helpers for various components.

        In the future we should support built-in tasks from external modules.

        :param name: The name of the builtin task to execute (e.g. ``release/resolve-version``).

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "builtin", [name]))

    @jsii.member(jsii_name="env")
    def env(self, name: builtins.str, value: builtins.str) -> None:
        '''(experimental) Adds an environment variable to this task.

        :param name: The name of the variable.
        :param value: The value. If the value is surrounded by ``$()``, we will evaluate it within a subshell and use the result as the value of the environment variable.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "env", [name, value]))

    @jsii.member(jsii_name="exec")
    def exec(
        self,
        command: builtins.str,
        *,
        cwd: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Executes a shell command.

        :param command: Shell command.
        :param cwd: (experimental) The working directory for this step. Default: - determined by the task
        :param name: (experimental) Step name. Default: - no name

        :stability: experimental
        '''
        options = TaskStepOptions(cwd=cwd, name=name)

        return typing.cast(None, jsii.invoke(self, "exec", [command, options]))

    @jsii.member(jsii_name="lock")
    def lock(self) -> None:
        '''(experimental) Forbid additional changes to this task.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "lock", []))

    @jsii.member(jsii_name="prepend")
    def prepend(
        self,
        shell: builtins.str,
        *,
        cwd: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(deprecated) Adds a command at the beginning of the task.

        :param shell: The command to add.
        :param cwd: (experimental) The working directory for this step. Default: - determined by the task
        :param name: (experimental) Step name. Default: - no name

        :deprecated: use ``prependExec()``

        :stability: deprecated
        '''
        options = TaskStepOptions(cwd=cwd, name=name)

        return typing.cast(None, jsii.invoke(self, "prepend", [shell, options]))

    @jsii.member(jsii_name="prependExec")
    def prepend_exec(
        self,
        shell: builtins.str,
        *,
        cwd: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Adds a command at the beginning of the task.

        :param shell: The command to add.
        :param cwd: (experimental) The working directory for this step. Default: - determined by the task
        :param name: (experimental) Step name. Default: - no name

        :stability: experimental
        '''
        options = TaskStepOptions(cwd=cwd, name=name)

        return typing.cast(None, jsii.invoke(self, "prependExec", [shell, options]))

    @jsii.member(jsii_name="prependSay")
    def prepend_say(
        self,
        message: builtins.str,
        *,
        cwd: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Says something at the beginning of the task.

        :param message: Your message.
        :param cwd: (experimental) The working directory for this step. Default: - determined by the task
        :param name: (experimental) Step name. Default: - no name

        :stability: experimental
        '''
        options = TaskStepOptions(cwd=cwd, name=name)

        return typing.cast(None, jsii.invoke(self, "prependSay", [message, options]))

    @jsii.member(jsii_name="prependSpawn")
    def prepend_spawn(
        self,
        subtask: "Task",
        *,
        cwd: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Adds a spawn instruction at the beginning of the task.

        :param subtask: The subtask to execute.
        :param cwd: (experimental) The working directory for this step. Default: - determined by the task
        :param name: (experimental) Step name. Default: - no name

        :stability: experimental
        '''
        options = TaskStepOptions(cwd=cwd, name=name)

        return typing.cast(None, jsii.invoke(self, "prependSpawn", [subtask, options]))

    @jsii.member(jsii_name="reset")
    def reset(
        self,
        command: typing.Optional[builtins.str] = None,
        *,
        cwd: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Reset the task so it no longer has any commands.

        :param command: the first command to add to the task after it was cleared.
        :param cwd: (experimental) The working directory for this step. Default: - determined by the task
        :param name: (experimental) Step name. Default: - no name

        :stability: experimental
        '''
        options = TaskStepOptions(cwd=cwd, name=name)

        return typing.cast(None, jsii.invoke(self, "reset", [command, options]))

    @jsii.member(jsii_name="say")
    def say(
        self,
        message: builtins.str,
        *,
        cwd: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Say something.

        :param message: Your message.
        :param cwd: (experimental) The working directory for this step. Default: - determined by the task
        :param name: (experimental) Step name. Default: - no name

        :stability: experimental
        '''
        options = TaskStepOptions(cwd=cwd, name=name)

        return typing.cast(None, jsii.invoke(self, "say", [message, options]))

    @jsii.member(jsii_name="spawn")
    def spawn(
        self,
        subtask: "Task",
        *,
        cwd: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Spawns a sub-task.

        :param subtask: The subtask to execute.
        :param cwd: (experimental) The working directory for this step. Default: - determined by the task
        :param name: (experimental) Step name. Default: - no name

        :stability: experimental
        '''
        options = TaskStepOptions(cwd=cwd, name=name)

        return typing.cast(None, jsii.invoke(self, "spawn", [subtask, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''(experimental) Task name.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="steps")
    def steps(self) -> typing.List["TaskStep"]:
        '''(experimental) Returns an immutable copy of all the step specifications of the task.

        :stability: experimental
        '''
        return typing.cast(typing.List["TaskStep"], jsii.get(self, "steps"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="condition")
    def condition(self) -> typing.Optional[builtins.str]:
        '''(experimental) A command to execute which determines if the task should be skipped.

        If it
        returns a zero exit code, the task will not be executed.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "condition"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Returns the description of this task.

        Sets the description of this task.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="projen.TaskCommonOptions",
    jsii_struct_bases=[],
    name_mapping={
        "condition": "condition",
        "cwd": "cwd",
        "description": "description",
        "env": "env",
        "required_env": "requiredEnv",
    },
)
class TaskCommonOptions:
    def __init__(
        self,
        *,
        condition: typing.Optional[builtins.str] = None,
        cwd: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        required_env: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param condition: (experimental) A shell command which determines if the this task should be executed. If the program exits with a zero exit code, steps will be executed. A non-zero code means that task will be skipped.
        :param cwd: (experimental) The working directory for all steps in this task (unless overridden by the step). Default: - process.cwd()
        :param description: (experimental) The description of this build command. Default: - the task name
        :param env: (experimental) Defines environment variables for the execution of this task. Values in this map will be evaluated in a shell, so you can do stuff like ``$(echo "foo")``. Default: {}
        :param required_env: (experimental) A set of environment variables that must be defined in order to execute this task. Task execution will fail if one of these is not defined.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if condition is not None:
            self._values["condition"] = condition
        if cwd is not None:
            self._values["cwd"] = cwd
        if description is not None:
            self._values["description"] = description
        if env is not None:
            self._values["env"] = env
        if required_env is not None:
            self._values["required_env"] = required_env

    @builtins.property
    def condition(self) -> typing.Optional[builtins.str]:
        '''(experimental) A shell command which determines if the this task should be executed.

        If
        the program exits with a zero exit code, steps will be executed. A non-zero
        code means that task will be skipped.

        :stability: experimental
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cwd(self) -> typing.Optional[builtins.str]:
        '''(experimental) The working directory for all steps in this task (unless overridden by the step).

        :default: - process.cwd()

        :stability: experimental
        '''
        result = self._values.get("cwd")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) The description of this build command.

        :default: - the task name

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def env(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) Defines environment variables for the execution of this task.

        Values in this map will be evaluated in a shell, so you can do stuff like ``$(echo "foo")``.

        :default: {}

        :stability: experimental
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def required_env(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) A set of environment variables that must be defined in order to execute this task.

        Task execution will fail if one of these is not defined.

        :stability: experimental
        '''
        result = self._values.get("required_env")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TaskCommonOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.TaskOptions",
    jsii_struct_bases=[TaskCommonOptions],
    name_mapping={
        "condition": "condition",
        "cwd": "cwd",
        "description": "description",
        "env": "env",
        "required_env": "requiredEnv",
        "exec": "exec",
        "steps": "steps",
    },
)
class TaskOptions(TaskCommonOptions):
    def __init__(
        self,
        *,
        condition: typing.Optional[builtins.str] = None,
        cwd: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        required_env: typing.Optional[typing.Sequence[builtins.str]] = None,
        exec: typing.Optional[builtins.str] = None,
        steps: typing.Optional[typing.Sequence["TaskStep"]] = None,
    ) -> None:
        '''
        :param condition: (experimental) A shell command which determines if the this task should be executed. If the program exits with a zero exit code, steps will be executed. A non-zero code means that task will be skipped.
        :param cwd: (experimental) The working directory for all steps in this task (unless overridden by the step). Default: - process.cwd()
        :param description: (experimental) The description of this build command. Default: - the task name
        :param env: (experimental) Defines environment variables for the execution of this task. Values in this map will be evaluated in a shell, so you can do stuff like ``$(echo "foo")``. Default: {}
        :param required_env: (experimental) A set of environment variables that must be defined in order to execute this task. Task execution will fail if one of these is not defined.
        :param exec: (experimental) Shell command to execute as the first command of the task. Default: - add steps using ``task.exec(command)`` or ``task.spawn(subtask)``
        :param steps: (experimental) List of task steps to run.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if condition is not None:
            self._values["condition"] = condition
        if cwd is not None:
            self._values["cwd"] = cwd
        if description is not None:
            self._values["description"] = description
        if env is not None:
            self._values["env"] = env
        if required_env is not None:
            self._values["required_env"] = required_env
        if exec is not None:
            self._values["exec"] = exec
        if steps is not None:
            self._values["steps"] = steps

    @builtins.property
    def condition(self) -> typing.Optional[builtins.str]:
        '''(experimental) A shell command which determines if the this task should be executed.

        If
        the program exits with a zero exit code, steps will be executed. A non-zero
        code means that task will be skipped.

        :stability: experimental
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cwd(self) -> typing.Optional[builtins.str]:
        '''(experimental) The working directory for all steps in this task (unless overridden by the step).

        :default: - process.cwd()

        :stability: experimental
        '''
        result = self._values.get("cwd")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) The description of this build command.

        :default: - the task name

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def env(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) Defines environment variables for the execution of this task.

        Values in this map will be evaluated in a shell, so you can do stuff like ``$(echo "foo")``.

        :default: {}

        :stability: experimental
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def required_env(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) A set of environment variables that must be defined in order to execute this task.

        Task execution will fail if one of these is not defined.

        :stability: experimental
        '''
        result = self._values.get("required_env")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def exec(self) -> typing.Optional[builtins.str]:
        '''(experimental) Shell command to execute as the first command of the task.

        :default: - add steps using ``task.exec(command)`` or ``task.spawn(subtask)``

        :stability: experimental
        '''
        result = self._values.get("exec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def steps(self) -> typing.Optional[typing.List["TaskStep"]]:
        '''(experimental) List of task steps to run.

        :stability: experimental
        '''
        result = self._values.get("steps")
        return typing.cast(typing.Optional[typing.List["TaskStep"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TaskOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TaskRuntime(metaclass=jsii.JSIIMeta, jsii_type="projen.TaskRuntime"):
    '''(experimental) The runtime component of the tasks engine.

    :stability: experimental
    '''

    def __init__(self, workdir: builtins.str) -> None:
        '''
        :param workdir: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [workdir])

    @jsii.member(jsii_name="runTask")
    def run_task(
        self,
        name: builtins.str,
        parents: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) Runs the task.

        :param name: The task name.
        :param parents: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "runTask", [name, parents]))

    @jsii.member(jsii_name="tryFindTask")
    def try_find_task(self, name: builtins.str) -> typing.Optional["TaskSpec"]:
        '''(experimental) Find a task by name, or ``undefined`` if not found.

        :param name: -

        :stability: experimental
        '''
        return typing.cast(typing.Optional["TaskSpec"], jsii.invoke(self, "tryFindTask", [name]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="MANIFEST_FILE")
    def MANIFEST_FILE(cls) -> builtins.str:
        '''(experimental) The project-relative path of the tasks manifest file.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "MANIFEST_FILE"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="manifest")
    def manifest(self) -> "TasksManifest":
        '''(experimental) The contents of tasks.json.

        :stability: experimental
        '''
        return typing.cast("TasksManifest", jsii.get(self, "manifest"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tasks")
    def tasks(self) -> typing.List["TaskSpec"]:
        '''(experimental) The tasks in this project.

        :stability: experimental
        '''
        return typing.cast(typing.List["TaskSpec"], jsii.get(self, "tasks"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="workdir")
    def workdir(self) -> builtins.str:
        '''(experimental) The root directory of the project and the cwd for executing tasks.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "workdir"))


@jsii.data_type(
    jsii_type="projen.TaskSpec",
    jsii_struct_bases=[TaskCommonOptions],
    name_mapping={
        "condition": "condition",
        "cwd": "cwd",
        "description": "description",
        "env": "env",
        "required_env": "requiredEnv",
        "name": "name",
        "steps": "steps",
    },
)
class TaskSpec(TaskCommonOptions):
    def __init__(
        self,
        *,
        condition: typing.Optional[builtins.str] = None,
        cwd: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        required_env: typing.Optional[typing.Sequence[builtins.str]] = None,
        name: builtins.str,
        steps: typing.Optional[typing.Sequence["TaskStep"]] = None,
    ) -> None:
        '''(experimental) Specification of a single task.

        :param condition: (experimental) A shell command which determines if the this task should be executed. If the program exits with a zero exit code, steps will be executed. A non-zero code means that task will be skipped.
        :param cwd: (experimental) The working directory for all steps in this task (unless overridden by the step). Default: - process.cwd()
        :param description: (experimental) The description of this build command. Default: - the task name
        :param env: (experimental) Defines environment variables for the execution of this task. Values in this map will be evaluated in a shell, so you can do stuff like ``$(echo "foo")``. Default: {}
        :param required_env: (experimental) A set of environment variables that must be defined in order to execute this task. Task execution will fail if one of these is not defined.
        :param name: (experimental) Task name.
        :param steps: (experimental) Task steps.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if condition is not None:
            self._values["condition"] = condition
        if cwd is not None:
            self._values["cwd"] = cwd
        if description is not None:
            self._values["description"] = description
        if env is not None:
            self._values["env"] = env
        if required_env is not None:
            self._values["required_env"] = required_env
        if steps is not None:
            self._values["steps"] = steps

    @builtins.property
    def condition(self) -> typing.Optional[builtins.str]:
        '''(experimental) A shell command which determines if the this task should be executed.

        If
        the program exits with a zero exit code, steps will be executed. A non-zero
        code means that task will be skipped.

        :stability: experimental
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cwd(self) -> typing.Optional[builtins.str]:
        '''(experimental) The working directory for all steps in this task (unless overridden by the step).

        :default: - process.cwd()

        :stability: experimental
        '''
        result = self._values.get("cwd")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) The description of this build command.

        :default: - the task name

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def env(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) Defines environment variables for the execution of this task.

        Values in this map will be evaluated in a shell, so you can do stuff like ``$(echo "foo")``.

        :default: {}

        :stability: experimental
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def required_env(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) A set of environment variables that must be defined in order to execute this task.

        Task execution will fail if one of these is not defined.

        :stability: experimental
        '''
        result = self._values.get("required_env")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) Task name.

        :stability: experimental
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def steps(self) -> typing.Optional[typing.List["TaskStep"]]:
        '''(experimental) Task steps.

        :stability: experimental
        '''
        result = self._values.get("steps")
        return typing.cast(typing.Optional[typing.List["TaskStep"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TaskSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.TaskStepOptions",
    jsii_struct_bases=[],
    name_mapping={"cwd": "cwd", "name": "name"},
)
class TaskStepOptions:
    def __init__(
        self,
        *,
        cwd: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Options for task steps.

        :param cwd: (experimental) The working directory for this step. Default: - determined by the task
        :param name: (experimental) Step name. Default: - no name

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if cwd is not None:
            self._values["cwd"] = cwd
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def cwd(self) -> typing.Optional[builtins.str]:
        '''(experimental) The working directory for this step.

        :default: - determined by the task

        :stability: experimental
        '''
        result = self._values.get("cwd")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Step name.

        :default: - no name

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TaskStepOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Tasks(Component, metaclass=jsii.JSIIMeta, jsii_type="projen.Tasks"):
    '''(experimental) Defines project tasks.

    Tasks extend the projen CLI by adding subcommands to it. Task definitions are
    synthesized into ``.projen/tasks.json``.

    :stability: experimental
    '''

    def __init__(self, project: Project) -> None:
        '''
        :param project: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [project])

    @jsii.member(jsii_name="addEnvironment")
    def add_environment(self, name: builtins.str, value: builtins.str) -> None:
        '''(experimental) Adds global environment.

        :param name: Environment variable name.
        :param value: Value.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addEnvironment", [name, value]))

    @jsii.member(jsii_name="addTask")
    def add_task(
        self,
        name: builtins.str,
        *,
        exec: typing.Optional[builtins.str] = None,
        steps: typing.Optional[typing.Sequence["TaskStep"]] = None,
        condition: typing.Optional[builtins.str] = None,
        cwd: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        required_env: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> Task:
        '''(experimental) Adds a task to a project.

        :param name: The name of the task.
        :param exec: (experimental) Shell command to execute as the first command of the task. Default: - add steps using ``task.exec(command)`` or ``task.spawn(subtask)``
        :param steps: (experimental) List of task steps to run.
        :param condition: (experimental) A shell command which determines if the this task should be executed. If the program exits with a zero exit code, steps will be executed. A non-zero code means that task will be skipped.
        :param cwd: (experimental) The working directory for all steps in this task (unless overridden by the step). Default: - process.cwd()
        :param description: (experimental) The description of this build command. Default: - the task name
        :param env: (experimental) Defines environment variables for the execution of this task. Values in this map will be evaluated in a shell, so you can do stuff like ``$(echo "foo")``. Default: {}
        :param required_env: (experimental) A set of environment variables that must be defined in order to execute this task. Task execution will fail if one of these is not defined.

        :stability: experimental
        '''
        options = TaskOptions(
            exec=exec,
            steps=steps,
            condition=condition,
            cwd=cwd,
            description=description,
            env=env,
            required_env=required_env,
        )

        return typing.cast(Task, jsii.invoke(self, "addTask", [name, options]))

    @jsii.member(jsii_name="removeTask")
    def remove_task(self, name: builtins.str) -> typing.Optional[Task]:
        '''(experimental) Removes a task from a project.

        :param name: The name of the task to remove.

        :return: The ``Task`` that was removed, otherwise ``undefined``.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[Task], jsii.invoke(self, "removeTask", [name]))

    @jsii.member(jsii_name="synthesize")
    def synthesize(self) -> None:
        '''(experimental) Synthesizes files to the project output directory.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "synthesize", []))

    @jsii.member(jsii_name="tryFind")
    def try_find(self, name: builtins.str) -> typing.Optional[Task]:
        '''(experimental) Finds a task by name.

        Returns ``undefined`` if the task cannot be found.

        :param name: The name of the task.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[Task], jsii.invoke(self, "tryFind", [name]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="all")
    def all(self) -> typing.List[Task]:
        '''(experimental) All tasks.

        :stability: experimental
        '''
        return typing.cast(typing.List[Task], jsii.get(self, "all"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="env")
    def env(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''(experimental) Returns a copy of the currently global environment for this project.

        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "env"))


@jsii.data_type(
    jsii_type="projen.TasksManifest",
    jsii_struct_bases=[],
    name_mapping={"env": "env", "tasks": "tasks"},
)
class TasksManifest:
    def __init__(
        self,
        *,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tasks: typing.Optional[typing.Mapping[builtins.str, TaskSpec]] = None,
    ) -> None:
        '''(experimental) Schema for ``tasks.json``.

        :param env: (experimental) Environment for all tasks.
        :param tasks: (experimental) All tasks available for this project.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if env is not None:
            self._values["env"] = env
        if tasks is not None:
            self._values["tasks"] = tasks

    @builtins.property
    def env(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) Environment for all tasks.

        :stability: experimental
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tasks(self) -> typing.Optional[typing.Mapping[builtins.str, TaskSpec]]:
        '''(experimental) All tasks available for this project.

        :stability: experimental
        '''
        result = self._values.get("tasks")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, TaskSpec]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TasksManifest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Testing(metaclass=jsii.JSIIMeta, jsii_type="projen.Testing"):
    '''(experimental) A Testing static class with a .synth helper for getting a snapshots of construct outputs. Useful for snapshot testing with Jest.

    :stability: experimental

    Example::

        `expect(Testing.synth(someProject)).toMatchSnapshot()`
    '''

    @jsii.member(jsii_name="synth") # type: ignore[misc]
    @builtins.classmethod
    def synth(cls, project: Project) -> typing.Mapping[builtins.str, typing.Any]:
        '''(experimental) Produces a simple JS object that represents the contents of the projects with field names being file paths.

        :param project: the project to produce a snapshot for.

        :return: : any }

        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.sinvoke(cls, "synth", [project]))


class TextFile(FileBase, metaclass=jsii.JSIIMeta, jsii_type="projen.TextFile"):
    '''(experimental) A text file.

    :stability: experimental
    '''

    def __init__(
        self,
        project: Project,
        file_path: builtins.str,
        *,
        lines: typing.Optional[typing.Sequence[builtins.str]] = None,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Defines a text file.

        :param project: The project.
        :param file_path: File path.
        :param lines: (experimental) The contents of the text file. You can use ``addLine()`` to append lines. Default: [] empty file
        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true

        :stability: experimental
        '''
        options = TextFileOptions(
            lines=lines,
            committed=committed,
            edit_gitignore=edit_gitignore,
            executable=executable,
            marker=marker,
            readonly=readonly,
        )

        jsii.create(self.__class__, self, [project, file_path, options])

    @jsii.member(jsii_name="addLine")
    def add_line(self, line: builtins.str) -> None:
        '''(experimental) Adds a line to the text file.

        :param line: the line to add (can use tokens).

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addLine", [line]))

    @jsii.member(jsii_name="synthesizeContent")
    def _synthesize_content(self, _: IResolver) -> typing.Optional[builtins.str]:
        '''(experimental) Implemented by derived classes and returns the contents of the file to emit.

        :param _: -

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "synthesizeContent", [_]))


@jsii.data_type(
    jsii_type="projen.TextFileOptions",
    jsii_struct_bases=[FileBaseOptions],
    name_mapping={
        "committed": "committed",
        "edit_gitignore": "editGitignore",
        "executable": "executable",
        "marker": "marker",
        "readonly": "readonly",
        "lines": "lines",
    },
)
class TextFileOptions(FileBaseOptions):
    def __init__(
        self,
        *,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
        lines: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) Options for ``TextFile``.

        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true
        :param lines: (experimental) The contents of the text file. You can use ``addLine()`` to append lines. Default: [] empty file

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if committed is not None:
            self._values["committed"] = committed
        if edit_gitignore is not None:
            self._values["edit_gitignore"] = edit_gitignore
        if executable is not None:
            self._values["executable"] = executable
        if marker is not None:
            self._values["marker"] = marker
        if readonly is not None:
            self._values["readonly"] = readonly
        if lines is not None:
            self._values["lines"] = lines

    @builtins.property
    def committed(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether this file should be committed to git or ignored.

        By
        default, all generated files are committed and anti-tamper is used to
        protect against manual modifications.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("committed")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def edit_gitignore(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Update the project's .gitignore file.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("edit_gitignore")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def executable(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be marked as executable.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("executable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def marker(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Adds the projen marker to the file.

        :default: - marker will be included as long as the project is not ejected

        :stability: experimental
        '''
        result = self._values.get("marker")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def readonly(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be readonly.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("readonly")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def lines(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) The contents of the text file.

        You can use ``addLine()`` to append lines.

        :default: [] empty file

        :stability: experimental
        '''
        result = self._values.get("lines")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TextFileOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TomlFile(ObjectFile, metaclass=jsii.JSIIMeta, jsii_type="projen.TomlFile"):
    '''(experimental) Represents a TOML file.

    :stability: experimental
    '''

    def __init__(
        self,
        project: Project,
        file_path: builtins.str,
        *,
        obj: typing.Any = None,
        omit_empty: typing.Optional[builtins.bool] = None,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param project: -
        :param file_path: -
        :param obj: (experimental) The object that will be serialized. You can modify the object's contents before synthesis. Default: {} an empty object (use ``file.obj`` to mutate).
        :param omit_empty: (experimental) Omits empty objects and arrays. Default: false
        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true

        :stability: experimental
        '''
        options = TomlFileOptions(
            obj=obj,
            omit_empty=omit_empty,
            committed=committed,
            edit_gitignore=edit_gitignore,
            executable=executable,
            marker=marker,
            readonly=readonly,
        )

        jsii.create(self.__class__, self, [project, file_path, options])

    @jsii.member(jsii_name="synthesizeContent")
    def _synthesize_content(self, resolver: IResolver) -> typing.Optional[builtins.str]:
        '''(experimental) Implemented by derived classes and returns the contents of the file to emit.

        :param resolver: -

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "synthesizeContent", [resolver]))


@jsii.data_type(
    jsii_type="projen.TomlFileOptions",
    jsii_struct_bases=[ObjectFileOptions],
    name_mapping={
        "committed": "committed",
        "edit_gitignore": "editGitignore",
        "executable": "executable",
        "marker": "marker",
        "readonly": "readonly",
        "obj": "obj",
        "omit_empty": "omitEmpty",
    },
)
class TomlFileOptions(ObjectFileOptions):
    def __init__(
        self,
        *,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
        obj: typing.Any = None,
        omit_empty: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Options for ``TomlFile``.

        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true
        :param obj: (experimental) The object that will be serialized. You can modify the object's contents before synthesis. Default: {} an empty object (use ``file.obj`` to mutate).
        :param omit_empty: (experimental) Omits empty objects and arrays. Default: false

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if committed is not None:
            self._values["committed"] = committed
        if edit_gitignore is not None:
            self._values["edit_gitignore"] = edit_gitignore
        if executable is not None:
            self._values["executable"] = executable
        if marker is not None:
            self._values["marker"] = marker
        if readonly is not None:
            self._values["readonly"] = readonly
        if obj is not None:
            self._values["obj"] = obj
        if omit_empty is not None:
            self._values["omit_empty"] = omit_empty

    @builtins.property
    def committed(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether this file should be committed to git or ignored.

        By
        default, all generated files are committed and anti-tamper is used to
        protect against manual modifications.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("committed")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def edit_gitignore(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Update the project's .gitignore file.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("edit_gitignore")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def executable(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be marked as executable.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("executable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def marker(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Adds the projen marker to the file.

        :default: - marker will be included as long as the project is not ejected

        :stability: experimental
        '''
        result = self._values.get("marker")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def readonly(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be readonly.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("readonly")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def obj(self) -> typing.Any:
        '''(experimental) The object that will be serialized.

        You can modify the object's contents
        before synthesis.

        :default: {} an empty object (use ``file.obj`` to mutate).

        :stability: experimental
        '''
        result = self._values.get("obj")
        return typing.cast(typing.Any, result)

    @builtins.property
    def omit_empty(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Omits empty objects and arrays.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("omit_empty")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TomlFileOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Version(Component, metaclass=jsii.JSIIMeta, jsii_type="projen.Version"):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        project: Project,
        *,
        artifacts_directory: builtins.str,
        version_input_file: builtins.str,
        tag_prefix: typing.Optional[builtins.str] = None,
        versionrc_options: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param project: -
        :param artifacts_directory: (experimental) The name of the directory into which ``changelog.md`` and ``version.txt`` files are emitted.
        :param version_input_file: (experimental) A name of a .json file to set the ``version`` field in after a bump.
        :param tag_prefix: (experimental) The tag prefix corresponding to this version.
        :param versionrc_options: (experimental) Custom configuration for versionrc file used by standard-release.

        :stability: experimental
        '''
        options = VersionOptions(
            artifacts_directory=artifacts_directory,
            version_input_file=version_input_file,
            tag_prefix=tag_prefix,
            versionrc_options=versionrc_options,
        )

        jsii.create(self.__class__, self, [project, options])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="STANDARD_VERSION")
    def STANDARD_VERSION(cls) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "STANDARD_VERSION"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bumpTask")
    def bump_task(self) -> Task:
        '''
        :stability: experimental
        '''
        return typing.cast(Task, jsii.get(self, "bumpTask"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="changelogFileName")
    def changelog_file_name(self) -> builtins.str:
        '''(experimental) The name of the changelog file (under ``artifactsDirectory``).

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "changelogFileName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="releaseTagFileName")
    def release_tag_file_name(self) -> builtins.str:
        '''(experimental) The name of the file that contains the release tag (under ``artifactsDirectory``).

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "releaseTagFileName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="unbumpTask")
    def unbump_task(self) -> Task:
        '''
        :stability: experimental
        '''
        return typing.cast(Task, jsii.get(self, "unbumpTask"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionFileName")
    def version_file_name(self) -> builtins.str:
        '''(experimental) The name of the file that contains the version (under ``artifactsDirectory``).

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "versionFileName"))


@jsii.data_type(
    jsii_type="projen.VersionOptions",
    jsii_struct_bases=[],
    name_mapping={
        "artifacts_directory": "artifactsDirectory",
        "version_input_file": "versionInputFile",
        "tag_prefix": "tagPrefix",
        "versionrc_options": "versionrcOptions",
    },
)
class VersionOptions:
    def __init__(
        self,
        *,
        artifacts_directory: builtins.str,
        version_input_file: builtins.str,
        tag_prefix: typing.Optional[builtins.str] = None,
        versionrc_options: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''(experimental) Options for ``Version``.

        :param artifacts_directory: (experimental) The name of the directory into which ``changelog.md`` and ``version.txt`` files are emitted.
        :param version_input_file: (experimental) A name of a .json file to set the ``version`` field in after a bump.
        :param tag_prefix: (experimental) The tag prefix corresponding to this version.
        :param versionrc_options: (experimental) Custom configuration for versionrc file used by standard-release.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "artifacts_directory": artifacts_directory,
            "version_input_file": version_input_file,
        }
        if tag_prefix is not None:
            self._values["tag_prefix"] = tag_prefix
        if versionrc_options is not None:
            self._values["versionrc_options"] = versionrc_options

    @builtins.property
    def artifacts_directory(self) -> builtins.str:
        '''(experimental) The name of the directory into which ``changelog.md`` and ``version.txt`` files are emitted.

        :stability: experimental
        '''
        result = self._values.get("artifacts_directory")
        assert result is not None, "Required property 'artifacts_directory' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version_input_file(self) -> builtins.str:
        '''(experimental) A name of a .json file to set the ``version`` field in after a bump.

        :stability: experimental

        Example::

            "package.json"
        '''
        result = self._values.get("version_input_file")
        assert result is not None, "Required property 'version_input_file' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tag_prefix(self) -> typing.Optional[builtins.str]:
        '''(experimental) The tag prefix corresponding to this version.

        :stability: experimental
        '''
        result = self._values.get("tag_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def versionrc_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(experimental) Custom configuration for versionrc file used by standard-release.

        :stability: experimental
        '''
        result = self._values.get("versionrc_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VersionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class XmlFile(ObjectFile, metaclass=jsii.JSIIMeta, jsii_type="projen.XmlFile"):
    '''(experimental) Represents an XML file.

    Objects passed in will be synthesized using the npm "xml" library.

    :see: https://www.npmjs.com/package/xml
    :stability: experimental
    '''

    def __init__(
        self,
        project: Project,
        file_path: builtins.str,
        *,
        obj: typing.Any = None,
        omit_empty: typing.Optional[builtins.bool] = None,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param project: -
        :param file_path: -
        :param obj: (experimental) The object that will be serialized. You can modify the object's contents before synthesis. Default: {} an empty object (use ``file.obj`` to mutate).
        :param omit_empty: (experimental) Omits empty objects and arrays. Default: false
        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true

        :stability: experimental
        '''
        options = XmlFileOptions(
            obj=obj,
            omit_empty=omit_empty,
            committed=committed,
            edit_gitignore=edit_gitignore,
            executable=executable,
            marker=marker,
            readonly=readonly,
        )

        jsii.create(self.__class__, self, [project, file_path, options])

    @jsii.member(jsii_name="synthesizeContent")
    def _synthesize_content(self, resolver: IResolver) -> typing.Optional[builtins.str]:
        '''(experimental) Implemented by derived classes and returns the contents of the file to emit.

        :param resolver: -

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "synthesizeContent", [resolver]))


@jsii.data_type(
    jsii_type="projen.XmlFileOptions",
    jsii_struct_bases=[ObjectFileOptions],
    name_mapping={
        "committed": "committed",
        "edit_gitignore": "editGitignore",
        "executable": "executable",
        "marker": "marker",
        "readonly": "readonly",
        "obj": "obj",
        "omit_empty": "omitEmpty",
    },
)
class XmlFileOptions(ObjectFileOptions):
    def __init__(
        self,
        *,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
        obj: typing.Any = None,
        omit_empty: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Options for ``XmlFile``.

        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true
        :param obj: (experimental) The object that will be serialized. You can modify the object's contents before synthesis. Default: {} an empty object (use ``file.obj`` to mutate).
        :param omit_empty: (experimental) Omits empty objects and arrays. Default: false

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if committed is not None:
            self._values["committed"] = committed
        if edit_gitignore is not None:
            self._values["edit_gitignore"] = edit_gitignore
        if executable is not None:
            self._values["executable"] = executable
        if marker is not None:
            self._values["marker"] = marker
        if readonly is not None:
            self._values["readonly"] = readonly
        if obj is not None:
            self._values["obj"] = obj
        if omit_empty is not None:
            self._values["omit_empty"] = omit_empty

    @builtins.property
    def committed(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether this file should be committed to git or ignored.

        By
        default, all generated files are committed and anti-tamper is used to
        protect against manual modifications.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("committed")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def edit_gitignore(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Update the project's .gitignore file.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("edit_gitignore")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def executable(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be marked as executable.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("executable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def marker(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Adds the projen marker to the file.

        :default: - marker will be included as long as the project is not ejected

        :stability: experimental
        '''
        result = self._values.get("marker")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def readonly(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be readonly.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("readonly")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def obj(self) -> typing.Any:
        '''(experimental) The object that will be serialized.

        You can modify the object's contents
        before synthesis.

        :default: {} an empty object (use ``file.obj`` to mutate).

        :stability: experimental
        '''
        result = self._values.get("obj")
        return typing.cast(typing.Any, result)

    @builtins.property
    def omit_empty(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Omits empty objects and arrays.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("omit_empty")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "XmlFileOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class YamlFile(ObjectFile, metaclass=jsii.JSIIMeta, jsii_type="projen.YamlFile"):
    '''(experimental) Represents a YAML file.

    :stability: experimental
    '''

    def __init__(
        self,
        project: Project,
        file_path: builtins.str,
        *,
        line_width: typing.Optional[jsii.Number] = None,
        obj: typing.Any = None,
        omit_empty: typing.Optional[builtins.bool] = None,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param project: -
        :param file_path: -
        :param line_width: (experimental) Maximum line width (set to 0 to disable folding). Default: - 0
        :param obj: (experimental) The object that will be serialized. You can modify the object's contents before synthesis. Default: {} an empty object (use ``file.obj`` to mutate).
        :param omit_empty: (experimental) Omits empty objects and arrays. Default: false
        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true

        :stability: experimental
        '''
        options = YamlFileOptions(
            line_width=line_width,
            obj=obj,
            omit_empty=omit_empty,
            committed=committed,
            edit_gitignore=edit_gitignore,
            executable=executable,
            marker=marker,
            readonly=readonly,
        )

        jsii.create(self.__class__, self, [project, file_path, options])

    @jsii.member(jsii_name="synthesizeContent")
    def _synthesize_content(self, resolver: IResolver) -> typing.Optional[builtins.str]:
        '''(experimental) Implemented by derived classes and returns the contents of the file to emit.

        :param resolver: -

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "synthesizeContent", [resolver]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lineWidth")
    def line_width(self) -> jsii.Number:
        '''(experimental) Maximum line width (set to 0 to disable folding).

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "lineWidth"))

    @line_width.setter
    def line_width(self, value: jsii.Number) -> None:
        jsii.set(self, "lineWidth", value)


@jsii.data_type(
    jsii_type="projen.YamlFileOptions",
    jsii_struct_bases=[ObjectFileOptions],
    name_mapping={
        "committed": "committed",
        "edit_gitignore": "editGitignore",
        "executable": "executable",
        "marker": "marker",
        "readonly": "readonly",
        "obj": "obj",
        "omit_empty": "omitEmpty",
        "line_width": "lineWidth",
    },
)
class YamlFileOptions(ObjectFileOptions):
    def __init__(
        self,
        *,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
        obj: typing.Any = None,
        omit_empty: typing.Optional[builtins.bool] = None,
        line_width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Options for ``JsonFile``.

        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true
        :param obj: (experimental) The object that will be serialized. You can modify the object's contents before synthesis. Default: {} an empty object (use ``file.obj`` to mutate).
        :param omit_empty: (experimental) Omits empty objects and arrays. Default: false
        :param line_width: (experimental) Maximum line width (set to 0 to disable folding). Default: - 0

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if committed is not None:
            self._values["committed"] = committed
        if edit_gitignore is not None:
            self._values["edit_gitignore"] = edit_gitignore
        if executable is not None:
            self._values["executable"] = executable
        if marker is not None:
            self._values["marker"] = marker
        if readonly is not None:
            self._values["readonly"] = readonly
        if obj is not None:
            self._values["obj"] = obj
        if omit_empty is not None:
            self._values["omit_empty"] = omit_empty
        if line_width is not None:
            self._values["line_width"] = line_width

    @builtins.property
    def committed(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether this file should be committed to git or ignored.

        By
        default, all generated files are committed and anti-tamper is used to
        protect against manual modifications.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("committed")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def edit_gitignore(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Update the project's .gitignore file.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("edit_gitignore")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def executable(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be marked as executable.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("executable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def marker(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Adds the projen marker to the file.

        :default: - marker will be included as long as the project is not ejected

        :stability: experimental
        '''
        result = self._values.get("marker")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def readonly(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be readonly.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("readonly")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def obj(self) -> typing.Any:
        '''(experimental) The object that will be serialized.

        You can modify the object's contents
        before synthesis.

        :default: {} an empty object (use ``file.obj`` to mutate).

        :stability: experimental
        '''
        result = self._values.get("obj")
        return typing.cast(typing.Any, result)

    @builtins.property
    def omit_empty(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Omits empty objects and arrays.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("omit_empty")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def line_width(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Maximum line width (set to 0 to disable folding).

        :default: - 0

        :stability: experimental
        '''
        result = self._values.get("line_width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "YamlFileOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.Dependency",
    jsii_struct_bases=[DependencyCoordinates],
    name_mapping={
        "name": "name",
        "version": "version",
        "type": "type",
        "metadata": "metadata",
    },
)
class Dependency(DependencyCoordinates):
    def __init__(
        self,
        *,
        name: builtins.str,
        version: typing.Optional[builtins.str] = None,
        type: DependencyType,
        metadata: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''(experimental) Represents a project dependency.

        :param name: (experimental) The package manager name of the dependency (e.g. ``leftpad`` for npm). NOTE: For package managers that use complex coordinates (like Maven), we will codify it into a string somehow.
        :param version: (experimental) Semantic version version requirement. Default: - requirement is managed by the package manager (e.g. npm/yarn).
        :param type: (experimental) Which type of dependency this is (runtime, build-time, etc).
        :param metadata: (experimental) Additional JSON metadata associated with the dependency (package manager specific). Default: {}

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if version is not None:
            self._values["version"] = version
        if metadata is not None:
            self._values["metadata"] = metadata

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) The package manager name of the dependency (e.g. ``leftpad`` for npm).

        NOTE: For package managers that use complex coordinates (like Maven), we
        will codify it into a string somehow.

        :stability: experimental
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''(experimental) Semantic version version requirement.

        :default: - requirement is managed by the package manager (e.g. npm/yarn).

        :stability: experimental
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> DependencyType:
        '''(experimental) Which type of dependency this is (runtime, build-time, etc).

        :stability: experimental
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(DependencyType, result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(experimental) Additional JSON metadata associated with the dependency (package manager specific).

        :default: {}

        :stability: experimental
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Dependency(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IDockerComposeServiceName)
class DockerComposeService(
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.DockerComposeService",
):
    '''(experimental) A docker-compose service.

    :stability: experimental
    '''

    def __init__(
        self,
        service_name: builtins.str,
        *,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        depends_on: typing.Optional[typing.Sequence[IDockerComposeServiceName]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        image: typing.Optional[builtins.str] = None,
        image_build: typing.Optional[DockerComposeBuild] = None,
        ports: typing.Optional[typing.Sequence[DockerComposeServicePort]] = None,
        volumes: typing.Optional[typing.Sequence[IDockerComposeVolumeBinding]] = None,
    ) -> None:
        '''
        :param service_name: -
        :param command: (experimental) Provide a command to the docker container. Default: - use the container's default command
        :param depends_on: (experimental) Names of other services this service depends on. Default: - no dependencies
        :param environment: (experimental) Add environment variables. Default: - no environment variables are provided
        :param image: (experimental) Use a docker image. Note: You must specify either ``build`` or ``image`` key.
        :param image_build: (experimental) Build a docker image. Note: You must specify either ``imageBuild`` or ``image`` key.
        :param ports: (experimental) Map some ports. Default: - no ports are mapped
        :param volumes: (experimental) Mount some volumes into the service. Use one of the following to create volumes:

        :stability: experimental
        '''
        service_description = DockerComposeServiceDescription(
            command=command,
            depends_on=depends_on,
            environment=environment,
            image=image,
            image_build=image_build,
            ports=ports,
            volumes=volumes,
        )

        jsii.create(self.__class__, self, [service_name, service_description])

    @jsii.member(jsii_name="addDependsOn")
    def add_depends_on(self, service_name: IDockerComposeServiceName) -> None:
        '''(experimental) Make the service depend on another service.

        :param service_name: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addDependsOn", [service_name]))

    @jsii.member(jsii_name="addEnvironment")
    def add_environment(self, name: builtins.str, value: builtins.str) -> None:
        '''(experimental) Add an environment variable.

        :param name: environment variable name.
        :param value: value of the environment variable.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addEnvironment", [name, value]))

    @jsii.member(jsii_name="addPort")
    def add_port(
        self,
        published_port: jsii.Number,
        target_port: jsii.Number,
        *,
        protocol: typing.Optional[DockerComposeProtocol] = None,
    ) -> None:
        '''(experimental) Add a port mapping.

        :param published_port: Published port number.
        :param target_port: Container's port number.
        :param protocol: (experimental) Port mapping protocol. Default: DockerComposeProtocol.TCP

        :stability: experimental
        '''
        options = DockerComposePortMappingOptions(protocol=protocol)

        return typing.cast(None, jsii.invoke(self, "addPort", [published_port, target_port, options]))

    @jsii.member(jsii_name="addVolume")
    def add_volume(self, volume: IDockerComposeVolumeBinding) -> None:
        '''(experimental) Add a volume to the service.

        :param volume: -

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addVolume", [volume]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dependsOn")
    def depends_on(self) -> typing.List[IDockerComposeServiceName]:
        '''(experimental) Other services that this service depends on.

        :stability: experimental
        '''
        return typing.cast(typing.List[IDockerComposeServiceName], jsii.get(self, "dependsOn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="environment")
    def environment(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''(experimental) Environment variables.

        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "environment"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ports")
    def ports(self) -> typing.List[DockerComposeServicePort]:
        '''(experimental) Published ports.

        :stability: experimental
        '''
        return typing.cast(typing.List[DockerComposeServicePort], jsii.get(self, "ports"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        '''(experimental) Name of the service.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> typing.List[IDockerComposeVolumeBinding]:
        '''(experimental) Volumes mounted in the container.

        :stability: experimental
        '''
        return typing.cast(typing.List[IDockerComposeVolumeBinding], jsii.get(self, "volumes"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="command")
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Command to run in the container.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "command"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="image")
    def image(self) -> typing.Optional[builtins.str]:
        '''(experimental) Docker image.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "image"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageBuild")
    def image_build(self) -> typing.Optional[DockerComposeBuild]:
        '''(experimental) Docker image build instructions.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[DockerComposeBuild], jsii.get(self, "imageBuild"))


@jsii.implements(IDevEnvironment)
class Gitpod(Component, metaclass=jsii.JSIIMeta, jsii_type="projen.Gitpod"):
    '''(experimental) The Gitpod component which emits .gitpod.yml.

    :stability: experimental
    '''

    def __init__(
        self,
        project: Project,
        *,
        prebuilds: typing.Optional[GitpodPrebuilds] = None,
        docker_image: typing.Optional[DevEnvironmentDockerImage] = None,
        ports: typing.Optional[typing.Sequence[builtins.str]] = None,
        tasks: typing.Optional[typing.Sequence[Task]] = None,
        vscode_extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param project: -
        :param prebuilds: (experimental) Optional Gitpod's Github App integration for prebuilds If this is not set and Gitpod's Github App is installed, then Gitpod will apply these defaults: https://www.gitpod.io/docs/prebuilds/#configure-the-github-app. Default: undefined
        :param docker_image: (experimental) A Docker image or Dockerfile for the container.
        :param ports: (experimental) An array of ports that should be exposed from the container.
        :param tasks: (experimental) An array of tasks that should be run when the container starts.
        :param vscode_extensions: (experimental) An array of extension IDs that specify the extensions that should be installed inside the container when it is created.

        :stability: experimental
        '''
        options = GitpodOptions(
            prebuilds=prebuilds,
            docker_image=docker_image,
            ports=ports,
            tasks=tasks,
            vscode_extensions=vscode_extensions,
        )

        jsii.create(self.__class__, self, [project, options])

    @jsii.member(jsii_name="addCustomTask")
    def add_custom_task(
        self,
        *,
        command: builtins.str,
        before: typing.Optional[builtins.str] = None,
        init: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        open_in: typing.Optional[GitpodOpenIn] = None,
        open_mode: typing.Optional[GitpodOpenMode] = None,
        prebuild: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Add a task with more granular options.

        By default, all tasks will be run in parallel. To run tasks in sequence,
        create a new ``Task`` and set the other tasks as subtasks.

        :param command: (experimental) Required. The shell command to run
        :param before: (experimental) In case you need to run something even before init, that is a requirement for both init and command, you can use the before property.
        :param init: (experimental) The init property can be used to specify shell commands that should only be executed after a workspace was freshly cloned and needs to be initialized somehow. Such tasks are usually builds or downloading dependencies. Anything you only want to do once but not when you restart a workspace or start a snapshot.
        :param name: (experimental) A name for this task. Default: - task names are omitted when blank
        :param open_in: (experimental) You can configure where in the IDE the terminal should be opened. Default: GitpodOpenIn.BOTTOM
        :param open_mode: (experimental) You can configure how the terminal should be opened relative to the previous task. Default: GitpodOpenMode.TAB_AFTER
        :param prebuild: (experimental) The optional prebuild command will be executed during prebuilds. It is meant to run additional long running processes that could be useful, e.g. running test suites.

        :stability: experimental
        '''
        options = GitpodTask(
            command=command,
            before=before,
            init=init,
            name=name,
            open_in=open_in,
            open_mode=open_mode,
            prebuild=prebuild,
        )

        return typing.cast(None, jsii.invoke(self, "addCustomTask", [options]))

    @jsii.member(jsii_name="addDockerImage")
    def add_docker_image(self, image: DevEnvironmentDockerImage) -> None:
        '''(experimental) Add a custom Docker image or Dockerfile for the container.

        :param image: The Docker image.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addDockerImage", [image]))

    @jsii.member(jsii_name="addPorts")
    def add_ports(self, *ports: builtins.str) -> None:
        '''(experimental) Add ports that should be exposed (forwarded) from the container.

        :param ports: The new ports.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addPorts", [*ports]))

    @jsii.member(jsii_name="addPrebuilds")
    def add_prebuilds(
        self,
        *,
        add_badge: typing.Optional[builtins.bool] = None,
        add_check: typing.Optional[builtins.bool] = None,
        add_comment: typing.Optional[builtins.bool] = None,
        add_label: typing.Optional[builtins.bool] = None,
        branches: typing.Optional[builtins.bool] = None,
        master: typing.Optional[builtins.bool] = None,
        pull_requests: typing.Optional[builtins.bool] = None,
        pull_requests_from_forks: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Add a prebuilds configuration for the Gitpod App.

        :param add_badge: (experimental) Add a "Review in Gitpod" button to the pull request's description. Default: false
        :param add_check: (experimental) Add a check to pull requests. Default: true
        :param add_comment: (experimental) Add a "Review in Gitpod" button as a comment to pull requests. Default: false
        :param add_label: (experimental) Add a label once the prebuild is ready to pull requests. Default: false
        :param branches: (experimental) Enable for all branches in this repo. Default: false
        :param master: (experimental) Enable for the master/default branch. Default: true
        :param pull_requests: (experimental) Enable for pull requests coming from this repo. Default: true
        :param pull_requests_from_forks: (experimental) Enable for pull requests coming from forks. Default: false

        :stability: experimental
        '''
        config = GitpodPrebuilds(
            add_badge=add_badge,
            add_check=add_check,
            add_comment=add_comment,
            add_label=add_label,
            branches=branches,
            master=master,
            pull_requests=pull_requests,
            pull_requests_from_forks=pull_requests_from_forks,
        )

        return typing.cast(None, jsii.invoke(self, "addPrebuilds", [config]))

    @jsii.member(jsii_name="addTasks")
    def add_tasks(self, *tasks: Task) -> None:
        '''(experimental) Add tasks to run when gitpod starts.

        By default, all tasks will be run in parallel. To run tasks in sequence,
        create a new ``Task`` and specify the other tasks as subtasks.

        :param tasks: The new tasks.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "addTasks", [*tasks]))

    @jsii.member(jsii_name="addVscodeExtensions")
    def add_vscode_extensions(self, *extensions: builtins.str) -> None:
        '''(experimental) Add a list of VSCode extensions that should be automatically installed in the container.

        These must be in the format defined in the Open VSX registry.

        :param extensions: The extension IDs.

        :see: https://www.gitpod.io/docs/vscode-extensions/
        :stability: experimental

        Example::

            'scala-lang.scala@0.3.9:O5XmjwY5Gz+0oDZAmqneJw=='
        '''
        return typing.cast(None, jsii.invoke(self, "addVscodeExtensions", [*extensions]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="config")
    def config(self) -> typing.Any:
        '''(experimental) Direct access to the gitpod configuration (escape hatch).

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "config"))


class IniFile(ObjectFile, metaclass=jsii.JSIIMeta, jsii_type="projen.IniFile"):
    '''(experimental) Represents an INI file.

    :stability: experimental
    '''

    def __init__(
        self,
        project: Project,
        file_path: builtins.str,
        *,
        obj: typing.Any = None,
        omit_empty: typing.Optional[builtins.bool] = None,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param project: -
        :param file_path: -
        :param obj: (experimental) The object that will be serialized. You can modify the object's contents before synthesis. Default: {} an empty object (use ``file.obj`` to mutate).
        :param omit_empty: (experimental) Omits empty objects and arrays. Default: false
        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true

        :stability: experimental
        '''
        options = IniFileOptions(
            obj=obj,
            omit_empty=omit_empty,
            committed=committed,
            edit_gitignore=edit_gitignore,
            executable=executable,
            marker=marker,
            readonly=readonly,
        )

        jsii.create(self.__class__, self, [project, file_path, options])

    @jsii.member(jsii_name="synthesizeContent")
    def _synthesize_content(self, resolver: IResolver) -> typing.Optional[builtins.str]:
        '''(experimental) Implemented by derived classes and returns the contents of the file to emit.

        :param resolver: -

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "synthesizeContent", [resolver]))


@jsii.data_type(
    jsii_type="projen.IniFileOptions",
    jsii_struct_bases=[ObjectFileOptions],
    name_mapping={
        "committed": "committed",
        "edit_gitignore": "editGitignore",
        "executable": "executable",
        "marker": "marker",
        "readonly": "readonly",
        "obj": "obj",
        "omit_empty": "omitEmpty",
    },
)
class IniFileOptions(ObjectFileOptions):
    def __init__(
        self,
        *,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
        obj: typing.Any = None,
        omit_empty: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Options for ``IniFile``.

        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true
        :param obj: (experimental) The object that will be serialized. You can modify the object's contents before synthesis. Default: {} an empty object (use ``file.obj`` to mutate).
        :param omit_empty: (experimental) Omits empty objects and arrays. Default: false

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if committed is not None:
            self._values["committed"] = committed
        if edit_gitignore is not None:
            self._values["edit_gitignore"] = edit_gitignore
        if executable is not None:
            self._values["executable"] = executable
        if marker is not None:
            self._values["marker"] = marker
        if readonly is not None:
            self._values["readonly"] = readonly
        if obj is not None:
            self._values["obj"] = obj
        if omit_empty is not None:
            self._values["omit_empty"] = omit_empty

    @builtins.property
    def committed(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether this file should be committed to git or ignored.

        By
        default, all generated files are committed and anti-tamper is used to
        protect against manual modifications.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("committed")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def edit_gitignore(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Update the project's .gitignore file.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("edit_gitignore")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def executable(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be marked as executable.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("executable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def marker(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Adds the projen marker to the file.

        :default: - marker will be included as long as the project is not ejected

        :stability: experimental
        '''
        result = self._values.get("marker")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def readonly(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be readonly.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("readonly")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def obj(self) -> typing.Any:
        '''(experimental) The object that will be serialized.

        You can modify the object's contents
        before synthesis.

        :default: {} an empty object (use ``file.obj`` to mutate).

        :stability: experimental
        '''
        result = self._values.get("obj")
        return typing.cast(typing.Any, result)

    @builtins.property
    def omit_empty(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Omits empty objects and arrays.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("omit_empty")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IniFileOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JsonFile(ObjectFile, metaclass=jsii.JSIIMeta, jsii_type="projen.JsonFile"):
    '''(experimental) Represents a JSON file.

    :stability: experimental
    '''

    def __init__(
        self,
        project: Project,
        file_path: builtins.str,
        *,
        newline: typing.Optional[builtins.bool] = None,
        obj: typing.Any = None,
        omit_empty: typing.Optional[builtins.bool] = None,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param project: -
        :param file_path: -
        :param newline: (experimental) Adds a newline at the end of the file. Default: true
        :param obj: (experimental) The object that will be serialized. You can modify the object's contents before synthesis. Default: {} an empty object (use ``file.obj`` to mutate).
        :param omit_empty: (experimental) Omits empty objects and arrays. Default: false
        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true

        :stability: experimental
        '''
        options = JsonFileOptions(
            newline=newline,
            obj=obj,
            omit_empty=omit_empty,
            committed=committed,
            edit_gitignore=edit_gitignore,
            executable=executable,
            marker=marker,
            readonly=readonly,
        )

        jsii.create(self.__class__, self, [project, file_path, options])

    @jsii.member(jsii_name="synthesizeContent")
    def _synthesize_content(self, resolver: IResolver) -> typing.Optional[builtins.str]:
        '''(experimental) Implemented by derived classes and returns the contents of the file to emit.

        :param resolver: -

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "synthesizeContent", [resolver]))


@jsii.data_type(
    jsii_type="projen.JsonFileOptions",
    jsii_struct_bases=[ObjectFileOptions],
    name_mapping={
        "committed": "committed",
        "edit_gitignore": "editGitignore",
        "executable": "executable",
        "marker": "marker",
        "readonly": "readonly",
        "obj": "obj",
        "omit_empty": "omitEmpty",
        "newline": "newline",
    },
)
class JsonFileOptions(ObjectFileOptions):
    def __init__(
        self,
        *,
        committed: typing.Optional[builtins.bool] = None,
        edit_gitignore: typing.Optional[builtins.bool] = None,
        executable: typing.Optional[builtins.bool] = None,
        marker: typing.Optional[builtins.bool] = None,
        readonly: typing.Optional[builtins.bool] = None,
        obj: typing.Any = None,
        omit_empty: typing.Optional[builtins.bool] = None,
        newline: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Options for ``JsonFile``.

        :param committed: (experimental) Indicates whether this file should be committed to git or ignored. By default, all generated files are committed and anti-tamper is used to protect against manual modifications. Default: true
        :param edit_gitignore: (experimental) Update the project's .gitignore file. Default: true
        :param executable: (experimental) Whether the generated file should be marked as executable. Default: false
        :param marker: (experimental) Adds the projen marker to the file. Default: - marker will be included as long as the project is not ejected
        :param readonly: (experimental) Whether the generated file should be readonly. Default: true
        :param obj: (experimental) The object that will be serialized. You can modify the object's contents before synthesis. Default: {} an empty object (use ``file.obj`` to mutate).
        :param omit_empty: (experimental) Omits empty objects and arrays. Default: false
        :param newline: (experimental) Adds a newline at the end of the file. Default: true

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if committed is not None:
            self._values["committed"] = committed
        if edit_gitignore is not None:
            self._values["edit_gitignore"] = edit_gitignore
        if executable is not None:
            self._values["executable"] = executable
        if marker is not None:
            self._values["marker"] = marker
        if readonly is not None:
            self._values["readonly"] = readonly
        if obj is not None:
            self._values["obj"] = obj
        if omit_empty is not None:
            self._values["omit_empty"] = omit_empty
        if newline is not None:
            self._values["newline"] = newline

    @builtins.property
    def committed(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether this file should be committed to git or ignored.

        By
        default, all generated files are committed and anti-tamper is used to
        protect against manual modifications.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("committed")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def edit_gitignore(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Update the project's .gitignore file.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("edit_gitignore")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def executable(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be marked as executable.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("executable")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def marker(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Adds the projen marker to the file.

        :default: - marker will be included as long as the project is not ejected

        :stability: experimental
        '''
        result = self._values.get("marker")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def readonly(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether the generated file should be readonly.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("readonly")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def obj(self) -> typing.Any:
        '''(experimental) The object that will be serialized.

        You can modify the object's contents
        before synthesis.

        :default: {} an empty object (use ``file.obj`` to mutate).

        :stability: experimental
        '''
        result = self._values.get("obj")
        return typing.cast(typing.Any, result)

    @builtins.property
    def omit_empty(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Omits empty objects and arrays.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("omit_empty")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def newline(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Adds a newline at the end of the file.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("newline")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JsonFileOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.TaskStep",
    jsii_struct_bases=[TaskStepOptions],
    name_mapping={
        "cwd": "cwd",
        "name": "name",
        "builtin": "builtin",
        "exec": "exec",
        "say": "say",
        "spawn": "spawn",
    },
)
class TaskStep(TaskStepOptions):
    def __init__(
        self,
        *,
        cwd: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        builtin: typing.Optional[builtins.str] = None,
        exec: typing.Optional[builtins.str] = None,
        say: typing.Optional[builtins.str] = None,
        spawn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) A single step within a task.

        The step could either be  the execution of a
        shell command or execution of a sub-task, by name.

        :param cwd: (experimental) The working directory for this step. Default: - determined by the task
        :param name: (experimental) Step name. Default: - no name
        :param builtin: (experimental) The name of a built-in task to execute. Built-in tasks are node.js programs baked into the projen module and as component runtime helpers. The name is a path relative to the projen lib/ directory (without the .task.js extension). For example, if your built in builtin task is under ``src/release/resolve-version.task.ts``, then this would be ``release/resolve-version``. Default: - do not execute a builtin task
        :param exec: (experimental) Shell command to execute. Default: - don't execute a shell command
        :param say: (experimental) Print a message. Default: - don't say anything
        :param spawn: (experimental) Subtask to execute. Default: - don't spawn a subtask

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if cwd is not None:
            self._values["cwd"] = cwd
        if name is not None:
            self._values["name"] = name
        if builtin is not None:
            self._values["builtin"] = builtin
        if exec is not None:
            self._values["exec"] = exec
        if say is not None:
            self._values["say"] = say
        if spawn is not None:
            self._values["spawn"] = spawn

    @builtins.property
    def cwd(self) -> typing.Optional[builtins.str]:
        '''(experimental) The working directory for this step.

        :default: - determined by the task

        :stability: experimental
        '''
        result = self._values.get("cwd")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Step name.

        :default: - no name

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def builtin(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of a built-in task to execute.

        Built-in tasks are node.js programs baked into the projen module and as
        component runtime helpers.

        The name is a path relative to the projen lib/ directory (without the .task.js extension).
        For example, if your built in builtin task is under ``src/release/resolve-version.task.ts``,
        then this would be ``release/resolve-version``.

        :default: - do not execute a builtin task

        :stability: experimental
        '''
        result = self._values.get("builtin")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exec(self) -> typing.Optional[builtins.str]:
        '''(experimental) Shell command to execute.

        :default: - don't execute a shell command

        :stability: experimental
        '''
        result = self._values.get("exec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def say(self) -> typing.Optional[builtins.str]:
        '''(experimental) Print a message.

        :default: - don't say anything

        :stability: experimental
        '''
        result = self._values.get("say")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spawn(self) -> typing.Optional[builtins.str]:
        '''(experimental) Subtask to execute.

        :default: - don't spawn a subtask

        :stability: experimental
        '''
        result = self._values.get("spawn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TaskStep(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Component",
    "CreateProjectOptions",
    "Dependencies",
    "Dependency",
    "DependencyCoordinates",
    "DependencyType",
    "DepsManifest",
    "DevEnvironmentDockerImage",
    "DevEnvironmentOptions",
    "DockerCompose",
    "DockerComposeBuild",
    "DockerComposePortMappingOptions",
    "DockerComposeProps",
    "DockerComposeProtocol",
    "DockerComposeService",
    "DockerComposeServiceDescription",
    "DockerComposeServicePort",
    "DockerComposeVolumeConfig",
    "DockerComposeVolumeMount",
    "FileBase",
    "FileBaseOptions",
    "GitAttributesFile",
    "Gitpod",
    "GitpodOnOpen",
    "GitpodOpenIn",
    "GitpodOpenMode",
    "GitpodOptions",
    "GitpodPort",
    "GitpodPortVisibility",
    "GitpodPrebuilds",
    "GitpodTask",
    "IDevEnvironment",
    "IDockerComposeServiceName",
    "IDockerComposeVolumeBinding",
    "IDockerComposeVolumeConfig",
    "IResolvable",
    "IResolver",
    "IgnoreFile",
    "IniFile",
    "IniFileOptions",
    "InitProject",
    "InitProjectOptionHints",
    "JsonFile",
    "JsonFileOptions",
    "License",
    "LicenseOptions",
    "LogLevel",
    "Logger",
    "LoggerOptions",
    "Makefile",
    "MakefileOptions",
    "ObjectFile",
    "ObjectFileOptions",
    "Project",
    "ProjectBuild",
    "ProjectOptions",
    "ProjectType",
    "Projects",
    "Projenrc",
    "ProjenrcOptions",
    "Renovatebot",
    "RenovatebotOptions",
    "RenovatebotScheduleInterval",
    "ResolveOptions",
    "Rule",
    "SampleDir",
    "SampleDirOptions",
    "SampleFile",
    "SampleFileOptions",
    "SampleReadme",
    "SampleReadmeProps",
    "Semver",
    "SourceCode",
    "SourceCodeOptions",
    "Task",
    "TaskCommonOptions",
    "TaskOptions",
    "TaskRuntime",
    "TaskSpec",
    "TaskStep",
    "TaskStepOptions",
    "Tasks",
    "TasksManifest",
    "Testing",
    "TextFile",
    "TextFileOptions",
    "TomlFile",
    "TomlFileOptions",
    "Version",
    "VersionOptions",
    "XmlFile",
    "XmlFileOptions",
    "YamlFile",
    "YamlFileOptions",
    "awscdk",
    "build",
    "cdk",
    "cdk8s",
    "cdktf",
    "github",
    "gitlab",
    "java",
    "javascript",
    "python",
    "release",
    "typescript",
    "vscode",
    "web",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import awscdk
from . import build
from . import cdk
from . import cdk8s
from . import cdktf
from . import github
from .github import workflows
from . import gitlab
from . import java
from . import javascript
from . import python
from . import release
from . import typescript
from . import vscode
from . import web
