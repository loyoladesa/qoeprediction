from scipy.stats import chi2_contingency
import numpy as np

# Dados
data = np.array([[176, 136,222,114], [24, 24,18,6]])

# Teste qui-quadrado
chi2, p, dof, expected = chi2_contingency(data)

print(f"Chi-squared: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of freedom: {dof}")
print(f"Expected Frequencies:\n{expected}")