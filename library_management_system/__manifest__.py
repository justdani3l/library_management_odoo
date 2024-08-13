{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Summery',
    'description': 'Library Management',
    'category': 'Library',
    'author': 'Author',
    'website': 'Website',
    'depends': ['base'],
    'data': [
        'views/member_views.xml',
        'views/books_views.xml',
        'views/authors_views.xml',
        'views/issue_books_views.xml',
        'views/categories_views.xml',
        'views/configuration_views.xml',
        'views/employees_views.xml',
        'views/invoice_views.xml',
        'views/menu.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
