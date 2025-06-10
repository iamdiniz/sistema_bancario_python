class ContaBancaria:
    def __init__(self, limite=500, limite_saques=3):
        self.saldo = 0.0
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0
        self.extrato = []

    def depositar(self, valor, /):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, *, valor):
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif valor > self.saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > self.limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif self.numero_saques >= self.limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            print("Saque realizado com sucesso!")

    def mostrar_extrato(self):
        print("\n========== EXTRATO ==========")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for operacao in self.extrato:
                print(operacao)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("=============================")

    def mostrar_menu(self):
        return f"""
        Digite a opção desejada:

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nu] Novo Usuário
        [nc] Nova Conta
        [lc] Listar Contas
        [q] Sair

        => """

    def executar(self):
        while True:
            opcao = input(self.mostrar_menu()).lower()

            if opcao == "d":
                try:
                    valor = float(input("Informe o valor do depósito: "))
                    self.depositar(valor)
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número válido.")

            elif opcao == "s":
                try:
                    valor = float(input("Informe o valor do saque: "))
                    self.sacar(valor=valor)
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número válido.")

            elif opcao == "e":
                self.mostrar_extrato()

            elif opcao == "nu":
                cadastrar_usuario()

            elif opcao == "nc":
                criar_conta()

            elif opcao == "lc":
                listar_contas()

            elif opcao == "q":
                print("Obrigado por utilizar nosso sistema. Volte sempre!")
                break

            else:
                print("Operação inválida. Por favor, selecione uma opção válida.")

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = ''.join(filter(str.isdigit, cpf))
        self.endereco = endereco

def cadastrar_usuario():
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    cpf = ''.join(filter(str.isdigit, input("CPF (somente números ou com pontuação): ")))
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    if any(u.cpf == cpf for u in usuarios):
        print("Usuário já cadastrado com esse CPF!")
        return
    usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def encontrar_usuario_por_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None

def criar_conta():
    cpf = ''.join(filter(str.isdigit, input("Informe o CPF do usuário: ")))
    usuario = encontrar_usuario_por_cpf(cpf)
    if not usuario:
        print("Usuário não encontrado. Conta não criada.")
        return
    numero_conta = len(contas) + 1
    conta = {
        'agencia': '0001',
        'numero_conta': numero_conta,
        'usuario': usuario
    }
    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: 0001, Número da conta: {numero_conta}")

def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        usuario = conta['usuario']
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {usuario.nome} | CPF: {usuario.cpf}")

if __name__ == "__main__":
    usuarios = []
    contas = []

    conta = ContaBancaria()
    conta.executar()