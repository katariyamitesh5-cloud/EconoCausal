import importlib

print("WEEK 1 LIBRARY REVIEW")
print("=" * 30)

# Required libraries
libraries = [
    "pandas",
    "numpy",
    "sklearn",
    "matplotlib",
    "seaborn",
    "dowhy"
]

print("\nChecking required libraries:")

installed = []
missing = []

for library in libraries:

    try:
        importlib.import_module(library)
        installed.append(library)
        print("[OK]", library)

    except ImportError:
        missing.append(library)
        print("[MISSING]", library)

print("\nLibrary Summary")
print("-" * 20)

print("Installed:", len(installed))
print("Missing:", len(missing))

if missing:
    print("\nInstall missing libraries using:")
    print("pip install " + " ".join(missing))
else:
    print("\nAll required libraries are installed.")

print("\nLibrary review completed.")