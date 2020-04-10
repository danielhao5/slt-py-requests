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
    print_response(resp, dump_body=True)

    resp = requests.get("http://dummy.restapiexample.com/api/v1/employees")
    # import pdb; pdb.set_trace()
    print_response(resp, dump_body=True)

if __name__ == "__main__":
    main()
