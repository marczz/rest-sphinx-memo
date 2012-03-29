:tocdepth: 3

===============================
:mod:`reST` -- reStructuredText
===============================

.. module:: reST
   :synopsis: Documentation of reStructuredText and Sphinx
.. moduleauthor:: Marc Zonzon <marc.zonzon@gmail.com>

.. highlight:: rest

A simple markup language for plain text files.

Structural elements
===================

.. index::
   single: emacs; mode

Sectioning
----------
.. sidebar:: Emacs

   =======================  ==========================================
   ``C-c C-=``              Adjust/rotate  or promote/demote the decorations
   ``C-- C-c C-=``          reverse Adjust
   ``C-c C-a C-d``          Display the title decoration hierarchy.
   ``C-- C-c C-r <tab>``    shift region left
   ``C-c C-r <tab>``        shift region right
   =======================  ==========================================

.. index::
   !title
   single: title; hierarchy

Titles are under- (and over-)lined (decorated) by ``=*-^"~`:.'#`` as below.  The
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

.. index::
   emphasize
   strong
   code
   inline markup
   inline markup; strong
   inline markup; emphasize
   inline markup; code

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

.. index::
   !list

Lists
=====

.. index::
   single: list; bullet
   single: list; itemize
   bullet list

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

.. index::
   single: list; horizontal
   horizontal list

Horizontal lists
----------------
    .. hlist::
       :columns: 3

       * list of
       * short items
       * that should be
       * displayed
       * horizontally

.. index::
   single: list; enumerated
   enumerated list

Enumerated list
---------------
2. We start with point number 2
#. Automatically numbered item.

a) Point a
b) Point b
#) Automatic point c.

.. index::
   single: list; definition
   definition list

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
        We define "why" we do it.

        In many paragraphs

what
  Definition of "what". We add a few
  words to show the line wrapping.
how
  Definition of "how".
why : cause
  We define "why" we do it.

  In many paragraphs.

.. index::
   single: list; field
   field list

Field list
----------
.. sidebar:: Code for examples

   ::

      :Name: Isaac Newton
      :Long: Here we insert more
         text to show the effect of
         many lines.
      :Remark:
        Start on the next line.

   ::

      -v           An option
      -o file      Same with value
      --delta      A long option
      --delta=len  Same with value

:Name: Isaac Newton
:Long: Here we insert more
   text to show the effect of
   many lines.
:Remark:
  The source starts on the next line.

.. index::
   single: list; options

Options list
------------
E.g. for listing command line options.

-v           An option
-o file      Same with value
--delta      A long option
--delta=len  Same with value

.. index::
   !block
   single: block; literal
   literal block

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

   .. warning::

      Sphinx use literal blocks to :ref:`highlight source code
      <code_highlighting>`, so the previous ``**No**`` is still written
      with a  bold font.


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


.. index::
   single: block; line
   single: quotes; line block

:restref:`Line blocks <restructuredtext.html#line-blocks>`
----------------------------------------------------------
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

.. index::
   pair: block; quotes
   !blockquotes
   single: blockquotes; pull-quote
   single: blockquotes; epigraph
   single: blockquotes; highlights
   directive; pull-quote
   directive; epigraph
   directive; highlights

:restref:`Block quotes <restructuredtext.html#block-quotes>`
------------------------------------------------------------
.. sidebar:: Code for example

   ::

      indenting them more than the surrounding paragraphs.

         Neither from itself nor from another,
         Nor from both,
         Nor without a cause,
         Does anything whatever, anywhere arise.

         --Nagarjuna - *Mulamadhyamakakarika*

         .. pull-quote::

            Just as a solid rock ...

         .. highlights::

            With these *highlights* ...


:restref:`Block quotes <restructuredtext.html#block-quotes>` are created by just
indenting them more than the surrounding paragraphs.

    Neither from itself nor from another,
    Nor from both,
    Nor without a cause,
    Does anything whatever, anywhere arise.

    --Nagarjuna - *Mulamadhyamakakarika*

