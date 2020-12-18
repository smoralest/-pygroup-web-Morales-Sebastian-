from flask import Blueprint

# TAREA VISTAS + CONSULTA render_template
name = Blueprint('name', __name__, url_prefix='/name')
@name.route('/<string:name>', methods=['GET'])
def get_name(name):
    if name!="pygroup":
        return "Felicitaciones! Trabajo exitoso {}".format(name), 200
    return "ERROR! No se puede usar el nombre pygroup", 400

    

"""flask.render_template( nombre_plantilla_o_lista , ** contexto ) 
Renderiza una plantilla de la carpeta de plantillas con el contexto dado.

Parámetros:
    template_name_or_list - el nombre de la plantilla que se va a representar, o un iterable con nombres
    de plantilla, se renderizará la primera existente.
    contexto : las variables que deberían estar disponibles en el contexto de la plantilla.

Funcion: Flask a traves de render_template() te permite usar plantillas para el contenido dinámico de páginas web.
Esto hará que gestionar HTML sea mucho más fácil escribiendo su código HTML en archivos .html, además de utilizar la 
lógica en su código HTML. Usará estos archivos HTML, (plantillas), para crear todas las páginas de su aplicación,
de igual forma que la página principal donde mostrará las entradas actuales del blog, la página de la entrada 
del blog, la página donde el usuario puede añadir una nueva entrada, etcétera.
"""
