# Presentaciones recuperativas
- Belén Bravo: https://youtu.be/1NLfMcxS_AY
- Andres Alvarez: https://drive.google.com/file/d/1vB1djAGyUMVD8tsvrwJa-gLkZ9Ds9cCy/view?usp=sharing
- 
# Análisis de Burnout en Estudiantes Universitarios

**Integrantes:**
- Andrés Alvarez
- Belén Bravo
- Viviana Castro
- Valentina Cifuentes

---

## Problema y objetivo

El burnout estudiantil es un estado de agotamiento crónico que afecta el desempeño académico y el bienestar de los estudiantes universitarios. Con la creciente adopción de herramientas de inteligencia artificial en el ámbito educativo, surge la pregunta de si el uso intensivo de IA, combinado con factores como horas de sueño, horas de estudio y ansiedad laboral, se asocia con niveles elevados de burnout.

**Objetivo:** Identificar y caracterizar los patrones de variables (hábitos de estudio, uso de IA, ansiedad profesional, indicadores de salud mental) que se asocian con niveles altos de `burnout_score` en una muestra sintética de 15 000 estudiantes universitarios, mediante análisis exploratorio de datos y minería de reglas de asociación.

---

## Requisitos

- Python ≥ 3.10
- Dependencias declaradas en `requirements.txt`

## Instalación

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

python -m pip install -r requirements.txt
```

Para ejecutar los notebooks desde este entorno, selecciona el kernel `python3` ubicado en `.venv`.

---

## Cómo reproducir

Ejecutar los notebooks **en el siguiente orden** desde la raíz del repositorio:

| Paso | Notebook | Descripción |
|------|----------|-------------|
| 1 | `notebooks/01_calidad_datos.ipynb` | Limpieza, reporte de nulos, duplicados y tipos. Genera `data/processed/dataset_limpio.csv` |
| 2 | `notebooks/02_analisis_univariado.ipynb` | Estadísticas descriptivas, outliers y distribuciones de cada variable |
| 3 | `notebooks/03_relacion_variables.ipynb` | Correlaciones, comparaciones por grupo y variables candidatas para modelamiento |
| 4 | `notebooks/04_integracion_resultados.ipynb` | Síntesis de hallazgos del EDA y dashboard visual |
| 5 | `notebooks/05_reglas_asociacion.ipynb` | Minería de reglas con FP-Growth; análisis de reglas con consecuente `burnout_score=alto` |

> **Nota:** El notebook `01` debe ejecutarse antes que cualquier otro porque genera `dataset_limpio.csv`, que es el insumo de todos los análisis posteriores.

---

## Estructura de carpetas

```text
proyecto-ingenieria-datos/
├── data/
│   ├── raw/
│   │   ├── ai_dependency_career_anxiety_students.csv
│   │   ├── dataset_metadata.json
│   │   └── feature_dictionary.csv
│   └── processed/
│       └── dataset_limpio.csv          ← generado por 01_calidad_datos
├── docs/
│   ├── metodologia_reglas_asociacion_burnout.md
│   └── relacion_entre_variables_actualizado.md
├── notebooks/
│   ├── 01_calidad_datos.ipynb
│   ├── 02_analisis_univariado.ipynb
│   ├── 03_relacion_variables.ipynb
│   ├── 04_integracion_resultados.ipynb
│   └── 05_reglas_asociacion.ipynb
├── outputs/
│   ├── graficos/                        ← imágenes .png generadas por los notebooks
│   ├── reportes/                        ← reportes .md generados por los notebooks
│   └── tablas/                          ← archivos .csv generados por los notebooks
├── utils/
│   └── eda_helpers.py
├── requirements.txt
└── run_eda.py
```

---

## Descripción de cada análisis

### 1. Calidad de datos (`01_calidad_datos.ipynb`)

Comprensión inicial del dataset y limpieza. Artefactos generados:

- `outputs/tablas/resumen_variables.csv`
- `outputs/tablas/reporte_nulos.csv`
- `outputs/tablas/reporte_duplicados.csv`
- `outputs/tablas/revision_columnas.csv`
- `outputs/reportes/reporte_calidad_datos.md`
- `data/processed/dataset_limpio.csv`

### 2. Análisis univariado (`02_analisis_univariado.ipynb`)

Análisis de cada variable por separado. Cubre:

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

### 3. Relación entre variables (`03_relacion_variables.ipynb`)

Analiza asociaciones entre las variables del dataset limpio y `burnout_score`. Genera tablas de correlaciones, comparaciones por grupo y variables candidatas para una futura etapa de modelamiento.

### 4. Integración de resultados (`04_integracion_resultados.ipynb`)

Síntesis de los hallazgos de los análisis anteriores y dashboard visual con los patrones más relevantes.

### 5. Reglas de asociación (`05_reglas_asociacion.ipynb`)

Transforma cada estudiante en una transacción de atributos discretizados y aplica FP-Growth. El análisis prioriza reglas cuyo consecuente es `burnout_score=alto` y evalúa soporte, confianza, lift, leverage y conviction.

Artefactos generados:

- `outputs/tablas/itemsets_frecuentes_reglas_asociacion.csv`
- `outputs/tablas/reglas_burnout_alto.csv`
- `outputs/tablas/reglas_burnout_alto_relevantes.csv`
- `outputs/tablas/frecuencia_variables_reglas_asociacion.csv`
- `outputs/tablas/comparacion_reglas_sueno_bajo.csv`

---

## Fuente y licencia del dataset

- **Nombre:** AI Dependency and Career Anxiety Among Students
- **Naturaleza:** Dataset **sintético** (15 000 registros, 30 variables) generado mediante *latent trait modeling* con ruido controlado.
- **Fuente:** [Kaggle — sridipbasu/ai-depndency-career-anxiety-and-student-burnout](https://www.kaggle.com/datasets/sridipbasu/ai-depndency-career-anxiety-and-student-burnout)
- **Licencia:** MIT License
