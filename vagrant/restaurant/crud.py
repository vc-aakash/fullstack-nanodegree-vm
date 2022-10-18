from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# CREATE

# myFirstRestaurant = Restaurant(name = "Pizza Palace")
# session.add(myFirstRestaurant)
# session.commit()
# print(session.query(Restaurant).all())

# cheesePizza = MenuItem(name = "Cheese Pizza",
#                         description = "Made with all natural ingredients and fresh mozzarella",
#                         course = "Entree",
#                         price = "$8.99",
#                         restaurant = myFirstRestaurant)
# session.add(cheesePizza)
# session.commit()
# print(session.query(MenuItem).all())



# READ

# firstResult = session.query(Restaurant).first()
# print(firstResult.name)

# items = session.query(MenuItem).all()
# for item in items:
#     print(item.name)



# UPDATE

# veggieBurgers  = session.query(MenuItem).filter_by(name = 'Veggie Burger')
# for veggieBurger in veggieBurgers:
#     print(veggieBurger.id)
#     print(veggieBurger.price)
#     print(veggieBurger.restaurant.name)
#     print('\n')

# urbanVeggieBurger = session.query(MenuItem).filter_by(id = 2).one()
# urbanVeggieBurger.price = '$2.99'
# session.add(urbanVeggieBurger)
# session.commit()

# for veggieBurger in veggieBurgers:
#     if veggieBurger.price != '$2.99':
#         veggieBurger.price = '$2.99'
#         session.add(veggieBurger)
#         session.commit()

# for veggieBurger in veggieBurgers:
#     print(veggieBurger.id)
#     print(veggieBurger.price)
#     print(veggieBurger.restaurant.name)
#     print('\n')



# DELETE

# spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
# print(spinach.restaurant.name)
# session.delete(spinach)
# session.commit()