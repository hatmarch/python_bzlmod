from test_lib import TestClass
import sys
import os

def main():
    test = TestClass()
    print (f"Python version: {test.py_version()}")
    print (f"Local version: {sys.version}")
    # print (f"env: {os.environ['PYTHONPATH']}")

if __name__ == "__main__":
    main()