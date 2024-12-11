from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, name):
        names = [author.name for author in Author.query.all()]
        if name == '':
            raise ValueError("name is invalid")
        elif name in names:
            raise ValueError("no")
        return name
    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        phone_numbers = [author.phone_number for author in Author.query.all()]
        num = int(phone_number)
        if len(phone_number) != 10:
            raise ValueError("no")
        elif type(num) is not int:
            raise ValueError("no")
        return phone_number
    

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validates_title(self, key, title):
        if title == '':
            raise ValueError("no")
        elif "Won't Believe" in title:
            return title
        elif "Secret" in title:
            return title
        elif "Top" in title:
            return title
        elif "Guess" in title:
            return title
        else:
            raise ValueError("no")
    
    @validates('content')
    def validates_content_length(self, key, content):
        if len(content) < 250:
            raise ValueError("no")
        return content
    
    @validates('summary')
    def validates_summary_length(self, key, summary):
        if len(summary) > 250:
            raise ValueError("no")
        return summary
    
    @validates('category')
    def validates_category(self, key, category):
        if 'Fiction' not in category:
            raise ValueError("no")

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
