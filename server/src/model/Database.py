from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint, Boolean, create_engine, DATETIME, Double
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship


class Base(DeclarativeBase):
    pass

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True, nullable=False)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    login = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(Integer, ForeignKey('roles.id'), default=0)
    balance = Column(Integer, default=0)


    role_data = relationship("Role", backref="users")
    comments = relationship("Comment", back_populates="user_data")


class Type(Base):
    __tablename__ = 'types'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True, nullable=False)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer)
    fineness = Column(Integer)
    carat = Column(Double)
    type = Column(String, nullable=False)
    material = Column(String, nullable=False)
    color = Column(String, nullable=False)
    size = Column(Integer)
    date = Column(DATETIME)
    popularity = Column(Integer)
    image = Column(String)

class Favor(Base):
    __tablename__ = 'favors'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)





DATABASE_URL = 'sqlite:///../database.db'
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

