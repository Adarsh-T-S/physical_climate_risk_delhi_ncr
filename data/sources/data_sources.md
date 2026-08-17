# Data Sources

| Dataset | Variable | Spatial Resolution | Temporal Coverage | Source | Purpose |
|---|---|---|---|---|---|
| TBD | Temperature | TBD | TBD | TBD | Extreme heat |
| TBD | Precipitation | TBD | TBD | TBD | Extreme precipitation |
| TBD | Administrative boundary | TBD | TBD | TBD | Delhi-NCR boundary |
| TBD | Asset locations | TBD | TBD | TBD | Exposure |

## Hazard Data Strategy

The project focuses on two physical climate hazards:

1. Extreme Heat
2. Extreme Precipitation

These were selected because they represent materially different physical climate-risk pathways for commercial and industrial assets in Delhi-NCR.

### Hazard 1 - Extreme Heat

Heat can affect:

- worker health and productivity
- cooling demand
- electricity consumption
- outdoor operations
- equipment performance
- transportation and logistics

The project will therefore investigate extreme rather than average temperature conditions.

## Hazard 2 - Extreme Precipitation

Extreme precipitation can affect:

- surface flooding
- transportation and logistics
- access to facilities
- drainage system
- equipment and inventory
- business continuity

The project will therefore focus on precipitation extremes rather than annual rainfall alone.

## Evidence Hierarchy 

Priority will generally be given to:

1. Government datasets
2. Official scientific institutions
3. Peer-reviewed research
4. International scientific/data institutions
5. Reputable secondary datasets where necessary 

Dataset selection will consider:

- authority
- spatial resolution
- temporal coverage
- methodological transparency
- geographic coverage 
- reproducibility
- accessibility


## Data Requirements for Asset-Level Risk Screening

Before selecting datasets, I defined the minimum information required to connect climate hazards with individual assets in the study area.

| Analysis component | What I need | Spatial requirement | Temporal requirement | Why I need it |
|---|---|---|---|---|
| Extreme heat | Temperature/extreme-heat indicator | Gridded data covering Delhi-NCR | Multi-year | To characterise heat exposure at asset locations |
| Extreme precipitation | Extreme precipitation indicator | Gridded data covering Delhi-NCR | Multi-year | To identify assets exposed to intense precipitation |
| Delhi-NCR boundary | Administrative/geographic boundary | Polygon | Current | To define and consistently clip the study area |
| Asset locations | Verified latitude/longitude coordinates | Point | Current | To link climate hazards to individual assets |
| Vulnerability/context | Asset and surrounding-area characteristics | Point/polygon | Current or appropriate historical period | To distinguish exposure from susceptibility |

## Dataset Selection Criteria

Before using a dataset, I will evaluate:

1. Source authority
2. Spatial resolution
3. Temporal coverage
4. variable definition
5. Geographic coverage
6. Processing requirements
7. Reproducibility
8. Known limitations

## Dataset Evaluation Criteria

Each candidate dataset will be evaluated against the following criteria:

1. Authority and provenance
2. Spatial coverage and resolution
3. Temporal coverage and resolution
4. Variable relevance to the hazard
5. Accessibility and reproducibility
6. Geographic suitability for Delhi-NCR
7. Processing requirements
8. Known limitations

## Candidate Dataset Evaluation

| Component | Candidate dataset/source | Authority | Spatial characteristics | Temporal characteristics | Access/format | Suitability | Decision |
|---|---|---|---|---|---|---|---|
| Extreme heat | To evaluate | To evaluate | To evaluate | To evaluate | To evaluate | To evaluate | Pending |
| Extreme precipitation | To evaluate | To evaluate | To evaluate | To evaluate | To evaluate | To evaluate | Pending |
| Delhi-NCR boundary | To evaluate | To evaluate | To evaluate | Current | To evaluate | To evaluate | Pending |
| Asset locations | To evaluate | To evaluate | Point locations | Current | To evaluate | To evaluate | Pending |


### Extreme Heat - Candidate 1

Candidate: ERA5-Land

Provider: Copernicus Climate Change Service / ECMWF

Potential variables:

2m air temperature

Daily maximum temperature derived from hourly 2m air temperature

Daily minimum temperature derived from hourly 2m air temperature

