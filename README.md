## Como iniciar el proyecto en modo desarrollo

Para usar la aplicación en modo desarrollo primero se tiene que crear una base de datos llamada "presentes-db":

```
createdb presentes-db
```

Luego tienes que ejecutar en un terminal los comandos:

```
make iniciar
make migrar
make ejecutar
```

## Cómo crear modelos

Para crear modelos nuevos se puede ejecutar este comando, especificando el nombre de la aplicación,
módulo y módulo en plural. Por ejemplo:

```
pipenv run python django-api-helper/generar.py presentes Perfil "perfiles"
```
