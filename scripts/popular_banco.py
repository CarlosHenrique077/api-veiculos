from app.core.database import configurar_banco, get_colecao

configurar_banco()
colecao = get_colecao()

exemplos = [
    {"marca": "Fiat", "modelo": "Uno", "ano": 2015, "placa": "ABC1D23", "cor": "Branco"},
    {"marca": "Chevrolet", "modelo": "Onix", "ano": 2020, "placa": "XYZ9K87", "cor": "Preto"},
    {"marca": "Volkswagen", "modelo": "Gol", "ano": 2012, "placa": "QWE4R56", "cor": None},
]

for v in exemplos:
    if not colecao.find_one({"placa": v["placa"]}):
        colecao.insert_one(v)

print("Banco populado com sucesso!")