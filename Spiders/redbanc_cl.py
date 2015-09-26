import xmltodict, json, urllib2,os

def dataxml(uri):
    file = urllib2.urlopen(uri)
    data = file.read()
    file.close()    
    return data

def savejson(data,archivo):
    fn = os.path.join(os.path.dirname(__file__), 'data\/json\/'+archivo)
    with open(fn, 'w+') as fp:
        json.dump(data, fp)

def loadjson(archivo):
    fn = os.path.join(os.path.dirname(__file__), 'data\/json\/'+archivo)
    with open(fn) as json_data:
        d = json.load(json_data)
        json_data.close()
        return d
    


#declaramos variables a utilizar mas tarde

comunascl={}
comunasrms={}
comunasregioness={}
cajeroschile={}

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

comunascl["regiones"]=comunasregioness
comunascl["rm"]=comunasrms
#Guardamos el Json de Comunas
savejson(comunascl,"comunas.json")

#iteramos por las comunas para obtener data de cajeros

 
comunas=loadjson("comunas.json")
#Iterando en las comunas de la region metropolitana

#cajeros = xmltodict.parse(dataxml("http://www.redbanc.cl/portal_redbanc/browse?pagina=portal_redbanc/Localizador_cajeros.xml&idioma=0&id_comuna=13110"))
 
# la estructura del xml cambio el  2011, ahora en lugar de mostrar el codigo de cajero, muestra la cantidad de cajeros que hay en la direccion, es menos util que la primera version del XML, previo al 2011




for id, comuna in comunas["rm"].items():
    cajeros = xmltodict.parse(dataxml("http://www.redbanc.cl/portal_redbanc/browse?pagina=portal_redbanc/Localizador_cajeros.xml&idioma=0&id_comuna="+id))
    cuenta=0
    if cajeros["retorno"].has_key("cajero"):
        for cajeross in cajeros["retorno"]["cajero"]:
            cuenta=cuenta+1
            cajerob={}
            cajerob["comuna"]=id
            cajerob["region"]="rm"
            cajerob["cantidad"]=cajero["numero"]
            cajerob["institucion"]=cajero["institucion"]
            cajerob["direccion"]=cajero["direccion"]
            cajerob["tipolocal"]=cajero["tipolocal"]
            cajerob["cirrus"]=cajero["cirrus"]
            cajerob["plus"]=cajero["plus"]
            cajerob["tipocajero"]=cajero["tipocajero"]
            cajerob["horario"]=cajero["horario"]
            cajeroschile[cuenta]=cajerob
    else:
        print id
        


        
for id, comuna in comunas["regiones"].items():
    cajeros = xmltodict.parse(dataxml("http://www.redbanc.cl/portal_redbanc/browse?pagina=portal_redbanc/Localizador_cajeros.xml&idioma=0&id_comuna="+id))
    cuenta=0
    if cajeros["retorno"].has_key("cajero"):
        for cajeross in cajeros["retorno"]["cajero"]:
            cuenta=cuenta+1
            cajerob={}
            cajerob["comuna"]=id
            cajerob["region"]="regiones"
            cajerob["cantidad"]=cajero["numero"]
            cajerob["institucion"]=cajero["institucion"]
            cajerob["direccion"]=cajero["direccion"]
            cajerob["tipolocal"]=cajero["tipolocal"]
            cajerob["cirrus"]=cajero["cirrus"]
            cajerob["plus"]=cajero["plus"]
            cajerob["tipocajero"]=cajero["tipocajero"]
            cajerob["horario"]=cajero["horario"]
            cajeroschile[cuenta]=cajerob
    else:
        print id
        


 


print cajeroschile

"""     for cajero in cajeros["retorno"]["cajero"]:
        print cajero["direccion"]
"""
