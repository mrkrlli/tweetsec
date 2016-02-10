# tweetsec

A python solution with the [Web2py](http://www.web2py.com/) framework for the TweetSec challenge (https://gist.github.com/patbenatar/069e46e6a34d65f35108)

## Code and Environment overview
The app is start through `python web2py.py` (assuming that this app is already in the applications directory of the parent web2py folder).

Tests are run by using `python tests.py` in the commandline. The separate test files are located in the "fts" directory. For this challenge, I have only one file (test_tweetsec.py) in the "fts" folder with all the tests.

Note that the app must already be running for the TweetSec Responses test to work.

## Tweetsec Password Strength Evaluator
The TweetSec Password Strength Evaluator code is located in the password_eval module (modules/password_eval.py). Different functions here a responsible for a different part of the strength evaluator algorithm.


## Tweetsec Response
For the Tweetsec responses, send a POST request to the evaluator controller function, which will be at URL `http://127.0.0.1:8000/tweetsec/default/evaluator` if you're running Web2py on your local machine at port 8000. Pass in the password as the 'password' parameter in the POST request.

For weak passwords, Tweetsec will modify the password by replacing the first 4 chars with " #a1" if the password string length is >=13 (ensuring that the password will be strong). For passwords with <13 chars, I add " #a1" to the beginning, and then add " " characters until is reaches 13 characters for a strong password.

There is one big caveat that I did not have time to account for, with respect to the weak passwords. So far, it runs under the assumption that there are no >1 length english words in the password. I would have to further change the code to accomodate for english words in weak passwords.

There might also be other errors with respect to the weak password response code, as this is when I ran out of time.

