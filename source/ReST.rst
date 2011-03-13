:tocdepth: 3

===============================
:mod:`reST` -- reStructuredText
===============================

.. module:: reST
   :synopsis: Documentation of reStructuredText and Sphinx
.. moduleauthor:: Christoph Reller <reller@isi.ee.ethz.ch> and
                  Marc Zonzon <marc.zonzon@gmail.com>

.. highlight:: rest

A simple markup language for plain text files.

Structural elements
===================

Sectioning
----------
.. sidebar:: Emacs

   ====================== =========================================
   ``C-c C-a`` or ``C-=`` Adjust/rotate  or promote/demote the decorations
   ``C-- C-c C-a``        Move the title one level up.
   ``C-c C-h``            Display the title decoration hierarchy.
   ``C-c C-l``            shift region left
   ``C-c C-r``            shift region right
   ====================== =========================================

Titles are under- (and over-)lined (decorated) by ``=*-^"~`` as below.  The
exact order of the decoration is not important, the one below is the Python
convention. ::

  ####
  Part
  ####

  *******
  Chapter
  *******

  Section
  =======

  Subsection
  ----------

  Subsubsection
  ^^^^^^^^^^^^^

  Paragraph
  """""""""

Normal paragraphs are separated by a blank line.

Transitions
-----------
Any repetition of 4 or more punctuation characters with preceding and trailing
blank line is a transition, and looks like this:

----


Inline markup
=============

========================== ======================
``*emphasize*``            *emphasize*
``**emphasize strongly**`` **emphasize strongly**
````code````               ``code``
```don't know```           `don't know`
========================== ======================

.. sidebar:: Code for example

   ::

      Asterisk \*, back-quote \`
      and a **mark**\ up.

The following example illustrates special cases:

Asterisk \*, back-quote \`
and a **mark**\ up.

Lists
=====

Bullet list
-----------
.. sidebar:: Code for examples

   ::

      - First item with some lengthy
        text wrapping hopefully
        across several lines.
      - Second item

   ::

    .. hlist::
       :columns: 3

       * list of
       * short items
       * that should be
       * displayed
       * horizontally

   ::

      2. We start with point number 2
      #. Automatically numbered item.

      a) Point a
      b) Point b
      #) Automatic point c.

- First item with some lengthy
  text wrapping hopefully
  across several lines.
- Second item


Horizontal lists
----------------
    .. hlist::
       :columns: 3

       * list of
       * short items
       * that should be
       * displayed
       * horizontally

Enumerated list
---------------
2. We start with point number 2
#. Automatically numbered item.

a) Point a
b) Point b
#) Automatic point c.

.. note:: Automatic alphabetic numbering works wrongly in Sphinx, but does work
   with plain ``rst2html``.

Definition list
---------------
.. sidebar:: Code for example

   ::

      what
        Definition of "what". We add a few
        words to show the line wrapping.
      how
        Definition of "how".
      why : cause
        We define why we do it

        In many paragraphs

what
  Definition of "what". We add a few
  words to show the line wrapping.
how
  Definition of "how".
why : cause
  We define "why" we do it

  In many paragraphs.

.

Field list
----------
.. sidebar:: Code for examples

   ::

      :Name: Christoph Reller
      :Long: Here we insert more
         text to show the effect of
         many lines (in Pygments).
      :Remark:
        Start on the next line.

   ::

      -v           An option
      -o file      Same with value
      --delta      A long option
      --delta=len  Same with value

:Name: Christoph Reller
:Long: Here we insert more
   text to show the effect of
   many lines (in Pygments).
:Remark:
  Start on the next line.

Options list
------------
E.g. for listing command line options.

-v           An option
-o file      Same with value
--delta      A long option
--delta=len  Same with value

Blocks
======

Literal Blocks
--------------
.. sidebar:: Code for example

   ::

      Block one::

         **No** interpretation of
         |special| characters.

      Another block! ::

         In the text body,
            indentation is
         preserved

A block which is not interpreted at all is preceded by a ``::`` and a blank
line. The block must be intended.  If no white space is preceding the
``::`` then it is displayed as ":".

Block one::

   **No** interpretation of
   |special| characters.

Another block! ::

   In the text body,
      indentation is
   preserved

Line blocks
-----------
.. sidebar:: Code for example

   ::

      | Line block
      | New line and we are still on
        the same line
      |   Yet a new line

In a line block every line is preceded with ``|`` and at least one space.

| Line block
| New line and we are still on
  the same line
|   Yet a new line

Block quotes
------------
.. sidebar:: Code for example

   ::

      blah blah blah

        blah blah blah blah blah
        blah blah blah blah blah
        blah blah blah blah blah

      blah blah blah.

The different indentation levels of paragraphs are preserved.

blah blah blah

  blah blah blah blah blah
  blah blah blah blah blah
  blah blah blah blah blah

blah blah blah.


Tables
======

Simple tables
-------------
.. sidebar:: Code for the examples

   ::

      ==  ==
      aA  bB
      cC  dD
      ==  ==

      =====  ======
      Vokal  Umlaut
      =====  ======
      aA     äÄ
      oO     öÖ
      =====  ======

      =====  =====  ======
      Inputs        Output
      ------------  ------
        A      B    A or B
      =====  =====  ======
      False         False
      ------------  ------
      True   False  True
      False  True   True
      True          True
      ============  ======

      ===========  ================
      1. Hallo     | blah blah blah
                     blah blah blah
                     blah
                   | blah blah
      2. Here      We can wrap the
                   text in source
      32. There    **aha**
      ===========  ================

Tables are preceded and ended with a sequence of "``=``" to indicate the
columns, e.g:

==  ==
aA  bB
cC  dD
==  ==

Headers are indicated by another sequence of "``=``", e.g:

=====  ======
Vokal  Umlaut
=====  ======
aA     äÄ
oO     öÖ
=====  ======

Column spans are followed by a sequence of "``-``" (except for the last header
or last row of the table where we must have "``=``"), e.g:

=====  =====  ======
Inputs        Output
------------  ------
  A      B    A or B
=====  =====  ======
False         False
------------  ------
True   False  True
False  True   True
True          True
============  ======

Table cells are treated like a small document on their own up to line breaks,
e.g:

===========  ================
1. Hallo     | blah blah blah
               blah blah blah
               blah
             | blah blah
2. Here      We can wrap the
             text in source
32. There    **aha**
===========  ================

Grid tables
-----------
.. sidebar:: Code for example

   ::

      +--------+--------+-----------+
      | Header | Header with 2 cols |
      +========+========+===========+
      | A      | Lists: | **C**     |
      +--------+  - aha +-----------+
      | B::    |  - yes | | a block |
      |        |        |   of text |
      |  *hey* |  #. hi | | a break |
      +--------+--------+-----------+

`Grid tables <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#grid-tables>`_
have a more difficult syntax but can express more complex tables.

+--------+--------+-----------+
| Header | Header with 2 cols |
+========+========+===========+
| A      | Lists: | **C**     |
+--------+  - aha +-----------+
| B::    |  - yes | | a block |
|        |        |   of text |
|  *hey* |  #. hi | | a break |
+--------+--------+-----------+

You can edit them under emacs with ``table.el``
(but be carefull about conflicts with ``rst-mode``) or
use *org tables* with ``orgtbl-mode`` and export to table with
``org-table-convert`` or ``org-table-create-with-table.el`` ( bound
to :kbd:`C-c ~` in ``org-mode``, but not in ``orgtbl-mode``)

Explicit Markup
===============
They all begin with two periods and a white space.

Footnotes
---------
.. sidebar:: Code

   ::

      In the text [2]_.

      .. [2] In the footnote.

      First automatic [#]_.
      Another automatic [#]_.

      .. [#] The first automatic.
      .. [#] The other automatic.

      A labeled automatic [#one]_.
      Another of these [#two]_.

      .. [#one] footnote.
      .. [#two] labeled footnotes.

      An autosymbol [*]_.
      More autosymbol [*]_.

      .. rubric:: Footnotes

      .. [*] Footnotes can be put in a *Footnotes*
         ``rubric`` at end of document.
      .. [*] other labeled footnote.

``.. [2]`` precedes the definition of the footnote 2.  It is referenced by
``[2]_``. E.g.

In the text [2]_.

.. [2] In the footnote.

First automatic [#]_.
Another automatic [#]_.

.. [#] The first automatic.
.. [#] The other automatic.

A labeled automatic [#one]_.
Another of these [#two]_.

.. [#one] footnote.
.. [#two] labeled footnotes.

An autosymbol [*]_.
More autosymbol [*]_.

.. rubric:: Footnotes

.. [*] Footnotes can be put in a *Footnotes*
   ``rubric`` at end of document.
.. [*] other labeled footnote.


*There is no labeled version of these autosymbol footnotes.*

Citations
---------
.. sidebar:: Code for example

   ::

      We cite [REL09]_ or REL09_
      or even rel09_.

      .. [REL09] Citation

``.. [REL2009]`` is followed by the definition of the citation ``REL2009``.  It
is referenced as ``[REL2009]_`` or ``REL2009_``.  Citation labels can contain
underlines, hyphens and fullstops.  Case is not significant.  In Sphinx,
definition and reference can reside in different files.

We cite [REL09]_ or REL09_
or even rel09_.

.. [REL09] Citation

Hypertext links
---------------

External
^^^^^^^^
There exist two version for doing this.  Either in a citation style or in an
inline style.

.. sidebar:: Code for examples

   ::

      A link_ in citation style.

      .. _link: http://www.google.ch

      In-line versions are
      `link <http://www.google.ch>`_
      or `<http://www.google.ch>`_
      or (in Sphinx) http://www.google.ch.


**Citation style**:

A link_ in citation style.

.. _link: http://www.google.ch

In printed documents the link will be listed similar as a citation, as opposed
to HTML documents.

**In-line style**:

In-line versions are `link <http://www.google.ch>`_ or
`<http://www.google.ch>`_ or (in Sphinx) http://www.google.ch.

.. _internal:

Internal
^^^^^^^^
To define a label for any text location, precede it with::

   .. _‹label›:

plus a blank line.  There are two ways of referencing a label.

The reST way is::

    `‹label›`_

The *preferred* Sphinx way, allows linking across files, it  use::

   :ref:`‹displayed text› <‹label›>`

To reference ``‹label›`` defined in *any* document of the project

   :ref:`‹displayed text› <‹label›>`

If the ``‹label›`` definition is followed by a section title then ``‹displayed
text›`` can be omitted and will be replaced by the title.

E.g. this section is preceded with ``.. _internal:``, so we have:

================================== ==============================
``:ref:`internal```                :ref:`internal`
``:ref:`This section <internal>``` :ref:`This section <internal>`
================================== ==============================


In Sphinx it is possible to reference a document as follows

===============  ==============
``:doc:`ReST```  :doc:`ReST`
===============  ==============



Section titles, footnotes, and citations automatically are link targets.
```Project`_`` produces `Project`_.

.. ```Internal`_`` produces `Internal`_.

To reference  a Python Enhancement Proposal use ``:pep``, for a
Request for Comments ``:rfc:``

.. note::  The reference for *Rest way of hyperlinking*  is
   `in ReST Specification <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#hyperlink-targets>`_
   and
   `in Quick ReST <http://docutils.sourceforge.net/docs/ref/rst/quick.html>`_

   For the *Sphinx way of hyperlinking*  see
   `Sphinx: Cross-referencing syntax <http://sphinx.pocoo.org/latest/markup/inline.html#cross-referencing-syntax>`_

Directives
==========

`Directives <http://docutils.sourceforge.net/docs/ref/rst/directives.html>`_
are a general-purpose extension mechanism.  The general syntax is
similar to `Explicit Markup`_::

   .. ‹name›:: ‹argument 1›
               ‹argument 2›
      :‹option 1›: ‹value›

      ‹body›

reST directives
---------------

.. contents::
   :local:

table of contents
^^^^^^^^^^^^^^^^^

.. _reST-tableOfContents:

Create a `table of contents
<http://docutils.sourceforge.net/docs/ref/rst/directives.html#table-of-contents>`_
containing (sub)titles ranging from level 1 to
level ‹number› if you use the ``:local:`` option the TOC is local to
the section where it appears, otherwise it is for the whole file, the title may be empty::

   .. contents:: `Table of contents`
      :depth: ‹number›
      :local:



images and figures
^^^^^^^^^^^^^^^^^^

.. sidebar:: Code for examples

   ::

    .. image:: _static/sphinx.png
       :width: 250
       :alt: sphinx logo
    .. figure:: _static/sphinx.png
       :width: 250
       :alt: sphinx logo

       The logo for Sphinx

**Include an image** (see also in the `Sphinx documentation
<http://sphinx.pocoo.org/rest.html#images>`_ and
`ReST reference
<http://docutils.sourceforge.net/docs/ref/rst/directives.html##images>`_)

.. image:: _static/sphinx.png
   :width: 250
   :alt: sphinx logo

**Include a figure**

.. figure:: _static/sphinx.png
   :width: 250
   :alt: sphinx logo

   The logo for Sphinx

replacement,  include
^^^^^^^^^^^^^^^^^^^^^

General replacements::

   .. |‹something›| ‹directive›:: here we define what ‹something› is

   here |‹something›| will be replaced by its definition.

Possible ``‹directive›``\ s are ``replace`` or ``image``.

----

+----------------------------+------------------------------------------------------+
|**Including** a reST file   | .. note::  Don't use the same file name              |
|::                          |            extension as your source files.           |
|                            |            Otherwise Sphinx will mistake this        |
|   .. include:: ‹file name> |            file as one of your regular source file.  |
+----------------------------+------------------------------------------------------+

Sphinx directives
-----------------

.. contents::
   :depth: 1
   :local:


table of contents
^^^^^^^^^^^^^^^^^
::

   .. toctree::
      :maxdepth: ‹depth›
      :glob:

      ‹file 1 without file name extension›
      ‹file 2 without file name extension›

Create a table of contents across files

A ``glob`` option enables to use wildcards in the filenames, e.g. ``/comp/*``
means all files under the directory ``comp``.

The depth can be further restricted per file by inserting the
following `Field list`_ type element in the very first line of the file::

   :tocdepth: ‹depth›


.. Note::  Don't try to reference the file which contains the ``toctree``
   directive, otherwise a recursive loop occurs. Use the normal
   :ref:`reST table of contents <reST-tableOfContents>` directive instead.

Index and glossaries
^^^^^^^^^^^^^^^^^^^^
.. index::
       single: index (Rest)

Entries in the **index** are created automatically from all information units
(like functions, classes or attributes).  Explicit manual entries are made as::

   .. index:: ‹keyword 1›, ‹keyword 2›, ...

   .. index::
      single: ‹keyword›; ‹sub-keyword›

   .. index::
      pair: ‹keyword 1st part›; ‹keyword 2nd part›

The first two versions create single (sub-)entries, while the last version
creates two entries "‹keyword 1st part›; ‹keyword 2nd part›" and "‹keyword 2nd
part›; ‹keyword 1st part›".

A **glossary** is a ‹reST definition list›::

   .. glossary::

      name
         definition


sidebar, and topic
^^^^^^^^^^^^^^^^^^

A **sidebar** or a **topic** with ‹Title› and ‹body› are treated like documents on
their own::

   .. sidebar:: ‹Title›

      ‹body›


   .. topic:: Topic Title

       Subsequent indented lines comprise
       the body of the topic, and are
       interpreted as *body elements*.


.. topic:: Topic Title

    Subsequent indented lines comprise
    the body of the topic, and are
    interpreted as *body elements*.

note, warning, seealso
^^^^^^^^^^^^^^^^^^^^^^^

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


rubric, centered
^^^^^^^^^^^^^^^^

A rubric is a title not appearing in the table of contents::

   .. rubric:: ‹Title›


A centered, boldface text block::

   .. centered:: ‹text block›

.. centered:: This text is
      *centered, boldface*



Sphinx code highlighting
-----------------------------

**Highlighting language** used by  `Pygment <http://pygments.org>`_ in
`Literal Blocks`_  is set for following text by::

   .. highlight:: ‹language›
      :linenothreshold: ‹number›


The additional ``linenothreshold`` option switches on line numbering for blocks
of size beyond ‹number› lines.

Specify the highlighting for a single literal block::

   .. code-block:: ‹language›
      :linenos:

      ‹body›

The ``linenos`` option switches on line numbering.

----

**Including a file** as a literal block::

   .. literalinclude:: ‹filename›
      :language: ‹language›
      :linenos:
      :lines: 1,3,5-10,20-

The options ``language`` and ``linenos`` set the highlighting to ``‹language›``
and enables line numbers respectively.

You can select lines by the ``:lines:`` option or by
``start-after:<string>`` and/or ``end-before:<string>``


If it is a Python module, you can select a class, function or method to
include using the pyobject option::

    .. literalinclude:: example.py
       :pyobject: MyClass.some_method

Sphinx source code directives
-----------------------------

There are very powerful directives in Sphinx
for `documenting source code
<http://sphinx.pocoo.org/markup/desc.html#module-specific-markup>`_
most are since *version 1.0* in `specific domains
<http://sphinx.pocoo.org/domains.html>`_ the following are related to
`documenting python source code
<http://sphinx.pocoo.org/domains.html#the-python-domain>

+--------------------------------------+-----------------------------------------------------+
|``.. module:: name``                  |Marks the beginning of the description of a module   |
|                                      |                                                     |
+--------------------------------------+-----------------------------------------------------+
|``.. currentmodule:: name``           |Tells Sphinx that the classes, functions             |
|                                      |etc. documented from here are in the given module    |
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

.. [#class] Methods and attributes belonging to the class should be placed in this directive’s body.
.. [#signature] Signatures of functions, methods and class constructors can be given like in Python, but with  optional parameters indicated by brackets::

   .. function:: compile(source[, filename, symbol])

Info field lists
^^^^^^^^^^^^^^^^
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

Inside Python object description directives the following fields are recognized:
``param``,  ``arg``,  ``key``, ``type``, ``raises``, ``raise``, ``except``, ``exception``, ``var``, ``ivar``, ``cvar``, ``returns``, ``return``, ``rtype``

..  function:: divide( i, j)

    divide two numbers

    :param i: numerator
    :type i: int
    :param j: denominator
    :type i: int
    :return: quotient
    :rtype: integer
    :raises: :exc:`ZeroDivisionError`

autodoc
^^^^^^^

There is also an `autodoc <http://sphinx.pocoo.org/latest/ext/autodoc.html>`_
version of the source code directives which include documentation from docstrings:

- ``automodule``, ``autoclass``, ``autoexception``.
   They  accept an option ``:member:`` to include
   a specific list of members, or all members when the ``:member:`` option is empty.

   ::

      .. autoclass:: Noodle
         :members: eat, slurp

- ``autofunction``, ``autodata``, ``automethod``, ``autoattribute``


Sphinx Roles
------------

they are described in `Sphinx: Inline markup
<http://localhost/doc/python-sphinx/html/markup/inline.html>`_
or in new *(> 1.0)* documentation
`Sphynx domains - python roles
<http://sphinx.pocoo.org/latest/domains.html#python-roles>`_

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


python
------

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
| ``:py:meth:``  | method [#dotted]_ [#role]_               |
+----------------+------------------------------------------+
| ``:py:attr:``  | data attribute of an object              |
+----------------+------------------------------------------+
| ``:py:exc:``   | exception [#dotted]_                     |
+----------------+------------------------------------------+


.. [#dotted] Class, methods, exceptions may be dotted names.
.. [#role] The role text should include the type name and the method name


You may supply an explicit title and reference target: ``:role:`title <target>```

Comments
--------

.. sidebar:: Code for example

   ::

      .. Comment
         Even more comment

      Not comment anymore

Everything starting like a directive with two periods and a space but is
followed by normal text is a comment.  Mark the indentation in the example:

.. Comment
   Even more comment

Not comment anymore


`Sphinx <http://sphinx.pocoo.org/>`_
====================================

Project
-------

To start a Sphinx project use the interactive ``sphinx-quickstart`` command.
This will ask you all the necessary questions.You can choose to build with a
Makefile.

Customization is done in the file ``conf.py`` and the Makefile.

Math
----

There is a `mathematical typesetting Sphinx extension
<file:///usr/share/doc/python-sphinx/html/ext/math.html?highlight=options#module-sphinx.ext.mathbase>`_
called ``sphinx.ext.pngmath`` based on LaTeX.

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

.. sidebar:: Code for example

   ::

      .. math:: \[a = b\]
         :nowrap:

   or equivalently::

      .. math::
         :nowrap:

         \[a = b\]


**Explicit LaTeX with amsmath mechanism**

If the option ``nowrap`` is specified then the full LaTeX code (including the
math-environment) has to be given.  We can assume that the ``amsmath`` package
is loaded.  This is not limited to math typesetting, any LaTeX construct can be
rendered in this way.

.. math:: \[a = b\]
   :nowrap:

or equivalenty

.. math::
   :nowrap:

   \[a = b\]


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

Graphs with `Graphviz <http://graphviz.org/>`_
----------------------------------------------

There is a `graph drawing Sphinx extension
<http://sphinx.pocoo.org/ext/graphviz.html>`_ based on `Graphviz
<http://graphviz.org/>`_.

To enable the extension we have to add it to the ``extensions`` list in
``conf.py``::

  extensions = ['sphinx.est.graphviz']

On Ubuntu Linux the packages ``graphviz`` and ``libgraphviz4`` have to me
installed.  There is no need to install ``python-graphviz``.

Examples
^^^^^^^^

.. sidebar:: Undirected graph

   ::

      .. graph:: foo

         "bar" -- "baz";

.. graph:: foo

   "bar" -- "baz";

.. sidebar:: Directed graph

   ::

      .. digraph:: foo

         "bar" -> "baz";

.. digraph:: foo

   "bar" -> "baz";

References
==========

- This doc is slurped from `Cristoph Reller Memo
  <http://people.ee.ethz.ch/~creller/web/tricks/reST.html>`_
  and slightly changed according to my needs.

- `Sphinx documentation <http://sphinx.pocoo.org/latest/contents.html>`_
  - `reStructuredText Primer <http://sphinx.pocoo.org/latest/rest.html>`_

- `Documenting Your Project Using
  Sphinx <http://packages.python.org/an_example_pypi_project/sphinx.html>`_
  from `an example pypi project’s <http://packages.python.org/an_example_pypi_project/>`_


- The `ReStructuredText Documentation <http://docutils.sourceforge.net/docs/>`_

  - `A ReStructuredText Primer
    <http://docutils.sourceforge.net/docs/user/rst/quickstart.html>`_
    you may prefer the python the *Sphinx* nicely formated
    documentation cited above, also available _with a distinct layout_ as
    `reStructuredText Primer <http://docs.python.org/dev/documenting/rest.html>`_
  - `Quick reStructuredText
    <http://docutils.sourceforge.net/docs/ref/rst/quick.html>`_
  - `reStructuredText Markup Specification
    <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>`_
  - `Interpreted Text Roles <http://docutils.sourceforge.net/docs/ref/rst/roles.html>`_
- `Emacs Support for reStructuredText
  <http://docutils.sourceforge.net/docs/user/emacs.html>`_

- `Epydoc reST markup <http://epydoc.sourceforge.net/manual-othermarkup.html>`_

- `Documenting Python <http://docs.python.org/dev/documenting/index.html>`_

- `Pylons Book:  Documentation <http://pylonsbook.com/en/1.1/documentation.html>`_ is itself a good example of sphinx documentation.

- Projects using Sphinx

  - `Official list of projects using Sphinx <http://sphinx.pocoo.org/examples.html>`_

  - `OpenAlea <http://openalea.gforge.inria.fr/wiki/doku.php?id=documentation:doctests:how_to_document_python_api>`_

    - `template.py <https://gforge.inria.fr/scm/viewvc.php/trunk/doc/source/sphinx/template.py?view=markup&root=openalea>`_

- Extending sphinx

  - `Sphinx Tutorial: Writing a simple extension <http://sphinx.pocoo.org/ext/tutorial.html>`_
  - `Defining Custom Roles in Sphinx <http://www.doughellmann.com/articles/how-tos/sphinx-custom-roles/index.html>`_ a
    `Sphinx post by Doug Hellmann <http://blog.doughellmann.com/search/label/sphinx>`_
  - `Creating Interpreted Text Roles <http://docutils.sourceforge.net/docs/ref/rst/rst-roles.html>`_ from docutils .project
  - `Creating reStructuredText Directives <http://docutils.sourceforge.net/docs/ref/rst/rst-directives.html>`_ from docutils project.
