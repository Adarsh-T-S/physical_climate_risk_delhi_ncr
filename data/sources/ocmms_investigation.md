# OCMMS Asset Dataset Investigation

## Source

OCMMS — Online Consent Management & Monitoring System

## Investigation date

18 August 2026

## Coverage

The publicly accessible OCMMS industry-registration tables provide industrial records by state and district. For Delhi, the 2014–2024 query showed 43,597 industry-registration records across the listed Delhi districts. NCR-relevant records can also be queried for areas such as Gurugram and Faridabad in Haryana. Coverage therefore appears useful for Delhi-NCR industrial analysis, but NCR-wide completeness must be verified across all constituent districts and relevant state pollution-control systems.

## Available fields

Important fields observed in the public industry-detail tables include:

Industry Name

Industry Address

Registration Date

Industry Type

Category

Industry Login ID (where exposed)

Serial Number


Separate application/status views also contain fields such as:

Application Number

Application Type

Application For

Application Submission Date

Application Status


## Geographic information

Industry addresses are provided and can include plot numbers, industrial areas, villages, roads, floors and postal information. Direct latitude/longitude coordinates were not observed in the inspected public industry-detail tables. Coordinates will therefore need to be derived through geocoding or spatial enrichment using sources such as OpenStreetMap and subsequently verified.

## Asset identity

Industry Name provides a documented industry/facility or operator identity and is substantially more useful for asset identification than an anonymous geographic feature. However, the field does not always represent a formal registered company name, and the same industry/company may appear in multiple records. Therefore, Industry Name should not automatically be treated as a unique physical asset identifier.

## Sector and facility information

Industry Type and Category fields are available. Industry Type provides information about the industrial activity, while Category includes regulatory classifications such as White, Green, Orange and Red. These fields provide useful sector and regulatory-context information for asset classification and later vulnerability/exposure analysis.

## Currency / operational status

Registration Date is available and provides a temporal reference for the regulatory record. However, registration date does not establish that a facility is currently operational. Separate OCMMS application/status views provide application status information, but a simple, definitive current-operational-status field was not observed in the main industry-registration table. Current operational status will therefore require additional verification.

## Duplicate / multi-record issue

Multiple records associated with the same industry/company and address were observed. Some entities appear more than once, sometimes with different registration dates or industry types. This indicates that OCMMS records represent regulatory registrations/consent-related records rather than guaranteed unique physical facilities.

## Initial data-quality concerns

One OCMMS record does not necessarily equal one physical asset.

Duplicate and multi-record entries are present.

Direct latitude/longitude coordinates are not provided in the inspected public industry-detail table.

Industry Name does not always represent a formal company/legal entity.

Registration Date does not establish current operational status.

Facility footprint and physical asset boundaries are not provided.

Facility size is not provided in the inspected tables.

NCR-wide completeness requires verification across all relevant NCR districts and states.

Address quality may vary and will affect geocoding accuracy.

Regulatory coverage may not represent every type of commercial/industrial facility.

Public data-access and reuse conditions should be documented before bulk redistribution.


## Implications for the project

OCMMS should not be treated as a ready-made physical asset inventory. Instead, it can serve as a strong facility-candidate and regulatory identity layer. OCMMS records can be deduplicated at the physical-site level, geocoded using their addresses, spatially matched with OpenStreetMap features, and independently verified using satellite imagery or additional authoritative sources. The final asset layer should preserve the original OCMMS identifiers and fields while separately recording enriched coordinates, verification sources and confidence.

## Decision

Modify and supplement OCMMS. Continue using OCMMS as the primary source for facility identity, address, sector/category and regulatory information, while supplementing it with OpenStreetMap/geospatial data for coordinates and physical-location verification. A small sample should be tested before full-scale processing.

## Decision status

Provisional — based on initial dataset inspection.