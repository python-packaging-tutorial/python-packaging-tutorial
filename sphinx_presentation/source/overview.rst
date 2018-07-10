********
Overview
********

Outline:
========

How are we spending our afternoon?


0:00-00:20 Overview of packaging
--------------------------------

 * Source/binary
 * Wheel vs conda packages
 * PyPI/anaconda.org

0:20-0:45 python packages: the setup.py file
--------------------------------------------

* Essential specifications
* Optional specifications
* Specifying requirements
* In setup.py vs requirements file
* When and how to "pin" requirements


0:45-1:00 Building and uploading to PyPI:
-----------------------------------------

Tools and package types

* **flit:** great for simple packages - https://github.com/takluyver/flit
* **twine:** the secure way to upload to PyPI - https://github.com/pypa/twine
* Multibuild - https://github.com/matthew-brett/multibuild
* Manylinux docker image - https://github.com/pypa/manylinux
* Delocate - https://github.com/matthew-brett/delocate
* Auditwheel - https://github.com/pypa/auditwheel

* Building a source distribution
* Building a wheel


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


1:30-1:45 Binaries and dependencies:
------------------------------------

how scikit-build and conda-build can make life easier

1:45-2:00 Scikit-build overview:

Why + Motivations

From [distutils.core.Extension] to [scikit-build + CMake] in few lines
Support for developer mode (bonus)


2:00-2:45 Exercise:
-------------------

* Add CMake project that generates python extension.  Tie it into previous python project.

Cookie cutter template integrating conda, pypi, etc. will be provided.

2:45-3:00 Break
---------------


3:00-3:15 Conda-build overview
------------------------------


3:15-3:30 Exercise:
-------------------

* Write a conda recipe for the sample package from previous exercises (pure python)
* noarch packages
* Upload to anaconda cloud


3:15-3:45 Exercise:
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

conda-forge (optional; as time allows)

http://scikit-ci.readthedocs.io

http://scikit-ci-addons.readthedocs.io

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


Packages
========


What is a “package”?
--------------------

* In a broad sense, anything you install using your package manager

* Some kinds of packages have implied behavior and requirements

* Unfortunate overloading: python “package”: a folder that python imports


Package Managers and Repos
--------------------------

* Many package managers: some OS specific -- some language specific:

* NPM, apt, yum, dnf, chocolatey, pip, conda, homebrew, etc.

* PyPI, anaconda.org, CRAN, CPAN


But they all contain:

* Some form of dependency management

* Artifact and/or source repository

The idea is that you install something, and have it "just work".


Package types:
--------------

Focusing now on the Python world:

A package can be essentially in two forms:

* source
* binary

As Python is a dynamic language, this distinction can get a bit blurred:

There is little difference between a source and binary package *for a pure python package*

But if there is any compiled code in there, building from source can be a challenge:

 - binary packages are very helpful

Source Packages
---------------

A source package is all the source required to build the package.

Package managers (like pip) can automatically build your package from source.

**But:**

 - Your system needs to be set up to build (compiler)
 - You need to have the dependencies, etc available
 - Sometimes it take time

Binary Packages
---------------

A collection of code all ready to run.

 - Everything is already compiled and ready to go

**But:**

 - It's likely to be platform dependent
 - Maybe require dependencies to be installed


Python Packaging
----------------

There are essentially two package managers widely used for Python.

**pip:**

  - Pulls packages from PyPI

  - Handles both source and binary packages (wheels)

  - Python only

**conda:**

  - Pulls packages from anaconda.org

  - Binary only

  - Supports other languages / libraries: C, Fortran, R, Perl, Java (anything, really)

  - Manages Python itself


OS package managers:
--------------------

  - System package managers:

	  - Linux

	    - rpm

	    - apt-get, homebrew

	  - OS-X

	    - homebrew

	    - macports

	  - Windows

	  	- chocolatey

Also sometimes handle python packages -- but we won't talk about those here.

