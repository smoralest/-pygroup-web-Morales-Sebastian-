	# Tipos de peticiones y codigos de respuesta HTTP

## Peticiones:outbox_tray: :

Las peticiones se pueden clasificar en dos grupos:

* Safe: Es considerado safe o seguro si no altera el estado del servidor. En otras palabras, un método es seguro si conduce a una operación de ‘sólo lectura’. Algunos de los métodos HTTP más comunes son seguros: OPTIONS, GET o HEAD. 

Incluso si los métodos seguro tienen una semántica de sólo lectura, los servidores pueden alterar su estado, como por ejemplo: pueden registrar o mantener estadísticas. Lo importante es que de esta forma los usuarios pueden hacer uso de los métodos seguros sin preocuparse de que se realicen cambios en el servidor o de crearle cargas innecesarias a este último.

* Idempotent: Así como un objeto cualquiera tiene la propiedad de idempotencia si al realizar una operación muchas veces da el mismo resultado cual si se hubiese realizado la operación una sola vez, un método HTTP es idempotente si una solicitud idéntica puede realizarse una o demasiadas veces consecutivamente obteniendo el mismo resultado dejando al servidor en el mismo estado.

Los métodos que (implementados correctamente) son idempotentes son el GET, HEAD, PUT y DELETE.	

### Listado de peticiones HTTP :

* **GET** : El método GET significa recuperar cualquier información (en forma de una entidad) identificada por el Request-URI. Si el Request-URI se refiere a un proceso de producción de datos, son los datos producidos los que se devolverán como entidad en la respuesta y no el texto fuente del proceso. Cabe señalar que todas las peticiones que usan el método GET, deberán recuperar únicamente datos.

* **OPTIONS** : El método OPTIONS representa una solicitud de información acerca de las opciones de comunicación disponibles en el canal de solicitud/respuesta identificada por el Request-URI. En otras palabras, éste método es el que utilizamos para describir las opciones de comunicación existentes de un recurso destino.

* **HEAD** : El método HEAD es muy similar al GET (funcionalmente hablando), a excepción de que el servidor responde con líneas y headers, pero no con el body de la respuesta.

* **PUT** : El método PUT es usado para solicitar que el servidor almacene el cuerpo de la entidad en una ubicación específica dada por el URL.

* **POST** : El método POST es usado cuando se requiere enviar información al servidor como, por ejemplo, un archivo de actualización, información de formulario, etc. En otras palabras, éste método se usa cuando se necesita enviar una entidad para algún recurso determinado. La diferencia entre PUT y POST es que PUT es idempotente, mientras que si realizamos repetidas idénticas peticiones con el método POST, podría haber efectos adicionales como pasar una orden varias ocasiones.

* **DELETE** : Este método es utilizado para solicitar al servidor que elimine un archivo en una ubicación específica dada por la URL. En otras palabras más simples, este método elimina un recurso determinado.

* **CONNECT** : Este método por su parte es usado por el cliente para establecer una conexión de red con un servidor web mediante HTTP misma que se establece en forma de un túnel.

* **TRACE** : Éste método se utiliza para realizar pruebas de eco (de retornos) de mensajes en el camino que existe hacia un recurso determinado. Es un método muy utilizado para la depuración y también para el desarrollo.

![Listado peticiones](\Semana2-HTTP\HTTP.jpg)

## Codigos de estado :1234: :

Los códigos de estado HTTP describen de forma abreviada la respuesta HTTP. Estos códigos están especificados por el  RFC2616 (https://tools.ietf.org/html/rfc2616.)

El primer dígito del código de estado especifica uno de los 5 tipos de respuesta, el mínimo para que un cliente pueda trabajar con HTTP es que reconozca estas 5 clases. La Internet Assigned Numbers Authority (IANA) mantiene el registro oficial de códigos de estado HTTP.

* **1xx Respuestas informativas**  : Cuando se envía un código de estado HTTP 1xx, el servidor le notifica al cliente que la petición actual aún continúa. Esta clase reúne y proporciona información sobre el procesamiento y envío de una solicitud.

* **2xx Peticiones correctas** : Cuando se reciben este tipo de respuestas quiere decir que la solicitud del cliente fue recibida, comprendida y aceptada. Es muy frecuente que los códigos 2xx sean envíados desde el servidor junto con los datos de la página web deseada. Por lo general, el usuario solo percibe la web solicitada.

* **3xx Redirecciones** : Aquellos códigos que comienzan con 3 indican que la solicitud ha sido recibida por el servidor. Sin embargo, para asegurar un procesamiento exitoso es necesario que el cliente tome una acción adicional. Este tipo de códigos aparecen principalmente cuando hay redirecciones.

* **4xx Errores del cliente** : Esto quiere decir que el servidor ha recibido la solicitud, pero esta no se puede llevar a cabo. Una de las principales causas de este tipo de respuestas son las solicitudes defectuosas.  Los usuarios de Internet son informados de este error por medio de una página HTML generada automáticamente.

* **5xx Errores del servido** :  Este tipo de respuestas indican que la solicitud correspondiente está temporalmente deshabilitada o es imposible de llevar a cabo. De nuevo, se generará automáticamente una página en formato HTML.

Algunos codigos de estado mas importantes

CODIGO | SIGNIFICADO
-------- | ----------
100 Continue | El servidor ha recibido los headers del request y el cliente debería proceder a enviar el cuerpo de la respuesta.
200 OK | El request es correcto. Esta es la respuesta estándar para respuestas correctas.
301 Moved Permanently | La página solicitada se ha movido permanentemente a una nueva URI.
302 Found | La página solicitada se ha movido temporalmente a una nueva URI.
403 Forbidden | El request fue válido pero el servidor se niega a responder.
404 Not Found | Esto sucede cuando la dirección ya no existe o los contenidos han sido trasladados sin especificar la nueva dirección. Aquellos enlaces que dirigen a páginas inexistentes suelen conocerse como “enlaces muertos”.
500 Internal Server Error | Error genérico, cuando se ha dado una condición no esperada y no se puede concretar el mensaje.
503 Service Unavailable | El servidor está actualmente no disponible, ya sea por mantenimiento o por sobrecarga.

Referencias :

https://www.ionos.es/digitalguide/hosting/cuestiones-tecnicas/una-mirada-a-los-codigos-de-estado-http-mas-comunes/
https://yosoy.dev/peticiones-http-get-post-put-delete-etc/
https://diego.com.es/codigos-de-estado-http

