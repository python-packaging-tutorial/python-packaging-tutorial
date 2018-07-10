********
Overview
********

Outline:
========


0:00-00:20 Overview of packaging
--------------------------------

 * Source/binary
 * Wheel vs conda packages
 * PyPI/anaconda.org

0:20-0:45 setup.py
------------------

* Essential specifications
* Optional specifications
* Specifying requirements
* In setup.py vs requirements file
* When and how to "pin" requirements

Exercise:
.........

Fill in the missing pieces in a setup.py for a sample package
Build a source distribution for the package

0:45-1:00 Building and uploading to PyPI:
-----------------------------------------

Tools and package types


**flit:** great for simple packages

**twine:** the secure way to upload to PyPI

* Building a source distribution

* Building a wheel

* Multibuild - https://github.com/matthew-brett/multibuild

* Manylinux docker image - https://github.com/pypa/manylinux

* Delocate - https://github.com/matthew-brett/delocate

* Auditwheel - https://github.com/pypa/auditwheel

1:00-1:10 Break
---------------

1:10-1:30 Worked example/exercise:
----------------------------------

Building a package and uploading to pypi

Continuing from the the previous exercise, build a wheel for the package

Register the package on the pypi testing server

Upload the built distributions using twine

Delete one of the uploaded files on pypi and try re-uploading (will fail)

Introduce the idea of .post releases (it will happen to everyone who uploads)

1:30-1:45 Binaries and dependencies:
------------------------------------

how scikit-build and conda-build can make life easier

1:45-2:00 Scikit-build overview:

Why + Motivations

From [distutils.core.Extension] to [scikit-build + CMake] in few lines
Support for developer mode (bonus)

2:00-2:45 Exercise:
-------------------

Add CMake project that generates python extension.  Tie
it into previous python project.

Cookie cutter template integrating conda, pypi, etc. will be provided.

2:45-3:00 Break
---------------

3:00-3:15 Conda-build overview
------------------------------

3:15-3:30 Exercise:
-------------------

Write a conda recipe for the sample package from previous exercises (pure python)

noarch packages

Upload to anaconda cloud

3:15-3:45 Exercise:
-------------------

Recipe for package with compiled extensions

Add compiled extension (source will be provided to students) to sample package

Modify recipe, if needed

Rebuild the package

Version pinning (python, numpy)

Split packages - multi-ecosystem ones

Compiler packages + pin_downstream

Interoperation with scikit-build

3:45-4:00 Automated building with cloud-based CI services:
----------------------------------------------------------

conda-forge (optional; as time allows)

http://scikit-ci.readthedocs.io

http://scikit-ci-addons.readthedocs.io

CI service overview & Conda-forge -- what are the pieces and how do they fit together?

Recipe format

staged-recipes

feedstocks

Re-rendering and conda-smithy

Updating package when new version released

Future direction/community needs

Invitation to sprints

Contributing to Conda-forge

Intro to conda-forge: staged-recipes, maintainer role, contributing to an existing package

conda-smithy lint/rerender

Example to go from the conda-skeleton to a PR on staged-recipes

Comment on some special cases: cython extensions,  non-python pkgs, the use of the CIs, etc.

Exercise: put a package on staged-recipes


Tutorial code base layout:
--------------------------

Name of the organization: python-packaging-tutorial

All projects should be associated with a cookiecutter template

One organization with multiple repos (or multiple branches ?)

0_readme
1_helloworld_pure

Install python

Work with virtual env

Include pytest, documentation building, …

2_helloworld_c

Show how C extensions are included in setup.py, and how they are made available to python

3_helloworld_with_ci

Introduce Appveyor, CircleCi, Travis

Difference between CI for testing and CI for creating packages (CD)

4_helloworld_skbuild

Introduce C extensions with cmake

Show how scikitbuild can help tie python and cmake together nicely

5_helloworld_skbuild_ci

Show how scikitbuild-ci can be used to simplify and unify CI scripts

6_helloworld_skbuild_conda

Show how conda-build can be used to produce conda packages and wheels, using the build files we’ve already used from previous exercises.

7_Uploading_to_PyPI_&_anaconda.org
