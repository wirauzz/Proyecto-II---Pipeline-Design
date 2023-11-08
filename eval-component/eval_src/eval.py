import argparse
from pathlib import Path
import pandas as pd
import csv
from sklearn.metrics import classification_report

parser = argparse.ArgumentParser("eval")
parser.add_argument("--scoring_result", type=str, help="Path of scoring result")
parser.add_argument("--y_test", type=str, help="Path of y_test")
parser.add_argument("--eval_output", type=str, help="Path of output evaluation result")

args = parser.parse_args()

print("Hola desde eval...")

lines = [
    f"Scoring result path: {args.scoring_result}",
    f"y_test path: {args.y_test}",
    f"Evaluation output path: {args.eval_output}",
]

for line in lines:
    print(line)

y_test = pd.read_csv(args.y_test)

y_pred = []
with open(args.scoring_result, 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        y_pred = [int(value) for value in row]

report = classification_report(y_test, y_pred, target_names=["Not Potable", "Potable"], output_dict=True)
df = pd.DataFrame(report)
df = df.transpose()
df.to_csv(args.eval_output)