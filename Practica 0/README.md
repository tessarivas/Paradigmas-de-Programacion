# **REPORTE DE PRÁCTICA 0**
# *Introducción a Git*
## 1. Iniciar en Git Bash
- ### 1.1 Ubicarte en tu usuario
  Empezar a escribir después de **cd** el nombre de la carpeta y dar a la tecla TAB.

  **ls** Lista de archivos en esa dirección
  
  **ls -a** Con archivos ocultos

![Imagen1](/Practica%200/Imagenes/Practica0.1.png)

- ### 1.2 Crear un folder
  **mkdir** Practica0
  
  **mkdir** ‘Practica 0’ (con espacio se encierra en coma simple **‘** )

![Imagen2](/Practica%200/Imagenes/Practica0.2.png)

- ### 1.3 Editor de texto
  **nano** prueba.md

![Imagen3](/Practica%200/Imagenes/Practica0.3.png)
![Imagen4](/Practica%200/Imagenes/Practica0.4.png)

## 2. Crear un Repositorio
- ### 2.1 Iniciarlo
  Una vez ubicado en la carpeta donde deseaste crear tu repositorio anteriormente, podemos inicializar nuestro repositorio con **git init**.

![Imagen5](/Practica%200/Imagenes/Practica0.5.png)

- ### 2.2 Subir archivos
  **git add .**

![Imagen6](/Practica%200/Imagenes/Practica0.6.png)

- ### 2.3 Primer comentario
  **git commit -m**

![Imagen7](/Practica%200/Imagenes/Practica0.7.png)

## 3. Crear llave pública o privada
Solo se hace una vez por computadora.
  
- **ssh-keygen**
- **ls ~/.ssh**
- **cat ~/.ssh/id.rsa.pub**

![Imagen8](/Practica%200/Imagenes/Practica0.8.png)

## 4. Repositorio remoto y local
- ### 4.1 Agregar a repositorio local
  Utilizar el comando **git remote add origin (URL)** con el enlace proporcionado en nuestro repositorio remoto.

![Imagen12](/Practica%200/Imagenes/Practica0.12.png)
![Imagen9](/Practica%200/Imagenes/Practica0.9.png)
![Imagen10](/Practica%200/Imagenes/Practica0.10.png)

- ### 4.2 Subirlo
  **git push -u origin master**, master o main depende del usuario y version de bash que tenga.

![Imagen11](/Practica%200/Imagenes/Practica0.11.png)