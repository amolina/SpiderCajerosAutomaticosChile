import xmltodict, json, urllib2

def dataxml(uri):
    file = urllib2.urlopen(uri)
    data = file.read()
    file.close()
    
    return data

 #Descargamos el listado de Comunas
comunas = xmltodict.parse(dataxml("http://www.redbanc.cl/portal_redbanc/browse?pagina=portal_redbanc/comunas.xml"))

#Iteramos con la region metropolitana
comunasrm=comunas["retorno"]["comuna-metropolitana"]["comuna"]
#Al iterar meteremos las comunas en una base de datos local
for comuna in comunasrm:
    print comuna

