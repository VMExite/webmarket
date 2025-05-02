from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, sessionmaker


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


class Type(Base):
    __tablename__ = 'types'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True, nullable=False)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    type = Column(String, ForeignKey('types.id'))
    price = Column(Integer, default=0)
    quantity = Column(Integer, default=0)
    rating = Column(Integer, default=0)
    rating_quantity = Column(Integer, default=0)
    views = Column(Integer, default=0)
    pic = Column(String)

    __table_args__ = (
        CheckConstraint('price >= 0', name='check_price_positive'),
        CheckConstraint('quantity >= 0', name='check_quantity_positive'),
        CheckConstraint('rating >= 0', name='check_rating_positive'),
        CheckConstraint('rating_quantity >= 0', name='check_ratingQuantity_positive'),
        CheckConstraint('views >= 0', name='check_views_positive')
    )

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('users.id'))
    product = Column(Integer, ForeignKey('products.id'))
    grade = Column(Boolean, nullable=False)
    text = Column(String)
    likes = Column(Integer, default=0)
    date = Column(String, nullable=False)

    __table_args__ = (
        CheckConstraint('likes >= 0', name='check_likes_positive'),
    )

DATABASE_URL = 'sqlite:///../database.db'
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
