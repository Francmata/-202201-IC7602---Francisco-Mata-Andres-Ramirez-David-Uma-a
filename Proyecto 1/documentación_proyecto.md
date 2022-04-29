# Proyecto #1

## Instituto Tecnológico de Costa Rica

### Curso de Redes


Integrantes:

David Umaña Blanco - 2016175133

Francisco Mata Blanco - 2016106889

Andrés Ramirez Ortega - 2018172107


 <font size="4"> 

# 1. Marco Teórico 
## Docker
Docker es una plataforma de software que permite crear, probar e implementar aplicaciones empaquetando software en unidades estandarizadas llamadas contenedores que incluyen todo lo necesario para que el software se ejecute, incluidas bibliotecas, herramientas de sistema, código y tiempo de ejecución. 
Docker es un sistema operativo para contenedores. De manera similar a cómo una máquina virtual virtualiza el hardware del servidor, los contenedores virtualiza el sistema operativo de un servidor. Docker se instala en cada servidor y proporciona comandos sencillos que puede utilizar para crear, iniciar o detener contenedores. 

## Docker Compose
 Docker Compose es una herramienta para definir y ejecutar aplicaciones de Docker de varios contenedores. En Compose, se usa un archivo YAML para configurar los servicios de la aplicación. Después, con un solo comando, se crean y se inician todos los servicios de la configuración.

## DHCP
El Protocolo de configuración dinámica de host (DHCP) es un protocolo cliente/servidor que proporciona automáticamente un host de Protocolo de Internet (IP) con su dirección IP y otra información de configuración relacionada, como la máscara de subred y la puerta de enlace predeterminada. El servidor DHCP mantiene un conjunto de direcciones IP y arrienda una dirección a cualquier cliente habilitado para DHCP cuando se inicia en la red.

Algunos beneficios son: 

    1. Configuración confiable de direcciones IP: minimiza los errores de configuración causados por la configuración manual de direcciones IP, como errores tipográficos o conflictos de direcciones causados por la asignación de una dirección IP a más de una computadora al mismo tiempo.

    2. Administración de red reducida: el manejo eficiente de los cambios de dirección IP para clientes que deben actualizarse con frecuencia, como los dispositivos portátiles que se mueven a diferentes ubicaciones en una red inalámbrica.

## DNS
El Sistema de nombres de dominio se encarga de encontrar la dirección IP correcta para esos sitios. Los navegadores utilizan esas direcciones para comunicarse con los servidores de origen o los servidores perimetrales de CDN para acceder a la información del sitio web. Todo esto sucede gracias a los servidores DNS, que son máquinas dedicadas a responder a las consultas DNS.

El proceso de solución de DNS supone convertir un nombre de servidor en una dirección IP compatible con el ordenador . Se da una dirección IP a cada dispositivo en Internet, y esa dirección será necesaria para encontrar el dispositivo apropiado de Internet, al igual que se usa la dirección de una calle para encontrar una casa concreta. Cuando un usuario quiere cargar una página, se debe traducir lo que el usuario escribe en su navegador web a una dirección que el ordenador pueda entender para poder localizar la página web.

## Web Servers
Un servidor web es un software y hardware que utiliza  HTTP y otros protocolos para responder a las solicitudes de los clientes realizadas a través de la World Wide Web. El trabajo principal de un servidor web es mostrar el contenido del sitio web mediante el almacenamiento, el procesamiento y la entrega de páginas web a los usuarios. Además de HTTP, los servidores web también admiten SMTP y FTP, que se utilizan para correo electrónico, transferencia de archivos y almacenamiento. El hardware del servidor web está conectado a Internet y permite el intercambio de datos con otros dispositivos conectados, mientras que el software del servidor web controla cómo un usuario accede a los archivos alojados. El proceso del servidor web es un ejemplo del  modelo cliente/servidor. 
Se accede al software del servidor web a través de los nombres de dominio de los sitios web y garantiza la entrega del contenido del sitio al usuario que lo solicita. El lado del software también se compone de varios componentes, con al menos un servidor HTTP. El servidor HTTP es capaz de entender HTTP y URL. Como hardware, un servidor web es una computadora que almacena software de servidor web y otros archivos relacionados con un sitio web, como  documentos HTML, imágenes y archivos JavaScript.

## Routers
El enrutamiento virtual es una forma de virtualización de funciones de red, en la que las funciones de los dispositivos de red tradicionales basados ​​en hardware se convierten en software que se puede ejecutar en hardware estándar comercial listo para usar. Esto tiene las ventajas de reducir los costos de hardware y permitir una mayor interoperabilidad de hardware, en lugar de requerir una plataforma de hardware propietaria.
En la función de enrutamiento de software básico, el software de enrutamiento se agrega al servidor de productos básicos y esa pieza de hardware se convierte en un enrutador . En un entorno de enrutamiento distribuido más sofisticado, las piezas del software de enrutamiento se pueden mover por redes enteras mientras son administradas por un plano de control centralizado.

