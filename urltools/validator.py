import re

# this is the regular expression used by Django's url validator
# see: http://stackoverflow.com/questions/7160737/python-how-to-validate-a-url-in-python-malformed-or-not
# Note: this requires the protocol be specified. We can modify it if that's not what we want.
URLregex= re.compile(
          r'^(?:http|ftp)s?://' # http:// or https://
          r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
          r'localhost|' #localhost...
          r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
          r'(?::\d+)?' # optional port
          r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def validate(urls):
    return [url for url in urls if re.search(URLregex, url) is not None]

