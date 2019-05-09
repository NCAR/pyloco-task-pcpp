=========================
'pcpp' task version 0.1.2
=========================

'pcpp' task wraps pcpp Python C99 preprocessing package to work with other Pyloco tasks.

Installation
------------

Before installing 'pcpp' task, please make sure that 'pyloco' is installed.
Run the following command if you need to install 'pyloco'. ::

    >>> pip install pyloco

Or, if 'pyloco' is already installed, upgrade 'pyloco' with the following command ::

    >>> pip install -U pyloco

To install 'pcpp' task, run the following 'pyloco' command.  ::

    >>> pyloco install pcpp

Command-line syntax
-------------------

usage: pyloco pcpp [-h] [-o OUTPUT] [-D DEFINES] [-I INCLUDES]
                   [--general-arguments]
                   data 

a wrapper task for pcpp Python C99 preprocessing package

positional arguments:
  data                  File to preprocess (use '-' for stdin)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output to a file instead of stdout
  -D DEFINES            Predefine name as a macro [with value]
  -I INCLUDES           Path to search for unfound #include's
  --general-arguments   Task-common arguments. Use --verbose to see a list of
                        general arguments

forward output variables:
   data                 preprocessed source code


Example
-------

Following example reads 'my.f90' Fortran source file and displays preprocessed output
on screen using XVAL=1 and YVAL=2 macro definitions.

An example Fortran source file of 'my.f90'. ::

        program test
            integer, parameter :: x = XVAL, y = YVAL
            print *, x, "+", y, "=", x+y
        end program

An example pyloco command to preprocess 'my.f90'. ::

        >>> pyloco pcpp my.f90 -D XVAL=1 -D YVAL=2
        #line 1 "my.f90"
               program test
                  integer, parameter :: x = 1, y = 2
                  print *, x, "+", y, "=", x+y
               end program
