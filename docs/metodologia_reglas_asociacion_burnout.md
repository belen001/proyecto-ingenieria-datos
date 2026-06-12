# Metodología propuesta para aplicar reglas de asociación al análisis de burnout estudiantil

## 1. Propósito del análisis

El objetivo de esta etapa es utilizar **reglas de asociación** para identificar combinaciones de características estudiantiles que aparecen frecuentemente asociadas a niveles altos de burnout. A diferencia del análisis de correlación, que permite observar relaciones entre pares de variables, las reglas de asociación permiten estudiar patrones compuestos, por ejemplo:

```text
sleep_hours=bajo + stress_level=alto -> burnout_cat=alto
```

Esto permite responder preguntas como:

- ¿Qué combinaciones de factores aparecen con mayor frecuencia en estudiantes con burnout alto?
- ¿El bajo sueño se asocia más al burnout cuando aparece junto con estrés alto, dependencia de IA o ansiedad laboral?
- ¿Qué variables aumentan más la probabilidad de observar burnout alto cuando se combinan con otras?
- ¿Existen patrones más informativos que las relaciones individuales entre burnout y una sola variable?

Por lo tanto, el análisis no busca demostrar causalidad, sino encontrar **asociaciones frecuentes e interpretables** dentro del conjunto de datos.

---

## 2. Justificación del uso de reglas de asociación

Las reglas de asociación son adecuadas para este problema porque el burnout estudiantil puede estar relacionado con múltiples dimensiones al mismo tiempo: factores emocionales, hábitos de estudio, uso de herramientas de IA, ansiedad laboral y contexto académico.

En etapas previas del análisis exploratorio se observaron relaciones esperables entre `burnout_score` y variables subjetivas como `stress_level`, `motivation_score`, `placement_anxiety_score` e `interview_anxiety_score`. Sin embargo, analizar solo estas variables puede limitar la interpretación, ya que son factores directamente vinculados a la autopercepción del estudiante.

Por ello, se propone complementar el análisis con variables menos obvias, tales como:

- Horas de sueño.
- Horas de estudio.
- Uso diario de herramientas de IA.
- Dependencia percibida de IA.
- Miedo a perder el trabajo por IA.
- Búsqueda de orientación vocacional o profesional.
- Área de estudio.
- Tipo de institución.
- Experiencia de práctica o internship.

Este enfoque permite observar si el burnout alto aparece asociado a combinaciones de variables subjetivas, conductuales y contextuales.

---

## 3. Pregunta de análisis

La pregunta que guía esta etapa es:

> ¿Qué combinaciones de características estudiantiles se asocian con mayor fuerza a un nivel alto de burnout?

De forma más específica, se busca comparar reglas como:

```text
sleep_hours=bajo + stress_level=alto -> burnout_cat=alto
```

frente a reglas como:

```text
sleep_hours=bajo + fear_of_job_loss_to_ai=alto -> burnout_cat=alto
```

o:

```text
sleep_hours=bajo + motivation_score=alto -> burnout_cat=alto
```

La intención es determinar qué combinaciones presentan mejor soporte, confianza y lift, y cuáles entregan una interpretación más útil para el problema.

---

## 4. Variable objetivo del análisis

Aunque las reglas de asociación no funcionan como un modelo supervisado tradicional, en este caso se creará `burnout_cat` a partir de `burnout_score` y se orientará el análisis hacia reglas cuyo consecuente sea:

```text
burnout_cat=alto
```

Para lograr esto, la variable `burnout_score` debe transformarse desde su escala numérica original a una variable categórica. Una discretización propuesta es:

| Rango de burnout_score | Categoría propuesta |
|---|---|
| 1 a 3 | burnout bajo |
| 4 a 6 | burnout medio |
| 7 a 10 | burnout alto |

El foco del análisis estará en las reglas que tengan como resultado `burnout_cat=alto`, debido a que esta categoría representa el escenario de mayor interés para interpretar factores asociados al agotamiento estudiantil.

