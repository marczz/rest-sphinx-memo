***********************
:mod:`Sphinx` -- Sphinx
***********************

.. module:: Sphinx
   :synopsis:  Sphinx Memo.
.. moduleauthor:: Marc Zonzon <marc.zonzon@gmail.com>

.. highlight:: rest
.. index::
   pair: role; sphinx
   pair: sphinx; in-line markup

.. contents::
   :local:
   :depth: 1

.. _sphinx_inline_markup:

Sphinx inline markup
====================

.. contents::
   :local:

:sphinx:`sphinx reference: Inline markup <markup/inline.html>`

.. _sphinx_roles:

Sphinx inline markup is down through interpreted text roles;
they are written ``:rolename:`content`.``.

There are three types of roles:

- The :ref:`ReStructuredText Text Roles <rest_roles>`.
-  The Sphinx roles that are described in the section
   :ref:`sphinx_role` and the :ref:`Sphinx cross references
   <sphinx_cross_references>`
-  The roles added by :sphinx:`Sphinx domains <domains.html>` like
   the :ref:`Python roles <python_roles>` referenced below.

.. _sphinx_ref:
.. _sphinx_cross_references:

.. index::
   pair: sphinx; cross-reference

Location cross references
-------------------------
:sphinx:`sphinx ref:  Cross-referencing arbitrary locations
<markup/inline.html#cross-referencing-arbitrary-locations>`

We use::

   :ref:`displayed text <label>`

To reference ``label`` defined in *any* document of the project.
It allows linking across files, while the :ref:`rest way <rest_ref>`
is limited to a location in the same file.

If the ``label`` definition is followed by a section title then ``displayed
text`` can be omitted and will be replaced by the title.

E.g. the *rest reference* section is preceded
with ``.. _internal:``, so we have:

================================== ==============================
``:ref:`internal```                :ref:`internal`
``:ref:`This section <internal>``` :ref:`This section <internal>`
``:ref:`ref to a name <mytopic>``` :ref:`ref to a name <mytopic>`
================================== ==============================

.. index::
   pair: document; cross-reference

Cross-referencing documents
---------------------------
:sphinx:`sphinx ref: Cross-referencing documents
<markup/inline.html#cross-referencing-documents>`

In Sphinx it is possible to reference a document as follows

===============  ==============
``:doc:`ReST```  :doc:`ReST`
===============  ==============

.. index::
   pair: role; cross-reference

Extra cross-reference roles
---------------------------
Many are described in the
:sphinx:`sphinx ref:Cross-referencing other items of interest
<markup/inline.html#cross-referencing-other-items-of-interest>`.

To reference  a Python Enhancement Proposal use ``:pep:``, for a
Request for Comments ``:rfc:``

.. index::
   pair: extension; intersphinx
   pair: extension; extlink
   single: hyperlink; target

Extensions that define new hyperlinks targets
---------------------------------------------
.. _intersphinx_extension:
.. _extlinks_extension:

-  The :sphinx:`intersphinx extension <ext/intersphinx.html>`
   generates automatic links to the documentation
   in other projects for objects not in your own project. It interprets
   the  references  to `roles <role>`_

   To configure it, give in ``conf.py`` a dictionary like::

      intersphinx_mapping = {
          'python': ('http://docs.python.org/3', None)}

-  The extension :sphinx:`extlinks <ext/extlinks.html>` help when you
   have many links pointing to the same site. I use it for the
   previous reference with the code
   ``:sphinx:`extlinks <ext/extlinks.html>``` and the configuration::

      extlinks = {'sphinx': ('http://sphinx.pocoo.org/en/latest/%s', 'Sphinx: ')}


.. index
   pair: sphinx; role

.. _sphinx_role:


Sphinx Roles
------------

The Sphinx roles  are described in :sphinx:`Sphinx: Inline markup
<markup/inline.html>`
and in the specific domains,  e.g.
:sphinx:`python roles <domains.html#python-roles>`.

Some common markup are:

+--------------------------------------+-----------------------------------+
|``:abbr:`RFC(request for comments)``` |:abbr:`RFC(request for comments)`  |
|                                      |                                   |
+--------------------------------------+-----------------------------------+
| ``:file:`/etc/profile```             |:file:`/etc/profile`               |
+--------------------------------------+-----------------------------------+
| ``:manpage:`ls(1)```                 |:manpage:`ls(1)`                   |
+--------------------------------------+-----------------------------------+
| ``:regexp:`^[a-z]*.[0-9]```          |:regexp:`^[a-z]*.[0-9]`            |
+--------------------------------------+-----------------------------------+
| ``:samp:`cp {file} {target}```       |:samp:`cp {file} {target}`         |
+--------------------------------------+-----------------------------------+

