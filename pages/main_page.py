import flet as ft
from flet_route import Params, Basket

class MainPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Main page'
        return ft.View(
            '/main_page',
            controls=[
                ft.Text('Hello, note app')
                ]
        )


