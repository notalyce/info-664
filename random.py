import csv
import random

filename = "release_data_styles.csv"

with open(filename) as f:
    reader = csv.reader(f)
    chosen_row = random.choice(list(reader))
    print(chosen_row)