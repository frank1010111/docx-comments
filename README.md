# docx-comments

[![Code style: black][black-badge]][black-link][![GitHub Discussion][github-discussions-badge]][github-discussions-link]

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
pipx run dump_comments <input_file.docx> <output_file.txt>
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
[conda-link]:               https://github.com/conda-forge/docx-comments-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/frank10101111/docx-comments/discussions
[gitter-badge]:             https://badges.gitter.im/https://github.com/frank10101111/docx-comments/community.svg
[gitter-link]:              https://gitter.im/https://github.com/frank10101111/docx-comments/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
[pypi-link]:                https://pypi.org/project/docx-comments/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/docx-comments
[pypi-version]:             https://badge.fury.io/py/docx-comments.svg
[rtd-badge]:                https://readthedocs.org/projects/docx-comments/badge/?version=latest
[rtd-link]:                 https://docx-comments.readthedocs.io/en/latest/?badge=latest
[sk-badge]:                 https://scikit-hep.org/assets/images/Scikit--HEP-Project-blue.svg
<!-- prettier-ignore-end -->
