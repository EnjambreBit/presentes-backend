VERSION=$(shell git describe --tags)
NOMBRE=presentes-backend

DB_NOMBRE_DEL_DUMP= ~/Dropbox/4cores/Backups/presentes/presentes_`date +'%Y%m%d_%Hhs%Mmin'`.dump
DB_DUMP_MAS_RECIENTE=`ls -Art ~/Dropbox/4cores/Backups/presentes/presentes_*.dump  | tail -n 1`

N=[0m
R=[00;31m
G=[01;32m
Y=[01;33m
B=[01;34m
L=[01;30m

comandos:
	@echo ""
	@echo "${B}Comandos disponibles para ${G}${NOMBRE}${N} (versión: ${VERSION})"
	@echo ""
	@echo "  ${Y}Para desarrolladores${N}"
	@echo ""
	@echo "    ${G}iniciar${N}                            Instala todas las dependencias."
	@echo "    ${G}crear_migraciones${N}                  Genera las migraciones."
	@echo "    ${G}migrar${N}                             Ejecuta las migraciones."
	@echo ""
	@echo "    ${G}test${N}                               Ejecuta los tests."
	@echo "    ${G}test_live${N}                          Ejecuta los tests de forma continua."
	@echo "    ${G}${N}                                   (en ambos casos, se puede usar un filtro)"
	@echo "    ${G}${N}                                   (por ejemplo: make test filtro="trabajos")"
	@echo ""
	@echo "    ${G}ejecutar${N}                           Ejecuta el servidor en modo desarrollo."
	@echo "    ${G}ejecutar_worker${N}                    Ejecuta el job queue."
	@echo "    ${G}shell${N}                              Ejecuta un intérprete de python."
	@echo "    ${G}version${N}                            Incrementa la versión."
	@echo "    ${G}cargar_datos${N}                       Carga el archivo .xls inicial."
	@echo "    ${G}deploy${N}                             Realiza un deploy sobre dokku."
	@echo ""
	@echo "    ${G}realizar_backup_desde_produccion${N}   Incrementa la versión."
	@echo "    ${G}cargar_ultimo_dump_localmente${N}      Carga el útimo backup."
	@echo ""
	@echo ""


iniciar:
	@pipenv install

crear_migraciones:
	@pipenv run python manage.py makemigrations

migrar:
	@pipenv run python manage.py migrate --noinput

clear:
	dropdb --if-exists presentes-test -e
	@clear;

test:
ifeq ($(filtro),)
	@echo "${G}Ejecutando tests ...${N}"
	pipenv run pytest
else
	pipenv run pytest -k $(filtro)
endif

test_live:
ifeq ($(filtro),)
	pipenv run ptw
else
	pipenv run ptw -- -k $(filtro)
endif

ejecutar:
	@pipenv run python manage.py runserver

shell:
	@pipenv run python manage.py shell -i ipython

version:
	@pipenv run bumpversion patch --verbose
	@git push
	@git push --tags

deploy:
	git remote add dokku dokku@enjambrelab.space:presentes-backend || true
	git checkout devel
	git push dokku devel:master

cargar_datos:
	@pipenv run python cargar_datos.py

ejecutar_worker:
	@pipenv run python manage.py rqworker default

monitor:
	@pipenv run python manage.py rqstats --interval=1

realizar_backup_desde_produccion:
	@echo "${G}Creando el archivo ${DB_NOMBRE_DEL_DUMP}${N}"
	@ssh dokku@enjambrelab.space postgres:export presentes-backend > ${DB_NOMBRE_DEL_DUMP}

cargar_ultimo_dump_localmente:
	@echo "${G}Se cargará el dump mas reciente: ${DB_DUMP_MAS_RECIENTE}${N}"
	dropdb --if-exists presentes-db -e; createdb presentes-sb
	pg_restore --no-acl --no-owner -d presentes-db ${DB_DUMP_MAS_RECIENTE}
