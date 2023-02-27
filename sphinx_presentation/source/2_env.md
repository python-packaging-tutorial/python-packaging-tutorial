# Environments and task runners

You will see two _very_ common recommendations when installing a package:

```console
$ pip install <package>         # Use only in virtual environment!
$ pip install --user <package>  # Almost never use
```

Don't use them unless you know exactly what you are doing! The first one will
try to install globally, and if you don't have permission, will install to your
user site packages. In global site packages, you can get conflicting versions
of libraries, you can't tell what you've installed for what, packages can
update and break your system; it's a mess. And user site packages are worse,
because all installs of Python on your computer share it, so you might override
and break things you didn't intend to. And with pip's new smart solver,
updating packages inside a global environment can take many minutes and produce
unexpectedly solves that are technically "correct" but don't work because it
backsolved conflicts to before issues were discovered.

There is a solution: virtual environments (libraries) or pipx (applications).

There are likely a _few_ libraries (ideally just `pipx`) that you just have to
install globally. Go ahead, but be careful (and always use your system package
manager instead if you can, like [`brew` on macOS](https://brew.sh) or the
Windows ones -- Linux package managers tend to be too old to use for Python libraries).


## Virtual Environments

:::{note}
The following uses the standard library `venv` module. The `virtualenv`
module can be installed from PyPI, and works identically, though is a bit
faster and provides newer pip by default.
:::

Python 3 comes with the `venv` module built-in, which supports making virtual environments.
To make one, you call the module with


```console
$ python3 -m venv .venv
```

This creates links to Python and pip in `.venv/bin`, and creates a
site-packages directory at `.venv/lib`. You can just use `.venv/bin/python` if
you want, but many users prefer to source the activation script:

```console
$ . .venv/bin/activate
```

(Shell specific, but there are activation scripts for all common shells here).
Now `.venv/bin` has been added to your PATH, and usually your shell's prompt
will be modified to indicate you are "in" a virtual environment. You can now
use `python`, `pip`, and anything you install into the virtualenv without
having to prefix it with `.venv/bin/`.

:::{attention}
Check the version of pip installed! If it's old, you might want to run
`pip install -U pip` or, for modern versions of Python, you can add
`--upgrade-deps` to the venv creation line.
:::

To "leave" the virtual environment, you
undo those changes by running the deactivate function the activation added to
your shell:

```bash
deactivate
```

:::{admonition} What about conda?

The same concerns apply to Conda. You should avoid installing things to the
`base` environment, and instead make environments and use those above. Quick tips:

```console
$ conda config --set auto_activate_base false  # turn off the default environment
$ conda env create -n some_name  # or use paths with `-p`
$ conda activate some_name
$ conda deactivate
```
:::


## Pipx

There are many Python packages that provide a command line interface and are
not really intended to be imported (`pip`, for example, should not be
imported). It is really inconvenient to have to set up venvs for every command
line tool you want to install, however. `pipx`, from the makers of `pip`,
solves this problem for you.  If you `pipx install` a package, it will be
created inside a new virtual environment, and just the executable scripts will
be exposed in your regular shell.

Pipx also has a `pipx run <package>` command, which will download a package and
run a script of the same name, and will cache the temporary environment for a
week. This means you have all of PyPI at your fingertips in one line on any
computer that has pipx installed!

## Task runner (nox)


A task runner, like [make][] (fully general), [rake][] (Ruby general),
[invoke][] (Python general), [tox][] (Python packages), or [nox][] (Python
simi-general), is a tool that lets you specify a set of tasks via a common
interface. These can be a crutch, allowing poor packaging practices to be
employed behind a custom script, and they can hide what is actually happening.

Nox has two strong points that help with this concern. First, it is very
explicit, and even prints what it is doing as it operates. Unlike the older
tox, it does not have any implicit assumptions built-in. Second, it has very
elegant built-in support for both virtual and Conda environments. This can
greatly reduce new contributor friction with your codebase.

A daily developer is not expected to use nox for simple tasks, like running
tests or linting. You should not rely on nox to make a task that should be made
simple and standard (like building a package) complicated. You are not expected
to use nox for linting on CI, or sometimes even for testing on CI, even if
those tasks are provided for users. Nox is a few seconds slower than running
directly in a custom environment - but for new users and rarely run tasks, it
is _much_ faster than explaining how to get setup or manually messing with
virtual environments. It is also highly reproducible, creating and destroying
the temporary environment each time by default.

You should use nox to make it easy and simple for new contributors to run
things. You should use nox to make specialized developer tasks easy. You should
use nox to avoid making single-use virtual environments for docs and other
rarely run tasks.

[nox]: https://nox.thea.codes
[tox]: https://tox.readthedocs.io
[invoke]: https://www.pyinvoke.org
[rake]: https://ruby.github.io/rake/
[make]: https://www.gnu.org/software/make/

Since nox is an application, you should install it with `pipx`. If you use
Homebrew, you can install `nox` with that (Homebrew isolates Python apps it
distributes too, just like pipx).

## Running nox

If you see a `noxfile.py` in a repository, that means nox is supported. You can start
by checking to see what the different tasks (called `sessions` in nox) are provided
by the noxfile author. For example, if we do this on `packaging.python.org`'s repository:

```console
$ nox -l  # or --list-sessions
Sessions defined in /github/pypa/packaging.python.org/noxfile.py:

- translation -> Build the gettext .pot files.
- build -> Make the website.
- preview -> Make and preview the website.
- linkcheck -> Check for broken links.

sessions marked with * are selected, sessions marked with - are skipped.
```

You can see that there are several different sessions. You can run them with `-s`:

```console
$ nox -s preview
```

Will build and start up a preview of the site.

If you need to pass options to the session, you can separate nox options with
and the session options with `--`.

## Writing a Noxfile

For this example, we'll need a minimal test file for pytest to run. Let's make
this file in a local directory:

```python
# test_nox.py

def test_runs():
    assert True
```

Let's write our own noxfile. If you are familiar with pytest, this should look
familiar as well; it's intentionally rather close to pytest. We'll make a
minimal session that runs pytest:

```python
# noxfile.py
import nox

@nox.session()
def tests(session):
    session.install("pytest")
    session.run("pytest")
```

A noxfile is valid Python, so we import nox. The session decorator tells nox
that this function is going to be a session. By default, the name will be the
function name, the description will be the function docstring, it will run on
the current version of Python (the one nox is using), and it will make a
virtual environment each time the session runs, though all of this is
changeable via keyword arguments to session.

The session function will be given a `nox.Session` object that has various
useful methods. `.install` will install things with pip, and `.run` will run a
command in a sesson. The `.run` command will print a warning if you use an
executable outside the virtual environment unless `external=True` is passed.
Errors will exit the session.

Let's expand this a little:


```python
# noxfile.py
import nox

@nox.session()
def tests(session: nox.Session) -> None:
    """
    Run our tests.
    """
    session.install("pytest")
    session.run("pytest", *session.posargs)
```

This adds a type annotation to the session object, so that IDE's and type
checkers can help you write the code in the function. There's a docstring,
which will print out nice help text when a user lists the sessions. And we pass
through to pytest anything the user passes in via `session.posargs`


Let's try running it:

```console
$ nox -s tests
nox > Running session tests
nox > Creating virtual environment (virtualenv) using python3.10 in .nox/tests
nox > python -m pip install pytest
nox > pytest
==================================== test session starts ====================================
platform darwin -- Python 3.10.5, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/henryschreiner/git/teaching/packaging
collected 1 item

test_nox.py .                                                                          [100%]

===================================== 1 passed in 0.05s =====================================
nox > Session tests was successful.
```




Nox is really just doing the same thing we would do manually (and printing all
the steps except the exact details of creating the virtual environment). You can
see the virtual environment in `.nox/tests`!



:::{admonition} Passing arguments through
Try passing `-v` to pytest.


<details><summary>Solution</summary>

```console
$ nox -s tests -- -v
```

</details>

:::

:::{admonition} Virtual environments
How would you activate this environment?


<details><summary>Solution</summary>

```console
$ source .nox/tests/bin/activate
```

</details>

:::

In general, packages you work on daily are worth fully setting up with virtual
environments, but if you are new to development or just occasionally
contributing to a package, nox is a huge help.
