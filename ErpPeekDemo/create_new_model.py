import erppeek

client = erppeek.Client('http://localhost:8080', 'ErpPeekDemoDatabase', 'admin', 'admin')
model_proxy = client.model('ir.model')
field_proxy = client.model('ir.model.fields')

values = {
    'model': 'x_example_tutorial',
    'name': 'Example model',
    'state': 'manual',
}

# With this instruction, you are going to create the model
# in the database without one line of python code.
model = model_proxy.create(values)

values = {
    'name': 'x_name',
    'ttype': 'char',
    'size': 64,
    'field_description': 'Firstname',
    'model_id': model.id,
    'model': model.model,
    'domain': '[]',
}
field = field_proxy.create(values)
print('Congratulations your new model has been created!')
