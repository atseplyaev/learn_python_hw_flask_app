from getpass import getpass
import sys

from webapp import create_app
from webapp.model import db, User

app = create_app()

with app.app_context():
    username = input("Введите имя пользователя: ")

    if User.query.filter(User.username == username).count():
        print("Такой пользователь уже существует")
        sys.exit(0)

    password = getpass(prompt='Введите пароль: ')
    repeat_password = getpass("Повторите пароль: ")

    if not password == repeat_password:
        print("Пароли не совпадают")
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print("User with id {} added".format(new_user.id))