---

## 5. Selección inicial de variables

La selección de variables no debe hacerse incluyendo todo el dataset sin criterio. Para que el análisis sea interpretable, se propone agrupar las variables en dimensiones conceptuales.

### 5.1 Variables subjetivas o emocionales

Estas variables reflejan percepción personal del estudiante y se espera que estén directamente relacionadas con burnout.

| Variable | Justificación |
|---|---|
| `stress_level` | Mide nivel de estrés percibido. Es una variable central para explicar burnout. |
| `motivation_score` | Permite observar si la baja motivación aparece asociada al burnout alto. |
| `placement_anxiety_score` | Representa ansiedad frente a la inserción laboral. |
| `interview_anxiety_score` | Representa ansiedad frente a entrevistas laborales. |
| `career_clarity_score` | Permite analizar si la baja claridad profesional se asocia con burnout. |
| `resume_confidence_score` | Permite estudiar si la baja confianza curricular aparece en reglas relevantes. |

### 5.2 Variables relacionadas con inteligencia artificial

Estas variables permiten incorporar el componente tecnológico del dataset y evaluar si el uso o dependencia de IA aparece asociado al burnout.

| Variable | Justificación |
|---|---|
| `daily_ai_tool_usage_hrs` | Mide intensidad de uso diario de herramientas de IA. |
| `uses_ai_for_assignments` | Indica frecuencia de uso de IA para tareas académicas. |
| `ai_replaces_own_thinking_score` | Mide si el estudiante percibe que la IA reemplaza su propio razonamiento. |
| `ai_dependency_score` | Mide nivel de dependencia percibida hacia herramientas de IA. |
| `fear_of_job_loss_to_ai` | Mide preocupación laboral asociada al avance de la IA. |
| `primary_ai_tools_used` | Permite observar patrones asociados al tipo principal de herramienta usada. |

### 5.3 Variables conductuales

Estas variables representan hábitos o comportamientos del estudiante.

| Variable | Justificación |
|---|---|
| `sleep_hours` | Permite analizar si dormir pocas horas se asocia con burnout alto. |
| `daily_study_hours` | Permite observar si una alta carga de estudio se asocia con burnout. |
| `self_learning_hours_per_week` | Representa tiempo adicional de aprendizaje autónomo. |
| `social_media_hrs_per_day` | Permite estudiar el rol del uso de redes sociales. |
| `weekly_job_application_count` | Representa intensidad de búsqueda laboral. |
| `skill_development_courses_taken` | Puede reflejar presión por mejorar empleabilidad. |

### 5.4 Variables contextuales y académicas

Estas variables permiten analizar diferencias por contexto institucional o trayectoria académica.

| Variable | Justificación |
|---|---|
| `gender` | Permite observar diferencias descriptivas por grupo. |
| `degree_type` | Permite comparar tipos de programas académicos. |
| `stream` | Permite observar diferencias por área de estudio. |
| `year_of_study` | Permite analizar si el avance en la carrera se asocia con burnout. |
| `college_tier` | Representa contexto institucional. |
| `urban_or_rural` | Permite observar diferencias contextuales. |
| `internship_experience` | Permite estudiar si la experiencia previa se asocia con menor o mayor burnout. |
| `seeks_career_counseling` | Permite observar si quienes buscan orientación aparecen en reglas asociadas a burnout. |

### 5.5 Variables a excluir o usar con precaución

| Variable | Decisión | Justificación |
|---|---|---|
| `student_id` | Excluir | Es un identificador único y no aporta información analítica. |
| `overall_career_readiness_score` | Usar con precaución | Puede ser una variable compuesta a partir de otras variables del dataset, por lo que podría introducir redundancia. |
| `age` | Opcional | Puede categorizarse, pero no necesariamente es central para la hipótesis del análisis. |

---

## 6. Transformación de variables numéricas a categorías

Las reglas de asociación trabajan mejor con variables categóricas, por lo que las variables numéricas deben discretizarse. Esta transformación convierte valores continuos o escalas numéricas en etiquetas interpretables.

