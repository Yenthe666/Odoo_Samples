# -*- encoding: utf-8 -*-
from odoo import models, fields, api

class res_partner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def send_mail_template(self):
        # Find the e-mail template
        template = self.env.ref('mail_template_demo.example_email_template')
        # You can also find the e-mail template like this:
        # template = self.env['ir.model.data'].get_object('mail_template_demo', 'example_email_template')

        # Send out the e-mail template to the user
        self.env['mail.template'].browse(template.id).send_mail(self.id)