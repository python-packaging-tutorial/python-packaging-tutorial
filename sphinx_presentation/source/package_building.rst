####################
The Joy of Packaging
####################


Scipy 2018 Tutorial
===================

Instructors
-----------

Michael Sarahan, PhD: Conda-build tech lead, Anaconda, Inc.

Matt McCormick (thewtex): Maintainer of dockcross, of Python packages for the Insight Toolkit (ITK)

Jean-Christophe Fillion-Robin (jcfr): Maintainer of scikit-build, scikit-ci, scikit-ci-addons and python-cmake-buildsystem

Filipe Fernandes (ocefpaf): Conda-forge core team, Maintainer of folium and a variety of libraries for ocean sciences.

Matt Craig (mwcraig): Maintainer of ccdproc, reducer, astropy, lead on conda packaging for astropy, Conda-forge core team.

Chris Barker (PythonCHB): Python instructor for the Univ. Washington Continuing Education Program, Contributor to conda-forge project.

Ray Donnelly (mingwandroid): Anaconda employee, working on Anaconda Distribution. MSYS2 co-founder, Likes build systems too much.

Jonathan Helmus (jjhelmus): Anaconda employee, working on Anaconda Distribution Builds tensorflow for fun, conda-forge core team member
Contributor to various open source packages in the scientific Python ecosystem.


Outline
-------

Packaging fundamentals

Conda packaging

Compatibility and automation


What is a “package”?
--------------------

In a broad sense, anything you install using your package manager

some kinds of packages have implied behavior and requirements

Unfortunate overloading: python “package”: a folder that python imports


Package Managers and Repos
--------------------------

NPM, apt, yum, dnf, chocolatey, pip, conda, homebrew, etc.

PyPI, anaconda.org, CRAN, CPAN

Some form of dependency management

Artifact and/or source repository


Implicit behavior & Requirements
--------------------------------

Folder structure

Directly usable, or must be unpacked/installed?

Python packages

::

  sound/
      __init__.py
  formats/
      __init__.py
      wavwrite.py
  effects/
      __init__.py
      echo.py


``https://docs.python.org/3/tutorial/modules.html#packages``

Folders must have ``__init__.py`` file to make Python able to import them

``__init__.py`` can be empty (and is, most of the time)


``from sound.effects.echo import somefunc``

Python packages - why?
----------------------

.. code-block:: python

	# import nested module

	import sound.effects.echo

	from sound.effects import echo

	# import function or variable from nested module


https://docs.python.org/3/tutorial/modules.html#packages

::

    mypkg/
        __init__.py
        subpkg/
            __init__.py
            a.py



Let’s make a package
--------------------

Windows
.......


.. code-block::

	mkdir mypkg/subpkg

	echo. > mypkg/__init__.py

	echo . > mypkg/subpkg/__init__.py

	echo . > mypkg/subpkg/a.py


Mac/Linux
.........

.. code-block:: bash

	mkdir -p mypkg/subpkg

	touch mypkg/__init__.py

	touch mypkg/subpkg/__init__.py

	touch mypkg/subpkg/a.py


How Python finds packages
-------------------------

In python interpreter:

.. code-block: python

	import sys
	from pprint import pprint
	pprint(sys.path)



``sys.path`` explanation: https://stackoverflow.com/a/38403654/1170370



How to get things on sys.path
-----------------------------

.pth files in sys.path locations

``PYTHONPATH`` environment variable (fragile)

Installing packages (destination: site-packages folder)


Find your site-packages folder
------------------------------

Mac/Linux: ``(install root)/lib/pythonX.Y/site-packages``


Windows: ``(install root)\Lib\site-packages``


Installing packages
-------------------

pip install -e .


Installing:

.. code-block:: python

	python setup.py install

	pip install .

	Development installs:

	python setup.py develop



Installing
==========


Development install
-------------------

Copies package into site-packages

Adds a ``.pth`` file to site-packages, pointed at package source root

Used when creating conda packages

Used when developing software locally

Normal priority in sys.path

End of ``sys.path`` (only found if nothing else comes first)

https://grahamwideman.wikispaces.com/Python-+site-package+dirs+and+.pth+files


What about setup.py?
--------------------

