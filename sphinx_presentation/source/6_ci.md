# Continuous Integration

Continuous Integration (CI) allows you to perform tasks on a server
for various events on your repository (called triggers). For example,
you can use GitHub Actions (GHA) to run a test suite on every pull request.

GHA is made up of workflows which consist of actions. Workflows are files
in the `.github/workflows` folder ending in `.yml`.

## Triggers

Workflows start with triggers, which define when things run. Here are three
triggers:

```yaml
on:
  pull_request:
  push:
    branches:
      - main
```

This will run on all pull requests and pushes to main. You can also specify
specific branches for pull requests instead of running on all PRs (will run on
PRs targeting those branches only).

## Running unit tests

Let's set up a basic test. We will define a jobs dict, with a single job named
"tests". For all jobs, you need to select an image to run on - there are images
for Linux, macOS, and Windows. We'll use `ubuntu-latest`.

```yaml
jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Install package
        run: python -m pip install -e .[test]

      - name: Test package
        run: python -m pytest
```

This has five steps:

1. Checkout the source (your repo).
2. Prepare Python 3.10 (will use a preinstalled version if possible, otherwise will download a binary).
3. Install your package with testing extras - this is just an image that will be removed at the end of the run, so "global" installs are fine. We also provide a nice name for the step.
4. Run your package's tests.

By default, if any step fails, the run immediately quits and fails.


## Running in a matrix

You can parametrize values, such as Python version or operating system. Do do
this, make a `strategy: matrix:` dict. Every key in that dict (except `include:`
and `exclude` should be set with a list, and a job will be generated with every
possible combination of values. You can access these values via the `matrix`
variable; they do not "automatically" change anything.

For example:

```yaml
example:
  strategy:
    matrix:
      onetwothree: [1, 2, 3]
  name: Job ${{ matrix.onetwothree }}
```


would produce three jobs, with names `Job 1`, `Job 2`, and `Job 3`. Elsewhere,
if you refer to the `exmaple` job, it will implicitly refer to all three.

This is commonly used to set Python and operating system versions:

```yaml
tests:
  strategy:
    fail-fast: false
    matrix:
      python-version: ["3.7", "3.11"]
      runs-on: [ubuntu-latest, windows-latest, macos-latest]
  name: Check Python ${{ matrix.python-version }} on ${{ matrix.runs-on }}
  runs-on: ${{ matrix.runs-on }}
  steps:
    - uses: actions/checkout@v3
      with:
        fetch-depth: 0 # Only needed if using setuptools-scm

    - name: Setup Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install package
      run: python -m pip install -e .[test]

    - name: Test package
      run: python -m pytest
```

There are two special keys: `include:` will take a list of jobs to include one
at a time. For example, you could add Python 3.9 on Linux (but not the others):

```yaml
include:
  - python-version: 3.9
    runs-on: ubuntu-latest
```

`include` can also list more keys than were present in the original
parametrization; this will add a key to an existing job.

The `exclude:` key does the opposite, and lets you remove jobs from the matrix.

## Other actions

GitHub Actions has the concept of actions, which are just GitHub repositories of the form `org/name@tag`, and there are lots of useful actions to choose from (and you can write your own by composing other actions, or you can also create them with JavaScript or Dockerfiles). Here are a few:

There are some GitHub supplied ones:

- [actions/checkout](https://github.com/actions/checkout): Almost always the first action. v2+ does not keep Git history unless `with: fetch-depth: 0` is included (important for SCM versioning). v1 works on very old docker images.
- [actions/setup-python](https://github.com/actions/setup-python): Do not use v1; v2+ can setup any Python, including uninstalled ones and pre-releases. v4 requires a Python version to be selected.
- [actions/cache](https://github.com/actions/cache): Can store files and restore them on future runs, with a settable key.
- [actions/upload-artifact](https://github.com/actions/upload-artifact): Upload a file to be accessed from the UI or from a later job.
- [actions/download-artifact](https://github.com/actions/download-artifact): Download a file that was previously uploaded, often for releasing. Match upload-artifact version.

And many other useful ones:

- [ilammy/msvc-dev-cmd](https://github.com/ilammy/msvc-dev-cmd): Setup MSVC compilers.
- [jwlawson/actions-setup-cmake](https://github.com/jwlawson/actions-setup-cmake): Setup any version of CMake on almost any image.
- [wntrblm/nox](https://github.com/wntrblm/nox): Setup all versions of Python and provide nox.
- [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish): Publish Python packages to PyPI.
- [pre-commit/action](https://github.com/pre-commit/action): Run pre-commit with built-in caching.
- [conda-incubator/setup-miniconda](https://github.com/conda-incubator/setup-miniconda): Setup conda or mamba on GitHub Actions.
- [peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages): Deploy built files to to GitHub Pages
- [ruby/setup-miniconda](https://github.com/ruby/setup-ruby) Setup Ruby if you need it for something.


## Exercise

Add a CI file for your package.
