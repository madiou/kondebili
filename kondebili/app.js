const express = require('express');
const app = express();
const port = 3000;

// Définir les routes
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.get('/articles', (req, res) => {
    res.sendFile(__dirname + '/articles.html');
});

app.get('/about', (req, res) => {
    res.sendFile(__dirname + '/about.html');
});

app.get('/contact', (req, res) => {
    res.sendFile(__dirname + '/contact.html');
});

// Démarrer le serveur
app.listen(port, () => {
    console.log(`Serveur à l'écoute sur http://localhost:${port}`);
});
