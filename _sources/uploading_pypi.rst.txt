.. _uploading:

******************************
Building and Uploading to PyPi
******************************

Learning Objectives
===================

In the following section we will ...
------------------------------------

* Review the packaging terminology
* Understand how to build, package and publish a python package


Packaging Terminology 101
=========================

Introduction
------------

This section reviews the key python packaging concepts and definitions.


PyPI
----

PyPI is the default `Package Index <https://packaging.python.org/glossary/#term-package-index>`_ for the Python community.
It is open to all Python developers to consume and distribute their **distributions**.

.. nextslide::

There are two instances of the Package Index:

* PyPI: Python Package Index hosted at https://pypi.org/

* TestPyPI: a separate instance of the Python Package Index (PyPI) that allows you to try out the
  distribution tools and process without worrying about affecting the real index.
  TestPyPI is hosted at https://test.pypi.org

Reference: https://packaging.python.org/glossary/#term-python-package-index-pypi


pip
---

The `PyPA <https://www.pypa.io/en/latest/>`_ recommended tool for installing Python packages.

.. nextslide::

A multi-faceted tool:

* It is an *integration frontend* that takes a set of package requirements (e.g. a requirements.txt file)
  and attempts to update a working environment to satisfy those requirements. This may require locating,
  building, and installing a combination of **distributions**.

* It is a **build frontend** that can takes arbitrary source trees or source distributions and builds wheels
  from them.

Reference: http://pip.readthedocs.io/


PyPA
----

The Python Packaging Authority (PyPA) is a working group that maintains many of the relevant
projects in Python packaging.

.. nextslide::

The associated website https://www.pypa.io references the PyPA Goals, Specifications and Roadmap
as well as `Python Packaging User Guide <https://packaging.python.org/>`_, a collection of tutorials
and references to help you distribute and install Python packages with modern tools.

Reference: https://www.pypa.io


Source distribution
-------------------

* Synonyms: sdist, Source release

* provides metadata + source files

* needed for installing

  * by a tool like pip
  * or for generating a Built Distribution

Reference: https://packaging.python.org/glossary/#term-source-distribution-or-sdist


Built Distribution
------------------

* Synonyms: bdist

* provides metadata + pre-built files

* only need to be moved (usually by pip) to the correct locations on the target system

Reference: https://packaging.python.org/glossary/#term-built-distribution


Python Distribution: pure vs non-pure
-------------------------------------

* **pure**:

  * Not specific to a CPU architecture
  * No `ABI (Application Binary Interface) <https://en.wikipedia.org/wiki/Application_binary_interface>`_

.. nextslide::

* **non-pure**

  * `ABI <https://en.wikipedia.org/wiki/Application_binary_interface>`_
  * Platform specific

Reference: https://packaging.python.org/glossary/#term-module


Binary Distribution
-------------------

* is a **Built Distribution**
* is **non-pure**
* uses platform-specific compiled extensions

Reference: https://packaging.python.org/glossary/#term-binary-distribution


Wheel
-----

* a **Built Distribution**

* a ZIP-format archive with .whl extension

  * ``{distribution}-{version}(-{build tag})?-{python tag}-{abi tag}-{platform tag}.whl``

* described  by `PEP 427 <https://www.python.org/dev/peps/pep-0427/>`_

Reference: https://packaging.python.org/glossary/#term-wheel


Wheels vs. Conda packages
-------------------------

+-------------------------------------+-------------------------------------+
|  Wheels                             |    Conda packages                   |
+=====================================+=====================================+
| Employed by pip, blessed by PyPA    |  Foundation of Anaconda ecosystem   |
+-------------------------------------+-------------------------------------+
| Used by any python installation     |  Used by conda python installations |
+-------------------------------------+-------------------------------------+
| Mostly specific to Python ecosystem |  General purpose (any ecosystem)    |
+-------------------------------------+-------------------------------------+
| Good mechanism for specifying range |  Primitive support for multiple     |
| of python compatibility             |  python versions (noarch)           |
+-------------------------------------+-------------------------------------+
| Depends on static linking or other  | Can bundle core system-level shared |
| system package managers to provide  | libraries as packages, and resolve  |
| core libraries                      | dependencies                        |
+-------------------------------------+-------------------------------------+


To learn more about Conda, see :ref:`conda_build` section.


Virtual Environment
-------------------

An isolated Python environment that allows packages to be installed for use by a
particular application, rather than being installed system wide.

Learn more reading `Creating Virtual Environments <https://packaging.python.org/tutorials/installing-packages/#creating-and-using-virtual-environments>`_


Build system
------------

Synonym: Build backend

* `setuptools <https://setuptools.readthedocs.io>`_ associated with the `wheel <https://wheel.readthedocs.io>`_ package
  form the default build system. They support the creation of source and **built distributions** based on a ``setup.py`` and
  optionally a ``setup.cfg`` file.

* `flit <https://flit.readthedocs.io/en/latest/>`_ is an alternative backend allowing to also create (and also publish)
  **built distributions**.


Python Package Lifecycle
------------------------

