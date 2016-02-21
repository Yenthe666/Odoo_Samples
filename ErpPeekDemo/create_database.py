import erppeek

DATABASE = 'ErpPeekDemoDatabase'
SERVER = 'http://localhost:8080'
ADMIN_PASSWORD = 'admin'

client = erppeek.Client(server=SERVER)

if not DATABASE in client.db.list():
    print("The database does not exist yet, creating one!")
    client.create_database(ADMIN_PASSWORD, DATABASE)
else:
    print("The database " + DATABASE + " already exists.")
