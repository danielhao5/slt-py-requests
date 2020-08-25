#!/usr/bin/env python

"""
Author: Nick Russo (njrusmc@gmail.com)
Purpose: Demonstrate basic HTTP cache-control mechanisms using a variety
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

    # Use our standard logger template
    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG,
    )
    logger = logging.getLogger()

    # Specify list of URLs to perform an HTTP GET against
    # Author's note: These files don't have "Cache-Control" anymore as I removed
    # them after the demo. Please replace these URLs with your own!
    url_list = [
        "http://njrusmc.net/jobaid/mpls_pcap.zip",  # Cache-Control: public (300s)
        "http://njrusmc.net/jobaid/ipsec_pcap.zip",  # Cache-Control: no-store
    ]

    # For each URL, run two GET requests, and use the logger to print out
    # the relevant information as requests are processed
    for url in url_list:

        # Create the cached session object, which automatically intereprets
        # caching-related headers (requests doesn't do it natively)
        cached_sess = CacheControl(requests.session())

        # Print information from first run, include key headers
        logger.info("First GET to %s", url)
        resp = cached_sess.get(url)
        resp.raise_for_status()
        print_response(resp, dump_body=False)

        # Slight delay just to show the cache timer countdown
        # Print information from second run, but focus is on background debugs
        time.sleep(2)
        logger.info("Second GET to %s", url)
        resp = cached_sess.get(url)
        resp.raise_for_status()
        print_response(resp, dump_body=False)


if __name__ == "__main__":
    main()
