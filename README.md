<h3>Information</h3>
This repository contains samples in different modules.  
Every folder is a module which you can easily install to see how things work or you can browse the code!

<h3>Module default_data_demo</h3>
This module will learn you how to automatically insert default data in to a database. It will create a new model (demo.default.data) which is filled with records that are made in the file defaultdata.xml (under data/ folder).

<h3>Module many2many_default_data_demo</h3>
This module is a new module from scratch that inherits sale.order. It will create a new many2many to the model sale.order.printorder and will automatically fill this many2many with all the data from the model sale.order.printorder.
In this sample you can see how to use default=, how to use functions and how to use self.pool.

<h3>Module on_change_function</h3>
This module is a new module from scratch which inherits the model product.template.
It adds the fields CostPrice and ShippingCost, which you can see in models.py. This is also where the on_change event is programmed. The fields are then added to the products view in the file templates.xml, which inherits the default product view.

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

<h3>Module upload_images</h3>
This module is a new module, from scratch which creates a new model (upload_images.tutorial), a new report (report_images.xml) and a new menu_item named 'Images' under Sales. In this new menu item you can upload images in multiple sizes and you will see a new report detail here. With this report you will see the image printed in multiple sizes.

<h3>Module xpath_expressions</h3>
This module is a new module, from scratch which inherits the model product.template and inherits the product view (sale > products). In this sample you can see how to add new pages, groups or fields with xpath expressions. You can see the samples in templates.xml.
