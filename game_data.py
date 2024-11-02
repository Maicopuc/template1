
import csv

class DataLoadError(Exception):
    """Exceção personalizada para erros de carregamento de dados."""
    pass

class GameData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []
        
    def load_data(self):
        """Carrega os dados do arquivo CSV e armazena em self.data."""
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.data.append(row)
            if not self.data:
                raise DataLoadError("Nenhum dado carregado. Verifique o conteúdo do arquivo.")
        except FileNotFoundError:
            raise DataLoadError(f"Arquivo {self.file_path} não encontrado.")
    
    def calculate_free_paid_percentage(self):
        """Calcula o percentual de jogos gratuitos e pagos na plataforma."""
        total_games = len(self.data)
        free_games = sum(1 for game in self.data if float(game['Price']) == 0.0)
        paid_games = total_games - free_games
        return {
            "free_percentage": (free_games / total_games) * 100,
            "paid_percentage": (paid_games / total_games) * 100
        }
    
    def get_year_with_most_releases(self):
        """Determina o ano com o maior número de lançamentos de jogos."""
        year_count = {}
        for game in self.data:
            year = game['Release date'][-4:]  # Extrai o ano da data de lançamento
            if year.isdigit():
                year_count[year] = year_count.get(year, 0) + 1
        
        max_count = max(year_count.values())
        most_common_years = [year for year, count in year_count.items() if count == max_count]
        
        return most_common_years

    def count_games_with_portuguese_support(self):
        """Conta o número de jogos que oferecem suporte ao idioma português."""
        count = 0
        for game in self.data:
            supported_languages = game['Supported languages'].lower()
            if 'portuguese' in supported_languages:
                count += 1
        return count

    def filter_first_20_paid_games(self):
        """Filtra os primeiros 20 jogos pagos do conjunto de dados."""
        paid_games = [game for game in self.data if float(game['Price']) > 0]
        return paid_games[:20]
