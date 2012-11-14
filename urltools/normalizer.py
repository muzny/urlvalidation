##################################################
# URL Normalization methods                      #
##################################################
import re
import posixpath
from urlparse import urlparse, urlunparse

# normalizations that preserve semantics

def _lowercase(url):
    """Convert the scheme and host to lowercase"""
    res = urlparse(url)
    norm = (res.scheme.lower(), res.netloc.lower(), res.path, res.params, res.query, res.fragment)
    return urlunparse(norm)

def _capitalize_escapes(url):
    escapes = re.findall("%[0-9a-f]{2}", url)
    for escape in escapes:
        url = re.sub(escape, escape.upper(), url)
    return url

def _remove_default_port(url):
    return re.sub(r'(?::\d+)?', '', url)

# normalizations that usually preserve semantics

def _add_trailing_slash(url):
    # no way to be sure if url path ends in a directory. Here we treat as a directory
    # anything that doesn't contain a .
    if re.search(r'/\w*\.\w*$', url):
        return url   # it's a file, probably

    res = urlparse(url)
    if res.params != '' or res.query != '' or res.fragment != '':
        return url  # it has stuff after the path

    if url[len(url) - 1] != '/':
        url = url + '/'

    return url

def _remove_dot_segments(url):
    # Note: add trailing slash must be called after this method, since this method
    # will remove trailing slashes.
    # Also, urlparse only gives us a good path element for urls whose scheme is specified
    # this is fine for now since scheme-less urls will fail validation anyway
    res = urlparse(url)
    path = res.path

    if res.scheme != '' and res.path != '':
        path = posixpath.abspath(path)

    norm = (res.scheme, res.netloc, path, res.params, res.query, res.fragment)
    return urlunparse(norm)

# normalizations that change semantics

def _remove_empty_querystring(url):
    if len(url) < 2:
        return url

    # need to account for the \n at the end
    if url[len(url) - 1] == r'?':
        url = url[:-1]
    return url


normalizations = [_lowercase,
                  _capitalize_escapes,
                  _remove_default_port,
                  _remove_dot_segments,
                  _add_trailing_slash,
                  _remove_empty_querystring]

def normalize(urls):
    result = []
    for url in urls:
        curr = url
        for norm in normalizations:
            curr = norm(curr)
        result.append(curr)

    return result
