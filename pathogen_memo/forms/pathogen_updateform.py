from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class PathogenUpdateForm(FlaskForm):
    """Pathogen form."""
    id = StringField('Id', [ DataRequired()])
    organism = StringField('Organism', [ DataRequired()])
    taxonid = StringField('TaxonId', [ DataRequired()])
    rank = StringField('Rank', [ DataRequired()])
    gram = StringField('Gram', [ DataRequired()])
    aerobe = StringField('Aerobe', [ DataRequired()])
    habitat = StringField('Habitat', [ DataRequired()])
    isolation = StringField('Isolation', [ DataRequired()])
    pathostate =StringField('Pathogenicity', [ DataRequired()])
    submit = SubmitField('Submit')