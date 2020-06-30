#!/usr/bin/env python
from google import search
import csv
import random

array_of_q = []

with open("Keywords - Sample.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        array_of_q.append(row[1])

for i in array_of_q:
    num = 0
    for url in search(i, stop=10, pause=random.randint(1,3)):
        num += 1
        with open("output.csv", "a") as w:
            writer = csv.writer(w)
            row = [str(i), str(num), str(url)]
            print(row)
            writer.writerow(row)
