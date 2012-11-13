##################################################
# URL Normalization methods                      #
##################################################
import re

def _lowercase(url):
    return url.lower()

def _capitalize_escapes(url):
    escapes = re.findall("%[0-9a-f]{2}", url)
    for escape in escapes:
        url = re.sub(escape, escape.upper(), url)
    return url

def _remove_default_port(url):
    return re.sub(r'(?::\d+)?', '', url)

def _remove_empty_querystring(url):
    # need to account for the \n at the end
    if url[len(url) - 2] == '?':
        url = url[:-2] + '\n'
    return url

normalizations = [_lowercase,
                  _capitalize_escapes,
                  _remove_default_port,
                  _remove_empty_querystring]

def normalize(urls):
    result = []
    for url in urls:
        curr = url
        for norm in normalizations:
            curr = norm(curr)
        result.append(curr)

    return result