An optional attribution can be set by a line beginning by two or three
minus signs flushed left at the level of the quote.

There is also a :restref:`pull-quote
<directives.html#pull-quote>`

.. pull-quote::

  Just as a solid rock is not shaken by the storm, even so
  the wise are not affected by praise or blame.

An :restref:`epigraph <directives.html#epigraph>` and an
:restref:`highlights <directives.html#highlights>` *dont forget the
final* **s** *or you fall down on the* :ref:`Sphinx code highlighting
directive <code_highlighting>`.

.. highlights::

   With these *highlights* we have completed the Rest blocks.

They all generates an
html ``<blockquote>`` but with a `class` of ``pull-quote``,
``highlights`` or ``epigraph`` that your css may use *but default css
does not!*

.. index:
   block; container
   directive; container

Container
---------
.. sidebar:: Code for example

   ::

      .. container:: myclass

         There is also a general ...

.. container:: myclass

   There is also a general :restref:`container directive
   <directives.html#container>` whose unique effect is adding some class
   name to the block that your css may use. In html this paragraph
   is enclosed in a

   .. code-block:: html

      <div class="myclass container">  ... </div>



.. index::
   !tables


Tables
======
.. _simple_tables:

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

Simple tables (:restref:`ref <restructuredtext.html#simple-tables>`)
are preceded and ended with a sequence of "``=``" to indicate the
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

Simple table cells are treated like a small document on their own up to line
breaks, but the first column must contain a single line.
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

.. _grid_tables:

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

Grid tables (:restref:`ref <restructuredtext.html#grid-tables>`)
have a more difficult syntax but can express more complex tables.

.. only:: html

          +--------+--------+-----------+
          | Header | Header with 2 cols |
          +========+========+===========+
          | A      | Lists: | **C**     |
          +--------+  - aha +-----------+
          | B::    |  - yes | | a block |
          |        |        |   of text |
          |  *hey* |  #. hi | | a break |
          +--------+--------+-----------+

.. only:: latex

          .. tabularcolumns:: |p{0.15\linewidth}|p{0.15\linewidth}|p{0.15\linewidth}|

          +--------+--------+-----------+
          | Header | Header with 2 cols |
          +========+========+===========+
          | A      | Lists: | **C**     |
          |        |  - aha |           |
          | B::    |  - yes | | a block |
          |        |        |   of text |
          |  *hey* |  #. hi | | a break |
          +--------+--------+-----------+

You can edit them under emacs with ``table.el``
(but be carefull about conflicts with ``rst-mode``) or
use *org tables* with ``orgtbl-mode`` and export to table with
``org-table-convert`` or ``org-table-create-with-table.el`` ( bound
to :kbd:`C-c ~` in ``org-mode``, but not in ``orgtbl-mode``)

.. _csv_tables:

csv tables
----------
.. sidebar:: Code

   ::

    .. csv-table:: Balance Sheet
       :header: Description,In,Out,Balance
       :widths: 20, 10, 10, 10
       :stub-columns: 1

       Travel,,230.00,-230.00
       Fees,,400.00,-630.00
       Grant,700.00,,70.00
       Train Fare,,70.00,**0.00**

    .. list-table:: Weather forecast
       :header-rows: 1
       :widths: 7 7 7 7 60
       :stub-columns: 1

       *  -  Day
          -  Min Temp
          -  Max Temp
          -
          -  Summary
       *  -  Monday
          -  11C
          -  22C
          -  .. image:: _static/sunny.svg
                :width: 30

          -  A clear day with lots of sunshine.
             However, the strong breeze will bring
             down the temperatures.
       *  -  Tuesday
       ........

