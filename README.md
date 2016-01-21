<h3>Information</h3>
This repository contains samples in different modules.  
Every folder is a module which you can easily install to see how things work or you can browse the code!

<h3>Module button_action_demo</h3>
This module will learn you how to create buttons at the top of forms and how to make it perform actions.
All Python (model data) is under models/button_action_demo.py and you can find the views under views/button_view.xml.

<h3>Module default_data_demo</h3>
This module will learn you how to automatically insert default data in to a database. It will create a new model (demo.default.data) which is filled with records that are made in the file defaultdata.xml (under data/ folder).

<h3>Module inherit_report_demo</h3>
This module will learn you how to inherit existing QWeb reports and how to modify them.
In this example I will modify the default quotation/order report and only show the description with the total price.
To make it look a bit better I've added a table header color.

<h3>Module logging_demo</h3>
This module will learn you how to create log statements in Odoo. You can use these log statements to debug values
or to write unusual behaviour to the Odoo logfile.

<h3>Module many2many_default_data_demo</h3>
This module is a new module from scratch that inherits sale.order. It will create a new many2many to the model sale.order.printorder and will automatically fill this many2many with all the data from the model sale.order.printorder.
In this sample you can see how to use default=, how to use functions and how to use self.pool.

<h3>Module many2many_handle_widget_demo</h3>
This module is a new module from scratch that inherits sale.order. In this module you can see how the handle widget (drag and drop) works
with many2many and how sequencing works.

<h3>Module on_change_function</h3>
This module is a new module from scratch which inherits the model product.template.
It adds the fields CostPrice and ShippingCost, which you can see in models.py. This is also where the on_change event is programmed. The fields are then added to the products view in the file templates.xml, which inherits the default product view.

<h3>Module project_task_agenda_colouring</h3>
<b>Note:</b> If you want to use this module you will also need to install the module web_widget_color. This module builds on top of that module.
This module will give you the ability to add custom colours to tasks which will then re-color the agenda view.
There is a new view created 'Agenda statuses' where you can create a status with a color from the color picker. On the project task you can then choose an agenda status. When you'd go to the agenda view you will see it being re-coloured.
This module does almost the same as ```project_task_kanban_colouring``` but this module colours the agenda view, not the Kanban view.
Agenda statusses view:<br/>
<img src="http://i.imgur.com/ZlHcm9R.png" alt="Agenda statuses"/><br/>
Project task view:<br/>
<img src="http://i.imgur.com/OhP9Vau.png" alt="Project task view"/><br/>
Tasks calendar view:<br/>
<img src="http://i.imgur.com/3PwRhEG.png" alt="Project tasks calendar view"/>

<h3>Module project_task_kanban_colouring</h3>
<b>Note:</b> If you want to use this module you will also need to install the module web_widget_color. This module builds on top of that module.
This module will give you the ability to add custom colours to tasks which will then re-color the agenda view.
There is a new view created 'Agenda statuses' where you can create a status with a color from the color picker. On the project task you can then choose an agenda status. When you'd go to the kanban view you will see it being re-coloured.
This module does almost the same as ```project_task_agenda_colouring``` but this module colours the Kanban view, not the agenda view.
Agenda statusses view:<br/>
<img src="http://i.imgur.com/ZlHcm9R.png" alt="Agenda statuses"/><br/>
Project task view:<br/>
<img src="http://i.imgur.com/OhP9Vau.png" alt="Project task view"/><br/>
Tasks kanban view:<br/>
<img src="http://i.imgur.com/zIy1zoX.png" alt="Project task kanban view"/>

<h3>Module sale</h3>
This module is the default sale module with a few modifications. All the changes can be seen in sale.py and sale_view.xml.<br />
Changes in sale.py:
```
    def _get_default_currency(self, cr, uid, context=None):
        res = self.pool.get('res.company').search(cr, uid, [('currency_id','=','EUR')], context=context)
        return res and res[0] or False

    _columns = {
        #This fills the Many2one with all data from res.currency
        'currency_id_invoices': fields.many2one('res.currency', string="Valuta", required=True),
      
    _defaults = {
        #This makes the function go off that sets EUR.
        'currency_id_invoices': _get_default_currency,
  ```
Changes in sale_view.xml:
  ```
    <field name="currency_id_invoices"/>
  ```
  
<h3>Module scheduler_demo</h3>
This module is a new module, from scratch, which creates a new model (scheduler.demo), new views and an automated action (scheduler). This module will learn you how to create an automated action from scratch, how to loop over all records in a model and how to update those values from within a scheduler.

<h3>Module static_resources_demo</h3>
This module is a new module, from scratch which creates a new CSS and JavaScript file.
This module will learn you how to create new static files and how to add them to the main Odoo CSS / JavaScript.
 
<h3>Module statusbar_demo</h3>
This module is a new module, from scratch, which creates a new model (statusbar.demo) and new views.
This module will learn you how to create a statusbar (selection) and how to handle different states and writing on the current record. You will learn how to add buttons, how to trigger functions and how to change the state of your record.

<h3>Module upload_images</h3>
This module is a new module, from scratch, which creates a new model (upload_images.tutorial), a new report (report_images.xml) and a new menu_item named 'Images' under Sales. In this new menu item you can upload images in multiple sizes and you will see a new report detail here. With this report you will see the image printed in multiple sizes.

<h3>Module web_widget_color</h3>
This module adds a colour picker widget to Odoo. The picker itself is inspired on the <a href="http://jscolor.com">jsColor </a> library.
To use this widget you need to create a char field in with a size of atleast 7 characters in the database:
```
color = fields.Char(
    string="Color",
    help="Choose your color"
)
```
Afterwards call it in the view with ```widget="color"```:
```
<field name="arch" type="xml">
    <tree string="View name">
        ...
        <field name="name"/>
        <field name="color" widget="color"/>
        ...
    </tree>
</field>
```
Picker sample:<br/>
<img src="/web_widget_color/images/picker.png"/><br/>
Tree view sample:<br/>
<img src="/web_widget_color/images/list_view.png"/>

<h3>Module xpath_expressions</h3>
This module is a new module, from scratch which inherits the model product.template and inherits the product view (sale > products). In this sample you can see how to add new pages, groups or fields with xpath expressions. You can see the samples in templates.xml.
