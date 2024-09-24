# determina_pKa

Esse repositório considera as etapas que são necessárias para realizar um projeto de 
determinação de pKa's em um conjunto de ácidos em solvetes que não são aquosos, utilizando
os recursos de química computacional.
O repositório será considerado como uma agenda das etapas. Tanto para que se possa lembrar 
das etapas ao longo do processo como para documentar as dificuldades encontradas e as 
soluções propostas.

## Etapa 1 
 - Gerar(produzir) as geometrias dos ácidos no formato *.xyz.
   
  **Solução** 
   - Utilizar o CAS de cada ácido contido no artigo (x) para produzir as geometrias.
      - [x] Criar um arquivo .txt com os dados do artigo (x) cujo os atributos são: nome da molécula (Name), tipo do ácido(Type), simbolo(CAS), fórmula molecular(Formula) e valor de pKa (pKa).
            - O arquivo é o dados_acidos.txt.            
      - [x] Criar um script python com a biblioteca pubchem do Python e buscar as geometrias contidas no banco de dados.
            - O script é o gera_geometrias.py.
       
   - Problema encontrado:
     - A biblioteca pubchem não apresenta todos os CAS dos ácidos contidos no arquido de ácidos do artigo (X).
       
   - Foi necessário recorrer a biblioteca scifinder afim de obter as geometrias não encontradas no script pelo pubchem.
      - 