.. csv-table:: Balance Sheet
   :header: Description,In,Out,Balance
   :widths: 20, 10, 10, 10
   :stub-columns: 1

   Travel,,230.00,-230.00
   Fees,,400.00,-630.00
   Grant,700.00,,70.00
   Train Fare,,70.00,**0.00**

The options are explained in the reference: :restref:`rst directive: csv-table
<directives.html#csv-table>`

You can choose a delimiter with ``:delim:`` and source an external
file with the option::

   :file:/path/of/the/file

.. _list_tables:

List Tables
-----------

A list-table (:restref:`ref <directives.html#list-table>`) is a two
level list, where the first level is a row and the second one a column
list. The number of column must be uniform (*no column span*) but
cell may contain structured markup.


.. list-table:: Weather forecast
   :header-rows: 1
   :widths: 7 7 7 7 60
   :stub-columns: 1

   *  -  Day
      -  Min Temp
      -  Max Temp
      -
      -  Summary
   *  -  Monday
      -  11C
      -  22C
      -  .. only:: html

            .. image:: _static/sunny.svg
               :width: 30

         .. only:: latex

            .. image:: _static/sunny.png
               :width: 30

      -  A clear day with lots of sunshine.
         However, the strong breeze will bring
         down the temperatures.
   *  -  Tuesday
      -  9C
      -  10C
      -  .. only:: html

            .. image:: _static/cloudy.svg
               :width: 30

         .. only:: latex

            .. image:: _static/cloudy.png
               :width: 30

      -  Cloudy with rain, across many northern regions. Clear spells
         across most of Scotland and Northern Ireland,
         but rain reaching the far northwest.


LaTeX table rendering
---------------------

Rendering with `tabulary`
^^^^^^^^^^^^^^^^^^^^^^^^^
Sphinx use the latex package `tabulary
<http://ctan.org/tex-archive/macros/latex/contrib/tabulary/tabulary.pdf>`_
to render tables in laTeX.

Tabulary is an extension of the *tabular* package which calculate le width
of columns; it has four new formats specifications: ``LRCJ`` for Left
(Right, Centered, Justified) column with automatic width.

Sphinx uses by default ``L``, but you can override it with a directive
like::

    .. tabularcolumns:: |L|C|C|R|

As examples in this document the re:`source code directives table
source_code_directives` which has a proper Sphinx automatic rendering
in tabulary ``|L|L|``, which adapt the column size with a wider left one.

The two first :ref:`simple tables <simple_tables>` the :ref:`csv table
<csv_tables>` and the :ref:`list table <list_tables>` are also
rendered in `tabulary` with a proper calculation of table width by
latex.

Rendering with `tabular`
^^^^^^^^^^^^^^^^^^^^^^^^

Tables that contain any kind of lists, such as object descriptions,
blockquotes, or  literal blocks are set by
default with the *tabular* environment with equal column size,
you can taylor the rendering by giving
`tabularcolumns` directive which uses the `p{width}` column
type.

An example is the following :ref:`source code include table
<source_code_include>`
which use both description and verbatim for wich the automatic
Sphinx rendering in latex is::

   \begin{tabular}{|p{0.475\linewidth}|p{0.475\linewidth}|}

If necessary we can adapt the relative length of columns.

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

      A link to `Sphinx Home`_ in citation style.

      .. _Sphinx Home: http://sphinx.pocoo.org

      In-line versions are
      `Sphinx Home <http://sphinx.pocoo.org>`_
       or `<http://sphinx.pocoo.org>`_
      or (in Sphinx) http://sphinx.pocoo.org


**Citation style**:

A link to `Sphinx Home`_ in citation style.

.. _Sphinx Home: http://sphinx.pocoo.org

In printed documents the link will be listed similar as a citation, as opposed
to HTML documents.

**In-line style**:

In-line versions are `Sphinx Home <http://sphinx.pocoo.org>`_ or
`<http://sphinx.pocoo.org>`_ or (in Sphinx) http://sphinx.pocoo.org

.. _internal:

Internal
^^^^^^^^
To define a label for any text location, precede it with::

   .. _‹label›:

plus a blank line.

A ``:name:`` option in any block is also an internal reference target.

There are two ways of referencing a label.

The :restref:`reST way
<restructuredtext.html#hyperlink-targets>`
is::

    `‹label›`_

The *preferred* `Sphinx way
<http://sphinx.pocoo.org/latest/markup/inline.html#cross-referencing-syntax>`_,
allows linking across files, it  uses::

   :ref:`‹displayed text› <‹label›>`

To reference ``‹label›`` defined in *any* document of the project.

If the ``‹label›`` definition is followed by a section title then ``‹displayed
text›`` can be omitted and will be replaced by the title.

E.g. this section is preceded with ``.. _internal:``, so we have:

================================== ==============================
``:ref:`internal```                :ref:`internal`
``:ref:`This section <internal>``` :ref:`This section <internal>`
``:ref:`ref to a name <mytopic>``` :ref:`ref to a name <mytopic>`
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

Extensions that define new hyperlinks targets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
-  The :sphinx:`extension intersphinx <ext/intersphinx.html>`
   which generate automatic links to the documentation
   in other projects for objects not in your own project. It interprets
   the  references  to `roles`_

   To configure it give in conf.py a dictionary like::

      intersphinx_mapping = {
          'python': ('http://docs.python.org/3.2', None)}

-  The extension :sphinx:`extlinks` generates the previous link with
   the code ``:sphinx:`extlinks``` and the configuration::

      extlinks = {'sphinx': ('http://sphinx.pocoo.org/latest/%s', 'Sphinx: ')}

Directives
==========

:restref:`Directives <directives.html>`
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

They are detailled in the document
:restref:`reStructuredText Directives
<directives.html>`

.. _reST-tableOfContents:

table of contents
^^^^^^^^^^^^^^^^^

Create a :restref:`table of contents
<directives.html#table-of-contents>`
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

   `Other options <ReST image directive>`_ are:

   -  ``:scale: <integer percentage>``,
   -  ``:align: {top|middle|bottom|left|right}``,
   -  ``:target: <URI or reference>``

**Include an image** (see also  `images in the Sphinx documentation
<http://sphinx.pocoo.org/rest.html#images>`_ and
:restref:`ReST image directive
<directives.html#images>` )

.. image:: _static/sphinx.png
   :width: 250px
   :alt: sphinx logo


**Include a figure**

.. figure:: _static/sphinx.png
   :width: 250px
   :alt: sphinx logo

   The logo for Sphinx

**figures and LaTeX export**

The reST commant `rst2latex` use the width an hight of images and
figures but
the Sphinx laTeX exporter use also ``\includegraphics`` to import the figure;
but (as a far as Sphinx 1.2pre) it does not use the width and height
attribute.

To get proper figure size in latex generated by Sphinx you may have either to

   - resize the figure before including it,
   - use the ``:scale:`` option that is supported and generates a latex
     ``\scalebox``
   - or put a distinct laTeX code in an ``only:: latex`` directive that
     use something like::

       \includegraphics[width=60mm, height=40mm]{myfig.png}

Latex does not support svg and it has to be converted to eps or pdf,
pdf being the only one to support transparency.
The conversion can be done with  Inscape, it can be automated as `explained by Johan B. C. Engelen
<http://ctan.tug.org/tex-archive/info/svg-inkscape/InkscapePDFLaTeX.pdf>`_.
You can also use the `ipe drawing editor
<http://ipe7.sourceforge.net/>`_.


replacement
^^^^^^^^^^^

General replacements::

   .. |‹something›| ‹directive›:: here we
      define what ‹something› is.

.. sidebar:: Code for example

   ::

      .. |more-doc| replace::  *more in directives manual*
      .. _more-doc: http://docutils.sourceforge.net/doc...

      Possible ...  or ``image`` |more-doc|_

