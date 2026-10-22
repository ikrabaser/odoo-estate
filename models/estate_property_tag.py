from odoo import models, fields

class EstatePropertytag(models.Model):
    _name= "estate.property.tag"
    _description = "Gayrimenkul Tagi Tablosu"

    name = fields.Char(required = True)
    color = fields.Integer("Color")
    _unique_tag_name = models.Constraint(
        'UNIQUE(name)',
        'Gayrimenkul tagi tekduze olmali',
    )