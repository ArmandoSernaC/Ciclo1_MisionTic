def actualizar_estado_editor(operaciones_usuario):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    texto_actual=""
    texto_escrito=[]
    rehacer=[]
    cadena_final=""
    for a in operaciones_usuario:
        if texto_actual== None:
            texto_escrito.append(a)
            texto_actual=a
        if a == "DESHACER" and texto_escrito != []:
            rehacer.append(texto_actual)
            texto_actual=texto_escrito.pop()
        if a == "REHACER" and rehacer != []:
            texto_escrito.append(texto_actual)
            texto_actual=rehacer.pop()
    cadena_final="".join(texto_escrito)
    return cadena_final
