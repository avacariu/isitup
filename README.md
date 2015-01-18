Isitup
======

Isitup is a hosted service for checking if some server is still up or not. It
requires that servers send an HTTP GET request to a specific URL to say that
they're still up. The easiest way to set this up is as a cron job.

The only method of authentication accepted is Google OAuth2 (OpenID Connect).
Since this service is just something I've written for my own personal use, I'm
not too interested in extending the user management features.

It isn't pretty, there are no error messages, there are no success messages,
but it works.

MIT Licensed.


Google OAuth2 setup
-------------------

You'll need a `local_config.py` file containing your key and secret. This
should contain the following two variables:

    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'XXXXXX.apps.googleusercontent.com'
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'XXXXXXXXX'

As you can tell, these exist in the `config.py`, which then tries `from
local_config import *`. This will overwrite the existing variables.

I did it this way so I can add `config.py` to git without adding my keys.
