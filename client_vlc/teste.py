import pandas as pd
from scipy.stats import chi2_contingency

dados = {
    'Wife': [156, 124, 77, 82, 53, 32, 33, 12, 10, 13, 8, 0, 0],
    'Alternating': [14, 20, 11, 36, 11, 24, 23, 46, 51, 13, 1, 3, 1],
    'Husband': [2, 5, 7, 15, 1, 4, 9, 23, 75, 21, 53, 160, 6],
    'Jointly': [4, 4, 13, 7, 57, 53, 55, 15, 3, 66, 77, 2, 153]
}
df = pd.DataFrame(dados, index=['Laundry', 'Main_meal', 'Dinner', 'Breakfeast', 'Tidying', 'Dishes', 'Shopping', 'Official', 'Driving', 'Finances', 'Insurance', 'Repairs', 'Holidays'])

# Definição das Hipóteses:
# H0: as frequências das categorias da característica escolhida são igualmente prováveis.
# Ha: as frequências das categorias são diferentes das esperadas.

qui_quadrado, p_value, graus_de_liberdade, _ = chi2_contingency(df)

print(f'Valor do Qui-Quadrado: {qui_quadrado}')
print(f'p-value: {p_value}')
print(f'Graus de Liberdade: {graus_de_liberdade}')

if p_value < 0.05:
    print("Rejeitamos a hipótese nula.")
else:
    print("Não rejeitamos a hipótese nula.") 