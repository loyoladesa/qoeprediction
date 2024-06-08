from scipy.stats import chi2_contingency
import numpy as np

# Dados
data = np.array([[30, 10], [20, 30], [15, 25]])

# Teste qui-quadrado
chi2, p, dof, expected = chi2_contingency(data)

print(f"Chi-squared: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of freedom: {dof}")
print(f"Expected Frequencies:\n{expected}")
