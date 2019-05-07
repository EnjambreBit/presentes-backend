import sys
import io
import os

ROJO = '\x1b[31m'
AZUL = '\x1b[34m'
RESTAURAR = '\x1b[0m'
# print('\x1b[31mfoo\x1b[0m')

if len(sys.argv) != 4:
    print(ROJO + "Numero incorrecto de argumentos." + RESTAURAR)
    print("Uso:")
    print("")
    print("  python generar.py aplicacion modulo modulo_plural")
    print("")
    print("Por ejemplo:")
    print("")
    print(AZUL + "  python generar.py electronica Perfil perfiles" + RESTAURAR)
    print("")
    sys.exit(1)

aplicacion = sys.argv[1]
modelo = sys.argv[2]
modelo_plural = sys.argv[3]

print("Parámetros ingresados:")
print("")
print(f" Modelo: '{modelo}'")
print(f" Archivos y plurales: '{modelo_plural}'")
print("")

archivos = [
    "templates/admin.py"
]


def obtener_ruta_absoluta(origen):
    este_directorio = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(este_directorio, origen)


def sustituir_nombres(linea):
    linea = linea.replace('Modelo', modelo)
    linea = linea.replace('modelo_plural', modelo_plural)
    linea = linea.replace('aplicacion', aplicacion)
    linea = linea.replace('modelo', modelo_plural)
    return linea


def aplicar_template(origen, destino):
    print("- Creando el archivo {}".format(destino))
    archivo = io.open(destino, 'w')

    for line in io.open(obtener_ruta_absoluta(origen), 'r'):
        line = sustituir_nombres(line)
        archivo.write(line)

    archivo.close()


def editar_archivo_urls():
    ruta = "backend/urls.py"
    archivo = io.open(ruta, 'rt')
    contenido = archivo.read()
    archivo.close()

    codigo = [
        'from aplicacion.views.modelo import ModeloViewSet',
        'router.register("modelo_plural", ModeloViewSet)'
        ''
        '\n## placeholder para django-api-helper\n'
        ''
    ]

    nuevo_contenido = "\n".join([sustituir_nombres(linea) for linea in codigo])
    contenido = contenido.replace("## placeholder para django-api-helper", nuevo_contenido)

    archivo = io.open(ruta, 'w')
    archivo.write(contenido)
    archivo.close()

def editar_archivo_admin():
    ruta = sustituir_nombres("aplicacion/admin.py")
    archivo = io.open(ruta, 'rt')
    contenido = archivo.read()
    archivo.close()

    codigo = [
        'from aplicacion.admin_classes.modelo import Modelo, ModeloAdmin',
        'admin.site.register(Modelo, ModeloAdmin)'
        ''
        '\n## placeholder para django-api-helper\n'
        ''
    ]

    nuevo_contenido = "\n".join([sustituir_nombres(linea) for linea in codigo])
    contenido = contenido.replace("## placeholder para django-api-helper", nuevo_contenido)

    archivo = io.open(ruta, 'w')
    archivo.write(contenido)
    archivo.close()

print("")
aplicar_template("templates/admin.py", f"{aplicacion}/admin_classes/{modelo_plural}.py")
aplicar_template("templates/model.py", "%s/models/%s.py" %
                 (aplicacion, modelo_plural))
aplicar_template("templates/serializador.py",
                 "%s/serializers/%s.py" % (aplicacion, modelo_plural))
aplicar_template("templates/view.py", "%s/views/%s.py" %
                 (aplicacion, modelo_plural))
aplicar_template("templates/tests.py", "%s/tests/tests_api_%s.py" %
                 (aplicacion, modelo_plural))

print("")
print("Se crearon todos los archivos, y se modificaron los archivos:")
print("urls.py y admin.py")

editar_archivo_urls()
editar_archivo_admin()

print("")

print("Recodá ejecutar los comandos: make crear_migraciones y make migrar")
print("")
