#!/usr/bin/env python

import sys
import traceback

try:
  from cli import CommandLineRunner

  if __name__ == "__main__":
    runner = CommandLineRunner()
    runner.run(sys.argv)
except Exception as e:
  stderr = sys.stderr
  with open('error.log', 'w') as f:
    sys.stderr = f
    traceback.print_exc()
    sys.stderr = stderr
  traceback.print_exc()
