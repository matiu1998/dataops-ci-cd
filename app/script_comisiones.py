import pandas as pd

data = {
    "vendedor": ["Ana", "Luis", "Carlos"],
    "ventas": [1000, 1500, 2000]
}

df = pd.DataFrame(data)
df["comision"] = df["ventas"] * 0.10

df.to_excel("comisiones.xlsx", index=False)

print("Archivo comisiones.xlsx generado correctamente")