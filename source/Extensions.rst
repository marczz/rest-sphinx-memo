*****************
Sphinx extensions
*****************

We have described in the previous section the extensions:
:ref:`intersphinx <intersphinx_extension>`,
:ref:`extlinks <extlinks_extension>`,
:ref:`ifconfig <ifconfig_extension>`.

.. index:
   pair: extension; todo
   pair: directive; todo
   pair: directive; todolist

todo extension
==============
The extension ``sphinx.ext.todo`` allow to include todo blocks like::
::

   .. todo::

         We need to achieve:

         .. include:: include/feature.rst


An other directive ``todolist`` is replaced by a list of all todo directives in the whole documentation.

These blocks are by default excluded but can be included by setting to
``True`` the configuration variable ``todo_include_todos``.

You can either set it in the ``conf.py`` file or trigger it by adding
the option to sphinx-build. An easy way is through the Make process by
doing:

.. code-block:: shell-session

   $ make -k html SPHINXOPTS="-D todo_include_todos=True"


.. index::
   math expression
   pair: extension; pngmath


Sphinx Math
===========

There are three  :sphinx:`mathematical typesetting Sphinx extensions
<ext/math.html>` :ref:`pngmath <pngmath_extension>`,
:sphinx:`mathjax
</ext/math.html#module-sphinx.ext.mathjax>`,
and
:sphinx:`jsmath
</ext/math.html#module-sphinx.ext.jsmath>`.

.. _pngmath_extension:

The extension :sphinx:`pngmath
</ext/math.html#module-sphinx.ext.pngmath>`
is based on LaTeX.

To enable the extension, the following line has to appear in ``conf.py``:

.. code-block:: python

   extensions = ['sphinx.ext.pngmath']

.. note:: The ``sphinx.ext.pngmath`` extension needs ``dvipng``.

You then can type standard LaTeX math expressions, either inline::

   :math:`‹LaTeX math expression›`

or in display mode::

   .. math::

      ‹LaTeX math expressions›

The second version is also available for a one line expression::

   .. math:: ‹1 Line LaTeX math expression›

.. sidebar:: Code for example

   ::

      Pythagoras :math:`a^2+b^2=c^2`

      .. math:: \sum_{n=0}^N x_n = y

E.g:

Pythagoras :math:`a^2+b^2=c^2`

.. math:: \sum_{n=0}^N x_n = y

:sphinx:`mathjax <ext/math.html#module-sphinx.ext.mathjax>`
is an other extension that render math through javascript.


Multiline Math
--------------

.. sidebar:: Code for example

   ::

      .. math::

         a+b = c

         b = x_n

         a &= y_n\\
           &= c-b

**Sphinx Built-in Mechanism**

Several lines of math expressions can be entered by leaving a blank line between
them.  In addition there is something like an ``align`` environment syntax if
lines are not separated by a blank line.

.. math::

   a+b = c

   b = x_n

   a &= y_n\\
     &= c-b


**Explicit LaTeX with amsmath mechanism**

If the option ``nowrap`` is specified then the full LaTeX code (including the
math-environment) has to be given.  We can assume that the :index:`amsmath` package
is loaded.  This is not limited to math typesetting, any LaTeX construct can be
rendered in this way.

+----------------------------------------+----------------------------------------+
|::                                      |                                        |
|                                        |.. math:: \[a = b\]                     |
|    .. math:: \[a = b\]                 |   :nowrap:                             |
|       :nowrap:                         |                                        |
|                                        |or equivalenty                          |
|    or equivalenty                      |                                        |
|                                        |.. math::                               |
|    .. math::                           |   :nowrap:                             |
|       :nowrap:                         |                                        |
|                                        |   \[a = b\]                            |
|       \[a = b\]                        |                                        |
|                                        |                                        |
+----------------------------------------+----------------------------------------+


Equation Numbers
----------------

Equations are labeled with the ``label`` option and referred to using::

  :eq:`‹label›`

.. sidebar:: Code for example

   ::

      .. math:: a^2 + b^2 = c^2
         :label: pythag

      See equation :eq:`pythag`.

E.g:

.. math:: a^2 + b^2 = c^2
   :label: pythag

See equation :eq:`pythag`.

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
