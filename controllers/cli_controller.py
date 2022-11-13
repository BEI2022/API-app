from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.comment import Comment
from models.property_feature import Property, Feature
from datetime import date

db_commands = Blueprint('db', __name__)


@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            name = 'Bei Zhang',
            email = 'bei.zhang@gmail.com',
            password = bcrypt.generate_password_hash('dog').decode('utf-8'),
            is_admin = True
        ),
        User(
            name = 'Good guy',
            email = 'goodguy@gmail.com',
            password = bcrypt.generate_password_hash('goodguy').decode('utf-8'),
            type = 'seller'
        ),
        User(
            name = 'JB',
            email = 'jb@gmail.com',
            password = bcrypt.generate_password_hash('jb').decode('utf-8'),
            type = 'buyer'
        ),
        User(
            name = 'Big W',
            email = 'bigw@gmail.com',
            password = bcrypt.generate_password_hash('bigw').decode('utf-8'),
            type = 'user'
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    properties = [
        Property(
            address = '38 big pig street',
            state = 'QLD',
            postcode = '4000',
            bedrooms ='4',
            bathrooms ='4',
            garages = '2',
            user_id = 1
        ),
        Property(
            address = '109 big monkey street',
            state = 'NSW',
            postcode = '2000',
            bedrooms ='5',
            bathrooms ='2',
            garages = '2',
            user_id = 1
        ),
        Property(
            address = '109 big dog street',
            state = 'VIC',
            postcode = '3000',
            bedrooms ='3',
            bathrooms ='1',
            garages = '2',
            user_id = 1
        ),
        Property(
            address = '109 big cat street',
            state = 'SA',
            postcode = '5000',
            bedrooms ='4',
            bathrooms ='2',
            garages = '2',
            user_id = 1
        ),
    ]

    db.session.add_all(properties)
    db.session.commit()

    comments = [
        Comment(
            message = 'comments 1',
            date = date.today(),
            user_id = 1,
            property_id = 1

        ),
        Comment(
            message = 'comments 2',
            date = date.today(),
            user_id = 1,
            property_id = 1

        ),
        Comment(
            message = 'comments 3',
            date = date.today(),
            user_id = 1,
            property_id = 1

        ),
        Comment(
            message = 'comments 4',
            date = date.today(),
            user_id = 1,
            property_id = 1

        ),
    ]

    db.session.add_all(comments)
    db.session.commit()

    features = [
        Feature(
            name = 'pool',

        ),
        Feature(
            name = 'study room',

        ),
        Feature(
            name = 'media room',

        ),
        Feature(
            name = 'fashion kitchen',

        ),
    ]


    db.session.add_all(features)
    db.session.commit()

 


    print('Tables seeded')