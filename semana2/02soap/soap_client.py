from zeep import Client

client = Client('http://localhost:8000')
result = client.service.Saludar(nombre="Fiorela")
print(result)