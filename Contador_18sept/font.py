import time


def cuenta_regresiva(segundos, funcion_actualizar):
    while segundos > 0:
    # 1. Primero declaramos los minutos y segundos sobrantes.
        minutos, seg = divmod(segundos, 60)

    # 2. De los minutos declaramos las horas y minutos sobrantes.
        horas, minutos = divmod(minutos, 60)

        # 3. De las horas declaramos los dias y las horas restantes.
        dias, horas = divmod(horas, 24)

        # 4. Formateamos para que el programa muestre Dias:Horas:Minutos:Segundo.
        tiempo_formateado = f"{dias:02d}:{horas:02d}:{minutos:02d}:{seg:02d}"

# Enviamos el tiempo a la interfaz grafica (False = aun no termina)
        funcion_actualizar(tiempo_formateado, False)
        
        time.sleep(1)
        segundos -= 1
    
    # Enviamos tu mensaje final personalizado (True = ya termino)
        funcion_actualizar("00:00:00:00\nEs el 18 de Septiembre Pariente!!!!!", True)