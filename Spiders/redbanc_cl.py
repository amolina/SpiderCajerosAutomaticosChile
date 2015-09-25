import xmltodict, json, urllib2

def dataxml(uri):
    file = urllib2.urlopen(uri)
    data = file.read()
    file.close()
    
    return data

#declaramos variables a utilizar mas tarde

comunascl={}
comunasrms={}
comunasregioness={}

 #Descargamos el listado de Comunas
comunas = xmltodict.parse(dataxml("http://www.redbanc.cl/portal_redbanc/browse?pagina=portal_redbanc/comunas.xml"))

#Iteramos con la region metropolitana
comunasrm=comunas["retorno"]["comuna-metropolitana"]["comuna"]


#Al iterar meteremos las comunas en una base de datos local
cuenta=0
for comuna in comunasrm:
    cuenta=cuenta+1
    #lacomuna={}
    codigo=comuna["id"]
    nombre=comuna["nombre"].encode("utf-8")
    #lacomuna[codigo]=nombre
    #lacomuna['nombre']=nombre
    comunasrms[codigo]=nombre

#iteramos por regiones
comunasreg=comunas["retorno"]["comuna-regional"]["comuna"]
#Al iterar meteremos las comunas en una base de datos local
cuenta=0
for comuna in comunasreg:
    cuenta=cuenta+1
    #lacomuna={}
    codigo=comuna["id"]
    nombre=comuna["nombre"].encode("utf-8")
    #lacomuna[codigo]=nombre
    #lacomuna['nombre']=nombre
    comunasregioness[codigo]=nombre

print comunasrms
print "-----"
print comunasregioness

