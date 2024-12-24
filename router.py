import flet as ft
from flet_route import Routing, path
from pages.account import AccPage
from pages.login import LoginPage
from pages.settings import SettPage
from pages.singup import SingupPage
from pages.main_page import MainPage
from pages.createnote import CreateNotePage
from pages.editnote import EditNotePage
from pages.chart import ChartPage


class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.app_routers = [
            path(url=r'/', clear=True, view=MainPage().view),  # view=LoginPage().view
            path(url=r'/singup', clear=True, view=SingupPage().view),
            path(url=r'/main_page', clear=False, view=MainPage().view),
            path(url=r'/acc', clear=False, view=AccPage().view),
            path(url=r'/settings', clear=False, view=SettPage().view),
            path(url=r'/create_note', clear=False, view=CreateNotePage().view),
            path(url=r'/edit_note', clear=False, view=EditNotePage().view),
            path(url=r'/chart', clear=False, view=ChartPage().view)
        ]

        Routing(
            page=self.page,
            app_routes=self.app_routers
        )
        self.page.go(self.page.route)