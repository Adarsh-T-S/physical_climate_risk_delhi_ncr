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
