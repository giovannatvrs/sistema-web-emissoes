# Sistema Web de Emissões
## Link
Link do Projeto Live: https://sistema-web-emissoes-1.onrender.com (Deploy no render)

## Descrição do Projeto
Uma plataforma para gestão e análise de ofertas da planilha "Primário 2025". O sistema permite o gerenciamento completo (CRUD parcial) das emissões, oferecendo visualizações analíticas através de um dashboard interativo.

## Funcionalidades
- Página inicial:
  - Tabela que apresenta a data, tipo, emissor, valor, link e um botão de editar para cada oferta da planilha "Primário 2025".
  - Ao clicar no botão "Editar", é exibido um modal onde é possível fazer alterações na emissão escolhida.
  - Barra lateral que contém um link para a página de Dashboard e campo de filtros para a tabela
  - Paginação
  - Ordenação de ofertas por coluna de forma ascendente ou descente ao clicar no cabeçalho da tabela. Também é possível voltar a ordenação inicial com o botão de resetar ordenação.

- Dashboard:
  - Exibição de dados referentes a planilha, como o total de todas as emissões, quantidade de emissões, média do valores, e principal tipo de ativo.
  -  Análises com gráficos: Gráfico de pizza para mostrar os ativos mais utilizados, gráfico de linha para mostrar a quantidade de operações por mês e gráfico de barras para mostrar o total em cada mês.
  -  Ranking: Na parte inferior da página, há duas tabelas com os maiores emissores por valor (R$) e por quantidade de operações.

## Tecnologias e Ferramentas
Esse projeto foi desenvolvido com FastAPI no back-end e Angular no frontend. Foi utilizado a biblioteca Angular Material para os botões de paginação da página devido ao fato de ter muitas emissões. Dessa forma, as informações são divididas em paǵinas e não ocorre sobrecarga de dados de uma vez. Para a exibição de gráficos, foi utilizado Google Charts, uma ferramenta de visualização de dados baseada na web que usa HTML5 e SVG para criar gráficos interativos para sites e aplicativos. Entre as bibliotecas utilizadas no back-end, destaca-se o Pydantic pela validação de dados, o SQLAlchemy para uma comunicação robusta com o banco de dados SQLite e o pandas para a leitura de arquivos e análises estatísticas.

## Decisões
Eu escolhi o fastAPI pela sua performace, garantia de validação de dados e facilidade de implemetação de análises estatísticas, além de mostrar meus conehcimentos em Python. O projeto foi dividido em duas pastas backend e frontend por ser uma aplicação menor comparada com outras e pela facilidade maior de comunicação. O backend foi divido em pastas menores de acordo com a resposabilidade delas: data para o banco de dados e a planilha utilizada, script para o script de importação e test para os testes automatizados. O frontend possui duas pastas maiores enviroments (para o ambiente de produção e desenvolvimento) e src, que contém o projeto, divido em pastas menores também com relação as suas funções: páginas, componentes, serviços e modelos. Eu escolhi o Angular por ser possível reutilizar os componentes e por ser mais fácil de realizar alterações em apenas uma parte do site. A longo prazo, isso é uma característica positivas para a implementação de novas funcionalidades.

## Rodar localmente
git clone https://github.com/giovannatvrs/sistema-web-emissoes.git

No PyCharm ou outra IDE
cd backend  

ativar ambiente virtual

pip install -r requirements.txt  

python -m app.script.import_file  

uvicorn app.main:app --reload  

No vscode, por exemplo:

cd frontend  

npm install  

npx ng serve  


# Melhorias Futuras
- Implementação de sistema de autenticação e login para acessar dados.
- Possibilidade de inserir as próprias planilhas de emissões.
- Barra de busca global.
- Mais gráficos no dashboard e possibilidade de ver dados de outros anos
- Tornar a aplicação mais responsiva

## Página Inicial
<img width="1893" height="930" alt="image" src="https://github.com/user-attachments/assets/d4a5cb00-8b52-42d0-bdc5-58d9f6f39993" />

<img width="1893" height="930" alt="image" src="https://github.com/user-attachments/assets/12d06477-7136-48c0-bc62-b3d3fe5736ea" />

<img width="1893" height="930" alt="image" src="https://github.com/user-attachments/assets/5ff45456-79c5-4ce8-9aa2-14cf34b51492" />


## Dashboard
<img width="1893" height="930" alt="image" src="https://github.com/user-attachments/assets/c4e5a123-b112-47b7-ae16-4bcc5b87cb67" />





