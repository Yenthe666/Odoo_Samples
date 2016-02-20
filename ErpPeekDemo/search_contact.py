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

# Calling the remote ORM create method to search for records 
contact_ids = sock.execute(dbname, uid, pwd, 'res.partner', 'search', [])
print('Contact IDs found: ' + str(contact_ids))

# Get the details from all contacts
for contact_id in contact_ids:
    # Get the details by the id
    contact = sock.execute(dbname, uid, pwd, 'res.partner', 'read', contact_id, [])
    print('Contact name: ' + contact['name'])
