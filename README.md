# proyecto-ingenieria-datos

## Requisitos
- Python ≥ 3.14
- Dependencias declaradas en `requirements.txt`

## Instalación
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Para ejecutar notebooks desde este entorno, selecciona el kernel `python3` ubicado en `.venv`.

## 1. Comprensión y calidad de datos

Este proyecto incluye un análisis exploratorio de datos (EDA) centrado en la comprensión del dataset y la calidad de los datos. Se generan los siguientes artefactos:

- `outputs/tablas/resumen_variables.csv`
- `outputs/tablas/reporte_nulos.csv`
- `outputs/tablas/reporte_duplicados.csv`
- `outputs/tablas/revision_columnas.csv`
- `outputs/reportes/reporte_calidad_datos.md`
- `data/processed/dataset_limpio.csv`

El notebook `notebooks/01_calidad_datos.ipynb` contiene los pasos reproducibles.

## 2. Relación entre variables

El notebook `notebooks/03_relacion_variables.ipynb` analiza asociaciones entre las variables del dataset limpio y `burnout_score`. Genera tablas de correlaciones, comparaciones por grupo y variables candidatas para una futura etapa de modelamiento.

## 3. Análisis univariado

El notebook `notebooks/02_analisis_univariado.ipynb` analiza cada variable por separado. Cubre:

- Estadísticas descriptivas (media, mediana, mín, máx, desv. estándar, P25/P75/P90).
- Detección de valores atípicos por regla IQR.
- Identificación de variables con baja variabilidad (coeficiente de variación / categoría dominante).
- Histogramas con KDE, boxplots y gráficos de barras por variable.
- Comentarios sobre forma de distribución (asimetría, curtosis).

Artefactos generados:

- `outputs/tablas/estadisticas_descriptivas.csv`
- `outputs/tablas/reporte_outliers.csv`
- `outputs/tablas/baja_variabilidad.csv`
- `outputs/tablas/forma_distribuciones.csv`
- `outputs/graficos/univar_<variable>.png` (histograma + boxplot por variable numérica)
- `outputs/graficos/bar_<variable>.png` (gráfico de barras por variable categórica)
- `outputs/graficos/resumen_outliers.png`
- `outputs/graficos/panel_distribuciones_asimetricas.png`

### Estructura de carpetas

```text
EDA_Proyecto/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_calidad_datos.ipynb
│   ├── 02_analisis_univariado.ipynb      ← nuevo
│   ├── 03_analisis_bivariado.ipynb
│   └── 04_integracion_resultados.ipynb
├── outputs/
│   ├── graficos/                         ← nuevo
│   ├── reportes/
│   └── tablas/
└── utils/
    └── eda_helpers.py                    ← extendido con funciones univariadas
```
