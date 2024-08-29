import sys
import websockets
import requests

class TestClass:
    def py_version(self) -> str:
        return f"python: {sys.version} requests: {requests.__version__}"
    