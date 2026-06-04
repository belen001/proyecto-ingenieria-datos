# Definición de la sección de análisis relacional del proyecto

## 1. Enfoque general

En esta etapa del proyecto se analizarán las relaciones entre las variables del dataset **AI Dependency, Career Anxiety and Student Burnout**, con el propósito de comprender qué factores se asocian con el nivel de burnout estudiantil.

La problemática central se enfocará en estudiar cómo distintas dimensiones del estudiante, tales como la dependencia de herramientas de inteligencia artificial, la ansiedad frente al futuro laboral, el estrés, la motivación, los hábitos académicos y ciertos factores contextuales, se relacionan con el `burnout_score`.

El análisis será desarrollado en un notebook de Python, ya que este formato permite integrar código, gráficos, tablas e interpretación textual en un mismo documento. De esta manera, el notebook no solo mostrará los resultados, sino también el razonamiento utilizado para llegar a las conclusiones exploratorias.

## 2. Problemática propuesta

El uso creciente de herramientas de inteligencia artificial en contextos académicos puede influir en la forma en que los estudiantes estudian, resuelven tareas y enfrentan su preparación profesional. Al mismo tiempo, existen variables asociadas al bienestar estudiantil, como el estrés, la motivación, la ansiedad por entrevistas, la ansiedad por inserción laboral y la percepción de preparación profesional.

A partir de esto, la problemática del proyecto se puede formular de la siguiente manera:

**¿Qué variables del dataset se relacionan con mayores niveles de burnout estudiantil y cómo pueden estas relaciones orientar una futura etapa de modelamiento predictivo?**

Esta problemática permite abordar el dataset desde una perspectiva de machine learning, ya que el análisis exploratorio permitirá identificar variables relevantes para posteriormente construir un modelo capaz de predecir o clasificar el burnout estudiantil.

## 3. Variable objetivo tentativa

La variable objetivo principal será:

**`burnout_score`**

Esta variable representa el nivel de burnout del estudiante y será utilizada como referencia para estudiar su relación con las demás variables del dataset.

Dependiendo de la etapa posterior del proyecto, esta variable podría utilizarse de dos formas:

1. **Como variable numérica**, para un problema de regresión.
2. **Como variable categorizada**, para un problema de clasificación, por ejemplo: burnout bajo, medio y alto.

Para esta etapa exploratoria se mantendrá inicialmente como variable numérica, ya que esto permite analizar correlaciones, tendencias y diferencias entre grupos sin perder información.

## 4. Hipótesis inicial del análisis

La hipótesis exploratoria principal será:

**Los estudiantes con mayor dependencia de herramientas de inteligencia artificial, mayor ansiedad profesional, mayor estrés y menor motivación tienden a presentar niveles más altos de burnout.**

A partir de esta hipótesis general, se derivan hipótesis específicas:

1. Los estudiantes con mayor `ai_dependency_score` podrían presentar mayor `burnout_score`.
2. Los estudiantes con mayor `placement_anxiety_score` podrían mostrar mayores niveles de burnout.
3. Los estudiantes con mayor `interview_anxiety_score` podrían presentar mayor burnout.
4. Los estudiantes con mayor `stress_level` podrían tener una relación positiva con el burnout.
5. Los estudiantes con mayor `motivation_score` podrían presentar menor burnout.
6. Los estudiantes que usan IA con mayor frecuencia para tareas académicas podrían mostrar diferencias en sus niveles de burnout respecto a quienes la usan menos.

Estas hipótesis no buscan demostrar causalidad, sino identificar patrones iniciales que puedan ser útiles para la etapa de modelamiento.

## 5. Objetivo del análisis relacional

El objetivo de esta sección será identificar y describir relaciones relevantes entre el `burnout_score` y las demás variables del dataset.

Para ello, se analizarán tres tipos de relaciones:

1. Relaciones entre variables numéricas.
2. Relaciones entre variables categóricas y el burnout.
3. Comparaciones entre grupos de estudiantes según uso de IA, área académica y contexto institucional.

Con este análisis se espera determinar qué variables parecen más relevantes para explicar o predecir el burnout estudiantil.

## 6. Variables principales a considerar

Las variables numéricas más importantes para el análisis serán:

* `daily_ai_tool_usage_hrs`
* `ai_replaces_own_thinking_score`
* `ai_dependency_score`
* `placement_anxiety_score`
* `fear_of_job_loss_to_ai`
* `career_clarity_score`
* `weekly_job_application_count`
* `resume_confidence_score`
* `interview_anxiety_score`
* `daily_study_hours`
* `self_learning_hours_per_week`
* `skill_development_courses_taken`
* `social_media_hrs_per_day`
* `sleep_hours`
* `stress_level`
* `motivation_score`
* `overall_career_readiness_score`
* `burnout_score`

Las variables categóricas relevantes serán:

* `gender`
* `degree_type`
* `stream`
* `year_of_study`
* `college_tier`
* `urban_or_rural`
* `primary_ai_tools_used`
* `uses_ai_for_assignments`

Estas variables permitirán analizar si existen diferencias relevantes en el burnout según perfil académico, contexto del estudiante y uso de herramientas de inteligencia artificial.

## 7. Metodología del notebook

El notebook se organizará en secciones progresivas para mantener claridad y trazabilidad del análisis.

### 7.1 Carga de datos

Se cargará el dataset limpio desde el archivo procesado. En esta sección se verificará que las columnas estén correctamente disponibles y que la variable objetivo `burnout_score` exista en el dataset.

### 7.2 Selección de variables

Se separarán las variables numéricas y categóricas. Esta separación es necesaria porque cada tipo de variable requiere técnicas de análisis diferentes.

Las variables numéricas serán utilizadas para correlaciones, gráficos de dispersión y análisis de tendencias.

