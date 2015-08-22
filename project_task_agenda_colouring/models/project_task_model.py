# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.osv import osv
import logging
_logger = logging.getLogger(__name__)
from openerp.tools.translate import _

#External imports
from random import randint

class ProjectTask(models.Model):
    _inherit = 'project.task'

    agenda_status = fields.Many2one(
        'agenda.status',
        'Agenda status'
    )
    hex_value = fields.Char(
        string="Hex Value",
        related="agenda_status.color",
        store=False,
        size=7
    )

class AgendaStatus(models.Model):
    _name = 'agenda.status'

    name = fields.Char(
        String='Description'
    )
    color = fields.Char(
        string="Color",
        help="Choose your color",
        size=7
    )
