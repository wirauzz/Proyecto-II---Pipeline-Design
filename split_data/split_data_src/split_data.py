import argparse
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

parser = argparse.ArgumentParser("split_data")
parser.add_argument("--data_set_cleaned", type=str, help="Path of dataset cleaned")
parser.add_argument("--split_ratio_train", type=float, help="Split ratio for train")
parser.add_argument("--x_train", type=str, help="Path of output x_train")
parser.add_argument("--y_train", type=str, help="Path of output y_train")
parser.add_argument("--x_test", type=str, help="Path of output x_test")
parser.add_argument("--y_test", type=str, help="Path of output y_test")

args = parser.parse_args()

print("Hola desde split...")

lines = [
    f"data_set_cleaned path: {args.data_set_cleaned}",
    f"split_ratio_train path: {args.split_ratio_train}",
    f"x_train output path: {args.x_train}",
    f"y_train output path: {args.y_train}",
    f"x_test output path: {args.x_test}",
    f"y_test output path: {args.y_test}",
]

for line in lines:
    print(line)

data = pd.read_csv(args.data_set_cleaned)

# Dependent vs Independent Variables
X = data.drop(columns=['Potability'])
y = data['Potability']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=args.split_ratio_train, random_state=1342)

X_train.to_csv(args.x_train, index=False)
y_train.to_csv(args.y_train, index=False)
X_test.to_csv(args.x_test, index=False)
y_test.to_csv(args.y_test, index=False)