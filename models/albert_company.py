# -*- coding: utf-8 -*-
from openerp import models, api, _, fields
class liuxl_test(models.Model):
    _inherit="res.company"
    name1 = fields.Char("网站说明")
    description = fields.Char("描述")
    note = fields.Text("备注")
    image = fields.Binary("图片")
