from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class PathogenForm(FlaskForm):
    """Pathogen form."""

    gram_types = [
        ('Gram-positive', 'Gram-positive'),
        ('Gram-negative', 'Gram-negative')
    ]

    aerobe_types = [
        ('Aerobic', 'Aerobic'),
        ('Anaerobic', 'Anaerobic'),
        ('Aerophilic', 'Aerophilic'),
        ('Facultative Anaerobic', 'Facultative Anaerobic'),
        ('NA', 'NA')
    ]


    pathogen_types = [
        ('Pathogen', 'Pathogen'),
        ('Potential Pathogen', 'Potential Pathogen'),
        ('Non Pathogen', 'Non Pathogen'),
        ('NA', 'NA')
    ]

    rank_types = [
        ('species', 'species'),
        ('genus','genus'),
        ('order','order'),
        ('family','family'),
        ('Notin','Notin'),
        ('NA', 'NA')
    ]

    organism = StringField('Organism', [ DataRequired()])
    taxonid = StringField('TaxonId', [ DataRequired()])
    rank = SelectField('Rank', choices=rank_types)
    gram = SelectField('Gram', choices=gram_types)
    aerobe = SelectField('Aerobe', choices=aerobe_types)
    habitat = StringField('Habitat', [ DataRequired()])
    isolation = StringField('Isolation', [ DataRequired()])
    pathostate = SelectField('Pathogenicity', choices=pathogen_types)
    submit = SubmitField('Submit')