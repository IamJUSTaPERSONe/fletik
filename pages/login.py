import flet as ft
from flet_route import Params, Basket
from database import connect_db
import sqlite3
import time


class LoginPage:

    error = ft.Text(' ', color='red')

    email_input = ft.Container(
        content=ft.TextField(label='Email',
                             bgcolor='#22242B',
                             border=ft.InputBorder.NONE,
                             filled=True,
                             color='#E6D6FF'),
        border_radius=10
    )

    password_input = ft.Container(
        content=ft.TextField(label='Password',
                             password=True, can_reveal_password=True,
                             bgcolor='#22242B',
                             border=ft.InputBorder.NONE,
                             filled=True,
                             color='#E6D6FF'),
        border_radius=10
    )

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Страница авторизации'
        page.window.width = 1000
        page.window.height = 600
        page.window.min_width = 800
        page.window.min_height = 400

        def auth_user(email, password):
            conn = connect_db()
            cursor = conn.cursor()
            try:
                # Проверяем, существует ли уже email
                cursor.execute('SELECT COUNT(*) FROM users WHERE email = ? AND password = ?', (email, password))
                count = cursor.fetchone()[0]
                if count > 0:
                    # page.go('/main_page')
                    print('Вход выполнен')
                    return True
                else:
                    print('Такой записи нет')

            except sqlite3.Error as e:
                print(f"Ошибка базы данных: {e}")
                return False
            finally:
                conn.close()

        def auth_button(e):
            email_value = self.email_input.content.value
            password_value = self.password_input.content.value
            if email_value and password_value:
                if auth_user(email_value, password_value):
                    print('вход норм')
                    self.error.value = 'Выполняется вход в аккаунт'
                    self.error.size = 12
                    self.error.color = 'green'
                    self.error.update()
                    time.sleep(3)
                    self.error.size = 0
                    page.go('/main_page')

                else:
                    self.error.value = 'Такого аккаунта нет. Зарегестрируйтесь'
                    self.error.size = 12
                    self.error.color = 'red'
                    self.error.update()
                    time.sleep(3)
                    self.error.size = 0
            else:
                self.error.value = 'Заполните все поля'
                self.error.size = 12
                self.error.color = 'red'
                self.error.update()
                time.sleep(3)
                self.error.size = 0

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
                                    ft.Text('Вход',
                                            size=25,
                                            color='#E6D6FF',
                                            weight=ft.FontWeight.NORMAL),

                                    self.email_input,
                                    self.password_input,
                                    self.error,


                                    ft.Container(
                                        ft.Text('Авторизация', color='#E6D6FF'),
                                        alignment=ft.alignment.center, height=40, bgcolor='#9B5CFF',
                                        on_click=lambda e: auth_button(e)
                                    ),
                                    ft.Container(ft.Text('Создать аккаунт', color='#E6D6FF'),
                                                 on_click=lambda e: page.go('/singup'))
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
                                    ft.Icon(name=ft.icons.VERIFIED_USER_ROUNDED,
                                            color='#E6D6FF',
                                            size=140),
                                    ft.Text('Авторизация',
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
    