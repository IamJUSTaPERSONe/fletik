import sqlite3
import time
import flet as ft
from flet_route import Params, Basket
from database import connect_db


class CreateNotePage:

    error = ft.Text(' ', color='red')

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Создание заметки'

        def save_note(user_id, title_note, text_note):
            conn = connect_db()  # Подключение к БД
            cur = conn.cursor()  # Подключение курсора
            cur.execute('INSERT INTO notes (user_id, title_note, text_note) VALUES (?, ?, ?)',
                        (user_id, title_note, text_note))  # Запрос к БД
            conn.commit()  # Фиксация изменений
            conn.close()  # Закрытие соединения

        def submit_note(e):
            title_note = title_input.value
            text_note = text_input.value
            user_id = 1
            if title_note and text_note:
                save_note(user_id, title_note, text_note)
                title_input.value = ''
                text_input.value = ''
                save_btn.text = 'Сохранено'
                page.update()
                time.sleep(3)
                page.go('/main_page')
            else:
                self.error.value = 'Заполните все поля'
                self.error.size = 15
                self.error.update()
                time.sleep(2)
                self.error.size = 0
                self.error.update()

        style_save = ft.ButtonStyle(color={ft.ControlState.HOVERED: '#9B5CFF',
                                           ft.ControlState.DEFAULT: ft.colors.WHITE},
                                    overlay_color='white20', shadow_color='black')
        style_back = ft.ButtonStyle(color={ft.ControlState.HOVERED: '#9B5CFF',
                                           ft.ControlState.DEFAULT: ft.colors.WHITE},
                                    overlay_color='white20', shadow_color='black')

        title_input = ft.TextField(label='Заголовок', width=500, border_radius=15,
                                   bgcolor='#22242B', color='#E6D6FF')
        text_input = ft.TextField(label='Текст заметки', expand=True, border_radius=15,
                                  bgcolor='#22242B', color='#E6D6FF')
        save_btn = ft.ElevatedButton('Сохранить', style=style_save, height=50, on_click=submit_note)
        back_btn = ft.ElevatedButton('На главную',icon='ARROW_BACK_IOS', icon_color='red80',
                                     style=style_back, on_click=lambda e: page.go('/main_page'))
        return ft.View(
            '/create_note',
            controls=[
                ft.Column(
                    controls=[
                        back_btn,
                        title_input,
                        text_input,
                        save_btn,
                        self.error,
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ], bgcolor='#111014', padding=15
        )

