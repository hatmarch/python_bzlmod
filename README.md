# Testing Python with bzlmod

## Experiment one: mixed closures

It looks like either:
-> the pydantic version of the importing module is the one that wins
X The highest version of the model wins

Pydantic when run in the module_1 module:
```
bazel run //python:main_3_11 --sandbox_debug

INFO: Analyzed target //python:main_3_11 (0 packages loaded, 0 targets configured).
INFO: Found 1 target...
Target //python:main_3_11 up-to-date:
  bazel-bin/python/_main_3_11
INFO: Elapsed time: 0.069s, Critical Path: 0.01s
INFO: 1 process: 1 internal.
INFO: Build completed successfully, 1 total action
INFO: Running command line: bazel-bin/python/main_3_11
Command: /private/var/tmp/_bazel_mwh/f42525795c639401f0ae478412e50c67/execroot/_main/bazel-out/darwin_arm64-fastbuild-ST-ab24b1cc52a2/bin/python/main_3_11.runfiles/_main/python/main.py
[MOD1] Python version: [MOD1] python: 3.11.9 (main, Jul 25 2024, 21:51:29) [Clang 18.1.8 ] requests: 2.31.0 pydantic: 1.9.2
[MOD1] Python version: [MOD2_lib] python: 3.11.9 (main, Jul 25 2024, 21:51:29) [Clang 18.1.8 ] requests: 2.31.0 pydantic: 1.9.2
Local version: 3.11.9 (main, Jul 25 2024, 21:51:29) [Clang 18.1.8 ]
```

When run by import in the root module (pydantic <2.8):
```
bazel 'run' '//:main_3_11' 

INFO: Analyzed target //:main_3_11 (39 packages loaded, 502 targets configured).
INFO: Found 1 target...
Target //:main_3_11 up-to-date:
  bazel-bin/_main_3_11
INFO: Elapsed time: 0.229s, Critical Path: 0.01s
INFO: 1 process: 1 internal.
INFO: Build completed successfully, 1 total action
INFO: Running command line: bazel-bin/main_3_11
Python version (root): [ROOT] python: 3.11.9 (main, Jul 25 2024, 21:51:29) [Clang 18.1.8 ] requests: 2.31.0 pydantic: 2.0
Python version (module 1): [MOD1] python: 3.11.9 (main, Jul 25 2024, 21:51:29) [Clang 18.1.8 ] requests: 2.31.0 pydantic: 2.0
Pydantic version: 2.0
```

When run module_1 (pydantic <2)
```
bazel run //python:main_3_11 --sandbox_debug
INFO: Analyzed target //python:main_3_11 (0 packages loaded, 0 targets configured).
INFO: Found 1 target...
Target //python:main_3_11 up-to-date:
  bazel-bin/python/_main_3_11
INFO: Elapsed time: 0.069s, Critical Path: 0.01s
INFO: 1 process: 1 internal.
INFO: Build completed successfully, 1 total action
INFO: Running command line: bazel-bin/python/main_3_11
Command: /private/var/tmp/_bazel_mwh/f42525795c639401f0ae478412e50c67/execroot/_main/bazel-out/darwin_arm64-fastbuild-ST-ab24b1cc52a2/bin/python/main_3_11.runfiles/_main/python/main.py
[MOD1] Python version: [MOD1] python: 3.11.9 (main, Jul 25 2024, 21:51:29) [Clang 18.1.8 ] requests: 2.31.0 pydantic: 1.9.2
[MOD1] Python version: [MOD2_lib] python: 3.11.9 (main, Jul 25 2024, 21:51:29) [Clang 18.1.8 ] requests: 2.31.0 pydantic: 1.9.2
Local version: 3.11.9 (main, Jul 25 2024, 21:51:29) [Clang 18.1.8 ]
```

But when run as module_2 (pydantic >2)
```
bazel run @module_2//python_2:main_3_11 --sandbox_debug
INFO: Analyzed target @@module_2~//python_2:main_3_11 (0 packages loaded, 3 targets configured).
INFO: Found 1 target...
Target @@module_2~//python_2:main_3_11 up-to-date:
  bazel-bin/external/module_2~/python_2/_main_3_11
INFO: Elapsed time: 0.384s, Critical Path: 0.31s
INFO: 9 processes: 9 internal.
INFO: Build completed successfully, 9 total actions
INFO: Running command line: bazel-bin/external/module_2~/python_2/main_3_11
[MOD2] Python version: [MOD2_lib] python: 3.11.9 (main, Jul 25 2024, 21:51:29) [Clang 18.1.8 ] requests: 2.31.0 pydantic: 2.8.2
Local version: 3.11.9 (main, Jul 25 2024, 21:51:29) [Clang 18.1.8 ]
```