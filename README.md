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
