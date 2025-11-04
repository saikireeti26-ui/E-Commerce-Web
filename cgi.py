"""Small shim to provide minimal `cgi` module functions missing in Python 3.13+
This is a compatibility shim used so older libraries (e.g. Django<4) that
import the stdlib `cgi` still work. It only implements a tiny subset of the
original API used by this project: parse_header, parse_qs, valid_boundary.

Note: This is intentionally small — if you see more import errors referencing
other `cgi` APIs add minimal wrappers here or prefer using a Python runtime
compatible with the project's Django version.
"""
from urllib.parse import parse_qs as parse_qs
import re

def parse_header(line):
    """Parse a Content-type like header.

    Returns (value, params_dict) — similar enough for Django's usage.
    """
    if not line:
        return '', {}
    parts = line.split(';')
    main = parts[0].strip()
    params = {}
    for p in parts[1:]:
        if '=' in p:
            k, v = p.split('=', 1)
            params[k.strip().lower()] = v.strip().strip('"')
    return main, params


_boundary_re = re.compile(r"^[ -~]{1,70}$")

def valid_boundary(boundary):
    """Return True if boundary looks like a valid multipart boundary.

    We use a lightweight check: must be ASCII-printable and length <= 70.
    """
    if not boundary or not isinstance(boundary, str):
        return False
    return bool(_boundary_re.match(boundary))


# Expose common names expected by code importing `cgi`.
__all__ = ["parse_header", "parse_qs", "valid_boundary"]
