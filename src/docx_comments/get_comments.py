# get_comments.py
"""Get comments from Word document."""

from __future__ import annotations

import zipfile
from pathlib import Path

from lxml import etree

ooxml_namespaces = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def get_comments(file_name: str | Path) -> list[dict[str, str]]:
    """Extract comments from Word file.

    Parameters
    ----------
    file_name : str | Path
        location of the file

    Returns
    -------
    list[dict[str,str]]
        list of comments with author, date, and text gathered

    References
    ----------
    https://stackoverflow.com/questions/47390928/extract-docx-comments
    """
    docx_zip = zipfile.ZipFile(file_name)
    comments_xml = docx_zip.read("word/comments.xml")
    comments = etree.XML(comments_xml).xpath("//w:comment", namespaces=ooxml_namespaces)
    comments_parsed = [
        {
            "author": c.xpath("@w:author", namespaces=ooxml_namespaces),
            "date": c.xpath("@w:date", namespaces=ooxml_namespaces),
            "text": c.xpath("string(.)", namespaces=ooxml_namespaces),
        }
        for c in comments
    ]
    return comments_parsed


# @click
