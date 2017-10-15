# Utility scripts to deal with LabTS as a PPT

Use the fetch_scripts to download all the submissions of your students. Read the
usage first by running `./fetch_scripts -h`. This was not intended to be very
portable and the defaults reflect my own setup.

## Dependencies

You will need an install of Python 3 and above that can deal with SSL i.e. you
need to be able to write `import ssl` in your interpreter. You will also need to
have the `requests` module not part of the Python standard library. To install
it on your system follow the instructions
[here](http://docs.python-requests.org/en/master/user/install/)
This all the dependencies I am aware of. If there is anything else let me know,
or better make a pull request for this document.

## Contributions

This was intended as helpers scripts for PPTs at Imperial. If there is any other
script you would like to contribute for the purposes of PPTing or PMTing feel
free to create a PR.
