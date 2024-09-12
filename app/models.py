from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Column, ForeignKey, Table
from sqlalchemy.types import Integer, String, Float, Enum
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

order_details = Table(
    "order_details",
    db.Model.metadata,
    Column("menu_item_id", ForeignKey("menu_items.id"), primary_key=True),
    Column("order_id", ForeignKey("orders.id"), primary_key=True)
)

class Employee(db.Model, UserMixin):
    __tablename__ = 'employees'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(100), nullable=False)
    employee_number = Column('employee_number', Integer, nullable=False, unique=True)
    hashed_password = Column('hashed_password', String(255), nullable=False)

    @property
    def password(self):
        return self.hashed_password
    
    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    

class Menu(db.Model):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

    menu_items = relationship("MenuItem", back_populates="menu")


class MenuItem(db.Model):
    __tablename__ = 'menu_items'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    menu_id = Column(Integer, ForeignKey('menus.id'), nullable=False)
    menu_type_id = Column(Integer, ForeignKey('menu_item_types.id'), nullable=False)

    type = relationship("MenuItemType", back_populates="menu_items")
    menu = relationship("Menu", back_populates="menu_items")
    orders = relationship("Order",
                          secondary=order_details,
                          back_populates="menu_items")
    

class MenuItemType(db.Model):
    __tablename__ = 'menu_item_types'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

    menu_items = relationship("MenuItem", back_populates="type")


class Table(db.Model):
    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False, unique=True)
    capacity = Column(Integer, nullable=False)


class Order(db.Model):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    table_id = Column(Integer, ForeignKey('tables.id'), nullable=False)
    server_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    price = Column(Integer, nullable=False)
    status = Column(Enum("Active", "Ended"), nullable=False)

    menu_items = relationship("MenuItem",
                              secondary=order_details,
                              back_populates="orders")