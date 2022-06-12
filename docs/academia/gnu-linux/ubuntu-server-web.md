title: Configurar Ubuntu Server para servicios web | GNU/Linux | Academia | Hektor Profe
description: Aprende a configurar tu propio servidor Ubuntu Server para desplegar servicios web usando Nginx y certificados SSL.

# Configurar Ubuntu Server para servicios web

<div class="contenedor_youtube">
  <iframe id="odysee-iframe" width="560" height="315" src="https://odysee.com/$/embed/-Curso--Ubuntu-Server-b%C3%A1sico/2b53b43cefdd68ed78c3d01ff27309bf2663b1e3?r=3icueB68NV3UEFHyqs2QRfzRUeABmHDU" allowfullscreen></iframe>
</div>

## Bienvenida

Vamos a aprender a configurar un servidor GNU/Linux para desplegar diferentes servicios web utilizando la distribución Ubuntu Server. Pero... ¿por qué os debería interesar aprender esto? Porque si sois desarrolladores web podréis ahorraros muchísimo dinero.

La mayoría de empresas de hosting ofrecen la posibilidad de publicar un proyecto como un producto, de manera que si quieres tener varios proyectos alojados debes pagar múltiples veces. No me refiero al dominio, eso siempre hay que pagarlo, sino al servidor que tendrá en marcha tu proyectos las 24 horas del día.

Yo nunca trabajo de esa forma y eso es porque sé configurar mis propios servidores. Gracias a ello me ahorro mucho dinero porque pago una infraestructura y la reutilizo. Por ejemplo puedo tener un blog personal con PHP y Wordpress, mi bot para Discord, el frontend de mi academia funcionando con Node.js y varias API creadas con Python y Django, todo corriendo en paralelo en la misma máquina pero en diferentes dominios y subdominios.

Eso es lo que quiero compartir con vosotros, unas guías paso a paso para que podáis configurar vuestro propio servidor y alojar en él tantos servicios como queráis. Evidentemente lo suyo es que sepáis de antemano címo funciona la línea de comandos de Linux, pero al final como son sólo configuraciones podéis seguir los pasos y deberíais de lograr el mismo resultado.

Para tomar estos cursos no os voy a pedir que instaléis Ubuntu Server sino que creéis una cuenta en el proveedor Digital Ocean donde podréis manejar unos servidores virtuales llamados Droplets que soportan diferentes sistemas operativos. Mantener en marcha un Droplet tiene un coste mínimo de $5 dólares mensuales pero yo os facilitaré un enlace para registraros y probar el servicio de forma gratuita durante 30 días para que podáis practicar. Pasado ese primer mes podéis borrar la cuenta o seguir utilizando el servicio si os ha convencido. Óbviamente si tenéis Ubuntu Server en cualquier otro hosting pues también podéis seguir el curso sin problemas.

## Registro en Digital Ocean

