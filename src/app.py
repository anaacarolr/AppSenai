import flet
from flet import ThemeMode, Text, TextField, Button, Column, CrossAxisAlignment, OutlinedButton
from flet.controls.border_radius import horizontal


def main(page: flet.Page):
    #configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.LIGHT # Ou ThemeMode.Dark
    page.window.width = 400
    page.window.height = 700

    #funções
    def salvar_nome():
        text.value = f'Bom dia , {input_nome.value} {input_sobrenome.value}'


    #componentes
    text = Text()
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="sobrenome")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)

    #Construção de tela

    page.add(
        Column([
            input_nome,
            input_sobrenome,
            btn_salvar,
            text
        ],
        width=400,
        horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )

flet.run(main)

