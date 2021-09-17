def sede_bancaria(cola_general):

 
    cola_caja, cola_info, suma_retiros, suma_consignaciones= [ ], [ ], 0, 0

    
    edades_retiro, edades_info, edades_consig = [ ], [ ], [ ]
    
     
    for i in cola_general:  
        
        if i.fila_interes == 'caja':  
            cola_caja.append(i.nombre)  
        if i.fila_interes == 'info':  
            cola_info.append(i.nombre)  
            edades_info.append(i.edad)  
        if i.transaccion == 'consignar':  
            suma_consignaciones += i.cantidad_consignar  
            edades_consig.append(i.edad)  
        if i.transaccion == 'retirar': 
            suma_retiros += i.cantidad_retirar  
            edades_ '''complete acá'''.append(i.edad)  
            
     
    for i in edades_retiro, edades_info, edades_consig:  
        if i == []:  
            i.append(-1)  
    edad_minima_retiro, edad_minima_info, edad_minima_consignacion = min(edades_retiro), min(edades_info), min(edades_consig)  
    
    return cola_caja, cola_info, suma_retiros, suma_consignaciones, edad_minima_retiro, edad_minima_info, edad_minima_consignacion 
