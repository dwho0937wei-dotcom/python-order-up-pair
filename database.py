from app.models import Menu, MenuItem, MenuItemType, Table
from dotenv import load_dotenv
load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded
from app import app, db
from app.models import Employee


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    db.session.add(employee)
    db.session.commit()

    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    dinner = Menu(name="Dinner")

    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)

    db.session.add(dinner)
    db.session.commit()

    table1 = Table(number=1, capacity=2)
    table2 = Table(number=2, capacity=2)
    table3 = Table(number=3, capacity=3)
    table4 = Table(number=4, capacity=4)
    table5 = Table(number=5, capacity=6)
    table6 = Table(number=6, capacity=7)
    table7 = Table(number=7, capacity=8)
    table8 = Table(number=8, capacity=10)
    table9 = Table(number=9, capacity=11)
    table10 = Table(number=10, capacity=12)

    for table in [table1, table2, table3, table4, table5, table6, table7, table8, table9, table10]:
        db.session.add(table)
    db.session.commit()