# Virtual Environment in Python
# 1. What is it?

# A virtual environment (venv) is an isolated environment for Python projects.

# Each project can have its own dependencies, without affecting others.

# 2. Why use it?

# Prevents dependency conflicts between projects.

# Different projects can use different library versions.

# Keeps the global Python installation clean.

# 3. Create Virtual Environment
# # Create
# python -m venv myenv

# 4. Activate

# Windows (cmd/PowerShell):

# myenv\Scripts\activate


# Linux/Mac:

# source myenv/bin/activate

# 5. Deactivate
# deactivate

# 6. Install Packages
# pip install requests


# (Packages install inside venv, not globally)

# 7. Common Interview Q&A
# Q	A
# What is a virtual environment?	Isolated environment for Python projects, with separate dependencies.
# Why use venv?	To avoid dependency/version conflicts between projects.
# Difference between venv and virtualenv?	venv is built-in (since Python 3.3); virtualenv is an external package, older & more feature-rich.
# How to check if venv is active?	Prompt shows environment name (e.g., (myenv) before path).
# Where are packages installed in venv?	Inside myenv/lib/site-packages (or Lib\site-packages on Windows).

# ⚡ Shortcut memory hook →
# 👉 python -m venv env → activate → install packages → deactivate.