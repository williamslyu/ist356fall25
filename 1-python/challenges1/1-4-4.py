from datetime import datetime

def parsedate_mdy(text: str) -> datetime:
    return datetime.strptime(text.strip(), "%m/%d/%Y")

def formatdate_ymd(date: datetime) -> str:
    return date.strftime("%Y-%m-%d")

# ------------------------------
# Tests for pytest
# ------------------------------

def test_parsedate_mdy():
    d1 = parsedate_mdy("1/15/2025")
    assert d1 == datetime(2025, 1, 15)

    d2 = parsedate_mdy("01/05/2025")
    assert d2 == datetime(2025, 1, 5)

def test_formatdate_ymd():
    d = datetime(2025, 1, 15)
    assert formatdate_ymd(d) == "2025-01-15"

    d2 = datetime(2023, 12, 31)
    assert formatdate_ymd(d2) == "2023-12-31"
