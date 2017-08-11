# -*- coding: utf-8 -*-

PASSWORD = '95059402'
TIME_LIMIT = 2

db.define_table('tbAction',
                Field('mCommand', requires=IS_IN_SET([-1,1]), label=T('Command')),
                Field('mDateTime', 'datetime',default=lambda: request.now, readable=False, writable=False)
               )
