class Loja:
    def __init__(self, descricao, responsavel, custo, status):
        self.descricao = descricao
        self.responsavel = responsavel
        self.custo = custo
        self.status = status

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        if nova_descricao == "":
            raise ValueError("A descrição não pode está vazia")

        self.__descricao = nova_descricao
        print("Dscrição cadastrada/alterada com sucesso")

    @property
    def responsavel(self):
        return self.__responsavel

    @responsavel.setter
    def responsavel(self, novo_responsavel):
        if novo_responsavel == "":
            raise ValueError("O reponsavel não pode está vazio")

        self.__responsavel = novo_responsavel
        print("Responsavel cadastrado/alterado com sucesso")

    @property
    def custo(self):
        return self.__custo

    @custo.setter
    def custo(self, novo_custo):
        if novo_custo < 0:
            raise ValueError("O custo não pode ser negativo")

        self.__custo = novo_custo
        print("Custo cadastrado/alterado com sucesso")

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, novo_status):
        if novo_status != "concluido" and novo_status != "em andamento" and novo_status != "aberto":
            raise ValueError("Status invalido")

        self.__status = novo_status
        print("Status salvo com sucesso")

    def exibir_informacao(self):
        print("\nDescriçao: ", self.descricao)
        print("Reponsavel: ", self.responsavel)
        print("Custo: ", self.custo)
        print("Status: ", self.status)

try:
    produto = Loja("Troca de spoiler", "Ugo", 2000, "concluido")
    produto.exibir_informacao()
except ValueError as erro:
    print("ERRO", erro)

#teste para ver se estão fucionando certinho. Tá ok

print("\nTeste das invalidas")
try:
    produto.descricao = ""
    produto.responsavel = ""
    produto.custo = -2000
    produto.status = "Vai caga"
except ValueError as erro:
    print("ERRO", erro)

print("\nTeste das certas")
try:
    produto.descricao = "Troca de olio"
    produto.responsavel = "Eduardo"
    produto.custo = 78
    produto.status = "em andamento"
    produto.exibir_informacao()
except ValueError as erro:
    print("ERRO", erro)

print("\n2° teste dos certos")
try:
    produto.descricao = "Troca de paralama"
    produto.responsavel = "Lucas"
    produto.custo = 300
    produto.status = "aberto"
    produto.exibir_informacao()
except ValueError as erro:
    print("ERRO", erro)