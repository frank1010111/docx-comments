# docx-comments

[![License][license-badge]][license-link]
[![Python version][python-badge]][python-link]

[![Code-cov][codecov-badge]][codecov-link]
[![Code style: black][black-badge]][black-link]
[![Pre-commit][pre-commit-badge]][pre-commit-link]

Extract comments from Word files. This is mostly meant as a script to put
comments in a text file.

To install, use one of these commands

**acceptable:**

```
pip install git+https://github.com/frank1010111/docx-comments.git
```

**better:**

```
pipx install git+https://github.com/frank1010111/docx-comments.git
```

**best:**

```
uv tool install git+https://github.com/frank1010111/docx-comments.git
```

Then, to run

```
dump_comments <input_file.docx> <output_file.txt>
```

This was inspired by a mildly entertaining personal story and `khjughes`'s
answer to someone with a similar issue on
[StackOverflow](https://stackoverflow.com/questions/47390928/extract-docx-comments).

<!-- prettier-ignore-start -->
[black-badge]:              https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]:               https://github.com/psf/black
[license-badge]:            https://img.shields.io/badge/License-BSD_3--Clause-orange.svg
[license-link]:             https://opensource.org/licenses/BSD-3-Clause
[codecov-badge]:            https://codecov.io/gh/frank1010111/docx-comments/branch/main/graph/badge.svg?token=ZWEQSAXJIH
[codecov-link]:             https://codecov.io/gh/frank1010111/docx-comments
[pre-commit-badge]:         https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit-link]:          https://github.com/pre-commit/pre-commit
[python-badge]:             https://img.shields.io/badge/Python-3.9_--_3.13-blue
[python-link]:              https://www.python.org/downloads/
<!-- prettier-ignore-end -->
