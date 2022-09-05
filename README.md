# Api de ceps
O projeto API CEP foi desenvolvido como primeiro projeto em grupo em Django entre os alunos do BuserTech! 

A hospedagem está em https://busertecocep.herokuapp.com/ 

O projeto contém:
1) Um banco de dados próprio com mais de 1 milhão de CEPs.
2) Esse projeto roda com o postgres no Docker.
3) Temos test desenvolvido em pytest-django (ainda melhorando...)

# CEP Clara

O CEP Clara é um fork do projeto em grupo e a extensão do projeto com mais features. 

1) Existe uma atualização do banco de dados com API de terceiro (https://viacep.com.br/), quando a pesquisa não é encontrado nessa base. 



## Possíveis problemas do banco de dados. 
Por algum motivo, o ID sequence descasou e acaba tendo problemas com a criação de novos CEPs por API. Então, caso haja um estouro de problema do tipo:

 `django.db.utils.IntegrityError: duplicate key value violates unique constraint "buscador_cep_cidade_pkey" DETAIL:  Key (id)=(1) already exists.`

Ou qualquer outro número de ID apontado. A ideia é corrigir o set do setval. 

Investigue qual o id máximo que existe na tabela de cep com o seguinte comando nesse banco no dbeaver. 
`select max(id) from buscador_cep_cep`

Agora ajuste para que o ID dos novos registros por API não conflite entre si, com o seguinte comando:

`select setval('buscador_cep_cidade_id_seq', {Insira aqui o próximo número depois do max(id)}, false)`# CEP_API
