# -*- coding: utf-8 -*-


###
# Copyright (c) 2009, Tuxce <tuxce.net@gmail.com>
# All rights reserved.
#
#
###

import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Archfr', True)


Archfr = conf.registerPlugin('Archfr')
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(Archfr, 'someConfigVariableName',
#     registry.Boolean(False, """Help for someConfigVariableName."""))
conf.registerGroup(Archfr, 'wiki')
conf.registerGlobalValue(Archfr.wiki, 'max',
    registry.NonNegativeInteger(2, """Indique le maximum de pages
		à afficher."""))
conf.registerGroup(Archfr, 'bug')
conf.registerGlobalValue(Archfr.bugs, 'max',
    registry.NonNegativeInteger(2, """Indique le maximum de bugs
		à afficher."""))
conf.registerGroup(Archfr, 'pkg')
conf.registerGlobalValue(Archfr.pkg, 'max',
    registry.NonNegativeInteger(2, """Indique le maximum de paquets
		à afficher."""))
conf.registerGroup(Archfr, 'pkgfile')
conf.registerGlobalValue(Archfr.pkgfile, 'max',
    registry.NonNegativeInteger(2, """Indique le maximum de paquets/fichiers
		à afficher."""))
conf.registerGroup(Archfr, 'quote')
conf.registerGlobalValue(Archfr.quote, 'theme',
    registry.String('chuck', """Indique le theme des citations.""",
        private=True))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79: