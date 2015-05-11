# -*- coding: utf-8 -*-
from openerp import models, fields, api, tools
from openerp.osv import osv, fields

class upload_images(osv.osv):
    _name = 'upload_images.tutorial'
    _description = 'Tutorial image uploading'

    def _get_image(self, cr, uid, ids, name, args, context=None):
        result = dict.fromkeys(ids, False)
        for obj in self.browse(cr, uid, ids, context=context):
            result[obj.id] = tools.image_get_resized_images(obj.image)
        return result

    def _set_image(self, cr, uid, id, name, value, args, context=None):
        return self.write(cr, uid, [id], {'image': tools.image_resize_image_big(value)}, context=context)

    _columns = {
    'name': fields.char('Name', required=True, translate=True),
    'image': fields.binary("Image",
            help="This field holds the image used as image for our customers, limited to 1024x1024px."),
    'image_medium': fields.function(_get_image, fnct_inv=_set_image,
            string="Image (auto-resized to 128x128):", type="binary", multi="_get_image",
            store={
                'upload_images.tutorial': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },help="Medium-sized image of the category. It is automatically "\
                 "resized as a 128x128px image, with aspect ratio preserved. "\
                 "Use this field in form views or some kanban views."),
    'image_small': fields.function(_get_image, fnct_inv=_set_image,
            string="Image (auto-resized to 64x64):", type="binary", multi="_get_image",
            store={
                'upload_images.tutorial': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Small-sized image of the category. It is automatically "\
                 "resized as a 64x64px image, with aspect ratio preserved. "\
                 "Use this field anywhere a small image is required."),
    }