Las variables categóricas serán utilizadas para comparaciones entre grupos mediante boxplots y tablas de resumen.

### 7.3 Matriz de correlación

Se construirá una matriz de correlación entre variables numéricas. Para este análisis se utilizará preferentemente la correlación de Spearman, ya que muchas variables del dataset corresponden a puntajes, escalas ordinales o mediciones que no necesariamente tienen una distribución normal.

La matriz de correlación permitirá identificar qué variables se mueven en conjunto con el `burnout_score`.

### 7.4 Ranking de variables relacionadas con burnout

Luego de calcular la matriz de correlación, se extraerá un ranking de las variables más asociadas con `burnout_score`.

Este ranking permitirá priorizar variables para la interpretación y para una futura etapa de modelamiento.

Se analizarán especialmente:

* correlaciones positivas fuertes o moderadas;
* correlaciones negativas relevantes;
* variables con relación débil pero conceptualmente importantes.

### 7.5 Gráficos de dispersión

Se generarán gráficos de dispersión entre `burnout_score` y variables numéricas clave, tales como:

* `stress_level`
* `motivation_score`
* `ai_dependency_score`
* `placement_anxiety_score`
* `interview_anxiety_score`
* `daily_ai_tool_usage_hrs`
* `sleep_hours`

Estos gráficos permitirán observar visualmente si existen tendencias crecientes, decrecientes o patrones dispersos entre las variables.

### 7.6 Comparación entre grupos

Se comparará el `burnout_score` entre grupos definidos por variables categóricas.

Por ejemplo:

* burnout según frecuencia de uso de IA en tareas académicas;
* burnout según herramienta principal de IA utilizada;
* burnout según área de estudio;
* burnout según tipo de institución;
* burnout según zona urbana o rural.

Para esto se utilizarán boxplots y tablas de medias agrupadas.

### 7.7 Interpretación de resultados

Cada gráfico y tabla deberá incluir una interpretación breve. La interpretación no debe limitarse a describir el gráfico, sino explicar qué significa el patrón observado en relación con la problemática del proyecto.

Por ejemplo:

* si `stress_level` tiene una correlación positiva con `burnout_score`, se interpretará como una asociación entre mayor estrés y mayor burnout;
* si `motivation_score` tiene una correlación negativa, se interpretará como una posible relación protectora de la motivación frente al burnout;
* si los estudiantes que usan IA con mayor frecuencia tienen mayor dependencia y mayor burnout promedio, se planteará como una hipótesis para análisis posterior.

## 8. Visualizaciones esperadas

El notebook debería incluir al menos las siguientes visualizaciones:

1. Heatmap de correlación entre variables numéricas.
2. Gráfico de barras con las variables más correlacionadas con `burnout_score`.
3. Scatter plot entre `stress_level` y `burnout_score`.
4. Scatter plot entre `motivation_score` y `burnout_score`.
5. Scatter plot entre `ai_dependency_score` y `burnout_score`.
6. Scatter plot entre `placement_anxiety_score` y `burnout_score`.
7. Boxplot de `burnout_score` según `uses_ai_for_assignments`.
8. Boxplot de `burnout_score` según `primary_ai_tools_used`.
9. Boxplot de `burnout_score` según `stream`.
10. Boxplot de `burnout_score` según `college_tier`.

Estas visualizaciones permitirán respaldar las conclusiones con evidencia gráfica.

## 9. Tablas esperadas

Además de los gráficos, el notebook debería incluir tablas que sinteticen los resultados principales.

Las tablas recomendadas son:

1. Ranking de correlaciones con `burnout_score`.
2. Media de `burnout_score` por frecuencia de uso de IA.
3. Media de `burnout_score` por herramienta principal de IA utilizada.
4. Media de `burnout_score` por área de estudio.
5. Media de `burnout_score` por tipo de institución.
6. Tabla resumen con las variables más relevantes para la futura etapa de modelamiento.

Estas tablas permitirán que los resultados sean más fáciles de interpretar y defender.

## 10. Criterios de interpretación

Para evitar conclusiones incorrectas, el análisis seguirá los siguientes criterios:

1. Una correlación no implica causalidad.
2. Las relaciones encontradas serán tratadas como asociaciones exploratorias.
3. Las variables con alta correlación serán candidatas para la etapa de modelamiento, pero no necesariamente serán definitivas.
4. Las diferencias entre grupos deberán interpretarse considerando el tamaño de cada grupo.
5. Las conclusiones deberán estar respaldadas por gráficos o tablas.
6. Las variables conceptualmente importantes no serán descartadas solo por tener una correlación baja.

## 11. Resultados esperados

Al finalizar el notebook, se espera obtener una visión clara de qué variables están más relacionadas con el burnout estudiantil.

Se espera identificar si el burnout está más asociado con:

* dependencia de IA;
* ansiedad profesional;
* estrés;
* motivación;
* hábitos académicos;
* horas de sueño;
* contexto académico;
* tipo de uso de herramientas de IA.

Estos resultados permitirán justificar la selección de variables para la siguiente etapa del proyecto.

## 12. Conclusión esperada de la sección

Esta sección permitirá transformar el dataset limpio en evidencia exploratoria útil para el proyecto. A través del análisis bivariado, se buscará identificar patrones que expliquen qué factores podrían estar relacionados con el burnout estudiantil.

El resultado principal no será entrenar un modelo todavía, sino construir una base analítica sólida para decidir qué variables considerar en la etapa de machine learning.

De esta forma, el proyecto avanzará desde una simple descripción del dataset hacia una problemática más clara: comprender y eventualmente predecir el burnout estudiantil a partir de variables relacionadas con dependencia de IA, ansiedad profesional, hábitos académicos y bienestar personal.
