import flet as ft
from flet_route import Params, Basket
from utils.validations import Validation
from database import connect_db
from utils.function import hash_password
import time
import sqlite3



class SingupPage:
    validation = Validation()

    error = ft.Text(' ', color='red')

    email_input = ft.Container(
        content=ft.TextField(label='Email',
                             bgcolor='#22242B',
                             border=ft.InputBorder.NONE,
                             filled=True,
                             color='#E6D6FF'),
        border_radius=10
    )
    login_input = ft.Container(
        content=ft.TextField(label='Login',
                             bgcolor='#22242B',
                             border=ft.InputBorder.NONE,
                             filled=True,
                             color='#E6D6FF'),
        border_radius=10
    )
    password_input = ft.Container(
        content=ft.TextField(label='Пароль',
                             password=True, can_reveal_password=True,
                             bgcolor='#22242B',
                             border=ft.InputBorder.NONE,
                             filled=True,
                             color='#E6D6FF'),
        border_radius=10
    )
    conf_password_input = ft.Container(
        content=ft.TextField(label='Повторите пароль',
                             password=True, can_reveal_password=True,
                             bgcolor='#22242B',
                             border=ft.InputBorder.NONE,
                             filled=True,
                             color='#E6D6FF'),
        border_radius=10
    )

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Страница регистрации'
        page.window.width = 1000
        page.window.height = 600
        page.window.min_width = 800
        page.window.min_height = 400

        def reg_user(email, login, password):
            conn = connect_db()
            cursor = conn.cursor()
            try:
                # Проверяем, существует ли уже email или login
                cursor.execute('SELECT COUNT(*) FROM users WHERE email = ? OR login = ?', (email, login))
                count = cursor.fetchone()[0]
                if count > 0:
                    print("Такая запись уже существует")
                    return False

                # Если записи нет, добавляем новую
                cursor.execute('INSERT INTO users (email, login, password) VALUES (?, ?, ?)',
                               (email, login, password))
                conn.commit()
                print('Запись добавлена')
                return True
            except sqlite3.Error as e:
                print(f"Ошибка базы данных: {e}")
                return False
            finally:
                conn.close()

        def sing_up_button(e):
            email_value = self.email_input.content.value
            login_value = self.login_input.content.value
            password_value = self.password_input.content.value
            conf_password_value = self.conf_password_input.content.value
            if email_value and login_value and password_value and conf_password_value:
                if not self.validation.is_valid_email(email_value):
                    self.email_input.content.bgcolor = '#1E0245'
                    self.error.value = 'Email не соответствует верному формату'
                    self.error.size = 12
                    self.error.update()
                    self.email_input.update()
                    time.sleep(3)
                    self.error.size = 0
                    self.email_input.content.bgcolor = '#22242B'
                    self.error.update()
                    self.email_input.update()
                elif not self.validation.is_valid_password(password_value):
                    self.password_input.content.bgcolor = '#1E0245'
                    self.error.value = 'Пароль не соответствует формату'
                    self.error.size = 12
                    self.error.update()
                    self.password_input.update()

                    time.sleep(3)
                    self.error.size = 0
                    self.error.update()
                    self.password_input.content.bgcolor = '#22242B'
                    self.password_input.update()
                elif password_value != conf_password_value:
                    self.password_input.content.bgcolor = '#1E0245'
                    self.conf_password_input.content.bgcolor = '#1E0245'
                    self.error.value = 'Пароли не совпадают'
                    self.error.size = 12
                    self.error.update()
                    self.password_input.update()
                    self.conf_password_input.update()

                    time.sleep(3)
                    self.error.size = 0
                    self.error.update()
                    self.password_input.content.bgcolor = '#22242B'
                    self.conf_password_input.content.bgcolor = '#22242B'
                    self.password_input.update()
                    self.conf_password_input.update()
                else:
                    if reg_user(email_value, login_value, hash_password(password_value)):
                        self.error.value = 'Вы успешно зарегестрированы'
                        self.error.size = 12
                        self.error.color = 'green'
                        self.error.update()
                        self.email_input.content.value = ''
                        self.login_input.content.value = ''
                        self.password_input.content.value = ''
                        self.conf_password_input.content.value = ''
                        self.email_input.update()
                        self.login_input.update()
                        self.password_input.update()
                        self.conf_password_input.update()

                        time.sleep(3)
                        self.error.size = 0
                    else:
                        return True


            else:
                self.error.value = 'Заполните все поля'
                self.error.update()

                time.sleep(3)
                self.error.size = 0
                self.error.update()

        return ft.View(
            '/',
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Container(
                            expand=2,
                            padding=ft.padding.all(40),
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text('Регистрация',
                                            size=25,
                                            color='#E6D6FF',
                                            weight=ft.FontWeight.NORMAL),

                                    self.email_input,
                                    self.login_input,
                                    self.password_input,
                                    self.conf_password_input,
                                    self.error,

                                    ft.Container(
                                        ft.Text('Зарегестрироваться', color='#E6D6FF'),
                                        alignment=ft.alignment.center, height=40, bgcolor='#9B5CFF',
                                        on_click=lambda e: sing_up_button(e)
                                    ),
                                    ft.Container(ft.Text('Уже есть аккаунт?', color='#E6D6FF'),
                                                 on_click=lambda e: page.go('/'))
                                ]
                            )
                        ),
                        ft.Container(
                            expand=3,
                            image_src='resours/images/bg1.png',
                            image_fit=ft.ImageFit.COVER,
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Icon(name=ft.icons.LOCK_PERSON_ROUNDED,
                                            color='#E6D6FF',
                                            size=140),
                                    ft.Text('Регистрация',
                                            color='#E6D6FF',
                                            size=30,
                                            weight=ft.FontWeight.BOLD)
                                ]

                            )
                        )
                    ]
                )
            ], bgcolor='#111014', padding=0

        )
