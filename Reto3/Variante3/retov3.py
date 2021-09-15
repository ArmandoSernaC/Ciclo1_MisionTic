#Forma 1
def cal(bits1, bits2, operacion):
  respuesta = ""
  if operacion == "OR":
    for i in range(len(bits1)):
      if bits1[i]=="1" or bits2[i]=="1":
        respuesta += "1"
      else:
         respuesta += "0"

  elif operacion == "AND":
    for i in range(len(bits1)):
      if bits1[i]=="1" and bits2[i]=="1":
        respuesta += "1"
      else:
         respuesta += "0"

  else: 
    for i in range(len(bits1)):
      if bits1[i] != bits2[i]:
        respuesta += "1"
      else:
         respuesta += "0"
  return respuesta

#--------------------------------------------------------------------------------------------------------------------------------
#Forma 2
def cal2(bits1, bits2, operacion):
  dic= {"0": False, "1": True}
  respuesta = ""
  if operacion == "OR":
    for i in range(len(bits1)):
      if dic[bits1[i]] or dic[bits2[i]]:
        respuesta += "1"
      else:
         respuesta += "0"

  elif operacion == "AND":
    for i in range(len(bits1)):
      if dic[bits1[i]] and dic[bits2[i]]:
        respuesta += "1"
      else:
         respuesta += "0"

  else: 
    for i in range(len(bits1)):
      if int(bits1[i]) ^ int(bits2[i]):
        respuesta += "1"
      else:
         respuesta += "0"
  return respuesta
