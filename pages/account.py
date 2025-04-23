import flet as ft
from flet_route import Params, Basket
from database import connect_db


class AccPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Аккаунт'
        page.window.width = 1300
        page.window.height = 800
        page.window.min_width = 900
        page.window.min_height = 600

        login = page.session.get('login_value')
        email = page.session.get('email_value')

        # меню -> заголовок
        logotip = ft.Container(
            padding=ft.padding.symmetric(17, 13),
            content=ft.Row(
                controls=[
                    ft.CircleAvatar(foreground_image_src='https://avatars.mds.yandex.net/i?id=e17a4e0b861858d4c57dd34d0de833d868b5fea3-4078555-images-thumbs&n=13',
                                    width=50, height=40, content=ft.Text('?')),
                    ft.Text(f'{login}', expand=True, color='white', size=30)
                ], alignment=ft.MainAxisAlignment.START,
                spacing=5,
            )
        )

        # стиль меню
        style_menu = ft.ButtonStyle(color={ft.ControlState.HOVERED: '#9B5CFF',
                                           ft.ControlState.DEFAULT: ft.colors.WHITE},
                                    icon_size=25, overlay_color='white20', shadow_color='black')
        style_btn = ft.ButtonStyle(color={ft.ControlState.HOVERED: 'red',
                                           ft.ControlState.DEFAULT: ft.colors.WHITE},
                                    icon_size=25, overlay_color='white20', shadow_color='black')
        # меню -> кнопки
        sidebar = ft.Container(
            padding=ft.padding.symmetric(0, 13),
            content=ft.Column(
                controls=[
                    ft.Text('МЕНЮ', color='grey', size=20),
                    ft.TextButton('ГлавнаЯ', icon='space_dashboard_rounded', style=style_menu,
                                  on_click=lambda e: page.go('/main_page')),
                    ft.TextButton('Аккаунт', icon='ACCOUNT_CIRCLE', style=style_menu,
                                  on_click=lambda e: page.go('/acc')),
                    ft.TextButton('Настройки', icon='SETTINGS', style=style_menu,
                                  on_click=lambda e: page.go('/settings')),
                    ft.TextButton('График', icon='BUBBLE_CHART_ROUNDED', style=style_menu,
                                  on_click=lambda e: page.go('/chart')),
                    ft.Container(height=300),
                    ft.TextButton('Выход', icon='EXIT_TO_APP_SHARP', style=style_menu,
                                  on_click=lambda e: page.go('/'))
                ], spacing=20,
            )
        )

        def close(e):
            page.close(confirmation_dialog)

        def delete_account(email):
            conn = connect_db()  # Подключение к базе данных
            cur = conn.cursor()  # Подключение курсора
            cur.execute('DELETE FROM users WHERE email = ?', (email,))  # Запрос к БД
            conn.commit()  # Фиксация изменений
            conn.close()  # Закрытие соединения
            page.close(confirmation_dialog)
            page.snack_bar = ft.SnackBar(ft.Text('Успешно удалено'))
            page.snack_bar.open = True
            page.update()
            page.go('/')

        confirmation_dialog = ft.AlertDialog(
            title=ft.Text("Подтверждение удаления аккаунта"),
            content=ft.Text("Вы уверены, что хотите удалить аккаунт?"),
            actions=[
                ft.TextButton("Отмена", on_click=close),
                ft.TextButton("Удалить", on_click=lambda e: delete_account(email))
            ],

        )

        name_user = ft.Text(f'Имя пользователя: {login}', size=18)
        email_user = ft.Text(f'Почта: {email} ', size=18)
        delete_acc = ft.ElevatedButton('Удалить аккаунт', icon=ft.icons.LOGIN_SHARP,
                                       style=style_btn, on_click=lambda e: page.open(confirmation_dialog))

        return ft.View(
            '/acc',
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Container(
                            expand=1,
                            content=ft.Column(
                                controls=[
                                    logotip,
                                    sidebar,
                                ]
                            ), bgcolor='#22242B'
                        ),
                        ft.Container(
                            expand=4,
                            content=ft.Column(
                                controls=[
                                    email_user,
                                    name_user,
                                    delete_acc,

                                ]
                            ), padding=20
                        )
                    ]
                )
            ], bgcolor='#111014', padding=0
        )