.. code-block:: python

	#!/usr/bin/env

	pythonfrom setuptools import setups

	setup(name='Distutils',
	      version='1.0',
	      description='Python Distribution Utilities',
	      author='Greg Ward',
	      author_email='gward@python.net',
	      url='https://www.python.org/sigs/distutils-sig/',      packages=['distutils', 'distutils.command'],
	      )

``https://docs.python.org/2/distutils/setupscript.html``

What does setup.py do?
----------------------

Version & package metadata

List of packages to include

List of other files to include

Lists of dependencies

Lists of extensions to be compiled


Let’s write setup.py
--------------------

.. code-block:: python

    #!/usr/bin/env python

    from setuptools import setup

    setup(name='mypkg',
          version='1.0', # list folders, not files
          packages=['mypkg', 'mypkg.subpkg'],
          )


Setuptools
----------

Separate library (ships with Python by default, though)

Adds entry point capability

provides find_packages function (use with caution)

creates eggs by default (people spend time fighting this later in the process)



Where does setup.py go?
-----------------------

.. code-block::

	mypkg-src
	setup.py
	mypkg/
	    __init__.py
	    subpkg/
	        __init__.py
	        a.py

New outer folder

``setup.py`` alongside package to be installed

``mypkg`` is what will get installed

``mypkg-src`` is what gets linked to by develop


Try installing your package
---------------------------

.. code-block:: bash

	cd mypkg-src

	python setup.py install

	python -c “import mypkg.subpkg.a”



Go look in your ``site-packages`` folder


Making packages the easy way
----------------------------

``https://github.com/audreyr/cookiecutter``

.. code-block:: bash

    conda install -c conda-forge cookiecutter


Let’s make a project
--------------------

cookiecutter: ``https://goo.gl/Jge1g8``


That’s a shortened link to:

``https://github.com/conda/cookiecutter-conda-python``


What did we get?
----------------

Adding requirements in ``setup.py``

.. code-block:: python

	#!/usr/bin/env python
	from distutils.core import setup

	setup(name='mypkg',
	      version='1.0',
	      # list folders, not files
	      packages=['mypkg', 'mypkg.subpkg'],
          install_requires=['click'],
          )


Requirements in ``requirements.txt``

**common mistake:**

``requirements.txt`` often from pip freeze

Pinned way too tightly.  OK for env creation, bad for packaging.

Donald Stufft (PyPA): Abstract vs. Concrete dependencies


``https://caremad.io/posts/2013/07/setup-vs-requirement/``



Requirements in ``setup.cfg`` (ideal)

[metadata]name = my_package
version = attr:
src.VERSION[options]
packages = find:
install_requires =  click


``http://setuptools.readthedocs.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files``

Parseable without execution, unlike setup.py




Break time!
-----------

Up next: producing redistributable artifacts


Redistributable artifacts
-------------------------


sdists

wheels

conda packages

eggs (deprecated)


When/how to use an sdist
------------------------

Pure python (no build requirements)

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



Introducing conda-build
-----------------------

Orchestrates environment creation, activation, and build/test processes

Can build conda packages and/or wheels

Separate project from conda, but very tightly integrated

Open-source, actively developedhttps://github.com/conda/conda-build


Getting conda-build to work for you
-----------------------------------

Input: meta.yaml files

::

	package:

	  name: mypkg

	  version: 1.0


Let’s use conda-build
---------------------

.. code-block:: bash

	conda install conda-build

	conda build mypkg-src


What happened?
--------------

templates filled in, recipe interpreted

build environment created (isolated)

build script run

new files in build environment bundled into package

test environment created (isolated)

tests run on new package

cleanup


Obtaining recipes
------------------

Existing recipes (best)

https://github.com/AnacondaRecipes

https://github.com/conda-forge

Skeletons from other repositories (PyPI, CRAN, CPAN, RPM)

DIY


Anaconda Recipes
----------------

Official recipes that Anaconda uses for building packages

Since Anaconda 5.0, forked from conda-forge recipes.

Intended to be compatible with conda-forge long-term

Presently, ahead of conda-forge on use of conda-build 3 features


Conda-forge
-----------

Numfocus-affiliated community organization made up of volunteers

One github repository per recipe

Fine granularity over permissions

Heavy use of automation for building, deploying, and updating recipes

Free builds on public CI services (TravisCI, CircleCI, Appveyor)


