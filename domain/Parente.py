class Parente:
    def __init__(self, nome, email, parentesco, dna_compartilhado, mt_dna, y_dna):
        self.nome = nome
        self.email = email
        self.parentesco = parentesco
        self.dna_compartilhado = dna_compartilhado
        self.mt_dna = mt_dna
        self.y_dna = y_dna

    def __str__(self):
        return f'{self.nome} - {self.email}\n\t{self.parentesco}\n\t{self.dna_compartilhado}\n\t{self.mt_dna} - {self.y_dna}'
