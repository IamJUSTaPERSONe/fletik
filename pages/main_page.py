import flet as ft
from flet_route import Params, Basket


class MainPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Main page'
        return ft.View(
            '/main_page',
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Container(
                            expand=2,
                            padding=ft.padding.all(40),
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text('menu'),
                                    ft.Container(
                                        ft.ElevatedButton(text='Аккаунт'),
                                    ),

                                    ft.Container(
                                        ft.Text('Настройки')
                                    )

                                ]
                            )
                        )
                    ]
                )
            ]
        )


