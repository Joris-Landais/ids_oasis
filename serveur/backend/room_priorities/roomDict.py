#nested dictionary with all the rooms available for booking

rooms = {
    'L019':{'type':'petit', 'personnes':12, 'aile':'L', 'numero':19, 'lettre':'', 'tabb':True, 'tabn':False, 'videop': False, 'tele': True},#
     'L026':{'type':'petit', 'personnes':10, 'aile':'L', 'numero':26, 'lettre':'', 'tabb':True, 'tabn':False, 'videop': False, 'tele': True},#
     'L209':{'type':'petit', 'personnes':18, 'aile':'L', 'numero':209, 'lettre':'', 'tabb':True, 'tabn':True, 'videop': False, 'tele': True},#
     'L210':{'type':'petit', 'personnes':18, 'aile':'L', 'numero':210, 'lettre':'', 'tabb':True, 'tabn':True, 'videop': False, 'tele': True},#
     'L211':{'type':'petit', 'personnes':18, 'aile':'L', 'numero':211, 'lettre':'', 'tabb':True, 'tabn':True, 'videop': False, 'tele': True},#
     'L227':{'type':'petit', 'personnes':18, 'aile':'L', 'numero':227, 'lettre':'', 'tabb':True, 'tabn':False, 'videop': False, 'tele': True},#
     'L228':{'type':'petit', 'personnes':18, 'aile':'L', 'numero':228, 'lettre':'', 'tabb':True, 'tabn':False, 'videop': False, 'tele': True},#
     'L313':{'type':'petit', 'personnes':20, 'aile':'L', 'numero':313, 'lettre':'', 'tabb':True, 'tabn':False, 'videop': False, 'tele': True},#
     'L318':{'type':'petit', 'personnes':16, 'aile':'L', 'numero':318, 'lettre':'', 'tabb':True, 'tabn':False, 'videop': False, 'tele': True},#
     'L319':{'type':'petit', 'personnes':16, 'aile':'L', 'numero':319, 'lettre':'', 'tabb':True, 'tabn':False, 'videop': False, 'tele': True},#
     'L321':{'type':'petit', 'personnes':16, 'aile':'L', 'numero':321, 'lettre':'', 'tabb':True, 'tabn':False, 'videop': False, 'tele': True},#
     'L322':{'type':'petit', 'personnes':16, 'aile':'L', 'numero':322, 'lettre':'', 'tabb':True, 'tabn':False, 'videop': False, 'tele': True},#
     'BIBLIO':{'type':'moyen', 'personnes':30, 'aile':'V', 'numero':105, 'lettre':'', 'tabb':True, 'tabn':False, 'videop': False, 'tele': True},#
     'L027':{'type':'moyen', 'personnes':28, 'aile':'L', 'numero':27, 'lettre':'', 'tabb':True, 'tabn':True, 'videop': False, 'tele': True},#
     'L213':{'type':'moyen', 'personnes':48, 'aile':'L', 'numero':213, 'lettre':'', 'tabb':False, 'tabn':True, 'videop': True, 'tele': False},#
     'L218':{'type':'moyen', 'personnes':48, 'aile':'L', 'numero':218, 'lettre':'', 'tabb':False, 'tabn':True, 'videop': True, 'tele': False},#
     'L224':{'type':'moyen', 'personnes':48, 'aile':'L', 'numero':224, 'lettre':'', 'tabb':False, 'tabn':True, 'videop': True, 'tele': False},#
     'L226':{'type':'moyen', 'personnes':30, 'aile':'L', 'numero':226, 'lettre':'', 'tabb':True, 'tabn':False, 'videop': False, 'tele': True},#
     'L312':{'type':'moyen', 'personnes':30, 'aile':'L', 'numero':312, 'lettre':'', 'tabb':False, 'tabn':True, 'videop': True, 'tele': False},#
     'L316':{'type':'moyen', 'personnes':32, 'aile':'L', 'numero':316, 'lettre':'', 'tabb':True, 'tabn':True, 'videop': True, 'tele': False},
     'V106B':{'type':'moyen', 'personnes':33, 'aile':'V', 'numero':106, 'lettre':'B', 'tabb':False, 'tabn':True, 'videop': True, 'tele': False},#
     'V124':{'type':'moyen', 'personnes':24, 'aile':'V', 'numero':124, 'lettre':'', 'tabb':True, 'tabn':True, 'videop': False, 'tele': True},#
     'V106A':{'type':'grand', 'personnes':64, 'aile':'V', 'numero':106, 'lettre':'A', 'tabb':False, 'tabn':True, 'videop': True, 'tele': False},#
     'V107':{'type':'grand', 'personnes':132, 'aile':'V', 'numero':107, 'lettre':'', 'tabb':False, 'tabn':True, 'videop': True, 'tele': False},#
     'V005A':{'type':'projet', 'personnes':12, 'aile':'V', 'numero':5, 'lettre':'A', 'tabb':True, 'tabn':True, 'videop': True, 'tele': False},#
     'V005B':{'type':'projet', 'personnes':10, 'aile':'V', 'numero':5, 'lettre':'B', 'tabb':True, 'tabn':False, 'videop': False, 'tele': True},#
     'V005C':{'type':'projet', 'personnes':5, 'aile':'V', 'numero':5, 'lettre':'C', 'tabb':True, 'tabn':False, 'videop': False, 'tele': True},#
     'V005D':{'type':'projet', 'personnes':5, 'aile':'V', 'numero':5, 'lettre':'D', 'tabb':True, 'tabn':False, 'videop': False, 'tele': True},#
     'V334':{'type':'projet', 'personnes':50, 'aile':'V', 'numero':334, 'lettre':'', 'tabb':True, 'tabn':False, 'videop': True, 'tele': False},#
     'V335':{'type':'projet', 'personnes':25, 'aile':'V', 'numero':335, 'lettre':'', 'tabb':False, 'tabn':False, 'videop': True, 'tele': True},#
     'V111':{'type':'mixte', 'personnes':12, 'aile':'V', 'numero':111, 'lettre':'', 'tabb':True, 'tabn':False, 'videop': False, 'tele': True},#
     'V112':{'type':'mixte', 'personnes':18, 'aile':'V', 'numero':112, 'lettre':'', 'tabb':True, 'tabn':False, 'videop': False, 'tele': False},#
     'V115':{'type':'mixte', 'personnes':32, 'aile':'V', 'numero':115, 'lettre':'', 'tabb':False, 'tabn':True, 'videop': False, 'tele': True},#
     'V116':{'type':'mixte', 'personnes':32, 'aile':'V', 'numero':116, 'lettre':'', 'tabb':False, 'tabn':False, 'videop': False, 'tele': True},#
     'V119':{'type':'mixte', 'personnes':20, 'aile':'V', 'numero':119, 'lettre':'', 'tabb':True, 'tabn':False, 'videop': False, 'tele': True}#
}  