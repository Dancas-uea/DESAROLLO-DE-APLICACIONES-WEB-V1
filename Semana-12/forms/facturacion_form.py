from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class FacturacionForm(FlaskForm):
    numero = StringField('Número de Factura', validators=[
        DataRequired(message='El número de factura es obligatorio.'),
        Length(min=3, max=20, message='El número debe tener entre 3 y 20 caracteres.')
    ])
    cliente = StringField('Cliente', validators=[
        DataRequired(message='El cliente es obligatorio.'),
        Length(min=3, max=100, message='El nombre del cliente debe tener entre 3 y 100 caracteres.')
    ])
    fecha = StringField('Fecha (YYYY-MM-DD)', validators=[
        DataRequired(message='La fecha es obligatoria.'),
        Length(min=10, max=10, message='Use el formato YYYY-MM-DD.')
    ])
    total = FloatField('Total ($)', validators=[
        DataRequired(message='El total es obligatorio.'),
        NumberRange(min=0.01, message='El total debe ser mayor a 0.')
    ])
    submit = SubmitField('Guardar Factura')