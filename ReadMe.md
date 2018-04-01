Verification course
===================

[![Build Status](https://travis-ci.org/stoyanovd/verification_course.svg?branch=master)](https://travis-ci.org/stoyanovd/verification_course)


Executable
----------
Executables can be found in `dist` directory.
It is `verifier` and `verifier.exe` for Linux and Windows respectively.
They should be running from **root** directory of the project.

For example:
`./dist/verifier -m ./data/AChart.xstd -l "false"`


Development
-----------
Work with pip for travis:
```
pip install -r requirements-shortenings.txt && pip freeze > requirements-py3.txt
```


Test
----
Run tests from **root** directory.
`python -m pytest`
or
`python -m pytest <path_to_test>`
