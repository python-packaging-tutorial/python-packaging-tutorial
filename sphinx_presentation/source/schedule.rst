*****************
Tutorial Schedule
*****************

Outline
=======

How are we spending our afternoon?


0:00-00:20 Overview of packaging
--------------------------------

.. ifnotslides::

  :ref:`overview`

* What is a package, anyway?
* Source/binary
* Wheel vs conda packages
* PyPI/anaconda.org


0:20-0:45 python packages: the setup.py file
--------------------------------------------

.. ifnotslides::

  :ref:`setup`


* Python packages -- what are they?
* The setup.py file
* Specifying requirements
* When and how to "pin" requirements
* Let's make a package!


0:45-1:00 Building and uploading to PyPI:
-----------------------------------------

.. ifnotslides::

  :ref:`uploading`

* Packaging Terminology 101
* Building and publishing a python distribution


1:00-1:10 Break
---------------

1:10-1:30 Worked example/exercise:
----------------------------------

* Building a package and uploading to pypi
* Continuing from the the previous exercise, build a wheel for the package
* Register the package on the pypi testing server
* Upload the built distributions using twine
* Delete one of the uploaded files on pypi and try re-uploading (will fail)
* Introduce the idea of .post releases (it will happen to everyone who uploads)


1:30-2:00 Binaries and dependencies:
------------------------------------

.. ifnotslides::

  :ref:`binaries`

* Why we build Python packages with native binaries: 1)
  **performance** and 2) **library integration**
* Different components of the binary build process and their role:
  *headers, libraries, compilers, linkers, build systems, system introspection
  tools, package managers*
* Basic requirements for binary compatibility: a) **C-runtime library
  compatibility** and b) **shared library compatibilty**
* Joyous tools: **scikit-build**'s role in coordinating components of the binary
  build process and **conda**'s role in resolving dependencies and creating compatible platform binaries

2:00-2:45 Exercise:
-------------------

* Build a Python package with a C++-based C-extension.
* Build a Python package with a Cython-based C-extension.


2:45-3:00 Break
---------------


3:00-3:15 Conda-build overview
------------------------------

.. ifnotslides::

  :ref:`conda-build`


3:15-3:30 Exercise:
-------------------

* Write a conda recipe for the sample package from previous exercises (pure python)
* noarch packages
* Upload to anaconda cloud


3:30-3:45 Exercise:
-------------------

* Recipe for package with compiled extensions
* Add compiled extension (source will be provided to students) to sample package
* Modify recipe, if needed
* Rebuild the package
* Version pinning (python, numpy)
* Split packages - multi-ecosystem ones
* Compiler packages + pin_downstream
* Interoperation with scikit-build


3:45-4:00 Automated building with cloud-based CI services:
----------------------------------------------------------

.. ifnotslides::

  :ref:`conda-forge`


**conda-forge** (optional; as time allows)

CI service overview & Conda-forge -- what are the pieces and how do they fit together?

* Recipe format
* staged-recipes
* feedstocks
* Re-rendering and conda-smithy
* Updating package when new version released
* Future direction/community needs
* Invitation to sprints
* Contributing to Conda-forge
* Intro to conda-forge: staged-recipes, maintainer role, contributing to an existing package
* conda-smithy lint/rerender
* Example to go from the conda-skeleton to a PR on staged-recipes
* Comment on some special cases: cython extensions,  non-python pkgs, the use of the CIs, etc.
* Exercise: put a package on staged-recipes

