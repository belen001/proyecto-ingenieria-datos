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

## 4. Reglas de asociación

El notebook `notebooks/05_reglas_asociacion.ipynb` transforma cada estudiante
en una transacción de atributos discretizados y aplica FP-Growth. El análisis
prioriza reglas cuyo consecuente es `burnout_score=alto` y evalúa soporte,
confianza, lift, leverage y conviction.

Artefactos secundarios:

- `outputs/tablas/itemsets_frecuentes_reglas_asociacion.csv`
- `outputs/tablas/reglas_burnout_alto.csv`
- `outputs/tablas/reglas_burnout_alto_relevantes.csv`
- `outputs/tablas/frecuencia_variables_reglas_asociacion.csv`
- `outputs/tablas/comparacion_reglas_sueno_bajo.csv`

### Estructura de carpetas

```text
EDA_Proyecto/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_calidad_datos.ipynb
│   ├── 02_analisis_univariado.ipynb       
│   ├── 03_analisis_bivariado.ipynb
│   └── 04_integracion_resultados.ipynb
├── outputs/
│   ├── graficos/                         
│   ├── reportes/
│   └── tablas/
└── utils/
    └── eda_helpers.py                        
```

## Fuente y licencia del dataset

- **Nombre:** AI Dependency and Career Anxiety Among Students
- **Naturaleza:** dataset **sintético** (15 000 registros, 30 variables) generado mediante *latent trait modeling* con ruido controlado.
- **Fuente:** _PENDIENTE_CONFIRMAR_ — pegar aquí el enlace exacto de Kaggle (u origen real) desde donde se descargó el dataset.
- **Licencia:** _PENDIENTE_CONFIRMAR_ — indicar la licencia declarada en la fuente (p. ej. CC0, CC-BY-4.0) y sus condiciones de uso.

> Estos dos campos también están en `data/raw/dataset_metadata.json` (`source_url`, `license`).
> Una vez confirmados, reemplazar los marcadores aquí, en el JSON y reservar la cita para el bloque "Referencias" del póster.
