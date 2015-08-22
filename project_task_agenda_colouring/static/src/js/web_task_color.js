openerp.project_task_agenda_colouring = function (instance) {
    instance.web_calendar.CalendarView = instance.web_calendar.CalendarView.extend({
        event_data_transform: function (event) {
            var res = this._super.apply(this, arguments);
	    //This would go off when there is no color set for hex_value. You could control this too.
            if (res && res.hasOwnProperty('className')) {
		//If you would uncomment the next line it would use the default colour that is set for the user. (default behaviour from Odoo calendars)
                //res.className = res.className.substring(0, res.className.indexOf(' calendar_color_'));
		res.backgroundColor = '#DBDBDB';
		if(res.title.indexOf('false') > -1)
		{
		   res.title = res.title.substring(0, res.title.indexOf(','));
		}
            }
            if (event.hex_value && res.title) {
                res.backgroundColor = event.hex_value;
                res.title = res.title.substring(0, res.title.indexOf(', ' + event.hex_value));
            }
            return res;
        }
    });

};
