TABLES_SCHEMA_JOINS_PROMPT = """
Below are the join tables used in the marts_production schema.

### main_marts.marts_production_join_campaigns_housing

| Name             | Type    | Comment                                      |
|------------------|---------|----------------------------------------------|
| campaign_id      | UUID    | Campaign identifier                          |
| housing_id       | UUID    | Housing identifier                           |
| advice           | VARCHAR | Advice or recommendation                     |
| housing_geo_code | VARCHAR | Geographic code of the housing               |

---

### main_marts.marts_production_join_establishment_cities

| Name             | Type    | Comment                                      |
|------------------|---------|----------------------------------------------|
| establishment_id | VARCHAR | Establishment identifier                     |
| geo_code         | VARCHAR | Geographic code of the city                  |

---

### main_marts.marts_production_join_establishment_housing

| Name             | Type    | Comment                                      |
|------------------|---------|----------------------------------------------|
| establishment_id | VARCHAR | Establishment identifier                     |
| geo_code         | VARCHAR | Geographic code                              |
| id               | UUID    | Housing identifier                           |

---

### main_marts.marts_production_join_housing_groups

| Name             | Type    | Comment                                      |
|------------------|---------|----------------------------------------------|
| group_id         | UUID    | Group identifier                             |
| housing_id       | UUID    | Housing identifier                           |
| housing_geo_code | VARCHAR | Geographic code of the housing               |

---

### main_marts.marts_production_join_owner_housing

| Name             | Type    | Comment                                      |
|------------------|---------|----------------------------------------------|
| owner_id         | UUID    | Owner identifier                             |
| housing_id       | UUID    | Housing identifier                           |
| rank             | INTEGER | Rank of the owner for the housing            |
| start_date       | DATE    | Start date of ownership                      |
| end_date         | DATE    | End date of ownership                        |
| origin           | VARCHAR | Origin of the ownership record               |
| housing_geo_code | VARCHAR | Geographic code of the housing               |
| idprocpte        | VARCHAR | Proprietor process identifier                |
| idprodroit       | VARCHAR | Property right identifier                    |
| locprop_source   | VARCHAR | Source of the property/ownership information |
| property_right   | VARCHAR | Type of property right                       |
"""