"""6 - O DBA da empresa criou um script para fazer uma atualização no banco de dados
MongoDB:
var sku = "" // a pessoa informa o sku aqui
var estoque = 0 // valor a ser informado do novo estoque
db.produto.update(
{
sku: sku
},
{
$inc: estoque
}
)
O problema que esse script está em JavaScript do MongoDB. Logo, escreva para
nós a função Python ajustar_estoque() com o seus devidos parâmetros para que
realize a atualização na coleção produto conforme o script que o DBA passou para

nós.
Tempo estimado: 10 minutos. Dificuldade: média. A pessoa sabe ler o script do
MongoDB? Consegue ver e traduzir o que precisamos para o Python?"""

from pymongo import  MongoClient

def obter_colecao_mongodb(url_conexao, colecao):
    cliente = MongoClient(url_conexao)
    db = cliente.get_database()
    coll = db.get_collection(colecao)

    return coll


def update_product():
    sku = {"sku": input('Digite o SKU: ')}
    quant = {"$set":{"estoque": int(input("Digite a quantidade: ")) }}
    
    data = obter_colecao_mongodb("mongodb://root:root@localhost:27017/teste_prod?authSource=admin&retryWrites=true&w=majority", "produto")
    data.update_one(sku, quant)
    print("\nItem atualizado!")


update_product()

