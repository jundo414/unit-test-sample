# Sample for unit testing tools

## for Python

### pytest
#### How to setup

You don't need any install if you've already installed python.

#### How to run

You can test your code by running the following command.

```
$ pytest pytest_calc.py 
========================================================================= test session starts ==========================================================================
platform linux2 -- Python 2.7.13, pytest-3.2.1, py-1.4.34, pluggy-0.4.0
rootdir: /work/unit-test/src/hoge/tests, inifile:
collected 4 items                                                                                                                                                       

pytest_calc.py ....

======================================================================= 4 passed in 0.04 seconds =======================================================================
```

If you want to display the debug information, issue the following command.

```
$ pytest -v pytest_calc.py 
========================================================================= test session starts ==========================================================================
platform linux2 -- Python 2.7.13, pytest-3.2.1, py-1.4.34, pluggy-0.4.0 -- /root/anaconda3/bin/python
cachedir: .cache
rootdir: /work/unit-test/src/hoge/tests, inifile:
collected 4 items                                                                                                                                                       

pytest_calc.py::test_add PASSED
pytest_calc.py::test_sub PASSED
pytest_calc.py::test_mul PASSED
pytest_calc.py::test_div PASSED

======================================================================= 4 passed in 0.02 seconds =======================================================================
```

### unittest
#### How to setup
you should install unittest using pip.

```
$ pip install unittest
```


#### How to run

You can test your code by running the following command.

```
$ python -m unittest -v unittest_calc
test_add (unittest_calc.UnitestCalc) ... ok
test_div (unittest_calc.UnitestCalc) ... ok
test_mul (unittest_calc.UnitestCalc) ... ok
test_sub (unittest_calc.UnitestCalc) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

If you want to display the debug information, issue the following command

```
$ python -m unittest -v unittest_calc
test_add (unittest_calc.UnitestCalc) ... ok
test_div (unittest_calc.UnitestCalc) ... ok
test_mul (unittest_calc.UnitestCalc) ... ok
test_sub (unittest_calc.UnitestCalc) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

## for Bash
### Bats
#### How to setup

Run the following command to place the executable file.

```
$ git clone https://github.com/sstephenson/bats.git
$ cd bats
$ sudo ./install.sh /usr/local
Installed Bats to /usr/local/bin/bats
```

#### How to run

You can run your codes below.

```
# ./test_sum_num.sh 
 ✓ sum all numbers 1
 ✓ sum all numbers 2
 ✓ sum all numbers 3

3 tests, 0 failures
```
