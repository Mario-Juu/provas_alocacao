import os
import subprocess
import pandas as pd
import tabulate


def run_algorithm(algorithm, sala):
    """
    Executa um algoritmo para uma determinada sala de aula

    Parâmetros:
    - algorithm: inteiro (1-4) para aloca_provas ou 'alg5' para o algoritmo de referência
    - sala: nome do arquivo da sala (ex: 'sala1.txt')

    Retorna o número de tipos de prova
    """
    try:
        if algorithm == 'alg5':
            # Executa o algoritmo de referência
            resultado = subprocess.check_output(
                [f'./alg5', sala],
                stderr=subprocess.STDOUT,
                text=True
            ).strip()
            return resultado
        else:
            # Executa o script de alocação de provas
            resultado = subprocess.check_output(
                ['python', 'aloca_provas.py', str(algorithm), sala],
                stderr=subprocess.STDOUT,
                text=True
            ).strip()

        # Extrai o número de tipos de prova
        return int(resultado.split(': ')[-1])
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar algoritmo {algorithm} para {sala}: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None


def main():
    # Lista de salas
    salas = [f'salas/sala{i}.txt' for i in range(1, 13)]

    # Algoritmos a serem testados
    algoritmos = [1, 2, 3, 4, 'alg5']

    # Dicionário para armazenar resultados
    resultados = {
        'Sala': salas,
    }

    # Executa cada algoritmo para cada sala
    for alg in algoritmos:
        nome_alg = f'Alg {alg}' if isinstance(alg, int) else alg
        resultados[nome_alg] = [run_algorithm(alg, sala) for sala in salas]

    # Cria DataFrame
    df = pd.DataFrame(resultados)

    # Configura o estilo da tabela
    tabela_formatada = tabulate.tabulate(
        df,
        headers='keys',
        tablefmt='pipe',
        numalign='center'
    )

    # Imprime a tabela
    print("\nResultados da Alocação de Provas:")
    print(tabela_formatada)

    # Salva resultados em um arquivo CSV
    df.to_csv('resultados_alocacao.csv', index=False)
    print("\nResultados salvos em 'resultados_alocacao.csv'")


if __name__ == "__main__":
    main()