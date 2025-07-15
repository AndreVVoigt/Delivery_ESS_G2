class Constants:
    PEDIDOS_FILE = "data/pedidos_realizados.json"
    CARDAPIO_FILE = "data/dados.json"
    HISTORY_FILE = "data/order_history.json"
    SUGESTOES_FILE = "data/regras_sugestao.json"

    PEDIDOS_REALIZADOS_DEFAULT = {
        "mesas": ["mesa_1", "mesa_2", "mesa_3", "mesa_4", "mesa_5"],
        "mesa_1": {"pedidos": [], "total": 0},
        "mesa_2": {"pedidos": [], "total": 0},
        "mesa_3": {"pedidos": [], "total": 0},
        "mesa_4": {"pedidos": [], "total": 0},
        "mesa_5": {"pedidos": [], "total": 0}
    }

    CARDAPIO_DEFAULT = {
    "categorias": [
        "BEBIDAS",
        "LANCHES",
        "PIZZAS",
        "SOBREMESAS",
        "OUTROS"
    ],
    "produtos": [
        {
        "ID": "B001",
        "NOME": "Coca-Cola Lata 350ml",
        "DESCRICAO": "Refrigerante de cola, gelado.",
        "DESCONTO": 0,
        "PRECO": 5.5,
        "CATEGORIA": "BEBIDAS"
        },
        {
        "ID": "B002",
        "NOME": "Suco de Laranja Natural 500ml",
        "DESCRICAO": "Suco feito com laranjas frescas, sem adição de açúcar.",
        "DESCONTO": 0,
        "PRECO": 8.0,
        "CATEGORIA": "BEBIDAS"
        },
        {
        "ID": "B003",
        "NOME": "Água Mineral com Gás 500ml",
        "DESCRICAO": "Água mineral gaseificada naturalmente.",
        "DESCONTO": 0,
        "PRECO": 4.0,
        "CATEGORIA": "BEBIDAS"
        },
        {
        "ID": "B004",
        "NOME": "Cerveja Heineken Long Neck",
        "DESCRICAO": "Cerveja Premium Lager, 330ml.",
        "DESCONTO": 10,
        "PRECO": 9.0,
        "CATEGORIA": "BEBIDAS"
        },
        {
        "ID": "L001",
        "NOME": "X-Burger Clássico",
        "DESCRICAO": "Pão, hambúrguer de 150g, queijo mussarela, alface, tomate e maionese da casa.",
        "DESCONTO": 0,
        "PRECO": 22.0,
        "CATEGORIA": "LANCHES"
        },
        {
        "ID": "L002",
        "NOME": "X-Salada Bacon",
        "DESCRICAO": "Pão, hambúrguer, queijo, bacon crocante, alface, tomate e molho especial.",
        "DESCONTO": 15,
        "PRECO": 28.0,
        "CATEGORIA": "LANCHES"
        },
        {
        "ID": "L003",
        "NOME": "Misto Quente",
        "DESCRICAO": "Pão de forma, duas fatias de queijo e duas fatias de presunto.",
        "DESCONTO": 0,
        "PRECO": 12.0,
        "CATEGORIA": "LANCHES"
        },
        {
        "ID": "L004",
        "NOME": "Sanduíche de Frango Grelhado",
        "DESCRICAO": "Pão baguete, filé de frango grelhado, queijo, alface e tomate.",
        "DESCONTO": 0,
        "PRECO": 25.0,
        "CATEGORIA": "LANCHES"
        },
        {
        "ID": "P001",
        "NOME": "Pizza Margherita",
        "DESCRICAO": "Massa tradicional, molho de tomate, mussarela e manjericão fresco. Tamanho grande.",
        "DESCONTO": 0,
        "PRECO": 45.0,
        "CATEGORIA": "PIZZAS"
        },
        {
        "ID": "P002",
        "NOME": "Pizza Calabresa",
        "DESCRICAO": "Massa tradicional, molho de tomate, mussarela, calabresa fatiada e cebola. Tamanho grande.",
        "DESCONTO": 0,
        "PRECO": 50.0,
        "CATEGORIA": "PIZZAS"
        },
        {
        "ID": "P003",
        "NOME": "Pizza Quatro Queijos",
        "DESCRICAO": "Massa tradicional, molho de tomate, mussarela, provolone, parmesão e gorgonzola. Tamanho grande.",
        "DESCONTO": 0,
        "PRECO": 55.0,
        "CATEGORIA": "PIZZAS"
        },
        {
        "ID": "P004",
        "NOME": "Pizza Portuguesa",
        "DESCRICAO": "Massa tradicional, molho, mussarela, presunto, ovo, cebola, azeitona e pimentão. Tamanho grande.",
        "DESCONTO": 20,
        "PRECO": 58.0,
        "CATEGORIA": "PIZZAS"
        },
        {
        "ID": "S001",
        "NOME": "Pudim de Leite",
        "DESCRICAO": "Fatia generosa de pudim de leite condensado com calda de caramelo.",
        "DESCONTO": 0,
        "PRECO": 9.5,
        "CATEGORIA": "SOBREMESAS"
        },
        {
        "ID": "S002",
        "NOME": "Mousse de Chocolate",
        "DESCRICAO": "Mousse de chocolate meio amargo, cremoso e aerado.",
        "DESCONTO": 0,
        "PRECO": 12.0,
        "CATEGORIA": "SOBREMESAS"
        },
        {
        "ID": "S003",
        "NOME": "Torta Alemã (Fatia)",
        "DESCRICAO": "Fatia de torta com base de bolacha, creme holandês e cobertura de ganache.",
        "DESCONTO": 0,
        "PRECO": 15.0,
        "CATEGORIA": "SOBREMESAS"
        },
        {
        "ID": "S004",
        "NOME": "Açaí na Tigela 500ml",
        "DESCRICAO": "Açaí batido com banana. Acompanha granola e leite em pó.",
        "DESCONTO": 0,
        "PRECO": 20.0,
        "CATEGORIA": "SOBREMESAS"
        },
        {
        "ID": "O001",
        "NOME": "Porção de Batata Frita",
        "DESCRICAO": "Porção de 400g de batata frita sequinha. Acompanha maionese da casa.",
        "DESCONTO": 0,
        "PRECO": 25.0,
        "CATEGORIA": "OUTROS"
        },
        {
        "ID": "O002",
        "NOME": "Porção de Calabresa Acebolada",
        "DESCRICAO": "Porção de 400g de calabresa fatiada e frita com anéis de cebola.",
        "DESCONTO": 0,
        "PRECO": 30.0,
        "CATEGORIA": "OUTROS"
        },
        {
        "ID": "O003",
        "NOME": "Molho Extra (Maionese da casa)",
        "DESCRICAO": "Pote de 50g da nossa maionese especial.",
        "DESCONTO": 0,
        "PRECO": 3.0,
        "CATEGORIA": "OUTROS"
        },
        {
        "ID": "O004",
        "NOME": "Anéis de Cebola Empanados",
        "DESCRICAO": "Porção de 12 anéis de cebola empanados e fritos.",
        "DESCONTO": 0,
        "PRECO": 22.0,
        "CATEGORIA": "OUTROS"
        }
    ]
    }