## VPN
Virtual Private Network: permite crear una red local sin necesidad de que sus integrantes estén físicamente conectados entre sí, sino a través de Internet. Es importante el componente "virtual" dentro de una VPN. Obtienen las ventajas de la red local con una mayor flexibilidad, pues la conexión es a través de Internet y puede por ejemplo ser de una punta del mundo a la otra. Cuando tenemos conexión a internet, los dispositivos tienen conexión con el proveedor de Internet, que es el que conecta con los distintos servicios web, cuando se utiliza una VPN el tráfico de red se dirige directo al servidor VPN. Esa conexión está cifrada, así el proveedor de internet no sabe realmente a que se está accediendo. La IP es la del servidor VPN, es como si físicamente se estuviera en un lugar diferente. Un gran problema de una VPN es que 
Las conexiones VPN son utilizadas en teletrabajo cuando están fuera de las oficinas y tener seguridad, evitar censura y bloqueos geográficos de contenido, capa extra de seguridad, descargas P2P.

## Proxy Reverso
Un servidor proxy es una interfaz de comunicación en una red que se hace cargo de las peticiones y las transmite en calidad de representante a un ordenador destino. En las redes corporativas se recurre a esta estructura para que los dispositivos cliente tengan un acceso controlado a Internet. Un proxy se presenta como la única posibilidad de conexión con la red pública. Un servidor de reenvío canaliza todas las solicitudes procedentes de la red interna y las transmite al servidor de destino en Internet con su propia dirección remitente. Las respuestas del servidor suelen llegar al proxy antes de que se repartan por los diferentes dispositivos cliente.
Ámbitos de aplicación de un proxy inverso: anonimización, protección y cifrado, balanceo de carga, caché, compresión de datos.


## Clientes
Un cliente es un ordenador o software que accede a un servidor y recupera servicios especiales o datos de él. Es tarea del cliente estandarizar las solicitudes, transmitirlas al servidor y procesar los datos obtenidos para que puedan visualizarse en un dispositivo de salida como una pantalla. Los clientes comúnmente son los navegadores web o los clientes de correo electrónico.
Tipos: Sistemas Operativos, Navegador web, Clientes de correo electrónico, clientes DNS, clientes VPN, aplicaciones basadas en web.


## Web Caché 
La Web Caché almacena datos en un servidor para su reutilización futura. Cuando se abre un sitio, la caché reúne todos los datos del sitio web, lo convierte en un archivo HTML y lo abre en el navegador. Si se abre el mismo sitio la caché cargará una copia, ayudando al servidor a trabajar más rápido. No todos los sitios web usan caché. En segundo lugar, la caché puede caducar o eliminarse manualmente. La caché es importante para tener un mejor rendimiento en la velocidad de carga del sitio web, menos procesamiento para solicitudes HTTP significa que el sitio web usará menos ancho de banda, especialmente si tienes recursos limitados. 
Existen diferentes tipos de caché web: de página completa, de objetos y de fragmentos. Y cada tipo de web caché tiene diferentes funciones.

## Bibliografía
1. Contenedores de Docker | ¿Qué es Docker? | AWS. (s. f.). Amazon Web Services, Inc. https://aws.amazon.com/es/docker/

2. Uso de Docker Compose para implementar varios contenedores - Azure Cognitive Services. (2022, 27 abril). Microsoft Docs. https://docs.microsoft.com/es-es/azure/cognitive-services/containers/docker-compose-recipe

3. I, Ramirez. (29 enero 2021). ¿Qué es una conexión VPN, para qué sirve y qué ventajas tiene?. Recuperado de:
https://www.xataka.com/basics/que-es-una-conexion-vpn-para-que-sirve-y-que-ventajas-tiene

4. J. (2021, 29 julio). Dynamic Host Configuration Protocol (DHCP). Microsoft Docs. https://docs.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top#:%7E:text=Dynamic%20Host%20Configuration%20Protocol%20(DHCP)%20is%20a%20client%2Fserver,subnet%20mask%20and%20default%20gateway.

5. What is a DNS server? | Cloudflare. (s. f.). Cloudflare. https://www.cloudflare.com/es-es/learning/dns/what-is-a-dns-server/

6. (17 marzo 2020). Servidor proxy inverso: componente central de la seguridad. Recuperado de: https://www.ionos.es/digitalguide/servidores/know-how/que-es-un-servidor-proxy-inverso/

7. Gillis, A. S. (2020, 22 julio). web server. WhatIs.Com. https://www.techtarget.com/whatis/definition/Web-server

8. ¿Qué es un Cliente? Cliente. (s/f). Ryte.com. Recuperado el 29 de abril de 2022, de: https://es.ryte.com/wiki/Cliente

9. SDxCentral. (2021, 19 marzo). Server Resolution Error 1001. https://www.sdxcentral.com/networking/nfv/mano-lso/definitions/whats-a-virtual-router-vrouter/#:%7E:text=A%20Virtual%20Router%2C%20or%20vRouter,used%20a%20dedicated%20hardware%20device.

</font>  