Skeletons
---------

Read metadata from upstream repository

Translate that into a recipe

Will save you some boilerplate work

Might work out of the box (should not assume automatic, though)

.. nextslide::

.. code-block:: bash

	conda skeleton pypi

	conda skeleton pypi <package name on pypi>

	conda skeleton pypi click

	conda skeleton pypi --recursive pyinstrument


	conda skeleton cran

	conda skeleton cran <name of pkg on cran>

	conda skeleton cran acs

	conda skeleton cran --recursive biwt



When all else fails, write a recipe
-----------------------------------

Only required section:


.. code-block:: yaml

	package:

	  name: abc

	  version: 1.2.3


Source types
------------

url

git

hg

svn

local path

https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#source-section


Source patches
--------------

patch files live alongside meta.yaml

create patches with diff, git diff, or git format-patch


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#source-section


.. code-block:: yaml

	package:

	  name: test-patch

	  version: 1.2.3

	source:

	  url: https://zlib.net/zlib-1.2.11.tar.gz

	build:

	  script: exit 1

Exercise: let’s make a patch
----------------------------

https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#source-section

Builds that fail leave their build folders in place

look in output for source tree in: ``*/conda-bld/test-patch_<numbers>/work``

cd there


.. nextslide::

https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#source-section

.. code-block:: bash

	git init

	git add *

	git commit -am “init”

	edit file of choice

	git commit -m “changing file because …”

	git format-patch HEAD~1

.. nextslide::


copy that patch back alongside meta.yaml

modify meta.yaml to include the patch



Multiple sources
----------------

.. code-block:: yaml

	source:
	  - url: https://package1.com/a.tar.bz2
	    folder: stuff
	  - url: https://package1.com/b.tar.bz2
	    folder: stuff
	    patches:
	      - something.patch
	  - git_url: https://github.com/conda/conda-build
	    folder: conda-build


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#source-section

Build options
-------------

number: version reference of recipe (as opposed to version of source code)

script: quick build steps, avoid separate build.sh/bld.bat files

skip: skip building recipe on some platforms

entry_points: python code locations to create executables for

run_exports: add dependencies to downstream consumers to ensure compatibility

https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#build-section



Requirements
------------

build

host

run


Requirements: build vs. host
----------------------------

Historically, only build

Still fine to use only build

host introduced for cross compiling

host also useful for separating build tools from packaging environment


.. nextslide::

If in doubt, put everything in host

build is treated same as host for old-style recipes
(only build, no {{ compiler() }})

packages are bundled from host env, not build env


Post-build tests
----------------

Help ensure that you didn’t make a packaging mistake

Ideally checks that necessary shared libraries are included as dependencies



Post-build tests: dependencies
------------------------------

Describe dependencies that are required for the tests
(but not for normal package usage)

..code-block:: yaml

	test:
	  requires:
	    - pytest



Post-build tests: test files
----------------------------


run_test.pl, run_test.py, run_test.r, run_test.lua

Windows

Linux/Mac

run_test.bat

run_test.sh



Post-build tests
----------------

May have specific requirements

May specify files that must be bundled for tests (source_files)

imports: language specific imports to try, to verify correct installation

commands: sequential shell-based commands to run (not OS-specific)


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#test-section


Import tests
------------

.. code-block:: yaml

	test:

	  imports:

		- dateutil

		- dateutil.rrule

		- dateutil.parser

		- dateutil.tz


Test commands
-------------

.. code-block:: yaml

test:
  commands:
      - curl --version
      - curl-config --features  # [not win]
      - curl-config --protocols  # [not win]
      - curl https://some.website.com


Outputs - more than one pkg per recipe
--------------------------------------

.. code-block:: yaml

	package:
	  name: some-split
	  version: 1.0

	outputs:
	  - name: subpkg

	  - name: subpkg2


.. nextslide::

* Useful for consolidating related recipes that share (large) source

* Reduce update burden

* Reduce build time by keeping some parts of the build, while looping over other parts

* Also output different types of packages from one recipe (wheels)


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#outputs-section


Outputs rules
-------------

* list of dicts

* each list must have name or type key

* May use all entries from build, requirements, test, about sections

* May specify files to bundle either using globs or by running a script


Outputs examples
----------------

