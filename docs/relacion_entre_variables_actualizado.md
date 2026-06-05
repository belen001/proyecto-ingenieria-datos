# Definición actualizada de la sección de análisis relacional del proyecto

## 1. Enfoque general

En esta etapa del proyecto se analizarán las relaciones entre las variables del dataset **AI Dependency, Career Anxiety and Student Burnout** y la variable objetivo `burnout_score`.

El análisis mantiene como foco el burnout estudiantil, pero incorpora una distinción metodológica importante: no todas las variables tienen el mismo nivel de cercanía conceptual con el burnout. Algunas variables, como `stress_level`, `motivation_score`, `placement_anxiety_score` o `interview_anxiety_score`, son de autopercepción y su relación con burnout es esperable. Por ello, además de revisar estas variables, el análisis se complementará con variables menos directas, asociadas a hábitos, uso de IA y contexto académico.

De esta forma, el notebook no solo buscará identificar las variables más correlacionadas con el burnout, sino también diferenciar entre relaciones esperables y patrones menos evidentes que puedan ser útiles para una futura etapa de modelamiento.

## 2. Problemática propuesta

La problemática del proyecto se reformula de la siguiente manera:

**¿Qué variables subjetivas, conductuales y contextuales se relacionan con mayores niveles de burnout estudiantil, y cuáles de ellas podrían orientar una futura etapa de modelamiento predictivo?**

Esta formulación permite analizar el burnout desde tres dimensiones:

1. **Subjetiva o de autopercepción:** variables vinculadas directamente con estrés, motivación, ansiedad, confianza y preparación percibida.
2. **Conductual o de hábitos:** variables que describen acciones o rutinas del estudiante, como uso de IA, horas de estudio, sueño, redes sociales, postulaciones, cursos y experiencia de práctica.
3. **Contextual o demográfica:** variables que describen el perfil o entorno del estudiante, como género, edad, área de estudio, tipo de institución, año académico y zona urbana/rural.

Esta separación permite evitar que el análisis dependa únicamente de relaciones evidentes y ayuda a construir una lectura más útil para machine learning.

## 3. Variable objetivo

La variable objetivo principal será:

**`burnout_score`**

Esta variable representa el nivel de burnout del estudiante y será utilizada como referencia para estudiar su relación con las demás variables.

En esta etapa se mantendrá como variable numérica para observar correlaciones, tendencias y diferencias entre grupos. En una etapa posterior podría mantenerse como problema de regresión o transformarse en categorías para un problema de clasificación, siempre que se definan umbrales justificados.

## 4. Hipótesis del análisis

La hipótesis general será:

**Los estudiantes con mayor dependencia de IA, mayor ansiedad profesional, mayor estrés y menor motivación tenderán a presentar mayores niveles de burnout.**

Sin embargo, se agrega una hipótesis complementaria:

**Aunque las variables subjetivas probablemente presenten las asociaciones más fuertes, variables conductuales y contextuales podrían entregar patrones menos evidentes y más útiles para perfilar el problema de machine learning.**

A partir de esto, el análisis buscará responder dos preguntas:

1. ¿Qué variables de autopercepción se relacionan más fuertemente con `burnout_score`?
2. ¿Qué variables de hábitos, uso de IA y contexto académico muestran patrones relevantes aunque su correlación sea menor?

## 5. Bloques de variables

### 5.1 Variables subjetivas o de autopercepción

Estas variables están más cercanas conceptualmente al burnout y, por lo tanto, se espera que tengan relaciones más fuertes:

- `stress_level`
- `motivation_score`
- `placement_anxiety_score`
- `interview_anxiety_score`
- `fear_of_job_loss_to_ai`
- `ai_dependency_score`
- `ai_replaces_own_thinking_score`
- `career_clarity_score`
- `resume_confidence_score`
- `overall_career_readiness_score`

Estas variables permiten revisar la coherencia interna del dataset, pero deben interpretarse con cautela porque dependen de autopercepción.

### 5.2 Variables conductuales o de hábitos

Estas variables describen rutinas, acciones o exposición del estudiante:

- `daily_ai_tool_usage_hrs`
- `uses_ai_for_assignments`
- `daily_study_hours`
- `self_learning_hours_per_week`
- `skill_development_courses_taken`
- `social_media_hrs_per_day`
- `sleep_hours`
- `weekly_job_application_count`
- `internship_experience`
- `seeks_career_counseling`

Estas variables pueden ser menos obvias, pero son importantes porque permiten observar patrones conductuales asociados al burnout.

### 5.3 Variables contextuales o demográficas

Estas variables describen el perfil académico o social del estudiante:

