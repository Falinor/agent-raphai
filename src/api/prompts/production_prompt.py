TABLES_SCHEMA_PRODUCTION_PROMPT = """
### Table : main_marts.marts_production_campaigns

| Nom du champ                              | Type                        | Commentaire (français)                                      |
|-------------------------------------------|-----------------------------|-------------------------------------------------------------|
| campaign_id                               | VARCHAR                     | Identifiant de la campagne                                  |
| campaign_id_1                             | UUID                        | Identifiant UUID de la campagne                             |
| id                                        | UUID                        | Identifiant unique                                          |
| campaign_number_deprecated                | INTEGER                     | Numéro de campagne (obsolète)                               |
| start_month_deprecated                    | VARCHAR                     | Mois de début (obsolète)                                    |
| reminder_number_deprecated                | INTEGER                     | Numéro de relance (obsolète)                                |
| filters                                   | VARCHAR                     | Filtres appliqués                                           |
| created_at                                | TIMESTAMP WITH TIME ZONE    | Date de création                                            |
| validated_at                              | TIMESTAMP WITH TIME ZONE    | Date de validation                                          |
| exported_at                               | TIMESTAMP WITH TIME ZONE    | Date d'export                                               |
| sent_at                                   | TIMESTAMP WITH TIME ZONE    | Date d'envoi                                                |
| establishment_id                          | UUID                        | Identifiant de l'établissement                              |
| user_id                                   | UUID                        | Identifiant de l'utilisateur                                |
| recovery_id                               | VARCHAR                     | Identifiant de récupération                                 |
| kind_deprecated                           | INTEGER                     | Type de campagne (obsolète)                                 |
| title                                     | VARCHAR                     | Titre de la campagne                                        |
| archived_at                               | TIMESTAMP WITH TIME ZONE    | Date d'archivage                                            |
| confirmed_at                              | TIMESTAMP WITH TIME ZONE    | Date de confirmation                                        |
| group_id                                  | UUID                        | Identifiant du groupe                                       |
| status                                    | VARCHAR                     | Statut de la campagne                                       |
| file                                      | VARCHAR                     | Fichier associé                                             |
| description                               | VARCHAR                     | Description                                                 |
| is_validated                              | INTEGER                     | Validée (1 = oui, 0 = non)                                  |
| is_confirmed                              | INTEGER                     | Confirmée (1 = oui, 0 = non)                                |
| is_sent                                   | INTEGER                     | Envoyée (1 = oui, 0 = non)                                  |
| is_creation_gt_30_days                    | INTEGER                     | Création > 30 jours (1 = oui, 0 = non)                      |
| is_creation_lt_30_days                    | INTEGER                     | Création < 30 jours (1 = oui, 0 = non)                      |
| next_campaign_sent_at                     | TIMESTAMP WITH TIME ZONE    | Date d'envoi de la prochaine campagne                       |
| time_to_next_campaign                     | INTERVAL                    | Temps jusqu'à la prochaine campagne                         |
| housing_number_in_campaign                | BIGINT                      | Nombre de logements dans la campagne                        |
| return_count_3_months                     | BIGINT                      | Nombre de retours à 3 mois                                  |
| return_rate_3_months                      | DOUBLE                      | Taux de retour à 3 mois                                     |
| has_next_campaign_in_3_months             | INTEGER                     | Prochaine campagne dans 3 mois (1 = oui, 0 = non)           |
| return_count_3_months_before_next_campaign| BIGINT                      | Retours 3 mois avant prochaine campagne                     |
| return_rate_3_months_before_next_campaign | DOUBLE                      | Taux de retour 3 mois avant prochaine campagne              |
| return_count_6_months                     | BIGINT                      | Nombre de retours à 6 mois                                  |
| return_rate_6_months                      | DOUBLE                      | Taux de retour à 6 mois                                     |
| has_next_campaign_in_6_months             | INTEGER                     | Prochaine campagne dans 6 mois (1 = oui, 0 = non)           |
| return_count_6_months_before_next_campaign| BIGINT                      | Retours 6 mois avant prochaine campagne                     |
| return_rate_6_months_before_next_campaign | DOUBLE                      | Taux de retour 6 mois avant prochaine campagne              |
| return_count_9_months                     | BIGINT                      | Nombre de retours à 9 mois                                  |
| return_rate_9_months                      | DOUBLE                      | Taux de retour à 9 mois                                     |
| has_next_campaign_in_9_months             | INTEGER                     | Prochaine campagne dans 9 mois (1 = oui, 0 = non)           |
| return_count_9_months_before_next_campaign| BIGINT                      | Retours 9 mois avant prochaine campagne                     |
| return_rate_9_months_before_next_campaign | DOUBLE                      | Taux de retour 9 mois avant prochaine campagne              |
| return_count_36_months                    | BIGINT                      | Nombre de retours à 36 mois                                 |
| return_rate_36_months                     | DOUBLE                      | Taux de retour à 36 mois                                    |
| has_next_campaign_in_36_months            | INTEGER                     | Prochaine campagne dans 36 mois (1 = oui, 0 = non)          |
| return_count_36_months_before_next_campaign| BIGINT                     | Retours 36 mois avant prochaine campagne                    |
| return_rate_36_months_before_next_campaign| DOUBLE                      | Taux de retour 36 mois avant prochaine campagne             |
| first_event_global_date                   | TIMESTAMP WITH TIME ZONE    | Date du premier événement global                            |
| last_event_global_date                    | TIMESTAMP WITH TIME ZONE    | Date du dernier événement global                            |
| first_event_followup_date                 | TIMESTAMP WITH TIME ZONE    | Date du premier suivi                                       |
| last_event_followup_date                  | TIMESTAMP WITH TIME ZONE    | Date du dernier suivi                                       |
| first_event_ownership_date                | TIMESTAMP WITH TIME ZONE    | Date du premier événement de propriété                      |
| last_event_ownership_date                 | TIMESTAMP WITH TIME ZONE    | Date du dernier événement de propriété                      |

---

### Table : main_marts.marts_production_establishments

| Nom du champ                              | Type                        | Commentaire (français)                                      |
|-------------------------------------------|-----------------------------|-------------------------------------------------------------|
| establishment_id                          | VARCHAR                     | Identifiant de l'établissement                              |
| id                                       | UUID                        | Identifiant unique                                          |
| siren                                    | INTEGER                     | Numéro SIREN                                                |
| name                                     | VARCHAR                     | Nom de l'établissement                                      |
| available                                | BOOLEAN                     | Disponible                                                  |
| localities_geo_code                      | VARCHAR[]                   | Codes géographiques des localités                           |
| kind                                     | VARCHAR                     | Type d'établissement                                        |
| updated_at                               | TIMESTAMP WITH TIME ZONE    | Date de mise à jour                                         |
| source                                   | VARCHAR                     | Source                                                      |
| establishment_kind_label                  | VARCHAR                     | Libellé du type d'établissement                             |
| establishment_synthetic_type_label        | VARCHAR                     | Libellé du type synthétique                                 |
| covered_by_state_service                  | BOOLEAN                     | Couvert par un service de l'État                            |
| establishment_id_1                        | UUID                        | Identifiant supplémentaire                                  |
| user_ids                                 | VARCHAR                     | Identifiants des utilisateurs                               |
| user_emails                              | VARCHAR                     | Emails des utilisateurs                                     |
| user_number                              | BIGINT                      | Nombre d'utilisateurs                                       |
| last_activated_at                        | TIMESTAMP WITH TIME ZONE    | Dernière activation                                         |
| first_activated_at                       | TIMESTAMP WITH TIME ZONE    | Première activation                                         |
| last_authenticated_at                    | TIMESTAMP WITH TIME ZONE    | Dernière authentification                                   |
| connected_last_30_days                   | BOOLEAN                     | Connecté dans les 30 derniers jours                         |
| connected_last_60_days                   | BOOLEAN                     | Connecté dans les 60 derniers jours                         |
| connected_last_90_days                   | BOOLEAN                     | Connecté dans les 90 derniers jours                         |
| establishment_id_2                        | UUID                        | Identifiant supplémentaire                                  |
| has_campaigns                            | BOOLEAN                     | A des campagnes                                             |
| total_campaigns                          | BIGINT                      | Nombre total de campagnes                                   |
| total_sent_campaigns                     | HUGEINT                     | Nombre total de campagnes envoyées                          |
| total_exported_campaigns                 | HUGEINT                     | Nombre total de campagnes exportées                         |
| last_campaign_created                    | TIMESTAMP WITH TIME ZONE    | Date de création de la dernière campagne                    |
| first_campaign_created                   | TIMESTAMP WITH TIME ZONE    | Date de création de la première campagne                    |
| is_creation_gt_30_days                   | INTEGER                     | Création > 30 jours (1 = oui, 0 = non)                      |
| is_creation_lt_30_days                   | INTEGER                     | Création < 30 jours (1 = oui, 0 = non)                      |
| establishment_id_3                        | UUID                        | Identifiant supplémentaire                                  |
| has_groups                               | BOOLEAN                     | A des groupes                                               |
| total_groups                             | BIGINT                      | Nombre total de groupes                                     |
| total_exported_groups                    | HUGEINT                     | Nombre total de groupes exportés                            |
| last_group_created                       | TIMESTAMP WITH TIME ZONE    | Date de création du dernier groupe                          |
| first_group_created                      | TIMESTAMP WITH TIME ZONE    | Date de création du premier groupe                          |
| establishment_id_4                        | UUID                        | Identifiant supplémentaire                                  |
| has_perimeters                           | BOOLEAN                     | A des périmètres                                            |
| total_perimeters                         | BIGINT                      | Nombre total de périmètres                                  |
| total_shapes                             | BIGINT                      | Nombre total de formes                                      |
| total_kinds                              | BIGINT                      | Nombre total de types                                       |
| establishment_id_5                        | UUID                        | Identifiant supplémentaire                                  |
| contacted_housing_2020                   | HUGEINT                     | Logements contactés en 2020                                 |
| contacted_housing_2021                   | HUGEINT                     | Logements contactés en 2021                                 |
| contacted_housing_2022                   | HUGEINT                     | Logements contactés en 2022                                 |
| contacted_housing_2023                   | HUGEINT                     | Logements contactés en 2023                                 |
| contacted_housing_2024                   | HUGEINT                     | Logements contactés en 2024                                 |
| contacted_housing_2025                   | HUGEINT                     | Logements contactés en 2025                                 |
| contacts_number_2020                     | HUGEINT                     | Nombre de contacts en 2020                                  |
| contacts_number_2021                     | HUGEINT                     | Nombre de contacts en 2021                                  |
| contacts_number_2022                     | HUGEINT                     | Nombre de contacts en 2022                                  |
| contacts_number_2023                     | HUGEINT                     | Nombre de contacts en 2023                                  |
| contacts_number_2024                     | HUGEINT                     | Nombre de contacts en 2024                                  |
| contacts_number_2025                     | HUGEINT                     | Nombre de contacts en 2025                                  |
| contacted_housing_followup_ended_2020    | HUGEINT                     | Suivis terminés en 2020                                     |
| contacted_housing_followup_ended_2021    | HUGEINT                     | Suivis terminés en 2021                                     |
| contacted_housing_followup_ended_2022    | HUGEINT                     | Suivis terminés en 2022                                     |
| contacted_housing_followup_ended_2023    | HUGEINT                     | Suivis terminés en 2023                                     |
| contacted_housing_followup_ended_2024    | HUGEINT                     | Suivis terminés en 2024                                     |
| contacted_housing_followup_ended_2025    | HUGEINT                     | Suivis terminés en 2025                                     |
| contacted_housing_followup_ended_not_vacant_2020 | HUGEINT              | Suivis terminés non vacants en 2020                         |
| contacted_housing_followup_ended_not_vacant_2021 | HUGEINT              | Suivis terminés non vacants en 2021                         |
| contacted_housing_followup_ended_not_vacant_2022 | HUGEINT              | Suivis terminés non vacants en 2022                         |
| contacted_housing_followup_ended_not_vacant_2023 | HUGEINT              | Suivis terminés non vacants en 2023                         |
| contacted_housing_followup_ended_not_vacant_2024 | HUGEINT              | Suivis terminés non vacants en 2024                         |
| contacted_housing_followup_ended_not_vacant_2025 | HUGEINT              | Suivis terminés non vacants en 2025                         |
| establishment_id_6                        | UUID                        | Identifiant supplémentaire                                  |
| last_event_status_user_followup           | INTEGER                     | Statut du dernier suivi utilisateur                         |
| last_event_status_label_user_followup     | VARCHAR                     | Libellé du dernier suivi utilisateur                        |
| last_event_date_user_followup             | TIMESTAMP WITH TIME ZONE    | Date du dernier suivi utilisateur                           |
| last_event_sub_status_label_user_followup | VARCHAR                     | Libellé du sous-statut du dernier suivi utilisateur         |
| last_event_occupancy_user_occupancy       | VARCHAR                     | Dernière occupation utilisateur                             |
| last_event_date_user_occupancy            | TIMESTAMP WITH TIME ZONE    | Date de la dernière occupation utilisateur                  |

---

### Table : main_marts.marts_production_housing

| Nom du champ                              | Type                        | Commentaire (français)                                      |
|-------------------------------------------|-----------------------------|-------------------------------------------------------------|
| housing_id                                | VARCHAR                     | Identifiant du logement                                     |
| id                                       | UUID                        | Identifiant unique                                          |
| invariant                                | VARCHAR                     | Invariant                                                   |
| local_id                                 | VARCHAR                     | Identifiant local                                           |
| building_id                              | VARCHAR                     | Identifiant du bâtiment                                     |
| geo_code                                 | VARCHAR                     | Code géographique                                           |
| cadastral_classification                 | INTEGER                     | Classification cadastrale                                   |
| uncomfortable                            | BOOLEAN                     | Inconfortable                                               |
| vacancy_start_year                       | INTEGER                     | Année de début de vacance                                   |
| housing_kind                             | VARCHAR                     | Type de logement                                            |
| rooms_count                              | INTEGER                     | Nombre de pièces                                            |
| living_area                              | INTEGER                     | Surface habitable                                           |
| cadastral_reference                      | VARCHAR                     | Référence cadastrale                                        |
| building_year                            | INTEGER                     | Année de construction                                       |
| mutation_date                            | DATE                        | Date de mutation                                            |
| taxed                                    | BOOLEAN                     | Imposable                                                   |
| data_years                               | INTEGER[]                   | Années de données                                           |
| beneficiary_count                        | INTEGER                     | Nombre de bénéficiaires                                     |
| building_location                        | VARCHAR                     | Localisation du bâtiment                                    |
| rental_value                             | INTEGER                     | Valeur locative                                             |
| condominium                              | VARCHAR                     | Copropriété                                                 |
| status                                   | INTEGER                     | Statut                                                      |
| sub_status                               | VARCHAR                     | Sous-statut                                                 |
| energy_consumption_bdnb                   | VARCHAR                     | Consommation énergétique BDNB                               |
| occupancy_source                         | VARCHAR                     | Source de l'occupation                                      |
| occupancy                                | VARCHAR                     | Occupation                                                  |
| occupancy_intended                       | VARCHAR                     | Occupation prévue                                           |
| plot_id                                  | VARCHAR                     | Identifiant de la parcelle                                  |
| energy_consumption_at_bdnb                | TIMESTAMP WITH TIME ZONE    | Date de la consommation énergétique BDNB                    |
| building_group_id                        | VARCHAR                     | Identifiant du groupe de bâtiments                          |
| data_source                              | VARCHAR                     | Source des données                                          |
| data_file_years                          | VARCHAR[]                   | Années des fichiers de données                              |
| geolocation                              | VARCHAR                     | Géolocalisation                                             |
| plot_area                                | INTEGER                     | Surface de la parcelle                                      |
| last_mutation_date                       | TIMESTAMP WITH TIME ZONE    | Date de la dernière mutation                                |
| last_transaction_date                    | TIMESTAMP WITH TIME ZONE    | Date de la dernière transaction                             |
| last_transaction_value                   | INTEGER                     | Valeur de la dernière transaction                           |
| occupancy_history                        | VARCHAR                     | Historique d'occupation                                     |
| city_code                                | VARCHAR                     | Code de la ville                                            |
| last_event_status_zlv_followup           | INTEGER                     | Statut du dernier suivi ZLV                                 |
| last_event_status_label_zlv_followup     | VARCHAR                     | Libellé du dernier suivi ZLV                                |
| last_event_date_zlv_followup             | TIMESTAMP WITH TIME ZONE    | Date du dernier suivi ZLV                                   |
| last_event_status_user_followup          | INTEGER                     | Statut du dernier suivi utilisateur                        |
| last_event_status_label_user_followup    | VARCHAR                     | Libellé du dernier suivi utilisateur                       |
| last_event_date_user_followup            | TIMESTAMP WITH TIME ZONE    | Date du dernier suivi utilisateur                          |
| last_event_status_followup               | INTEGER                     | Statut du dernier suivi                                    |
| last_event_status_label_followup         | VARCHAR                     | Libellé du dernier suivi                                   |
| last_event_date_followup                 | TIMESTAMP WITH TIME ZONE    | Date du dernier suivi                                      |
| last_event_status_zlv_occupancy          | INTEGER                     | Statut de la dernière occupation ZLV                       |
| last_event_status_label_zlv_occupancy    | VARCHAR                     | Libellé de la dernière occupation ZLV                      |
| last_event_date_zlv_occupancy            | TIMESTAMP WITH TIME ZONE    | Date de la dernière occupation ZLV                         |
| last_event_status_user_occupancy         | INTEGER                     | Statut de la dernière occupation utilisateur               |
| last_event_status_label_user_occupancy   | VARCHAR                     | Libellé de la dernière occupation utilisateur              |
| last_event_date_user_occupancy           | TIMESTAMP WITH TIME ZONE    | Date de la dernière occupation utilisateur                 |
| last_event_status_occupancy              | INTEGER                     | Statut de la dernière occupation                           |
| last_event_status_label_occupancy        | VARCHAR                     | Libellé de la dernière occupation                          |
| last_event_date_occupancy                | TIMESTAMP WITH TIME ZONE    | Date de la dernière occupation                             |
| energy_sieve                             | BOOLEAN                     | Passoire énergétique                                        |
| vacant_two_years                         | BOOLEAN                     | Vacant depuis deux ans                                      |
| is_in_opah_teritory                      | BOOLEAN                     | Situé en territoire OPAH                                    |
| is_in_tlv1_teritory                      | BOOLEAN                     | Situé en territoire TLV1                                    |
| is_in_tlv2_teritory                      | BOOLEAN                     | Situé en territoire TLV2                                    |
| is_in_action_coeur_de_ville_teritory     | BOOLEAN                     | Situé en territoire Action Cœur de Ville                    |
| is_in_action_coeur_de_ville_1_teritory   | BOOLEAN                     | Situé en territoire Action Cœur de Ville 1                  |
| is_in_petite_ville_de_demain_teritory    | BOOLEAN                     | Situé en territoire Petite Ville de Demain                  |
| is_in_village_davenir_teritory           | BOOLEAN                     | Situé en territoire Village d'Avenir                        |
| label                                    | VARCHAR                     | Libellé                                                     |
| housing_id_1                             | UUID                        | Identifiant supplémentaire                                 |
| first_campaign_created                   | TIMESTAMP WITH TIME ZONE    | Date de création de la première campagne                    |
| last_campaign_created                    | TIMESTAMP WITH TIME ZONE    | Date de création de la dernière campagne                    |
| first_campaign_sent                      | TIMESTAMP WITH TIME ZONE    | Date d'envoi de la première campagne                        |
| last_campaign_sent                       | TIMESTAMP WITH TIME ZONE    | Date d'envoi de la dernière campagne                        |
| total_validated                          | HUGEINT                     | Nombre total de validations                                 |
| total_confirmed                          | HUGEINT                     | Nombre total de confirmations                               |
| total_sent                               | HUGEINT                     | Nombre total d'envois                                       |
| housing_id_2                             | UUID                        | Identifiant supplémentaire                                 |
| total_groups                             | BIGINT                      | Nombre total de groupes                                     |
| group_titles                             | VARCHAR                     | Titres des groupes                                          |
| first_group_created                      | TIMESTAMP WITH TIME ZONE    | Date de création du premier groupe                          |
| last_group_created                       | TIMESTAMP WITH TIME ZONE    | Date de création du dernier groupe                          |
| first_group_exported                     | TIMESTAMP WITH TIME ZONE    | Date d'export du premier groupe                             |
| last_group_exported                      | TIMESTAMP WITH TIME ZONE    | Date d'export du dernier groupe                             |
| establishment_ids                        | VARCHAR                     | Identifiants des établissements                             |
| establishment_ids_array                  | UUID[]                      | Tableau des identifiants d'établissements                   |
| is_on_user_teritory                      | BOOLEAN                     | Sur le territoire de l'utilisateur                          |

---

### Table : main_marts.marts_production_owners

| Nom du champ                              | Type                        | Commentaire (français)                                      |
|-------------------------------------------|-----------------------------|-------------------------------------------------------------|
| owner_id                                  | VARCHAR                     | Identifiant du propriétaire                                 |
| id                                       | UUID                        | Identifiant unique                                          |
| administrator                            | VARCHAR                     | Administrateur                                              |
| kind_class                               | VARCHAR                     | Classe de type                                              |
| owner_kind_detail                        | VARCHAR                     | Détail du type de propriétaire                              |
| email                                    | VARCHAR                     | Email                                                       |
| phone                                    | VARCHAR                     | Téléphone                                                   |
| idpersonne                               | VARCHAR                     | Identifiant personne                                        |
| siren                                    | VARCHAR                     | Numéro SIREN                                                |
| data_source                              | VARCHAR                     | Source des données                                          |
| created_at                               | TIMESTAMP WITH TIME ZONE    | Date de création                                            |
| updated_at                               | TIMESTAMP WITH TIME ZONE    | Date de mise à jour                                         |
| entity                                   | VARCHAR                     | Entité                                                      |
| postal_code                              | VARCHAR                     | Code postal                                                 |
| city                                     | VARCHAR                     | Ville                                                       |
"""