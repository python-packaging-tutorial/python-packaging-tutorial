******************************
Building and Uploading to PyPi
******************************

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




