import sys
import subprocess
subprocess.check_call([sys.executable, "-m", "pip", "install", "seaborn==0.11.2"])

import argparse
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
parser = argparse.ArgumentParser("save_correlation")
parser.add_argument("--data_set_cleaned", type=str, help="Path of dataset cleaned")
parser.add_argument("--correlation_img", type=str, help="Path of output correlation img")

args = parser.parse_args()

print("Hola desde img...")

lines = [
    f"data_set_cleaned path: {args.data_set_cleaned}",
    f"correlation_img output path: {args.correlation_img}",
]

for line in lines:
    print(line)

data = pd.read_csv(args.data_set_cleaned)
# Calculate the correlation matrix
correlation_matrix = data.corr(method='pearson')

# Create a pair plot
sns.set(style="ticks")
sns.pairplot(data, diag_kind='kde')
plt.suptitle("Pair Plot of Columns")

output_path = args.correlation_img
print(output_path)

plt.savefig(output_path, format="jpg")


