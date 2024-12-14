import flet as ft
from database import connect_db
from flet_route import Params, Basket


class MainPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'Заметки'
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
                    ft.TextButton('Главная', icon='space_dashboard_rounded',  style=style_menu,
                                  on_click=lambda e: page.go('/main_page')),
                    ft.TextButton('Аккаунт', icon='ACCOUNT_CIRCLE', style=style_menu,
                                  on_click=lambda e: page.go('/acc')),
                    ft.TextButton('Настройки', icon='SETTINGS', style=style_menu,
                                  on_click=lambda e: page.go('/settings')),
                    ft.Container(height=300),
                    ft.TextButton('Выход', icon='EXIT_TO_APP_SHARP', style=style_menu,
                                  on_click=lambda e: page.go('/'))
                ], spacing=20,
            )
        )

        def get_all_notes():
            conn = connect_db()
            cur = conn.cursor()
            cur.execute('SELECT id_note, title_note, text_note, date_created FROM notes')
            notes = cur.fetchall()
            conn.close()
            return notes

        def delete_note(id_note):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute('DELETE FROM notes WHERE id_note = ?', (id_note,))
            conn.commit()
            conn.close()

        def update_notes():
            notes_list.controls.clear()
            notes = get_all_notes()
            for note in notes:
                id_note = note[0]
                title_note = note[1]
                text_note = note[2]
                date_created = note[3]
                note_container = ft.Container(
                    content=ft.Row([
                        ft.Column([
                            ft.Text(date_created, size=10, color='grey'),
                            ft.Text(title_note, size=20),
                            ft.Text(text_note)
                        ]),
                        ft.IconButton(
                            icon=ft.icons.DELETE,  # Иконка для удаления
                            tooltip="Удалить заметку",
                            icon_color='WHITE50',
                            on_click=lambda e, note_id=id_note: delete_note_and_update(note_id)  # Передаем id заметки
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    margin=ft.margin.only(bottom=10),
                    bgcolor='#616161',
                    border_radius=10,
                    padding=ft.padding.all(10),
                    on_click=lambda e,: page.go('/edit_note', id_note)
                )
                notes_list.controls.append(note_container)
            page.update()
                # notes_list.controls.append(ft.Container(
                #     content=ft.Column([
                #         ft.Text(date_created,size=10, color='grey'),
                #         ft.Text(title_note, size=20),
                #         ft.Text(text_note)
                #     ]), margin=ft.margin.only(bottom=10),
                #     bgcolor='#616161',
                #     border_radius=10,
                #     padding=ft.padding.all(10),
                #     on_click=lambda e, : page.go('/edit_note', id_note)
                # ))
            # page.update()

        def delete_note_and_update(note_id):
            delete_note(note_id)  # Удаляем заметку из базы данных
            update_notes()  # Обновляем список заметок

        #  строка поиска
        search = ft.TextField(label=('Найти заметку'), border_radius=20, width=100, expand=1,
                              color='#B02C2F', bgcolor='#22242B')
        search_btn = ft.ElevatedButton('🔎', bgcolor='#22242B',
                                       style=ft.ButtonStyle(text_style=ft.TextStyle(size=20)))

        create_note_button = ft.TextButton(icon='ADD_SHARP', style=ft.ButtonStyle(color='white', icon_size=70),
                                           on_click=lambda e: page.go('/create_note'),)

        notes_list = ft.Column()

        update_notes()
        return ft.View(
            '/main_page',
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Container(
                            expand=1,
                            content=ft.Column(
                                controls=[
                                    logotip,
                                    sidebar,
                                ]
                            ), bgcolor='#22242B'
                        ),
                        ft.Container(
                            expand=4,
                            padding=ft.padding.symmetric(20, 20),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            search,
                                            search_btn,
                                            create_note_button
                                        ]
                                    ),

                                    ft.Container(
                                        content=ft.ListView(
                                                controls=[
                                                    notes_list,
                                                ]
                                            ), expand=True
                                        )
                                ]
                            )
                        )

                    ]
                )

            ], bgcolor='#111014', padding=0
        )



