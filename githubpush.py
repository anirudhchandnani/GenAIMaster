import os
import random
import subprocess
from datetime import date

# Define the repository URL
repo_url = "https://github.com/anirudhchandnani/GenAIMaster.git"

# Set the path to your local clone of the repository
local_repo_path = r"C:\Users\LENOVO\Desktop\work\github"

# Change to the local repository directory
os.chdir(local_repo_path)

# Create a random change in a Python file
random_value = random.randint(1, 100)
file_to_modify = "hello.py"  # Change this to the actual file you want to modify
with open(file_to_modify, "a") as file:
    file.write(f"\n# Random change: {random_value} ({date.today()})")

# Commit and push the change
commit_message = f"Daily random change: {random_value} ({date.today()})"
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", commit_message])
subprocess.run(["git", "push", "origin", "main"])

print(f"Pushed a random change to {repo_url}")