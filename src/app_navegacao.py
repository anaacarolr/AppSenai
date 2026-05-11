import flet
from flet import ThemeMode, Text, TextField, Button, Column, CrossAxisAlignment, OutlinedButton, ElevatedButton, \
    TextButton, Container, Colors, FontWeight
from flet.controls.border_radius import horizontal
from flet.controls.material import button
from datetime import datetime


def main(page: flet.Page):
    #configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.LIGHT # Ou ThemeMode.Dark
    page.window.width = 400
    page.window.height = 700

    #Funçoes
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    #Componentes


    #Eventos