https://github.com/AnacondaRecipes/curl-feedstock/blob/master/recipe/meta.yaml


https://github.com/AnacondaRecipes/aggregate/blob/master/ctng-compilers-activation-feedstock/recipe/meta.yaml


Exercise: split a package
-------------------------

Curl is a library and an executable.  Splitting them lets us clarify where Curl is only a build time dependency, and where it also needs to be a runtime dependency.

Starting point:

https://github.com/conda-forge/curl-feedstock/tree/master/recipe


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#outputs-section



.. nextslide::

Solution:

https://github.com/AnacondaRecipes/curl-feedstock/tree/master/recipe


About section
-------------

Provide this stuff

[insert image here!]


Extra section: free-for-all
---------------------------

* Used for external tools or state management

* No schema

* Conda-forge’s maintainer list

* Conda-build’s notion of whether a recipe is “final”


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#extra-section


Break time!
-----------

Advanced recipe tricks coming next



Conditional lines (selectors)
-----------------------------

::

  some_content    # [some expression]


content inside [] is eval’ed

namespace includes OS info, python info, and a few others


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#preprocessing-selectors


Exercise: limit a recipe to only Linux
--------------------------------------

.. code-block:: yaml

	package:
	  name: example_skip_recipe
	  version: 1.0

	  build:
	  skip: True

.. nextslide::

.. code-block:: yaml

	package:
	  name: example_skip_recipe
	  version: 1.0

	  build:
	  skip: True# [not linux]


Intro to templating with Jinja2
--------------------------------

* Fill in information dynamically

	- git tag info

	- setup.py recipe data

	- centralized version numbering

	- string manipulation

How does templating save you time?
----------------------------------

.. code-block:: yaml

	{% set version = "3.0.2" %}
	package:
	  name: example
	  version: {{ version }}
	source:
	  url: https://site/{{version}}.tgz


Jinja2 templating in meta.yaml
------------------------------

Set variables::

  {% set somevar=”someval” %}

Use variables::

  {{ somevar }}

Expressions in ``{{ }}`` are roughly python


Jinja2 conditionals
-------------------

Selectors are one line only.  When you want to toggle a block,
use jinja2::

  {%- if foo -%}

  toggled content

  on many lines

  {% endif %}


Exercise: use Jinja2 to reduce edits
------------------------------------

.. code-block:: yaml

	package:

	  name: abc

	  version: 1.2.3

	source:

	  url: http://my.web/abc-1.2.3.tgz


Variants: Jinja2 on steroids
----------------------------

Matrix specification in yaml files

.. code-block:: yaml

	somevar:

	  - 1.0

	  - 2.0

	anothervar:

	  - 1.0


All variant variables exposed in jinja2
---------------------------------------

In meta.yaml,

``{{ somevar }}``

And this loops over values


Exercise: try looping
---------------------

meta.yaml:

.. code-block:: yaml

	package:

	  name: abc

	  version: 1.2.3

	build:

	  skip: True # [skipvar]

	conda_build_config.yaml:

	skipvar:

			- True

	- False

.. nextslide::

meta.yaml:

.. code-block:: yaml

	package:

	  name: abc

	  version: 1.2.3

	requirements:

	  build:

	    - python {{ python }}

	  run:

	    - python {{ python }}

conda_build_config.yaml:

.. code-block:: yaml

	python:

			- 2.7

	- 3.6

.. nextslide::

meta.yaml:

.. code-block:: yaml

	package:

	  name: abc

	  version: 1.2.3

	requirements:

	  build:

	    - python

	  run:

	    - python

.. nextslide::

conda_build_config.yaml:

.. code-block:: yaml

	python:

			- 2.7

	- 3.6


Jinja2 functions
----------------

load_setup_py_data

load_file_regex

pin_compatible

pin_subpackage

compiler

cdt


Dynamic pinning

Loading source data

Compatibility control


Loading setup.py data
---------------------

.. code-block:: yaml

	{% set setup_data = load_setup_py_data() %}

	package:
	  name: abc
	  version: {{ setup_data[‘version’] }}


Primarily a development recipe tool - release recipes specify version instead, and template source download link

Centralizing version info is very nice - see also versioneer, setuptools_scm, autover, and many other auto-version tools

81



Loading arbitrary data