Related land-surface temperature variables where relevant


Potential strengths:

Long historical record from 1950 to present

High spatial resolution for a global reanalysis dataset (~0.1° × 0.1°, approximately 9 km)

Hourly temporal resolution

Consistent methodology across the study period

Suitable for deriving extreme-heat indicators

Well suited for spatial climate analysis in Python and QGIS

Programmatic access supports a reproducible workflow

Particularly suitable for creating a Delhi-NCR gridded heat-hazard layer


Potential limitations:

Reanalysis rather than direct station observations

~9 km resolution is still insufficient to interpret temperature at individual assets directly

Extreme-heat indicator must be derived/defined

Urban-scale temperature variations may not be fully represented

Processing hourly data can require substantial storage and computation


Status: Candidate — strong candidate for primary extreme-heat hazard analysis; further evaluation required

### Extreme Heat - Candidate 2

Candidate: IMD Daily Gridded Temperature Dataset

Provider: India Meteorological Department (IMD)

Potential variables:

Daily maximum temperature

Daily minimum temperature

Daily mean temperature, where available/relevant


Potential strengths:

Official Indian meteorological dataset

Based on observations from the IMD station network

Long historical record, with daily gridded temperature data available from 1951

Specifically designed for India

Directly relevant to Delhi-NCR

Suitable for calculating observed extreme-temperature statistics

Strong source for validating or benchmarking reanalysis-based results

Useful for establishing the historical observed temperature/extreme-heat signal


Potential limitations:

Coarser spatial resolution (~1° × 1°) than ERA5-Land

Coarse resolution limits fine-scale spatial interpretation within Delhi-NCR

Not suitable by itself for detailed asset-level spatial differentiation

Data processing may require handling IMD-specific binary/grid formats

Extreme-heat indicator must be derived/defined

Current publicly available period should be checked before final analysis because dataset availability may change


Status: Candidate — strong observational benchmark; further evaluation required

### Extreme Heat - Candidate 3

Candidate: ERA5

Provider: Copernicus Climate Change Service / ECMWF

Potential variables:

2m air temperature

Daily maximum temperature derived from hourly 2m air temperature

Daily minimum temperature derived from hourly 2m air temperature

Related atmospheric temperature variables


Potential strengths:

Very long historical record, from 1940 to present

Global spatial coverage

Hourly temporal resolution

0.25° × 0.25° spatial grid

Consistent reanalysis methodology

Suitable for deriving multiple extreme-heat indicators

Widely used in climate and atmospheric research

Strong compatibility with Python-based climate-data processing

Can provide an independent comparison against ERA5-Land and IMD


Potential limitations:

Reanalysis rather than direct station observations

Coarser spatial resolution than ERA5-Land

Resolution limits asset-level interpretation

Extreme-heat indicator must be derived/defined

Model/reanalysis estimates may differ from local station observations

Urban-scale temperature variability may not be fully captured


Status: Candidate — strong independent reanalysis/validation dataset; further evaluation required

### Extreme Precipitation - Candidate 1

Candidate: NASA GPM IMERG V07B

Provider: NASA Global Precipitation Measurement Mission

Potential variables:

Precipitation accumulation

Precipitation rate

Daily precipitation

Sub-daily precipitation


Potential strengths:

Gridded precipitation data at approximately 0.1° spatial resolution

Temporal coverage extending from 1998 to present

Multiple temporal resolutions, including 30-minute and daily products

High spatial resolution relative to many global precipitation datasets

Suitable for deriving extreme precipitation indicators

GIS-compatible GeoTIFF products available

Suitable for spatial precipitation analysis across Delhi-NCR

NASA provides programmatic/data-access options that support reproducible Python workflows


Potential limitations:

Satellite/multisource precipitation estimates rather than purely ground observations

May contain regional and event-specific precipitation biases

~10 km spatial resolution limits direct interpretation at individual asset locations

Extreme precipitation indicator must be derived/defined

Different IMERG processing runs have different characteristics; Final Run should be considered for historical research analysis


Status: Candidate — strong candidate for primary extreme precipitation analysis; further evaluation required

### Extreme Precipitation - Candidate 2

Candidate: IMD Daily Gridded Rainfall

