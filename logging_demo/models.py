# -*- coding: utf-8 -*-

from openerp import models, fields, api
#Import logger
import logging
#Get the logger
_logger = logging.getLogger(__name__)

class logging_demo(models.Model):
    _name = 'logging.demo'
    name = fields.Char()
    #This function will go off when the user clicks on the button named print_log_data
    def print_log_data(self, cr, uid, ids, context=None):
	_logger.debug("Use _logger.debug for debugging purposes, nothing else.")
	_logger.info("Use _logger.info for information messages. This is used for notifying about something important.")
	_logger.warning("Use _logger.warning for minor issues, which will not crash your module.")
	_logger.error("Use _logger.error to report a failed operation.")
	_logger.critical("Use _logger.critical for critical message: when this goes off the module will not work anymore.")
