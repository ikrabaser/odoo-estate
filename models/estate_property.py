from odoo import models, fields, api
from odoo.exceptions import UserError



class EstateProperty(models.Model):
    _name= "estate.property"
    _description= "Gayrimenkul Tablosu"

    name=fields.Char(required=True)
    description= fields.Text()
    date_availability = fields.Date(string="Availability Date")
    expected_price= fields.Float()
    selling_price= fields.Float()
    bedrooms= fields.Integer()
    living_area= fields.Integer()
    has_garden=fields.Boolean()
    garden_area=fields.Integer()
    total_area=fields.Integer(compute = "_compute_total_area")
    property_type_id = fields.Many2one('estate.property.type',string = 'Gayrimenkul Tipi')
    buyer_id= fields.Many2one("res.partner")
    sales_person_id= fields.Many2one("res.users")
    offer_ids=fields.One2many("estate.property.offer","property_id")
    best_price=fields.Float(compute="_compute_best_price", string = "En Iyi Teklif")
    tag_ids=fields.Many2many("estate.property.tag")
    state = fields.Selection(
        selection= [('new','Yeni'), ('offer_received','Teklif Alindi'), ('offer_accepted',"Teklif Kabul Edildi"),
        ('sold','Satildi'),('cancelled','Iptal Edildi')],default = 'new' , required=True
        

    )

    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area=record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price=max(record.offer_ids.mapped("price"))
            else:
                record.best_price = 0.0
    
    def sell_property(self):
        for record in self:
            if record.state == 'cancelled':
                raise UserError("Iptal Edilmis Gayrimenkuller Satilamaz")
            else:
                record.state='sold'
    def cancel_property(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("Satilmis Gayrimenkuller Iptal Edilemez")
            else:
                record.state='cancelled'
