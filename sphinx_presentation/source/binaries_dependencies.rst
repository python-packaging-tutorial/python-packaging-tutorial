*************************
Binaries and Dependencies
*************************

Learning Objectives
===================

In this section we will ...
---------------------------

* Understand why we build Python packages with native binaries: 1)
  performance and 2) library integration
* Understand different components of the binary build process and their role:
  *headers, libraries, compilers, linkers, makefiles, system introspection
  tools, package managers*
* Understand basic requirements for binary compatibility: a) C-runtime library
  compatibility and b) shared library compatibilty
* Understand **scikit-build**'s role in coordinating components of the binary
  build process and **conda**'s role in resolving dependencies and creating compatible platform binaries


Tutorial
========

Introduction
------------

This section discusses the creation of Python packages that contain native
binaries. First, we explain why building Python packages with native binaries
is often necessary or desirable for scientific applications. Next, an overview
of the requirements to build native binaries is provided. Within this the
context, we explain how *scikit-build* and *conda-build* make life easier when
we want to satisfy these requirements. Finally, we conclude with an exercise
where we build a native Python wth native binaries package and analyze the
different stages of the build process.

Motivation
----------

Build Requirements
------------------

Scientific Python Build Tools
-----------------------------

Exercises
=========

Exercise 1: Build a Python Package with a C++ Extension Module
---------------------------------------------------------------

Exercise 2: Build a Python Package with a Cython Extension Module
-----------------------------------------------------------------
