# Asset Data Schema

| Field | Description | Required? |
|---|---|---|
| asset_id | Unique identifier assigned by the project | Yes |
| asset_name | Facility/site name | Yes |
| company | Company/organization associated with asset | Preferred |
| sector | Commercial/industrial sector | Yes |
| facility_type | Type of facility | Preferred |
| latitude | Geographic latitude | Yes |
| longitude | Geographic longitude | Yes |
| address | Available physical address | Preferred |
| source | Original data source | Yes |
| source_date | Date/version of source | Yes |
| location_accuracy | Known/estimated positional accuracy | Preferred |
| verification_status | Verification status | Yes |
| notes | Additional information | Optional |

## Asset Universe

The project will screen publicly identifiable commercial and industrial
physical assets located within Delhi-NCR.

The unit of analysis is the individual physical facility/site rather
than the parent company as a whole.

The initial asset universe should prioritise facilities for which:
- geographic location can be established,
- facility identity can be documented,
- commercial/industrial relevance can be established,
- current relevance can be reasonably assessed,
- source provenance can be recorded.

# Asset Dataset Schema

## Purpose

The asset dataset will serve as the exposure layer linking
commercial/industrial facilities in Delhi-NCR with spatial climate
hazard information.

The dataset must contain enough information to establish:

1. what the asset is,
2. where it is,
3. what type of activity it represents,
4. whether it is plausibly operational/current,
5. and how confidently the record can be linked to a physical site.

## Minimum Required Fields

| Field | Requirement | Purpose |
|---|---|---|
| Asset ID | Required | Unique identifier for each physical asset |
| Facility/company name | Required | Asset identification |
| Sector/industry | Required where available | Sector-specific risk interpretation |
| Facility/type/category | Preferred | Understand asset function |
| Address | Required where available | Geographic identification and verification |
| Latitude | Required for spatial analysis | Hazard intersection |
| Longitude | Required for spatial analysis | Hazard intersection |
| Operational/current status | Preferred | Avoid screening inactive/non-existent assets |
| Source record/reference | Required | Provenance and traceability |
| Source date/access date | Required | Establish data currency |
| Coordinate confidence | Required after verification | Quantify location reliability |
| Verification status | Required | Track whether the asset/location was independently checked |

## Data Quality Principle

A record should not be treated as a fully verified asset merely because
it has geographic coordinates.

The final asset layer must distinguish between source records,
geocoded locations and independently verified physical sites.

Field	             Purpose

source_record_id   	 Preserve original OCMMS identity
industry_name	     Facility/operator identity
industry_address	 Original location evidence
registration_date	 Temporal evidence
industry_type	     Sector/activity
category	         Regulatory category
latitude	         Enriched/verified location
longitude	         Enriched/verified location
coordinate_source	 Where coordinates came from
location_confidence	 Reliability of location
duplicate_group_id	 Physical-site reconciliation
operational_status	 Currentness assessment
verification_source	 Independent evidence
verification_status	 Pass/uncertain/exclude
exclusion_reason	 Why a record was rejected