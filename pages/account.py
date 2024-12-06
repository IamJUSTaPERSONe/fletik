import flet as ft
from flet_route import Params, Basket

class AccPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Аккаунт'
        page.window.width = 1300
        page.window.height = 800
        page.window.min_width = 900
        page.window.min_height = 600


        return ft.View(
            '/acc',
            controls=[
                ft.ElevatedButton('На главную', icon='ARROW_BACK_IOS', on_click=lambda e: page.go('/main_page')),
                ft.Text('Тут будет инфа об аккаунту', color='white')

            ], bgcolor='#111014', padding=0
        )