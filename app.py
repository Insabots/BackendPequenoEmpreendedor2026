import requests
from complementos.empresas import Empresa
from complementos.ItensDaLoja.produtos import Produto

answareEmpresas = requests.get('aqui entra a url da API com os dados de cadastro das empresas')
answareProdutos = requests.get('aqui entra a url da API com os dados de cadastro dos produtos')
if answareEmpresas.status_code == 200 and answareProdutos.status_code == 200:
    print(f'Your request has been complete')
    Empresas = {}
    for empresa in answareEmpresas.json():
        NovaEmpresa = Empresa(
            nome=empresa['nome'],
            dono1=empresa['dono1'],
            dono2=empresa['dono2'],
            id=empresa['id']
        )
        Empresas[NovaEmpresa._id] = NovaEmpresa


    for produto in answareProdutos.json():
        NovoProduto = Produto(
            nome=produto['nome'],
            descricao=produto['descricao'],
            preco=produto['preco'],
            id =produto['id'],
            id_da_empresa=produto['id_da_empresa']
        )

        Empresas[NovoProduto.id_da_empresa].adicionar_produto(NovoProduto)

else:
    print(f'your request for Empresas failed with statuts code: {answareEmpresas.status_code}')
    print(f'your request for Produtos failed with statuts code: {answareProdutos.status_code}')

