import flet as ft
from flet_route import Params, Basket
from database import connect_db


class EditNotePage:

    error = ft.Text(' ', color='red')

    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Создание заметки'

        id_note = params.get('id_note')


        def edit_note_page(e):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute('SELECT title_note, text_note FROM notes WHERE id_note = ?',
                        (id_note,))
            note = cur.fetchall()
            conn.close()

            if note:
                title_input.value = note[0]  # Заголовок заметки
                text_input.value = note[1]  # Текст заметки
            else:
                print('something wrong')

        # def save_note(note_id, title_note, text_note):
        #     conn = connect_db()
        #     cur = conn.cursor()
        #     cur.execute('UPDATE notes SET title_note = ?, text_note = ? WHERE id_note = ?',
        #                 (note_id, title_note, text_note))
        #     conn.commit()
        #     conn.close()

        def delete_note():
            pass



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
        save_btn = ft.ElevatedButton('Сохранить', style=style_save, height=50)
        delete_btn = ft.ElevatedButton('Удалить', style=style_save, height=50, on_click=delete_note)
        back_btn = ft.ElevatedButton('На главную', icon='ARROW_BACK_IOS', icon_color='red80',
                                     style=style_back, on_click=lambda e: page.go('/main_page'))

        edit_note_page(id_note)
        return ft.View(
            '/edit_note',
            controls=[
                ft.Column(
                    controls=[
                        back_btn,
                        title_input,
                        text_input,
                        save_btn,
                        delete_btn,
                        self.error,
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ], bgcolor='#111014', padding=15
        )