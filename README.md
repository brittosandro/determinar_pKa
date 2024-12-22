# determina_pKa

Esse repositório considera as etapas que são necessárias para realizar um projeto de 
determinação de pKa's em um conjunto de ácidos em solvetes não aquosos utilizando
os recursos de química computacional.
O repositório será considerado como uma agenda das etapas. Tanto para que se possa lembrar 
delas ao longo do processo como para documentar as dificuldades encontradas e as 
soluções propostas.

## Etapa 1 
 - Gerar (produzir) as geometrias dos ácidos no formato *.xyz.
   
  **Solução** 
   - Utilizar o CAS de cada ácido contido no artigo 'Strengths of Acids in Acetonitrile' para produzir as geometrias.
      - [x] Criar um arquivo .txt com os dados do artigo 'Strengths of Acids in Acetonitrile' cujo os atributos são: nome da molécula (Name), tipo do ácido(Type), simbolo(CAS), fórmula molecular(Formula) e valor de pKa (pKa).\
            - O arquivo criado é o dados_acidos.txt.            
      - [x] Criar um script python com a biblioteca pubchem do Python e buscar as geometrias contidas no banco de dados.\
            - O script é o gera_geometrias.py.
       
   - Problema encontrado:
     - A biblioteca pubchem **não** apresenta todos os CAS dos ácidos contidos no arquivo de ácidos do artigo 'Strengths of Acids in Acetonitrile'. Dentre as 231 estruturas presentes, 102 não foram encontradas pelo pubchem.
       
   - Foi necessário recorrer a biblioteca **scifinder** afim de obter as geometrias não encontradas no script pelo pubchem.
     
       - Essa tarefa é terrível, pois é uma tarefa manual (só sei fazer essa assim :( ). Acrescido o fato de que as estruturas mostradas no scifinder escondem os hidrogênios e portanto
         será necessário realizar outras tarefas adicionais como: acrescentar hidrogênios por meio da abertura do arquivo no avogadro, esta geometria não será otimizada então será necessário
         otimizar a geometria com o xtb. Assim eu terei o conjunto de todas as etapas possíveis. As subtarefas são:
         
         - [x] Buscar as geometrias dos ácidos no scifinder.
               É necessário ter acesso a biblioteca privada do scifinder. Os CAS, ou moléculas encontradas no scifinder foram adicionadas em arquivos
               de acordo com o tipo de ácido especificado.
                              
         - [x] Acrescentar os hidrogênios faltantes.
               Os hidrogênios foram adicionados utilizando o avogadro.
                
         - [x] Otimizar as geometrias com xtb.

  Uma vez que, temos o arquivo dados_acidos.txt o script gerando_geometrias.py e os diretórios CH_scifinder, NH_scifinder, SH_scifinder, OH_scifinder e HHal_scifinder em que estão as geometrias .xyz não encontradas
  no pubchempy, concluimos a **Etapa 1**.
  
## Etapa 2
- Executar todos os arquivos *.xyz com os respectivos ácidos de interesse.
- Nessa atapa já temos os diretórios com os respectivos ácidos de interesse. Por exemplo no diretório CH teremos todas as geometrias *.xyz dos ácidos do tipo CH. Portanto será nesse diretório que iremos executar
o script faz_tudo_modif.sh. É esse script que executa os cálculos de interesse.
- O script faz_tudo_modif.sh tem por objetivo:
  1) Criar inputs do ORCA com o funcional, modelo de solvente e tipo de solvente de interesse.
  2) Realizar os cálculos do ORCA.
  3) Realizar os cálculos xtb com o tipo de solvente de interesse.
  4) Fazer a proponação e desprotonação das estruturas.
- Uma vez que os cálculos forem concluidos, serão criados vários diretórios com o CAS das várias moléculas e dentro de cada um destes diretórios teremos dois novos diretórios: ACIDcalc e BASEcalc. Nestes estão
contidos os output dos cálculos, com informações necessárias para o andamento do projeto.
- O script verifica_calcs.py foi executado para inspecionar todos os diretórios e verificar se todos os cálculos foram de fato concluidos com a terminação padrão do ORCA (****ORCA TERMINATED NORMALLY****).
Como todos os cálculos foram concluidos então podemos passar para a próxima etapa.

## Etapa 3
 - Essa etapa é a de extração de dados. Agora deveremos executar o script pega_dados.py e esse script irá extrair todos os dados de interesse e escreve-los em um arquivos denominado de
fitting_data.csv. Todos os parâmetros iniciais para realizar a proxima etapa que é a de análise de dados serão armazenados nesse arquivo.; 
  
               Essa etapa foi realizada conjuntamente com os outros cálculos.
         
