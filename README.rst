===============================
pinecone
===============================

.. image:: https://img.shields.io/travis/audreyr/pinecone.svg
        :target: https://travis-ci.org/audreyr/pinecone

.. image:: https://img.shields.io/pypi/v/pinecone.svg
        :target: https://pypi.python.org/pypi/pinecone


Pinecone is a Processing-inspired drawing library powered by Pillow.

* Free software: BSD license
* Documentation: https://pinecone.readthedocs.org.

Features
--------

Easy Syntax
~~~~~~~~~~~~

Here is a simple Pinecone script::

    from pinecone import size, ellipse

    size(600, 400)
    ellipse(300, 200, 100, 40)

Pinecone is designed to be simple enough for first-time programmers to use, including:

* Artists of all ages who come from non-programming backgrounds
* Elementary school-aged children
* Teens
* Adults who learn best visually

When you run a Pinecone script, your drawing is automatically displayed.

It's Just Python
~~~~~~~~~~~~~~~~~

Pinecone scripts are just standard Python scripts. You run them like this::

    python hello.py

This means that:

* You can use other Python modules in your Pinecone scripts, such as `math`, `random`, and even third-party libraries
* The learning curve between learning Pinecone and learning Python is minimized, since you can use a standard text editor and command line

Status
-------

Pre-alpha, currently just a proof-of-concept.