# Testing Python with bzlmod

## Experiment one: mixed closures

It looks like either:
- the pydantic model of the importing module is the one that wins
- The highest version of the model wins

Pydantic when run in the module_1 module:
```
bazel 'run' '//python:main_3_12' 

INFO: Analyzed target //python:main_3_12 (9 packages loaded, 2365 targets configured).
INFO: Found 1 target...
Target //python:main_3_12 up-to-date:
  bazel-bin/python/_main_3_12
INFO: Elapsed time: 0.204s, Critical Path: 0.02s
INFO: 1 process: 1 internal.
INFO: Build completed successfully, 1 total action
INFO: Running command line: bazel-bin/python/main_3_12
Python version: [MOD1] python: 3.12.4 (main, Jul 25 2024, 22:11:22) [Clang 18.1.8 ] requests: 2.32.3 pydantic: 1.10.18
Local version: 3.12.4 (main, Jul 25 2024, 22:11:22) [Clang 18.1.8 ]
```

When run by import in the root module:
```
bazel 'run' '//:main_3_12' 

INFO: Analyzed target //:main_3_12 (15 packages loaded, 2548 targets configured).
INFO: Found 1 target...
Target //:main_3_12 up-to-date:
  bazel-bin/_main_3_12
INFO: Elapsed time: 0.291s, Critical Path: 0.17s
INFO: 9 processes: 9 internal.
INFO: Build completed successfully, 9 total actions
INFO: Running command line: bazel-bin/main_3_12
Python version (root): [ROOT] python: 3.12.4 (main, Jul 25 2024, 22:11:22) [Clang 18.1.8 ] requests: 2.32.3 pydantic: 2.8.2
Python version (module 1): [MOD1] python: 3.12.4 (main, Jul 25 2024, 22:11:22) [Clang 18.1.8 ] requests: 2.32.3 pydantic: 2.8.2
Local version: 3.12.4 (main, Jul 25 2024, 22:11:22) [Clang 18.1.8 ]
Command: /private/var/tmp/_bazel_mwh/edab09eb93d43b7d9af27486ad695aa4/execroot/_main/bazel-out/darwin_arm64-fastbuild-ST-308aef2d6938/bin/main_3_12.runfiles/_main/main.py
```