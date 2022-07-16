from __future__ import annotations

from datetime import datetime

from dateutil import parser
from dateutil.tz import tzutc

import docx_comments as m


def test_version():
    assert m.__version__


def test_comments():
    comments = m.get_comments("tests/data/test_document.docx")
    assert len(comments) == 2
    c1 = comments[0]
    assert c1["text"] == "This is a test comment"
    assert c1["author"] == "Unknown Author"
    date = parser.parse(c1["date"])
    assert date == datetime(2022, 7, 16, 13, 1, 52, tzinfo=tzutc())
    assert comments[1]["text"] == "test2"
