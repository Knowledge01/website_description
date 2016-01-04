# -*- coding: utf-8 -*-
{
    'name': u'网站描述',
    'category': 'Tools',
    'sequence': 1,
    'summary': u'电商中添加网站描述。',
    'website': 'http://www.metochina.cn',
    'version': '1.0',
    'author':'Albert',
    'description': u"""
    电商中添加网站描述
    """,


    'depends': ['base','website','website_sale'],
    'data': [
        'views/albert_company.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}