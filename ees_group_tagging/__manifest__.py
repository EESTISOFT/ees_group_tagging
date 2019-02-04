{
    'name': 'EESTISOFT group tagging',
    'version': '12.0.4.8',
    'author': 'EESTISOFT, ''Hideki Yamamoto, ''Giulio Milani',
	'mantainer':'EESTISOFT',
	'license':'LGPL-3',
    'category': 'Productivity',
    'website': 'https://eestisoft.com',
    'sequence': 2,
    'summary': 'Adds group tag / untagging for partners',
    'description': """
Adds group tag / untagging for partners.
	
Made with love.
    """,
	'images':['thumb.png'],
    'depends': ['base','contacts'],
    'data': ['views/ees_group_tagging.xml','views/ir.model.access.csv'],
    'installable': True,
    'application': True,
    'auto_install': False
}
