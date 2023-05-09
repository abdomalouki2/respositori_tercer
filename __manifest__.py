{
    'name': 'Fleet Management',
    'version': '1.0',
    'category': 'Fleet',
    'description': "Aquest modul es de Vehicles",
    'author': 'Abde-Tarik',
    'depends': ['base'],
    'data': [
        'data/fleet.vehicle.csv'
        'security/ir.model.access.csv',
        'views/fleet_vehicle_views.xml'
    ],
    'installable': True,
    'aplication':True,
    'auto_install': False,
}
