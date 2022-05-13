

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        
    @property
    def formatada(self):
        return f"{self.dia}/{self.mes}/{self.ano}"