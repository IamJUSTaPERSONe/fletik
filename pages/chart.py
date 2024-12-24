import flet as ft
import matplotlib.pyplot as plt
import numpy as np
from database import connect_db
from flet_route import Params, Basket
import sqlite3


class ChartPage:
    def view(self, page: ft.Page, params: Params, basket: Basket):
        page.title = 'График'
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
                    ft.CircleAvatar(
                        foreground_image_src='https://avatars.mds.yandex.net/i?id=e17a4e0b861858d4c57dd34d0de833d868b5fea3-4078555-images-thumbs&n=13',
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
                    ft.TextButton('Главная', icon='space_dashboard_rounded', style=style_menu,
                                  on_click=lambda e: page.go('/main_page')),
                    ft.TextButton('Аккаунт', icon='ACCOUNT_CIRCLE', style=style_menu,
                                  on_click=lambda e: page.go('/acc')),
                    ft.TextButton('Настройки', icon='SETTINGS', style=style_menu,
                                  on_click=lambda e: page.go('/settings')),
                    ft.TextButton('График', icon='BUBBLE_CHART_ROUNDED', style=style_menu,
                                  on_click=lambda e: page.go('/chart')),
                    ft.Container(height=300),
                    ft.TextButton('Выход', icon='EXIT_TO_APP_SHARP', style=style_menu,
                                  on_click=lambda e: page.go('/'))
                ], spacing=20,
            )
        )

        def get_notes_count_by_day():
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT DATE(date_created) AS date, COUNT(*) AS count FROM notes GROUP BY DATE(date_created)")
            data = cursor.fetchall()
            conn.close()

            return data

        # Функция для получения общего количества заметок
        def get_total_notes_count():
            conn = sqlite3.connect('notes_app.db')
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM notes")
            total_count = cursor.fetchone()[0]
            conn.close()

            return total_count

        # Функция для построения графика
        def plot_notes_statistics():
            # Получаем данные
            notes_data = get_notes_count_by_day()
            total_count = get_total_notes_count()

            # Подготовка данных для графика
            if notes_data:
                dates = [row[0] for row in notes_data]
                counts = [row[1] for row in notes_data]

                # Построение графика
                plt.figure(figsize=(10, 5))
                plt.bar(dates, counts, color='#9B5CFF')
                plt.xlabel('Дата')
                plt.ylabel('Количество заметок')
                plt.title('Количество созданных заметок по дням')
                plt.xticks(rotation=45)
                plt.tight_layout()
                average_per_day = np.mean(counts) if counts else 0

                # Вывод дополнительной информации на график
                plt.figtext(1.0, 0.01, f"Общее количество заметок: {total_count}", horizontalalignment='right',
                            fontsize=10)
                plt.figtext(1.0, 0.04, f"Среднее количество заметок в день: {average_per_day:.2f}",
                            horizontalalignment='right', fontsize=10)
                plt.show()
            else:
                print('Нет данных')

        plot_notes_statistics()


        return ft.View(
            '/chart',
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Container(
                            expand=1,
                            content=ft.Column(
                                controls=[
                                    logotip,
                                    sidebar
                                ]
                            ), bgcolor='#22242B'

                        ),
                        ft.Container(
                            expand=4,
                            content=ft.Column(
                                controls=[

                                ]
                            ), padding=20
                        )
                    ]
                )
            ], bgcolor='#111014', padding=0
        )

