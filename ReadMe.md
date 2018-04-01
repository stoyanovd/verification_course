Verification course
===================

[![Build Status](https://travis-ci.org/stoyanovd/verification_course.svg?branch=master)](https://travis-ci.org/stoyanovd/verification_course)


Executable
----------
Executables can be found in `dist` directory.
It is `verifier` and `verifier.exe` for Linux and Windows respectively.
They should be running from **root** directory of the cloned project (`ltl2ba/ltl2ba` is used inside)

For example:
`./dist/verifier -m ./data/AChart.xstd -l "false"`  
`./dist/verifier -m ./data/AChart.xstd -f ./data/AChart.ltl.correct`


Syntax of LTL formulas
--------------------
Formulas can contain these operators: `!`, `X`, `G`, `F`, `R`, `U`, `&`, `|`, `->`, `<->`.
There are also brackets and values `true` and `false`. Variables can be written in single or double quotes.

Priority of operators are the same as in list written above, e.g. `'a' | 'b' & 'c'` will mean `'a' | ('b' & 'c')`.

Examples of the formulas can be found in these files: `data/*.ltl.*`.


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
