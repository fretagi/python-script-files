#!/usr/bin/env python
import subprocess

result = subprocess.run(["lscpu"], capture_output=True, text=True)
print(result.stdout)
