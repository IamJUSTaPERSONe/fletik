import flet as ft
from flet_route import Params, Basket


class CreateNotePage:

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Создание заметки'


        def save_note(e):
            title_note = title_input.value
            body_note = body_input.value
            page.session.set('title_note', title_note)
            print(title_note, body_note)
            page.update()
            page.go('/main_page')

        title_input = ft.TextField(label='Заголовок', width=400)
        body_input = ft.TextField(label='Текст заметки', expand=True)
        save_btn = ft.ElevatedButton('Сохранить', on_click=save_note)

        return ft.View(
            '/create_note',
            controls=[
                ft.Column(
                    controls=[
                        title_input,
                        body_input,
                        save_btn
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )
