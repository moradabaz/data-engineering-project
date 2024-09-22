
# Amazon EC2 

Amazon EC2 (Elastic Compute Cloud) es un servicio web que proporciona capacidad de cómputo escalable en la nube de Amazon Web Services (AWS). EC2 permite a los usuarios lanzar y administrar instancias virtuales de servidores, proporcionando una infraestructura de computación flexible y económica.

### Características Principales de Amazon EC2

1. **Escalabilidad y Flexibilidad**:
   - **Escalado Vertical y Horizontal**: Puedes escalar tus recursos hacia arriba (más potencia) o hacia abajo (menos potencia), así como añadir o eliminar instancias según sea necesario para manejar las cargas de trabajo.
   - **Amplia Gama de Tipos de Instancia**: EC2 ofrece una variedad de tipos de instancias optimizadas para diferentes necesidades de computación, memoria, almacenamiento y redes.

2. **Modelos de Compra**:
   - **On-Demand**: Paga por la capacidad de computación que utilizas por hora o por segundo sin compromisos a largo plazo.
   - **Reserved Instances**: Compra instancias reservadas para obtener descuentos significativos en comparación con las instancias On-Demand.
   - **Spot Instances**: Aprovecha la capacidad de computación no utilizada a precios reducidos, ideal para aplicaciones flexibles y tolerantes a fallos.
   - **Savings Plans**: Programas de ahorro que ofrecen descuentos en el uso de computación, independientemente de la familia de instancias, el tamaño, la región, el sistema operativo o el tenencia.

3. **Seguridad y Redes**:
   - **Seguridad**: Las instancias EC2 pueden estar aisladas dentro de una Virtual Private Cloud (VPC) y pueden ser configuradas con grupos de seguridad y roles IAM para controlar el acceso.
   - **Elastic IP Addresses**: IP estáticas que se pueden reasignar entre diferentes instancias dentro de una cuenta de AWS.
   - **Elastic Load Balancing (ELB)**: Distribuye automáticamente el tráfico entrante entre múltiples instancias de EC2.

4. **Almacenamiento**:
   - **Amazon EBS (Elastic Block Store)**: Proporciona almacenamiento de bloques persistente para instancias EC2.
   - **Instance Store**: Almacenamiento temporal que se elimina cuando la instancia se detiene o termina.

5. **Gestión y Automatización**:
   - **Amazon CloudWatch**: Monitorea tus instancias y otros recursos de AWS, recolectando y rastreando métricas.
   - **Auto Scaling**: Ajusta automáticamente el número de instancias EC2 en función de las condiciones que definas para mantener el rendimiento y minimizar el costo.
   - **AWS Lambda**: Ejecuta código en respuesta a eventos sin necesidad de aprovisionar o gestionar servidores.

### Ejemplos de Uso de Amazon EC2

1. **Alojamiento de Aplicaciones Web y Móviles**:
   - Lanza instancias EC2 para alojar servidores web, aplicaciones móviles y APIs, escalando la capacidad según el tráfico.

2. **Procesamiento de Grandes Volúmenes de Datos**:
   - Utiliza instancias optimizadas para tareas de computación intensiva, como el procesamiento de big data, análisis de datos y aprendizaje automático.

3. **Entornos de Desarrollo y Pruebas**:
   - Crea entornos de desarrollo y pruebas replicables y escalables, permitiendo a los desarrolladores desplegar y probar sus aplicaciones de manera eficiente.

4. **Ejecutar Aplicaciones Empresariales**:
   - Implementa aplicaciones empresariales como SAP, Oracle, y Microsoft en instancias EC2 para aprovechar la escalabilidad y flexibilidad de la nube.

### Lanzar una Instancia EC2 Básica

Aquí hay una guía rápida para lanzar una instancia EC2 básica usando la consola de AWS:

