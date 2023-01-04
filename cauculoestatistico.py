import pandas as pd

data1 = pd.Series([10,2,15,11,9,3,7,12,5,8])

sorted_data1 = data1.sort_values()

mediana = sorted_data1.median()
media = sorted_data1.mean()
moda = sorted_data1.mode()
desvio_padrao = sorted_data1.std()
variancia = sorted_data1.var()
amplitude_total = sorted_data1.max() - sorted_data1.min()
primeiro_quartil = round(sorted_data1.quantile(0.25))
terceiro_quartil = round(sorted_data1.quantile(0.75))

print([mediana,media,moda,desvio_padrao,variancia, amplitude_total, primeiro_quartil,terceiro_quartil])
print(sorted_data1)
sorted_data1.describe()