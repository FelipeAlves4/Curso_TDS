const http = require('http');
// Cria um servidor que responde com uma mensagem
const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Bem-vindo ao meu servidor Node.js!');
});
// Define a porta em que o servidor vai ouvir
const port = 3000;
server.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}/`);
});