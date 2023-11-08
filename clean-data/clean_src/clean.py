import argparse
from pathlib import Path
import pandas as pd

parser = argparse.ArgumentParser("clean")
parser.add_argument("--standard_data", type=str, help="Path of dataset standard")
parser.add_argument("--cleaned_data", type=str, help="Path of output data cleaned")

args = parser.parse_args()

lines = [
    f"standard_data input path: {args.standard_data}",
    f"cleaned_data output path: {args.cleaned_data}",
]

for line in lines:
    print(line)


data = pd.read_csv(args.standard_data)
# Replace null values with the mean of each column
data = data.fillna(data.mean())

data.to_csv(args.cleaned_data, index=False)
