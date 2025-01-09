import __init__
from models.database import engine
from models.model import Subscription, Payments
from sqlmodel import Session, select
from datetime import date

class SubscriptionService:
    def __init__(self, engine):
        self.engine = engine

    def create(self, subscription: Subscription):
        with Session(self.engine) as session:
            session.add(subscription)
            session.commit()
            return subscription
        
    def list_all(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            results = session.exec(statement).all()
        return results

    def _has_pay(self, results):
        for result in results:
            if result.date.month == date.today().month:
                return True
        return False

    def pay(self, subscription: Subscription):
        with Session(self.engine) as session:
            statement = select(Payments).join(Subscription).where(Subscription.empresa==subscription.empresa)
            results = session.exec(statement).all()
            if self._has_pay(results):
                question = input('Essa conta já foi paga esse mês, deseja pagar novamente? Y ou N: ')

                if not question.upper() == 'Y':
                    return
            
            pay = Payments(subscription_id=subscription.id, date=date.today())
            session.add(pay)
            session.commit()

    def total_value(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            results = session.exec(statement).all()
            
        total = 0
        for result in results:
            total += result.valor

        return float(total)

ss = SubscriptionService(engine)

print(ss.total_value())

