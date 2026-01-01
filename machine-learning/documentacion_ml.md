# Modelado de Machine Learning – Tienda Aurelion

Este documento resume el proceso de modelado aplicado en el proyecto, incluyendo regresión y clasificación supervisada. No se incluyen datos ni notebooks, los resultados se presentan mediante gráficos exportados y descripciones del procedimiento.

---

## 1. Objetivo del modelado

Se aplicaron técnicas de *machine learning* con dos propósitos:

- **Regresión:** predecir el *importe* de una venta a partir de variables numéricas y temporales.  
- **Clasificación:** predecir el *medio de pago* más probable según características de la transacción.

Ambos enfoques complementan el análisis exploratorio y aportan información útil para la toma de decisiones.

---

## 2. Preparación de los datos

Antes del modelado se realizaron los siguientes pasos:

- Selección de variables relevantes.  
- Codificación de variables categóricas mediante **One-Hot Encoding**.  
- Estandarización de variables numéricas (solo para modelos que lo requieren).  
- División en **train/test (80/20)** con `random_state=42`.  
- Codificación de la variable objetivo en clasificación mediante `LabelEncoder`.

---

## 3. Regresión lineal

### Objetivo
Predecir el importe de las ventas a partir de:

- cantidad  
- precio_unitario  
- mes (codificado con One-Hot)

### Modelo
Se utilizó **Regresión Lineal**, elegida por su interpretabilidad y capacidad para cuantificar el impacto de cada variable.

### Métricas obtenidas

- **MSE:** 2,655,368.94  
- **RMSE:** ≈ 1629.6  
- **R²:** 0.846  

El modelo explica el **84.6% de la variabilidad** del importe, un desempeño sólido considerando la simplicidad del algoritmo.

### Interpretación de coeficientes
- `cantidad` es la variable más influyente.  
- `precio_unitario` también aporta positivamente.  
- Algunos meses muestran efectos estacionales positivos o negativos.

### Gráficos

**Valores reales vs predichos**  

<img src="graficos/regresion_scatter.png" width="550">

**Coeficientes del modelo**  

<img src="graficos/regresion_coef.png" width="550">


---

## 4. Clasificación supervisada

### Objetivo
Predecir el **medio de pago** utilizado en una venta.

### Variables utilizadas
- cantidad  
- precio_unitario  
- categoría (One-Hot)  
- ciudad (One-Hot)  
- mes (One-Hot)

### Modelos probados

#### 1. Logistic Regression
- Accuracy: ~0.38–0.43  
- Problemas de convergencia  
- Sensible al desbalance de clases  

#### 2. XGBoost
- Accuracy: ~0.39  
- No mejoró respecto a Random Forest  

#### 3. Random Forest (modelo elegido)
- Accuracy: ~0.45–0.48  
- Más estable en datasets pequeños  
- Maneja bien variables categóricas codificadas  
- Permite interpretar importancia de variables  

### Matriz de confusión – Random Forest

<img src="graficos/RF_matriz.png" width="550">


### Importancia de variables

<img src="graficos/RF_featureImportance.png" width="550">

### Interpretación
- `precio_unitario` y `cantidad` son las variables más relevantes.  
- Las variables de ciudad y mes aportan menos información.  
- La clase 2 es difícil de predecir por su baja frecuencia.

---

## 5. Limitaciones del dataset

- Dataset pequeño.  
- Clases desbalanceadas en la variable objetivo.  
- Variables categóricas con poco poder discriminante.  

---

## 6. Conclusiones

- **Regresión lineal** obtuvo un desempeño sólido (R² = 0.846).  
- **Random Forest** fue el mejor modelo de clasificación, aunque con accuracy moderada debido al tamaño y desbalance del dataset.  
- Los modelos sirven como prototipo válido para análisis exploratorio y planificación.  

**Futuras mejoras:**
- Recolección de más datos  
- Balanceo de clases (SMOTE)  
- Ingeniería de nuevas features  
- Modelos más robustos con mayor volumen de datos  

> **Nota:** Este trabajo forma parte del Sprint 3 del programa *Fundamentos de Inteligencia Artificial* de IBM + Guayerd (2025). El objetivo del sprint fue aplicar técnicas de Machine Learning para regresión y clasificación utilizando un dataset de ventas.
