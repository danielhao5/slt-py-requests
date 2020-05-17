#!/usr/bin/env python

"""
Author: Nick Russo (njrusmc@gmail.com)
Purpose: Simple printing mechanism for HTTP responses that come back
from the 'requests' library for troubleshooting/learning.
"""

import json
import xml.dom.minidom as prettyx


def print_response(resp, filedir="resp", filename=None):
    """
    Print the key details from a given response. Set dump_body to true
    to reveal the body content in the most appropriate format based on
    the response's Content-Type header.
    """

    # For context, print the original request
    # ... and a line of dashes of equal length
    header = f"\n\n{resp.request.method} {resp.request.url}"
    print(header)
    print(len(header) * "-")

    # Print the status code and reason, along with the elapsed time
    print(f"Result: {resp.status_code}/{resp.reason}")
    print(f"Elapsed time: {resp.elapsed.microseconds} us")

    # Iterate over all kv-pairs in the headers dictionary and print them
    print("HTTP headers:")
    for header_name, header_value in resp.headers.items():
        print(f"  - {header_name}: {header_value}")

    # Print the number of redirects. If any exist, print out the URL/status
    print(f"HTTP redirect count: {len(resp.history)}")
    for hist in resp.history:
        print(f"  - {hist.url} -> {hist.status_code}/{hist.reason}")

    # First, determine the content type, defaulting to "text"
    content_type = resp.headers.get("Content-Type", "text")

    # If a filename was not supplied, create a dynamic one using
    # the method name and the in-memory ID of the response object
    if not filename:
        filename = f"{resp.request.method}_{id(resp)}".lower()

    # Define the entire filepath using the directory and name
    filepath = f"{filedir}/{filename}"

    # Based on the content type, create different files
    if "text" in content_type:
        filepath += ".txt"
        with open(filepath, "w") as handle:
            handle.write(resp.text)
    elif "html" in content_type:
        filepath += ".html"
        with open(filepath, "w") as handle:
            handle.write(resp.text)
    elif "html" in content_type:
        filepath += ".html"
        with open(filepath, "w") as handle:
            handle.write(resp.text)
    elif "json" in content_type:
        filepath += ".json"
        with open(filepath, "w") as handle:
            json.dump(resp.json(), handle, indent=2)
    elif "xml" in content_type:
        filepath += ".xml"
        with open(filepath, "w") as handle:
            handle.write(prettyx.parseString(resp.text).toprettyxml())
    elif "image" in content_type:
        filepath += ".jpg"
        with open(filepath, "wb") as handle:
            handle.write(resp.content)

    print(f"HTTP body written to {filepath}")
