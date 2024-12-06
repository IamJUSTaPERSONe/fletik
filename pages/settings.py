import flet as ft
from flet_route import Params, Basket

class SettPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Настройки'
        page.window.width = 1300
        page.window.height = 800
        page.window.min_width = 900
        page.window.min_height = 600

        return ft.View(
            '/settings',
            controls=[
                ft.ElevatedButton('На главную', icon='ARROW_BACK_IOS', on_click=lambda e: page.go('/main_page')),
                ft.Text('Ремонтные работы', color='white')

            ], bgcolor='#111014', padding=0
        )


