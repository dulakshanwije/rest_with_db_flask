from app import db,app

with app.app_context():
    db.create_all()

'''
The db.create_all() function does not recreate or update a table if it already exists. For example, if you modify your model by adding a new column, and run the db.create_all() function, the change you make to the model will not be applied to the table if the table already exists in the database. The solution is to delete all existing database tables with the db.drop_all() function and then recreate them with the db.create_all() function like so:

db.drop_all()
db.create_all()

This will apply the modifications you make to your models, but will also delete all the existing data in the database. To update the database and preserve existing data, you’ll need to use schema migration, which allows you to modify your tables and preserve data. You can use the Flask-Migrate extension to perform SQLAlchemy schema migrations through the Flask command-line interface.
'''