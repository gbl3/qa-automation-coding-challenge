# TrueNorth Challenge

This repository code is part of the Homework Challenge of TrueNorth selection process.

## Tech Stack

**Language:** [Python](https://www.python.org/)

**Test Framework:** [Selenium](https://www.selenium.dev/)

**Most Relevant Libraries/Modules**: [Python's virtualenv](https://docs.python.org/3.11/library/venv.html), 
[Python's unittest](https://docs.python.org/3/library/unittest.html) and [Webdriver-manager](https://pypi.org/project/webdriver-manager/)  

All used libraries and their version can be checked on the `requirements.txt` file.

## Installation
To properly run the test code, some programs needs to be installed.

* GitHub (See how to, depending on your OS [here](https://github.com/git-guides/install-git))
* Python version 3.11.4, [here](https://www.python.org/downloads/)
* Chrome browser, [here](https://www.google.com/intl/en_us/chrome/)

## Running Locally

Clone the project

```bash
git clone https://github.com/gbl3/qa-automation-coding-challenge.git
```

Go to the project directory

```bash
cd qa-automation-coding-challenge
```

Activate the virtualenv (**Note: this runs different depending on your OS**)

For **Windows PowerShell**:
```bash
appenv\Scripts\Activate.ps1  
```

For **Windows cmd**:
```bash
appenv\Scripts\activate.bat
```

For **Linux/MacOs**:
```bash
source appenv/Scripts/activate
```

----
**Before running the tests, make sure you have the project running. Check instructions on root file _README.md_**

With the project running and the virtualenv activated, you can run the tests by typing:

```bash
cd tests && python -m unittest tests -v
```

Once you are already on the `tests` folder and want to run again, exclude the `cd` part and run only
```bash
python -m unittest tests -v
```
If an error occurs, please try running the following. After that, retry the previous command
```bash
pip install -r requirements.txt 
```

To deactivate the virtual environment, simply type:   
```bash
deactivate
```