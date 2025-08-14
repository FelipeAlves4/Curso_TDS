const { ApolloServer, gql } = require('apollo-server');

// Dados de exemplo
const clientes = [
    { id: '1', nome: 'Alice', email: 'alice@example.com', telefone: '123456789' },
    { id: '2', nome: 'Bob', email: 'bob@example.com', telefone: '987654321' },
];

const produtos = [
    { id: '1', nome: 'Notebook', preco: 2000, estoque: 5 },
    { id: '2', nome: 'Mouse', preco: 50, estoque: 10 },
];

// Definição do schema
const typeDefs = gql`
    type Cliente {
        id: ID!
        nome: String!
        email: String!
        telefone: String
    }

    type Produto {
        id: ID!
        nome: String!
        preco: Float!
        estoque: Int!
    }

    type Query {
        cliente(id: ID!): Cliente
        produtos(estoqueMin: Int): [Produto]
    }
`;

// Resolvers para consultas
const resolvers = {
    Query: {
        cliente: (_, { id }) => clientes.find(cliente => cliente.id === id),
        produtos: (_, { estoqueMin = 0 }) => produtos.filter(produto => produto.estoque >= estoqueMin),
    },
};

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({ url }) => {
    console.log(`Servidor rodando em ${url}`);
});