Provider: India Meteorological Department (IMD)

Potential variables:

Daily rainfall/precipitation

Daily precipitation accumulation

Derived extreme rainfall indicators


Potential strengths:

Official Indian meteorological dataset

India-specific observationally based gridded rainfall product

0.25° × 0.25° spatial resolution

Long historical record extending from 1901

Daily temporal resolution

Highly relevant for Delhi-NCR and Indian climate analysis

Suitable for calculating extreme precipitation indices

Strong observational benchmark for satellite and reanalysis datasets

Useful for validating IMERG-derived extreme precipitation results


Potential limitations:

Coarser spatial resolution than IMERG

Gridded observational product may not fully represent local rainfall variability

Data are provided in IMD-specific binary/grid formats, requiring preprocessing

Not suitable for direct interpretation of rainfall at individual assets

Extreme precipitation indicator must be derived/defined

Spatial interpolation and station distribution can influence the gridded rainfall representation


Status: Candidate — strong India-specific observational benchmark; further evaluation required

### Extreme Precipitation - Candidate 3

Candidate: ERA5

Provider: Copernicus Climate Change Service / ECMWF

Potential variables:

Total precipitation

Hourly precipitation

Daily precipitation derived from hourly data

Related precipitation variables


Potential strengths:

Long historical record extending from 1940 to present

Globally consistent reanalysis dataset

0.25° × 0.25° spatial resolution

Hourly temporal resolution

Suitable for deriving daily and extreme precipitation indicators

Strong compatibility with Python and xarray-based workflows

Programmatic access through the Copernicus Climate Data Store

Suitable for independent comparison and validation of IMD and IMERG results

Well established in climate and atmospheric research


Potential limitations:

Reanalysis estimates rather than direct ground observations

Coarser spatial resolution than NASA IMERG

Resolution limits direct asset-level interpretation

Precipitation estimates may differ from local observations, particularly for intense rainfall events

Extreme precipitation indicator must be derived/defined

Processing hourly data requires additional aggregation and storage


Status: Candidate — strong reanalysis and validation dataset; further evaluation required

### Delhi-NCR Boundary

Requirement: A polygon defining the study area consistently across all analyses.

Preferred source: NCR Planning Board (NCRPB) Geo Portal / Government of India

Required checks:

Geographic definition of NCR according to the NCRPB

Currentness of the NCR administrative boundary

Polygon completeness and inclusion of all NCR constituent areas

Coordinate reference system

Availability of downloadable GIS polygon/vector data

GIS format compatibility with Python and QGIS

Licensing/access conditions

Consistency of the boundary with official NCRPB planning documents


Status: Candidate source under evaluation

### Asset Definition

For this screening exercise, an asset refers to a publicly identifiable commercial or industrial facility for which a reasonably reliable geographic location can be established.

The initial asset dataset will be selected based on:
- geographic relevance to Delhi-NCR 
- identifiable facility locations
- publicly documented provenance
- sufficient location accuracy
- reproducibility
- relevance to operational/business exposure

## Dataset Selection Criteria for Asset-Level Screening

Because the objective is to screen physical climate risk for currently identifiable commercial commercial and industrial assets in Delhi-NCR, dataset selection will not prioritize historical length alone.

The primary criteria are:

1. Spatial suitability for distinguishing conditions across the Delhi-NCR study area
2. Temporal resolution appropriate for deriving extreme-event indicators
3. Sufficient historical coverage to characterize the hazard reliably
4. Geographic relevance to Delhi-NCR
5. Data provenance and scientific credibility
6. Reproducibility and accessibility
7. Compatibility with Python and QGIS
8. Suitability for linking the hazard layer to asset locations

For this project, spatial detail and relevance to the asset-screening period may be more important than an unnecessarily long historical record, provided that the selected dataset contains a sufficiently long period for robust hazard characterization.

A long historical record is therefore treated as an advantage, but not as a decisive selection criterion by itself.

### Historical Coverage vs Asset-Relevance

Historical coverage and asset relevance are not identical requirements.

A dataset extending back to the early twentieth century may be valuable for long-term climate analysis, but much of that record may predate the existence or operation of the commercial and industrial assets being screened.

