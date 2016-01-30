# -*- coding: utf-8 -*-
#Odoo imports
from openerp import models, fields, api

class statusbar(models.Model):
    _name = 'statusbar.demo'
    name = fields.Char('Name', required=True)
    """
    This selection field contains all the possible values for the statusbar.
    The first part is the database value, the second is the string that is showed. Example:
    ('finished','Done'). 'finished' is the database key and 'Done' the value shown to the user
    """
    state = fields.Selection([
            ('concept', 'Concept'),
            ('started', 'Started'),
            ('progress', 'In progress'),
            ('finished', 'Done'),
            ],default='concept')

    #This function is triggered when the user clicks on the button 'Set to concept'
    @api.multi
    def concept_progressbar(self):
	self.ensure_one()
	self.write({
	    'state': 'concept',
	})

    #This function is triggered when the user clicks on the button 'Set to started'
    @api.multi
    def started_progressbar(self):
	self.ensure_one()
	self.write({
	    'state': 'started'
	})

    #This function is triggered when the user clicks on the button 'In progress'
    @api.multi
    def progress_progressbar(self):
	self.ensure_one()
	self.write({
	    'state': 'progress'
	})

    #This function is triggered when the user clicks on the button 'Done'
    @api.multi
    def done_progressbar(self):
	self.ensure_one()
	self.write({
	    'state': 'finished',
	})
