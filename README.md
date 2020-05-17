[![Build Status](
https://travis-ci.com/nickrusso42518/slt-py-requests.svg?branch=master)](
https://travis-ci.com/nickrusso42518/slt-py-requests)

# Safari Live Training - Getting Started with Python requests
Source code for the training course. Please contact me with any questions.
Before beginning, be sure you know how to use `git` at a basic level on
your computer (Windows, Mac OS, or Linux).


> Contact information:\
> Email:    njrusmc@gmail.com\
> Twitter:  @nickrusso42518

  * [Download Instructions](#download-instructions)
  * [Usage](#usage)
  * [Testing](#testing)

## Download Instructions
The easiest way to consume this code is to clone it using SSH or HTTPS.

SSH: `git clone git@github.com:nickrusso42518/slt-py-requests.git`

or

HTTPS: `git clone https://github.com/nickrusso42518/slt-py-requests.git`

After cloning, you should see the following file system structure:

```
$ tree
TODO
```

Ensure you have Python 3.6 or newer installed along with pip.

> Visit https://www.python.org/downloads/ to download Python.

`sudo python -m ensurepip`

or

`sudo easy_install pip`

No need to install any packages via pip; this is done during the course.

To get setup, first run `make setup` which will install the required
Python packages and create the `resp/` directory. Failing to take
this step could result in errors later in the course.

Optionally, run `make` to run a full suite of testing on the code
to ensure everything works. After a fresh `git clone` there should
be no errors.

## Usage
This repository contains several scripts which are detailed in the course.
Below is a summary of each one:
TODO

## Testing
A GNU Makefile with phony targets is used for testing this codebase.
There are currently three steps:
  * `setup`: Installs required Python packages in the `requirements.txt`
    file using `pip`. Creates `resp/` directory.
  * `lint`: Runs Python linter (`pylint`) and code formatter (`black`).
    This captures any syntax or styling errors with the code.
  * `run`: Runs all of the Python scripts described in the "Usage" section.
  * `clean`: Removes any `*.pyc` files and all files in the `resp/` directory.
    circle classes. This ensures the methods in each classes are operating
    correctly.

You can run `make` or `make all` to run all the testing in series when doing
manual regression testing from the shell. As mentioned earlier in the README,
this is a good idea after first cloning the repository.
