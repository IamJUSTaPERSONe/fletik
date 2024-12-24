import flet as ft
from flet_route import Params, Basket


class SettPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Настройки'
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
        # меню -> кнопки
        sidebar = ft.Container(
            padding=ft.padding.symmetric(0, 13),
            content=ft.Column(
                controls=[
                    ft.Text('МЕНЮ', color='grey', size=20),
                    ft.TextButton('Главная', icon='space_dashboard_rounded', style=style_menu,
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

        def switch_to_light(e):
            page.theme_mode = ft.ThemeMode.LIGHT
            page.update()

        def switch_to_dark(e):
            page.theme_mode = ft.ThemeMode.DARK
            page.update()

        text_color = ft.Row(
            controls=[
                ft.Text('Цвет текста:', size=18),
                ft.ElevatedButton(text="dark", color='black', on_click=switch_to_light),
                ft.ElevatedButton(text="white", color='WHITE70', on_click=switch_to_dark)
            ],
        )
        # def update_ava(e):
        #     if e.files:
        #         file_url = e.files[0].url
        #         logotip.content.controls[0].foreground_image_scr = file_url
        #         logotip.update()
        #     page.remove(file)
        #
        # file = ft.FilePicker(on_result=update_ava)
        #
        # def upload_file(e):
        #     page.add(file)
        #     file.pick_files()
        #
        # change_ava_btn = ft.ElevatedButton('Изменить аватарку', on_click=upload_file)

        return ft.View(
            '/settings',
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Container(
                            expand=1,
                            content=ft.Column(
                                controls=[
                                    logotip,
                                    sidebar
                                ]
                            ), bgcolor='#22242B'

                        ),
                        ft.Container(
                            expand=4,
                            content=ft.Column(
                                controls=[
                                    text_color
                                ]
                            ), padding=20
                        )
                    ]
                )
            ], bgcolor='#111014', padding=0
        )