Ejemplo general:

```text
sleep_hours=5.2 -> sleep_hours=bajo
stress_level=8 -> stress_level=alto
motivation_score=2 -> motivation_score=bajo
```

### 6.1 Propuesta de discretización

| Tipo de variable | Criterio propuesto |
|---|---|
| Escalas de 1 a 10 | bajo: 1 a 3, medio: 4 a 6, alto: 7 a 10 |
| Escalas de 1 a 5 | bajo: 1 a 2, medio: 3, alto: 4 a 5 |
| Horas de sueño | bajo: menos de 6, medio: 6 a 8, alto: más de 8 |
| Horas diarias de estudio | bajo: menos de 2, medio: 2 a 5, alto: más de 5 |
| Uso diario de IA | bajo: menos de 1 hora, medio: 1 a 3 horas, alto: más de 3 horas |
| Redes sociales por día | bajo: menos de 2 horas, medio: 2 a 4 horas, alto: más de 4 horas |
| Postulaciones laborales semanales | bajo, medio y alto según distribución o percentiles |
| Variables categóricas originales | Mantener categorías originales, limpiando nombres si es necesario |

Esta discretización debe validarse en el notebook revisando la distribución de cada variable para evitar categorías con muy pocos casos.

---

## 7. Construcción de transacciones

Una vez categorizadas las variables, cada fila del dataset se transformará en una transacción. Cada transacción contiene los atributos categóricos del estudiante.

Ejemplo conceptual:

```text
[
  "sleep_hours=bajo",
  "stress_level=alto",
  "motivation_score=bajo",
  "ai_dependency_score=alto",
  "uses_ai_for_assignments=Frequently",
  "burnout_cat=alto"
]
```

Sobre estas transacciones se aplicará el algoritmo de reglas de asociación para detectar patrones frecuentes.

---

## 8. Tipo de reglas que se buscarán

El análisis se enfocará en reglas donde el consecuente sea únicamente:

```text
burnout_cat=alto
```

Esto permite que la interpretación sea directa. Por ejemplo:

```text
stress_level=alto + motivation_score=bajo -> burnout_cat=alto
```

No se priorizarán reglas cuyo consecuente sea otra variable, como:

```text
stress_level=alto -> motivation_score=bajo
```

Aunque esas reglas pueden ser interesantes, no responden directamente al objetivo principal del análisis.

---

## 9. Métricas de evaluación de reglas

Para evaluar las reglas se utilizarán tres métricas principales: soporte, confianza y lift.

### 9.1 Support

El soporte indica qué proporción del dataset contiene simultáneamente el antecedente y el consecuente de una regla.

Una regla con soporte demasiado bajo puede ser poco confiable, aunque tenga un lift alto.

Ejemplo:

```text
sleep_hours=bajo + stress_level=alto -> burnout_cat=alto
```

Si esta regla aparece en muchos estudiantes, tendrá mayor soporte y será más relevante para el análisis general.

### 9.2 Confidence

La confianza indica qué proporción de los estudiantes que cumplen el antecedente también presentan burnout alto.

Ejemplo:

```text
stress_level=alto -> burnout_cat=alto
```

Una confianza de 0.70 significa que el 70% de los estudiantes con estrés alto tienen burnout alto.

### 9.3 Lift

El lift compara la probabilidad de burnout alto dado el antecedente contra la probabilidad base de burnout alto en todo el dataset.

La interpretación será:

| Valor de lift | Interpretación |
|---|---|
| Menor que 1.00 | Asociación negativa con burnout alto |
| Cercano a 1.00 | Asociación débil o inexistente |
| 1.10 a 1.30 | Asociación débil |
| 1.30 a 1.70 | Asociación moderada |
| 1.70 a 2.00 | Asociación fuerte |
| Mayor que 2.00 | Asociación muy fuerte |

