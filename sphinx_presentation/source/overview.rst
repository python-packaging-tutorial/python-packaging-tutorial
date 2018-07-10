.. _overview:

********
Overview
********


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

