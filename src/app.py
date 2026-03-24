import flet
from flet import ThemeMode, Text, TextField, Button, Column, CrossAxisAlignment, OutlinedButton, ElevatedButton
from flet.controls.border_radius import horizontal
from flet.controls.material import button


def main(page: flet.Page):
    #configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.LIGHT # Ou ThemeMode.Dark
    page.window.width = 400
    page.window.height = 700

    #funções
    def salvar_nome():
        text.value = f'Bom dia , {input_nome.value} {input_sobrenome.value}'

    def vericar_parimpar():
        numero = int(input_numero.value)
        if numero % 2 == 0:
            text_parimpar.value = f'O {numero} é par'
        else:
            text_parimpar.value = f'O {numero} é impar'



    #componentes
    text = Text()
    text_parimpar = Text()
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="sobrenome")
    input_numero= TextField(label="Digite um numero")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)
    btn_verificar = ElevatedButton("Verificar", on_click=vericar_parimpar)



    #Construção de tela

    page.add(
        Column([
            input_nome,
            input_sobrenome,
            btn_salvar,
            text,
            input_numero,
            text_parimpar,
            btn_verificar
        ],
        width=400,
        horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )

flet.run(main)

