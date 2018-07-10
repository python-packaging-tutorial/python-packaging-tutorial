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

**Modules**

A python "module" is a single namespace, with a collection of values:

  * functions
  * constants
  * class definitions
  * really any old value.

A module usually corresponds to a single file: ``something.py``


Packages
--------

A "package" is essentially a module, except it can have other modules (and indeed other packages) inside it.

A package usually corresponds to a directory with a file in it called ``__init__.py`` and any number of python files or other package directories::

  a_package
     __init__.py
     module_a.py
     a_sub_package
       __init__.py
       module_b.py

.. nextslide::

The ``__init__.py`` can be totally empty -- or it can have arbitrary python code in it.

The code will be run when the package is imported -- just like a module,

modules inside packages are *not* automatically imported. So, with the above structure::

  import a_package

will run the code in ``a_package/__init__.py``.

.. nextslide::

Any names defined in the
``__init__.py`` will be available in::

  a_package.a_name

but::

 a_package.module_a

will not exist. To get submodules, you need to explicitly import them:

``import a_package.module_a``


https://docs.python.org/3/tutorial/modules.html#packages


The module search path
----------------------

The interpreter keeps a list of all the places that it looks for modules or packages when you do an import:

.. code-block:: python

    import sys
    for p in sys.path:
        print p

You can manipulate that list to add or remove paths to let python find modules on a new place.

And every module has a ``__file__`` name that points to the path it lives in. This lets you add paths relative to where you are, etc.

*NOTE:*  it's usually better to use setuptools' "develop" mode instead -- see below.


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
structured package simplifies development.


What is a Package?
--------------------

**A collection of modules**

... and the documentation

... and the tests

... and any top-level scripts

... and any data files required

... and a way to build and install it...


Python packaging tools:
------------------------

``distutils``: included with python

.. code-block:: python

    from distutils.core import setup

Getting clunky, hard to extend, maybe destined for deprecation ...

``setuptools``: for extra features, technically third party

- present in most modern Python installations

"The Python Packaging Authority" -- PyPA

https://www.pypa.io/en/latest/

setuptools
-----------

``setuptools`` is an extension to ``distutils`` that provides a number of extensions:

.. code-block:: python

    from setuptools import setup

superset of the ``distutils setup``

This buys you a bunch of additional functionality:

  * auto-finding packages
  * better script installation
  * resource (non-code files) management
  * **develop mode**
  * a LOT more

http://pythonhosted.org//setuptools/


Where do I go to figure this out?
---------------------------------

This is a really good guide:

Python Packaging User Guide:

https://packaging.python.org/

and a more detailed tutorial:

http://python-packaging.readthedocs.io/en/latest/

**Follow one of them**

.. nextslide::

There is a sample project here:

https://github.com/pypa/sampleproject

(this has all the complexity you might need...)

You can use this as a template for your own packages.

Here is an opinionated update -- a little more fancy, but some good ideas:

https://blog.ionelmc.ro/2014/05/25/python-packaging/


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

.. nextslide::

``CHANGES.txt``: log of changes with each release

``LICENSE.txt``: text of the license you choose (do choose one!)

``MANIFEST.in``: description of what non-code files to include

``README.txt``: description of the package -- should be written in ReST
or Markdown (for PyPi):

``setup.py``: the script for building/installing package.

.. nextslide::

``bin/``: This is where you put top-level scripts

( some folks use ``scripts`` )

``docs/``: the documentation

``package_name/``: The main package -- this is where the code goes.

.. nextslide::

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

http://docs.python.org/3/distutils/


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

Provides a way to give the end user some ability to customize the install

It's an ``ini`` style file::

  [command]
  option=value
  ...

simple to read and write.

``command`` is one of the Distutils commands (e.g. build_py, install)

``option`` is one of the options that command supports.

Note that an option spelled ``--foo-bar`` on the command-line is spelled
``foo_bar`` in configuration files.


Running ``setup.py``
--------------------

With a ``setup.py`` script defined, setuptools can do a lot:

Builds a source distribution (a tar archive of all the files needed to build and install the package)::

    python setup.py sdist

Builds wheels::

    ./setup.py bdist_wheel

(you need the wheel package for this to work:)

``pip install wheel``

.. nextslide::

Build from source::

    python setup.py build

And install::

    python setup.py install

Develop mode
------------

Install in "develop" or "editable" mode::

    python setup.py develop

or::

   pip install .


Under Development
------------------

Develop mode is *really*, *really* nice::

  $ python setup.py develop

or::

  $ pip install -e ./

(the e stands for "editable" -- it is the same thing)

.. nextslide::

It puts a link (actually ``*.pth`` files) into the python installation to your code, so that your package is installed, but any changes will immediately take effect.

This way all your test code, and client code, etc, can all import your package the usual way.

No ``sys.path`` hacking

Good idea to use it for anything more than a single file project.

.. nextslide::

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


Aside on pip and dependencies
-----------------------------

* ``pip`` does not currently have a solver: http://github.com/pypa/pip/issues/988

* pip may replace packages in your environment with incompatible versions.  Things will break when that happens.

* use caution (and ideally, disposable environments) when using pip


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

Start with the silly code in the tutorial repo in:

``python-packaging-tutorial/setup_example/``

or you can download a zip file here:

:download:`capitalize.zip <examples/capitalize.zip>`


capitalize
----------

capitalize is a useless little utility that will capitalize the words in a text file.

