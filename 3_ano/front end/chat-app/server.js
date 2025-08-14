const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8081 });
wss.on('connection', (ws) => {
    console.log('Novo cliente conectado');

    ws.on('message', (message) => {
        console.log('Mensagem recebida:', message);
        // Envie a mensagem para todos os clientes conectados
        wss.clients.forEach((client) => {
            if (client.readyState === WebSocket.OPEN) {
                client.send(message);
            }
        });
    });

    ws.on('close', () => {
        console.log('Cliente desconectado');
    });
    ws.onopen = () => {
        console.log('Conexão WebSocket estabelecida');
    };
    
    ws.onerror = (error) => {
        console.error('Erro no WebSocket:', error);
    };
    
    ws.onclose = () => {
        console.log('Conexão WebSocket fechada');
    };
    
});

console.log('Servidor WebSocket rodando na porta 8081');
