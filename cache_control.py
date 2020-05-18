#!/usr/bin/env python

"""
Author: Nick Russo (njrusmc@gmail.com)
Purpose: Demonstrate basic HTTP cache-control mechanisms usinga variety
of URLs with different cache-control characteristics.
"""

import logging
import time
import requests
from cachecontrol import CacheControl
from print_response import print_response


def main():
    """
    Execution begins here.
    """

    # Create a logger object to let us see what is happening behind the
    # scenes with the HTTP URLs
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Specify list of URLs to perform an HTTP GET against
    # Author's note: These files don't have "Cache-Control" anymore as I removed
    # them after the demo. Please replace these URLs with your own!
    url_list = [
        "http://njrusmc.net/jobaid/wlan_pcap.zip",  # Cache-Control: public (300s)
        "http://njrusmc.net/jobaid/lmnop_answers.pdf",  # Cache-Control: no-store
    ]

    # For each URL, run two GET requests, and use the logger to print out
    # the relevant information as requests are processed
    for url in url_list:

        # Create the cached session object, which automatically intereprets
        # caching-related headers (requests doesn't do it natively)
        cached_sess = CacheControl(requests.session())

        # Print information from first run, include key headers
        resp = cached_sess.get(url)
        resp.raise_for_status()
        print_response(resp, dump_body=False)

        # Slight delay just to show the cache timer countdown
        # Print information from second run, but focus is on background debugs
        time.sleep(2)
        resp = cached_sess.get(url)
        resp.raise_for_status()
        print_response(resp, dump_body=False)


if __name__ == "__main__":
    main()