- `age`
- `gender`
- `degree_type`
- `stream`
- `year_of_study`
- `college_tier`
- `urban_or_rural`
- `primary_ai_tools_used`

Estas variables permiten analizar diferencias descriptivas entre grupos y detectar si ciertos contextos presentan mayor burnout promedio.

## 6. Metodología del notebook

El notebook se organizará en las siguientes secciones:

### 6.1 Carga y validación de datos

Se cargará el dataset limpio desde `data/processed/dataset_limpio.csv`. Se validará la existencia de `burnout_score`, dimensiones del dataset, tipos de datos, nulos y duplicados.

### 6.2 Selección y agrupación de variables

Se definirán listas de variables por bloque conceptual:

- variables subjetivas;
- variables conductuales;
- variables contextuales;
- variables categóricas para comparación de grupos.

También se excluirá `student_id`, porque corresponde a un identificador y no a una variable explicativa.

### 6.3 Correlaciones numéricas

Se calculará una matriz de correlación Spearman entre variables numéricas y `burnout_score`.

Además del ranking global, se agregará una columna que indique a qué bloque pertenece cada variable. Esto permitirá distinguir si las variables más asociadas son subjetivas, conductuales o contextuales.

### 6.4 Análisis por bloques

Se analizarán los resultados separando:

1. variables subjetivas más relacionadas con burnout;
2. variables conductuales con patrones relevantes;
3. variables contextuales con diferencias descriptivas.

Esta lectura evitará que el análisis se limite solo a las correlaciones más altas.

### 6.5 Visualizaciones bivariadas

Se mantendrán gráficos de dispersión para variables de alta relación, pero se agregarán gráficos para variables conductuales menos directas, como:

- `daily_ai_tool_usage_hrs`
- `sleep_hours`
- `social_media_hrs_per_day`
- `daily_study_hours`
- `weekly_job_application_count`
- `skill_development_courses_taken`

Esto permitirá observar si existen tendencias menos evidentes asociadas a burnout.

### 6.6 Comparaciones por grupos

Se comparará `burnout_score` entre grupos usando tablas con `count`, `mean`, `median`, `std`, `min` y `max`, además de boxplots para variables relevantes.

Las comparaciones principales serán:

- frecuencia de uso de IA en tareas;
- herramienta principal de IA utilizada;
- área de estudio;
- tipo de institución;
- búsqueda de orientación profesional;
- experiencia de práctica.

Como comparación secundaria, se revisarán variables de contexto como género, tipo de grado, año de estudio y zona urbana/rural.

### 6.7 Tabla final de variables candidatas

La tabla final no seleccionará variables solo por mayor correlación. También considerará:

- fuerza de asociación observada;
- tipo de variable;
- bloque conceptual;
- relevancia para la problemática;
- cautelas de interpretación.

Esto permitirá diferenciar variables que son predictivamente fuertes pero muy subjetivas, de variables menos fuertes pero más descriptivas del contexto o conducta del estudiante.

## 7. Criterios de interpretación

El análisis seguirá los siguientes criterios:

1. Una correlación no implica causalidad.
2. Las variables subjetivas deben interpretarse con cautela por su cercanía conceptual con burnout.
3. Las variables conductuales y contextuales pueden tener correlaciones menores, pero seguir siendo útiles para una futura etapa de modelamiento.
4. Las diferencias entre grupos se interpretarán considerando el tamaño de cada grupo.
5. Las conclusiones deberán estar respaldadas por gráficos o tablas.
6. No se descartarán variables únicamente por baja correlación si tienen valor conceptual para el problema.

## 8. Resultados esperados

Al finalizar el notebook, se espera obtener:

1. un ranking global de variables relacionadas con `burnout_score`;
2. una lectura separada por bloques de variables;
3. identificación de variables subjetivas altamente relacionadas con burnout;
4. identificación de variables conductuales y contextuales con patrones relevantes;
5. tablas y gráficos que respalden las interpretaciones;
6. una selección de variables candidatas para modelamiento futuro.

## 9. Conclusión esperada de la sección

Esta sección permitirá transformar el análisis relacional en una lectura más completa del problema. En lugar de concluir únicamente que estrés, motivación y ansiedad se relacionan con burnout, el análisis distinguirá entre variables esperables de autopercepción y variables menos evidentes asociadas a hábitos, uso de IA y contexto académico.

De esta manera, el proyecto avanzará hacia una problemática más sólida: comprender el burnout estudiantil no solo desde la percepción individual, sino también desde comportamientos y condiciones del entorno que podrían servir para una futura etapa de machine learning.
