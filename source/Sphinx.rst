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

Sphinx Roles
============

.. contents::
   :local:

.. _sphinx_roles:

Sphinx inline markup is down through interpreted text roles;
they are written ``:rolename:`content`.``.

There are four types of roles:

-  The :ref:`ReStructuredText Text Roles <rest_roles>`, which are valid both for
   ReStructuredText and Sphinx.
-  The :ref:`Sphinx cross references Roles<sphinx_cross_references>`
   which extend and are preferred to
   :ref:`ReStructuredText cross references<cross_reference>`
-  The :sphrst:`markup roles<other-semantic-markup>`
-  The roles added by :sphinx:`Sphinx domains <usage/domains.html>` like
   the :ref:`Python roles <python_roles>` referenced below.

.. _sphinx_ref:
.. _sphinx_cross_references:

.. index::
   pair: sphinx; cross-reference

Location cross references
-------------------------
sphinx ref: :sphrst:`Cross-referencing arbitrary locations
<roles.html#cross-referencing-arbitrary-locations>` which defines
the sphinx role :sphrst:`ref <roles.html#role-ref>`.

We use::

   :ref:`displayed text <label>`

To reference ``label`` defined in *any* document of the project.
It allows linking across files, while the :ref:`rest way <rest_ref>`
is limited to a location in the same file.

If the ``label`` definition is followed by a section title then
``displayed text`` can be omitted and will be replaced by the section
title.

E.g. the :doc:`ReST` *Explicit hyperlink target* section is preceded
with ``.. _explicit_target:``, so we have:

========================================= =====================================
``:ref:`explicit_target```                :ref:`explicit_target`
``:ref:`That section <explicit_target>``` :ref:`That section <explicit_target>`
========================================= =====================================

We can also use as reference target a :ref:`name option <name-option>` like

=================================== ===============================
``:ref:`see this topic <mytopic>``` :ref:`see this topic <mytopic>`
=================================== ===============================

See also :ref:`sphinx vs rest references` in the :doc:`ReST <ReST>` chapter.


.. index::
   sphinx; autosectionlabel
   autosectionlabel; sphinx extension
   extension;  autosectionlabel

.. _autosectionlabel:

Automatic labels for sections
-----------------------------
Sphinx as an extension :sphinx:`autosectionlabel
<usage/extensions/autosectionlabel.html>` that allow to reference
each section by its title. Its is similar to
:ref:`implicit hyperlink`, but works across document.

In the :doc:`ReST chapter <ReST>` we have used an :ref:`implicit hyperlink`
with:

.. code-block:: ReST

    `Transition`_
    `how to draw an horizontal line <Transition>`_

we cannot use in the present chapter this ReST way of referencing a target
because ReST processor know only one document. but we can use it with the
:sphinx:`autosectionlabel extension <usage/extensions/autosectionlabel.html>`
with

.. list-table::

   * - .. code-block:: ReST

          | The section :ref:`Transition` show
          | :ref:`how to draw an horizontal line <Transition>`
          | in your document.

     - | The section :ref:`Rest:Transition` show
       | :ref:`how to draw an horizontal line <Rest:Transition>`
       | in your document.

Once you use the :sphinx:`autosectionlabel extension
<usage/extensions/autosectionlabel.html>`
Sphinx will detect duplicate labels, in contrast with :ref:`implicit hyperlink`
*autolabel* define a new label for each section, so if you have manually put a label
before a section title which is identical to the title, it will be detected as
*duplicate*.

These duplicate are harmless since they reference the same point. But some title in many
document can be identical, you can have many *introduction* or *conclusion* in different
parts. The duplicate may be problematic as any one can be matched by a reference. To
disembiguate the labels there is an configuration option *beginning version 1.6*
``autosectionlabel_prefix_document`` which prefix the automatic labels with with the
name of the document it is in, followed by a colon.

With this setting instead of ``:ref:`Transition``` you have to use
``:ref:`ReST:Transition``` it avoid a potential ambiguity with a *Transition* paragraph
in an other document, and has the additional benefit to avoid also all ambiguities with
explicit labels in your documents.


.. index::
   pair:  sphinx; document cross-reference
   pair:  sphinx; cross-reference document

Cross-referencing documents.
----------------------------
:sphrst:`sphinx ref: Cross-referencing documents
<roles.html#cross-referencing-documents>`

In Sphinx it is possible to reference a document as follows

===============  ==============
``:doc:`ReST```  :doc:`ReST`
===============  ==============

.. index::
   pair: role; cross-reference

Extra cross-reference roles
---------------------------
Several  are described in the
:sphrst:`sphinx ref: Cross-referencing other items of interest
<roles.html#cross-referencing-other-items-of-interest>`.

To reference  a Python Enhancement Proposal use ``:pep:``, for a
Request for Comments ``:rfc:``

