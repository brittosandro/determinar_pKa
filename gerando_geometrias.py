import pubchempy as pcp
import os
import shutil


def cria_diretorio(tipo):
    '''
      Essa função recebe os dados do tipo de ácido: NH, OH, CH, etc.
      e cria um diretório se caso o diretório não exista na pasta corrente.
    '''
    if not os.path.exists(tipo):
        os.makedirs(tipo)

def gera_compostos(CAS):
    '''
    Essa função retorna um conjunto de compostos se caso esse composto exista
    na base de dados do pubchem.
    '''
    return pcp.get_compounds(CAS, 'name', record_type='3d')

def cria_arquivo_e_move(tipo, CAS, atomos):
    '''
    A função cria um arquivo com o nome da molécula e move esse arquivo
    para o diretório que corresponde ao ácido.
    '''
    with open(os.path.join(tipo, f"{CAS}.xyz"), 'w') as arq_output:
        arq_output.write(f"{len(atomos['atoms'])}\n")
        arq_output.write("Generated from PubChem\n")
        for atom in atomos['atoms']:
            x, y, z = atom['x'], atom['y'], atom['z']
            arq_output.write(f"{atom['element']} {x} {y} {z}\n")

def procura_e_move_arq(tipo, CAS):
    '''
    Essa função procura os arquivos que não foram encontrados no
    pubchem em nossos diretórios do scifinder e move estes arquivos
    para dentro da pasta relacionada ao tipo
    '''

    procura_dir = tipo + '_scifinder'
    arquivo_desejado = CAS + ".xyz"
    diretorio_origem = os.path.join(os.getcwd(), procura_dir)
    diretorio_destino = os.path.join(os.getcwd(), tipo)

    if os.path.exists(diretorio_origem):
        caminho_arquivo = os.path.join(diretorio_origem, arquivo_desejado)

        if os.path.isfile(caminho_arquivo):
            # Certificar-se de que o diretório de destino existe
            if not os.path.exists(diretorio_destino):
                os.makedirs(diretorio_destino)

            # Caminho do arquivo no diretório de destino
            destino_arquivo = os.path.join(diretorio_destino, arquivo_desejado)

            # Copiar o arquivo para o diretório de destino
            shutil.copy(caminho_arquivo, destino_arquivo)
            print(f"Arquivo '{arquivo_desejado}' copiado para '{diretorio_destino}'.")
        else:
            print(f"Arquivo '{arquivo_desejado}' não encontrado no diretório '{diretorio_origem}'.")


arq_input = 'dados_acidos.txt'

with open(arq_input, 'r') as file:
    # Ignora a primeira linha (cabeçalho)
    next(file)

    tot_CAS_encontrados_pubchem = 0
    tot_CAS_nao_encontrados = 0
    tot_CAS = 0

    for i, line in enumerate(file):
        colunas = line.split()
        tot_CAS += 1

        # Caso não exista alguma propriedade com menos de 5 colunas
        if len(colunas) < 5:
            continue

        nome_molecula = colunas[0]
        tipo = colunas[1]
        CAS = colunas[2].strip()

        cria_diretorio(tipo)

        try:
            compostos = gera_compostos(CAS)
            if compostos:
                print(f'{i} {nome_molecula} {CAS}')
                composto = compostos[0]
                atomos = composto.to_dict(properties=['atoms'])
                tot_CAS_encontrados_pubchem += 1
                cria_arquivo_e_move(tipo, CAS, atomos)
            else:
                print(f"{i} Comp. {nome_molecula} | CAS {CAS} não encontrado no PubChem.")
                procura_e_move_arq(tipo, CAS)
                tot_CAS_nao_encontrados += 1

        except pcp.PubChemHTTPError as e:
            print(f"Erro ao acessar o PubChem: {e}")
        except Exception as e:
            print(f"Erro inesperado com o CAS {CAS}: {e}")

print(f'CAS-total: {tot_CAS} | CAS-Encontrado: {tot_CAS_encontrados_pubchem} | Cas-Movido: {tot_CAS_nao_encontrados}')
