*******************************
:mod:`ReST` -- reStructuredText
*******************************

.. module:: reST
   :synopsis: reStructuredText Memo
.. moduleauthor:: Marc Zonzon <marc.zonzon@gmail.com>

.. highlight:: rest

A simple markup language for plain text files.

.. contents::
   :local:
   :depth: 1


Structural elements
===================
.. contents::
   :local:

.. index::
   single: emacs; mode

Emacs ReST mode
---------------

=======================  ==========================================
``C-c C-=``              Adjust/rotate  or promote/demote the decorations
``C-- C-c C-=``          reverse Adjust
``C-c C-a C-d``          Display the title decoration hierarchy.
``C-- C-c C-r <tab>``    shift region left
``C-c C-r <tab>``        shift region right
``C-c C-t C-t``          display a table of content to navigate buffer
=======================  ==========================================

Sectioning
----------



.. index::
   !title
   single: title; hierarchy

Titles are under- (and over-)lined (decorated) by ``=*-^"~`:.'#`` as below.  The
exact order of the decoration is not important, the one below is the
`Python convention <http://docs.python.org/devguide/documenting.html#sections>`_.

+------------------------------+------------------------------+
|  ::                          |  ::                          |
|                              |                              |
|     ####                     |                              |
|     Part                     |     Subsection               |
|     ####                     |     ----------               |
|                              |                              |
|     *********                |                              |
|     Chapter                  |     Subsubsection            |
|     *********                |     ^^^^^^^^^^^^^            |
|                              |                              |
|     Section                  |     Paragraph                |
|     =======                  |     """""""""                |
|                              |                              |
+------------------------------+------------------------------+


Normal paragraphs are separated by a blank line.

A ``=`` with overlines is very often preferred to a ``*`` with
overlines for chapters. The previously quoted
`Python development guide
<http://docs.python.org/devguide/documenting.html#sections>`_ while
advising to use stars uses internally equal character.

`Docutils documentation <http://docutils.sourceforge.net/>`_ uses
overlined ``=`` for parts, overlined ``-`` for chapters, ``=`` for
sections, ``-`` for subsections, back quotes (`) for subsubsections.

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

==========================  ======================
``*emphasize*``             *emphasize*
``**emphasize strongly**``  **emphasize strongly**
````code````                ``code``
```don't know```            `don't know`
``Asterisk \*``             Asterisk \*
``back-quote \```           back-quote \`
``**mark**\ up.``           **mark**\ up.
==========================  ======================

See :restref:`inline markup reference
<restructuredtext.html#inline-markup>`.

..  _rest_roles:

ReStructuredText Text Roles.
----------------------------

The :restref:`ReStructuredText Interpreted Text Roles <roles.html>`
are valid both for reST and Sphinx processing.  They are:
``:emphasis:``, ``:strong:``, ``:literal:``, ``:code:``, ``:math:``,
``:pep-reference:``, ``:rfc-reference:``, ``:subscript:``,
``:superscript:``, ``:title-reference:``, ``:raw:``. The first three
are seldom used because we prefer the shortcuts provided by previous
:ref:`reST inline markup <rest_inline_markup>`.

The :restref:`Custom Interpreted Text Roles <directives.html#role>`
which is a reST directive ``role``, the tailor the renderer to
apply some special formatting. We use it
:ref:`in Sphinx section <css_class>`
to use a special css class for some span of text.

.. index::
   !list

Lists
=====

.. contents::
   :local:


.. index::
   single: list; bullet
   single: list; itemize
   bullet list

Bullet list
-----------

::

   - First item with some lengthy
     text wrapping hopefully
     across several lines.

     * We can have subitems
     * separated by a blank line
     * and indented.

   - Second item


- First item with some lengthy
  text wrapping hopefully
  across several lines.

  * We can have subitems
  * separated by a blank line
  * and indented.

- Second item


We can begin each item with ``*``, ``+``, ``-``, ``•``, ``‣``, or
``⁃`` followed by at least one space, you should keep the indentation
of the text of the first line in subsequents lines.

See :restref:`bullet list reference<restructuredtext.html#bullet-lists>`

.. index::
   single: list; horizontal
   horizontal list

Horizontal lists
----------------
  ::

    .. hlist::
       :columns: 3

       * list of
       * short items
       * that should be
       * displayed
       * horizontally

.. hlist::
   :columns: 3

   * list of
   * short items
   * that should be
   * displayed
   * horizontally

*hlist is a sphinx extension, not a ReST directive*

.. index::
   single: list; enumerated
   enumerated list

Enumerated list
---------------
::

   2. We start with point number 2
   #. Automatically numbered item.

   a) Point a

      i) first subitem
      ii) second subitem

   b) Point b
   #) Automatic point c.

2. We start with point number 2
#. Automatically numbered item.

a) Point a

   i) first subitem
   ii) second subitem

b) Point b
#) Automatic point c.

We can use enumerate with numerals, alphabetic lower case or upper
case, roman numerals lower case or upper case.

We can write enumeration followed by a period, a right parenthese, or
surrounded by a parentheses; but these punctuation are not kept in the
rendering; *rst2html* render ``i.``, ``i)`` or ``(i)`` as "i." and
Sphinx render them as "a.".

A list must be separated from previous paragraph by a blank line, in
the same way sublists must be separated from items of upper list by a
blank line.

Any break of sequence in the source, produces a new list.

See :restref:`enumerated list reference
<restructuredtext.html#enumerated-lists>`.

.. index::
   single: list; definition
   definition list

.. _definition_list:

Definition list
---------------
::

   what
     Definition of "what". We add a few
     words to show the line wrapping.

   how
     Definition of "how".

   why :
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

With ReST but not Sphinx you can use a classifier after the main term
like
::

   why : cause
     We define "why" we do it.

We may have to escape a markup character to clear ambiguity between
a definition list and an other construct like:

::

   \(w)
      This is a definition list, not an enumeration.


See :restref:`definition list reference
<restructuredtext.html#definition-lists>`.

.. index::
   pair: list; field

.. _field list:

Field list
----------
.. list-table::
   :widths: 40, 60

   *
      - .. code-block:: ReST

             :Name: Isaac Newton
             :Long: Here we insert more text
                in many lines.
             :Remark:
               Starts on the next line.
      - :Name: Isaac Newton
        :Long: Here we insert more text
           in many lines.
        :Remark:
          Starts on the next line.

See :restref:`field list reference
<restructuredtext.html#field-lists>`.

.. index::
   single: list; options

Options list
------------
E.g. for listing command line options.

.. list-table::
   :widths: 40, 60

   *
      - .. code-block:: ReST

           -v         An option
           -o file    Same with value
           --delta    A long option
           --delta=len  Same with value
           --option-name-is-long
              description on the next line.

      - -v         An option
        -o file    Same with value
        --delta    A long option
        --delta=len  Same with value
        --option-name-is-long
           description on the next line.


It is nice to align option descriptions, but not mandatory, but at
least two spaces must separate an option from the description.

.. index::
   !block
   single: block; literal
   literal block

Blocks
======

.. contents::
   :local:

.. _literal_block:

Literal Block
-------------

:restref:`rest literal blocks <restructuredtext.html#literal-blocks>`

A block which is not interpreted at all is preceded by a  paragraph
consisting of ``::``   and a blank line. The block must be indented.

The double ``::`` is removed from the output.

To use a specific formatting, you can use the
:ref:`code directive <rst-code>`

.. list-table::
   :widths: 50, 50

   *
      - .. code-block:: ReST


           Block one

           ::

              **No** interpretation of
              |special| characters.


      - Block one

        ::

           **No** interpretation of
           |special| characters.

You can also put the ``::`` at the end of the paragraph preceding the
block. When text immediately precedes the ``::`` the two colons are
displayed as ":", if there is a space before the colons they are
removed from the output.



.. list-table::
   :widths: 50, 50

   *
      - .. code-block:: ReST

           Block in condensed syntax::

             -  I'm not a list.

      - Block in condensed syntax::

          -  I'm not a list.

   *   - .. code-block:: ReST

            Another block! ::

               In the text body,
                  indentation is
               preserved

       - Another block! ::

            In the text body,
               indentation is
            preserved

.. warning::

   *Sphinx* use literal blocks to :ref:`highlight source code
   <code_highlighting>`, so ``**No**`` is still written
   with a  bold font by *Sphinx* while being not interpreted by
   *rst2html*.

   To disable *Pygment* decorations in *Sphinx* use a
   :ref:`code block <code_block>` in ``text`` language.

.. index::
   single: block; line
   single: quotes; line block

Line blocks
-----------

In a line block (:restref:`ref <restructuredtext.html#line-blocks>`)
every line is preceded with ``|`` and at least one space.


.. list-table::
   :widths: 50, 50

   *
      - .. code-block:: ReST

           | Line block
           | New line and we are still on
             the same line
           |   Yet a new line

      - | Line block
        | New line and we are still on
          the same line
        |   Yet a new line

.. index::
   pair: block; quotes
   !blockquote

.. _blockquote:

Block quote
-----------


::

   created by ... surrounding paragraph.

      Neither from itself nor from another,
      Nor from both,
      Nor without a cause,
      Does anything whatever, anywhere arise.

      --Nagarjuna - *Mulamadhyamakakarika*

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



.. code-block:: ReST

   .. pull-quote::

      Just as a solid ...

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

*don't forget the final* **s** *of highlights, or you fall down on the*
:ref:`Sphinx code highlighting directive <code_highlighting>`

.. code-block:: ReST

   .. highlights::

      With these *highlights* ...

.. highlights::

   With these *highlights* we have completed the ReST blocks.

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
.. code-block:: ReST

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


.. _class_directive:

Class
-----

.. code-block:: ReST

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

   Sphinx shadows the class directive, so the previous code will not
   have the expected result. In Sphinx you have to replace ``class``
   by ``rst-class``.


.. index::
   !table


Tables
======

.. contents::
   :local:

.. index::
   pair: table; simple


.. _simple_table:

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

.. _grid_table:

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

.. only:: latex

   .. tabularcolumns:: |p{0.15\linewidth}|p{0.15\linewidth}|p{0.15\linewidth}|

+--------+--------+-----------+
| Header | Header with 2 cols |
+========+========+===========+
| A      | Lists: | **C**     |
+--------+  - aha +-----------+
| B::    |  - yes | | a block |
|        |        |   of text |
|  *hey* |  #. hi | | a break |
+--------+--------+-----------+

.. index::
   table; emacs

You can edit them under emacs with ``table.el``
(but be careful about conflicts with ``rst-mode``) or
use *org tables* with ``orgtbl-mode`` and export to table with
``org-table-convert`` or ``org-table-create-with-table.el`` ( bound
to :kbd:`C-c ~` in ``org-mode``, but not in ``orgtbl-mode``)


.. index::
   triple: directive; table; csv

.. _csv_table:

csv table.
----------
.. sidebar:: Code

   .. code-block:: ReST

      .. csv-table:: Balance Sheet
         :header: Description,In,Out,Balance
         :widths: 20, 10, 10, 10
         :stub-columns: 1

         Travel,,230.00,-230.00
         Fees,,400.00,-630.00
         Grant,700.00,,70.00
         Train Fare,,70.00,**0.00**


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
file with the option ``:file:/path/of/the/file``.


.. index::
   triple: directive;  table; list

.. _list_table:

List Table.
-----------

A list-table (:restref:`ref <directives.html#list-table>`) is a two
level list, where the first level is a row and the second one a column
list. The number of column must be uniform (*no column span*) but
cell may contain structured markup.


.. code-block:: ReST

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
         -  9C
         -  10C
      ...


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

LaTeX table rendering.
----------------------

.. index::
   latex; tabulary

Rendering with *tabulary*.
^^^^^^^^^^^^^^^^^^^^^^^^^^
Sphinx use the latex package `tabulary
<http://ctan.org/tex-archive/macros/latex/contrib/tabulary/tabulary.pdf>`_
to render tables in laTeX.

Tabulary is an extension of the *tabular* package which calculate the
width of columns; it has four new formats specifications: ``LRCJ`` for
Left (Right, Centered, Justified) column with automatic width.

Sphinx uses by default ``L``, but you can override it with a directive
like::

    .. tabularcolumns:: |L|C|C|R|

As examples in this document the :ref:`source code directives table
<source_code_directives>` which has a proper Sphinx automatic rendering
in tabulary ``|L|L|``, which adapt the column size with a wider left one.

The two first :ref:`simple tables <simple_table>` the :ref:`csv table
<csv_table>` and the :ref:`list table <list_table>` are also
rendered in `tabulary` with a proper calculation of table width by
latex.

.. index::
   latex; tabular

Rendering with *tabular*.
^^^^^^^^^^^^^^^^^^^^^^^^^

Tables that contain any kind of lists, such as object descriptions,
blockquotes, or literal blocks are set by default with the `tabular
<http://en.wikibooks.org/wiki/LaTeX/Tables#The_tabular_environment>`_.
In sphinx prior version 1.6 the `:column:` option for list table is not
used for latex, and all  columns are of the same size.

You can tailor the rendering by giving `tabularcolumns` directive
which uses the `p{width}` column type.

Like this for three uneven columns:

.. code-block:: ReST

   .. tabularcolumns::
         |p{0.10\linewidth}|p{0.10\linewidth}|p{0.30\linewidth}|

Cross reference.
================

.. contents::
   :local:

.. index::
   hyperlink
   hypertext; link
   hypertext; target
   reference; cross
   reference; indirect

Hypertext link.
---------------

Hypertext links are constituted of a reference and a target.


And there are  three types of hyperlink targets:

1. An external hyperlink target is an URI or an email addresses like

   .. code-block:: ReST

      _Docutils: http://docutils.sourceforge.net/
      _John Lee: john.lee@gmail.com

2. An :ref:`internal document reference <internal>` point to some location in the same
   document.

3. An `indirect hyperlink`_ has an other hyperlink reference as target.


There exist three ways to write hyperlink references
(:restref:`ref<restructuredtext.html#hyperlink-references>`)

1. In  `Citation Style`_
2. Inline with an `Embedded URI`_ which gives in the same construct
   both the reference and the target.
3. In a `standalone hyperlink` the text of the target URI is used as
   reference.

.. index::
   reference; citation style

.. _citation style:

Reference in citation style.
----------------------------

.. code-block:: ReST

   A link to `Sphinx Home`_ in citation style.

   .. _Sphinx Home: http://sphinx.pocoo.org


A link to `Sphinx Home`_ in citation style ( :restref:`ref
<restructuredtext.html#hyperlink-targets>`).

In printed documents the link will be listed similar as a citation, as
opposed to HTML documents.

.. _reference name:

The reference is composed of words made of alphabetic and numeric
characters and characters in the set ``[,:_+-]`` *without double
hyphens*, separated by spaces. (:restref:`ref
<restructuredtext.html#reference-names>`)

The references are equivalents when they differ only by case or number of spaces. The
space character class include spaces, horizontal or vertical tabs, newlines, carriage
returns, or form feeds.

When the reference has no embedded spaces the backquotes are not
necessary:

.. code-block:: ReST

   A link to Sphinx_ in citation style.

If you want to use a |styledref|_ you have to use a
Replacement.

.. |styledref| replace:: *styled* reference
.. _styledref: `styled reference`_

.. _indirect hyperlink:

Indirect Hyperlink.
-------------------

If for the same hyperlink target you want to use a you want to use
many references you can use an *indirect hyperlink* or *indirect
reference*. With the following indirect references pocoo_, Sphinx_,
`The manual`_ and Documentation_ refer to the same place.

Like above don't forget backquotes when there are embedded
whitespaces.

.. code-block:: ReST

   .. _pocoo:  http://sphinx.pocoo.org
   .. _Sphinx: pocoo_
   .. _The manual: pocoo_
   .. _Documentation: `The manual`_

.. _Sphinx Home: http://sphinx.pocoo.org
.. _pocoo:  http://sphinx.pocoo.org
.. _Sphinx: pocoo_
.. _The manual: pocoo_
.. _Documentation: `The manual`_

Note that if you only want to have multiple link text with the same
target you can also use:

.. code-block:: ReST

   .. _Sphinx:
   .. _The manual:
   .. _pocoo:  http://sphinx.pocoo.org

Multiple adjacent hyperlink references
will  all point to the same target.

An indirect hyperlink can also be defined inline with  an `embedded alias`.

.. index::
   hyperlink; standalone

Standalone Hyperlink.
---------------------
Reference: :restref:`ref
<restructuredtext.html#standalone-hyperlink>`

.. list-table::

   * - .. code-block:: ReST

          | We may use URI like
            http://sphinx.pocoo.org or
          | an email address like
            project@sphinx.org

     - | We may use URI like
         http://sphinx.pocoo or
       | an email address like
         project@sphinx.org

.. index::
   reference; embedded
   reference; in-line
   hyperlink; embedded

.. _embedded uri:
.. _embedded alias:

Embedded URI and Aliases
------------------------

Reference: :restref:`ref
<restructuredtext.html#embedded-uris-and-aliases>`

You can directly embed an URI or a label in a reference enclosed in ``<``, ``>``
in the reference.

+--------------------------------------+--------------------------------------+
|.. code-block:: ReST                  |In-line versions are `Sphinx Home     |
|                                      |<http://sphinx.pocoo.org>`_.          |
|   In-line versions are `Sphinx Home  |                                      |
|   <http://sphinx.pocoo.org>`_        |                                      |
+--------------------------------------+--------------------------------------+

With the label ``internal`` which precede the following section we can use

.. list-table::

   * - .. code-block:: ReST

          `Internal target <internal>`_

     -  `Internal target <internal>`_

.. index::
   reference
   ref
   reference; target
   reference; label
   pair: internal; reference
   pair: option; name


.. _internal:


Internal document reference.
----------------------------

.. _explicit target:

To define ``label`` as label also called :restref:`explicit hyperlink target
<explicit-hyperlink-targets>`
for any text location internal to a document, precede the text location with:

.. code-block:: ReST

   .. _label:
   .. _other label:

plus a blank line.

A ``:name:`` option in any block is also an internal reference target.

You can also use :restref:`inline internal targets
<restructuredtext.html#inline-internal-targets>`

::

   which are a _`span of running text` in a paragraph.

.. _rest_ref:

The ReST way of referencing a label or :restref:`hyperlink targets
<restructuredtext.html#hyperlink-targets>` is:

.. code-block:: ReST

   label_ or `other label`_

.. index::
   hyperlink; implicit target
   implicit hyperlink

.. _implicit hyperlink:

Implicit Hyperlink Targets
--------------------------

Section titles, footnotes, and citations automatically are
:restref:`implicit hyperlink targets  <implicit hyperlink targets>`.
```Transition`_`` produces `Transition`_.

.. _indirect reference to an implicit target:

In pure ReST syntax you can reference the `Transition`_ section
as `how to draw an horizontal line`_ with
the hyperlink: ```how to draw an horizontal line`_`` and the
`indirect hyperlink`_:

.. code-block:: ReST

  .. _how to draw an horizontal line: Transition_

.. _how to draw an horizontal line: Transition_

You can also use them with an `embedded alias`_

.. list-table::

   * - .. code-block:: ReST

          | The `Transition section <Transition>`_ shows
          | `how to draw an horizontal line`_
            in your document.

     - | The `Transition section <Transition>`_ shows
       | `how to draw an horizontal line`_ in your document.

.. index::
   pair: hyperlink; anonymous

Anonymous Hyperlinks
--------------------

:restref:`Anonymous hyperlinks <anonymous-hyperlinks>` are hyperlinks where the target
has no label text but begins with double leading underscores, the reference itself ends
with two trailing underscores. The target are found by their sequential order in the
document. The reference number n, reference the target number n.

Example:

.. code-block:: ReST

   .. __: http://docutils.sourceforge.net/docs/ref/rst/

   The `ReST reference manual`__

.. __: http://docutils.sourceforge.net/docs/ref/rst/

The `ReST reference manual`__

The anonymous hyperlinks make the source text quite obscure, as the association between
reference and targets can only be seen by enumerating both. They break easily. Moving a
bloc of text with either a target or reference invalidate all anonymous hyperlinks of the
document. So it is wise to avoid them.

.. index:
   Sphinx reference; vs ReST
   ReST reference; vs Sphinx

.. _sphinx vs rest references:

Difference between ReST and Sphinx location reference
-----------------------------------------------------

Sphinx has its own *preferred syntax*,
it uses:

.. code-block:: ReST

   :ref:`displayed text <label>`

it is specific to Sphinx and you find it :ref:`in the Sphinx section
<sphinx_cross_references>`.

While ReST internal hyperlinks reference a target in the same document, Sphinx
allow linking across files of the same project.

.. _sphinx vs rest ref rendering:

These two syntax do not have the same rendering, the text of the target label is used by
ReST as default displayed text, while Sphinx syntax either need a reference displayed
text or when the target is preceding a section the name of the section is used as
default displayed text, the text of the label is never used by Sphinx to display the
link.

In this document there is two reference targets before the section *Sidebar and Topic*,
the next table show how they are rendered.

.. list-table::

   * - .. code-block:: ReST

          `Sidebar`_ versus `Topic`_

     -  `Sidebar`_ versus `Topic`_

   * - .. code-block:: ReST

          :ref:`Sidebar` versus :ref:`Topic`

     - :ref:`Sidebar` versus :ref:`Topic`


You cannot use the Sphinx ``:ref:`` syntax to reference
:restref:`implicit hyperlink targets <implicit hyperlink targets>`.
but there is an :ref:`autosectionlabel extension <autosectionlabel>` which provides
a label for each section across the whole project.

When using the Sphinx syntax it is easier to always define an :ref:`explicit target
<explicit target>`, which is also is more robust as a rewording of a section title will
not invalidate the document.

.. _explicit_markup:

Explicit Markup
===============
They all begin with two periods and a white space.

.. index::
   !footnote

Footnotes (:restref:`ref <restructuredtext.html#footnotes>`)
------------------------------------------------------------
To define a footnote numbered 2 you write it
``.. [2]`` precedes the definition of the footnote 2.  It is referenced by
``[2]_``. E.g.


.. list-table::
   :widths: 40, 60

   *
      - .. code-block:: ReST

           In the text [2]_.

           .. [2] In the footnote.

      - In the text [2]_.

        .. [2] In the footnote.

   *  - .. code-block:: ReST

           First automatic [#]_.
           Another automatic [#]_.

           .. [#] The first automatic.
           .. [#] The other automatic.

      - First automatic [#]_.
        Another automatic [#]_.

        .. [#] The first automatic.
        .. [#] The other automatic.

   *  - .. code-block:: ReST

           A labeled automatic [#one]_.
           Another of these [#two]_.

           .. [#one] footnote.
           .. [#two] labeled footnotes.

      - A labeled automatic [#one]_.
        Another of these [#two]_.

        .. [#one] footnote.
        .. [#two] labeled footnotes.

   *  - .. code-block:: ReST

           An autosymbol [*]_.
           More autosymbol [*]_.

           .. rubric:: Footnotes

           .. [*] Footnote in a *Footnotes*
              ``rubric`` at end of document.
           .. [*] other labeled footnote.

      - An autosymbol [*]_.
        More autosymbol [*]_.

        .. rubric:: Footnotes

        .. [*] Footnote in a *Footnotes*
               ``rubric`` at end of document.
        .. [*] other labeled footnote.


*Labeled footnotes are always numerics.*

.. index::
   !citation

Citations
---------
ref: :restref:`citations <restructuredtext.html#citations>` and
:restref:`citation references
<restructuredtext.html#citation-references>`

.. sidebar:: Code

   ::

      We cite [REL09]_ or REL09_
      or even rel09_.

      .. [REL09] Citation

``.. [REL2009]`` is followed by the definition of the citation
``REL2009``.  It is referenced as ``[REL2009]_`` or ``REL2009_``.
Citation labels are single word `reference name`_
and can contain underlines, hyphens and fullstops.  Case
is not significant. In Sphinx, definition and reference can reside in
different files.

We cite [REL09]_ or REL09_
or even rel09_.

.. [REL09] Citation

.. index::
   !directive
   directives; rest

.. _rest_directives:

Rest Directives
===============

.. contents::
   :local:

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


**Images** (:restref:`ref <directives.html#images>`)
are simple pictures, see also
:sphinx:`images in the Sphinx documentation <rest.html#images>`

.. for ulterior reference

   http://www.britishmuseum.org/system_pages/beta_collection_introduction/beta_collection_object_details.aspx?objectId=1650465&partId=1


.. code-block:: ReST

   .. image:: _static/NeoHittiteSphinx.svg
      :width: 120px
      :alt: Sphinx Neo-Hittite
      :target: https://it.wikipedia.org/wiki/Telepinu_(divinità)

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
<http://it.wikipedia.org/wiki/Telipinu_(divinità)>`_.

.. _figure:


A **figure** (:restref:`ref <directives.html#figure>`) add to an image
an optional caption and an optional legend.

.. code-block:: ReST

   .. figure:: _static/NeoHittiteSphinx.svg
       :width: 120px
       :alt: Sphinx Neo-Hittite

       Sphinx Neo-Hittite

       Telepinu is an `Hitite <http://en.wikipedia.org/wiki/Hittites>`_
       deity.


.. only:: not latex

   .. figure::_static/NeoHittiteSphinx.svg

.. only:: latex

   .. figure::  _static/NeoHittiteSphinx.pdf

   :width: 120px
   :alt: Sphinx Hittite

   Sphinx Hittite

   Telepinu is an `Hitite <http://en.wikipedia.org/wiki/Hittites>`_
   deity.

.. comment
   only:: latex

   .. figure:: _static/NeoHittiteSphinx.pdf
      :width: 120px
      :alt: Sphinx Hittite

      Sphinx Hittite

      Telepinu is an `Hitite <http://en.wikipedia.org/wiki/Hittites>`_
      deity.

`Other options <ReST image directive>`_ are:

-  ``:scale: <integer percentage>``,
-  ``:align: {top|middle|bottom|left|right}``

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
The conversion can be done with  Inkscape, it can be automated as
`explained by Johan B. C. Engelen
<http://ctan.tug.org/tex-archive/info/svg-inkscape/InkscapePDFLaTeX.pdf>`_.
You can also use the `ipe drawing editor
<http://ipe7.sourceforge.net/>`_.


.. index::
   pair: code; directive
   pair: code-block; directive
   pair: sourcecode; directive

.. _rst-code:

Code blocks
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

.. _replacement:

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

Replacements
------------
ReST references:
:restref:`replace directive
<directives.html#replacement-text>`,
:restref:`unicode directive
<directives.html#unicode-character-codes>`,
:restref:`date directive
<directives.html#date>`,
:restref:`substitution definitions (specification)
<restructuredtext.html#substitution-definitions>`,
:restref:`substitution definition (definition files)
<definitions.html#substitution-definitions>`,
:restref:`Character Entity Sets
<definitions.html#character-entity-sets>`.

See also: `docutil FAQ: How can I represent esoteric characters?
<http://docutils.sourceforge.net/FAQ.html#how-can-i-represent-esoteric-characters-e-g-character-entities-in-a-document>`_.

General replacements:

.. list-table::
   :widths: 50, 50

   *  - .. code-block:: ReST

           This example is |stupid|

           .. |stupid| replace:: not so clever

      - This example is |stupid|

        .. |stupid| replace:: not so clever

.. _styled reference:

One use of replacements is to create styled reference.

If we are not satisfied by a reference like:
`more in ReST directives manual`_ that you get with

.. code-block:: ReST

   .. _ more in ReST directives manual:
        http://docutils.sourceforge.net/doc...

but you want to get: |more-doc|_.

You use the replacement:

.. code-block:: ReST

   ... want to get: |more-doc|_.

   .. |more-doc| replace::  *more in* **reST** *directives manual*
   .. _more-doc: http://docutils.sourceforge.net/doc...

We also use substitutions to include unicode characters like |copy|
with:

.. code-block:: ReST

   .. |copy|   unicode:: U+000A9 .. COPYRIGHT SIGN

If you use Sphinx there are also three :sphinx:`predefined substitutions
<markup/inline.html#substitutions>`:
``|release|``, ``|version|``, ``|today|``.

.. |more-doc| replace::  *more in* **reST** *directives manual*
.. _more in ReST directives manual:
.. _more-doc: http://docutils.sourceforge.net/docs/ref/rst/directives.html#replacement-text
.. |copy|   unicode:: U+000A9 .. COPYRIGHT SIGN

.. index::
   pair: include; directive
   file include

.. _file_include:

file includes
-------------
To include a ReST file use::

.. include:: subdir/incl.rst

You can put the file wherever you want the relative paths are
interpreted relative to the source directory.

The options: ``start-line``, ``end-line``, ``start-after``, ``end-before``
as referenced in :restref:`reST Directives
<directives.html#including-an-external-document-fragment>`.

If you use ``include`` with Sphinx, you should exclude the included
files from the source file lookup, by setting in ``conf.py`` the value
`exclude_patterns <config.html#confval-exclude_patterns>` to a glob
pattern in like::

   exclude_patterns = ["include/**"]

For including source code in Sphinx rather use the Sphinx directive
:ref:`literalinclude <source_code_include>`.

.. index::
   sidebar
   topic

.. _sidebar:

.. _topic:

Sidebar and Topic.
------------------

A :restref:`sidebar <directives.html#sidebar>` or a :restref:`topic
<directives.html#topic>` are treated like documents on their own::

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

Rubric
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

Everything starting like a directive with two periods and a space but
not a valid construct is a comment. The comment consume all indented
text following it. To avoid a confusion with an other constructs, you can
let the first line of a block comment empty except the two periods.

When the two dots are not followed by any text, but a blank line, this
is an empty comment, that will not consume a following indented block.
Empty comments are used to terminate a preceding construct.

.. code-block:: ReST

   .. One line comment

   ..
      A longer comment example
      more comment

      Still in comment

   ..

      Here is a block-quote,
      not a comment anymore


.. One line comment

..
   A longer comment example
   more comment

   Still in comment

..

   Here is a block-quote,
   not a comment anymore


.. _common_options:

.. index:
   pair: option; name
   pair: option; class

.. _name-option:

Common options
--------------
ref: `Directives Common Options
<http://docutils.sourceforge.net/docs/ref/rst/directives.html#common-options>`_

The class options ``:class:`` and ``:name:``
are supported by most of the directives.

In the following :ref:`topic <topic>` and `autre <#topic>`_ the ``:name:`` act as a
reference target. Here we can refer to the following block as `say-no-more`_.

.. code-block:: ReST

   .. topic:: The end
      :class: exceptional
      :name: say-no-more

      A final word.

The ``class`` render in html as:

.. code-block:: html

  <div class="exceptional topic" id="say-no-more">
  <p class="topic-title first">the end</p>
  <p>A final word.</p>
  </div>

.. topic:: the end
   :class: exceptional
   :name: say-no-more

   A final word.
