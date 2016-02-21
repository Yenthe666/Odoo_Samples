import erppeek
# You can use this client if you have Erppeek installed and have a erppeek.ini file
# client = erppeek.Client.from_config('ErpPeekDemoDatabase')
# The alternative is by specifying the settings by command
client = erppeek.Client('http://localhost:8080', 'ErpPeekDemoDatabase', 'admin', 'admin')

modules = client.modules('sale', installed=False)
if 'sale' in modules['uninstalled']:
    client.install('sale')
