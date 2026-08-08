import flet as ft
import threading

# Asegúrate de que el archivo font.py siga en la misma carpeta
from font import cuenta_regresiva

def main(page: ft.Page):
    # Diseño de la página web
    page.title = "Cuenta Regresiva 18 de Septiembre"
    
    # Usamos texto directo en lugar de ft.MainAxisAlignment para evitar errores
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.bgcolor = "#263238"  # Color azul oscuro grisáceo

    # Texto que mostrará los números en pantalla
    texto_tiempo = ft.Text(
        value="Calculando...", 
        size=60, 
        color="#80DEEA",  # Color Cyan
        weight="bold",
        text_align="center"
    )
    page.add(texto_tiempo)

    # Función que 'font.py' usará para actualizar la pantalla
    def actualizar_pantalla(texto, terminado):
        texto_tiempo.value = texto
        if terminado:
            # Si terminó, cambiamos a rojo y más grande para celebrar
            texto_tiempo.color = "#EF5350"  # Color Rojo
            texto_tiempo.size = 70
        page.update()

    # Iniciamos tu contador en un hilo separado
    hilo = threading.Thread(
        target=cuenta_regresiva, 
        args=(3567000, actualizar_pantalla)
    )
    hilo.start()

# Lanzamos la aplicación web
ft.app(target=main, view="web_browser")