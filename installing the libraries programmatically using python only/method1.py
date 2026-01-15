import subprocess
import sys

# List of libraries to install
libraries = ["requests", "numpy", "pandas"]

for lib in libraries:
    try:
        # Use sys.executable to ensure the correct python interpreter is used
        # The '-m pip install' runs the pip module
        # The '--quiet' flag suppresses most output, providing a silent installation
        subprocess.check_call([sys.executable, "-m", "pip", "install", lib, "--quiet"])
        print(f"Successfully installed {lib}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {lib}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while installing {lib}: {e}")
