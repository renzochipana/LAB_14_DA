// Requerir el módulo de New Relic
require('newrelic');

// Importar el módulo express
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

// Middleware para parsear JSON
app.use(express.json());




// Datos
const albums = [
    {
        id: 1,
        title: "Álbum Ejemplo 1",
        released: 2020,
        price: 15,
        genre: "Rock"
    },
    {
        id: 2,
        title: "Álbum Ejemplo 2",
        released: 2021,
        price: 15,
        genre: "Rock"
    }
];

app.get('/', (req, res) => {
    res.send('¡Hola Mundo!');
  });
  
// Ruta para obtener todos los álbumes
app.get('/api/albums', (req, res) => {
    res.json(albums);
});

// Iniciar el servidor
app.listen(port, () => {
    console.log(`Servidor escuchando en http://localhost:${port}`);
});