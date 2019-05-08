===========
'pcpp' task
===========

'pcpp' task wraps pcpp Python C99 preprocessing package to work with other Pyloco tasks.

Installation
------------

Before installing 'pcpp' task, please make sure that 'pyloco' is installed.
Run the following command if you need to install 'pyloco'.

>>> pip install pyloco

Or, if 'pyloco' is already installed, upgrade 'pyloco' with the following command

>>> pip install -U pyloco

To install 'pcpp' task, run the following 'pyloco' command.

>>> pyloco install pcpp

Command-line syntax
-------------------

usage: pyloco pcpp [-h] [-o OUTPUT] [-D DEFINES] [-I INCLUDES]
                   [--general-arguments]
                   [data [data ...]]

a wrapper task for pcpp Python C99 preprocessing package

positional arguments:
  data                  Files to preprocess (use '-' for stdin)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output to a file instead of stdout
  -D DEFINES            Predefine name as a macro [with value]
  -I INCLUDES           Path to search for unfound #include's
  --general-arguments   Task-common arguments. Use --verbose to see a list of
                        general arguments


Example
-------


::
       program test
          integer, parameter :: x = XVAL, y = YVAL
          print *, x, "+", y, "=", x+y
       end program


::
       >>> pyloco pcpp my.f90 -D XVAL=1 -D YVAL=1 -o pcpp_my.f90
