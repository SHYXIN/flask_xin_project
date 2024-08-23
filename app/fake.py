from random import randint
from sqlalchemy.exc import IntegrityError
from faker import Faker
from . import db
from .models import User, Post, Role

def users(admin=2, moderator=2, user=20):
    # fake = Faker()
    Role.insert_roles()
    roles = Role.query.all()[::-1]
    fake = Faker('zh_CN')
    last_fake_info = {'confirmed': True, 'location':fake.city(), 'about_me':fake.text(),  'member_since':fake.past_date()}
    admin_info = {'email': 'admin@qq.com', 'username': 'admin', 'password': 'admin',  'name':'王鑫'}
    admin_info = dict(**admin_info, **last_fake_info)
    u = User(**admin_info)
    u.role = roles[0]
    db.session.add(u)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
    roles_name = ['管理员', '编辑', '普通用户']
    role_email = ['admin', 'moderator', 'user']

    def create_user(role_id, count):
        for i in range(1, count+1):
            u = User(
                    # email=fake.email(),
                    email=f'{role_email[role_id]}_{i}@qq.com',
                    #  username=fake.user_name(),
                    username=f'{role_email[role_id]}_{i}',
                    password=f'{role_email[role_id]}',
                    confirmed=True,
                    name=fake.name(),
                    location=fake.city(),
                    about_me=fake.text(),
                    member_since=fake.past_date())
            u.role = roles[role_id]
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
    create_user(0, admin)
    create_user(1, moderator)
    create_user(2, user)


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