Here ``|<something>|`` will be replaced by its definition.

.. |more-doc| replace::  *more in directives manual*
.. _more-doc: http://docutils.sourceforge.net/docs/ref/rst/directives.html#replacement-text

Possible ``‹directive›``\ s are ``replace`` or ``image`` |more-doc|_

It can be used *like above* for nesting inline markup.


file include
^^^^^^^^^^^^
+----------------------------------+---------------------------------------------+
|**Including** a reST file ::      | .. note:: Don't use the same file name      |
|                                  |    extension as your source files.          |
|   .. include:: ‹file name>       |    Otherwise Sphinx will mistake this       |
|                                  |    file as one of your regular source file. |
|See also :ref:`Source code include|                                             |
|<source_code_include>`            |                                             |
+----------------------------------+---------------------------------------------+


sidebar, and topic
^^^^^^^^^^^^^^^^^^
A :restref:`sidebar
<directives.html#sidebar>`
or a :restref:`topic <directives.html#topic>`  are treated like documents on
their own::

   .. sidebar:: ‹Title›

      ‹body›

   .. topic:: Topic Title
      :name: mytopic

      Subsequent indented lines comprise
      the body of the topic, and are
      interpreted as *body elements*.


.. topic:: Topic Title
   :name: mytopic

   Subsequent indented lines comprise
   the body of the topic, and are
   interpreted as *body elements*.

rubric
^^^^^^
A :restref:`rubric
<directives.html#rubric>`
is a title not appearing in the table of contents::

   .. rubric:: ‹Title›




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

Relative names are relative to the document the directive occurs in,
absolute names are relative to the source directory.

The depth can be further restricted per file by inserting the
following `Field list`_ type element in the very first line of the file::

   :tocdepth: ‹depth›

See :sphinx:`Sphinx: Toc tree <markup/toctree.html>` for other
options.

To get a table of content *inside* a file, use the :ref:`reST table of
contents <reST-tableOfContents>`



Index and glossaries
^^^^^^^^^^^^^^^^^^^^
.. index::
       single: index (Rest)

Entries in the **index** are created automatically from all information units
like functions, classes or attributes but those with a ``:noindex:``
option.  Explicit manual entries are made as::

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


centered
^^^^^^^^

A centered, boldface text block::

   .. centered:: ‹text block›

.. centered:: This text is
      *centered, boldface*

Selective inclusion
^^^^^^^^^^^^^^^^^^^

A block may be included depending of the presence of some tag::

   ..only:: <expression>

The expression is made of *tags* like ``html and draft``.

You can define tags via the -t command-line option of ``sphinx-build``
or in the configuration file use  ``tags.has('tag')``  to query, ``tags.add('tag')``  and ``tags.remove('tag')``  to change.

.. _roles:

Sphinx Roles
------------

they are described in `Sphinx: Inline markup
<http://localhost/doc/python-sphinx/html/markup/inline.html>`_
and in the specific domains e.g.
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

Sphinx Source Code
==================

.. _code_highlighting:

Code highlighting
-----------------

**Highlighting language** used by  `Pygment <http://pygments.org>`_ in
`Literal Blocks`_  is set for following code examples by::

   .. highlight:: ‹language›
      :linenothreshold: ‹number›

The option language may be any of
`Pygment supported languages <http://pygments.org/languages/>`_

The additional ``linenothreshold`` option switches on line numbering for blocks
of size beyond ‹number› lines.

Specify the highlighting for a single literal block::

   .. code-block:: ‹language›
      :linenos:

      ‹body›

The ``linenos`` option switches on line numbering.

Details of options are in
`Sphinx Manual: code examples <http://sphinx.pocoo.org/markup/code.html>`_.

.. _source_code_include:

