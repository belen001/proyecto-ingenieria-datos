# Informe Final del EDA — AI Dependency, Career Anxiety and Student Burnout

## 1. Descripción del Dataset

- **Fuente:** Dataset sintético generado mediante *latent trait modeling* con ruido controlado.
- **Registros originales:** 15,000 | **Tras limpieza:** 11,119 (25.9% eliminados por valores nulos).
- **Variables:** 30 columnas (22 numéricas, 8 categóricas).
- **Variable objetivo (metadata):** `overall_career_readiness_score`.
- **Variable central del EDA relacional:** `burnout_score`.

## 2. Calidad de Datos

- Sin duplicados exactos.
- 5 variables con valores nulos; `primary_ai_tools_used` con 21.4% faltante.
- Tratamiento: eliminación de filas con NA.
- Sin variables de baja variabilidad.
- Outliers moderados (máximo: `internship_experience` con 5.24%).

## 3. Hallazgos Principales

### Distribuciones
- 17 de 22 variables numéricas son aproximadamente simétricas.
- `burnout_score` tiene media=5.64, mediana=6.0 y buena dispersión (σ=2.06).
- Variables sesgadas: `seeks_career_counseling`, `skill_development_courses_taken`, `age`.

### Relaciones con Burnout

**Variables más asociadas (Spearman):**
1. `stress_level` (ρ=+0.577) — la más fuerte.
2. `motivation_score` (ρ=−0.524) — relación protectora.
3. `seeks_career_counseling` (ρ=+0.386).
4. `placement_anxiety_score` (ρ=+0.370).
5. `interview_anxiety_score` (ρ=+0.356).
6. `fear_of_job_loss_to_ai` (ρ=+0.355).
7. `ai_dependency_score` (ρ=+0.351).

**Patrones por grupo:**
- Uso de IA "Always" → burnout promedio 6.64 vs 5.00 de "Never" (+1.64 puntos).
- Estudiantes de CS/IT → mayor burnout (5.87) vs otras áreas.
- Universidades Tier 3 → mayor burnout (5.76) que Tier 1 (5.30).
- Género, zona y tipo de grado no muestran diferencias relevantes.

## 4. Limitaciones

1. Dataset sintético (las relaciones reflejan la estructura de generación).
2. Diseño transversal (no se puede establecer causalidad).
3. Multicolinealidad entre variables subjetivas.
4. 25.9% de datos eliminados por valores nulos.
5. Escalas ordinales tratadas como numéricas.

## 5. Recomendaciones

### Para reglas de asociación

**Problemática recomendada:** Identificar combinaciones de comportamientos de uso de IA, hábitos de estudio y características académicas asociadas a burnout alto.

- Discretizar variables continuas en 3 niveles (Bajo/Medio/Alto).
- Usar FP-Growth con min_support=0.05, min_confidence=0.6.
- Variables prioritarias: `burnout_score`, `stress_level`, `ai_dependency_score`, `motivation_score`, `uses_ai_for_assignments`, `daily_ai_tool_usage_hrs`, `sleep_hours`, `stream`.

### Para modelamiento predictivo

- Variable objetivo: `burnout_score` (discretizada o continua).
- Features prioritarios: los 7 primeros del ranking de correlaciones.
- Considerar separar variables subjetivas de conductuales para evitar información redundante.

## 6. Artefactos Generados

| Artefacto | Ruta |
|-----------|------|
| Dataset limpio | `data/processed/dataset_limpio.csv` |
| Estadísticas descriptivas | `outputs/tablas/estadisticas_descriptivas.csv` |
| Reporte de outliers | `outputs/tablas/reporte_outliers.csv` |
| Forma de distribuciones | `outputs/tablas/forma_distribuciones.csv` |
| Ranking de correlaciones | `outputs/tablas/ranking_correlaciones_burnout.csv` |
| Variables candidatas | `outputs/tablas/variables_candidatas_modelamiento.csv` |
| Comparaciones por grupo | `outputs/tablas/burnout_por_*.csv` |
| Gráficos univariados | `outputs/graficos/univar_*.png`, `bar_*.png` |
| Gráficos de síntesis | `outputs/graficos/panel_variables_clave.png`, `top10_correlaciones_burnout.png`, `heatmap_variables_prioritarias.png` |
| Informe final | `outputs/reportes/informe_final_eda.md` |