For this project, the historical period should therefore be long enough to characterize extreme hazards while remaining relevant to the modern physical environment and asset-screening objective.

The project will use a common modern analysis period where dataset availability permits, rather than automatically using the maximum historical period available from each dataset.

Historical data may still be retained as a validation or contextual resource where useful.

## Preliminary Dataset Evaluation — Extreme Heat

| Dataset | Spatial resolution | Temporal coverage | Main strength | Main limitation | Role |
|---|---:|---:|---|---|---|
| ERA5-Land | ~9 km | 1950–present | Higher spatial detail with hourly data | Reanalysis; not direct station observation | Primary candidate |
| IMD gridded temperature | 1° | 1951–2024 | India-specific observationally based product | Very coarse for Delhi-NCR spatial differentiation | Benchmark |
| ERA5 | 0.25° | 1940–present | Long, consistent hourly reanalysis | Coarser than ERA5-Land | Secondary comparison |

### Heat-selection reasoning

ERA5-Land is preferred for the primary spatial heat-hazard layer because its approximately 9 km grid provides substantially greater spatial detail than the 1° IMD temperature product and the 0.25° ERA5 product.

The long historical coverage of ERA5 and IMD is valuable for climatological context, but does not outweigh the spatial suitability of ERA5-Land for this asset-screening application.

IMD gridded temperature will be retained as an observationally based benchmark rather than the primary spatial layer.

### Heat Dataset Decision

Primary: ERA5-Land

Benchmark: IMD gridded temperature

Secondary comparison: ERA5

Proposed common analysis period: 2000–2025, subject to final availability and completeness checks.

The final heat indicator will be derived from the selected temperature variable rather than using raw temperature directly as the final hazard score.

## Preliminary Dataset Evaluation — Extreme Precipitation

| Dataset | Spatial resolution | Temporal coverage | Main strength | Main limitation | Role |
|---|---:|---:|---|---|---|
| NASA GPM IMERG V07B | ~10 km / 0.1° | 1998–present | Highest spatial detail among candidates; sub-daily data | Satellite/multisource estimate; potential local biases | Primary candidate |
| IMD gridded rainfall | 0.25° | 1901–2024 | India-specific observationally based product | Coarser spatial resolution than IMERG | Benchmark |
| ERA5 | 0.25° | 1940–present | Consistent hourly reanalysis | Coarser than IMERG; reanalysis precipitation | Secondary comparison |

### Precipitation-selection reasoning

For asset-level screening, NASA GPM IMERG V07B is preferred as the primary precipitation dataset because its approximately 10 km spatial resolution and sub-daily temporal resolution are better suited to identifying spatial differences in extreme precipitation across Delhi-NCR.

The much longer historical record of IMD rainfall is valuable for validation and climatological context, but the additional historical depth is not by itself sufficient reason to prefer it over the finer-resolution IMERG product for the primary screening layer.

### Precipitation Dataset Decision

Primary: NASA GPM IMERG V07B

Benchmark: IMD 0.25° gridded rainfall

Secondary comparison: ERA5

Proposed common analysis period: 2000–2024/2025, subject to final data availability and completeness checks.

The precipitation hazard indicator will be derived from daily or sub-daily precipitation data according to the final extreme-precipitation methodology.

### Boundary Decision Framework

The Delhi-NCR boundary will be selected from the official NCR Planning Board/Government of India source where a usable GIS representation is available.

The boundary will be checked for:

- consistency with the official NCR definition
- currentness
- completeness of constituent areas
- geometry validity
- coordinate reference system
- GIS format compatibility
- reproducibility of access

The selected boundary will be used consistently to clip and analyse all hazard datasets.

## Asset Dataset — Next Evaluation Step

The asset layer is a core component of the physical-risk framework because climate hazards must ultimately be spatially associated with identifiable commercial or industrial assets.

The project will therefore evaluate publicly documented asset datasets alongside the hazard and boundary datasets.

Candidate asset sources will be assessed using:

- facility type
- geographic coverage across Delhi-NCR
- latitude/longitude availability
- location accuracy
- facility identification
- source provenance
- publication/update date
- reproducibility
- relevance to commercial or industrial operations
- ability to distinguish individual facilities

No asset dataset will be selected solely because it contains a large number of facilities.


