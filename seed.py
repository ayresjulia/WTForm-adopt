from models import db, Pet
from app import app

db.drop_all()
db.create_all()

DEFAULT_PET_PHOTO = 'https://thecontemporarypet.com/wp-content/themes/contemporarypet/images/default.png'

rosie = Pet(name='Rosie', species='dog', photo_url='https://thehappypuppysite.com/wp-content/uploads/2015/09/The-Siberian-Husky-HP-long.jpg',
            age=1, notes='very loving and kind', available=True)
pinot = Pet(name='Pinot', species='hamster', photo_url='https://cf-s3.petcoach.co/uploads/noslidesarticleimages/3c82064afebdba6cebf4692b94d87a37.jpg',
            age=3, notes='eats all the time', available=True)
archie = Pet(name='Archie', species='cat', photo_url='https://geniusvets.s3.amazonaws.com/gv-cat-breeds/Exotic-Shorthair-1.jpg',
             age=2, notes='loves snow', available=True)

db.session.add_all([rosie, pinot, archie])

db.session.commit()
