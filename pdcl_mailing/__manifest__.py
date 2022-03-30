{
    "name": "Create Mailing Lists For PDCL",
    'license': 'LGPL-3',
    'version': "15.0.1.0.0",
    "category": "Generic Modules/Human Resources",
    'author':  'Odoo Bangladesh',
    'website': 'http://odoobangladesh.com',
    "depends": ['base', "mass_mailing"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/mail_list_select_view.xml",
    ],
'images': ['static/description/banner.png'],


    "installable": True,

'images': ['static/description/banner.png'],

    'version': '15.0.1.0.1',

    'assets': {
        'web.assets_backend': [
            '/ks_binary_file_preview/static/src/js/ks_binary_preview.js',
            '/ks_binary_file_preview/static/src/js/widget/ksListDocumentViewer.js',

        ],

        'web.assets_qweb': ['ks_binary_file_preview/static/src/xml/ks_binary_preview.xml',
                            'ks_binary_file_preview/static/src/js/widget/ksListDocumentViewer.xml',
                            ],
    },
}
