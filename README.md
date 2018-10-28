# BreadBad

* Es un geolocalizador de direcciones ip's para buscar no solo la ubicación, también información importante como: País, Código del país, Ciudad, ISP, Organización, Latitud, Longitud, Asociación, Región, Nombre de la región, Zona horaria, Google maps
* Ademas de geolocalizar una ip tambien geolocaliza los dominios como ejemplo: example.com
* Se mostrara la informacion de tu ip al ejecutar BreadBad

# Uso

* Al ejecutar BreadBad nos aparecera la siguiente interface:

### NOTA: 
        ** Se quitaron los valores y se sobreescribieron por el valor '-', para que no se muestre la informacion correcta de la direccion ip **

### Interface:

BreadBad: An ip geolocation tool by means of a console, written in python and fully functional thanks to the api of: http://ip-api.com/json/

[*] Created by: DtxdF

Help Main:

        IPAdress        ::       The command to define the ip to geolocate
        Country         ::       See the country of the defined ip
        City            ::       See the city of the defined ip
        Country_Code    ::       See the country code of the defined ip
        ISP             ::       See the internet service protocol (ISP) of the defined ip
        ORG             ::       See the company organization of the defined ip
        latitude        ::       See the latitude of the defined ip
        longitude       ::       See the length of the defined ip
        Query           ::       See the query of the defined ip
        Association     ::       See the association of the company of the defined ip
        region          ::       See the region of the defined ip
        region_name     ::       See the name belonging to the defined ip
        TimeZone        ::       See the time zone of the defined ip
        Google_Maps     ::       Show the link of google maps
        zipCode         ::       Show the zip code
        all_information ::       Show the all information from the ip address


Geolocation to you:


        Country(-)              :: -
        City                    :: -
        ISP                     :: -
        Organization            :: -
        Latitude                :: -
        Longitude               :: -
        Query                   :: -
        Association             :: -
        Region                  :: -
        Region Name             :: -
        Time Zone               :: -
        Time Zone               :: -
        Zip Code                :: -
        Google maps             :: -


[BreadBad] >

### Para geolocalizar una ip se dispone del siguiente comando de BreadBad:

[BreadBad] > ipadress example.com

[BreadBad] > all_information


Geolocation to example.com:



        Country(US)             :: United States
        City                    :: Norwell
        ISP                     :: EdgeCast Networks
        Organization            :: Verizon Business
        Latitude                :: 42.1508
        Longitude               :: -70.8228
        Query                   :: 93.184.216.34
        Association             :: AS15133 MCI Communications Services, Inc. d/b/a Verizon Business
        Region                  :: MA
        Region Name             :: Massachusetts
        Time Zone               :: America/New_York
        Zip Code                :: 02061
        Google maps             :: https://www.google.com/maps/place/42.1508,-70.8228/@42.1508,-70.8228,16z


[BreadBad] >

# Instalacion

* Instale python(Recomendable 2.7), Desde la web oficial: https://www.python.org
* Instale la dependencia, colorama con el siguiente comando: pip install colorama

# Gracias a

* - Gracias a la api de: http://ip-api.com/json/, BreadBad tiene vida para geolocalizar una ip

# Imagenes:

![](https://i.imgur.com/pwQhMtg.png)

![](https://i.imgur.com/drWDU5R.png)
