from flask.ext.wtf import Form
from wtforms import TextField, HiddenField, IntegerField, BooleanField
from wtforms.validators import Required

class NewThingForm(Form):
    name = TextField('name', validators = [Required()])
    delta = IntegerField('delta', validators = [Required()])

class EditThingForm(Form):
    name = TextField('name', validators = [Required()])
    delta = IntegerField('delta', validators = [Required()])
    delete = BooleanField('delete')
