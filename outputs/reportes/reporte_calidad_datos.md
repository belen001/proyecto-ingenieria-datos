# Reporte de Calidad de Datos

## Resumen de Variables
| variable                        | dtype   |   num_unique |   num_missing |
|:--------------------------------|:--------|-------------:|--------------:|
| student_id                      | str     |        15000 |             0 |
| age                             | int64   |           11 |             0 |
| gender                          | str     |            3 |             0 |
| degree_type                     | str     |            4 |             0 |
| stream                          | str     |            4 |             0 |
| year_of_study                   | int64   |            4 |             0 |
| college_tier                    | str     |            3 |             0 |
| urban_or_rural                  | str     |            2 |             0 |
| daily_ai_tool_usage_hrs         | float64 |           81 |             0 |
| primary_ai_tools_used           | str     |            5 |          3215 |
| uses_ai_for_assignments         | str     |            5 |             0 |
| ai_replaces_own_thinking_score  | int64   |            5 |             0 |
| ai_dependency_score             | int64   |           10 |             0 |
| placement_anxiety_score         | int64   |           10 |             0 |
| fear_of_job_loss_to_ai          | int64   |            5 |             0 |
| career_clarity_score            | int64   |           10 |             0 |
| internship_experience           | int64   |            5 |             0 |
| weekly_job_application_count    | int64   |           36 |             0 |
| resume_confidence_score         | int64   |            5 |             0 |
| interview_anxiety_score         | int64   |           10 |             0 |
| daily_study_hours               | float64 |           95 |             0 |
| self_learning_hours_per_week    | float64 |          265 |           233 |
| skill_development_courses_taken | int64   |           11 |             0 |
| social_media_hrs_per_day        | float64 |           81 |           210 |
| sleep_hours                     | float64 |           61 |           203 |
| stress_level                    | int64   |           10 |             0 |
| burnout_score                   | int64   |           10 |             0 |
| motivation_score                | int64   |           10 |             0 |
| seeks_career_counseling         | float64 |            2 |           220 |
| overall_career_readiness_score  | float64 |          837 |             0 |

## Valores Nulos
| variable                     |   num_missing |
|:-----------------------------|--------------:|
| primary_ai_tools_used        |          3215 |
| self_learning_hours_per_week |           233 |
| social_media_hrs_per_day     |           210 |
| sleep_hours                  |           203 |
| seeks_career_counseling      |           220 |

## Registros Duplicados
No se encontraron filas duplicadas.

## Revisión de Nombres de Columnas
| original                        | normalized                      |
|:--------------------------------|:--------------------------------|
| student_id                      | student_id                      |
| age                             | age                             |
| gender                          | gender                          |
| degree_type                     | degree_type                     |
| stream                          | stream                          |
| year_of_study                   | year_of_study                   |
| college_tier                    | college_tier                    |
| urban_or_rural                  | urban_or_rural                  |
| daily_ai_tool_usage_hrs         | daily_ai_tool_usage_hrs         |
| primary_ai_tools_used           | primary_ai_tools_used           |
| uses_ai_for_assignments         | uses_ai_for_assignments         |
| ai_replaces_own_thinking_score  | ai_replaces_own_thinking_score  |
| ai_dependency_score             | ai_dependency_score             |
| placement_anxiety_score         | placement_anxiety_score         |
| fear_of_job_loss_to_ai          | fear_of_job_loss_to_ai          |
| career_clarity_score            | career_clarity_score            |
| internship_experience           | internship_experience           |
| weekly_job_application_count    | weekly_job_application_count    |
| resume_confidence_score         | resume_confidence_score         |
| interview_anxiety_score         | interview_anxiety_score         |
| daily_study_hours               | daily_study_hours               |
| self_learning_hours_per_week    | self_learning_hours_per_week    |
| skill_development_courses_taken | skill_development_courses_taken |
| social_media_hrs_per_day        | social_media_hrs_per_day        |
| sleep_hours                     | sleep_hours                     |
| stress_level                    | stress_level                    |
| burnout_score                   | burnout_score                   |
| motivation_score                | motivation_score                |
| seeks_career_counseling         | seeks_career_counseling         |
| overall_career_readiness_score  | overall_career_readiness_score  |

## Significado de Principales Variables
- **student_id** (string): Unique identifier for each student
- **age** (integer): Age of the student (18-28)
- **gender** (categorical): Gender identity
- **degree_type** (categorical): Enrolled degree program level
- **stream** (categorical): Primary academic field of study

## Variable objetivo detectada
La variable objetivo es **overall_career_readiness_score** según el metadata.