************
 References
************



Sphinx and Rest References
==========================

-  This doc began as a fork of a 2011 version of `Cristoph Reller reST Memo
   <http://aert-notes-dev.readthedocs.org/en/latest/content/rest/>`_
   which is now part of his `Programming Notes
   <http://aert-notes-dev.readthedocs.io/en/latest/>`_. I
   adapted it according to my needs, and they have largely diverged
   now, but it still inherits from some content and layout.
-  :sphinx:`Sphinx documentation <contents.html>`
-  :sphinx:`Sphinx reStructuredText Primer <rest.html>`
-  `Documenting Your Project Using
   Sphinx <http://packages.python.org/an_example_pypi_project/sphinx.html>`_
   from `an example pypi project’s
   <http://packages.python.org/an_example_pypi_project/>`_
-  Thomas Cokelaer `Openalea project: How to use sphinx ?
   <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/sphinx.html>`_
   and
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
-  `Documenting Python`_
   in the `Python Developer’s Guide <http://docs.python.org/devguide/>`_
-  `sampledoc tutorial <http://matplotlib.sourceforge.net/sampledoc/>`_
   from `matplotlib <http://matplotlib.sourceforge.neti/>`_
   *a python 2D plotting library*.
-  `rst2pdf <http://code.google.com/p/rst2pdf/>`_ is a
   tool for transforming reStructuredText to PDF using ReportLab.
   It supports Sphinx formatting.
-  `Epydoc reST markup <http://epydoc.sourceforge.net/manual-othermarkup.html>`_

How to write docstrings
=======================

-  Look at examples in `Official list of projects using Sphinx
   <http://sphinx.pocoo.org/examples.html>`_
-  `Documenting Python`_ use Sphinx in
   `function definitions
   <http://packages.python.org/an_example_pypi_project/sphinx.html#function-definitions>`_
   it prefers to the pure Sphinx Syntax the `Google style guide`_
   that is used in `Full Code Example
   <http://packages.python.org/an_example_pypi_project/sphinx.html#full-code-example>`_
-  `OpenAlea
   <http://openalea.gforge.inria.fr/wiki/doku.php?id=documentation:doctests:how_to_document_python_api>`_
   has a nice `comparaison of three ways of filling the docstring
   <http://openalea.gforge.inria.fr/wiki/doku.php?id=documentation:doctests:sphinx_proposal#filling_the_docstring>`_.
   which compare *Pure sphinx code*, *restructuredText and Sphinx*,
   *Numpy style*. But it predates the *Napoleon* extension, so the
   cause of rejecting Numpy may be no longer valid.
   The source is  `template.py
   <https://gforge.inria.fr/scm/viewvc.php/trunk/doc/source/sphinx/template.py?view=markup&root=openalea>`_
-  `Google style guide`_.
-  `NumPy style guide`_.
-  Sources of
   `mongo python driver
   <https://github.com/mongodb/mongo-python-driver>`_
   are also a good example

Extending Sphinx
================

-  `Sphinx Tutorial: Writing a simple extension
   <http://sphinx.pocoo.org/ext/tutorial.html>`_.
-  `Creating Custom Link Roles
   <http://protips.readthedocs.io/link-roles.html>`_.
-  `Defining Custom Roles in Sphinx
   <https://doughellmann.com/blog/2010/05/09/defining-custom-roles-in-sphinx/>`_
   a  `Sphinx blog post by Doug Hellmann
   <https://doughellmann.com/blog/>`_
-  :restref:`Creating Interpreted Text Roles
   <rst-roles.html>`
   from docutils project.
-  :restref:`Creating reStructuredText Directives
   <rst-directives.html>`
   from docutils project.


.. include:: include/commonref.rst

.. local variables

   Local Variables:
   mode: rst
   ispell-local-dictionary: "english"
   End:
