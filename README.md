# Cracking the Coding Interview
-------------------------------

python solutions to [Cracking the Coding Interview](http://www.crackingthecodinginterview.com).

## Running the tests
--------------------

Tests are run using [`pytest`](http://doc.pytest.org/). When multiple implementation of the
same algorithm are available in the module, a custom fixture takes care of running the tests
against all the implementations. In order to run all the test use

    make test

A virtualenv will be created, and `pytest` will be installed inside the virtualenv to run tests.
