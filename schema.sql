DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS beach;

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    nome TEXT NOT NULL,
    profile_pic_path TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS beach (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    pic_path TEXT NOT NULL
);

INSERT INTO users(username, password, nome, profile_pic_path) VALUES ('root', 'root', 'John Doe', 'static/images/profile_johndoe.jpg');

INSERT INTO beach(nome, descricao, pic_path) VALUES ('Praia de Porto de Galinhas', 'Conhecida internacionalmente por suas piscinas naturais formadas por recifes de corais, Porto de Galinhas é um paraíso tropical com águas cristalinas e areias douradas. É um destino imperdível para mergulho, snorkeling e relaxamento à beira-mar.', 'static/images/porto-de-galinhas.png');

INSERT INTO beach(nome, descricao, pic_path) VALUES ('Praia dos Carneiros', 'Rodeada por coqueiros e com um cenário de cartão postal, a Praia dos Carneiros oferece águas calmas e cristalinas ideais para nadar e fazer passeios de barco. A icônica Igreja de São Benedito à beira-mar adiciona um toque especial a essa praia deslumbrante.', 'static/images/carneiros.jpg');

INSERT INTO beach(nome, descricao, pic_path) VALUES ('Praia de Maracaípe', 'Popular entre os surfistas devido às suas ondas desafiadoras, Maracaípe também é famosa por ser um ponto de encontro das tartarugas marinhas. É uma ótima opção para quem busca um ambiente tranquilo e belas paisagens naturais.', 'static/images/Maracaípe-PE.jpg');

INSERT INTO beach(nome, descricao, pic_path) VALUES ('Praia de Calhetas', 'Uma pequena enseada com águas calmas e cristalinas cercadas por falésias verdes, Calhetas é um refúgio isolado para os amantes da natureza. A praia é ideal para relaxar, nadar e explorar a vida marinha.', 'static/images/praia-calhetas-pernambuco-3-740x.jpg');