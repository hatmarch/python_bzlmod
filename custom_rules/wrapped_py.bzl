# wrapped_py_library.bzl
# load("@python_3_11//:defs.bzl", py_binary_3_11 = "py_binary")



# #load("@rules_python//python:defs.bzl", "py_binary")
load("//custom_rules:custom_pyinfo.bzl", "WrappedPyInfo")
load("@rules_python//python:py_info.bzl", "PyInfo")

def _wrapped_py_library_impl(ctx):
    # Get the PyInfo provider from the dependency
    py_info = ctx.attr.dep[PyInfo]

    # Create and return an instance of CustomProvider
    custom_provider = WrappedPyInfo(pyinfo = py_info)

    return [
        custom_provider,
    ]

wrapped_py_library = rule(
    implementation = _wrapped_py_library_impl,
    attrs = {
        "dep": attr.label(providers = [PyInfo]),
    },
)

def _unwrapped_py_library_impl(ctx):
    # Get the PyInfo provider from the dependency
    custom_py_info = ctx.attr.dep[WrappedPyInfo]

    return [
        custom_py_info.pyinfo
    ]

unwrapped_py_library = rule(
    implementation = _unwrapped_py_library_impl,
    attrs = {
        "dep": attr.label(providers = [WrappedPyInfo]),
    },
)

