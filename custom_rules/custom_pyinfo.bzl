# custom_pyinfo.bzl

# load("@rules_python//python:py_info.bzl", "PyInfo")


# Define a custom provider with one field that holds the PyInfo
WrappedPyInfo = provider(
    fields = {
        "pyinfo": "The PyInfo provider passed in"
    }
)