But it has the core structure of a python package:

* a library of "logic code"
* a command line script
* a data file
* tests

.. nextslide::

So let's see what's in there::

	$ ls
	capital_mod.py           test_capital_mod.py
	cap_data.txt             main.py
	cap_script.py            sample_text_file.txt


What are these files?
---------------------

``capital_mod.py``
    The core logic code

``main.py``
    The command line app

``test_capital_mod.py``
    Test code for the logic

``cap_script.py``
    top-level script

``cap_data.txt``
    data file

``sample_text_file.txt``
    sample example file to test with.

.. nextslide::

Try it out:

::

	$ cd capitalize/

	$ python3 cap_script.py sample_text_file.txt

	Capitalizing: sample_text_file.txt and storing it in
	sample_text_file_cap.txt

	I'm done

So it works, as long as you are in the directory with all the code.


Setting up a package structure
------------------------------

Create a basic package structure::

    package_name/
        bin/
        README.txt
        setup.py
        package_name/
              __init__.py
              module1.py
              test/
                  __init__.py
                  test_module1.py

Let's create all that for capitalize:


.. nextslide::

Make the package:

.. code-block:: bash

	$ mkdir capitalize

	$ cd capitalize/

	$ touch __init__.py

Move the code into it:

.. code-block:: bash

 	$ mv ../capital_mod.py ./
    $ mv ../main.py ./
    $ mv ../cap_data.txt ./

.. nextslide::

Create a dir for the tests:

.. code-block:: bash

    $ mkdir test

Move the tests into that:

.. code-block:: bash

    $ mv ../test_capital_mod.py test/


.. nextslide::

Create a dir for the script:

.. code-block:: bash

    $ mkdir bin

Move the script into that:

.. code-block:: bash

    $ mv ../cap_script.py bin

Now we have a package!

.. nextslide::

Let's try it::

	$ python bin/cap_script.py
	Traceback (most recent call last):
	  File "bin/cap_script.py", line 8, in <module>
	    import capital_mod
	ImportError: No module named capital_mod

OK, that didn't work. Why not?

Well, we've moved everytihng around:

The modules don't know how to find each other.

Let’s Write a ``setup.py``
--------------------------

.. code-block:: python

	#!/usr/bin/env python

	from setuptools import setup

	setup(name='capitalize',
	      version='1.0',
	      # list folders, not files
	      packages=['capitalize',
	                'capitalize.test'],
	      scripts=['capitalize/bin/cap_script.py'],
	      )


(remember that a "package" is a folder with a ``__init__.py__`` file)

That's about the minimum you can do.

.. nextslide::

Save it as ``setup.py`` *outside* the capitalize package dir.

Install it in "editable" mode:

.. code-block:: bash

	$ pip install -e ./
	Obtaining file:///Users/chris.barker/HAZMAT/Conferences/SciPy-2018/PackagingTutorial/TutorialDay/capitalize
	Installing collected packages: capitalize
	  Running setup.py develop for capitalize
	Successfully installed capitalize

.. nextslide::

Try it out::

	$ cap_script.py
	Traceback (most recent call last):
	  File "/Users/chris.barker/miniconda2/envs/py3/bin/cap_script.py", line 6, in <module>
	    exec(compile(open(__file__).read(), __file__, 'exec'))
	  File "/Users/chris.barker/HAZMAT/Conferences/SciPy-2018/PackagingTutorial/TutorialDay/capitalize/capitalize/bin/cap_script.py", line 8, in <module>
	    import capital_mod
	ModuleNotFoundError: No module named 'capital_mod'

Still didn't work -- why not?

We need to update some imports.

.. nextslide::

in cap_script.py::

  import main

should be::

  from capitalize import main

and similarly in main.py::

    from capitalize import capital_mod

.. nextslide::

And try it::

	$ cap_script.py sample_text_file.txt

	Capitalizing: sample_text_file.txt and storing it in
	sample_text_file_cap.txt

	I'm done


Running the tests:
------------------

Option 1: cd to the test dir::

	$ cd capitalize/test/

	$ pytest
	$ ===================================
	  test session starts
	  ====================================
	...

	Traceback:
	test_capital_mod.py:14: in <module>
	    import capital_mod
	E   ModuleNotFoundError: No module named 'capital_mod'

Whoops -- we need to fix that import, too::

    from capitalize import capital_mod

.. nextslide::


And now we're good::

	$ pytest
	======test session starts =====

	collected 3 items

	test_capital_mod.py ...

	============== 3 passed in 0.06 seconds ============

.. nextslide::

You can also run the tests from anywhere on the command line::

    $ pytest --pyargs capitalize

	collected 3 items

	capitalize/capitalize/test/test_capital_mod.py ...                                   [100%]

	=============== 3 passed in 0.03 seconds ==========



Making Packages the Easy Way
----------------------------

To auto-build a full package structure:

|

.. image:: images/cookiecutter.png


.. nextslide::

Rather than doing it by hand, you can use the nifty "cookie cutter" project:

https://cookiecutter.readthedocs.io/en/latest/

And there are a few templates that can be used with that.

The core template written by the author:

https://github.com/audreyr/cookiecutter-pypackage

And one written by the author of the opinionated blog post above:

https://github.com/ionelmc/cookiecutter-pylibrary

Either are great starting points.

.. nextslide::

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

* requirements.txt often from pip freeze

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


Break time!
-----------

Up next: producing redistributable artifacts


