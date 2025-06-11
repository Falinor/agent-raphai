TABLES_SCHEMA_ESTABLISHMENT_PROMPT = """# Table : main_marts.marts_public_establishments_morphology_unpivoted

| Nom                       | Type            | Commentaire (français)                                               |
|---------------------------|-----------------|----------------------------------------------------------------------|
| establishment_id          | VARCHAR         | Identifiant de l'établissement                                      |
| count_type                | VARCHAR         | Type de comptage                                                    |
| count_label               | VARCHAR         | Libellé du comptage                                                 |
| "2019"                    | DECIMAL(38,3)   | Valeur pour l'année 2019                                            |
| "2020"                    | DECIMAL(38,3)   | Valeur pour l'année 2020                                            |
| "2021"                    | DECIMAL(38,3)   | Valeur pour l'année 2021                                            |
| "2022"                    | DECIMAL(38,3)   | Valeur pour l'année 2022                                            |
| "2023"                    | DECIMAL(38,3)   | Valeur pour l'année 2023                                            |
| "2024"                    | DECIMAL(38,3)   | Valeur pour l'année 2024                                            |
| "2025"                    | DECIMAL(38,3)   | Valeur pour l'année 2025                                            |
| var_2025_2024             | DECIMAL(38,3)   | Variation brute 2025 vs 2024                                        |
| var_pct_2025_2024         | DOUBLE          | Variation en % 2025 vs 2024                                         |
| var_2024_2023             | DECIMAL(38,3)   | Variation brute 2024 vs 2023                                        |
| var_pct_2024_2023         | DOUBLE          | Variation en % 2024 vs 2023                                         |
| var_2023_2022             | DECIMAL(38,3)   | Variation brute 2023 vs 2022                                        |
| var_pct_2023_2022         | DOUBLE          | Variation en % 2023 vs 2022                                         |
| var_2022_2021             | DECIMAL(38,3)   | Variation brute 2022 vs 2021                                        |
| var_pct_2022_2021         | DOUBLE          | Variation en % 2022 vs 2021                                         |
| var_2021_2020             | DECIMAL(38,3)   | Variation brute 2021 vs 2020                                        |
| var_pct_2021_2020         | DOUBLE          | Variation en % 2021 vs 2020                                         |
| var_2020_2019             | DECIMAL(38,3)   | Variation brute 2020 vs 2019                                        |
| var_pct_2020_2019         | DOUBLE          | Variation en % 2020 vs 2019                                         |

---

# Table : main_marts.marts_public_establishments_hierarchy

| Nom             | Type    | Commentaire (français)                                 |
|-----------------|---------|-------------------------------------------------------|
| ancestor_id     | UUID    | Identifiant de l'ancêtre                              |
| descendant_id   | UUID    | Identifiant du descendant                             |
| ancestor_type   | VARCHAR | Type d'entité ancêtre                                 |
| descendant_type | VARCHAR | Type d'entité descendante                             |
| depth           | INTEGER | Profondeur de la relation hiérarchique                |

---

# Table : main_marts.marts_public_establishments_morphology_catagorized

| Nom                                         | Type          | Commentaire (français)                                                        |
|----------------------------------------------|---------------|-------------------------------------------------------------------------------|
| establishment_id                            | VARCHAR       | Identifiant de l'établissement                                                |
| establishment_kind                          | VARCHAR       | Type d'établissement                                                          |
| establishment_echelon                       | INTEGER       | Échelon de l'établissement                                                    |
| data_year                                   | INTEGER       | Année de la donnée                                                            |
| count_vacant_housing_private_fil_ccthp      | HUGEINT       | Nombre de logements vacants privés FIL CCTHP                                  |
| housing_vacant_rate                         | FLOAT         | Taux de vacance des logements                                                 |
| housing_vacant_compared_2024                | DOUBLE        | Différence du nombre de logements vacants par rapport à 2024                  |
| housing_vacant_rate_compared_2024           | FLOAT         | Différence du taux de vacance par rapport à 2024                              |
| housing_vacant_compared_same_as_2024        | DOUBLE        | Différence du nombre de logements vacants par rapport à la même entité en 2024|
| housing_vacant_rate_compared_same_as_2024   | FLOAT         | Différence du taux de vacance par rapport à la même entité en 2024            |
| kind_housing_vacant_2024                    | VARCHAR       | Catégorie du nombre de logements vacants en 2024                              |
| kind_housing_vacant_same_as_2024            | VARCHAR       | Catégorie du nombre de logements vacants pour la même entité en 2024          |
| kind_housing_vacant_rate_2024               | VARCHAR       | Catégorie du taux de vacance en 2024                                          |
| kind_housing_vacant_rate_same_as_2024       | VARCHAR       | Catégorie du taux de vacance pour la même entité en 2024                      |
| housing_vacant_evolution_19_24              | HUGEINT       | Évolution du nombre de logements vacants 2019-2024                            |
| housing_vacant_rate_evolution_19_24         | FLOAT         | Évolution du taux de vacance 2019-2024                                        |
| housing_vacant_evolution_23_24              | HUGEINT       | Évolution du nombre de logements vacants 2023-2024                            |
| housing_vacant_rate_evolution_23_24         | FLOAT         | Évolution du taux de vacance 2023-2024                                        |
| housing_vacant_evolution_compared_19_24     | DOUBLE        | Différence d'évolution du nombre de logements vacants 2019-2024               |
| housing_vacant_rate_evolution_compared_19_24| FLOAT         | Différence d'évolution du taux de vacance 2019-2024                           |
| housing_vacant_evolution_compared_same_as_19_24     | DOUBLE  | Différence d'évolution du nombre de logements vacants pour la même entité 2019-2024 |
| housing_vacant_rate_evolution_compared_same_as_19_24| FLOAT   | Différence d'évolution du taux de vacance pour la même entité 2019-2024       |
| kind_housing_vacant_evolution_19_24         | VARCHAR       | Catégorie d'évolution du nombre de logements vacants 2019-2024                |
| kind_housing_vacant_rate_evolution_19_24    | VARCHAR       | Catégorie d'évolution du taux de vacance 2019-2024                            |
| kind_housing_vacant_evolution_same_as_19_24 | VARCHAR       | Catégorie d'évolution du nombre de logements vacants pour la même entité 2019-2024 |
| kind_housing_vacant_rate_evolution_same_as_19_24 | VARCHAR   | Catégorie d'évolution du taux de vacance pour la même entité 2019-2024        |

---

# Table : main_marts.marts_public_establishments_morphology

| Nom                                         | Type            | Commentaire (français)                                         |
|----------------------------------------------|-----------------|----------------------------------------------------------------|
| establishment_id                            | VARCHAR         | Identifiant de l'établissement                                 |
| year                                        | INTEGER         | Année                                                          |
| count_vacant_premisses                      | HUGEINT         | Nombre de locaux vacants                                       |
| count_vacant_housing                        | HUGEINT         | Nombre de logements vacants                                    |
| count_vacant_housing_private                | HUGEINT         | Nombre de logements vacants privés                             |
| count_vacant_housing_private_fil            | HUGEINT         | Nombre de logements vacants privés FIL                         |
| count_vacant_housing_private_fil_public     | HUGEINT         | Nombre de logements vacants privés FIL public                  |
| count_vacant_housing_private_fil_ccthp      | HUGEINT         | Nombre de logements vacants privés FIL CCTHP                   |
| count_housing                               | HUGEINT         | Nombre total de logements                                      |
| count_housing_private                       | HUGEINT         | Nombre de logements privés                                     |
| count_housing_private_rented                | HUGEINT         | Nombre de logements privés loués                               |
| count_housing_last_lovac_production         | HUGEINT         | Nombre de logements (dernière production LOVAC)                |
| count_housing_last_ff_production            | HUGEINT         | Nombre de logements (dernière production FF)                   |
| count_housing_rented_production             | HUGEINT         | Nombre de logements loués (production)                         |
| count_housing_vacant_production             | HUGEINT         | Nombre de logements vacants (production)                       |
| count_housing_energy_sieve_production       | HUGEINT         | Nombre de passoires énergétiques (production)                  |
| sum_living_area_vacant_housing_private_fil_ccthp | DECIMAL(38,3) | Surface habitable totale des logements vacants privés FIL CCTHP|
| sum_plot_area_vacant_housing_private_fil_ccthp  | DECIMAL(38,3) | Surface de parcelle totale des logements vacants privés FIL CCTHP|"""