1. **Iniciar Sesión en la Consola de AWS**:
   - Accede a la consola de AWS en [aws.amazon.com](https://aws.amazon.com).

2. **Navegar a EC2**:
   - En el panel de navegación, selecciona "EC2" bajo la categoría "Compute".

3. **Lanzar una Instancia**:
   - Haz clic en "Launch Instance".
   - Selecciona una AMI (Amazon Machine Image) que define el software que se ejecutará en la instancia, como Amazon Linux 2 o Ubuntu.
   - Elige el tipo de instancia (por ejemplo, t2.micro para uso gratuito).
   - Configura los detalles de la instancia, elige una VPC y subred, y establece otras opciones de red.
   - Añade almacenamiento (EBS).
   - Configura etiquetas (opcional).
   - Configura el grupo de seguridad para controlar el tráfico entrante y saliente.
   - Revisa y lanza la instancia. Se te pedirá que selecciones o crees un par de claves para acceder a la instancia mediante SSH.

4. **Acceder a la Instancia**:
   - Una vez que la instancia esté en estado "running", puedes acceder a ella utilizando el cliente SSH con la clave privada que descargaste.

```bash
ssh -i /path/to/your-key.pem ec2-user@your-instance-public-dns
```

### Similitudes con un Servidor Tradicional

1. **Capacidad de Computación**:
   - Al igual que un servidor tradicional, una instancia EC2 proporciona capacidad de computación, incluyendo CPU, memoria (RAM), y almacenamiento.

2. **Sistemas Operativos**:
   - Puedes elegir y configurar el sistema operativo en una instancia EC2, como Linux, Windows, o macOS, similar a cómo lo harías en un servidor físico.

3. **Aplicaciones y Servicios**:
   - Puedes instalar y ejecutar aplicaciones y servicios en una instancia EC2 del mismo modo que lo harías en un servidor físico.

4. **Acceso Remoto**:
   - Puedes acceder y gestionar una instancia EC2 de forma remota mediante SSH (para Linux) o RDP (para Windows), igual que lo harías con un servidor en tu infraestructura local.

### Diferencias con un Servidor Tradicional

1. **Elasticidad y Escalabilidad**:
   - **Escalabilidad Automática**: Puedes escalar fácilmente la capacidad de computación añadiendo o eliminando instancias según las necesidades, sin necesidad de comprar hardware adicional.
   - **Escalado Automático**: Con servicios como Auto Scaling, las instancias pueden aumentar o disminuir automáticamente en respuesta a cambios en la demanda.

2. **Pago por Uso**:
   - **Costo por Uso**: Pagas solo por la capacidad de computación que realmente utilizas, ya sea por hora o por segundo, en lugar de hacer una inversión inicial significativa en hardware.

3. **Flexibilidad de Configuración**:
   - **Amplia Variedad de Instancias**: Puedes elegir entre una amplia gama de tipos de instancias optimizadas para diferentes necesidades de computación, memoria, almacenamiento y redes.

4. **Integración con Otros Servicios de AWS**:
   - **Almacenamiento en la Nube**: Integración nativa con servicios de almacenamiento como Amazon S3 y Amazon EBS.
   - **Redes y Seguridad**: Configura redes privadas virtuales (VPC), balanceadores de carga (ELB), y políticas de seguridad de manera sencilla.

5. **Gestión y Mantenimiento**:
   - **Reducción del Mantenimiento de Hardware**: AWS se encarga del mantenimiento físico del hardware subyacente, lo que reduce la carga de gestión y mantenimiento en tu equipo de TI.
   - **Disponibilidad y Recuperación ante Desastres**: EC2 proporciona capacidades de alta disponibilidad y opciones de recuperación ante desastres.

6. **Despliegue Rápido**:
   - **Provisionamiento Rápido**: Puedes lanzar una instancia EC2 en minutos, lo que es mucho más rápido que adquirir y configurar un servidor físico.

### Ejemplo de Uso de Amazon EC2 como Servidor

Para ilustrar cómo Amazon EC2 puede actuar como un servidor, aquí tienes un ejemplo práctico de configuración de una instancia EC2 para alojar un sitio web:

1. **Lanzar una Instancia EC2**:
   - Accede a la consola de AWS, navega a EC2 y lanza una nueva instancia.
   - Selecciona una Amazon Machine Image (AMI), como Amazon Linux 2.
   - Elige un tipo de instancia (por ejemplo, `t2.micro` para uso gratuito).
   - Configura los detalles de la instancia y añade almacenamiento.
   - Configura un grupo de seguridad para permitir tráfico HTTP/HTTPS.

2. **Configurar el Servidor Web**:
   - Conéctate a la instancia utilizando SSH.
   
   ```bash
   ssh -i /path/to/your-key.pem ec2-user@your-instance-public-dns
   ```

   - Instala un servidor web (por ejemplo, Apache).

   ```bash
   sudo yum update -y
   sudo yum install -y httpd
   sudo systemctl start httpd
   sudo systemctl enable httpd
   ```

3. **Alojar el Sitio Web**:
   - Sube los archivos de tu sitio web al directorio del servidor web.

   ```bash
   sudo mv /path/to/your/website/* /var/www/html/
   ```

4. **Acceder al Sitio Web**:
   - Abre un navegador web y navega a la dirección pública de tu instancia EC2. Deberías ver tu sitio web en funcionamiento.

### Resumen

Amazon EC2 puede funcionar como un servidor, proporcionando capacidad de computación, almacenamiento y servicios de red. Sin embargo, ofrece ventajas significativas en términos de elasticidad, escalabilidad, flexibilidad de configuración, integración con otros servicios de AWS, y gestión simplificada en comparación con los servidores tradicionales. Esto lo hace ideal para una amplia variedad de aplicaciones y cargas de trabajo en la nube.

### Resumen

Amazon EC2 es una plataforma versátil y potente que ofrece capacidad de computación elástica en la nube. Su capacidad de escalar, junto con una amplia gama de opciones de configuración y modelos de compra, lo hacen ideal para una gran variedad de aplicaciones, desde sitios web y aplicaciones móviles hasta procesamiento de grandes volúmenes de datos y entornos de desarrollo.
