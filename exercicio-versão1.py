''''
Faca um programa para calcular os valores de um pedido
para isso crie um objeto dict de pedido que tenha relacao com um objeto dict de cliente

pedido = {
    "id": 1,
    "cliente": {
        "nome": "Walter"
    },
    "itens": []
}

nesse pedido, coloque uma propriedade de itens, contendo instancias de um dict de produto
no pedido, crie uma função para calcular o valor total
e uma função para mostrar um relatório do pedido, mostrando da seguinte forma:
----------------------------------------------------------------
Pedido Id: 1
Nome: João
Valor Total: R$ 999,99
----------------------------------------------------------------
O que terá no dict de pedido:
- id
- cliente
- itens []
O que terá no dict cliente:
- Nome
- email
O que terá no dict produto:
- Nome
- descrição
- preço
'''

pedidos = {
    "id": 1,
    "cliente": {
        "nome": "Joelmir R. Carvalho",
        "email": "jodeveloper@gmail.com"
    },
    "itens": [{
        "nome": "Notebook",
        "descricao": "1. Leitor de cartão SD (SD, SDHC, SDXC)  2. Porta USB 2.0 de 1ª Ger.  3. Slot de trava de segurança Wedge  4. Energia  5. HDMI 1.4  6. RJ45  7. USB 3.2 Gen 1  8. USB 3.2 Gen 1  9. Entrada de áudio",
        "preco": 4099.50
    }, {
        "nome": "Tablet Samsung Galaxy A7 Lite Wi-Fi 64GB 4GB RAM SM-T220NZAUZTO",
        "descricao": "O Samsung Galaxy Tab A7 Lite possui tela imersiva 8.7. Auto Hotspot, tela de alta resolução, câmera Traseira 8MP, câmera frontal de 2MP e Android 11. Design super portátil, com visual moderno e ótimo acabamento. Equipado com bateria de Longa duração Ions de Lítio.",
        "preco": 1185.00
    }, {
        "nome": "iPhone 11 Apple (64GB) Branco Tela 6,1 4G Câmera 12MP iOS",
        "descricao": "",
        "preco": 3689.00
    }]
}

valor_total = 0

def Calcular_Valor_Total(interator = 0):
    if interator == len(pedidos["itens"]):
        return

    global valor_total
    valor_total += pedidos["itens"][interator]["preco"]
    Calcular_Valor_Total(interator + 1)

Calcular_Valor_Total()
pedidos["valor_total"] = valor_total
print("==================== [RELATÓRIO DE PEDIDOS] ====================")
print(f"Pedido nº: {pedidos['id']}")
print(f"Cliente: {pedidos['cliente']['nome']}")
print("Valor total: {:.2f}".format(pedidos['valor_total']))