--show databases;
--database aula;

use aula;
CREATE TABLE produtos (
id SERIAL PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
categoria VARCHAR(50) NOT NULL,
preco DECIMAL(10, 2) NOT NULL,
estoque INT DEFAULT 0,
ativo BOOLEAN DEFAULT TRUE,
data_cadastro DATE DEFAULT CURRENT_DATE
);


INSERT INTO produtos (id, nome, categoria, preco, estoque, ativo, data_cadastro)
VALUES (1,'Teclado Mecânico RGB', 'Periféricos', 289.90, 45, TRUE, '2026-01-15');

INSERT INTO produtos (id, nome, categoria, preco, estoque) VALUES
(2,'Monitor 27" 144Hz', 'Monitores', 1450.00, 15),
(3,'Cadeira Ergonômica', 'Móveis', 890.00, 12),
(4,'Fone Bluetooth Over-Ear', 'Áudio', 350.00, 0),
(5,'Webcam Full HD 1080p', 'Periféricos', 210.00, 25),
(6,'Microfone Condensador USB', 'Áudio', 310.00, 18),
(7,'Cabo HDMI 2.1 2m', 'Cabos', 45.00, 150);

SELECT * FROM PRODUTOS;

UPDATE produtos SET preco = 269.90, estoque = 40 WHERE id = 1;
UPDATE produtos SET preco = ROUND(preco * 1.10, 2) WHERE categoria = 'Periféricos' AND ativo = TRUE;
UPDATE produtos SET ativo = FALSE WHERE estoque = 0;
SELECT * FROM PRODUTOS;

DELETE FROM produtos WHERE ativo = FALSE AND estoque = 0;
SELECT * FROM PRODUTOS;

SELECT nome AS 'Produto', preco AS 'Preço Cheio', estoque as 'Quantidade',
round((preco * estoque), 2) AS 'Total Estoque',
ROUND(preco * 0.85, 2) AS 'Preço Pix (c/desc.)'
FROM produtos;

SELECT id, nome, categoria, preco FROM produtos
WHERE categoria in ('Áudio', 'Monitores')
AND preco >= 300.00 AND ativo;

SELECT nome, categoria, 'preço entre 100 e 450' as Condicao FROM produtos WHERE preco BETWEEN 100.00 AND 450.00
union all
SELECT nome, categoria, 'categoria Áudio ou Móveis' as Condicao FROM produtos WHERE categoria IN ('Áudio', 'Móveis')
union all
SELECT nome, categoria, 'nome com "HD"' as Condicao FROM produtos WHERE nome LIKE '%HD%'
union all
SELECT nome, categoria, 'estoque zerado ou nulo' as Condicao FROM produtos WHERE estoque IS NULL OR estoque = 0;


SELECT id, nome, preco FROM produtos
WHERE ativo = TRUE
ORDER BY preco DESC, id ASC
LIMIT 3 offset 2;