{% set data = load_file_regex(load_file='meta.yaml',                    regex_pattern='git_tag: ([\\d.]+)') %}

package:

  name: conda-build-test-get-regex-data

  version: {{ data.group(1) }}

Useful when software provides version in some arbitrary file

Primarily a development recipe tool - release recipes specify version instead, and template source download link

82

82



Dynamic pinning

Use in meta.yaml, generally in requirements section:

requirements:

  host:

    - numpy

  run:

    - {{ pin_compatible(‘numpy’) }}

83

83



Dynamic pinning

Use in meta.yaml, generally in requirements section:

requirements:

  host:

    - numpy

  run:

    - {{ pin_compatible(‘numpy’) }}

84

Pin run req based on what is present at build time

84



Dynamic pinning in practice

Used a lot with numpy:

https://github.com/AnacondaRecipes/scikit-image-feedstock/blob/master/recipe/meta.yaml

85

85



Dynamic pinning within recipes

Refer to other outputs within the same recipe

when intradependencies exist

when shared libraries are consumed by other libraries

https://github.com/AnacondaRecipes/aggregate/blob/master/clang/meta.yaml



86

86



Compilers

Use in meta.yaml in requirements section:

requirements:  build:    - {{ compiler(‘c’) }}

explicitly declare language needs

compiler packages can be actual compilers, or just activation scripts

Compiler packages utilize run_exports to add necessary runtime dependencies automatically

87

87



run_exports

88

package:

  name: abc

  version: 1.0



build:

  run_exports:

    - abc 1.0.*

Upstream package “abc” (already built)

Downstream recipe

requirements:

  host:

    - abc



requirements:

  host:

    - abc 1.0 0

  run:

    - abc 1.0.*



Downstream package

88



run_exports

Add host or run dependencies for downstream packages that depend on upstream that specifies run_exports

expresses idea that “if you build and link against library abc, you need a runtime dependency on library abc”

Simplifies version tracking

89

89



Requirements: run_exports

90

build

host

run

“Strong” run_exports

“Weak” run_exports

90



Uploading packages: anaconda.org

91

91



Uploading packages: PyPI

92

92



Anaconda Survey

https://www.surveymonkey.com/r/conda

93


Install

Development install

Copies package into site-packages

Adds a .pth file to site-packages, pointed at package source root

Used when creating conda packages

Used when developing software locally

Normal priority in sys.path

End of sys.path (only found if nothing else comes first)

https://grahamwideman.wikispaces.com/Python-+site-package+dirs+and+.pth+files



What about setup.py?

#!/usr/bin/env pythonfrom setuptools import setupsetup(name='Distutils',      version='1.0',      description='Python Distribution Utilities',      author='Greg Ward',      author_email='gward@python.net',      url='https://www.python.org/sigs/distutils-sig/',      packages=['distutils', 'distutils.command'],     )


https://docs.python.org/2/distutils/setupscript.html

Lists of extensions to be compiled
----------------------------------
What does setup.py do?

Version & package metadata

List of packages to include

List of other files to include

Lists of dependencies


#!/usr/bin/env pythonfrom setuptools import setupsetup(name='mypkg',      version='1.0',      # list folders, not files      packages=['mypkg', 'mypkg.subpkg'],     )
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Let’s write setup.py


creates eggs by default (people spend time fighting this later in the process)
------------------------------------------------------------------------------
Setuptools

Separate library (ships with Python by default, though)

Adds entry point capability

provides find_packages function (use with caution)


mypkg/    __init__.py    subpkg/        __init__.py        a.py
-------------------------------------------------------------------
Where does setup.py go?

mypkg-src

setup.py


New outer folder

setup.py alongside package to be installed

mypkg is what will get installed

mypkg-src is what gets linked to by develop

Go look in your site-packages folder
------------------------------------
Try installing your package

cd mypkg-src

python setup.py install

python -c “import mypkg.subpkg.a”






Making packages the easy way

https://github.com/audreyr/cookiecutter





conda install -c conda-forge cookiecutter


https://github.com/conda/cookiecutter-conda-python
--------------------------------------------------
Let’s make a project

cookiecutter https://goo.gl/Jge1g8



That’s a shortened link to:


What did we get?
----------------

install_requires=['click'],     )
----------------------------------
Adding requirements in setup.py

