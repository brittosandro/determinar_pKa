# determina_pKa

Esse repositório considera as etapas que são necessárias para realizar um projeto de 
determinação de pKa's em um conjunto de ácidos em solvetes que não são aquosos, utilizando
os recursos de química computacional.
O repositório será considerado como uma agenda das etapas. Tanto para que se possa lembrar 
das etapas ao longo do processo como para documentar as dificuldades encontradas e as 
soluções propostas.

## Etapa 1 
 - Gerar(produzir) as geometrias dos ácidos no formato *.xyz.\
   
  **Solução** \
   - Utilizar o CAS de cada ácido contido no artigo (x) para produzir as geometrias. \
   - Como fazer?
     - Criar um script python com a biblioteca pubchem do Python e buscar as geometrias contidas no banco de dados.
   - Problemas encontrado:
     - A biblioteca pubchem não apresenta todos os CAS dos ácidos contidos no arquido de ácidos do artigo (X). 
