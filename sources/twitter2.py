import urllib.request
import urllib.parse
import urllib.error
import twurl
import json
import ssl


TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_info_by_nickname(acct):
    """
    (str) -> dict(...)
    Gets data about account with name str
    """
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '75'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    return js
