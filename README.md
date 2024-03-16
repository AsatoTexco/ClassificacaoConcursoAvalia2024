# ClassificacaoConcursoAvalia2024
Este repositório visa oferecer uma solução prévia para a classificação de informações provenientes dos concursos promovidos pela AVALIA CONCURSOS. Ao utilizar técnicas sólidas de tratamento de dados, busquei proporcionar uma experiência aprimorada aos usuários, facilitando o acesso e a compreensão das informações contidas nos documentos fornecidos. [Avalia Concursos](https://avalia.org.br/concursos)

# Requirements
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF)

# Funcionamento
- Este repositório inclui dois arquivos fornecidos no edital:`nota_objetiva.pdf` e `nota_redacao.pdf`, contendo todas as informações referentes aos candidatos do concurso.

![imagem_representativa](https://iili.io/JWm9AtS.png)

- Ao executar o arquivo `main.py`, o programa analisa os dados contidos no `nota_redacao.pdf` e cria instâncias de dados em um dicionário, incluindo informações como nome, número de inscrição e a nota da redação.

![imagem_representativa](https://iili.io/JWbpd0J.png)

- Em seguida, o programa analisa o arquivo de notas da prova objetiva `nota_objetiva.pdf` e atualiza o dicionário com as informações previamente adicionadas, incluindo a pontuação da prova objetiva e a média final calculada no momento.
 
- Finalmente, o sistema gera o arquivo `output.txt` com a classificação, da maior nota para a menor, dos concursos para "PROFESSOR - ANOS INICIAIS DO ENSINO FUNDAMENTAL" e "PROFESSOR - EDUCAÇÃO INFANTIL".

![imagem_representativa](https://iili.io/JWm9GAQ.png)
