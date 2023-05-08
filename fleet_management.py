from odoo import models, fields

class Vehicle(models.Model):
    _name = 'fleet.vehicle'
    _description = 'Vehicle'

    license_plate = fields.Char(string='Matrícula')
    brand = fields.Char(string='Marca')
    model = fields.Char(string='Model')
    year = fields.Integer(string='Any')
    current_mileage = fields.Float(string='Kilòmetres actuals')
    itv_valid = fields.Boolean(string='Té la ITV vigent?')
    owner_name = fields.Char(string='Nom del propietari')
    owner_dni = fields.Char(string='DNI del propietari')
