use analise_vendas;
SELECT * FROM PRODUTOS;

-- Exercício 01
Select v.id_venda as 'Pedido', v.data_venda as 'Data', c.nome as 'Nome Cliente'
from vendas as v inner join clientes as c
on v.id_cliente = c.id_cliente
order by v.data_venda, c.nome;

-- Exercício 02
Select c.id_cliente as 'ID', c.nome as 'Nome', c.cidade + c.estado as 'Cidade/UF'
from clientes as c left join vendas as v 
on c.id_cliente = v.id_cliente
where v.id_cliente = NULL
order by c.estado, c.cidade, c.nome;

-- Exercício 03
Select v.id_venda as 'Pedido', c.cidade + c.estado as 'Cidade/UF', p.nome_produto as 'Nome Produto', v.quantidade as 'Qtd. Adquirida',
round(p.preco_unitario * (1 - (v.desconto_percentual / 100)), 2) as 'Preço Venda'
from (clientes as c inner join vendas as v on c.id_cliente = v.id_cliente)
inner join produtos as p on v.id_produto = p.id_produto
order by v.id_venda asc;

-- Exercício 04
Select v.id_venda as 'Pedido', v.data_venda as 'Data', sum(v.quantidade * round(p.preco_unitario * (1 - (v.desconto_percentual / 100)), 2)) as 'Valor Total'
from vendas as v inner join produtos as p on v.id_produto = p.id_produto
group by v.id_venda, v.data_venda
order by sum(v.quantidade * round(p.preco_unitario * (1 - (v.desconto_percentual / 100)), 2)) desc, v.id_venda desc;

-- Exercício 05
With media as (
    Select avg(preco_unitario) as preco_medio from produtos where categoria = 'Periféricos'
)
SELECT nome_produto AS 'Produto', preco_unitario AS 'Preço Unitário'
FROM produtos cross join media where preco_unitario >= (preco_medio)
order by preco_unitario, nome_produto;

-- Exercício 06
Select id_produto as 'ID', nome_produto as 'Produto', preco_unitario AS 'Preço Unitário', categoria as 'Categoria'
from produtos
where not exists (select 1 from vendas where produtos.id_produto = vendas.id_produto)
order by id_produto;

-- Exercício 07
Select id_cliente as 'ID', nome as 'Nome'
from clientes  
where id_cliente in (
    select distinct v.id_cliente
    from vendas as v inner join produtos as p
    on v.id_produto = p.id_produto
    where p.categoria = 'Monitores'
)
order by id_cliente;

-- Exercício 08
Select p.categoria, sum(v.quantidade * p.preco_unitario) as 'Receita Bruta',
sum(v.quantidade * round(p.preco_unitario * (1 - (v.desconto_percentual / 100)), 2)) as 'Receita Líquida'
from vendas as v inner join produtos as p
on v.id_produto = p.id_produto
group by p.categoria
order by sum(v.quantidade * p.preco_unitario) desc, p.categoria;

-- Exercício 09
Select c.id_cliente as 'ID', c.nome as 'Nome', count(v.id_venda) as 'Qtd. Pedidos'
from clientes as c inner join vendas as v 
on c.id_cliente = v.id_cliente
group by c.id_cliente, c.nome
having count(v.id_venda) >= 2
order by c.nome, c.id_cliente;