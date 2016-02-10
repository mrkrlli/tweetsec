# tweetsec

A python solution with the Web2py framework for the TweetSec challenge (https://gist.github.com/patbenatar/069e46e6a34d65f35108)


The TweetSec Password Strength Evaluator code is located in the password_eval module (modules/password_eval.py). Different functions here a responsible for a different part of the strength evaluator algorithm.

The app is start through `python web2py.py` (assuming that this app is already in the applications directory of the parent web2py folder).

Tests are run by using `python tests.py` in the commandline. The separate test files are located in the "fts" directory. For this challenge, I have only one file (test_tweetsec.py) in the "fts" folder with all the tests.

Note that the app must already be running for the TweetSec Responses test to work.

