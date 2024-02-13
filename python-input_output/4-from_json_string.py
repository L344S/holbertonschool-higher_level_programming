#!/usr/bin/python3
import json
"""A module for from_json_string function."""


def from_json_string(my_str):
    """
    Description:
        A function that returns an object (Python data structure)
        represented by a JSON string.

    Args:
        my_str: The JSON string to convert to an object.

    Returns:
        The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
