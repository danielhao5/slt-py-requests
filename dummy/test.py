#!/usr/bin/env python

"""
Author: Nick Russo (njrusmc@gmail.com)
Purpose: ???
"""

import requests
from print_response import print_response


def main():
    """
    Execution starts here.
    """

    resp = requests.get("http://njrusmc.net")
    print_response(resp)

    resp = requests.get("http://dummy.restapiexample.com/api/v1/employees")
    print_response(resp)

    resp = requests.get("https://tinyurl.com/y9jt8ah4")
    print_response(resp)


if __name__ == "__main__":
    main()