#!/usr/bin/env pythonfrom distutils.core import setupsetup(name='mypkg',      version='1.0',      # list folders, not files      packages=['mypkg', 'mypkg.subpkg'],


Donald Stufft (PyPA): Abstract vs. Concrete dependencies
--------------------------------------------------------
Requirements in requirements.txt

common mistake

requirements.txt often from pip freeze

Pinned way too tightly.  OK for env creation, bad for packaging.


https://caremad.io/posts/2013/07/setup-vs-requirement/



Requirements in setup.cfg (ideal)

[metadata]name = my_packageversion = attr: src.VERSION[options]packages = find:install_requires =  click


http://setuptools.readthedocs.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files

Parseable without execution, unlike setup.py

Up next: producing redistributable artifacts
--------------------------------------------
Break time!


eggs (deprecated)
-----------------
Redistributable artifacts

sdists

wheels

conda packages


python setup.py sdist
---------------------
When/how to use an sdist

Pure python (no build requirements)


Wheels vs. Conda packages
-------------------------

Wheels

Conda packages

Employed by pip, blessed by PyPA

Foundation of Anaconda ecosystem

Used by any python installation

Used by conda python installations

Mostly specific to Python ecosystem

 General purpose (any ecosystem)

Good mechanism for specifying range of python compatibility

 Primitive support for multiple python

     versions (noarch)

Depends on static linking or other system package managers to provide core libraries

Can bundle core system-level shared libraries as packages, and resolve dependencies

Open-source, actively developedhttps://github.com/conda/conda-build
--------------------------------------------------------------------
Introducing conda-build

Orchestrates environment creation, activation, and build/test processes

Can build conda packages and/or wheels

Separate project from conda, but very tightly integrated


version: 1.0
------------
Getting conda-build to work for you

Input: meta.yaml files

package:

  name: mypkg


conda build mypkg-src
---------------------
Let’s use conda-build

conda install conda-build


cleanup
-------
What happened?

templates filled in, recipe interpreted

build environment created (isolated)

build script run

new files in build environment bundled into package

test environment created (isolated)

tests run on new package


DIY
---
Obtaining recipes

Existing recipes (best)

https://github.com/AnacondaRecipes

https://github.com/conda-forge

Skeletons from other repositories (PyPI, CRAN, CPAN, RPM)




Presently, ahead of conda-forge on use of conda-build 3 features
----------------------------------------------------------------
AnacondaRecipes

Official recipes that Anaconda uses for building packages

Since Anaconda 5.0, forked from conda-forge recipes.

Intended to be compatible with conda-forge long-term


Free builds on public CI services (TravisCI, CircleCI, Appveyor)
----------------------------------------------------------------
Conda-forge

Numfocus-affiliated community organization made up of volunteers

One github repository per recipe

Fine granularity over permissions

Heavy use of automation for building, deploying, and updating recipes


Might work out of the box (should not assume automatic, though)
---------------------------------------------------------------
Skeletons

Read metadata from upstream repository

Translate that into a recipe



Will save you some boilerplate work


conda skeleton pypi --recursive pyinstrument
--------------------------------------------
conda skeleton pypi

conda skeleton pypi <package name on pypi>

conda skeleton pypi click




conda skeleton cran --recursive biwt
------------------------------------
conda skeleton cran

conda skeleton cran <name of pkg on cran>

conda skeleton cran acs




version: 1.2.3
--------------
When all else fails, write a recipe

Only required section:

package:

  name: abc


local path
----------
Source types

url

git

hg

svn


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#source-section

create patches with diff, git diff, or git format-patch
-------------------------------------------------------
Source patches

patch files live alongside meta.yaml


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#source-section

Exercise: let’s make a patch
----------------------------
package:

  name: test-patch

  version: 1.2.3

source:

  url: https://zlib.net/zlib-1.2.11.tar.gz

build:

  script: exit 1


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#source-section

Exercise: let’s make a patch
----------------------------
Builds that fail leave their build folders in place

look in output for source tree in: */conda-bld/test-patch_<numbers>/work

cd there




https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#source-section

Exercise: let’s make a patch
----------------------------
git init

git add *

git commit -am “init”

edit file of choice

git commit -m “changing file because …”

git format-patch HEAD~1




https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#source-section

