.. _setup:

***********************
Making a Python Package
***********************

Specifying how to build your python package


Python Packages
===============

What is a "package" in Python ?


Packages, modules, imports, oh my!
----------------------------------

Before we get started on making your own package -- let's remind
ourselves about packages and modules, and importing....

**Modules**

A python "module" is a single namespace, with a collection of values:

  * functions
  * constants
  * class definitions
  * really any old value.

A module usually corresponds to a single file: ``something.py``


**Packages**

A "package" is essentially a module, except it can have other modules (and indeed other packages) inside it.

A package usually corresponds to a directory with a file in it called ``__init__.py`` and any number
of python files or other package directories::

  a_package
     __init__.py
     module_a.py
     a_sub_package
       __init__.py
       module_b.py

The ``__init__.py`` can be totally empty -- or it can have arbitrary python code in it.
The code will be run when the package is imported -- just like a module,

modules inside packages are *not* automatically imported. So, with the above structure::

  import a_package

will run the code in ``a_package/__init__.py``. Any names defined in the
``__init__.py`` will be available in::

  a_package.a_name

but::

 a_package.module_a

will not exist. To get submodules, you need to explicitly import them:

  import a_package.module_a


``https://docs.python.org/3/tutorial/modules.html#packages``


The module search path
----------------------

The interpreter keeps a list of all the places that it looks for modules or packages when you do an import:

.. code-block:: python

    import sys
    for p in sys.path:
        print p

You can manipulate that list to add or remove paths to let python find modules on a new place.

And every module has a ``__file__`` name that points to the path it lives in. This lets you add paths relative to where you are, etc.

*NOTE* it's usually better to use setuptools' "develop" mode instead -- see below.


Building Your Own Package
=========================

The very basics of what you need to know to make your own package.


Why Build a Package?
--------------------

There are a bunch of nifty tools that help you build, install and
distribute packages.

Using a well structured, standard layout for your package makes it
easy to use those tools.

Even if you never want to give anyone else your code, a well
structured package eases development.


What is a Package?
--------------------

**A collection of modules**

* ... and the documentation

* ... and the tests

* ... and any top-level scripts

* ... and any data files required

* ... and a way to build and install it...


Basic Package Structure:
------------------------

::

    package_name/
        bin/
        CHANGES.txt
        docs/
        LICENSE.txt
        MANIFEST.in
        README.txt
        setup.py
        package_name/
              __init__.py
              module1.py
              module2.py
              test/
                  __init__.py
                  test_module1.py
                  test_module2.py


``CHANGES.txt``: log of changes with each release

``LICENSE.txt``: text of the license you choose (do choose one!)

``MANIFEST.in``: description of what non-code files to include

``README.txt``: description of the package -- should be written in ReST (for PyPi):

