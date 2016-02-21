import erppeek

client = erppeek.Client('http://localhost:8080', 'ErpPeekDemoDatabase', 'admin', 'admin')
#installed_modules = client.modules(installed=True)

#for module in installed_modules['installed']:
#    print(module)

proxy = client.model('ir.module.module')
installed_modules = proxy.browse([('state', '=', 'installed')])

for module in installed_modules:
    print('Installed module: ' + module.name)
