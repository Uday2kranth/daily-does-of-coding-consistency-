import pip

# List of libraries to install
libraries = ["requests", "tk", "plotly"]

for lib in libraries:
    try:
        # Call pip.main with the install command and the library name
        # The '--quiet' flag can be added to suppress output
        pip.main(['install', lib, '--quiet'])
        print(f"Successfully installed {lib}")
    except Exception as e:
        print(f"An error occurred during installation of {lib}: {e}")

# for lib in libraries:
#     try:
#         # Call pip.main with the install command and the library name
#         # The '--quiet' flag can be added to suppress output
#         pip.main(['uninstall', lib, '--quiet'])
#         print(f"Successfully installed {lib}")
#     except Exception as e:
#         print(f"An error occurred during installation of {lib}: {e}")


# def upgrade_pip():
#     print("Checking for pip upgrades...")
#     try:
#         subprocess.check_call([
#             sys.executable, 
#             "-m", 
#             "pip", 
#             "install", 
#             "--upgrade", 
#             "pip"
#         ])
#     except subprocess.CalledProcessError:
#         print("Could not upgrade pip.")

# # Run this BEFORE your other installations
# upgrade_pip()