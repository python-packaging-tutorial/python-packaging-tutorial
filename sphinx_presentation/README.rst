===============================
Website and Presentation Slides
===============================

Overview
--------

This directory provides the infrastructure allowing to build the `website <https://python-packaging-tutorial.github.io/python-packaging-tutorial>`_ and set of slides associated the Python Packaging Tutorial.

Both are generated from the source files found in `sphinx_presentation/source <https://github.com/python-packaging-tutorial/python-packaging-tutorial/tree/master/sphinx_presentation/source>`_ directory.


Prerequisites
-------------

Create an environment and install requirements. For example::

    mkvirtualenv pypa-tutorial
    pip install -r requirements.txt


Building the website
--------------------

::

    make html


Then, open ``build/html/index.html``.


Publishing the website
----------------------

::

    ./build_gh_pages.sh



Building the slides
-------------------

::

    make slides

Then, open ``build/slides/index.html``.
