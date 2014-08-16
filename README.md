Isitup
======

Isitup is a hosted service for checking if some server is still up or not. It
requires that servers send an HTTP GET request to a specific IP address to
specify that they're still up. The easiest way to set this up is as a cron job.

The only method of authentication accepted is Google OAuth2.

It isn't pretty, there are no error messages, there are no success messages,
but it works.
