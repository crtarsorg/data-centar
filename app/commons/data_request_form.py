# coding=utf-8
from wtforms import Form, SelectField, SelectMultipleField, BooleanField, TextField, IntegerField

class DataRequestForm(Form):

    #TODO: translate
    parameter = SelectField(u'Parameter',
        choices=[
            ("ukupno", "Ukupno"),
            ("sopstveniPrihodi", "Sopstveni prihodi"),
            ("prihodiBudzeta", "Prihodi budzeta"),
            ("donacije", "Donacije"),
            ("ostali", "Ostali"),
        ])

    data_type = SelectField(u'Tip podataka',
        choices=[
            ('rashodi', 'Rashodi'),
            ('prihodi', 'Prihodi')
        ])

    ukupno_gte = IntegerField('Ukupno')
    ukupno_lte = IntegerField('Ukupno')
    sopstveni_prihodi_gte = IntegerField('Sopstveni Prihodi')
    sopstveni_prihodi_lte = IntegerField('Sopstveni Prihodi')
    prihodi_budzeta_gte = IntegerField('Prihodi Budzeta')
    prihodi_budzeta_lte = IntegerField('Prihodi Budzeta')
    donacije_gte = IntegerField('Donacije')
    donacije_lte = IntegerField('Donacije')
    ostali_gte = IntegerField('Ostali')
    ostali_lte = IntegerField('Ostali')

    ukupno = BooleanField('Ukupno')
    sopstveni_prihodi = BooleanField('Sopstveni Prihodi')
    prihodi_budzeta = BooleanField('Prihodi Budzeta')
    donacije = BooleanField('Donacije')
    ostali = BooleanField('Ostali')
    pocinje_sa = TextField("Klasifikacija broj pocinje sa:")


    years = SelectField(u'Godine',
        choices=[
            (2015, 2015)
        ])

    municipalities = SelectMultipleField(u'Opštine',
        choices=[
            ("chachak", u"Čačak"),
            ("indjija", u"Inđjija"),
            ("kraljevo", "Kraljevo"),
            ("loznitsa", "Loznitsa"),
            ("novi-beograd", "Novi Beograd"),
            ("prijepolje", "Pripolje"),
            ("valjevo", "Valjevo"),
            ("vranje", "Vranje"),
            ("zvezdara", "Zvezdara")
        ])

    classifications = SelectMultipleField(u'Ekonomskih klasifikacija',
        choices=[
            (411, u"411 - Plate, dodaci i naknade zaposlenih (zarade)"),
            (412, u"412 - Socijalni doprinosi na teret poslodavca"),
            (413, u"413 - Naknade u naturi"),
            (414, u"414 - Socijalna davanja zaposlenima"),
            (415, u"415 - Naknade troškova za zaposlene"),
            (416, u"416 - Nagrade zaposlenima i ostali posebni rashodi"),
            (417, u"417 - Odbornički dodatak"),
            (418, u"418 - Sudijski dodatak"),
            (421, u"421 - Stalni troškovi"),
            (422, u"422 - Troškovi putovanja"),
            (423, u"423 - Usluge po ugovoru"),
            (424, u"424 - Specijalizovane usluge"),
            (425, u"425 - Tekuće popravke i održavanje"),
            (426, u"426 - Materijal"),
            (431, u"431 - АМОРТИЗАЦИЈА И УПОТРЕБА СРЕДСТАВА ЗА РАД"),
            (432, u"432 - Amortizacija kultivisane imovine"),
            (433, u"433 - Upotreba dragocenosti"),
            (434, u"434 - Upotreba prirodne imovine"),
            (435, u"435 - Amortizacija nematerijalne imovine"),
            (441, u"441 - Otplata kamata domaćim poslovnim bankama"),
            (442, u"442 - Otplata stranih kamata"),
            (443, u"443 - Otplata kamata po garancijama"),
            (444, u"444 - Prateći troškovi zaduživanja"),
            (452, u"452 - Subvencije privatnim finansijskim institucijama"),
            (453, u"453 - Subvencije javnim finansijskim institucijama"),
            (454, u"454 - SUBVENCIJE PRIVATNIM PREDUZEĆIMA"),
            (461, u"461 - Donacije stranim vladama"),
            (462, u"462 - DOTACIJE MEĐUNARDNIM ORGANIZACIJAMA"),
            (463, u"463 - Transferi ostalim nivoima vlasti"),
            (465, u"465 - Ostale donacije, dotacije i transferi."),
            (472, u"472 - Naknade za socijalnu zaštitu iz budžeta"),
            (481, u"481 - Dotacije nevladinim organizacijama"),
            (482, u"482 - Porezi, obavezne takse, kazne i penali"),
            (483, u"483 - Novčane kazne i penali po rešenju sudova i sudskih tela"),
            (489, u"489 - Rashodi koji se finansiraju iz sredstava za realizaciju nacionalnog investicionog plana"),
            (494, u"494 - Administrativni transferi iz budžeta - Tekući rashodi"),
            (495, u"495 - Administrativni transferi iz budžeta - Izdaci za nefinansijsku imovinu"),
            (496, u"496 - Administrativni transferi iz budžeta - Izdaci za otplatu glavnice i nabavku finansijske imovine")
        ])