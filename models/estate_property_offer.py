from odoo import models, fields, api
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Gayrimenkul Teklif Tablosu"

    price = fields.Float()
    partner_id=fields.Many2one("res.partner",required = True)
    property_id =fields.Many2one("estate.property",required = True)
    status= fields.Selection(
        selection=[('accepted','Kabul Et'),('refused','Reddet')])


    @api.model_create_multi
    def create(self, vals_list):
        offers = super().create(vals_list)
        for offer in offers:
            if offer.property_id.state == 'new':
                offer.property_id.state = 'offer_received'
        return offers

    def accept_offer(self):
        for record in self:
            if record.property_id.state == 'offer_accepted':
                raise UserError("Bu Gayrimenkulun Zaten Kabul Edilmis Teklifi Var")
            record.status = 'accepted'
            record.property_id.write({
                "buyer_id": record.partner_id.id,
                "selling_price":record.price,
                "state": "offer_accepted",
            })

    def refuse_offer(self):
        for record in self:
            if record.status == 'accepted':
                raise UserError("Kabul Edilmis Teklifler Reddedilemez")
            else:
                record.status = 'refused'
   
   #offer price 0 dan buyuk olmali
    _check_offer_price = models.Constraint(
        'CHECK(price > 0)',
        'Teklif fiyati 0 dan buyuk olmali',
    )