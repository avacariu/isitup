from flask.ext.wtf import Form
from wtforms import TextField, HiddenField, IntegerField, BooleanField
from wtforms.validators import Required, ValidationError

def positive(form, field):
    if field.data <= 0:
        raise ValidationError('Field must be positive')

class NewThingForm(Form):
    name = TextField('name', validators = [Required()])
    delta = IntegerField('delta', validators = [Required(), positive])

class EditThingForm(Form):
    name = TextField('name', validators = [Required()])
    delta = IntegerField('delta', validators = [Required(), positive])
    delete = BooleanField('delete')
