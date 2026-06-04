import pandas as pd
import numpy as np
import os
import re
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

# Paths relative to project root
DATA_RAW_DIR = Path(__file__).parent.parent / "data" / "raw"
DATA_PROCESSED_DIR = Path(__file__).parent.parent / "data" / "processed"
OUTPUTS_TABLAS_DIR = Path(__file__).parent.parent / "outputs" / "tablas"
OUTPUTS_REPORTES_DIR = Path(__file__).parent.parent / "outputs" / "reportes"
OUTPUTS_GRAFICOS_DIR = Path(__file__).parent.parent / "outputs" / "graficos"

# ── Paleta corporativa ──────────────────────────────────────────────────────
PALETTE_NUM = "Blues_d"       # histogramas / boxplots numéricos
PALETTE_CAT = "Set2"          # barras categóricas
COLOR_MAIN  = "#3B82F6"       # azul principal
COLOR_OUT   = "#EF4444"       # rojo para outliers

def ensure_dirs():
    """Create required output directories if they do not exist."""
    for p in [DATA_PROCESSED_DIR, OUTPUTS_TABLAS_DIR, OUTPUTS_REPORTES_DIR, OUTPUTS_GRAFICOS_DIR]:
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


# ═══════════════════════════════════════════════════════════════════════════
#  ANÁLISIS UNIVARIADO
# ═══════════════════════════════════════════════════════════════════════════

def descriptive_stats_numeric(df: pd.DataFrame, cols: list = None) -> pd.DataFrame:
    """
    Estadísticas descriptivas para variables numéricas:
    media, mediana, mín, máx, desv. estándar y percentiles (P25, P75, P90).
    """
    if cols is None:
        cols = df.select_dtypes(include="number").columns.tolist()
    stats = df[cols].agg(
        ["mean", "median", "min", "max", "std"]
    ).T.rename(columns={
        "mean": "Media",
        "median": "Mediana",
        "min": "Mínimo",
        "max": "Máximo",
        "std": "Desv_std"
    })
    for p in [25, 75, 90]:
        stats[f"P{p}"] = df[cols].quantile(p / 100)
    stats.index.name = "Variable"
    return stats.reset_index()


def detect_outliers_iqr(df: pd.DataFrame, cols: list = None) -> pd.DataFrame:
    """
    Detecta outliers usando la regla IQR.
    Devuelve un DataFrame con: variable, n_outliers, pct_outliers,
    límite inferior y límite superior.
    """
    if cols is None:
        cols = df.select_dtypes(include="number").columns.tolist()
    records = []
    for col in cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        mask = (df[col] < lo) | (df[col] > hi)
        n_out = mask.sum()
        records.append({
            "Variable": col,
            "Límite_inf": round(lo, 4),
            "Límite_sup": round(hi, 4),
            "N_outliers": int(n_out),
            "Pct_outliers": round(n_out / len(df) * 100, 2)
        })
    return pd.DataFrame(records)


def detect_low_variability(df: pd.DataFrame, cv_threshold: float = 0.05,
                           cat_dominance: float = 0.95) -> pd.DataFrame:
    """
    Identifica variables con baja variabilidad:
    - Numéricas: coeficiente de variación < cv_threshold.
    - Categóricas: categoría dominante > cat_dominance de los registros.
    """
    records = []
    num_cols = df.select_dtypes(include="number").columns.tolist()
    cat_cols = df.select_dtypes(exclude="number").columns.tolist()

    for col in num_cols:
        mean_val = df[col].mean()
        cv = df[col].std() / mean_val if mean_val != 0 else np.inf
        if cv < cv_threshold:
            records.append({"Variable": col, "Tipo": "numérica",
                            "Motivo": f"CV = {cv:.4f} < {cv_threshold}"})

    for col in cat_cols:
        top_freq = df[col].value_counts(normalize=True).iloc[0]
        if top_freq > cat_dominance:
            records.append({"Variable": col, "Tipo": "categórica",
                            "Motivo": f"Categoría dominante = {top_freq:.2%}"})
    return pd.DataFrame(records) if records else pd.DataFrame(
        columns=["Variable", "Tipo", "Motivo"])


# ── Funciones de graficación ─────────────────────────────────────────────────

def _save_fig(fig: plt.Figure, name: str):
    """Guarda la figura en outputs/graficos/ y cierra."""
    ensure_dirs()
    path = OUTPUTS_GRAFICOS_DIR / name
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return path


def plot_histogram(df: pd.DataFrame, col: str, bins: int = 30) -> Path:
    """Histograma con KDE para una variable numérica."""
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.histplot(df[col].dropna(), bins=bins, kde=True, color=COLOR_MAIN,
                 edgecolor="white", linewidth=0.6, ax=ax)
    ax.set_title(f"Distribución de {col}", fontsize=13, fontweight="bold", pad=10)
    ax.set_xlabel(col)
    ax.set_ylabel("Frecuencia")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    sns.despine(ax=ax)
    fig.tight_layout()
    return _save_fig(fig, f"hist_{col}.png")


