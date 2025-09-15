from datetime import date

today = date.today()
year = today.year
iso_year = today.isocalendar()[0]

print(f"today: {today}")

print(f'year: {year}')
print(f'iso_year: {iso_year}')
