import sqlalchemy

print(sqlalchemy.__version__)
engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:mypassword@localhost:5432/testdb')
connection = engine.connect()


trans = connection.begin()
try:
    connection.execute("INSERT INTO book(book_id, title, isbn, publisher_id, weight) VALUES (32, 'worst book', 12345, 2, 10)")
    trans.commit()
except:
    trans.rollback()
    raise

# или
with connection.begin() as trans:
    connection.execute("INSERT INTO book(book_id, title, isbn, publisher_id, weight) VALUES (64, 'best book', 12345, 1, 10)")


# можно делать даже так, т.к. под капотом psycopg2
result = connection.execute("SELECT * FROM book")
for row in result:
    print('title', row['title'])
result.close()


# sqlalchemy как ORM
Base = declarative_base()

class Author(Base):
    __tablename__ = ' author'

    author_id = Column(Integer, primary_key=True)
    full_name = Column(String)
    rating = Column(Float)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

author = Author(author_id=18, full_name='Dan brown', rating=4.7)
session.add(author)

session.commit()

for item in session.query(Author).order_by(Author.rating):
    print(item.full_name, ' ', item.rating)

print("Separation")

for item in session.query(Author).filter(Author.rating > 4.5):
    print(item.full_name, ' ', item.rating)