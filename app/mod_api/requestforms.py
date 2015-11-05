# coding=utf-8
from wtforms import Form, SelectField, SelectMultipleField

class SumRequestForm(Form):

    data = SelectField(u'Data',
        choices=[
            ('rashodi', 'Rashodi'),
            ('prihodi', 'Prihodi')
        ])

    years = SelectField(u'Godine',
        choices=[
            (2015, 2015)
        ])

    municipalities = SelectMultipleField(u'Opštine',
        choices=[
            #("cacak", "Čačak"),
            ("indjija", "Indjija"),
            ("kraljevo", "Kraljevo"),
            ("loznica", "Loznica"),
            ("novi-beograd", "Novi Beograd"),
            ("pripolje", "Pripolje"),
            ("valjevo", "Valjevo"),
            ("vranje", "Vranje"),
            ("zvezdara", "Zvezdara")
        ])

    classifications = SelectMultipleField(u'Klasifikacije',
        choices=[
            (411, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
            (412, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
            (413, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
            (414, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
            (415, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
            (416, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
            (417, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
            (418, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
            (419, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
            (421, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
            (422, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
            (423, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
            (424, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
            (425, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
            (426, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
            (427, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
            (428, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
            (429, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        ])

class ClassificationsRequestForm(Form):
    pass