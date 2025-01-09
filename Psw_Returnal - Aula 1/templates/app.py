import __init__
from views.view import SubscriptionService
from models.database import engine
from models.model import Subscription
from datetime import datetime
from decimal import Decimal

class UI:
    def __init__(self):
        self.subscription_service = SubscriptionService(engine)


    def start(self):
        while True:
            print('''
            [1] -> Adicionar assinatura
            [2] -> Remover assinatura
            [3] -> Valor total
            [4] -> Gastos últimos 12 meses
            [5] -> Pagar
            [6] -> Sair
            ''')

            choice = int(input('Escolha uma opção: '))

            if choice == 1:
                self.add_subscription()
            elif choice == 2:
                self.delete_subscription()
            elif choice == 3:
                self.total_value()
            elif choice == 4:
                self.subscription_service.gen_chart()
            elif choice == 5:
                self.pay_s()
            else:
                break


    def add_subscription(self):
        empresa = input('Empresa: ')
        site = input('Site: ')
        data_assinatura = datetime.strptime(input('Data de assinatura: '), '%d/%m/%Y')
        valor = Decimal(input('Valor: '))
        
        subscription = Subscription(empresa=empresa, site=site, data_assinatura=data_assinatura, valor=valor)
        self.subscription_service.create(subscription)
        print('Assinatura adicionada com sucesso.')


    def delete_subscription(self):
        subscriptions = self.subscription_service.list_all()
        #todo: Quando excluir a assinatura, excluir todos os pagamentos dela. Inativar.
        print('Escolha qual assinatura deseja excluir')

        for i in subscriptions:
            print(f'[{i.id}] -> {i.empresa}')

        choice = int(input('Escolha a assinatura: '))
        self.subscription_service.delete(choice)
        print('Assinatura excluída com sucesso.')


    def total_value(self):
        print(f'Seu valor total mensal em assinaturas é: {self.subscription_service.total_value()}')


    def pay_s(self):
        subscriptions = self.subscription_service.list_all()

        if not subscriptions:
            print("Nenhuma assinatura encontrada.")
            return

        print("Escolha a assinatura para pagar:")
        for i in subscriptions:
            print(f'[{i.id}] -> {i.empresa}')

        choice = int(input("Escolha a assinatura: "))

        selected_subscription = next((sub for sub in subscriptions if sub.id == choice), None)
        if selected_subscription:
            self.subscription_service.pay(selected_subscription)
            print(f"Pagamento para {selected_subscription.empresa} realizado com sucesso.")
        else:
            print("Assinatura não encontrada.")

UI().start()
