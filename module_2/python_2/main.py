from python_2.module_2_test_lib import TestClass2
import sys
import os

try:
    import debugpy

    port=5678
    debugpy.listen(port)
    print(f'Waiting for debugger> Run: Python: Attach {port}')
    debugpy.wait_for_client()  # blocks execution until client is attached
except:
    pass

def main():
    test = TestClass2()
    print (f"[MOD2] Python version: {test.py_version()}")
    print (f"Local version: {sys.version}")
    # print (f"env: {os.environ['PYTHONPATH']}")

if __name__ == "__main__":
    main()