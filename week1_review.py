import os

print("WEEK 1 PROJECT REVIEW")
print("=" * 30)

# Main project files
files = [
    "README.md",
    "requirements.txt",
    "preprocessing.py",
    "causal_graph.py"
]

print("\nChecking project files:")

for file in files:
    if os.path.exists(file):
        print("[OK]", file)
    else:
        print("[MISSING]", file)

# Check data folder
print("\nChecking data folder:")

if os.path.exists("data"):
    print("[OK] data folder")

    for file in os.listdir("data"):
        print(" -", file)
else:
    print("[MISSING] data folder")

# Check Python files
print("\nPython files:")

for file in os.listdir("."):
    if file.endswith(".py"):
        print(" -", file)

print("\nProject structure review completed.")