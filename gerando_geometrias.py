import pubchempy as pcp
import os


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

def cria_arquivo_e_move(tipo, nome_molecula, atomos):
    '''
    A função cria um arquivo com o nome da molécula e move esse arquivo
    para o diretório que corresponde ao ácido.
    '''
    with open(os.path.join(tipo, f"{nome_molecula}.txt"), 'w') as arq_output:
        arq_output.write(f"{len(atomos['atoms'])}\n")
        arq_output.write("Generated from PubChem\n")
        for atom in atomos['atoms']:
            x, y, z = atom['x'], atom['y'], atom['z']
            arq_output.write(f"{atom['element']} {x} {y} {z}\n")

arq_input = 'dados_acidos.txt'

with open(arq_input, 'r') as file:
    next(file)  # Ignora a primeira linha (cabeçalho)

    tot_CAS_encontrados_pubchem = 0
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
                cria_arquivo_e_move(tipo, nome_molecula, atomos)
            else:
                print(f"{i} Composto {nome_molecula} | CAS {CAS} não encontrado no PubChem.")

        except pcp.PubChemHTTPError as e:
            print(f"Erro ao acessar o PubChem: {e}")
        except Exception as e:
            print(f"Erro inesperado com o CAS {CAS}: {e}")

print(f'CAS-total: {tot_CAS} | CAS-Encontrado: {tot_CAS_encontrados_pubchem}')
