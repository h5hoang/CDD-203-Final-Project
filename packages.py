import subprocess
import sys

packages = [
    "pandas",
    "numpy",
    "PyTDC",
    "rdkit",
    "scikit-learn",
    "seaborn"
]

def install_packages():
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# run this script file!!!!
if __name__ == "__main__":
    install_packages()
