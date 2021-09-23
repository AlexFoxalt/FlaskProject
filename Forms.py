from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

error_text_INVALID_EMAIL = 'Некорректный email'
error_text_PSW_LENGTH = 'Длина пароля должна быть от 4 до 100 символов'
error_text_NAME_LENGTH = 'Длина имени должна быть от 4 до 100 символов'
error_text_PSW_NOT_EQUAL = 'Пароли должны совпадать'


class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(),
                                               Email(error_text_INVALID_EMAIL)])
    psw = PasswordField('Пароль: ', validators=[DataRequired(),
                                                Length(min=4, max=100, message=error_text_PSW_LENGTH)])
    remember = BooleanField('Запомнить', default=False)
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    name = StringField('Имя: ', validators=[DataRequired(),
                                            Length(min=4, max=100, message=error_text_NAME_LENGTH)])
    email = StringField('Email: ', validators=[DataRequired(),
                                               Email(error_text_INVALID_EMAIL)])
    psw = PasswordField('Пароль: ', validators=[DataRequired(),
                                                Length(min=4, max=100, message=error_text_PSW_LENGTH)])
    psw2 = PasswordField('Пароль: ', validators=[DataRequired(),
                                                 Length(min=4, max=100, message=error_text_PSW_LENGTH),
                                                 EqualTo('psw', message=error_text_PSW_NOT_EQUAL)])
    submit = SubmitField('Регистрация')
