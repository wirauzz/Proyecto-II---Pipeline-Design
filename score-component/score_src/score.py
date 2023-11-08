import argparse
from pathlib import Path
import pickle
import pandas as pd
import csv

parser = argparse.ArgumentParser("score")
parser.add_argument("--model_input", type=str, help="Path of input model")
parser.add_argument("--x_test", type=str, help="Path to x_test data")
parser.add_argument("--y_pred", type=str, help="Path of scoring output")

args = parser.parse_args()

print("Hola desde score...")

lines = [
    f"Model path: {args.model_input}",
    f"Test data path: {args.x_test}",
    f"Scoring output path: {args.y_pred}",
]

for line in lines:
    print(line)

x_test = pd.read_csv(args.x_test)

dt = pickle.load(open(args.model_input, "rb"))

y_pred=dt.predict(x_test)

with open(args.y_pred, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(y_pred)