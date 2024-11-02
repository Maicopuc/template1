
from game_data import GameData

# Caminho completo para o arquivo CSV
game_data = GameData(r'C:\Users\maicon\Downloads\maiconpuc\data\steam_games.csv')
game_data.load_data()

# Resultados para o conjunto de dados completo
print("Resultados para o conjunto de dados completo:")
percentages = game_data.calculate_free_paid_percentage()
print(f"Percentual de jogos gratuitos: {percentages['free_percentage']}%")
print(f"Percentual de jogos pagos: {percentages['paid_percentage']}%")

most_releases_year = game_data.get_year_with_most_releases()
print(f"Ano(s) com o maior número de novos jogos: {most_releases_year}")

num_games_with_portuguese = game_data.count_games_with_portuguese_support()
print(f"Número de jogos com suporte ao português: {num_games_with_portuguese}")

# Teste com os primeiros 20 jogos pagos
print("\nResultados para os primeiros 20 jogos pagos:")
sample_data = game_data.filter_first_20_paid_games()
sample_game_data = GameData('')
sample_game_data.data = sample_data

sample_percentages = sample_game_data.calculate_free_paid_percentage()
print(f"Percentual de jogos gratuitos: {sample_percentages['free_percentage']}%")
print(f"Percentual de jogos pagos: {sample_percentages['paid_percentage']}%")

sample_most_releases_year = sample_game_data.get_year_with_most_releases()
print(f"Ano(s) com o maior número de novos jogos na amostra: {sample_most_releases_year}")

sample_num_games_with_portuguese = sample_game_data.count_games_with_portuguese_support()
print(f"Número de jogos com suporte ao português na amostra: {sample_num_games_with_portuguese}")