.. index::
   pair: extension; intersphinx
   pair: extension; extlinks
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
   have many links pointing to the same site. You use a configuration like::

      extlinks = {'sphinx': ('http://www.sphinx-doc.org/en/master/%s', 'Sphinx: %s')}

   Here `extlinks` is a dictionary, the second item of the tuple is the default
   caption, it must contain exactly one `%s` which will be replaced by the
   value substituted in the link. The second element can also be `None`, in
   this case the full url is used.

   with this setting when you  write::

      See also :sphinx:`Using Sphinx <using.html>` or :sphinx:`faq.html`.

   you get


   See also :sphinx:`Using Sphinx <using.html>` or :sphinx:`faq.html`.

.. index
   pair: sphinx; role

.. _markup_roles:


Markup Roles.
-------------

Ref: :sphrst:`Semantic markup roles<other-semantic-markup>`.

They don't generate a cross reference but only format the text in a different style.

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

Python Roles.
-------------

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

Sphinx includes its own :sphrst:`directives <directives.html>`, which
are not available in the docutils builders.

.. We reference here

   :ref:`sphinx_math`, :ref:`toctree`, :ref:`index`, :ref:`glossary`,
   :ref:`note`, :ref:`warning`, :ref:`seealso`,
   :ref:`only`,  :ref:`role`, :ref:`only`, :ref:`ifconfig`

.. contents::
   :local:

.. index::
   pair: toctree; directive
   see toc; table of contents
   see toc; toctree

.. _math:

Sphinx Math.
------------

The math directive is yet present in docutils ReST, but the rendering in
Sphinx, which is done through extensions, extend the original docutils math
extension. We give here some examples of its use.

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

Multiline Math
^^^^^^^^^^^^^^

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
math-environment) has to be given.  We can assume that the :index:`amsmath`
package is loaded.  This is not limited to math typesetting, any LaTeX
construct can be rendered in this way.

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
^^^^^^^^^^^^^^^^

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

.. _toctree:

Table of contents.
------------------
::

   .. toctree::
      :maxdepth: ‹depth›
      :glob:

      ‹file 1 without file name extension›
      ‹file 2 without file name extension›

The :sphrst:`toctree directive <directives.html#directive-toctree>` create a
table of contents across files.

