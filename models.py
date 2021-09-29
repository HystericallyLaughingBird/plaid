from sqlalchemy import Table, Column, String, Date, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import DATE, MONEY, VARCHAR

base = declarative_base()

class Transaction(base):
  __tablename__ = 'Transactions'

  transaction_id = Column(VARCHAR, primary_key=True)
  name = Column(VARCHAR)
  amount = Column(MONEY)
  date = Column(DATE)

  def __init__(self, transaction_id, name, amount, date):
    self.transaction_id = transaction_id
    self.name = name
    self.amount = amount
    self.date = date