.. index
   pair: python; role

.. _python_roles:

python roles
------------

.. tabularcolumns:: |p{0.15\linewidth}||p{0.25\linewidth}|

+----------------+------------------------------------------+
|    role        |       reference                          |
+================+==========================================+
| ``:py:mod:``   | module                                   |
+----------------+------------------------------------------+
| ``:py:func:``  | function                                 |
+----------------+------------------------------------------+
| ``:py:data:``  | module-level variable.                   |
+----------------+------------------------------------------+
| ``:py:const:`` | constant                                 |
+----------------+------------------------------------------+
| ``:py:class:`` | class [#dotted]_                         |
+----------------+------------------------------------------+
| ``:py:meth:``  | method [#dotted]_ [#text]_               |
+----------------+------------------------------------------+
| ``:py:attr:``  | data attribute of an object              |
+----------------+------------------------------------------+
| ``:py:exc:``   | exception [#dotted]_                     |
+----------------+------------------------------------------+


.. [#dotted] Class, methods, exceptions may be dotted names.
.. [#text] The role text should include the type name and the method name


You may supply an explicit title and reference target: ``:role:`title
<target>```.

.. index::
   pair: directive; sphinx

Sphinx directives
=================

Sphinx includes its own :sphinx:`directives <markup/index.html>`, which
are not available in the docutils builders.

.. We reference here

   :ref:`toctree`, :ref:`index`, :ref`glossary`,
   :ref:`note`, :ref:`warning`, :ref:`seealso`,
   :ref:`only`,  :ref:`role`, :ref:`only`, :ref:`ifconfig`

.. contents::
   :local:

.. index::
   pair: toctree; directive
   see toc; table of contents
   see toc; toctree

.. _toctree:

table of contents
-----------------
::

   .. toctree::
      :maxdepth: ‹depth›
      :glob:

      ‹file 1 without file name extension›
      ‹file 2 without file name extension›

The :sphinx:`toctree directive <markup/toctree.html>` create a table of
contents across files.

A ``glob`` option enables to use wildcards in the filenames, e.g. ``/comp/*``
means all files under the directory ``comp``.

Relative names are relative to the document the directive occurs in,
absolute names are relative to the source directory.

The depth can be further restricted per file by inserting the
following :ref:`Field list` type element in the very first line of the file::

   :tocdepth: ‹depth›

See :sphinx:`Sphinx: Toc tree <markup/toctree.html>` for other
options.

To get a table of content *inside* a file, use the :ref:`reST table of
contents <reST-tableOfContents>`

.. index::
   pair: index; directive
   index; single
   index; pair
   index; triple
   index; see
   index; seealso

.. _index:

Index
-----

Entries in the :sphinx:`index
<markup/misc.html#index-generating-markup>`
are created automatically from all information units
like functions, classes or attributes but those with a ``:noindex:``
option.  Explicit manual entries are made as::

   .. index:: ‹entry 1›, ‹entry 2›, !<entry 3> ...
      single: ‹entry›; ‹sub-entry›
      pair: ‹1st part›; ‹2nd part›
      triple:  ‹1st part›; ‹2nd part›; <3rd part>

The first two versions create single (sub-)entries, while `pair`
creates two entries "‹1st part›; ‹2nd part›" and "‹2nd part›; <1st
part›"; and `triple` makes three entries.

With the exclamation mark, the *<entry 3>* is the main entry for this
term and is put in bold.

You can also use the keywords  `see` and `seealso` with ``see: foo
bar`` or ``seealso: bar foo``.

.. index::
   pair: glossary; directive

.. _glossary:

glossary
--------

A :sphinx:`glossary <markup/para.html#directive-glossary>`
is a :ref:`definition_list`::

   .. glossary::
      :sorted:

      name1
      name2
         definition of both name1 and name2

.. index::
   pair: note; directive
   pair: warning; directive
   pair: seealso; directive

.. _note:
.. _warning:
.. _seealso:

note, warning, seealso
----------------------

They are :sphinx:`paragraph-level markups <markup/para.html>`

.. sidebar:: Code

   ::

      .. note:: ‹text›


   ::

       .. warning:: ‹text›

   ::

      .. seealso::

         ‹reST definition list›


.. note:: This is a note.


.. warning:: This is a warning.


.. seealso::

   `Apples <http://en.wikipedia.org/wiki/Apple>`_
      A kind of `fruit <http://en.wikipedia.org/wiki/Fruit>`_.

.. index::
   include; selective
   pair: only; directive
   pair: ifconfig; directive
   pair: ifconfig; extension
   config value
   tag

.. _only:

Selective inclusion
-------------------

A block may be included depending of the presence of some tag
(:sphinx:`Sphinx ref <markup/misc.html#including-content-based-on-tags>`)::

   ..only:: <expression>

The expression is made of *tags* combined in boolean expressions
like ``html and draft``.

The format and the name of the current
builder is set as predefined tag, if needed it can be prefixed to differentiate
format and builer, like ``format_html`` or ``builder_html``


You can define tags via the -t command-line option of
:sphinx:`sphinx-build <invocation.html#build>`.

In the configuration file you can use
``tags.has('tag')``  to query,
``tags.add('tag')``  and ``tags.remove('tag')``  to change.

.. _ifconfig_extension:

An alternative is the ``ifconfig`` directive
(:sphinx:`Sphinx ref <ext/ifconfig.html>`)
from the ``sphinx.ext.ifconfig`` extension::

   .. ifconfig:: <Python expression>

To evaluate the expression all variables registered from ``conf.py``
are availables, to add a config value use the setup function in
``conf.py``::

   def setup(app):
    app.add_config_value('newconf', 'default', True)

the third parameter should always be ``True``.

.. _css_class:

Defining a css class for some part
==================================

.. index::
   pair: role; directive
   pair: container; directive
   pair: class; directive
   pair: rst-class; directive

There is at least three ways of doing it:

.. sidebar:: Rendered result


   .. role:: red

   An example of :red:`red text`.

   .. container:: red

      Here the full block  is red.

   An undecorated paragraph.

   .. rst-class:: red

   This paragraph too is is red.

   .. admonition:: Big warning
      :class: red

      Big warning text is red.


.. code-block:: rest

   .. role:: red

   An example of :red:`red text`.

   .. container:: red

      Here the full block is red.

   An undecorated paragraph.

   .. class:: red

   This paragraph too is is red.

   .. admonition:: Big warning
      :class: red

      Big warning text is red.

After applying `rst2html` you get:

.. code-block:: html

   <p>An example of <span class="red">red text</span>.</p>
   <div class="red container">
   Here the full block of test is red.</div>
   <p>An undecorated paragraph.</p>
   <p class="red">This paragraph too is is red.</p>
   <div class="red admonition">
   <p class="first admonition-title">Big warning</p>
   <p class="last">Big warning text is red.</p>



Here I have taken the `admonition` directive as example but any
directive that allow the `:class:` option would do.

As it generates a `span` the `role` directive is the only one that
allow to apply your style to a part of a paragraph.

The ``class`` works as expected with ``rest2html``,
but directive fail with **Sphinx**. You have to replace it with

.. code-block:: rest

   .. rst-class:: red

   This paragraph too is is red.


Sphinx use ``rst-class`` to replace the ReSt
:ref:`class <class_directive>` directive that is shadowed by Sphinx.
This is *only* stated in a small `footnote of Sphinx reSt
Primer <http://sphinx-doc.org/rest.html#id3>`_.

Using your new style
--------------------

To use your new class you need a css style like:

.. code-block:: css

   .red {
     color: red;
   }

You put it in a stylesheet, to give it's location:

-  With ``rst2html`` you must specify the stylesheet's location with
   a ``--stylesheet`` (for a URL) or ``--stylesheet-path`` for a
   local file.
-  With Sphinx a flexible solution is to add your own css file in the
   ``_static`` directory and give its location with a template that
   you put in the ``_template`` directory. You can use a file ``layout.html``
   wich extend the original template of the same name::

      {% extends "!layout.html" %}
      {% set css_files = css_files + ["_static/style.css"] %}

   For more details refer to :sphinx:`Sphinx: Templating <templating.html>`.

Sphinx Source Code
==================

.. contents::
   :local:

.. _code-block:
.. _code_highlighting:

Code highlighting
-----------------
.. index::
   pair: highlight; directive
   single: block; literal
   literal block

:sphinx:`Sphinx ref: showing code <http://sphinx-doc.org/markup/code.html>`

The code blocks are highlighted by sphinx, there is a default language
of ``Python`` that can be changed in the configuration, by setting the
configuration option ``highlight_language``.

The default **Highlighting language** used by `Pygment
<http://pygments.org>`_ in :ref:`Literal Blocks <literal_block>` is
set for following snippets of code examples by::

   .. highlight:: ‹language›
      :linenothreshold: ‹number›

The option language may be any
`language <http://pygments.org/languages/>`_
supported by a `Pygment lexer
<http://pygments.org/docs/lexers/>`_.

The additional ``linenothreshold`` option switches on line numbering
for blocks of size beyond ‹number› lines.

.. _code_block:

.. index::
   pair: code-block; directive

When using Sphinx you can specify the highlighting in a single literal
block::

   .. code-block:: ‹language›
      :linenos:

      ‹body›

The ``linenos`` option switches on line numbering.
You can also use some options that are described for the
:ref:`literalinclude directive`, namely ``linenos``, ``lineno-start``,
``caption``, ``name``, ``dedent``.

When using base ReST parser use instead :ref:`code keyword <rst-code>`.

.. index::
   pair: literalinclude; directive
   pair: source code; include

.. _literalinclude directive:
.. _source_code_include:

Source code include
-------------------

Source code is included in Sphinx with the :sphinx:`directive
literalinclude <markup/code.html#directive-literalinclude>`.

To include the source file ``example.py`` as a literal block use::

   .. literalinclude:: code/example.py
      :linenos:

.. literalinclude:: code/example.py
   :linenos:

There are more options::

  .. literalinclude:: code/example.py
     :caption: Example of code
     :name: example.py
     :language: python
     :dedent: 4
     :linenos:
     :lines: 1,3,5-10,20-
     :emphasize-line: 4,5

``caption`` is the displayed title before the block, ``name`` is the
:ref:`reST name option <name-option>` used as an
:ref:`internal reference <internal>` target.

``dedent`` strip left whitespaces, ``linenos`` add a line numbering
alternatively ``lineno-start`` begin the numbering at the given number.

The options ``language`` and ``linenos`` set the highlighting to
``‹language›`` and enables line numbers respectively.

You can select lines by the ``lines`` option or by
``start-after: <string>`` and/or ``end-before: <string>``
*(<string>s are not quoted)*.

Whe emphasize the fourth and fifth *selected* line, which in the above
example are the lines 5 and 10 of the source.



If it is a Python module, instead of selecting by lines you can select
a a class function or method to include by using the option
``pyobject``::

  .. literalinclude:: code/example.py
     :pyobject: MyClass.some_method

For including a ReST source file use the :ref:`rest directive include
<file_include>`.

.. index::
   pair: directive; source code
   pair: directive; module
   pair: python directive; currentmodule
   pair: python directive; exception
   pair: python directive; class
   pair: python directive; attribute
   pair: python directive; method
   pair: python directive; staticmethod
   pair: python directive; classmethod
   pair: python directive; decorator

.. _source-code-directives:

Source code directives
----------------------

There are very powerful directives in Sphinx
for documenting source code, each programming langage
has a :sphinx:`specific domains <domains.html>` .

The following markups are related to
:sphinx:`documenting python source code
<domains.html#the-python-domain>`.

+--------------------------------------+-----------------------------------------------------+
|``.. module:: name``                  |Marks the beginning of the description of a module   |
|                                      |                                                     |
+--------------------------------------+-----------------------------------------------------+
|``.. currentmodule:: name``           |The classes, functions etc. documented from here     |
|                                      |are in the given module                              |
|                                      |                                                     |
+--------------------------------------+-----------------------------------------------------+
| ``.. exception:: name[(signature)]`` |  Describes an exception class.                      |
+--------------------------------------+-----------------------------------------------------+
| ``.. class:: name[(signature)]``     |  Describes a class.  [#class]_                      |
+--------------------------------------+-----------------------------------------------------+
|  ``.. attribute:: name``             |  Describes an object data attribute.                |
+--------------------------------------+-----------------------------------------------------+
| ``.. method:: name(signature)``      |  Describes an object method.                        |
+--------------------------------------+-----------------------------------------------------+
| ``.. staticmethod:: name(signature)``|  Describes a static method.                         |
+--------------------------------------+-----------------------------------------------------+
| ``.. classmethod:: name(signature)`` |  Describes a class method.                          |
+--------------------------------------+-----------------------------------------------------+
| ``.. decorator:: name(signature)``   |  Describes a class method.                          |
+--------------------------------------+-----------------------------------------------------+
| ``.. classmethod:: name(signature)`` |  Describes a class method.                          |
+--------------------------------------+-----------------------------------------------------+

.. [#class] Methods and attributes belonging to the class should be placed in this directive’s body.
.. [#signature] Signatures of functions, methods, class constructors,
   decorators can be given like in Python, but with
   optional parameters indicated by brackets::

   .. function:: compile(source[, filename, symbol])

.. index::
   pair: autodoc; directive

autodoc
-------

There is  an :sphinx:`autodoc  <ext/autodoc.html>`
version of the :ref:`source code directives <source-code-directives>`
which include documentation from docstrings:

-  ``automodule``, ``autoclass``, ``autoexception``.
   Document a module, class or exception. They insert the docstring
   of the object itself; if you add a ``:members:`` option followed by
   a specific list of members, they will be included in the
   documentation.
   An empty list of members includes all members.

   ::

      .. autoclass:: Noodle
         :members: eat, slurp

- ``autofunction``, ``autodata``, ``automethod``, ``autoattribute``
   are used to document the respective type of object. ``autodata``
   and ``autoattribute`` support an annotation option taht will show
   not only the name but the representation of the object.

.. index::
   info fields
   docstring

.. _info-fields:

Using info field lists in Docstrings.
-------------------------------------
.. sidebar:: Code for example

   ::

      ..  function:: divide( i, j)

          divide two numbers

          :param i: numerator
          :type i: int
          :param j: denominator
          :type j: int
          :return: quotient
          :rtype: integer
          :raises: :exc:`ZeroDivisionError`

Inside Python object description directives the
:sphinx:`following fields <domains.html#info-field-lists>`
are recognized:
``param``,  ``arg``,  ``key``, ``type``, ``raises``, ``raise``,
``except``, ``exception``, ``var``, ``ivar``, ``cvar``, ``returns``,
``return``, ``rtype``.

..  function:: divide( i, j)
    :noindex:

    divide two numbers

    :param i: numerator
    :type i: int
    :param j: denominator
    :type i: int
    :return: quotient
    :rtype: integer
    :raises: :exc:`ZeroDivisionError`


.. literalinclude:: code/divide.py
   :language: python

.. automodule:: code.divide
   :noindex:
   :members:


Docstring alternate syntax.
---------------------------

For docstrings you can use the :ref:`previous fields <info-fields>`
or the alternate syntax that is `recommended by Openalea Project
<http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/sphinx_python_docstring.html>`_.
:

.. literalinclude:: code/docstring.py
   :language: python

.. automodule:: code.docstring
   :noindex:
   :members:

.. index::
   extension; napoleon
   coding style; google
   coding style; numpy

.. _napoleon_extension:

Google style docstrings.
------------------------
Using Restructured texts in your python code, is quite cumbersome, it
produces an easily readable documentation, but cryptic source code.


If we want to follow the style of `PEP257
<https://www.python.org/dev/peps/pep-0257/>`_ we  can use
the `Google Python style guide`_ also recommended by the
`Khan Academy Style Guide
<https://github.com/Khan/style-guides/blob/master/style/python.md>`_.

`NumPy style guide`_
Alternatively there is a `NumPy/SciPy style of documentation`_.

But they produces docstrings that are not recognized by Sphinx, and
not decorated in html output.

The extension :sphinx:`napoleon <ext/napoleon.html>` preprocess NumPy
and Google style docstrings and converts them to reStructuredText
before Sphinx parse the source code. You need to
`configure it in your conf.py file
<http://www.sphinx-doc.org/en/latest/ext/napoleon.html#configuration>`_.

.. literalinclude:: code/gstyle_docstring.py
   :language: python

.. automodule:: code.gstyle_docstring
   :noindex:
   :members:

Look :sphinx:`here for a larger example
<http://www.sphinx-doc.org/en/latest/ext/example_google.html>`.

How napoleon transform my docstrings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We may be curious to know what exactly napoleon generates. It can
allow us to fix error in the output by changing our docstring or
adding Sphinx fields.

We can call napoleon from python to learn what it generates:

.. code-block:: pycon

   >>> docstring="""
   ... Division of two reals.
   ...
   ..."""
   >>> from sphinx.ext.napoleon import Config
   >>> from sphinx.ext.napoleon.docstring import GoogleDocstring
   >>> config = Config(napoleon_use_param=True, napoleon_use_rtype=True)
   >>> print(GoogleDocstring(docstring), config)

And we have the decorated result:

.. literalinclude:: code/napoleon_output.rst
   :language: rest


If you want to experiment with output of Napoleon you can look at the
parameters of ``GoogleDocstring`` in the `source code
<https://github.com/sphinx-doc/sphinx/blob/master/sphinx/ext/napoleon/docstring.py>`_

.. include:: include/commonref.rst
