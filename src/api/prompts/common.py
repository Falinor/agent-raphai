TABLES_SCHEMA_COMMON_PROMPT = """
### main_marts.marts_common_morphology

| Nom                                      | Type                | Commentaire (français)                                                        |
|-------------------------------------------|---------------------|-------------------------------------------------------------------------------|
| year                                     | INTEGER             | Année                                                                         |
| geo_code                                 | VARCHAR             | Code géographique                                                             |
| city_code                                | VARCHAR             | Code de la commune                                                            |
| count_housing_last_lovac_production      | HUGEINT             | Nombre de logements (dernière production LOVAC)                               |
| count_housing_last_ff_production         | HUGEINT             | Nombre de logements (dernière production FF)                                  |
| count_housing_rented_production          | HUGEINT             | Nombre de logements loués (production)                                        |
| count_housing_vacant_production          | HUGEINT             | Nombre de logements vacants (production)                                      |
| count_housing_energy_sieve_production    | HUGEINT             | Nombre de passoires énergétiques (production)                                 |
| count_vacant_premisses                   | BIGINT              | Nombre de locaux vacants                                                      |
| count_vacant_housing                     | HUGEINT             | Nombre de logements vacants                                                   |
| count_vacant_housing_private             | HUGEINT             | Nombre de logements vacants privés                                            |
| count_vacant_housing_private_fil         | HUGEINT             | Nombre de logements vacants privés (FIL)                                      |
| count_vacant_housing_private_fil_ccthp   | HUGEINT             | Nombre de logements vacants privés (FIL CCTHP)                                |
| count_vacant_housing_private_fil_public  | HUGEINT             | Nombre de logements vacants privés (FIL public)                               |
| sum_living_area_vacant_housing_private_fil_ccthp | DECIMAL(38,3)   | Surface habitable totale des logements vacants privés (FIL CCTHP)             |
| sum_plot_area_vacant_housing_private_fil_ccthp  | DECIMAL(38,3)   | Surface de parcelle totale des logements vacants privés (FIL CCTHP)           |
| count_housing                            | BIGINT              | Nombre total de logements                                                     |
| count_housing_private                    | HUGEINT             | Nombre de logements privés                                                    |
| count_housing_private_rented             | HUGEINT             | Nombre de logements privés loués                                              |
| merged_this_year                         | INTEGER             | Nombre de fusions cette année                                                 |
| split_this_year                          | INTEGER             | Nombre de divisions cette année                                               |
| merged_destionation_geocode              | VARCHAR             | Code géographique de destination fusionnée                                    |
| merged_destination_label                 | VARCHAR             | Libellé de la destination fusionnée                                           |
| split_destination_geocode                | VARCHAR             | Code géographique de destination scindée                                      |
| split_destination_label                  | VARCHAR             | Libellé de la destination scindée                                             |
| city_label                               | VARCHAR             | Libellé de la commune                                                         |
| dep_code                                 | VARCHAR             | Code du département                                                           |
| dep_label                                | VARCHAR             | Libellé du département                                                        |
| region_code                              | INTEGER             | Code de la région                                                             |
| region_label                             | VARCHAR             | Libellé de la région                                                          |
| epci_siren                               | INTEGER             | SIREN de l'EPCI                                                               |
| epci_label                               | VARCHAR             | Libellé de l'EPCI                                                             |

---

### main_marts.marts_common_cities

| Nom                              | Type      | Commentaire (français)                                         |
|-----------------------------------|-----------|----------------------------------------------------------------|
| city_code                        | VARCHAR   | Code de la commune                                             |
| label                            | VARCHAR   | Libellé de la commune                                          |
| department_code                  | VARCHAR   | Code du département                                            |
| region_code                      | INTEGER   | Code de la région                                              |
| tlv1                             | BOOLEAN   | Territoire labellisé 1                                         |
| tlv2                             | BOOLEAN   | Territoire labellisé 2                                         |
| action_coeur_de_ville            | BOOLEAN   | Action Cœur de Ville                                           |
| action_coeur_de_ville_1          | BOOLEAN   | Action Cœur de Ville 1                                         |
| petite_ville_de_demain           | BOOLEAN   | Petite Ville de Demain                                         |
| village_davenir                  | BOOLEAN   | Village d'Avenir                                               |
| opah                             | HUGEINT   | Nombre d'OPAH                                                  |
| type_opah                        | VARCHAR   | Type d'OPAH                                                    |
| pig                              | HUGEINT   | Nombre de PIG                                                  |
| ort_signed                       | BOOLEAN   | ORT signée                                                     |
| ort_signed_at                    | VARCHAR   | Date de signature de l'ORT                                     |
| uu_name                          | VARCHAR   | Nom de l'unité urbaine                                         |
| uu_code                          | VARCHAR   | Code de l'unité urbaine                                        |
| epci_code                        | VARCHAR   | Code de l'EPCI                                                 |
| epci_name                        | VARCHAR   | Nom de l'EPCI                                                  |
| inscrit_zlv_direct               | BOOLEAN   | Inscrit ZLV direct                                             |
| inscrit_zlv_via_intercommunalité | BOOLEAN   | Inscrit ZLV via intercommunalité                               |
| nom_intercommunalité             | VARCHAR   | Nom de l'intercommunalité                                      |
| type_intercommunalité            | VARCHAR   | Type d'intercommunalité                                        |
| couverte_via_service_etat        | BOOLEAN   | Couverte via service de l'État                                 |
| nom_service_etat_departemental   | VARCHAR   | Nom du service de l'État départemental                         |
| nom_service_etat_régional        | VARCHAR   | Nom du service de l'État régional                              |

"""