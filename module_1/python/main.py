try:
    import debugpy

    port=5678
    debugpy.listen(port)
    print(f'Waiting for debugger> Run: Python: Attach {port}')
    debugpy.wait_for_client()  # blocks execution until client is attached
except:
    pass

import sys
print (f"Command: {sys.argv[0]}")

from python.test_lib import TestClass
from python_2.module_2_test_lib import TestClass2
import os

def main():
    test = TestClass()
    test2 = TestClass2()
    print (f"[MOD1] Python version: {test.py_version()}")
    print (f"[MOD1] Python version: {test2.py_version()}")
    print (f"Local version: {sys.version}")
    # print (f"Command: {sys.argv[0]}")
    # print (f"env: {os.environ['PYTHONPATH']}")

if __name__ == "__main__":
    main()