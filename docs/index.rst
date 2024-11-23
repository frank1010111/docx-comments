
Welcome to docx-comments!
=========================

Introduction
------------

Docx-comments takes word comments and outputs them to a text file for you. The best way to start is...


.. code :: bash

   uv tool install git+https://github.com/frank1010111/docx-comments.git
   dump_comments <your-file-here.docx>

If you prefer pip or pipx, you can use them in the same way.

.. toctree::
   :maxdepth: 3
   :titlesonly:
   :caption: Contents
   :glob:

API
---
.. automodule:: docx_comments
   :members:

CLI
---

The CLI is how you'll probably use this package.

.. code:: bash

   $ dump_comments --help
   Usage: dump_comments [OPTIONS] IN_FILE OUT_FILE

   Dump comment texts from a Word file (IN_FILE) to a .txt file (OUT_FILE).

   Options:
   -s, --sort               sort comments alphabetically
   -d, --remove-duplicates  remove duplicate comments
   --help                   Show this message and exit.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
