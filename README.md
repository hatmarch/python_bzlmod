# Testing Python with bzlmod

This repo houses three different python based bazel modules to see how the three will interact, particularly with regard to importing overlapping librarys (such as `pydantic`).

Here is how the modules depend on one another:

![image](docs/images/module_diagram.png)

## Experiment one: mixed closures

It looks like the pydantic version of the importing module is the one that wins.  However, it may be simply that whichever closure is first in the `PYTHONPATH` is what gets used for a given wheel (which means this is somewhat non deterministic)

Pydantic when run in the `module_1` module:
```
cd $(git rev-parse --show-toplevel)/module_1
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

When run in the `module_root` (pydantic <2.8):
```
cd $(git rev-parse --show-toplevel)/module_root
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

When run in the `module_root` directory BUT targeting the `module_1` specifically
```
cd $(git rev-parse --show-toplevel)/module_root
bazel run @module_1//python:main_3_11

INFO: Analyzed target @@module_1~//python:main_3_11 (90 packages loaded, 3330 targets configured).
INFO: Found 1 target...
Target @@module_1~//python:main_3_11 up-to-date:
  bazel-bin/external/module_1~/python/_main_3_11
INFO: Elapsed time: 7.325s, Critical Path: 0.20s
INFO: 9 processes: 9 internal.
INFO: Build completed successfully, 9 total actions
INFO: Running command line: bazel-bin/external/module_1~/python/main_3_11
Command: /private/var/tmp/_bazel_mwh/edab09eb93d43b7d9af27486ad695aa4/execroot/_main/bazel-out/darwin_arm64-fastbuild-ST-ab24b1cc52a2/bin/external/module_1~/python/main_3_11.runfiles/_main/../module_1~/python/main.py
[MOD1] Python version: [MOD1] python: 3.11.9 (main, Jul 25 2024, 21:51:29) [Clang 18.1.8 ] requests: 2.31.0 pydantic: 1.9.2
[MOD1] Python version: [MOD2_lib] python: 3.11.9 (main, Jul 25 2024, 21:51:29) [Clang 18.1.8 ] requests: 2.31.0 pydantic: 1.9.2
Local version: 3.11.9 (main, Jul 25 2024, 21:51:29) [Clang 18.1.8 ]
```


But when run as `module_2` (pydantic >2)
```
cd $(git rev-parse --show-toplevel)/module_2
bazel run //python_2:main_3_11

INFO: Analyzed target //python_2:main_3_11 (84 packages loaded, 3250 targets configured).
INFO: Found 1 target...
Target //python_2:main_3_11 up-to-date:
  bazel-bin/python_2/_main_3_11
INFO: Elapsed time: 0.384s, Critical Path: 0.31s
INFO: 9 processes: 9 internal.
INFO: Build completed successfully, 9 total actions
INFO: Running command line: bazel-bin/python_2/main_3_11
[MOD2] Python version: [MOD2_lib] python: 3.11.9 (main, Jul 25 2024, 21:51:29) [Clang 18.1.8 ] requests: 2.31.0 pydantic: 2.8.2
Local version: 3.11.9 (main, Jul 25 2024, 21:51:29) [Clang 18.1.8 ]
```