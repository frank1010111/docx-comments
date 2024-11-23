"""Get comments from a Word document."""

from __future__ import annotations

import click
from docx_comments._core import get_comments


@click.command()
@click.argument("in_file", type=click.Path(exists=True))
@click.argument("out_file", type=click.Path(writable=True))
@click.option(
    "--sort", "-s", "sorted", is_flag=True, help="sort comments alphabetically"
)
@click.option(
    "-d",
    "--remove-duplicates",
    "remove_duplicates",
    is_flag=True,
    help="remove duplicate comments",
)
def dump_comments(
    in_file: str, out_file: str, sorted: bool = False, remove_duplicates: bool = False
) -> None:
    """Dump comment texts from a Word file (IN_FILE) to a .txt file (OUT_FILE)."""
    comments = get_comments(in_file)
    texts = [c["text"] for c in comments]
    if sorted:
        texts.sort()
    if remove_duplicates:
        texts = list(dict.fromkeys(texts))
    with open(out_file, "w", encoding="utf-8") as f:
        f.writelines([t + "\n" for t in texts])
