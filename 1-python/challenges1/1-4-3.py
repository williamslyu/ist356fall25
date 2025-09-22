# dateutils.py
from datetime import datetime




def parsedate_mdy(text: str) -> datetime:
    return datetime.strptime(text, "%m/%d/%Y")


def formatdate_ymd(date: datetime) -> str:
    return date.strftime("%Y-%m-%d")

# 1-4-3.py

def main():
    text = input("Enter a date (M/D/YYYY): ")
    date_obj = parsedate_mdy(text)
    formatted = formatdate_ymd(date_obj)
    print(formatted)

if __name__ == "__main__":
    main()

