odoo.define('example.tour', function(require) {
"use strict";

var core = require('web.core');
var tour = require('web_tour.tour');

var _t = core._t;

tour.register('example_tour', {
    url: "/web",
}, [tour.STEPS.MENU_MORE, {
    trigger: '.o_app[data-menu-xmlid="contacts.menu_contacts"]',
    content: _t('Want to <b>create customers</b>?<br/><i>Click on Contacts to start.</i>'),
    position: 'bottom',
}, {
    trigger: '.o-kanban-button-new',
    content: _t('Let\'s create your first contact.'),
    position: 'bottom',
    width: 200,
}, {
    // The trigger will tell that you would like to input a value in the field 'Name'
    trigger: 'input[placeholder="Name"]',
    extra_trigger: '.o_form_editable',
    // This is the 'hint' / tooltip that is shown to the enduser
    content: _t('Fill in the name of the contact.'),
    // When you run the test (from the developer tools) it will automatically fill in 'James Cook' automatically)
    run: 'text James Cook',
    position: 'right',
}, {
    trigger: '.o_form_button_save',
    content: _t('Save this contact and the modifications you\'ve made to it.'),
    position: 'bottom',
}]);

});