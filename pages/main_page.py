import flet as ft
from flet_route import Params, Basket
from pages.login import LoginPage


class MainPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Заметки'
        page.window.width = 1300
        page.window.height = 800
        page.window.min_width = 900
        page.window.min_height = 600




        # меню -> заголовок
        logotip = ft.Container(
            padding=ft.padding.symmetric(17, 13),
            content=ft.Row(
                controls=[
                    ft.CircleAvatar(foreground_image_src='https://i.pinimg.com/originals/d0/cf/a8/d0cfa8b3f2b9aa687e99cdd88bb82f10.jpg',
                                    width=50, height=40, content=ft.Text('A')),
                    # ft.Image(src='resours/images/logo.png', width=50, height=40, fit=ft.ImageFit.FILL),
                    ft.Text(f'username', expand=True, color='white', size=30)
                ], alignment=ft.MainAxisAlignment.START,
                spacing=5,
                vertical_alignment=ft.MainAxisAlignment.CENTER
            )
        )

        # стиль меню
        style_menu = ft.ButtonStyle(color={ft.ControlState.HOVERED: '#9B5CFF',
                                           ft.ControlState.DEFAULT: ft.colors.WHITE},
                                    icon_size=20,
                                    overlay_color='white20',
                                    shadow_color='black')
        # меню -> кнопки
        sidebar = ft.Container(
            padding=ft.padding.symmetric(0, 13),
            content=ft.Column(
                controls=[
                    ft.Text('МЕНЮ', color='grey', size=20),
                    ft.TextButton('Главная', width=100, icon='space_dashboard_rounded', style=style_menu),
                    ft.TextButton('Аккаунт', icon='ACCOUNT_CIRCLE', style=style_menu),
                    ft.TextButton('Настройки', icon='SETTINGS', style=style_menu),

                ]
            )
        )

        #  строка поиска
        def search_form(label):
            return ft.TextField(label=f'{label}', bgcolor='#22242B',
                                border=ft.InputBorder.NONE, filled=True, color='#E6D6FF')

        search = ft.Container(content=search_form('Найти заметку'), border_radius=20)
        search_btn = ft.ElevatedButton('🔎', bgcolor='#22242B')

        return ft.View(
            '/main_page',
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
                            padding=ft.padding.symmetric(10,20),
                            content=ft.Column(
                                controls=[
                                    search,
                                    search_btn
                                ]

                            )
                        )
                    ]
                )

            ], bgcolor='#111014', padding=0
        )

