import erppeek
# You can use this client if you have Erppeek installed and have a erppeek.ini file
# client = erppeek.Client.from_config('ErpPeekDemoDatabase')
client = erppeek.Client('http://localhost:8080', 'ErpPeekDemoDatabase', 'admin', 'admin')

modules = client.modules('crm', installed=False)
if 'crm' in modules['uninstalled']:
    client.install('crm')
