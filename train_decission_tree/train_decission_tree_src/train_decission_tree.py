import argparse
from pathlib import Path
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

parser = argparse.ArgumentParser("train_decission_tree")
parser.add_argument("--x_train", type=str, help="Path of input x_train")
parser.add_argument("--y_train", type=str, help="Path of input y_train")
parser.add_argument("--model_output", type=str, help="Path of output model_output")

args = parser.parse_args()

print("Hola desde train tree...")

lines = [
    f"x_train input path: {args.x_train}",
    f"y_train input path: {args.y_train}",
    f"model_output output path: {args.model_output}",
]

for line in lines:
    print(line)

x_train = pd.read_csv(args.x_train)
y_train = pd.read_csv(args.y_train)

# train model decission tree
dt = DecisionTreeClassifier(criterion= 'entropy', min_samples_split= 3, max_depth=4)
dt.fit(x_train,y_train)

# save model
pickle.dump(dt, open(args.model_output, "wb"))

