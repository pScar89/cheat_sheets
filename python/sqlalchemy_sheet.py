# SQLAlchemy Cheat Sheet

# INSTALLATION
# pip install sqlalchemy

# IMPORTS
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# DATABASE CONNECTION
# SQLite
engine = create_engine("sqlite:///example.db")
# PostgreSQL
# engine = create_engine('postgresql://user:password@localhost/dbname')

Base = declarative_base()


# MODEL DEFINITION
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    # Relationship
    addresses = relationship("Address", back_populates="user")


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    # Relationship
    user = relationship("User", back_populates="addresses")


# CREATE TABLES
Base.metadata.create_all(engine)

# SESSION SETUP
Session = sessionmaker(bind=engine)
session = Session()

# INSERT DATA
new_user = User(name="John", age=30)
session.add(new_user)
session.commit()

# INSERT MULTIPLE RECORDS
session.add_all([User(name="Alice", age=25), User(name="Bob", age=20)])
session.commit()

# QUERY DATA
users = session.query(User).all()  # Retrieves all users

# FILTER RESULTS
user_john = session.query(User).filter_by(name="John").first()

# UPDATE DATA
user_john.age = 31
session.commit()

# DELETE DATA
session.delete(user_john)
session.commit()

# JOIN QUERIES
users_with_addresses = (
    session.query(User)
    .join(Address)
    .filter(Address.email_address == "example@email.com")
    .all()
)

# ROLLBACK
# In case of an error
session.rollback()

# CLOSE SESSION
session.close()

# TIPS
# - Use sessions to interact with the database.
# - Always close the session after use.
# - Use filter_by for simple queries, and filter for more complex ones.
# - Be aware of the lazy loading and eager loading concepts.
# - Regularly backup your database.
