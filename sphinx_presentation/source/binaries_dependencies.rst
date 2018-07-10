*************************
Binaries and Dependencies
*************************

Learning Objectives
===================

In this section we will ...
---------------------------

* Understand why we build Python packages with native binaries: 1)
  **performance** and 2) **library integration**
* Understand different components of the binary build process and their role:
  *headers, libraries, compilers, linkers, makefiles, system introspection
  tools, package managers*
* Understand basic requirements for binary compatibility: a) **C-runtime library
  compatibility** and b) **shared library compatibilty**
* Understand **scikit-build**'s role in coordinating components of the binary
  build process and **conda**'s role in resolving dependencies and creating compatible platform binaries


Tutorial
========

Introduction
------------

This section discusses the creation of Python packages that contain **native
binaries**.

First, we explain why building Python packages with native binaries is often
*desirable* or *necessary* for *scientific applications*.

Next, an overview of the requirements to build native binaries is provided.
Within this the context, we explain how *scikit-build* and *conda-build* make
life easier when we want to satisfy these requirements.

Finally, run an exercise where we build a native Python wth native binaries
package and analyze the different stages of the build process.

Motivation
----------

Scientific computing applications demand **higher performance** than other
domains because of the:

1. **Size** of the **datasets** to be analyzed
2. **Complexity** of the **algorithms** evaluated

.. nextslide::

In order to achieve **high performance**, programs can:

1. **Minimized the number of operations** on the CPU required to acheive a certain
   task
2. **Execute in parallel** to leverage multi-core, many-core, and GPGPU system
   architectures
3. Carefully and precisely **manage memory** allocation and use

.. nextslide::

Greater performance is achieved with native binaries over CPython because:

1. Tasks are **compiled down to minimal processor operations**,
   as opposed to high level programming language instructions that must be
   **interpreted**
2. Parallel computing is not impared by CPython's `Global Interpreter Lock
   (GIL) <https://wiki.python.org/moin/GlobalInterpreterLock>`_
3. **Memory** can be managed **explicitly** and **deterministically**

.. nextslide::

Many existing scientific codes are written in **programming languages other than Python**.
It is necessary to **re-use** these libraries since:

- **Resources** are not available to re-implement work that is sometimes the
  result of multiple decades of effort from multiple researchers.
- The **scientific endeavor** is built on the practice of **reproducing** and **building on the top** of the efforts of our predecessors.

.. nextslide::

The *lingua franca* of computing is the **C programming language** because
most operating systems themselves are written in C.

As a consequence,

* **Native binaries** reflect characteristics and compatibility with of the C language
* The reference implementation of Python, *CPython*, is implemented in C
* CPython supports **binary extension modules written in C**
* Most other pre-compiled programming languages have a **compatibility layer
  with C**
* CPython is an excellent language to **integrate scientific codes**!

.. nextslide::

Common programming languages compiled into native libraries for scientific
computing include:

- Fortran
- C
- C++
- Cython
- Rust

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
