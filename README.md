# determina_pKa

Esse repositório considera as etapas que são necessárias para realizar um projeto de 
determinação de pKa's em um conjunto de ácidos em solvetes não aquosos utilizando
os recursos de química computacional.
O repositório será considerado como uma agenda das etapas. Tanto para que se possa lembrar 
delas ao longo do processo como para documentar as dificuldades encontradas e as 
soluções propostas.

## Etapa 1 
 - Gerar(produzir) as geometrias dos ácidos no formato *.xyz.
   
  **Solução** 
   - Utilizar o CAS de cada ácido contido no artigo (x) para produzir as geometrias.
      <li>- [x] </li> Criar um arquivo .txt com os dados do artigo (x) cujo os atributos são: nome da molécula (Name), tipo do ácido(Type), simbolo(CAS), fórmula molecular(Formula) e valor de pKa (pKa).\
            - O arquivo é o dados_acidos.txt.            
      - [x] Criar um script python com a biblioteca pubchem do Python e buscar as geometrias contidas no banco de dados.\
            - O script é o gera_geometrias.py.
       
   - Problema encontrado:
     - A biblioteca pubchem não apresenta todos os CAS dos ácidos contidos no arquivo de ácidos do artigo (X). Dentre as 231 estruturas presentes, 102 não foram encontradas pelo pubchem.
       
   - Foi necessário recorrer a biblioteca **scifinder** afim de obter as geometrias não encontradas no script pelo pubchem.
     
       - Essa tarefa é terrível, pois é uma tarefa manual (só sei fazer essa assim :( ). Acrescido o fato de que as estruturas mostradas no scifinder escondem os hidrogênios e portanto
         será necessário realizar outras tarefas adicionais: acrescentar hidrogênios por meio da abertura do arquivo no avogadro, esta geometria não será otimizada então será necessário
         otimizar a geometria com o xtb. Assim eu terei o conjunto de todas as etapas possíveis. As subtarefas são:
         
         - [ ] Buscar as geometrias dos ácidos no scifinder.
         - [ ] Acrescentar os hidrogênios faltantes.
         - [ ] Otimizar as geometrias com xtb.
         
