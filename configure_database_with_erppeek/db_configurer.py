import erppeek

database = 'Example'
server = 'http://localhost:8069'
admin_password = 'admin'
user = 'admin'

# Connect to the database
client = erppeek.Client(server, database, user, admin_password)

config_id = client.model('res.config.settings').search([], limit=1, order='id desc')
if config_id:
    # This means there is already a configuration record - let us write on it
    config_record = client.model('res.config.settings').browse(config_id[0])
    config_record.write({'group_uom': True})
    # Execute the record in order to trigger the save and to apply the values
    config_record.execute()
else:
    # This means there is no configuration yet - let us make a new record
    config_record = client.model('res.config.settings').create({})
    config_record.write({'group_uom': True})
    config_record.execute()
print 'The database is now configured!'