Source code include
-------------------
+---------------------------------------------+---------------------------------------------------------+
|To include the source file ``example.py``    |.. literalinclude:: example.py                           |
| as a literal block use::                    |   :linenos:                                             |
|                                             |                                                         |
|   .. literalinclude:: example.py            |                                                         |
|      :linenos:                              |                                                         |
|                                             |                                                         |
+---------------------------------------------+---------------------------------------------------------+
|More Options::                               |The options ``language`` and ``linenos``                 |
|                                             |set the highlighting to ``‹language›``                   |
|   .. literalinclude:: ‹filename›            |and enables line numbers respectively.                   |
|      :language: ‹language›                  |                                                         |
|      :linenos:                              |You can select lines by the ``:lines:`` option or by     |
|      :lines: 1,3,5-10,20-                   |``start-after:<string>`` and/or ``end-before:<string>``  |
|                                             |                                                         |
+---------------------------------------------+---------------------------------------------------------+
|::                                           |If it is a Python module, you can select a class,        |
|                                             | function or method to include using the ``pyobject``    |
|   .. literalinclude:: example.py            | option                                                  |
|      :pyobject: MyClass.some_method         |                                                         |
|                                             |                                                         |
+---------------------------------------------+---------------------------------------------------------+



.. _source-code-directives:

Source code directives
----------------------

There are very powerful directives in Sphinx
for `documenting source code
<http://sphinx.pocoo.org/markup/desc.html#module-specific-markup>`_
most are since *version 1.0* in `specific domains
<http://sphinx.pocoo.org/domains.html>`_ the following are related to
`documenting python source code
<http://sphinx.pocoo.org/domains.html#the-python-domain>`_

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

autodoc
-------

There is  an `autodoc <http://sphinx.pocoo.org/latest/ext/autodoc.html>`_
version of the :ref:`source code directives <source-code-directives>`
which include documentation from docstrings:

- ``automodule``, ``autoclass``, ``autoexception``.
   They  accept an option ``:members:`` to include
   a specific list of members, or all members when the ``:members:`` option is empty.

   ::

      .. autoclass:: Noodle
         :members: eat, slurp

- ``autofunction``, ``autodata``, ``automethod``, ``autoattribute``

.. _info-fields:

Info field lists
----------------
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
`following fields
<http://sphinx.pocoo.org/markup/desc.html#info-field-lists>`_
are recognized:
``param``,  ``arg``,  ``key``, ``type``, ``raises``, ``raise``, ``except``, ``exception``, ``var``, ``ivar``, ``cvar``, ``returns``, ``return``, ``rtype``

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

Source code docstring
---------------------
.. sidebar:: alternate syntax

   .. literalinclude:: docstring.py
      :language: python

You can use the :ref:`previous fields <info-fields>` or the alternate syntax

.. automodule:: docstring
   :noindex:
   :members:


`Sphinx <http://sphinx.pocoo.org/>`_
====================================

Project
-------

To start a Sphinx project use the interactive `sphinx-quickstart
<http://sphinx.pocoo.org/latest/man/sphinx-quickstart.html>`_ command.
This will ask you all the necessary questions.You can choose to build with a
Makefile.

Customization is done in the file `conf.py
<http://sphinx.pocoo.org/latest/config.html>`_
and the `Makefile
<http://sphinx.pocoo.org/latest/invocation.html#makefile-options>`_.

In the conf file you put the configuration of the extensions




Math
----

There is a :sphinx:`mathematical typesetting Sphinx extension
<ext/math.html?module-sphinx.ext.mathbase>`
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

-  This doc is a fork of `Cristoph Reller Memo
   <http://people.ee.ethz.ch/~creller/web/tricks/reST.html>`_
   adapted according to my needs, they have diverged now, but some
   part come from his work and  I have adopted his  layout.
