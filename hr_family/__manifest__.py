{
    'name': 'Employee Family Information',
    'version': "15.0.1.0.0",
    'category': 'Generic Modules/Human Resources',
    'author':  'Odoo Bangladesh',
    'website': 'http://odoobangladesh.com',
    'license': 'LGPL-3',
    'depends': [
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_children.xml',
        'views/hr_employee.xml',
    ],
    'installable': True,
}
