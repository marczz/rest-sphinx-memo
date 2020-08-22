*****************
Sphinx extensions
*****************

We have described in the previous section the extensions:
:ref:`autosectionlabel <autosectionlabel>`,
:ref:`intersphinx <intersphinx_extension>`,
:ref:`extlinks <extlinks_extension>`,
:ref:`ifconfig <ifconfig_extension>`,
:ref:`napoleon <napoleon_extension>`.

There are part of :sphinx:`Sphinx builtin extensions <usage/extensions/>`, a
collection of third-party Sphinx extensions is in `sphinx-contrib repository
<https://bitbucket.org/birkenfeld/sphinx-contrib>`_.

`Awesome Sphinx <https://github.com/yoloseem/awesome-sphinxdoc>`_ has also a list of
extensions, and sphinx documentation has :sphinx:`extension tutorials
<tutorials/index.html>` and a :sphinx:`Developing extensions for Sphinx
<extdev/>` chapter.



.. index:
   pair: extension; todo
   pair: directive; todo
   pair: directive; todolist

todo extension
==============

The extension :sphinx:`sphinx.ext.todo <ext/todo.html>` allow to
include todo blocks like ::

   .. todo::

         We need to achieve:

         .. include:: include/feature.rst


An other directive ``todolist`` is replaced by a list of all todo
directives in the whole documentation.

These blocks are by default excluded but can be included by setting to
``True`` the configuration variable ``todo_include_todos``.

You can either set it in the ``conf.py`` file or trigger it by adding
the option to sphinx-build. An easy way is through the Make process by
doing:

.. code-block:: shell-session

   $ make -k html SPHINXOPTS="-D todo_include_todos=1"


.. index::
   math expression
   pair: extension; pngmath


Math Extensions.
================

There are three  :sphinx:`mathematical typesetting Sphinx extensions
<ext/math.html>` :ref:`imgmath <imgmath_extension>`,
:sphinx:`mathjax
</ext/math.html#module-sphinx.ext.mathjax>`,
and
:sphinx:`jsmath
</ext/math.html#module-sphinx.ext.jsmath>`.

.. _imgmath_extension:

The extension :sphinx:`imgmath
</ext/math.html#module-sphinx.ext.pngmath>`
use LaTeX and ``dvipng`` or ``dvisvgm`` to render math into PNG or SVG
images. You need to install one of these utilities on the machine
where the doc is built.

To enable the extension, the following line has to appear in ``conf.py``:

.. code-block:: python

   extensions = ['sphinx.ext.imgmath']



:sphinx:`Mathjax <ext/math.html#module-sphinx.ext.mathjax>`
and its predecessor :sphinx:`jsmath
<ext/math.html#module-sphinx.ext.jsmath>`
render math through javascript.




.. index::
   pair: extension; graphviz

Graphs with :index:`Graphviz`
=============================

The `Graphviz
<http://graphviz.org/>`_
`graph drawing Sphinx extension
<http://sphinx.pocoo.org/ext/graphviz.html>`_ is provided in Sphinx distribution.

To enable the extension we have to add it to the ``extensions`` list in
``conf.py``::

  extensions = ['sphinx.est.graphviz']

It uses directly the dot command to process `DOT language
<http://graphviz.org/content/dot-language>`_.


Examples
--------

.. sidebar::  graph

   Undirected::

      .. graph:: foo

         "bar" -- "baz";

   Directed::

      .. digraph:: foo

         "bar" -> "baz";

.. graph:: foo

   "bar" -- "baz";

.. digraph:: foo

   "bar" -> "baz";