El lift será una métrica clave, porque permite saber si una combinación de variables realmente aumenta la presencia de burnout alto respecto al comportamiento base del dataset.

---

## 10. Criterio para seleccionar reglas relevantes

No todas las reglas generadas serán útiles. Para seleccionar reglas interpretables y relevantes, se propone aplicar los siguientes criterios:

1. El consecuente debe ser `burnout_cat=alto`.
2. El soporte debe superar un umbral mínimo definido en el notebook.
3. La confianza debe ser suficientemente alta para que la regla tenga valor interpretativo.
4. El lift debe ser mayor que 1.3 para considerar que existe una asociación relevante.
5. La regla debe ser interpretable desde el problema de burnout estudiantil.
6. Se deben evitar reglas redundantes o casi idénticas entre sí.
7. Se debe comparar la regla con reglas más simples para verificar si agregar una variable realmente mejora la asociación.

Por ejemplo, no basta con encontrar:

```text
sleep_hours=bajo + stress_level=alto + motivation_score=bajo -> burnout_cat=alto
```

También se debe comparar contra:

```text
sleep_hours=bajo -> burnout_cat=alto
stress_level=alto -> burnout_cat=alto
motivation_score=bajo -> burnout_cat=alto
sleep_hours=bajo + stress_level=alto -> burnout_cat=alto
```

Esto permite saber si la combinación aporta más información que cada variable por separado.

---

## 11. Comparación entre reglas simples y reglas compuestas

El análisis debe distinguir entre reglas simples y reglas compuestas.

### 11.1 Reglas simples

Son reglas con una sola condición en el antecedente:

```text
stress_level=alto -> burnout_cat=alto
```

Estas reglas sirven para identificar variables individuales relevantes.

### 11.2 Reglas compuestas

Son reglas con dos o más condiciones en el antecedente:

```text
sleep_hours=bajo + ai_dependency_score=alto -> burnout_cat=alto
```

Estas reglas permiten observar interacciones entre variables. Son especialmente importantes para este análisis, porque la hipótesis es que el burnout alto puede estar asociado a combinaciones de factores, no solo a variables aisladas.

---

## 12. Algoritmo propuesto

Se propone utilizar **FP-Growth** como algoritmo principal para encontrar itemsets frecuentes y generar reglas de asociación.

### 12.1 Justificación de FP-Growth

FP-Growth es adecuado porque evita generar explícitamente todas las combinaciones candidatas posibles, como ocurre con Apriori. Esto lo vuelve más eficiente cuando el dataset tiene varias variables categóricas y muchas posibles combinaciones.

En este análisis, después de discretizar las variables, cada estudiante tendrá múltiples etiquetas categóricas. Por lo tanto, el número de combinaciones posibles puede crecer rápidamente. FP-Growth permite trabajar de forma más eficiente con este tipo de estructura.

### 12.2 Comparación con otros algoritmos

| Algoritmo | Decisión | Justificación |
|---|---|---|
| Apriori | Alternativa secundaria | Es simple y fácil de explicar, pero puede generar demasiados candidatos. |
| FP-Growth | Algoritmo principal | Es más eficiente para encontrar patrones frecuentes en datasets con muchas variables categóricas. |
| Eclat | No prioritario | Puede ser rápido, pero puede consumir más memoria y no es necesario para el objetivo principal. |

Por tanto, la decisión metodológica propuesta es:

```text
Usar FP-Growth como algoritmo principal y conservar Apriori como alternativa explicativa si se necesita comparar métodos.
```

---

## 13. Flujo metodológico propuesto

El análisis numérico posterior en notebook debería seguir este flujo:

1. Cargar el dataset limpio.
2. Revisar columnas disponibles, tipos de datos y valores faltantes.
3. Seleccionar variables relevantes para reglas de asociación.
4. Excluir identificadores y variables redundantes.
5. Discretizar variables numéricas.
6. Convertir cada fila en una transacción de etiquetas categóricas.
7. Aplicar one-hot encoding sobre las transacciones.
8. Ejecutar FP-Growth para obtener itemsets frecuentes.
9. Generar reglas de asociación.
10. Filtrar reglas cuyo consecuente sea `burnout_cat=alto`.
11. Ordenar reglas por lift, confidence y support.
12. Comparar reglas simples contra reglas compuestas.
13. Interpretar las reglas más relevantes.
14. Seleccionar ejemplos concretos de uso para la presentación.
15. Redactar conclusiones y limitaciones.

---

## 14. Ejemplos de reglas esperadas

El análisis podría producir reglas similares a las siguientes:

```text
stress_level=alto + motivation_score=bajo -> burnout_cat=alto
```

```text
sleep_hours=bajo + ai_dependency_score=alto -> burnout_cat=alto
```

```text
placement_anxiety_score=alto + fear_of_job_loss_to_ai=alto -> burnout_cat=alto
```

```text
daily_ai_tool_usage_hrs=alto + ai_replaces_own_thinking_score=alto -> burnout_cat=alto
```

```text
sleep_hours=bajo + stress_level=alto + motivation_score=bajo -> burnout_cat=alto
```

Estas reglas deberán ser evaluadas numéricamente mediante soporte, confianza y lift antes de concluir que son relevantes.

---

## 15. Interpretación esperada

La interpretación debe centrarse en identificar qué combinaciones aumentan la asociación con burnout alto.

Una posible forma de interpretar una regla sería:

```text
stress_level=alto + motivation_score=bajo -> burnout_cat=alto
```

Si esta regla tiene confianza alta y lift mayor que 1.3, se puede interpretar que los estudiantes con estrés alto y baja motivación presentan una asociación mayor con burnout alto que la esperada por azar o por la frecuencia base del burnout alto en el dataset.

Sin embargo, se debe evitar afirmar causalidad. La interpretación correcta sería:

```text
Existe una asociación entre estrés alto, baja motivación y burnout alto.
```

No sería correcto afirmar:

```text
El estrés alto y la baja motivación causan burnout alto.
```

---

## 16. Limitaciones del enfoque

El análisis con reglas de asociación presenta algunas limitaciones que deben mencionarse:

1. Las reglas muestran asociaciones, no causalidad.
2. Los resultados dependen de cómo se discreticen las variables numéricas.
3. Un lift alto con soporte muy bajo puede representar un patrón poco generalizable.
4. Las variables subjetivas pueden estar fuertemente relacionadas por construcción o autopercepción.
5. Algunas reglas pueden ser redundantes entre sí.
6. El análisis no predice individualmente el burnout, sino que identifica patrones frecuentes asociados a burnout alto.

---

## 17. Criterio de éxito del análisis

El análisis será considerado útil si logra:

- Identificar reglas con buen soporte, confianza y lift.
- Encontrar combinaciones interpretables asociadas a burnout alto.
- Comparar variables subjetivas con variables conductuales, tecnológicas y contextuales.
- Determinar si factores como sueño bajo, dependencia de IA o miedo laboral por IA aumentan su asociación con burnout cuando se combinan con estrés o baja motivación.
- Producir conclusiones respaldadas por métricas y no solo por intuición.

---

## 18. Conclusión metodológica

El análisis de reglas de asociación se plantea como una forma de complementar el análisis exploratorio previo. Mientras la correlación permite observar relaciones individuales entre variables, las reglas de asociación permiten estudiar combinaciones de factores que aparecen frecuentemente junto a burnout alto.

La propuesta es transformar el dataset en transacciones categóricas, aplicar FP-Growth, generar reglas de asociación y filtrar aquellas cuyo consecuente sea `burnout_cat=alto`. Luego, las reglas serán evaluadas mediante support, confidence y lift, priorizando aquellas que tengan buena frecuencia, alta confianza, lift mayor a 1.3 e interpretación coherente con el problema.

Con esto, el análisis permitirá pasar desde una lectura simple de variables individuales hacia una interpretación más completa de patrones asociados al burnout estudiantil.
