const express = require('express');
const app = express();
const port = 3000;

// Définir les routes
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/home.html');
});

app.get('/articles', (req, res) => {
    res.sendFile(__dirname + '/base.html');
});

app.get('/about', (req, res) => {
    res.sendFile(__dirname + '/admin.html');
});

app.get('/contact', (req, res) => {
    res.sendFile(__dirname + '/contact.html');
});

// Démarrer le serveur
app.listen(port, () => {
    console.log(`Serveur à l'écoute sur http://localhost:${port}`);
});
