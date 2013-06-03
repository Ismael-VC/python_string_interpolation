#!/usr/bin/env python2

'''
string_interpolation 0.5 (Tested on python 2.7.3):

Ismael VC           < ismael.vc1337@gmail.com >             May-2013

This module provides a simple tool, that eases some of the complexity
of formatting many strings, using a string interpolation aproach.

help(interpolate)
'''

import sys


def get_scope(scope):
    scope = scope.lower()
    caller = sys._getframe(2)
    options = ['l', 'local', 'g', 'global']

    if scope not in options[:2]:
        if scope in options[2:]:
            return caller.f_globals
        else:
            raise ValueError('invalid mode: {0}'.format(scope))
    return caller.f_locals


def interpolate(format_string=str(),sequence=None,scope='local',returns=False):
    """
    interpolate([format_string[, sequence | scope[, returns]]]) -> formated string

    Prints format_string interpolated with the contents of sequence.

    format_string: string to be formated with embeded keyword conversion targets: {}
    sequence: dictionary containing the variables to be substituted in the 
                  format_string.
    scope: string specifying which namespace to use, options are, 'l' or 'local'
           and 'g' or 'global'. (Case insensitive)
    returns: if set to True, returns the string instead of printing it.

    If sequence is omitted, it defaults to the local namespace.
    """

    if type(sequence) is str:
        scope = sequence
        sequence = get_scope(scope)
    else:
        if not sequence:
            sequence = get_scope(scope)

    format = 'format_string.format(**sequence)'
    if returns is False:
        print eval(format)
        
    elif returns is True:
        return eval(format)





####### Here are some examples and limitations: #######

name = 'Maruja'
if __name__ == '__main__':

    import time
    
    # I found this elsewhere.
    def print_timing(func):
        def wrapper(*arg):
            t1 = time.time()
            res = func(*arg)
            t2 = time.time()
            diff = (t2-t1)*1000.0
            interpolate('{func.func_name} took: {diff:0.3g}ms\n')
            return res
        return wrapper

    @print_timing    
    def interpolation_test():
        print '\nstring_interpolation test:\n'
        print 'First\ttest\tEmpty string:'
        interpolate()

        # handle error?
        # interpolate('{}')   

        interpolate('Second\ttest:\tNullifying effect. {{}}')  
        interpolate('Third\ttest:\tHello my name is {{name}}.')
        interpolate('Second\ttest:\tWithout conversion target.')

        # Cant't use negative indexes, why? Also, interpolate several
        # strings and also from several sequences at the same time?
        names = ['Alejandro', 'Jessica', 'Luis']
        interpolate('''Fourth\ttest:\tHello my name is {names[0]}.
\t\t...no! wait my name is {names[2]},       
\t\tjust kidding my name is {names[0]}!''') 
        
        # nonlocal in python 3.x? to interpolate 'Israel'
        name = 'Israel'
        def inner_1():
            interpolate('Fifth\ttest:\tHello my name is {name}.', 'g')
        inner_1()

        name = ('Ismael',)
        message_1 = interpolate('Sixth\ttest:\tHello my name is {name[0]}.', 
                                    returns=True)
        print message_1        
        
        message_2 = interpolate('Seventh\ttest:\tHello my name is {name}.',
                                {'name': 'Oscar'}, returns=True)
        print message_2

        def inner_2():
            name = 'Monica'
            message_4 = interpolate('Eigth\ttest:\tHello my name is {name}.\n',
                                    returns=True)
            print message_4
        inner_2()     
   
    interpolation_test()
