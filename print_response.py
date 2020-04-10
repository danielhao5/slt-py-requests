#!/usr/bin/env python

"""
Author: Nick Russo (njrusmc@gmail.com)
Purpose: Simple printing mechanism for HTTP responses that come back
from the 'requests' library for troubleshooting/learning.
"""

import json
import xml.dom.minidom as prettyx


def print_response(resp, dump_body=False):
    """
    Print the key details from a given response. Set dump_body to true
    to reveal the body content in the most appropriate format based on
    the response's Content-Type header.
    """

    # For context, print the original request
    # ... and a line of dashes of equal length
    header = f"\n{resp.request.method} {resp.request.url}"
    print(header)
    print(len(header) * "-")

    # Print the status code and reason, along with the elapsed time
    print(f"Result: {resp.status_code}/{resp.reason}")
    print(f"Elapsed time: {resp.elapsed.microseconds} us")

    # Iterate over all kv-pairs in the headers dictionary and print them
    print("HTTP headers:")
    for header_name, header_value in resp.headers.items():
        print(f"  - {header_name}: {header_value}")

    # Print the body if dump_body is true
    if dump_body:

        # First, determine the content type, defaulting to "text"
        content_type = resp.headers.get("Content-Type", "text")
        print("HTTP body:")

        # Test for different content types; use appropriate display technique
        if "text" in content_type:
            print(resp.text)
        elif "json" in content_type:
            print(json.dumps(resp.json(), indent=2))
        elif "xml" in content_type:
            print(prettyx.parseString(resp.text).toprettyxml())
        elif "image" in content_type:
            # is this sensible?
            print(resp.content)
