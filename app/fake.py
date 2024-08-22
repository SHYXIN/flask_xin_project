from random import randint
from sqlalchemy.exc import IntegrityError
from faker import Faker
from . import db
from .models import User, Post, Role

def users(count=100):
    # fake = Faker()
    Role.insert_roles()
    roles = Role.query.all()[::-1]
    fake = Faker('zh_CN')
    i = 0
    while i < count:
        u = User(
                # email=fake.email(),
                email=f'wangxin_{i}@qq.com',
                #  username=fake.user_name(),
                 username=f'wangxin_{i}',
                 password='password',
                 confirmed=True,
                 name=fake.name(),
                 location=fake.city(),
                 about_me=fake.text(),
                 member_since=fake.past_date())
        u.role = roles[i % 3]
        db.session.add(u)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()

def posts(count=100):
    # fake = Faker()
    fake = Faker('zh_CN')
    user_count = User.query.count()
    for i in range(count):
        u = User.query.offset(randint(0, user_count - 1)).first()
        p = Post(body=fake.text(),
                 timestamp=fake.past_date(),
                 author=u)
        db.session.add(p)
    db.session.commit()
