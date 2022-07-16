"""Get comments from Word document."""

from __future__ import annotations

import zipfile
from pathlib import Path

import click
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
    with zipfile.ZipFile(file_name, "r") as docx_zip:
        comments_xml = docx_zip.read("word/comments.xml")
    comments = etree.XML(comments_xml).xpath("//w:comment", namespaces=ooxml_namespaces)
    comments_parsed = [
        {
            "author": c.xpath("@w:author", namespaces=ooxml_namespaces)[0],
            "date": c.xpath("@w:date", namespaces=ooxml_namespaces)[0],
            "text": c.xpath("string(.)", namespaces=ooxml_namespaces),
        }
        for c in comments
    ]
    return comments_parsed


@click.command()
@click.argument("in_file")
@click.argument("out_file")
def dump_comments(in_file: str, out_file: str) -> None:
    """Dump comment texts from a Word file to a .txt file.

    Arguments:

    in_file : Input Word file

    out_file :  Output text file
    """  # noqa: D
    comments = get_comments(in_file)
    with open(out_file, "w") as f:
        f.writelines(c["text"] + "\n" for c in comments)
