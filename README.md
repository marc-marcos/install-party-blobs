# install-party-blobs

## Configuración 

- clonar el repo 
- `cd install-party-blobs/`
- `source venv/bin/activate`
- `python -m pip install -r requirements.txt`

## Uso 

### Crear la base de datos 

- `python database_utils.py`

### Encender la app de Flask

- `flask run`

### Encender la visualización

- `python painting_blobs.py`

Ahora ya se pueden hacer las requests siguientes a la IP donde esté alojada la app de flask.

- /create (método POST) en el cuerpo de la request: `{"username" : String, "os" : String}` **Para dejar el campo de username blanco hay que enviarlo como una string vacía "", siempre en cada request hay que enviar el campo de username aunque sea vacío**

### Atajos

- **L**: Activa y desactiva la leyenda de las distribuciones.

## Todo
- [X] Hacer que las bolas spawneen un poco más lejos de los margenes. 
- [ ] Que se pueda cambiar el tamaño de las bolas y de la fuente desde la misma visualización.
- [ ] Que se pueda desactivar los nombres que sean numeros y que los otros sigan saliendo.
- [X] Que se pueda activar y desactivar la leyenda de distribuciones.
