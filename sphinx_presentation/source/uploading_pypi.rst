******************************
Building and Uploading to PyPi
******************************

Learning Objectives
===================

In this section we will ...
---------------------------

* Review the packaging terminology
* Understand how to build and package a python package


Tutorial
========

Introduction
------------

This section discusses how to build python packages (or distributions) and publish
them in a central repository to streamline their installation. Finally, we conclude
with an exercise where we publish a package with the `Test Python Package Index <http://test.pypi.org/>`_.


Packaging Terminology 101
=========================

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
  * No ABI


* **non-pure**

  * ABI
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


Tools and package types
=======================


**flit:** great for simple packages

**twine:** the secure way to upload to PyPI

* Building a source distribution

* Building a wheel

* Multibuild - https://github.com/matthew-brett/multibuild

* Manylinux docker image - https://github.com/pypa/manylinux

* Delocate - https://github.com/matthew-brett/delocate

* Auditwheel - https://github.com/pypa/auditwheel


Redistributable artifacts
=========================

* sdists

* wheels

* conda packages

* eggs (deprecated)


When/how to use an sdist
------------------------

* Pure python (no compilation requirements)

* Or, distributing source code that must be compiled prior to usage

.. code-block:: bash

    python setup.py sdist





