# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import pcpp
import pyloco

class PcppTask(pyloco.Task):
    """a wrapper task for pcpp Python C99 preprocessing package

'pcpp' task wraps pcpp Python C99 preprocessing package to work with other Pyloco tasks.


Example
-------

.. code-block:: fortran
       :linenos:
       :caption: my.f90

       program test
          integer, parameter :: x = XVAL, y = YVAL
          print *, x, "+", y, "=", x+y
       end program

.. code-block:: bash
       :linenos:
       :caption: example command

       >>> pyloco pcpp my.f90 -D XVAL=1 -D YVAL=1 -o pcpp_my.f90
"""
    _name_ = "pcpp"
    _version_ = "0.1.0"

    def __init__(self, parent):

        self.add_data_argument("data", nargs="*",
                               help="Files to preprocess (use \'-\' for stdin)")

        self.add_option_argument("-o", "--output",
                                 help="Output to a file instead of stdout")
        self.add_option_argument("-D", dest="defines", nargs=1, action="append",
                                 help="Predefine name as a macro [with value]")
        self.add_option_argument("-I", dest="includes", nargs=1, action="append",
                                 help="Path to search for unfound #include's")

    def perform(self, targs):

        valid_opts = {"output": ("-o", None, False),
                      "defines": ("-D", 1, True), "includes": ("-I", 1, True)}
        argv = ["pcpp"]

        for d in targs.data:
            argv.append(d)

        for opt, (flag, nargs, append) in valid_opts.items():
            val = getattr(targs, opt, None)

            if val:
                if append:
                    for v in val:
                        if nargs is None:
                            argv.extend([flag, v])     

                        else:
                            argv.extend([flag, *v])     
                else:
                    if nargs is None:
                        argv.extend([flag, val])     

                    else:
                        argv.extend([flag, *val])     

        p = pcpp.cmd.CmdPreprocessor(argv)
        return p.return_code

#argp.add_argument('inputs', metavar = 'input', default = [sys.stdin], nargs = '*', action = FileAction, help = 'Files to preprocess (use \'-\' for stdin)')
#argp.add_argument('-o', dest = 'output', metavar = 'path', type = argparse.FileType('wt'), default=sys.stdout, nargs = '?', help = 'Output to a file instead of stdout')
#argp.add_argument('-D', dest = 'defines', metavar = 'macro[=val]', nargs = 1, action = 'append', help = 'Predefine name as a macro [with value]')
#argp.add_argument('-U', dest = 'undefines', metavar = 'macro', nargs = 1, action = 'append', help = 'Pre-undefine name as a macro')
#argp.add_argument('-N', dest = 'nevers', metavar = 'macro', nargs = 1, action = 'append', help = 'Never define name as a macro, even if defined during the preprocessing.')
#argp.add_argument('-I', dest = 'includes', metavar = 'path', nargs = 1, action = 'append', help = "Path to search for unfound #include's")
##argp.add_argument('--passthru', dest = 'passthru', action = 'store_true', help = 'Pass through everything unexecuted except for #include and include guards (which need to be the first thing in an include file')
#argp.add_argument('--passthru-defines', dest = 'passthru_defines', action = 'store_true', help = 'Pass through but still execute #defines and #undefs if not always removed by preprocessor logic')
#argp.add_argument('--passthru-unfound-includes', dest = 'passthru_unfound_includes', action = 'store_true', help = 'Pass through #includes not found without execution')
#argp.add_argument('--passthru-unknown-exprs', dest = 'passthru_undefined_exprs', action = 'store_true', help = 'Unknown macros in expressions cause preprocessor logic to be passed through instead of executed by treating unknown macros as 0L')
#argp.add_argument('--passthru-comments', dest = 'passthru_comments', action = 'store_true', help = 'Pass through comments unmodified')
#argp.add_argument('--passthru-magic-macros', dest = 'passthru_magic_macros', action = 'store_true', help = 'Pass through double underscore magic macros unmodified')
#argp.add_argument('--disable-auto-pragma-once', dest = 'auto_pragma_once_disabled', action = 'store_true', default = False, help = 'Disable the heuristics which auto apply #pragma once to #include files wholly wrapped in an obvious include guard macro')
#argp.add_argument('--line-directive', dest = 'line_directive', metavar = 'form', default = '#line', nargs = '?', help = "Form of line directive to use, defaults to #line, specify nothing to disable output of line directives")
#argp.add_argument('--debug', dest = 'debug', action = 'store_true', help = 'Generate a pcpp_debug.log file logging execution')
#argp.add_argument('--time', dest = 'time', action = 'store_true', help = 'Print the time it took to #include each file')
#argp.add_argument('--filetimes', dest = 'filetimes', metavar = 'path', type = argparse.FileType('wt'), default=None, nargs = '?', help = 'Write CSV file with time spent inside each included file, inclusive and exclusive')
#argp.add_argument('--compress', dest = 'compress', action = 'store_true', help = 'Make output as small as possible')
#argp.add_argument('--version', action='version', version='pcpp ' + version)
#args = argp.parse_known_args(argv[1:])
#