def plot_boxplot(df: pd.DataFrame, col: str) -> Path:
    """Boxplot horizontal para una variable numérica."""
    fig, ax = plt.subplots(figsize=(7, 2.5))
    sns.boxplot(x=df[col].dropna(), color=COLOR_MAIN, linewidth=1.2,
                flierprops=dict(marker="o", markerfacecolor=COLOR_OUT,
                                markersize=4, linestyle="none"),
                ax=ax)
    ax.set_title(f"Boxplot de {col}", fontsize=13, fontweight="bold", pad=10)
    ax.set_xlabel(col)
    sns.despine(ax=ax, left=True)
    fig.tight_layout()
    return _save_fig(fig, f"box_{col}.png")


def plot_barplot(df: pd.DataFrame, col: str, top_n: int = 15) -> Path:
    """Gráfico de barras para una variable categórica."""
    counts = df[col].value_counts().head(top_n)
    palette = sns.color_palette(PALETTE_CAT, n_colors=len(counts))
    fig, ax = plt.subplots(figsize=(8, max(3, len(counts) * 0.45)))
    bars = ax.barh(counts.index[::-1], counts.values[::-1], color=palette[::-1],
                   edgecolor="white", height=0.65)
    for bar, val in zip(bars, counts.values[::-1]):
        ax.text(bar.get_width() + counts.max() * 0.01, bar.get_y() + bar.get_height() / 2,
                f"{val:,}", va="center", fontsize=9)
    ax.set_title(f"Distribución de {col}", fontsize=13, fontweight="bold", pad=10)
    ax.set_xlabel("Frecuencia")
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    sns.despine(ax=ax)
    fig.tight_layout()
    return _save_fig(fig, f"bar_{col}.png")


def plot_all_univariate(df: pd.DataFrame,
                        num_cols: list = None,
                        cat_cols: list = None) -> dict:
    """
    Genera histograma + boxplot para cada variable numérica,
    y gráfico de barras para cada variable categórica.
    Devuelve un dict {variable: [lista de rutas generadas]}.
    """
    if num_cols is None:
        num_cols = df.select_dtypes(include="number").columns.tolist()
    if cat_cols is None:
        cat_cols = df.select_dtypes(exclude="number").columns.tolist()

    paths = {}
    for col in num_cols:
        paths[col] = [
            plot_histogram(df, col),
            plot_boxplot(df, col),
        ]
    for col in cat_cols:
        paths[col] = [plot_barplot(df, col)]
    return paths


# ── Orquestador principal del análisis univariado ────────────────────────────

def run_univariate_analysis(df: pd.DataFrame = None) -> dict:
    """
    Ejecuta el análisis univariado completo sobre el dataset limpio:
    1. Estadísticas descriptivas numéricas.
    2. Detección de outliers por IQR.
    3. Detección de baja variabilidad.
    4. Generación de gráficos (histogramas, boxplots, barras).
    Guarda tablas en outputs/tablas/ y gráficos en outputs/graficos/.
    """
    ensure_dirs()

    if df is None:
        processed_path = DATA_PROCESSED_DIR / "dataset_limpio.csv"
        if not processed_path.exists():
            raw_df = load_dataset()
            df = clean_data(raw_df)
            save_dataframe(df, processed_path)
        else:
            df = pd.read_csv(processed_path)

    # Columnas por tipo (excluir identificadores sin variabilidad analítica)
    exclude = ["student_id"]
    num_cols = [c for c in df.select_dtypes(include="number").columns if c not in exclude]
    cat_cols = [c for c in df.select_dtypes(exclude="number").columns if c not in exclude]

    # 1. Estadísticas descriptivas
    stats_df = descriptive_stats_numeric(df, num_cols)
    stats_path = OUTPUTS_TABLAS_DIR / "estadisticas_descriptivas.csv"
    save_dataframe(stats_df, stats_path)

    # 2. Outliers
    outliers_df = detect_outliers_iqr(df, num_cols)
    outliers_path = OUTPUTS_TABLAS_DIR / "reporte_outliers.csv"
    save_dataframe(outliers_df, outliers_path)

    # 3. Baja variabilidad
    low_var_df = detect_low_variability(df)
    low_var_path = OUTPUTS_TABLAS_DIR / "baja_variabilidad.csv"
    save_dataframe(low_var_df, low_var_path)

    # 4. Gráficos
    graph_paths = plot_all_univariate(df, num_cols, cat_cols)

    return {
        "stats_path": stats_path,
        "outliers_path": outliers_path,
        "low_var_path": low_var_path,
        "graph_paths": graph_paths,
        "num_cols": num_cols,
        "cat_cols": cat_cols,
    }