(http://docutils.sourceforge.net/rst.html)

``setup.py``: the script for building/installing package.

``bin/``: This is where you put top-level scripts

  ( some folks use ``scripts`` )

``docs/``: the documentation

``package_name/``: The main package -- this is where the code goes.

``test/``: your unit tests. Options here:

Put it inside the package -- supports ::

     $ pip install package_name
     >> import package_name.test
     >> package_name.test.runall()

Or keep it at the top level.

Some notes on that:

` Where to put Tests <http://pythonchb.github.io/PythonTopics/where_to_put_tests.html>`_

The ``setup.py`` File
----------------------

Your ``setup.py`` file is what describes your package, and tells setuptools how to package, build and install it

It is python code, so you can add anything custom you need to it

But in the simple case, it is essentially declarative.


``http://docs.python.org/3/distutils/``

What Does ``setup.py`` Do?
--------------------------

* Version & package metadata

* List of packages to include

* List of other files to include

* List of dependencies

* List of extensions to be compiled (if you are not using `scikit-build <https://scikit-build.org>`_.


An example ``setup.py``:
------------------------

.. code-block:: python

  from setuptools import setup

  setup(
    name='PackageName',
    version='0.1.0',
    author='An Awesome Coder',
    author_email='aac@example.com',
    packages=['package_name', 'package_name.test'],
    scripts=['bin/script1','bin/script2'],
    url='http://pypi.python.org/pypi/PackageName/',
    license='LICENSE.txt',
    description='An awesome package that does something',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.1.1",
        "pytest",
    ],
 )


``setup.cfg``
--------------

**NOTE:** this is usually a pretty advanced option -- simple packages don't need this.

``setup.cfg`` provides a way to give the end user some ability to customize the install

It's an ``ini`` style file::

  [command]
  option=value
  ...

simple to read and write.

``command`` is one of the Distutils commands (e.g. build_py, install)

``option`` is one of the options that command supports.

Note that an option spelled ``--foo-bar`` on the command-line is spelled f``foo_bar`` in configuration files.


setuptools
-----------

``setuptools`` is an extension to ``distutils`` that provides a number of extensions::

    from setuptools import setup

superset of the ``distutils setup``

This buys you a bunch of additional functionality:

  * auto-finding packages
  * better script installation
  * resource (non-code files) management
  * **develop mode**
  * a LOT more

http://pythonhosted.org//setuptools/

Under Development
------------------

Develop mode is *really*, *really* nice::

  $ python setup.py develop

or::

  $ pip install -e ./

(the e stands for "editable" -- it is the same thing)

It puts a links into the python installation to your code, so that your package is installed, but any changes will immediately take effect.

This way all your test code, and client code, etc, can all import your package the usual way.

No ``sys.path`` hacking

Good idea to use it for anything more than a single file project.


+--------------------------------------+----------------------------------------+
| Install                              | Development Install                    |
+======================================+========================================+
| Copies package into site-packages    | Adds a ``.pth`` file to site-packages, |
|                                      | pointed at package source root         |
+--------------------------------------+----------------------------------------+
| Used when creating conda packages    | Used when developing software locally  |
+--------------------------------------+----------------------------------------+
| Normal priority in sys.path          | End of ``sys.path`` (only found if     |
|                                      | nothing else comes first)              |
+--------------------------------------+----------------------------------------+


https://grahamwideman.wikispaces.com/Python-+site-package+dirs+and+.pth+files


Getting Started With a New Package
----------------------------------

For anything but a single-file script (and maybe even then):

1. Create the basic package structure

2. Write a ``setup.py``

3. ``pip install -e .``

4. Put some tests in ``package/test``

5. ``pytest`` in the test dir, or ``pytest --pyargs package_name``

or use "Cookie Cutter":

https://cookiecutter.readthedocs.io/en/latest/


Exercise: A Small Example Package
---------------------------------

* Create a small package

  - package structure

  - ``setup.py``

  - ``python setup.py develop``

  - ``at least one working test``

Start with the silly code in:

:download:`capitalize.zip <examples/capitalize.zip>`


Let’s Make a Package
--------------------

::

    mypkg/
        __init__.py
        subpkg/
            __init__.py
            a.py



.. nextslide::

**Windows:**

.. code-block:: bash

	mkdir mypkg/subpkg

	echo. > mypkg/__init__.py

	echo . > mypkg/subpkg/__init__.py

	echo . > mypkg/subpkg/a.py


**Mac/Linux:**

.. code-block:: bash

	mkdir -p mypkg/subpkg

	touch mypkg/__init__.py

	touch mypkg/subpkg/__init__.py

	touch mypkg/subpkg/a.py



Let’s Write a ``setup.py``
--------------------------

.. code-block:: python

    #!/usr/bin/env python

    from setuptools import setup

    setup(name='mypkg',
          version='1.0',
          # list folders, not files
          packages=['mypkg', 'mypkg.subpkg'],
          )

(remember that a "package" is a folder with a ``__init__.py__`` file)


Try installing your package
---------------------------

.. code-block:: bash

	cd mypkg-src

	python setup.py install

	python -c “import mypkg.subpkg.a”

Go look in your ``site-packages`` folder


Making Packages the Easy Way
----------------------------

.. image:: images/cookiecutter.png


`github.com/audreyr/cookiecutter <https://github.com/audreyr/cookiecutter>`_

.. code-block:: bash

    conda install -c conda-forge cookiecutter

or

.. code-block:: bash

    pip install  cookiecutter

No time for that now :-(


Handling Requirements
=====================

Only the simplest of packages need only the Python standard library.


Requirements in ``setup.py``
----------------------------

.. code-block:: python

    #!/usr/bin/env python
    from distutils.core import setup

    setup(name='mypkg',
          version='1.0',
          # list folders, not files
          packages=['mypkg', 'mypkg.subpkg'],
          install_requires=['click'],
          )


Requirements in ``requirements.txt``
------------------------------------

**Common Mistake:**

* ``requirements.txt`` often from pip freeze

* Pinned way too tightly.  OK for env creation, bad for packaging.

|

* Donald Stufft (PyPA): `Abstract vs. Concrete dependencies <https://caremad.io/posts/2013/07/setup-vs-requirement>`_


Requirements in ``setup.cfg`` (ideal)
-------------------------------------

::

    [metadata]
    name = my_package
    version = attr:
    src.VERSION

    [options]
    packages = find:
    install_requires = click


Parse-able without execution, unlike ``setup.py``

`configuring setup using setup cfg files <http://setuptools.readthedocs.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files>`_

Exercise
---------

* Fill in the missing pieces in a setup.py for a sample package
* Do a development install for the package


Break time!
-----------

Up next: producing redistributable artifacts


