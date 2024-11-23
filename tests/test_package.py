from __future__ import annotations

import subprocess
from datetime import datetime

import docx_comments as m
from dateutil import parser
from dateutil.tz import tzutc


def test_version():
    assert m.__version__


def test_comments():
    comments = m.get_comments("tests/data/test_document.docx")
    assert len(comments) == 3
    c1 = comments[0]
    assert c1["text"] == "This is a test comment"
    assert c1["author"] == "Unknown Author"
    date = parser.parse(c1["date"])
    assert date == datetime(2022, 7, 16, 13, 1, 52, tzinfo=tzutc())
    assert comments[1]["text"] == "Test2"


def test_dump_comments(tmp_path):
    test_out = tmp_path / "test.txt"

    subprocess.run(
        [
            "dump_comments",
            "tests/data/test_document.docx",
            test_out,
        ],
        check=True,
    )
    with open("tests/data/test_comments.txt") as f:
        correct_text = f.read()
    with open(test_out) as f:
        output_text = f.read()
    assert correct_text == output_text


def test_dump_sort(tmp_path):
    """Test that comments are sorted."""
    test_out = tmp_path / "test.txt"

    subprocess.run(
        ["dump_comments", "tests/data/test_document.docx", test_out, "-s"],
        check=True,
    )
    with open(test_out) as f:
        lines = f.readlines()
    assert lines == ["Test2\n", "Test2\n", "This is a test comment\n"]


def test_dump_dedupe(tmp_path):
    """Test de-duplicate for dump_comments."""
    test_out = tmp_path / "test.txt"

    subprocess.run(
        ["dump_comments", "tests/data/test_document.docx", test_out, "-d"],
        check=True,
    )
    with open(test_out) as f:
        lines = f.readlines()
    assert lines == ["This is a test comment\n", "Test2\n"]
