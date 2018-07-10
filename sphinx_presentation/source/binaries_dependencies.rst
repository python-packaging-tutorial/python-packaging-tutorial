.. _binaries:

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
  *headers, libraries, compilers, linkers, build systems, system introspection
  tools, package managers*
* Understand basic requirements for binary compatibility: a) **C-runtime library
  compatibility** and b) **shared library compatibilty**
* Understand **scikit-build**'s role in coordinating components of the binary
  build process and **conda**'s role in resolving dependencies and creating compatible platform binaries


Tutorial
========

.. ifnotslides::

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

Build Components and Requirements
---------------------------------

Build component categories:

build tools
  Tools use in the build process, such as the compiler, linker, build systems,
  system introspection tool, and package manager

.. nextslide::

Example compilers:

- GCC
- Clang
- Visual Studio

*Compilers translate source code from a human readable to a machine readable
form.*

.. nextslide::

Example linkers:

- ld
- ld.gold
- link.exe

*Linkers combine the results of compilers into a shared library that is
executed at program runtime.*

.. nextslide::

Example build systems:

- distutils.build_ext
- Unix Makefiles
- Ninja
- MSBuild in Visual Studio

*Builds systems coordinate invocation of the compiler and linker, passing
flags, and only out-of-date build targets are built.*

.. nextslide::

Example system introspection tools:

- CMake
- GNU Autotools
- Meson

*System introspection tools examine the host system for available build tools,
the location of build dependencies, and properties of the build target to
generate the appropriate build system configuration files.*

.. nextslide::

Example package managers:

- conda
- pip
- apt
- yum
- chocolatey
- homebrew

*Package managers resolve dependencies so the required build host artifacts are
available for the build.*

.. nextslide::

build host artifacts
  These are files required on the *host* system performing the build. This
  includes **header files**, `*.h` files, which define the C program **symbols**,
  i.e. variable and function names, for the native binary with which we want
  to integrate. This also usually includes the native binaries themselves,
  i.e. the **executable or shared library**. An important exception to this rule
  is *libpython*, which we do not need on some platforms due to `weak linking
  rules <https://scikit-build.readthedocs.io/en/latest/cmake-modules/targetLinkLibrariesWithDynamicLookup.html>`_.

.. nextslide::

target system artifacts
  These are artifacts intended to be run on the **target** system, typically the
  shared library C-extension.

.. nextslide::

When the build *host* system is different from the *target* system, we are
**cross-compiling**.

For example, when we are building a Linux Python package on macOS is
cross-compiling. In this case macOS is the *host* system and Linux is the
*target* system.

.. nextslide::

Distributable binaries must use a **compatible C-runtime**.

The table below lists the different C runtime implementations, compilers and
their usual distribution mechanisms for each operating systems.

.. table::

    +------------------+---------------------------+-------------------------+-----------------------------------+
    |                  | Linux                     | MacOSX                  | Windows                           |
    +==================+===========================+=========================+===================================+
    | **C runtime**    | `GNU C Library (glibc)`_  | `libSystem library`_    | `Microsoft C run-time library`_   |
    +------------------+---------------------------+-------------------------+-----------------------------------+
    | **Compiler**     | `GNU compiler (gcc)`_     | `clang`_                | Microsoft C/C++ Compiler (cl.exe) |
    +------------------+---------------------------+-------------------------+-----------------------------------+
    | **Provenance**   | `Package manager`_        | OSX SDK within `XCode`_ | - `Microsoft Visual Studio`_      |
    |                  |                           |                         | - `Microsoft Windows SDK`_        |
    +------------------+---------------------------+-------------------------+-----------------------------------+

.. _GNU C Library (glibc): https://en.wikipedia.org/wiki/GNU_C_Library
.. _Package manager: https://en.wikipedia.org/wiki/Package_manager
.. _Microsoft C run-time library: https://en.wikipedia.org/wiki/Microsoft_Windows_library_files#Runtime_libraries
.. _libSystem library: https://www.safaribooksonline.com/library/view/mac-os-x/0596003560/ch05s02.html
.. _XCode: https://en.wikipedia.org/wiki/Xcode#Version_comparison_table
.. _Microsoft Windows SDK: https://en.wikipedia.org/wiki/Microsoft_Windows_SDK
.. _Microsoft Visual Studio: https://en.wikipedia.org/wiki/Microsoft_Visual_Studio
.. _GNU compiler (gcc): https://en.wikipedia.org/wiki/GNU_Compiler_Collection
.. _clang: https://en.wikipedia.org/wiki/Clang

.. nextslide::

Linux C-runtime compatibility is determined by the version of **glibc** used
for the build.

The glibc library shared by the system is forwards compatible but not
backwards compatible. That is, a package built on an older system *will*
work on a newer system, while a package built on a newer system will not
work on an older system.

