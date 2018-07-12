===============================
Website and Presentation Slides
===============================

Overview
--------

This directory provides the infrastructure allowing to locally build the website
and slides associated with the tutorial.

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

Thanks to the integration of this GitHub project with readthedocs, this happens
automatically after the ``master`` branch is updated.

Historically, the website was only updated if a contributor was locally generating
the associated web pages and commiting them on the `gh-pages` branch.


Building the slides
-------------------

::

    make slides

Then, open ``build/slides/index.html``.
