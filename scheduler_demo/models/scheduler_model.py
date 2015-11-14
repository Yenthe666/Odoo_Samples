# -*- coding: utf-8 -*-
from openerp import models, fields, api
#Import logger
import logging
#Get the logger
_logger = logging.getLogger(__name__)

#External import
import datetime

class scheduler_demo(models.Model):
    _name = 'scheduler.demo'
    name = fields.Char(required=True)
    numberOfUpdates = fields.Integer('Number of updates', help='The number of times the scheduler has run and updated this field')
    lastModified = fields.Date('Last updated')

    #This function is called when the scheduler goes off
    def process_demo_scheduler_queue(self, cr, uid, context=None):
	scheduler_line_obj = self.pool.get('scheduler.demo')
	#Contains all ids for the model scheduler.demo
  	scheduler_line_ids = self.pool.get('scheduler.demo').search(cr, uid, [])   
	#Loops over every record in the model scheduler.demo
        for scheduler_line_id in scheduler_line_ids :
	    #Contains all details from the record in the variable scheduler_line
            scheduler_line =scheduler_line_obj.browse(cr, uid,scheduler_line_id ,context=context)
	    numberOfUpdates = scheduler_line.numberOfUpdates
	    #Prints out the name of every record.
            _logger.info('line: ' + scheduler_line.name)
	    #Update the record
	    scheduler_line_obj.write(cr, uid, scheduler_line_id, {'numberOfUpdates': (numberOfUpdates +1), 'lastModified': datetime.date.today()}, context=context) 
	    