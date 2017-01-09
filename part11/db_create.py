from app import db
from models import BlogPost


db.create_all()


db.session.add(BlogPost('Good', "I'm very good."))
db.session.add(BlogPost("Well", "I'm very well."))

db.session.commit()