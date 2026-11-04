use aula;
SELECT * FROM PRODUTOS;

-- Exercício 01
INSERT INTO produtos (id, nome, categoria, preco, estoque, ativo, data_cadastro)
VALUES (8,'Mousepad Gamer Extra Grande', 'Acessórios', 89.90, 60, TRUE, now());
SELECT * FROM PRODUTOS where id = 8;

-- Exercício 02
UPDATE produtos SET preco = preco * 0.85 WHERE categoria = 'Áudio' and preco > 300;
SELECT * FROM PRODUTOS WHERE categoria = 'Áudio';

-- Exercício 03
DELETE FROM produtos WHERE ativo = FALSE AND categoria = 'Acessórios' and estoque = 0;
SELECT * FROM PRODUTOS;

-- Exercício 04
SELECT nome AS 'Produto', preco AS 'Preço Unitário', estoque as 'Qtd. Estoque'
FROM produtos where ativo
order by preco desc, nome asc;

-- Exercício 05
SELECT nome AS 'Produto', preco AS 'Preço Unitário', categoria as 'Categoria'
FROM produtos where (preco between 150 and 500) and not (categoria = 'Móveis')
order by categoria, nome;

-- Exercício 06
Select * from produtos where nome like '%Monitor%' or nome like '%USB%';

-- Exercício 07
Select count(nome) as 'Produtos Cadastrados', sum(estoque) as 'Itens em Estoque', round(avg(preco), 2) as 'Preço Médio'
from produtos;

-- Exercício 08
Select categoria, count(nome) as 'Produtos Ativos', max(preco) as 'Maior Preço'
from produtos where ativo
group by categoria;

-- Exercício 09
Select categoria, sum(estoque) as 'Itens em Estoque'
from produtos
group by categoria
having sum(estoque) > 50;

-- Exercício 10
Select id, nome, preco, round(preco / 10) as prestacao
from produtos where estoque > 0
order by preco, nome
limit 4;