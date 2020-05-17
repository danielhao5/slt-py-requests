#!/usr/bin/env python

"""
Author: Nick Russo (njrusmc@gmail.com)
Purpose: Demonstrate how requests handles HTTP redirects for
a typical GET request.
"""

import requests
from print_response import print_response


def main():
    """
    Execution begins here.
    """

    # This links to my "Python 3 By Example" course on O'Reilly
    resp = requests.get(f"https://tinyurl.com/y87gofyp")
    resp.raise_for_status()
    print_response(resp, dump_body=False)


if __name__ == "__main__":
    main()
