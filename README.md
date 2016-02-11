# tweetsec

A python solution with the [Web2py](http://www.web2py.com/) framework for the TweetSec challenge (https://gist.github.com/patbenatar/069e46e6a34d65f35108)

## Code and Environment Overview

### Python and pip
This application runs on Web2py, which requires Python 2.6 or 2.7 (I'm using 2.7.3, the version of Python that comes packaged with Ubuntu 12.04). Using the Python package management system "pip" will also be very helpful to install the required Python modules.

Many people recommend using [virtualenv](https://virtualenv.readthedocs.org/en/latest/) and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/index.html) to setup your Python environment, though is isn't absolutely necessary. pip is automatically installed in new environments setup by virtualenv.

Installation of pip will vary depending on your environment. More details on installing pip here (if necessary): 

https://pip.pypa.io/en/latest/installing/

http://stackoverflow.com/questions/17271319/installing-pip-on-mac-os-x (Stack Overflow question on installing on OS X)


### Installing web2py 

Instructions for installing Web2py: http://www.web2py.com/init/default/download

Download the source code (http://www.web2py.com/examples/static/web2py_src.zip), and then unzip the downloaded file in the desired directory.

You can now run web2py with `python2.7 web2py.py` (this requires Python 2.7) from the commandline in the web2py directory. A window will pop up shortly after starting web2py with this command. Choose first Server IP option "Local (IPv4 (127.0.0.1)" (the default option), and set the Server Port option to "8000" (the default). Choose your password (can be anything), and then click the "start server" button.

### Installing the Tweetsec application into Web2py

Clone this repo into the the `web2py/applications` directory. Your directory structure should look something like this (simplified version)
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

To install the required Python modules, run `pip install -r requirements.txt` in the commandline in the tweetsec directory. This will install all the modules listed in the requirements.txt file.

Note, depending on your Python environment setup, you may need `sudo pip install -r requirements.txt` if you are not using virtualenv. This is generally not recommended (http://stackoverflow.com/questions/15028648/is-it-acceptable-safe-to-run-pip-install-under-sudo).


### Running the Tweetsec app

The app is started as part of Web2py when you run `python2.7 web2py.py`. The specific URL for the Tweetsec app is `http://127.0.0.1:8000/tweetsec/`, though the UI is just the default UI created for new web2py apps.

Tests are run by using `python tests.py` in the commandline in the tweetsec directory. The separate test files are located in the "fts" directory. For this challenge, I have only one file (test_tweetsec.py) in the "fts" folder with all the tests.

The app must already be running for the TweetSec Responses tests to work.

## Tweetsec Password Strength Evaluator
The TweetSec Password Strength Evaluator code is located in the password_eval module (modules/password_eval.py). Different functions here a responsible for a different part of the strength evaluator algorithm.

I did not create a URL that directly returns a passwords numerical strength, but that could be simply added if necessary. For now, the evaluator controller function at URL `http://127.0.0.1:8000/tweetsec/default/evaluator` uses the password_eval module code to calculate the numerical strength, and then returns an appopriate response based off of the password's strength.

## Tweetsec Response
For the Tweetsec responses, send a POST request to the evaluator controller function, which will be at URL `http://127.0.0.1:8000/tweetsec/default/evaluator` (if you're running web2py on your local machine at port 8000). Pass in the password string as the 'password' parameter in the POST request.

For weak passwords, Tweetsec will modify the password by replacing the first 4 chars with " #a1" if the password string length is >=13 (ensuring that the password will be strong). For passwords with <13 chars, I add " #a1" to the beginning, and then add " " characters until is reaches 13 characters for a strong password.

There is one big caveat that I did not have time to account for, with respect to the weak passwords. So far, it runs under the assumption that there are no >1 length english words in the password. I would have to further change the code to accomodate for english words in weak passwords.

There might also be other errors with respect to the weak password response code, as this is when I ran out of time.