-  `Sphinx documentation <http://sphinx.pocoo.org/latest/contents.html>`_
-  Sphinx `reStructuredText Primer <http://sphinx.pocoo.org/latest/rest.html>`_
-  `Documenting Your Project Using
   Sphinx <http://packages.python.org/an_example_pypi_project/sphinx.html>`_
   from `an example pypi project’s
   <http://packages.python.org/an_example_pypi_project/>`_
-  `Openalea project: How to use sphinx ?
   <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/sphinx.html>`_
   by Thomas Cokelaer, the author also gives a more recent version:
   `Sphinx and RST syntax guide
   <http://thomas-cokelaer.info/tutorials/sphinx/contents.html>`_.
-  The `ReStructuredText Documentation <http://docutils.sourceforge.net/docs/>`_

   -  `Docutil reStructuredText Primer
      <http://docutils.sourceforge.net/docs/user/rst/quickstart.html>`_
      you may prefer the python the *Sphinx* nicely formated
      documentation cited above, also available *with a distinct layout* as
      `docs.python: reStructuredText Primer
      <http://docs.python.org/dev/documenting/rest.html>`_
   -  :restref:`Quick reStructuredText
      <quick.html>`
   -  :restref:`reStructuredText Markup Specification
      <restructuredtext.html>`
   -  :restref:`reST Directives <directives.html>`
   -  :restref:`Interpreted Text Roles <roles.html>`
   -  `ReStructuredText Demonstration <http://docutils.sourceforge.net/docs/user/rst/demo.html>`_
-  `Emacs Support for reStructuredText
   <http://docutils.sourceforge.net/docs/user/emacs.html>`_
-  `Epydoc reST markup <http://epydoc.sourceforge.net/manual-othermarkup.html>`_
-  `Documenting Python <http://docs.python.org/dev/documenting/index.html>`_
-  `Pylons Book:  Documentation
   <http://pylonsbook.com/en/1.1/documentation.html>`_
   is itself a good example of sphinx documentation.
-  `sampledoc tutorial <http://matplotlib.sourceforge.net/sampledoc/>`_
   from `matplotlib <http://matplotlib.sourceforge.neti/>`_
   *a python 2D plotting library*.
-  `rst2pdf <http://code.google.com/p/rst2pdf/>`_ is a
   tool for transforming reStructuredText to PDF using ReportLab.
   It supports Sphinx.
-  How to write docstrings:

   -  Look at examples in `Official list of projects using Sphinx
      <http://sphinx.pocoo.org/examples.html>`_
   -  The last parts of `Documenting Python`_:
      `function definitions
      <http://packages.python.org/an_example_pypi_project/sphinx.html#function-definitions>`_
      and `Full Code Example
      <http://packages.python.org/an_example_pypi_project/sphinx.html#full-code-example>`_
   -  `OpenAlea
      <http://openalea.gforge.inria.fr/wiki/doku.php?id=documentation:doctests:how_to_document_python_api>`_
      has a nice `comparaison of three way of filling the docstring
      <http://openalea.gforge.inria.fr/wiki/doku.php?id=documentation:doctests:sphinx_proposal#filling_the_docstring>`_.
      The source is  `template.py
      <https://gforge.inria.fr/scm/viewvc.php/trunk/doc/source/sphinx/template.py?view=markup&root=openalea>`_
   -  Sources of
      `mongo python driver
      <https://github.com/mongodb/mongo-python-driver>`_
      are also a good example

-  Extending sphinx:

   -  `Sphinx Tutorial: Writing a simple extension <http://sphinx.pocoo.org/ext/tutorial.html>`_
   -  `Defining Custom Roles in Sphinx
      <http://www.doughellmann.com/articles/how-tos/sphinx-custom-roles/index.html>`_
      a  `Sphinx blog post by Doug Hellmann
      <http://blog.doughellmann.com/search/label/sphinx>`_
   -  :restref:`Creating Interpreted Text Roles
      <rst-roles.html>`
      from docutils project.
   -  :restref:`Creating reStructuredText Directives
      <rst-directives.html>`
      from docutils project.