Exercise: let’s make a patch
----------------------------
copy that patch back alongside meta.yaml

modify meta.yaml to include the patch




https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#source-section



Multiple sources

source:  - url: https://package1.com/a.tar.bz2    folder: stuff  - url: https://package1.com/b.tar.bz2    folder: stuff    patches:      - something.patch  - git_url: https://github.com/conda/conda-build    folder: conda-build


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#source-section

Build options
-------------

number: version reference of recipe (as opposed to version of source code)

script: quick build steps, avoid separate build.sh/bld.bat files

skip: skip building recipe on some platforms

entry_points: python code locations to create executables for

run_exports: add dependencies to downstream consumers to ensure compatibility

https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#build-section

Requirements
------------

build

host

run

host also useful for separating build tools from packaging environment
----------------------------------------------------------------------
Requirements: build vs. host

Historically, only build

Still fine to use only build

host introduced for cross compiling


packages are bundled from host env, not build env
-------------------------------------------------
Requirements: build vs. host

If in doubt, put everything in host



build is treated same as host for old-style recipes (only build, no {{ compiler() }})




Post-build tests

Help ensure that you didn’t make a packaging mistake

Ideally checks that necessary shared libraries are included as dependencies


- pytest
--------
Post-build tests: dependencies

Describe dependencies that are required for the tests (but not for normal package usage)

test:

  requires:


Post-build tests: test files
----------------------------

run_test.pl, run_test.py, run_test.r, run_test.lua

Windows

Linux/Mac

run_test.bat

run_test.sh

commands: sequential shell-based commands to run (not OS-specific)
------------------------------------------------------------------
Post-build tests

May have specific requirements

May specify files that must be bundled for tests (source_files)

imports: language specific imports to try, to verify correct installation


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#test-section

- dateutil.tz
-------------
Import tests

test:

  imports:

	- dateutil

	- dateutil.rrule

	- dateutil.parser


test:  commands:    - curl --version    - curl-config --features  # [not win]    - curl-config --protocols  # [not win]    - curl https://some.website.com
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Test commands


- name: subpkg2
---------------
Outputs - more than one pkg per recipe

package:

  name: some-split  version: 1.0

outputs:

  - name: subpkg


subpkg

subpkg2

https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#outputs-section

Also output different types of packages from one recipe (wheels)
----------------------------------------------------------------
Outputs - more than one pkg per recipe

Useful for consolidating related recipes that share (large) source

Reduce update burden

Reduce build time by keeping some parts of the build, while looping over other parts


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#outputs-section

May specify files to bundle either using globs or by running a script
---------------------------------------------------------------------
Outputs rules

list of dicts

each list must have name or type key

May use all entries from build, requirements, test, about sections


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#outputs-section

https://github.com/AnacondaRecipes/aggregate/blob/master/ctng-compilers-activation-feedstock/recipe/meta.yaml
-------------------------------------------------------------------------------------------------------------
Outputs examples

https://github.com/AnacondaRecipes/curl-feedstock/blob/master/recipe/meta.yaml




https://github.com/conda-forge/curl-feedstock/tree/master/recipe
----------------------------------------------------------------
Exercise: split a package

Curl is a library and an executable.  Splitting them lets us clarify where Curl is only a build time dependency, and where it also needs to be a runtime dependency.

Starting point:


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#outputs-section

https://github.com/AnacondaRecipes/curl-feedstock/tree/master/recipe
--------------------------------------------------------------------
Exercise: split a package

Solution:


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#outputs-section

About section
-------------
https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#about-section


Provide this stuff

Conda-build’s notion of whether a recipe is “final”
---------------------------------------------------
Extra section: free-for-all

Used for external tools or state management

No schema

Conda-forge’s maintainer list


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#extra-section

Advanced recipe tricks coming next
----------------------------------
Break time!


namespace includes OS info, python info, and a few others
---------------------------------------------------------
Conditional lines (selectors)

some_content    # [some expression]



content inside [] is eval’ed


https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#preprocessing-selectors

Exercise: limit a recipe to only Linux
--------------------------------------

https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#preprocessing-selectors



Intro to templating with Jinja2

Fill in information dynamically

git tag info

setup.py recipe data

centralized version numbering

string manipulation


Expressions in {{ }} are roughly python
---------------------------------------
Jinja2 templating in meta.yaml

