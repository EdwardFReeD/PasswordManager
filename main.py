

class Manager(object):

    def lenght_check(self, lenght ):
        """Функция проверки длинны пароля"""
        lenght = int(lenght) # преобразование в int
        if lenght < 6:
            return ('Пароль должен быть длиннее 6 символов!')
        elif lenght > 50:
            return ('Длинна пароля не может привышать 50 символов!')
        else:
            return lenght

    def create_password(self):
        """Функция создания пароля"""
        import random
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

        name = input('Укажите user_name: ')
        lenght = input('Укажите длинну пароля: ')
        lenght = int(lenght)

        # Вызов функции lenght_check
        password_lenght = self.lenght_check(lenght)

        # Проверка ответа функции lenght_check
        if lenght != password_lenght:
            return password_lenght

        # Создание пароля
        password = ''
        while len(password) < lenght:
            password += (random.choice(letters))

        Config().updateConfig(name,password,'password.ini')

        return password


    def registration(self):
        """Функция регистрации"""
        user_name = input('Введите логин: ')
        user_password = input('Введите пароль: ')
        password_check = input('Введите пароль повторно: ')

        if user_password != password_check:
            return ('Пароли не совпадают!')
        password = HashManager().createHash(user_password)
        Config().updateConfig(user_name, password, 'user.ini', )
        return ('Регистрация прошла успешно!')

    def authorization(self):
        """Функция авторизации"""
        user_name = input('Введите логин: ')
        user_password = input('Введите пароль: ')
        user_password = HashManager().createHash(user_password)
        password_ini = Config().readConfig(user_name,'user.ini')

        if password_ini == None:
            return ('Не верное сочитаение логина и пароля.\nПовторите попытку!')
        elif password_ini != user_password:
            return ('Не верное сочитаение логина и пароля.\nПовторите попытку!')
        else:
            return ('Авторизация прошла успешно!')

    def password_seartch(self):
        application = input('Введите user_name: ')
        password = Config().readConfig(application, 'password.ini')
        return password

class Config(object):
    """Класс для работы с файлом конфигурации"""
    def createConfig(self, user_name, user_password):
        """Создании файла"""
        try:
            import configparser
        except ImportError:
            import ConfigParser as configparser
        """
        Create a config file
        """
        config = configparser.ConfigParser()
        config.add_section('User')
        config.set('User', user_name, user_password)


        with open('user.ini', "w") as config_file:
            config.write(config_file)

    def updateConfig(self, user_name, user_password,file):
        """Обновление данных"""
        try:
            import configparser
        except ImportError:
            import ConfigParser as configparser

        config = configparser.ConfigParser()
        config.read(file)
        config.set('User', user_name, user_password)


        with open(file, "w") as config_file:
            config.write(config_file)

        return ('Обновления произведены')


    def readConfig(self,user_name,file):
        """Чтение данных из конфига"""
        try:
            import configparser
        except ImportError:
            import ConfigParser as configparser

        config = configparser.ConfigParser()
        config.read(file)

        user_password = config.get("User", user_name)

        return user_password

class HashManager (object):

    def createHash(self, password):
        import hmac, hashlib
        result = hmac.new(bytearray('supersupport','utf-8'),
                          bytearray(password,'utf-8'),
                          hashlib.sha256).hexdigest()

        return result


print(Manager().registration())
print('==========================')
print(Manager().authorization())
print('==========================')
print(Manager().create_password())
print('==========================')
print(Manager().password_seartch())
