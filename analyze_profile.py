import pstats
import json
import os
import sys

def analyze_profile(prof_filename, json_filename):
    # Carregar as estatísticas de profiling do arquivo binário
    stats = pstats.Stats(prof_filename)
    
    # Limpar os nomes dos diretórios nos resultados
    stats.strip_dirs()
    
    # Ordenar por tempo cumulativo
    stats.sort_stats('cumulative')
    
    # Obter as estatísticas
    top_stats = stats.stats
    
    # Carregar dados existentes do arquivo JSON, se houver
    if os.path.exists(json_filename):
        with open(json_filename, 'r') as json_file:
            profile_data = json.load(json_file)
    else:
        profile_data = {}
    
    # Obter o nome do script (sem extensão) como chave principal
    script_name = os.path.splitext(os.path.basename(prof_filename))[0]
    if script_name not in profile_data:
        profile_data[script_name] = []
    
    # Atualizar os dados de profiling
    for func, (cc, nc, tt, ct, callers) in top_stats.items():
        file_name, line_num, func_name = func
        # Procurar a função existente
        function_data = next((item for item in profile_data[script_name] if item["function"] == func_name), None)
        if func_name[0] != '<' and func_name[0] != '_':
            if function_data:
                # Adicionar o tempo cumulativo ao array existente
                function_data["cumulative_time"].append(ct)
            else:
                # Criar novo item para a função
                profile_data[script_name].append({
                    "function": func_name,
                    "cumulative_time": [ct]
                })
    
    # Salvar os dados no arquivo JSON
    with open(json_filename, 'w') as json_file:
        json.dump(profile_data, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 analyze_profile.py <prof_file> <json_file>")
    else:
        analyze_profile(sys.argv[1], sys.argv[2])
