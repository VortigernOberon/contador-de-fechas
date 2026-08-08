import time


def cuenta_regresiva(segundos, funcion_actualizar):
    while segundos > 0:
    # 1. Primero declaramos los minutos y segundos sobrantes.
        minutos, seg = divmod(segundos, 60)

    # 2. De los minutos declaramos las horas y minutos sobrantes.
        horas, minutos = divmod(minutos, 60)

        # 3. De las horas declaramos los días y las horas restantes.
        dias, horas = divmod(horas, 24)

        # 4. Formateamos para que el programa muestre Días:Horas:Minutos:Segundo.
        tiempo_formateado = f"{dias:02d}:{horas:02d}:{minutos:02d}:{seg:02d}"

# Enviamos el tiempo a la interfaz gráfica (False = aún no termina)
        funcion_actualizar(tiempo_formateado, False)
        
        time.sleep(1)
        segundos -= 1
    
    # Enviamos tu mensaje final personalizado (True = ya terminó)
        funcion_actualizar("00:00:00:00\n¡Es el 18 de Septiembre Pariente!!!!!", True)