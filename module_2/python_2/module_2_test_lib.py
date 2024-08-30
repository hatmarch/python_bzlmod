import sys
import requests
# try:
#     from pydantic import v1 as pydantic
# except:
#     import pydantic
import pydantic

class TestClass2:
    def py_version(self) -> str:
        return f"[MOD2_lib] python: {sys.version} requests: {requests.__version__} pydantic: {pydantic.VERSION}"
    