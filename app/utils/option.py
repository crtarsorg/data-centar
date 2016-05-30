from flask.ext.babel import gettext

class Option():

    def __init__(self, value):
        self.value = value
        self.label = gettext(value)

    def label(self):
    	return self.label

    def value(self):
    	return self.value