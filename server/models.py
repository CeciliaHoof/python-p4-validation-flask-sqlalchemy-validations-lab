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

    # Add validators
    @validates('name')
    def validate_name(self, key, name):
        existing_author = Author.query.filter(Author.name == name).first()

        if not name:
            raise ValueError('Authors must have a name!')

        if existing_author:
            raise ValueError('Author names must be unique')

        return name

    @validates('phone_number')
    def validate_phone_num(self, key, num):
        if len(num) != 10 or not num.isdigit():
            raise ValueError('phone number must be 10 digits long')
        return num
    
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

    # Add validators  
    @validates('title')
    def validate_title(self, key, value):
        clickbait = ["Won't Believe", "Secret", "Top", "Guess"]
        if not value:
            raise ValueError('')
        
        if not any(word in value for word in clickbait):
            raise ValueError('')
            
        return value
    
    @validates('content')
    def validate_content(self, key, value):
        if len(value) < 250:
            raise ValueError('')
        return value
    
    @validates('summary')
    def validate_summary(self, key, value):
        if len(value) > 250:
            raise ValueError('')
        return value
    
    @validates('category')
    def validates_category(self, key, value):
        categories = ['Fiction', 'Non-Fiction']
        if value not in categories:
            raise ValueError('')
        return value

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