.. image:: images/python-package-life-cycle.png


Tutorial
========

Introduction
------------

This section discusses how to build python packages (or distributions) and publish
them in a central repository to streamline their installation. Finally, we conclude
with exercises where we publish a package with the `Test Python Package Index <http://test.pypi.org/>`_.


Creating an environment
-----------------------

Before developing or building your distribution, we highly recommend to create a
dedicated environment. This is supported by both ``conda`` and ``pip``.


Building a source distribution
------------------------------

By leveraging the ``setup.py`` script, setuptools can build a source
distribution (a tar archive of all the files needed to build and install the package):

.. code-block:: bash

    $ python setup.py sdist

    $ ls -1 dist
    SomePackage-1.0.tar.gz


Building a wheel
----------------

.. code-block:: bash

    $ pip wheel . -w dist

    $ ls -1 dist
    SomePackage-1.0-py2.py3-none-any.whl


.. nextslide::

This is equivalent to:

.. code-block:: bash

    $ python setup.py bdist_wheel


Installing a wheel
------------------

* Install a package from PyPI:

.. code-block:: bash

    $ pip install SomePackage
    [...]
    Successfully installed SomePackage

.. nextslide::

* Install a package file:

.. code-block:: bash

    $ pip install SomePackage-1.0-py2.py3-none-any.whl
    [...]
    Successfully installed SomePackage

For more details, see `QuickStart guide from pip documentation <https://pip.pypa.io/en/stable/quickstart/>`_.


Installing a source distribution
--------------------------------

.. code-block:: bash

    $ pip install SomePackage-1.0.tar.gz
        [...]
    Successfully installed SomePackage

It transparently builds the associated wheel and install it.


Publishing to PyPI
------------------

`twine <https://twine.readthedocs.io>`_ utility is used for publishing
Python packages on PyPI.

It is available as both a conda and a pypi package.

Learn more reading `Using TestPiPY <https://packaging.python.org/guides/using-testpypi/>`_.


Exercises
=========

Exercise 1: Prepare environment
-------------------------------

* In the context of this tutorial, because participants already `installed miniconda <https://github.com/python-packaging-tutorial/python-packaging-tutorial#installation-instructions>`_,
  we will create a conda environment and install packages using ``conda install SomePackage``.

.. code-block:: bash

    # create and activate a dedicated environment named "hello-pypi"
    conda create -n hello-pypi -y -c conda-forge
    conda activate hello-pypi

    # install pip, wheel and twine
    conda install -y twine wheel pip

.. nextslide::

* Create an account on TestPyPI (https://test.pypi.org/account/register/)


Exercise 2: Build source distribution and wheel
-----------------------------------------------

* `Download <https://github.com/python-packaging-tutorial/hello-pypi/archive/master.zip>`_ (or
  `checkout <https://github.com/python-packaging-tutorial/hello-pypi>`_ using git) the sources
  of our ``hello-pypi`` sample project:

.. code-block:: bash

    conda install -y wget
    wget https://github.com/python-packaging-tutorial/hello-pypi/archive/master.zip


.. nextslide::

* Extract sources

.. code-block:: bash

    conda install -y unzip
    unzip master.zip
    cd hello-pypi-master

.. nextslide::

* Modify package name so that it is unique

.. nextslide::

* Then, build the source distribution:


.. code-block:: bash

    $ python setup.py sdist


* And finally, build the wheel:

.. code-block:: bash

    $ pip wheel . -w dist

* Make sure artifacts have been generated in the ``dist`` subdirectory.


Exercise 3: Publish artifacts
-----------------------------

.. code-block:: bash

    $ twine upload --repository-url https://test.pypi.org/legacy/ dist/*


Bonus Exercise 4: Publish artifacts automating authentication
-------------------------------------------------------------

* Delete ``hello-pypi-master`` directory and extract archive again.

* Update name of package and rebuild source distribution and wheel.

.. nextslide::

* Create file ``.pypirc`` in your home directory with the following content:

::

    [distutils]
    index-servers=
        pypi
        testpypi

    [testpypi]
    repository: https://test.pypi.org/legacy/
    username: your testpypi username
    password: your testpypi password

    [pypi]
    username: your testpypi username
    password: your testpypi password

.. nextslide::

* Publish package on TestPyPI:

.. code-block:: bash

    $ twine upload --repository testpypi dist/*


Omitting the ``-repository testpypi`` argument allows to upload
to the regular PyPI server.


Resources
=========

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

.. nextslide::

Here is an opinionated update -- a little more fancy, but some good ideas:

https://blog.ionelmc.ro/2014/05/25/python-packaging/

.. nextslide::

Rather than doing it by hand, you can use the nifty "cookie cutter" project:

https://cookiecutter.readthedocs.io/en/latest/

.. nextslide::

And there are a few templates that can be used with that.

The core template written by the author:

https://github.com/audreyr/cookiecutter-pypackage

And one written by the author of the opinionated blog post above:

https://github.com/ionelmc/cookiecutter-pylibrary

Either are great starting points.

