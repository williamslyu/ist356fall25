from datetime import datetime


date_str = "1/15/2025"

parsed_date = datetime.strptime(date_str, "%m/%d/%Y")

formatted_date = parsed_date.strftime("%Y-%m-%d")

print(formatted_date)
