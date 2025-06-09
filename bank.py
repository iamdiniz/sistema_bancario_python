class ContaBancaria:
    def __init__(self, limite=500, limite_saques=3):
        self.saldo = 0.0
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
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
        Você possui um saldo de R$ {self.saldo:.2f}
        Digite a opção desejada:

        [d] Depositar
        [s] Sacar
        [e] Extrato
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
                    self.sacar(valor)
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número válido.")

            elif opcao == "e":
                self.mostrar_extrato()

            elif opcao == "q":
                print("Obrigado por utilizar nosso sistema. Volte sempre!")
                break

            else:
                print("Operação inválida. Por favor, selecione uma opção válida.")

if __name__ == "__main__":
    conta = ContaBancaria()
    conta.executar()