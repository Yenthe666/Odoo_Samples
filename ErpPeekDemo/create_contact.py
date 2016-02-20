import xmlrpclib

username = 'admin' # The Odoo user
pwd = 'admin'# The password of the Odoo user
dbname = 'ErpPeekDemoDatabase' # The Odoo database

# OpenERP Common login Service proxy object 
sock_common = xmlrpclib.ServerProxy ('http://localhost:8080/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)

# replace localhost with the address of the server if it is not on the same server
# OpenERP Object manipulation service 
sock = xmlrpclib.ServerProxy('http://localhost:8080/xmlrpc/object')

partner_record = {
    'name': 'Fabien',
    'email': 'example@odoo.com'
    }

# Calling the remote ORM create method to create a record 
result = sock.execute(dbname, uid, pwd, 'res.partner', 'create', partner_record)
print('Inserted new partner! Id: ' + str(result))
