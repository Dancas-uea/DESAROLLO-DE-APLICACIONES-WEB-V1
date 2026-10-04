from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class ProveedorForm(FlaskForm):
    empresa = StringField('Nombre de la Empresa', validators=[
        DataRequired(message='El nombre de la empresa es obligatorio.'),
        Length(min=3, max=100, message='El nombre debe tener entre 3 y 100 caracteres.')
    ])
    contacto = StringField('Nombre del Contacto', validators=[
        DataRequired(message='El contacto es obligatorio.'),
        Length(min=3, max=100, message='El contacto debe tener entre 3 y 100 caracteres.')
    ])
    telefono = StringField('Teléfono', validators=[
        DataRequired(message='El teléfono es obligatorio.'),
        Length(min=7, max=15, message='El teléfono debe tener entre 7 y 15 caracteres.')
    ])
    ciudad = StringField('Ciudad', validators=[
        DataRequired(message='La ciudad es obligatoria.'),
        Length(min=2, max=50, message='La ciudad debe tener entre 2 y 50 caracteres.')
    ])
    submit = SubmitField('Guardar Proveedor')