The `manylinux <https://github.com/pypa/manylinux>`_ project provides Docker
images that have an older version of glibc to use for distributable Linux
packages.

.. nextslide::

The C-runtime on macOS is determined by a build time option, the *osx
deployment target*, which defines the minmum version of macOS to support, e.g.
`10.9`.

A macOS system comes with support for running building binaries for its version of
OSX and older versions of OSX.

The XCode toolchain comes with SDK's that support multiple target versions of OSX.

When building a wheel, this can be specified with `--plat-name`::

    python setup.py bdist_wheel --plat-name macosx-10.6-x86_64

.. nextslide::

The C-runtime used on Windows is associated with the version of Visual Studio.

.. table::

    +-------------------+------------------------------------------------------+
    |                   | Architecture                                         |
    +-------------------+------------------------+-----------------------------+
    | CPython Version   | x86 (32-bit)           | x64 (64-bit)                |
    +===================+========================+=============================+
    | **3.5 and above** | Visual Studio 14 2015  | Visual Studio 14 2015 Win64 |
    +-------------------+------------------------+-----------------------------+
    | **3.3 to 3.4**    | Visual Studio 10 2010  | Visual Studio 10 2010 Win64 |
    +-------------------+------------------------+-----------------------------+
    | **2.7 to 3.2**    | Visual Studio 9 2008   | Visual Studio 9 2008 Win64  |
    +-------------------+------------------------+-----------------------------+

.. nextslide::

Distributable binaries are also built to be compatible with a certain
CPU architecture class. For example

- x86_64 (currently the most common)
- x86
- ppc64le


Scientific Python Build Tools
-----------------------------

**scikit-build** is an improved build system generator for CPython C/C++/Fortran/Cython
extensions.

.. nextslide::

**scikit-build** provides better support for additional compilers, build
systems, cross compilation, and locating dependencies and their associated
build requirements.

.. nextslide::

The **scikit-build** package is fundamentally just glue between
the `setuptools` Python module and `CMake <https://cmake.org/>`_.

.. nextslide::

To build and install a project configured with scikit-build::

  pip install .

.. nextslide::

To build and install a project configured with scikit-build for development::

  pip install -e .

.. nextslide::

To build and package a project configured with scikit-build::

  pip wheel -w dist .

.. nextslide::

**Conda** is an open source package management system and environment management system that runs on Windows, macOS and Linux.

.. nextslide::

**Conda** quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer.

.. nextslide::

**Conda** was created for Python programs, but it can package and distribute software for any language.

.. nextslide::

*scikit-build* and *conda* **abstract away** and **manage platform-specific details** for you!

Exercises
=========

Exercise 1: Build a Python Package with a C++ Extension Module
---------------------------------------------------------------

Download the `hello-cpp <https://github.com/python-packaging-tutorial/hello-cpp>`_ example C++ project and build a wheel package
with the commands::

  cd hello-cpp
  pip wheel -w dist --verbose .

Examine files referenced in the build output. What is the purpose of all
referenced files?

Exercise 2: Build a Python Package with a Cython Extension Module
-----------------------------------------------------------------

Download the `hello-cython
<https://github.com/python-packaging-tutorial/hello-cython>`_ example C++ project and build a wheel package
with the commands::

  cd hello-cython
  pip wheel -w dist --verbose .

Examine files referenced in the build output. What is the purpose of all
referenced files?

Bonus Exercise 3: Build a Distributable Linux Wheel Package
-----------------------------------------------------------

If Docker is installed, create a `dockcross
<https://github.com/dockcross/dockcross>`_ `manylinux`_ bash driver script.
From a bash shell, run::

  # cd into the hello-cpp project from Exercise 1
  cd hello-cpp
  docker run --rm dockcross/manylinux-x64 > ./dockcross-manylinux-x64
  chmod +x ./dockcross-manylinux-x64

The *dockcross* driver script simplifies execution of commands in the isolated
Docker build environment that use sources in the current working directory.

.. nextslide::

To build a distributable Python 3.6 Python wheel, run::

  ./dockcross-manylinux-x64 /opt/python/cp36-cp36m/bin/pip wheel -w dist .

Which will output::

  Processing /work
  Building wheels for collected packages: hello-cpp
  Running setup.py bdist_wheel for hello-cpp ... done
  Stored in directory: /work/dist
  Successfully built hello-cpp

and produce the wheel::

  ./dist/hello_cpp-1.2.3-cp36-cp36m-linux_x86_64.whl

.. nextslide::

To find the version of glibc required by the extension, run::

  ./dockcross-manylinux-x64 bash -c 'cd dist && unzip -o hello_cpp-1.2.3-cp36-cp36m-linux_x86_64.whl && objdump -T hello/_hello.cpython-36m-x86_64-linux-gnu.so | grep GLIBC'

What glibc version compatibility is required for this binary?


manylinux: https://github.com/pypa/manylinux
