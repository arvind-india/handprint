'''
exceptions.py: exceptions defined by Handprint

Authors
-------

Michael Hucka <mhucka@caltech.edu> -- Caltech Library

Copyright
---------

Copyright (c) 2018 by the California Institute of Technology.  This code is
open-source software released under a 3-clause BSD license.  Please see the
file "LICENSE" for more information.
'''

class UserCancelled(Exception):
    '''The user elected to cancel/quit the program.'''
    pass

class NetworkFailure(Exception):
    '''Unrecoverable problem involving network operations.'''
    pass

class AuthenticationFailure(Exception):
    '''Problem obtaining or using authentication credentials.'''
    pass

class ServiceFailure(Exception):
    '''Unrecoverable problem involving a remote service.'''
    pass

class RateLimitExceeded(Exception):
    '''The service flagged reports that its rate limits have been exceeded.'''
    pass

class InternalError(Exception):
    '''Unrecoverable problem involving Handprint itself.'''
    pass
