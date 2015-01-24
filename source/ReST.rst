:tocdepth: 3

*******************************
:mod:`reST` -- reStructuredText
*******************************

.. module:: reST
   :synopsis: reStructuredText Memo
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
exact order of the decoration is not important, the one below is the
`Python convention <http://docs.python.org/devguide/documenting.html#sections>`_. ::

  ####
  Part
  ####

  *********
   Chapter
  *********

  Section
  =======

  Subsection
  ----------

  Subsubsection
  ^^^^^^^^^^^^^

  Paragraph
  """""""""

  Normal paragraphs are separated by a blank line.

.. _Transition:

A ``=`` with overlines is very often preferred to a ``*`` with
overlines for chapters. The previously quoted
`Python development guide
<http://docs.python.org/devguide/documenting.html#sections>`_ while
advising to use stars uses internally equal character.

`Docutils documentation <http://docutils.sourceforge.net/>`_ uses
overlined ``=`` for parts, overlined ``-`` for chapters, ``=`` for sections,
``-`` for subsections, back quotes (`) for subsubsections.

Transition
----------
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

.. _rest_inline_markup:

Inline markup
=============
.. sidebar:: Special cases

   ================== =============
   ``Asterisk \*``    Asterisk \*
   ``back-quote \```  back-quote \`
   ``**mark**\ up.``  **mark**\ up.
   ================== =============

========================== ======================
``*emphasize*``            *emphasize*
``**emphasize strongly**`` **emphasize strongly**
````code````               ``code``
```don't know```           `don't know`
========================== ======================

See :restref:`inline markup reference
<restructuredtext.html#inline-markup>`.

These inline markups are also provided by
:restref:`ReStructuredText Interpreted Text Roles <roles.html>`.
The roles are described in the :ref:`Sphinx chapter <sphinx_roles>`

.. index::
   !list

Lists
=====
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

   ::

      what
        Definition of "what". We add a few
        words to show the line wrapping.
      how
        Definition of "how".
      why : cause
        We define "why" we do it.

        In many paragraphs

.. index::
   single: list; bullet
   single: list; itemize
   bullet list

Bullet list
-----------

- First item with some lengthy
  text wrapping hopefully
  across several lines.
- Second item

See :restref:`bullet list reference<restructuredtext.html#bullet-lists>`

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

See :restref:`enumerated list reference
<restructuredtext.html#enumerated-lists>`.

.. index::
   single: list; definition
   definition list

.. _definition_list:

Definition list
---------------

what
  Definition of "what". We add a few
  words to show the line wrapping.
how
  Definition of "how".
why : cause
  We define "why" we do it.

  In many paragraphs.

See :restref:`definition list reference
<restructuredtext.html#definition-lists>`.

.. index::
   single: list; field
   field list

.. _Field list:

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

See :restref:`field list reference
<restructuredtext.html#field-lists>`.

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

      *Sphinx* use literal blocks to :ref:`highlight source code
      <code_highlighting>`, so the previous ``**No**`` is still written
      with a  bold font by *Sphinx* while being not interpreted by
      *rst2html*.

      *Sphinx* users better use a :ref:`code block <code_block>` in
      ``text`` language, to disable *Pygment* decorations.

   ::

      | Line block
      | New line and we are still on
        the same line
      |   Yet a new line


Blocks
======

.. _literal_block:

Literal Block
-------------

:restref:`rest literal blocks <restructuredtext.html#literal-blocks>`

A block which is not interpreted at all is preceded by a ``::`` and a blank
line. The block must be indented.  If no white space is preceding the
``::`` then it is displayed as ":".

To use a specific formatting, you can use the :ref:`code directive <rst-code>`

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

Line blocks
-----------

In a line block (:restref:`ref <restructuredtext.html#line-blocks>`)
every line is preceded with ``|`` and at least one space.

| Line block
| New line and we are still on
  the same line
|   Yet a new line

.. index::
   pair: block; quotes
   !blockquote

.. _blockquote:

Block quote
-----------
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


Block quotes (:restref:`ref <restructuredtext.html#block-quotes>`) are
created by just indenting them more than the surrounding paragraphs.

    Neither from itself nor from another,
    Nor from both,
    Nor without a cause,
    Does anything whatever, anywhere arise.

    --Nagarjuna - *Mulamadhyamakakarika*

An optional attribution can be set by a line beginning by two or three
minus signs flushed left at the level of the quote.


.. index::
   pair:directive; pull-quote

.. _pull-quote:

Pull-quote
----------

Pull-quotes  (:restref:`ref <directives.html#pull-quote>`)
are similar to blockquotes but are :ref:`directives <rest_directives>`

.. pull-quote::

  Just as a solid rock is not shaken by the storm, even so
  the wise are not affected by praise or blame.

.. index::
   single: blockquote; epigraph
   single: blockquote; highlights
   directive; epigraph
   directive; highlights


.. _epigraph:

Epigraph and highlights
-----------------------

An `epigraph` directive (:restref:`ref <directives.html#epigraph>`) and an
`highlights` directive (:restref:`ref <directives.html#highlights>`)
are aimed to put a quotation in a distinct font.

*dont forget the final* **s** *of highlights, or you fall down on the*
:ref:`Sphinx code highlighting directive <code_highlighting>`

.. highlights::

   With these *highlights* we have completed the Rest blocks.

These three directives are similar in
html  rendering to :ref:`blockquote` but with a `class` of ``pull-quote``,
``highlights`` or ``epigraph`` that your css may use *but default css
does not!*

.. index::
   block; container
   pair: directive; container

.. _container:

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
   pair: directive; class


.. class_directive:

Class
-----
.. sidebar:: Code for example

   ::

      .. class:: myclass

      The class directive ....

.. class:: myclass

The class directive (:restref:`ref <directives.html#class>`) add a
class on its content or on the first immediately following non-comment
element.  The name of the class is normalized by docutil to conform to
the regexp: ``[a-z](-?[a-z0-9]+)*``.

.. note::

   While the docutil tool ``rst2html`` put as expected the previous
   paragraph in a::

     <p class="myclass">....</p>

   Sphinx *as far as 1.2pre* does not put any class on the ``<p>``
   element. The use of a :ref:`container` is presently better suited
   to  apply a css decoration.




.. index::
   !table


Tables
======

.. index::
   pair: table; simple


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

.. index::
   pair: grid; table

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
.. index::
   table; emacs

You can edit them under emacs with ``table.el``
(but be carefull about conflicts with ``rst-mode``) or
use *org tables* with ``orgtbl-mode`` and export to table with
``org-table-convert`` or ``org-table-create-with-table.el`` ( bound
to :kbd:`C-c ~` in ``org-mode``, but not in ``orgtbl-mode``)


.. index::
   triple: directive; table; csv

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


.. index::
   triple: directive;  table; list

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
      -  .. only:: not latex

            .. image:: _static/sunny.svg
               :width: 30

         .. only:: latex

            .. image:: _static/sunny.pdf
               :width: 30

      -  A clear day with lots of sunshine.
         However, the strong breeze will bring
         down the temperatures.
   *  -  Tuesday
      -  9C
      -  10C
      -  .. only:: not latex

            .. image:: _static/cloudy.svg
               :width: 30

         .. only:: latex

            .. image:: _static/cloudy.pdf
               :width: 30

      -  Cloudy with rain, across many northern regions. Clear spells
         across most of Scotland and Northern Ireland,
         but rain reaching the far northwest.


.. index::
   pair: table; latex

LaTeX table rendering
---------------------

Rendering with *:index:`tabulary`*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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

Rendering with *:index:`tabular`*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tables that contain any kind of lists, such as object descriptions,
blockquotes, or literal blocks are set by default with the `tabular
<http://en.wikibooks.org/wiki/LaTeX/Tables#The_tabular_environment>`_
environment with equal column size, you can taylor the rendering by
giving `tabularcolumns` directive which uses the `p{width}` column
type.

An example is the following :ref:`source code include table
<source_code_include>`
which use both description and verbatim for wich the automatic
Sphinx rendering in latex is::

   \begin{tabular}{|p{0.475\linewidth}|p{0.475\linewidth}|}

If necessary we can adapt the relative length of columns.


Cross references
================
.. index::
   hypertext; link
   hypertext; target
   cross reference

Hypertext links
---------------
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


Citation style
^^^^^^^^^^^^^^

A link to `Sphinx Home`_ in citation style.

.. _Sphinx Home: http://sphinx.pocoo.org

In printed documents the link will be listed similar as a citation, as opposed
to HTML documents.

In-line style
^^^^^^^^^^^^^

In-line versions are `Sphinx Home <http://sphinx.pocoo.org>`_ or
`<http://sphinx.pocoo.org>`_ or (in Sphinx) http://sphinx.pocoo.org


.. index::
   reference
   ref
   reference; target
   reference; label

.. _internal:
.. _ref:

internal document reference
---------------------------
To define ``label`` as label for any text location internal to a document,
precede the text location with::

   .. _label:

plus a blank line.

A ``:name:`` option in any block is also an internal reference target.

There are two ways of referencing a label.

.. _rest_ref:

The :restref:`reST way
<restructuredtext.html#hyperlink-targets>`
is::

    `label`_

The *preferred* `Sphinx way
<http://sphinx.pocoo.org/latest/markup/inline.html#cross-referencing-syntax>`_,
allows linking across files, it  uses::

   :ref:`displayed text <label>`

it is specific to Sphinx and :ref:`you find it in the Sphinx section
<sphinx_cross_references>`.

Section titles, footnotes, and citations automatically are link targets.
```Transition`_`` produces `Transition`_. But they don't work with the
:ref:`Sphinx ref syntax <sphinx_ref>`.

If you want to change the displayed text with the
:ref:`ReST ref syntax <rest_ref>`
you can use an indirect
reference. You can then also reference the `Transition`_ section
as `how to draw an horizontal line`_ with
the hyperlink: ```how to draw an horizontal line`_`` and the
indirect target::

  .. _how to draw an horizontal line: Transition_

.. _how to draw an horizontal line: Transition_


.. _explicit_markup:

Explicit Markup
===============
They all begin with two periods and a white space.

.. index::
   !footnote

Footnotes (:restref:`ref <restructuredtext.html#footnotes>`)
------------------------------------------------------------
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

.. index::
   !citation

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

.. index::
   !directive
   rest; directives

.. _rest_directives:

Rest Directives
===============

:restref:`Directives <directives.html>`
are a general-purpose extension mechanism.  The general syntax is
similar to `explicit_markup`_::

   .. ‹name›:: ‹argument 1›
               ‹argument 2›
      :‹option 1›: ‹value›

      ‹body›

The reST directives are detailed  in the
:restref:`docutils reference: reStructuredText Directives
<directives.html>`

.. here we reference

   :ref:`table of contents
   <reST-tableOfContents>`,  :ref:`image`, :ref:`figure`,
   :ref:`replacement <replacements>`, :ref:`file include
   <file_include>`, :ref:`sidebar, and topic <sidebar>`,
   :ref:`rubric`.

.. contents::
   :local:


We have yet see above the directives :ref:`pull-quote` and :ref:`epigraph`.

.. index::
   toc
   table; of contents
   pair: contents; directive

.. _reST-tableOfContents:

table of contents
-----------------

Create a :restref:`table of contents
<directives.html#table-of-contents>`
containing (sub)titles ranging from level 1 to
level ‹number› if you use the ``:local:`` option the TOC is local to
the section where it appears, otherwise it is for the whole file, the title may be empty::

   .. contents:: `Table of contents`
      :depth: ‹number›
      :local:

.. index::
   pair: image; directive
   pair: figure; directive

.. _image:

image and figure
----------------

.. sidebar:: Code for examples

   ::

      .. image:: _static/NeoHittiteSphinx.svg
         :width: 120px
         :alt: Sphinx Neo-Hittite
         :target: https://it.wikipedia.org/wiki/Telepinu_(divinità)

      .. figure:: _static/NeoHittiteSphinx.svg
         :width: 120px
         :alt: Sphinx Neo-Hittite

         Sphinx Neo-Hittite

         Telepinu is an `Hitite <http://en.wikipedia.org/wiki/Hittites>`_
         deity.

   `Other options <ReST image directive>`_ are:

   -  ``:scale: <integer percentage>``,
   -  ``:align: {top|middle|bottom|left|right}``

**Images** (:restref:`ref <directives.html#images>`)
are simple pictures, see also
`images in the Sphinx documentation
<http://sphinx.pocoo.org/rest.html#images>`_

.. for ulterior reference

   http://www.britishmuseum.org/system_pages/beta_collection_introduction/beta_collection_object_details.aspx?objectId=1650465&partId=1



.. only:: not latex

   .. image:: _static/NeoHittiteSphinx.svg
      :width: 120px
      :alt: Sphinx Hittite
      :target: https://it.wikipedia.org/wiki/Telipinu_(divinità)

.. only:: latex

   .. image::  _static/NeoHittiteSphinx.pdf
        :width: 120px
        :alt: Sphinx Hittite
        :target: https://it.wikipedia.org/wiki/Telipinu_(divinità)

You can click on this image to go to the target `Wikipedia (it): Telepinu
<http://it.wikipedia.org/wiki/Telipinu_(divinità)>`_

.. _figure:


A **figure** (:restref:`ref <directives.html#figure>`) add to an image
an optional caption and an optional legend.

.. only:: not latex

   .. figure:: _static/NeoHittiteSphinx.svg
      :width: 120px
      :alt: Sphinx Hittite

      Sphinx Hittite

      Telepinu is an `Hitite <http://en.wikipedia.org/wiki/Hittites>`_
      deity.

.. only:: latex

   .. figure:: _static/NeoHittiteSphinx.pdf
      :width: 120px
      :alt: Sphinx Hittite

      Sphinx Hittite

      Telepinu is an `Hitite <http://en.wikipedia.org/wiki/Hittites>`_
      deity.


.. index::
   image; latex
   figure; latex

Images and LaTeX export
^^^^^^^^^^^^^^^^^^^^^^^

The reST command `rst2latex` use the width an hight of images and
figures but
the Sphinx laTeX exporter use also ``\includegraphics`` to import the figure;
but (as a far as Sphinx 1.2pre) it does not use the width and height
attribute.

To get proper figure size in latex generated by Sphinx you may have either to

   - resize the figure before including it,
   - use the ``:scale:`` option that is supported and generates a latex
     ``\scalebox``
   - or put a distinct laTeX code in an ``raw:: latex`` directive that
     use something like::

       \includegraphics[width=60mm, height=40mm]{myfig.png}

Latex does not support svg and it has to be converted to eps or pdf,
pdf being the only one to support transparency.
The conversion can be done with  Inscape, it can be automated as `explained by Johan B. C. Engelen
<http://ctan.tug.org/tex-archive/info/svg-inkscape/InkscapePDFLaTeX.pdf>`_.
You can also use the `ipe drawing editor
<http://ipe7.sourceforge.net/>`_.


.. index::
   pair: code; directive
   pair: code-block; directive
   pair: sourcecode; directive

.. _rst-code:

code blocks
-----------

:restref:`ref: code directive <directives.html#code>`

::

   .. code:: ‹language›
      :linenos:

      ‹body›

is the ReST directive which is called in python
:ref:`code-block` or :ref:`sourcecode <code-block>`.

You must use ``code-block`` or ``sourcecode`` with Sphinx
and the  ``code`` with ReST utilities.

ReST use the same :ref:`code highlighting <code_highlighting>` than
Sphinx, look at  :ref:`Sphinx code highlighting <code_highlighting>`
to learn about the ways to specify it.

.. _replacements:

.. index::
   !replacement
   pair: replacement; image
   pair: replace; directive
   pair: image; directive
   pair: unicode; directive
   pair: date; directive
   single: substitution; definition
   single: reference; styled
   single: unicode; character code

replacements
------------
rest references: :restref:`substitution definitions (specification)
<restructuredtext.html#substitution-definitions>`,
:restref:`substitution definition (definition files)
<definitions.html#substitution-definitions>`,
:restref:`Character Entity Sets
<definitions.html#character-entity-sets>`,
:restref:`replace directive
<directives.html#replacement-text>`,
:restref:`unicode directive
<directives.html#unicode-character-codes>`,
:restref:`date directive
<directives.html#date>`.

See also: `docutil FAQ: How can I represent esoteric characters?
<http://docutils.sourceforge.net/FAQ.html#how-can-i-represent-esoteric-characters-e-g-character-entities-in-a-document>`_.

General replacements::

   .. |something| replace:: here we
      define what something is.

.. sidebar:: Code for example

   ::

      .. |more-doc| replace::  *more in* **reST** *directives manual*
      .. _more-doc: http://docutils.sourceforge.net/doc...
      .. |copy|   unicode:: U+000A9 .. COPYRIGHT SIGN

       Instead ...  use ``image`` |more-doc|_
       ... include unicode characters like |copy|.

Here ``|something|`` will be replaced by its definition.

.. |more-doc| replace::  *more in* **reST** *directives manual*
.. _more-doc: http://docutils.sourceforge.net/docs/ref/rst/directives.html#replacement-text

Instead of  ``replace`` you can also use ``image`` |more-doc|_

It is the only way  for nesting inline markup to create styled references
like we did  *above*.

.. |copy|   unicode:: U+000A9 .. COPYRIGHT SIGN

We also use substitutions to include unicode characters like |copy|.

If you use sphinx there are also three :sphinx:`predefined substitutions
<markup/inline.html#substitutions>`:
``|release|``, ``|version|``, ``|today|``.

.. index::
   pair: include; directive
   file include

.. _file_include:

file includes
-------------
To include a reST file use::

.. include:: subdir/incl.rst

You can put the file wherever you want the relative paths are
interpreted relative to the source directory.

The options: ``start-line``, ``end-line``, ``start-after``, ``end-before``
as referenced in :restref:`reST Directives
<directives.html#including-an-external-document-fragment>`.

For including source code in Sphinx rather use :ref:`Source code include
<source_code_include>` like:

If you use ``include`` with Sphinx, you should exclude the included
files from the source file lookup, by setting in ``conf.py`` a
glob pattern in ``exclude_patterns``, like::

   exclude_patterns = ["include/*"]


.. index::
   sidebar
   topic

.. _sidebar:

sidebar, and topic
------------------
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

.. index:: topic

.. topic:: Topic Title
   :name: mytopic

   Subsequent indented lines comprise
   the body of the topic, and are
   interpreted as *body elements*.

.. index:: rubric

.. _rubric:

rubric
------
A :restref:`rubric
<directives.html#rubric>`
is a title not appearing in the table of contents::

   .. rubric:: ‹Title›


.. index::
   comment

.. _comment:

Comment
-------

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

.. _common_options:

Common options
--------------

The class options ``:class:`` and ``:name:``
are supported by most of the directives.

The following topic render in html as::

  <div class="exceptional topic" id="say-no-more">
  <p class="topic-title first">the end</p>
  <p>A final word.</p>
  </div>

.. sidebar:: Code for example

   ::

      .. topic:: The end
         :class: exceptional
         :name: say-no-more

         A final word.


The ``:name:`` act as a reference target and allow to refer to the following
block as `say-no-more`_

.. topic:: the end
   :class: exceptional
   :name: say-no-more

   A final word.
