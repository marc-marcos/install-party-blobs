# install-party-blobs

## Fotos

### Frontend per afegir instal·lacions

![Foto Frontend](/readme-images/ejfrontend.png)

### Visualització per al projector

![Visualització al Projector](/readme-images/balls.gif)

<hr>

## About it 

Install Party Blobs és un projecte per la Linux Install Party de l'associació de LinuxUPC. Tenim una web on els organitzadors des del seu mòbil comptabilitzaran el registre de quina distribució de Linux s'instal·la cada participant. Aquestes dades es veuran reflectides en el projector de l'aula en forma de pilotes simulant un salvapantalles com en la foto anterior.

Durant tot l'esdeveniment es podrà veure en temps real la participació dels alumnes en el visualitzador.

## Configuració

- clonar el repo 
- `cd install-party-blobs/`
- `python -m venv venv`
- `python -m pip install -r requirements.txt`
- `pip install flask_cors`

## Ús

### Crear la base de dades 

- `python database_utils.py`

### Encendre l'app de Flask

- `flask run`

### Encendre la visualizació

- `python painting_blobs.py`

Ara ja es poden fer les requests següents a la IP on està allotjada l'app de Flask.

- /create (métode POST) en el cos de la request: `{"username" : String, "os" : String}` **Per deixar el camp de username blanc s'ha d'enviar com una string buida"", sempre en cada request s'ha d'enviar el campo de username tot i que sigui buit. En cas de que el camp d'username sigui buit es generarà un identificador incremental.**
- / **Frontend pper fer les peticions des del mòbil**
- /raw **Per aconseguir les dades en format JSON**

Els sistemas operatius que detecta el backend son:
- Arch
- Ubuntu
- Fedora
- Linux Mint
- Manjaro
- Debian
- Tota la resta color default.

### Shortcut

- **L**: Activa y desactiva la llegenda de les distribucions.

## Todo
- [ ] Que el backend detecti Debian.

## Authors

- Frontend: [@paulsssp](https://github.com/paulsssp)
- Backend and hosting: [@marc-marcos](https://github.com/marc-marcos)