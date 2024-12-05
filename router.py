import flet as ft
from flet_route import Routing, path
from pages.login import LoginPage
from pages.singup import SingupPage
from pages.main_page import MainPage


class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.app_routers = [
            path(url=r'/', clear=True, view=MainPage().view),  # view=LoginPage().view
            path(url=r'/singup', clear=True, view=SingupPage().view),
            path(url=r'/main_page', clear=False, view=MainPage().view)
        ]

        Routing(
            page=self.page,
            app_routes=self.app_routers
        )
        self.page.go(self.page.route)