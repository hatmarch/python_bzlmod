import sys
import requests
try:
    from pydantic import v1 as pydantic
except:
    import pydantic

class TestClass:
    def py_version(self) -> str:
        return f"python: {sys.version} requests: {requests.__version__} pydantic: {pydantic.VERSION}"
    