Lo primero será que os creéis [una cuenta en Digital Ocean a través de este enlace](https://m.do.co/c/e2ff725d5acf), os voy a mostrar los pasos pero tened en cuenta que el proceso puede cambiar en el futuro.

El requisito más importante para crear la cuenta es añadir un método de pago, ya sea una tarjeta de crédito o una cuenta Paypal. Os recomiendo configurar una tarjeta porque con Paypal os pedirán realizar un prepago de $5, no sé porqué pero así es como funciona y con la tarjeta no os cobrarán nada.

Si por alguna razón no tenéis tarjeta o cuenta de Paypal para utilizar Digital Ocean ni tampoco tenéis otro proveedor, como última alternativa podéis crear vuestro propio servidor Ubuntu Server para practicar en una máquina virtual, os [dejaré un tutorial](https://vivaubuntu.com/instalar-ubuntu-server-18-04-lts-en-virtualbox/) en los apuntes.

Eventualmente durante el registro os pedirá crear un primer proyecto, podéis poner el nombre que queráis por ejemplo **Pruebas** y finalizar la creación de la cuenta sin contestar las encuestas que os harán.

Al final acabaréis llegando al panel de usuario de Digital Ocean donde podremos empezar a trabajar.

## Creando un Droplet

Vamos a crear nuestro Droplet, para ello estando en el proyecto haremos clic en el botón superior **Create** > **Droplets**.

Crearemos un Droplet con las siguientes características:

- Ubuntu Server LTS
- Plan Standard de $5/m
- Datacenter en New York
- Autenticación usando contraseña de un uso.
- Optativamente podéis darle un nombre al droplet.

Una vez la barra llegue al final tendremos nuestro Droplet con Ubuntu Server creado y listo para empezar a usarlo.

En cuanto recibáis un correo de confirmación con los datos del Droplet y la contraseña podemos continuar con la siguiente lección.

## Primera conexión SSH

Para conectarnos al Droplet utilizaremos el protocolo SSH. En Windows os recomiendo [instalar Git](https://git-scm.com/), el software control de versiones, para utilizar su terminal integrada Git Bash que incluye un cliente SSH, podéis seguir todos los pasos por defecto en la instalación.

Una vez instalado Git abriremos una terminal en cualquier parte haciendo clic derecho y nos conectaremos al Droplet.

Necesitaremos las credenciales que habréis recibido en email:

- La IP del Droplet.
- La contraseña del usuario root.

El usuario **root** es el más importante de un sistema GNU/Linux y vamos a acceder con él para realizar la configuración inicial del servidor:

```bash
ssh root@WW.XX.YY.ZZ
```

Si se conecta correctamente lo primero que hará el servidor es establecer una nueva contraseña de preferencia personal, hay que repetir de nuevo la que nos dan de un uso y confirmar la nueva dos veces.

### Chuleta de comandos para terminal Bash

Una vez nos hemos conectado vamos a aprovechar para hacer un pequeño repaso de los comandos básicos de Linux que estaremos utilizando:

- **pwd**: Siglas del comando **print working directory** que nos muestra el directorio actual donde nos encontramos.
- **ls**: Del inglés **list** muestra el contenido del directorio donde nos encontramos.
- **ls -l**: Muestra el contenido del directorio en forma más amigable.
- **ls -la**: Muestra todo el contenido del directorio incluyendo los ficheros ocultos.
- **cd /ruta**: Siglas del comando **change directory** para cambiar de directorio. Un puntito **.** hace referencia al directorio actual y dos puntitos **..** al directorio anterior al actual.
- **tabulación**: Autocompleta nombres de ficheros y directorios.
- **touch /ruta/fichero**: Crea un fichero vacío en la ruta que indiquemos.
- **nano /ruta/fichero**: Abre el editor **nano** para la terminal que permite editar y guardar ficheros.
- **cat /ruta/fichero**: Muestra el contenido de un fichero en la terminal.
- **head -n 1 /ruta/fichero**: Muestra la primera línea (o las que especifiquemos) de un fichero.
- **rm /ruta/fichero**: Siglas del comando **remove** que sirve para borrar un fichero.
- **exit**: Cierra la sesión del usuario actual.
- **control + C**: Cierra forzosamente la conexión SSH.
- **control + L**: Limpia el contenido de la terminal.

Con esto ya hemos visto lo más esencial, a continuación procederemos a crear un usuario administrador.

## Creando un administrador

El usuario **root** en Linux es muy peligroso porque tiene todos los privilegios dentro de la máquina, por eso no es aconsejable utilizarlo como administrador del sistema.

En su lugar vamos a crear un nuevo usuario administrador con el que vamos a estar trabajando:

```bash
adduser usuario
```

Le daremos los permisos de administrador:

```bash
usermod -aG sudo usuario
```

Podemos listar los usuarios y grupos del sistema con el comando:

```bash
cat /etc/passwd
```

Con una tubería podemos usar la herramienta **grep** para filtrar por un texto:

```bash
cat /etc/passwd | grep usuario
```

Finalmente vamos a cambiar a la sesión del usuario **usuario**:

```bash
su usuario
```

Y a partir de ahora para conectarnos al servidor lo haremos con nuestro usuario administrador:

```bash
ssh usuario@WW.XX.YY.ZZ
```

## Accediendo con clave SSH

SSH proporciona distintos tipos de autenticación, incluyendo contraseña y autenticación basada en claves. La autenticación basada en claves es un método muy seguro porque utiliza claves criptográficas para establecer una conexión de confianza entre el servidor y el cliente.

Para usarla hay que generar un par de claves SSH que consisten en una clave pública y otra privada. La clave pública se guarda en el servidor, mientras que la privada se guarda en el ordenador cliente. Cuando te conectas mediante SSH se establece una conexión de confianza entre el servidor y el ordenador usando el par de claves. Si alguna de las claves falta o no concuerda con la otra no se podrá establecer conexión.

Si nunca habéis generado una clave tendréis que hacerlo desde una terminal de **Git Bash** en vuestro ordenador cliente:

```bash
ssh-keygen -o
```

Una vez completado el proceso podemos acceder al directorio donde se almacenan las claves SSH del usuario haciendo:

```bash
cd ~/.ssh
ls
```

Aquí podemos mostrar por pantalla la clave pública con:

```bash
cat id_rsa.pub
```

La tendréis que seleccionar y copiar al portapapeles.

A continuación accederemos de nuevo al servidor, nos identificaremos con la contraseña:

```bash
ssh usuario@WW.XX.YY.ZZ
```

Y añadiremos la clave pública al directorio **.ssh** de nuestro usuario, si no existe tendremos que crearlo antes:

```bash
mkdir .ssh
nano .ssh/id_rsa.pub
```

Ahora añadiremos la clave pública al fichero **.ssh/authorized_keys** para autorizarla como clave de confianza:

```bash
cd .ssh
cat id_rsa.pub >> authorized_keys
```

Finalmente reiniciaremos el servicio **ssh**:

```bash
sudo service ssh restart
```

Si salimos de la sesión y nos conectamos de nuevo al servidor ya no debería volver a pedirnos la contraseña:

```bash
ssh usuario@WW.XX.YY.ZZ
```

## Configurando un dominio

Antes de iniciar la configuración del servidor web deberéis configurar un dominio o subdominio para que apunte al Droplet usando un registro de tipo **A**.

Evidentemente necesitáis contar con un dominio de antemano, pero si no es así podéis registrar uno gratuito en [dot.tk](http://www.dot.tk/es/index.html) que os servirá para el curso y es lo que yo voy a hacer, buscáis si el dominio que queréis está disponible, en mi caso **hektorprofe.tk**, lo añadís al carro y finalizáis la compra.

Durante la confirmación podéis decirle que os dure 12 meses gratis y también podréis configurar los registros **A** para que apunten al Droplet de Digital Ocean, tanto para la raíz como para el subdominio www:

<div class="image">
   <img src="{{cdn}}/linux/dominiotk.png">
</div>

Cada proveedor os ofrecerá un panel diferente, tendréis que buscar la opción que os permita editar los registros de la zona DNS y si no la encontráis preguntar al soporte técnico para que os ayuden.

En todo caso si decidís crear el dominio **tk** os llegará un email para confirmar el último paso, tendréis que introducir vuestros datos y una vez hecho tendréis que esperar a que se propaguen las DNS, un proceso que puede tardar varias horas, así que paciencia.

De tanto en tanto vaciad el caché DNS y haced un **ping** desde la terminal al dominio a ver si lo encuentra:

```bash
ipconfig /flushdns
ping hektorprofe.tk
```

<div class="image">
   <img src="{{cdn}}/linux/pingdominio.png">
</div>

Cuando os devuelva una respuesta desde la IP del Droplet ya lo tendréis todo listo para la siguiente lección y aunque podéis continuar igualmente no podréis comprobar si lo que hacéis os funciona.

## Primeros pasos con Nginx

En este punto, con el usuario administrador ya creado y el subdominio o dominio apuntando al Droplet estamos preparados para configurar el servidor web Nginx, el programa que se encargará de tres tareas vitales:

- Exponer el puerto 80 del droplet públicamente en Internet.
- Procesar las peticiones que se reciban en los dominios y subdominios configurados.
- Actuar como proxy reverso para redirigir las peticiones a los diferentes servicios en ejecución.

Así que vamos a empezar con la instalación y configuración básica.

Para actualizar el repositorio e instalaremos Nginx necesitamos ejecutar los comandos como administradores, para ello pondremos el comando **sudo** delante de las instrucciones, que significa **super user do**:

```bash
sudo apt update
sudo apt install nginx
```

Añadiremos SSH y Nginx al cortafuegos:

```bash
sudo ufw enable
sudo ufw allow ssh
sudo ufw allow 'Nginx HTTP'
sudo ufw status
```

Si nos aparece en la lista lo tenemos bien.

Comprobaremos el estado de Nginx:

```bash
systemctl status nginx
```

Si aparece **active (running)** es que está funcionando así que desde un navegador podemos comprobar si la IP nos devuelve la bienvenida de Nginx:

```
http://WW.XX.YY.ZZ
```

### Chuleta de comandos para gestionar Nginx

Para **parar** el servidor:

```bash
sudo systemctl stop nginx
```

Para **iniciar** el servidor después de pararlo:

```bash
sudo systemctl start nginx
```

Para **reiniciar** el servidor:

```bash
sudo systemctl restart nginx
```

Para **recargar** los cambios después de editar la configuración:

```bash
sudo systemctl reload nginx
```

Para desactivar que Nginx se inicie automáticamente con el servidor:

```bash
sudo systemctl disable nginx
```

Para **reactivarlo**:

```bash
sudo systemctl enable nginx
```

## Bloques de servidor

Nginx trae una configuración por defecto que expone el puerto 80 del servidor pero nosotros queremos configurar dominios y subdominios así que tendremos que realizar configuraciones individuales para cada caso, eso se hace en lo que se denominan los **Server Blocks** de Nginx.

Así que vamos a configurar nuestro dominio en un server block, primero creando un directorio donde almacenar los ficheros:

```bash
sudo mkdir -p /var/www/hektorprofe.tk/html
```

La opción **-p** creará toda la ruta de directorios automáticamente hasta el último, que es la carpeta **html**.

Ahora un paso muy importante, asignaremos el propietario del directorio con la variable de sistema **$USER**:

```bash
sudo chown -R $USER:$USER /var/www/hektorprofe.tk/html
```

Y también le daremos unos permisos de lectura, escritura y ejecución:

```bash
sudo chmod -R 755 /var/www/hektorprofe.tk
```

Ahora crearemos un fichero **index.html** de prueba para nuestro dominio:

```bash
nano /var/www/hektorprofe.tk/html/index.html
```

Con el siguiente contenido:

`/var/www/hektorprofe.tk/html/index.html`

```html
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Bienvenido a hektorprofe.tk!</title>
  </head>
  <body>
    <h1>¡El bloque de servidor de hektorprofe.tk está funcionando!</h1>
  </body>
</html>
```

Ahora tendremos que añadir la configuración del bloque de servidor, eso lo haremos creando un fichero con el nombre del dominio o subdominio en el directorio **/etc/nginx/sites-available/**, que como su nombre indica almacena las configuraciones de los sitios disponibles para ser utilizados por **Nginx**:

```bash
sudo nano /etc/nginx/sites-available/hektorprofe.tk
```

Dentro añadiremos exactamente esta configuración:

`/etc/nginx/sites-available/hektorprofe.tk`

```
server {
    listen 80;
    listen [::]:80;

    root /var/www/hektorprofe.tk/html;
    index index.html index.htm;

    server_name hektorprofe.tk www.hektorprofe.tk;

    location / {
            try_files $uri $uri/ =404;
    }
}
```

Después de guardar nos faltará hacer una última cosa, activar el bloque de servidor, algo que haremos creando un enlace del fichero que acabamos de crear en el directorio **/etc/nginx/sites-enabled/**, que como su nombre indica almacena la configuración de los sitios activados:

```bash
sudo ln -s /etc/nginx/sites-available/hektorprofe.tk /etc/nginx/sites-enabled/
```

En este punto tendremos dos bloques activos:

- **hektorprofe.tk**: Para responder las peticiones a **hektorprofe.tk** y **www.hektorprofe.tk**
- **default**: Para responder cualquier petición al puerto 80 que no responda ningún otro bloque de servidor.

En este punto ya lo tenemos preparado pero haremos un último ajuste para permitir el uso de nombres largos de dominio descomentando una línea de la configuración de **Nginx**:

```bash
sudo nano /etc/nginx/nginx.conf
```

Esta es la línea:

`/etc/nginx/nginx.conf`

```
...
http {
    ...
    server_names_hash_bucket_size 64;
    ...
}
...
```

Ahora antes de reiniciar **Nginx** y aplicar los cambios podemos comprobar si la configuración está correcta con el comando:

```bash
sudo nginx -t
```

Si no se queja reiniciaremos el servidor:

```bash
sudo systemctl restart nginx
```

En este momento ya deberíamos ser capaces de acceder a nuestro dominio y ver el **index.html** que creamos en el bloque del servidor:

```
http://www.hektorprofe.tk
```

### Chuleta de ficheros y directorios de Nginx

- **/var/www/html**: Ruta donde se almacena el contenido por defecto que muestra Nginx (su default), puede ser cambiado en el fichero de configuración principal.
- **/etc/nginx/nginx.conf**: Ruta del fichero de configuración principal.
- **/etc/nginx/sites-available/**: Directorio que contiene las configuraciones de los bloques de servidor disponibles pero no activados.
- **/etc/nginx/sites-enabled/**: Directorio que contiene las configuraciones de los bloques de servidor activados, normalmente enlazado desde el directorios de bloques de servidor disponibles.
- **/etc/nginx/snippets**: Directorio que contiene fragmentos configurables incluidos globalmente en la configuración de Nginx.
- **/var/log/nginx/access.log**: Fichero que almacena un registro de las peticiones recibidas.
- **/var/log/nginx/error.log**: Fichero que almacena un registro de los posibles errores.

## Creando certificados SSL

Let's Encrypt es una Autoridad de Certificación que proporciona una manera fácil de obtener e instalar certificados TLS/SSL gratuitos para habilitar las conexiones HTTPS cifradas en los servidores web.

Simplifica el proceso al proporcionar un cliente de software llamado Certbot que intenta automatizar la mayoría de los pasos necesarios para obtener e instalar el certificado en los servidores Apache y Nginx.

En esta lección utilizaremos Certbot para obtener un certificado SSL gratuito, lo configuraremos para que funcione en nuestro dominio usando Nginx y haremos que se renueve automáticamente, ya que por defecto tienen una duración de 90 días.

Empezaremos instalando **Certbot**:

```bash
sudo add-apt-repository ppa:certbot/certbot
sudo apt install python-certbot-nginx
```

Con esto tendremos **Certbot** listo para funcionar con **Nginx**.

Ahora es vital comprobar que tenemos tanto el dominio raiz como el subdominio **www** configurados en el mismo bloque de servidor:

```bash
sudo nano /etc/nginx/sites-available/hektorprofe.tk
```

Apareciéndonos ambos en la línea del **server_name**:

`/etc/nginx/sites-available/hektorprofe.tk`

```
...
http {
    ...
    server_names_hash_bucket_size 64;
    ...
}
...
```

Si lo tenemos bien podemos continuar añadiendo permiso al cortafuegos para que Nginx pueda funcionar tanto por HTTP como HTTPS:

```bash
sudo ufw status
sudo ufw allow 'Nginx Full'
sudo ufw delete allow 'Nginx HTTP'
sudo ufw status
```

Si en la lista nos aparece **Nginx Full** ya tendremos bien.

Ahora vamos a generar los certificados SSL para nuestro dominio raíz y su subdominio **www**:

```bash
sudo ufw st
sudo certbot --nginx -d hektorprofe.tk -d www.hektorprofe.tk
```

Eventualmente tendremos que indicar si queremos redireccionar todas las peticiones a HTTPS, os recomiendo hacerlo así que podéis poner un **1**.

En este punto el certificado estará descargado, instalado y cargado en Nginx, lo último que nos falta es verificar que el servicio de renovación automática está funcionando:

```bash
sudo certbot renew --dry-run
```

Si no devuelve ningún error significa que tenemos configurado el servicio de renovación automático correctamente así que ya hemos acabado. Sólo nos falta reiniciar **Nginx**:

```bash
sudo nginx -t
sudo systemctl restart nginx
```

Y comprobar si al aceder al sitio nos carga el certificado correctamente:

```
https://www.hektorprofe.tk
```

### Tutoriales útiles de Certbot

- [Actualizar certificado de un dominio](https://certbot.eff.org/docs/using.html#re-creating-and-updating-existing-certificates)

- [Cambiar un certificado de un dominio](https://certbot.eff.org/docs/using.html#changing-a-certificate-s-domains)

---

<small class="edited"><i>Última edición: 17 de Marzo de 2021</i></small>
