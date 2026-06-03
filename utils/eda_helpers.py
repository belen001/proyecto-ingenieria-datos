import pandas as pd
import os
import re
from pathlib import Path

# Paths relative to project root
DATA_RAW_DIR = Path(__file__).parent.parent / "data" / "raw"
DATA_PROCESSED_DIR = Path(__file__).parent.parent / "data" / "processed"
OUTPUTS_TABLAS_DIR = Path(__file__).parent.parent / "outputs" / "tablas"
OUTPUTS_REPORTES_DIR = Path(__file__).parent.parent / "outputs" / "reportes"

def ensure_dirs():
    """Create required output directories if they do not exist."""
    for p in [DATA_PROCESSED_DIR, OUTPUTS_TABLAS_DIR, OUTPUTS_REPORTES_DIR]:
        p.mkdir(parents=True, exist_ok=True)

def load_metadata():
    meta_path = DATA_RAW_DIR / "dataset_metadata.json"
    return pd.read_json(meta_path, typ="series") if meta_path.exists() else pd.Series()

def load_feature_dictionary():
    dict_path = DATA_RAW_DIR / "feature_dictionary.csv"
    return pd.read_csv(dict_path) if dict_path.exists() else pd.DataFrame()

def load_dataset():
    csv_path = DATA_RAW_DIR / "ai_dependency_career_anxiety_students.csv"
    return pd.read_csv(csv_path)

def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Convert column names to snake_case, lower case, strip whitespace."""
    def to_snake(col):
        col = col.strip()
        col = re.sub(r"[\s]+", "_", col)
        col = re.sub(r"[^0-9a-zA-Z_]+", "", col)
        return col.lower()
    df = df.rename(columns=lambda x: to_snake(x))
    return df

def summarize_variables(df: pd.DataFrame) -> pd.DataFrame:
    """Return a summary table with name, dtype, unique values count, missing count."""
    summary = pd.DataFrame({
        "variable": df.columns,
        "dtype": df.dtypes.astype(str),
        "num_unique": df.nunique(),
        "num_missing": df.isna().sum()
    })
    return summary

def detect_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Return a DataFrame of duplicated rows (all columns)."""
    dup_mask = df.duplicated(keep=False)
    return df[dup_mask]

def treat_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Simple missing value treatment: drop any rows containing NA."""
    return df.dropna().reset_index(drop=True)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply all cleaning steps: normalize columns, drop exact duplicates, treat missing values."""
    df = normalize_column_names(df)
    df = df.drop_duplicates().reset_index(drop=True)
    df = treat_missing(df)
    return df

def save_dataframe(df: pd.DataFrame, path: Path):
    df.to_csv(path, index=False)

def generate_report(summary_df: pd.DataFrame, nulls_df: pd.DataFrame, dup_df: pd.DataFrame, column_review_df: pd.DataFrame, feature_dict: pd.DataFrame, target_var: str) -> str:
    """Create a markdown report string."""
    md = []
    md.append("# Reporte de Calidad de Datos")
    md.append("\n## Resumen de Variables")
    md.append(summary_df.to_markdown(index=False))
    md.append("\n## Valores Nulos")
    if nulls_df.empty:
        md.append("No se encontraron valores nulos.")
    else:
        md.append(nulls_df.to_markdown(index=False))
    md.append("\n## Registros Duplicados")
    if dup_df.empty:
        md.append("No se encontraron filas duplicadas.")
    else:
        md.append(dup_df.to_markdown(index=False))
    md.append("\n## Revisión de Nombres de Columnas")
    md.append(column_review_df.to_markdown(index=False))
    md.append("\n## Significado de Principales Variables")
    top_features = feature_dict.head(5)
    for _, row in top_features.iterrows():
        md.append(f"- **{row['feature']}** ({row['type']}): {row['description']}")
    md.append("\n## Variable objetivo detectada")
    md.append(f"La variable objetivo es **{target_var}** según el metadata.")
    return "\n".join(md)

def run_full_eda():
    """Execute the whole pipeline and write all artefacts."""
    ensure_dirs()
    meta = load_metadata()
    target_var = meta.get("target_variable", "")
    feature_dict = load_feature_dictionary()
    raw_df = load_dataset()
    # Paso 1: resumen inicial
    summary = summarize_variables(raw_df)
    # Nulls report
    nulls = raw_df.isna().sum().reset_index()
    nulls.columns = ["variable", "num_missing"]
    nulls = nulls[nulls["num_missing"] > 0]
    # Duplicados
    dup = detect_duplicates(raw_df)
    # Revisión de nombres de columnas (antes vs después)
    normalized = normalize_column_names(raw_df.copy())
    column_review = pd.DataFrame({
        "original": raw_df.columns,
        "normalized": normalized.columns
    })
    # Limpieza
    cleaned = clean_data(raw_df)
    # Guardar archivos
    save_dataframe(summary, OUTPUTS_TABLAS_DIR / "resumen_variables.csv")
    save_dataframe(nulls, OUTPUTS_TABLAS_DIR / "reporte_nulos.csv")
    save_dataframe(dup, OUTPUTS_TABLAS_DIR / "reporte_duplicados.csv")
    save_dataframe(column_review, OUTPUTS_TABLAS_DIR / "revision_columnas.csv")
    save_dataframe(cleaned, DATA_PROCESSED_DIR / "dataset_limpio.csv")
    # Generar reporte markdown
    report_md = generate_report(summary, nulls, dup, column_review, feature_dict, target_var)
    report_path = OUTPUTS_REPORTES_DIR / "reporte_calidad_datos.md"
    report_path.write_text(report_md, encoding="utf-8")
    return {
        "summary_path": OUTPUTS_TABLAS_DIR / "resumen_variables.csv",
        "nulls_path": OUTPUTS_TABLAS_DIR / "reporte_nulos.csv",
        "dup_path": OUTPUTS_TABLAS_DIR / "reporte_duplicados.csv",
        "column_review_path": OUTPUTS_TABLAS_DIR / "revision_columnas.csv",
        "processed_path": DATA_PROCESSED_DIR / "dataset_limpio.csv",
        "report_path": report_path
    }
