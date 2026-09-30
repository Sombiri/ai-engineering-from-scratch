"""CPU-only Docker runtime inspection trial.

Lesson: phases/00-setup-and-tooling/07-docker-for-ai/docs/en.md
Demonstrates the OS, architecture, Python version, and working directory.
Uses only the Python standard library.
"""


import os
import platform
import sys

print("Hello, I must learn")
print(platform.system())
print(platform.machine())
print(sys.version)
print(os.getcwd())

