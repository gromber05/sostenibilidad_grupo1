# Proyecto de Sostenibilidad - Grupo 1
### Gonzalo Romero Bernal, Luis Miguel Gomila Dominguez, Iván Roldán, Sergio Pixardo, Fran Letrán

## 1. Preparativos Iniciales

Nuestro objetivo es desarrollar una página web ecológica y sostenible, minimizando el consumo de energía. Para ello, utilizaremos los siguientes recursos:

- **Raspberry Pi**: Un pequeño ordenador de bajo consumo que servirá como servidor.
- **Tarjeta MicroSD**: Necesaria para instalar un sistema operativo en la Raspberry Pi y almacenar datos.
- **Cable Ethernet**: Para conectar la Raspberry Pi a Internet y asegurar una conexión estable.
- **Placas Solares**: Fuente de alimentación sostenible para la Raspberry Pi, reduciendo el impacto ambiental.

## 2. Configuración del Servidor Web

Para lograr una página web altamente sostenible, optaremos por un diseño minimalista sin CSS3, utilizando únicamente HTML5. Esto reducirá la carga de procesamiento y el consumo de energía.

El contenido de la página web incluirá los **17 Objetivos de Desarrollo Sostenible (ODS)**, promoviendo la concienciación sobre la sostenibilidad. La página será alojada en la Raspberry Pi con el protocolo **HTTPS** para garantizar una comunicación segura.

### Pasos para la configuración:
1. Instalar un sistema operativo ligero en la Raspberry Pi (por ejemplo, Raspberry Pi OS Lite).
2. Configurar un servidor web como **Nginx** o **Apache**.
3. Crear la página web estática con HTML5.
4. Configurar un certificado SSL gratuito con **Let's Encrypt** para habilitar HTTPS.
5. Optimizar la página para un consumo mínimo de recursos.

## 3. Configuración del Dominio

Si no dispones de una IP fija, puedes utilizar un servicio de **DNS dinámico** como **No-IP** para asignar un dominio a la IP pública de tu Raspberry Pi.

### Pasos para la configuración:
1. Registrarse en **No-IP** o un servicio similar.
2. Configurar el dominio para que apunte a la IP pública de la Raspberry Pi.
3. Abrir y redirigir los siguientes puertos en el router:
   - **Puerto 80**: Para tráfico HTTP.
   - **Puerto 443**: Para tráfico HTTPS.
4. Configurar reglas de firewall para permitir el tráfico web seguro.

Con estos pasos, lograremos una solución sostenible y accesible para nuestra página web ecológica.

---

Este proyecto busca demostrar que es posible crear una web funcional con un impacto ambiental mínimo, utilizando energías renovables y tecnologías eficientes.

