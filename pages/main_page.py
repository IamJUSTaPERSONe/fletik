import flet as ft
from flet_core.border_radius import vertical
from flet_route import Params, Basket
from pages.login import LoginPage


class MainPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Заметки'
        page.window.width = 1300
        page.window.height = 800
        page.window.min_width = 900
        page.window.min_height = 600

        login = page.session.get('login_value')

        # меню -> заголовок
        logotip = ft.Container(
            padding=ft.padding.symmetric(17, 13),
            content=ft.Row(
                controls=[
                    ft.CircleAvatar(foreground_image_src='https://i.pinimg.com/originals/d0/cf/a8/d0cfa8b3f2b9aa687e99cdd88bb82f10.jpg',
                                    width=50, height=40, content=ft.Text('A')),
                    ft.Text(f'{login}', expand=True, color='white', size=30)
                ], alignment=ft.MainAxisAlignment.START,
                spacing=5,
            )
        )

        # стиль меню
        style_menu = ft.ButtonStyle(color={ft.ControlState.HOVERED: '#9B5CFF',
                                           ft.ControlState.DEFAULT: ft.colors.WHITE},
                                    icon_size=25, overlay_color='white20', shadow_color='black')
        # меню -> кнопки
        sidebar = ft.Container(
            padding=ft.padding.symmetric(0, 13),
            content=ft.Column(
                controls=[
                    ft.Text('МЕНЮ', color='grey', size=20),
                    ft.TextButton('Главная', icon='space_dashboard_rounded',  style=style_menu,
                                  on_click=lambda e: page.go('/main_page')),
                    ft.TextButton('Аккаунт', icon='ACCOUNT_CIRCLE', style=style_menu,
                                  on_click=lambda e: page.go('/acc')),
                    ft.TextButton('Настройки', icon='SETTINGS', style=style_menu,
                                  on_click=lambda e: page.go('/settings')),
                    ft.Container(height=300),
                    ft.TextButton('Выход', icon='EXIT_TO_APP_SHARP', style=style_menu,
                                  on_click=lambda e: page.go('/'))
                ], spacing=20,
            )
        )

        #  строка поиска
        def search_form(label):
            return ft.TextField(label=f'{label}', bgcolor='#22242B',
                                border=ft.InputBorder.NONE, filled=True, color='#E6D6FF')

        search = ft.Container(content=search_form('Найти заметку'), border_radius=20, width=300, expand=2)
        search_btn = ft.ElevatedButton('🔎', bgcolor='#22242B',
                                       style=ft.ButtonStyle(text_style=ft.TextStyle(size=20)))

        folder = ft.Container(
            content=ft.Row(
                controls=[ft.TextButton('folder1'),
                          ft.TextButton('folder2')]
            )
        )

        create_note_button = ft.TextButton(icon='ADD_SHARP', style=ft.ButtonStyle(icon_size=70),
                                           on_click=lambda e: page.go('/create_note'))

        data = page.session.get('title_note')
        print(data)


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
                            padding=ft.padding.symmetric(20,20),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            search,
                                            search_btn,
                                        ]
                                    ),
                                    ft.Row(height=500),
                                    ft.Row(controls=[create_note_button],
                                           spacing=50,
                                           alignment=ft.MainAxisAlignment.END)

                                ]
                            )


                        ),


                    ]
                )

            ], bgcolor='#111014', padding=0
        )


