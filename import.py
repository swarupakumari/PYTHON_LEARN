# How import Works in Python
# 1. Purpose

# import lets you reuse code by bringing in modules (Python files, libraries, or packages).

# 2. Import Mechanism (Steps)

# When Python sees import module_name:

# Check sys.modules (cache of already loaded modules).

# If found → reuse.

# Search in built-in modules (like math, sys).

# Search in sys.path (list of directories: current dir → PYTHONPATH → site-packages).

# Load & execute the module’s code once (top-level runs at import).

# Store in sys.modules → reused for future imports.

# 3. Types of Import
# # 1. Import whole module
# import math
# print(math.sqrt(16))   # 4.0

# # 2. Import specific function/class
# from math import sqrt
# print(sqrt(25))        # 5.0

# # 3. Import with alias
# import numpy as np
# print(np.array([1,2,3]))

# # 4. Import all (not recommended)
# from math import *
# print(factorial(5))    # 12