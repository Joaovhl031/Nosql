import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import inspect 
from sqlalchemy import select

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    fullname = Column(String(40))

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(45), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship(
        "User", back_populates="address"
    )

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"
    

print("Criando conexao com banco de dados")
engine = create_engine("sqlite://")

#criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

#depreciando - será removida em futuro release
#print( engine.table_names() )

insp = inspect(engine)

print(insp.has_table("user_account"))

print(insp.get_table_names())
print(insp.default_schema_name)

with Session(engine) as session:
    joao = User(
        name= 'joao',
        fullname= 'joao henrique',
        address=[Address(email_address='joaohenrique@gmail.com')] 
    )

    kawan = User(
        name= 'kawan',
        fullname='kawan de sousa',
        address=[Address(email_address='kawandesousa@gmail.com'),Address(email_address='sousaKawan@gmail.com.br')]
    )

    pedro = User(
        name= 'pedro',
        fullname= 'pedro viana',
    )

    session.add_all([joao, kawan, pedro])

    session.commit()


stmt = select(User).where(User.id.in_([2]))
for user in session.scalars(stmt):
    print(user)

stmt_address= select(Address).where(Address.user_id.in_([3]))
for address in session.scalars(stmt_address):
    print(address)