# tweetsec

A python solution with the [Web2py](http://www.web2py.com/) framework for the TweetSec challenge (https://gist.github.com/patbenatar/069e46e6a34d65f35108)

## Code and Environment overview

### Installing Python and Pip
This application runs on Web2py, which requires Python 2.6 or 2.7 (I'm using 2.7.3, the version of Python that comes packaged with Ubuntu 12.04). Using the Python package management system "pip" will also be very helpful to install the required Python modules.

Installation of pip will vary depending on your environment, more details on installing pip here: https://pip.pypa.io/en/latest/installing/

### Installing web2py 

Instructions for installing Web2py: http://www.web2py.com/init/default/download

Download the source code (http://www.web2py.com/examples/static/web2py_src.zip), and then unzip the downloaded file in the desired directory.

Then run web2py with `python2.7 web2py.py` (this requires Python 2.7) from the commandline in the web2py directory.

### Installing the Tweetsec application into Web2py

In the `web2py/applications` directory, create a `tweetsec` directory. Then pull the contents of this repo into the the `web2py/applications/tweetsec` directory. Your directory structure should look something like this (simplified version)
 ```
 web2py/
    applications/
       admin/
       examples/
       tweetsec/
          controllers/
          cron/
          databases/
          errors/
          fts/
       welcome/
    deposit/
    examples/

 ```

### Installing the required Python modules
This application requires a few Python modules to run properly.

To install the required Python modules, run `pip install -r requirements.txt` in the commandline in the tweetsec directory. This will install all the modules listed in the requirements.txt file

### Running the Tweetsec app

The app is will be started as part of Web2py when you run `python2.7 web2py.py`. The specific URL for the Tweetsec app is `http://127.0.0.1:8000/tweetsec/`, though there UI is just the default UI created for new web2py apps.

Tests are run by using `python tests.py` in the commandline in the tweetsec directory. The separate test files are located in the "fts" directory. For this challenge, I have only one file (test_tweetsec.py) in the "fts" folder with all the tests.

The app must already be running for the TweetSec Responses tests to work.

## Tweetsec Password Strength Evaluator
The TweetSec Password Strength Evaluator code is located in the password_eval module (modules/password_eval.py). Different functions here a responsible for a different part of the strength evaluator algorithm.


## Tweetsec Response
For the Tweetsec responses, send a POST request to the evaluator controller function, which will be at URL `http://127.0.0.1:8000/tweetsec/default/evaluator` if you're running Web2py on your local machine at port 8000. Pass in the password as the 'password' parameter in the POST request.

For weak passwords, Tweetsec will modify the password by replacing the first 4 chars with " #a1" if the password string length is >=13 (ensuring that the password will be strong). For passwords with <13 chars, I add " #a1" to the beginning, and then add " " characters until is reaches 13 characters for a strong password.

There is one big caveat that I did not have time to account for, with respect to the weak passwords. So far, it runs under the assumption that there are no >1 length english words in the password. I would have to further change the code to accomodate for english words in weak passwords.

There might also be other errors with respect to the weak password response code, as this is when I ran out of time.

