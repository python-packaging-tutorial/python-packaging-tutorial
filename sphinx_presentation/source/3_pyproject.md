# The pyproject.toml file

Much research software is initially developed by hacking away in an interactive
setting, such as in a [Jupyter Notebook](https://jupyter.org) or a Python shell.
However, at some point when you have a more-complicated workflow that you want
to repeat, and/or make available to others, it makes sense to package your
functions into modules and ultimately a software package that can be installed.
This lesson will walk you through that process.

Consider the `rescale()` function written as an exercise in the Software
Carpentry [Programming with Python](https://swcarpentry.github.io/python-novice-inflammation/08-func/index.html)
lesson.

First, as needed, create your virtual environment and install NumPy with

```console
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install numpy
```

Then, in a Python shell or Jupyter Notebook, declare the function:

```python
import numpy as np

def rescale(input_array):
    """Rescales an array from 0 to 1.

    Takes an array as input, and returns a corresponding array scaled so that 0
    corresponds to the minimum and 1 to the maximum value of the input array.
    """
    L = np.min(input_array)
    H = np.max(input_array)
    output_array = (input_array - L) / (H - L)
    return output_array
```

and call the function:

```python
>>> rescale(np.linspace(0, 100, 5))
array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ])
```

## Creating our package in six lines

Let's create a Python package that contains this function.

First, create a new directory for your software package, called `package`, and move into that:

```console
$ mkdir package
$ cd package
```

You should immediately initialize an empty Git repository in this directory; if
you need a refresher on using Git for version control, check out the Software
Carpentry [Version Control with Git](https://swcarpentry.github.io/git-novice/)
lesson.  (This lesson will not explicitly remind you to commit your work after
this point.)

```console
$ git init
```

Next, we want to create the necessary directory structure for your package.
This includes:
- a `src` directory, which will contain another directory called `rescale` for the source files of your package itself;
- a `tests` directory, which will hold tests for your package and its modules/functions (this can also go inside the `rescale` directory, but we recommend keeping it at the top level so that your test suite is not installed along with the package itself);
- a `docs` directory, which will hold the files necessary for documenting your software package.

```console
$ mkdir -p src/rescale tests docs
```

(The `-p` flag tells `mkdir` to create the `src` parent directory for `rescale`.)

Putting the package directory and source code inside the `src` directory is not actually *required*;
instead, if you put the `<package_name>` directory at the same level as `tests` and `docs` then you could actually import or call the package directory from that location.
However, this can cause several issues, such as running tests with the local version instead of the installed version.
In addition, this package structure matches that of compiled languages, and lets your package easily contain non-Python compiled code, if necessary.

Inside `src/rescale`, create the files `__init__.py` and `rescale.py`:

```console
$ touch src/rescale/__init__.py src/rescale/rescale.py
```

`__init__.py` is required to import this directory as a package, and should remain empty (for now).
`rescale.py` is the module inside this package that will contain the `rescale()` function;
copy the contents of that function into this file. (Don't forget the NumPy import!)

The last element your package needs is a `pyproject.toml` file. Create this with

```console
$ touch pyproject.toml
```

and then provide the minimally required metadata, which include information about the build system (hatchling) and the package itself (`name` and `version`):

```toml
# contents of pyproject.toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "package"
version = "0.1.0"
```

The package name given here, "package," matches the directory `package` that contains our project's code. We've chosen 0.1.0 as the starting version for this package; you'll see more in a later episode about versioning, and how to specify this without manually writing it here.

The only elements of your package truly **required** to install and import it are the `pyproject.toml`, `__init__.py`, and `rescale.py` files.
At this point, your package's file structure should look like this:

```bash
.
├── docs
├── pyproject.toml
├── src
│   └── package
│   │   ├── __init__.py
│   │   └── rescale.py
└── tests
```

## Installing and using your package

Now that your package has the necessary elements, you can install it into your virtual environment (which should already be active). From the top level of your project's directory, enter

```bash
$ pip install -e .
```

The `-e` flag tells `pip` to install in editable mode, meaning that you can continue developing your package on your computer as you test it.

Then, in a Python shell or Jupyter Notebook, import your package and call the (single) function:

```python
>>> import numpy as np
>>> from package.rescale import rescale
>>> rescale(np.linspace(0, 100, 5))
```

```
array([0.  , 0.25, 0.5 , 0.75, 1.  ])
```
{: .output}

This matches the output we expected based on our interactive testing above! 😅

## Your first test

Now that we have installed our package and we have manually tested that it works, let's set up this situation as a test that can be automatically run using `nox` and `pytest`.

In the `tests` directory, create the `test_rescale.py` file:

```bash
touch tests/test_rescale.py
```

In this file, we need to import the package, and check that a call to the `rescale` function with our known input returns the expected output:
```python
# contents of tests/test_rescale.py
import numpy as np
from package.rescale import rescale

def test_rescale():
    np.testing.assert_allclose(
        rescale(np.linspace(0, 100, 5)),
        np.array([0., 0.25, 0.5, 0.75, 1.0 ]),
        )
```

Next, take the `noxfile.py` you created in an earlier episode, and modify it to
 - install `numpy`, necessary to run the package;
 - install `pytest`, necessary to automatically find and run the test(s);
 - install the package itself; and
 - run the test(s)

with:

```python
# contents of noxfile.py
import nox

@nox.session
def tests(session):
    session.install('numpy', 'pytest')
    session.install('.')
    session.run('pytest')
```

Now, with the added test file and `noxfile.py`, your package's directory structure should look like:

```bash
.
├── docs
├── noxfile.py
├── pyproject.toml
├── src
│   └── package
│   │   ├── __init__.py
│   │   └── rescale.py
└── tests
    └── test_rescale.py
```

(You may also see some `__pycache__` directories, which contain compiled Python bytecode that was generated when calling your package.)

Have `nox` run your tests. This should give you some information about what
`nox` is doing, and show output along the lines of

```console
$ nox
nox > Running session tests
nox > Creating virtual environment (virtualenv) using python in .nox/tests
nox > python -m pip install numpy pytest
nox > python -m pip install .
nox > pytest
======================================================================= test session starts =================================================
platform darwin -- Python 3.9.13, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/niemeyek/Desktop/rescale
collected 1 item

tests/test_rescale.py .                                                                                                                [100%]

======================================================================== 1 passed in 0.07s ==================================================
nox > Session tests was successful.
```

This tells us that the output of the test function matches the expected result, and therefore the test passes! 🎉

We now have a package that is installed, can be interacted with properly, and has a passing test.
Next, we'll look at other files that should be included with your package.


## Informational metadata

We left the metadata in our `project.toml` quite minimal; we just had
a name and a version. There are quite a few other fields that can really help
your package on PyPI, however. We'll look at them, split into categories:
Informational (like author, description) and Functional (like requirements).
There's also a special `dynamic` field that lets you list values that are going
to come from some other source.

### Name

Required. `.`, `-`, and `_` are all equivalent characters, and may be normalized
to `_`. Case is unimportant. This is the only field that must exist statically
in this table.

```toml
name = "some_project"
```

### Version

Required. Many backends provide ways to read this from a file or from a version
control system, so in those cases you would add `"version"` to the `dynamic`
field and leave it off here.

```toml
version = "1.2.3"
version = "0.2.1b1"
```


### Description

A string with a short description of your project.


```toml
description = "This is a very short summary of a very cool project."
```



### Readme

The name of the readme. Most of the time this is `README.md` or `README.rst`,
though there is a more complex mechanism if a user really desires to embed the
readme into your `pyproject.toml` file (you don't).

```toml
readme = "README.md"
readme = "README.rst"
```

### Authors and maintainers

This is a list of authors (or maintainers) as (usually inline) tables. A TOML table is very much like a Python dict.

```python
authors = [
    {name="Me Myself", email="email@mail.com"},
    {name="You Yourself", email="email2@mail.com"},
]
maintainers = [
    {name="It Itself", email="email3@mail.com"},
]
```

Note that TOML supports two ways two write tables and two ways to write arrays, so you might see this in a different form, but it should be recognizable.

### Keywords

A list of keywords for the project. This is mostly used to improve searchability.

```toml
keywords = ["example", "tutorial"]
```

### URLs

A set of links to help users find various things for your code; some common ones
are `Homepage`, `Source Code`, `Documentation`, `Bug Tracker`, `Changelog`,
`Discussions`, and `Chat`. It's a free-form name, though many common names get
recognized and have nice icons on PyPI.

```toml
# Inline form
urls.Homepage = "https://pypi.org"
urls."Source Code" = "https://pypi.org"

# Sectional form
[project.urls]
Homepage = "https://pypi.org"
"Source Code" = "https://pypi.org"
```

### Classifiers

This is a collection of classifiers as listed at
<https://pypi.org/classifiers/>. You select the classifiers that match your
projects from there. Usually, this includes a "Development Status" to tell users
how stable you think your project is, and a few things like "Intended Audience"
and "Topic" to help with search engines. There are some important ones though:
the "License" (s) is used to indicate your license. You also can give an idea of
supported Python versions, Python implementations, and "Operating System"s as
well. If you have statically typed Python code, you can tell users about that,
too.

```toml
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Information Analysis",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Topic :: Scientific/Engineering :: Physics",
    "Typing :: Typed",
]
```

### License (special mention)

There also is a license field, but that was rather inadequate; it didn't support
multiple licenses, for example. Currently, it's best to indicate the license
with a Trove Classifier, and make sure your file is called `LICENSE*` so build
backends pick it up and include it in SDist and wheels. There's work on
standardizing an update to the format in the future. You can manually specify a
license file if you want:

```toml
license = {file = "LICENSE"}
```

:::{admonition} Verify file contents
Always verify the contents of your SDist and Wheel(s) manually to make sure the license file is included.
```bash
tar -tvf dist/package-0.0.1.tar.gz
unzip -l dist/package-0.0.1-py3-none-any.whl
```
:::

## Functional metadata

The remaining fields actually change the usage of the package.

### Requires-Python

This is an important and sometimes misunderstood field. It looks like this:

```toml
requires-python = ">=3.7"
```

Pip will see if the current version of Python it's installing for passes this
expression. If it doesn't, pip will start checking older versions of the package
until it finds on that passes. This is how `pip install numpy` still works on
Python 3.7, even though NumPy has already dropped support for it.

You need to make sure you always have this and it stays accurate, since you
can't edit metadata after releasing - you can only yank or delete release(s) and
try again.

:::{admonition} Upper caps
Upper caps are generally discouraged in the Python ecosystem, but they are (even
more that usual) broken here, since this field was added to help users drop old
Python versions, and the idea it would be used to restrict newer versions was
not considered. The above procedures is not the right one for an upper cap!
Never upper cap this and instead use Trove Classifiers to tell users what
versions of Python your code was tested with.
:::

### Dependencies

Your package likely will need other packages from PyPI to run.

```toml
dependencies = [
  "numpy>=1.18",
]
```

You can list dependencies here without minimum versions, but if you have a lot of users, you might want minimum versions; pip will only upgrade an installed package if it's no longer viable via your requirements. You can also use a variety of markers to specify operating system specific packages.

:::{admonition} project.dependencies vs. build-system.requires

What is the difference between `project.dependencies` vs. `build-system.requires`?
<details><summary>Answer</summary>

`build-system.requires` describes what your project needs to "build", that is,
produce an SDist or wheel. Installing a built wheel will _not_ install anything
from `build-system.requires`, in fact, the `pyproject.toml` is not even present
in the wheel! `project.dependencies`, on the other hand, is added to the wheel
metadata, and pip will install anything in that field if not already present
when installing your wheel.

</details>
:::

### Optional Dependencies

Sometimes you have dependencies that are only needed some of the time. These can
be specified as optional dependencies. Unlike normal dependencies, these are
specified in a table, with the key being the option you pass to pip to install
it. For example:

```toml
[project.optional-dependenices]
test = ["pytest>=6"]
check = ["flake8"]
plot = ["matplotlib"]
```

Now, you can run `pip install 'package[test,check]'`, and pip will install both
the required and optional dependencies `pytest` and `flake8`, but not
`matplotlib`.

### Entry Points

A Python package can have entry points. There are three kinds: command-line
entry points (`scripts`), graphical entry points (`gui-scripts`), and general
entry points (`entry-points`). As an example, let's say you have a `main()`
function inside `__main__.py` that you want to run to create a command
`project-cli`. You'd write:

```toml
[project.scripts]
project-cli = "project.__main__:main"
```

The command line name is the table key, and the form of the entry point is
`package.module:function`. Now, when you install your package, you'll be able to
type `project-cli` on the command line and it will run your Python function.

## Dynamic

Any field from above that are specified by your build backend instead should be
listed in the special `dynamic` field.  For example, if you want `hatchling` to
read `__version__.py` from `src/package/__init__.py`:

```toml
[project]
name = "package"
dynamic = ["version"]

[tool.hatch]
version.path = "src/package/__init__.py"
```

## All together


Now let's take our previous example and expand it with more information. Here's an example:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "package"
version = "0.0.1"
authors = [
  { name="Example Author", email="author@example.com" },
]
description = "A small example package"
readme = "README.md"
license = { file="LICENSE" }
requires-python = ">=3.7"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
"Homepage" = "https://github.com/pypa/sampleproject"
"Bug Tracker" = "https://github.com/pypa/sampleproject/issues"
```