Set variables:

{% set somevar=”someval” %}

Use variables:

{{ somevar }}




Jinja2 conditionals

Selectors are one line only.  When you want to toggle a block, use jinja2:

{%- if foo -%}

toggled content

on many lines

{% endif %}


url: http://my.web/abc-1.2.3.tgz
--------------------------------
Exercise: use Jinja2 to reduce edits

package:

  name: abc

  version: 1.2.3

source:


- 1.0
-----
Variants: Jinja2 on steroids

Matrix specification in yaml files

somevar:

  - 1.0

  - 2.0

anothervar:


And this loops over values
--------------------------
All variant variables exposed in jinja2

In meta.yaml,



{{ somevar }}




skip: True # [skipvar]
----------------------
Exercise: try looping

meta.yaml:

package:

  name: abc

  version: 1.2.3

build:


conda_build_config.yaml:

skipvar:

		- True

- False

- python {{ python }}
---------------------
Exercise: try looping

meta.yaml:

package:

  name: abc

  version: 1.2.3

requirements:

  build:

    - python {{ python }}

  run:


conda_build_config.yaml:

python:

		- 2.7

- 3.6

- python
--------
Exercise: try looping

meta.yaml:

package:

  name: abc

  version: 1.2.3

requirements:

  build:

    - python

  run:


conda_build_config.yaml:

python:

		- 2.7

- 3.6

cdt
---
Jinja2 functions

load_setup_py_data

load_file_regex

pin_compatible

pin_subpackage

compiler


Dynamic pinning

Loading source data

Compatibility control

Loading setup.py data
---------------------

{% set setup_data = load_setup_py_data() %}



package:

  name: abc

  version: {{ setup_data[‘version’] }}





Primarily a development recipe tool - release recipes specify version instead, and template source download link

Centralizing version info is very nice - see also versioneer, setuptools_scm, autover, and many other auto-version tools

Primarily a development recipe tool - release recipes specify version instead, and template source download link
----------------------------------------------------------------------------------------------------------------
Loading arbitrary data

{% set data = load_file_regex(load_file='meta.yaml',                    regex_pattern='git_tag: ([\\d.]+)') %}

package:

  name: conda-build-test-get-regex-data

  version: {{ data.group(1) }}

Useful when software provides version in some arbitrary file


- {{ pin_compatible(‘numpy’) }}
-------------------------------
Dynamic pinning

Use in meta.yaml, generally in requirements section:

requirements:

  host:

    - numpy

  run:


- {{ pin_compatible(‘numpy’) }}
-------------------------------
Dynamic pinning

Use in meta.yaml, generally in requirements section:

requirements:

  host:

    - numpy

  run:


Pin run req based on what is present at build time

https://github.com/AnacondaRecipes/scikit-image-feedstock/blob/master/recipe/meta.yaml
--------------------------------------------------------------------------------------
Dynamic pinning in practice

Used a lot with numpy:




Dynamic pinning within recipes

Refer to other outputs within the same recipe

when intradependencies exist

when shared libraries are consumed by other libraries

https://github.com/AnacondaRecipes/aggregate/blob/master/clang/meta.yaml


Compiler packages utilize run_exports to add necessary runtime dependencies automatically
-----------------------------------------------------------------------------------------
Compilers

Use in meta.yaml in requirements section:

requirements:  build:    - {{ compiler(‘c’) }}

explicitly declare language needs

compiler packages can be actual compilers, or just activation scripts


run_exports
-----------

package:

  name: abc

  version: 1.0



build:

  run_exports:

    - abc 1.0.*

Upstream package “abc” (already built)

Downstream recipe

requirements:

  host:

    - abc



requirements:

  host:

    - abc 1.0 0

  run:

    - abc 1.0.*



Downstream package

Simplifies version tracking
---------------------------
run_exports

Add host or run dependencies for downstream packages that depend on upstream that specifies run_exports

expresses idea that “if you build and link against library abc, you need a runtime dependency on library abc”


Requirements: run_exports
-------------------------

build

host

run

“Strong” run_exports

“Weak” run_exports

Uploading packages: anaconda.org
--------------------------------

Uploading packages: PyPI
------------------------

https://www.surveymonkey.com/r/conda
------------------------------------
Anaconda Survey