A ``glob`` option enables to use wildcards in the filenames, e.g. ``/comp/*``
means all files under the directory ``comp``.

Relative names are relative to the document the directive occurs in,
absolute names are relative to the source directory.

The depth can be further restricted per file by inserting the
following :ref:`Field list` type element in the very first line of the file::

   :tocdepth: ‹depth›

See :sphrst:`toctree directive <directives.html#directive-toctree>` for other
options.

To get a table of content *inside* a file, use the :ref:`reST table of contents
<reST-tableOfContents>`

.. index::
   pair: index; directive
   index; single
   index; pair
   index; triple
   index; see
   index; seealso

.. _index:

Index.
------

Entries in the Index
are created automatically from all information units
like  modules, classes, functions or attributes but those with a ``:noindex:``
option.

Explicit manual entries use the
:sphrst:`index directive<directives.html#directive-index>`::

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

Glossary.
---------

A :sphrst:`glossary <basics.html#directive-glossary>`
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

Note, Warning, Seealso.
-----------------------

They are :sphrst:`paragraph-level markups <directives.html#paragraph-level-markup>`.

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

Selective inclusion.
--------------------

A block may be included depending of the presence of some tag
(:sphrst:`Sphinx ref <directives.html#including-content-based-on-tags>`)::

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
from the :sphinx:`ifconfig extension<usage/extensions/ifconfig.html>`::

   .. ifconfig:: <Python expression>

To evaluate the expression all variables registered from ``conf.py``
are availables, to add a config value use the setup function in
``conf.py``::

   def setup(app):
    app.add_config_value('newconf', 'default', True)

the third parameter should always be ``True``.

.. _css_class:

Defining a css class for some part.
===================================

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



Here I have taken the `admonition` directive as example but any directive that
allow the `:class:` option would do.

As it generates a `span` the `role` directive is the only one that allow to
apply your style to a part of a paragraph.

The ``class`` works as expected with ``rest2html``, but directive fail with
**Sphinx**. You have to replace it with

.. code-block:: rest

   .. rst-class:: red

   This paragraph too is is red.


Sphinx use ``rst-class`` to replace the ReSt :ref:`class <class_directive>`
directive that is shadowed by Sphinx.  This is *only* stated in a small
:sphrst:`footnote of Sphinx reSt Primer <basics.html#id2>`.

Using your new style
--------------------

To use your new class you need a css style like:

.. code-block:: css

   .red {
     color: red;
   }

You put it in a stylesheet, to give it's location:

- With ``rst2html`` you must specify the stylesheet's location with a
   ``--stylesheet`` (for a URL) or ``--stylesheet-path`` for a local file.

-  With Sphinx a flexible solution is to add your own css file in the
   ``_static`` directory and give its location with a template that
   you put in the ``_template`` directory. You can use a file ``layout.html``
   wich extend the original template of the same name::

      {% extends "!layout.html" %}
      {% set css_files = css_files + ["_static/style.css"] %}

   For more details refer to :sphinx:`Sphinx: Templating <templating.html>`.

Sphinx Source Code.
===================

.. contents::
   :local:

.. _code-block:
.. _code_highlighting:

Code highlighting.
------------------
.. index::
   pair: highlight; directive
   single: block; literal
   literal block

:sphrst:`Ref: showing code Examples<irectives.html#showing-code-examples>`

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
supported by a `Pygment lexer <http://pygments.org/docs/lexers/>`_.

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

Source code include.
--------------------

Source code is included in Sphinx with the
:sphrst:`directive literalinclude <directives.html#directive-literalinclude>`.

To include the source file ``example.py`` as a literal block use::

   .. literalinclude:: ../arithmetic/example.py
      :linenos:

.. literalinclude:: ../arithmetic/example.py
   :linenos:

There are more options::

  .. literalinclude:: ../arithmetic/example.py
     :caption: Example of code
     :name: example.py
     :language: python
     :dedent: 4
     :linenos:
     :lines: 1,3,5-10,20-
     :emphasize-line: 4,5

``caption`` is the displayed title before the block, ``name`` is the
:ref:`reST name option <name-option>` used as an
:ref:`internal reference <explicit_target>` target.

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

  .. literalinclude:: ../arithmetic/example.py
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

.. _source_code_directives:

Source code directives.
-----------------------

There are very powerful directives in Sphinx for documenting source code, each
programming langage has a :sphinx:`specific domains <usage/domains/>` .

The following markups are related to
:sphinx:`documenting python source code <usage/domains/python.html>`.

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

There is  an :sphinx:`autodoc  <usage/extensions/autodoc.html>`
version of the :ref:`source code directives <source_code_directives>`
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

- ``autofunction``, ``autodata``, ``automethod``, ``autoattribute`` are used to
   document the respective type of object. ``autodata`` and ``autoattribute``
   support an annotation option taht will show not only the name but the
   representation of the object.

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
:sphinx:`following fields <usage/domains/python.html#info-field-lists>`
are recognized::
``param``,  ``arg``,  ``key``, ``type``, ``raises``, ``raise``,
``except``, ``exception``, ``var``, ``ivar``, ``cvar``, ``returns``,
``return``, ``rtype``, ``meta``.

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


.. literalinclude:: ../arithmetic/divide.py
   :language: python

.. automodule:: arithmetic.divide
   :noindex:
   :members:

.. index::
   extension; napoleon
   coding style; numpy

.. _napoleon_extension:

Numpy alternate syntax for docstrings.
--------------------------------------

The :ref:`previous fields <info-fields>` have a very good rendering in Sphinx, but
they are quite cumbersome for the programmer and make the code cryptic. Two alternates
syntaxes are popular the Numpy docstring syntax and the Google docstring syntax.

These two styles are not recognized directly by the ``autocode`` extension but should
preprocessed.

The extension :sphinx:`napoleon <usage/extensions/napoleon.html>` preprocess NumPy and
Google style docstrings and converts them to reStructuredText before Sphinx parse the
source code. You need to :sphinx:`configure it in your conf.py file
<usage/extensions/napoleon.html#configuration>`.

We gives an example of `NumPy/SciPy style of documentation`_.

.. literalinclude:: ../arithmetic/docstring.py
   :language: python


.. automodule:: arithmetic.docstring
   :noindex:
   :members:

.. index::
   coding style; google

`NumPy style guide`_ includes many small examples,
the :sphinx:`Sphinx Manual <>` includes  :sphinx:`a larger Numpy style example
<usage/extensions/example_google.html>`, and `Material for Sphinx
<https://bashtage.github.io/sphinx-material/>`_ has a big `Polynomial Class (source)
<https://bashtage.github.io/sphinx-material/_modules/numpy/polynomial/polynomial.html>`_
and `generated result
<https://bashtage.github.io/sphinx-material/generated/numpy.polynomial.Polynomial.html>`_.


Google style docstrings.
------------------------
If we want to follow the style of `PEP257
<https://www.python.org/dev/peps/pep-0257/>`_ we  can use
the `Google Python style guide`_ also recommended by the
`Khan Academy Style Guide
<https://github.com/Khan/style-guides/blob/master/style/python.md>`_.


.. literalinclude:: ../arithmetic/gstyle_docstring.py
   :language: python

.. automodule:: arithmetic.gstyle_docstring
   :noindex:
   :members:

The `Sphinx Manual <>` includes  :sphinx:`a larger Google style example
<usage/extensions/example_google.html>`.

How *napoleon* transform my docstrings.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We may be curious to know what exactly napoleon generates. It can
allow us to fix error in the output by changing our docstring or
adding Sphinx fields.

We can call *napoleon* from python to learn what it generates:

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

.. literalinclude:: ../arithmetic/napoleon_output.rst
   :language: rest


If you want to experiment with output of *napoleon* you can look at
the parameters of ``GoogleDocstring`` in the `Napoleon source code
<https://github.com/sphinx-doc/sphinx/blob/master/sphinx/ext/napoleon/docstring.py>`_

.. include:: include/commonref.rst
