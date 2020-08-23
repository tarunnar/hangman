import json
import csv
with open("quotes.json") as fp, open("sample.csv", "w") as sample:
    quotes = json.load(fp)
    fieldnames = ['quote']
    writer = csv.DictWriter(sample, fieldnames=fieldnames)
    writer.writeheader()
    st = set()
    for quote in quotes:
        first_part = quote["Quote"].split('.')[0]
        removed = first_part.replace(" ", "").replace("'", "").replace(",", "").replace("-", "")
        if removed in st:
            continue
        writer.writerow({"quote": removed})
        st.add(removed)
