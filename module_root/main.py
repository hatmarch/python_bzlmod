from test_lib import TestClass
from python.test_lib import TestClass as Module1TestClass
import sys
# try:
#     from pydantic import v1 as pydantic
# except:
#     import pydantic
#import pydantic

try:
    import debugpy

    port=5678
    debugpy.listen(port)
    print(f'Waiting for debugger> Run: Python: Attach {port}')
    debugpy.wait_for_client()  # blocks execution until client is attached
except:
    pass

def main():
    test = TestClass()
    test_module_1 = Module1TestClass()
    print (f"Python version (root): {test.py_version()}")
    print (f"Python version (module 1): {test_module_1.py_version()}")
    #print (f"Pydantic version: {pydantic.VERSION}")
    print (f"Local version: {sys.version}")
    print (f"Command: {sys.argv[0]}")

if __name__ == "__main__":
    main()