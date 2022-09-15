# docx-comments

[![License][license-badge]][license-link]
[![Python version][python-badge]][python-link]

[![Code-cov][codecov-badge]][codecov-link]
[![Code style: black][black-badge]][black-link]
[![Pre-commit][pre-commit-badge]][pre-commit-link]

Extract comments from Word files. This is mostly meant as a script to put
comments in a text file.

To install and run

```
pip install git+https://github.com/frank1010111/docx-comments.git
dump_comments <input_file.docx> <output_file.txt>
```

or, better,

```
pipx install git+https://github.com/frank1010111/docx-comments.git
dump_comments <input_file.docx> <output_file.txt>
```

This was inspired by a mildly entertaining personal story and `khjughes`'s
answer to someone with a similar issue on
[StackOverflow](https://stackoverflow.com/questions/47390928/extract-docx-comments).

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/frank10101111/docx-comments/workflows/CI/badge.svg
[actions-link]:             https://github.com/frank10101111/docx-comments/actions
[black-badge]:              https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]:               https://github.com/psf/black
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/docx-comments
[sk-badge]:                 https://scikit-hep.org/assets/images/Scikit--HEP-Project-blue.svg
[license-badge]:            https://img.shields.io/badge/License-BSD_3--Clause-orange.svg
[license-link]:             https://opensource.org/licenses/BSD-3-Clause
[codecov-badge]:            https://codecov.io/gh/frank1010111/docx-comments/branch/main/graph/badge.svg?token=ZWEQSAXJIH
[codecov-link]:             https://codecov.io/gh/frank1010111/docx-comments
[pre-commit-badge]:         https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit-link]:          https://github.com/pre-commit/pre-commit
[python-badge]:             https://img.shields.io/badge/Python-3.8%2C%203.9%2C%203.10-blue
[python-link]:              https://www.python.org/downloads/
<!-- prettier-ignore-end -->
