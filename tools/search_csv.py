import csv

def search_csv(keyword, path="data/data.csv"):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader if keyword.lower() in str(row).lower()]
