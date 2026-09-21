# Methodology

## 1 Conceptual Risk Framework

This project follows the conceptual structure:

Hazard + Exposure + Vulnerability > Risk

### Hazard

The climate-related physical event or condition that may cause harm.

Examples: 
- extreme heat
- extreme precipitation

### Exposure

The presence of people, assets, infrastructure or economic activity in locations affected by a hazard.

In this project, exposure refers primarily to the geographic location of selected commercial and industrial assets.

### Vulnerability

The degree to which an exposed asset or operation may be susceptible to harm.

### Risk

The potential for adverse consequences resulting from the interaction of hazard, exposure and vulnerability.

## Scope and Limitations

This project is designed as a relative physical climate-risk screening framework rather than a detailed financial-loss or engineering risk model.

It does not estimate:
- asset-specific monetary losses
- insurance losses
- credit default probabilities
- precise business interuption costs
- engineering failure probabilities
- regulatory climate-risk metrics

The analysis is limited by the availability and spatial resolution of publicly accessible climate, geospatial and asset-level data.

## Hazard Components

The initial version of the framework will assess two physical climate hazards:
1. Extreme heat
2. Extreme precipitation

### Extreme Heat

Heat exposure will be represented using an appropriate climate indicator derived from authoritative temperature data.

### Extreme Precipitation

Precipitation exposure will be represented using an appropriate extreme-rainfall indicator derived from authoritative precipitation data.

## Exposure 

Exposure will be represented through the geographic locations of selected publicly identifiable commercial and industrial assets.

Potential asset categories include:

- manufacturing facilities
- warehouses
- logistics facilities
- large commercial facilities
- other identifiable
business-critical sites

The selected assets will be treated as a methodological sample and will not be presented as representative of the entire commercial or industrial asset base of Delhi-NCR.

## Vulnerability

Where asset-specific vulnerability information is unavailable, vulnerability will be represented using transparent proxy indicators or treated seperately from direct hazard exposure.

The project will avoid presenting inferred vulnerability as observed asset-specific vulnerability.

## Business Materiality

Physical climate hazards may translate into potential business consequences through pathways such as:
Hazard > Asset Exposure > Operational disruption > Potential business consequence > Financial relevance

### Extreme Heat

Potential Pathways:
- reduced worker productivity
- increased cooling demand 
- equipment stress
- energy-cost pressure
- operational downtime

### Extreme Precipitation

Potential Pathways:
- site access disruption
- flooding-related operational interuption
- logistics disruption
- supply-chain disruption
- infrastructure damage

## Analytical Architecture

Climate Hazard > Spatial Hazard Dataset > Asset Location > Spatial Extraction > Asset-Level Hazard Exposure > Risk Screening > Sensitivity / Uncertainty Analysis > Business Materiality > Adaptation Priorities

## Evidence and Claims Discipline 

The project will distingiush between:

1. Observed/measured data
2. Modelled or derived indicators
3. Proxy variables
4. Analytical Assumptions
5. Interpretive conclusion

No result will be presented as more precise than the underlying data allows.

## Evidence Hierarchy

Priority will generally be given to:

1. Government datasets
2. Official scientific institutions
3. Peer-reviewed research 
4. International scientific/data institutions
5. Reputable secondary datasets where necessary

## Known Methodological Risks

### 1. Spatial resolution 

Climate data may be too coarse to represent conditions at individual assets precisely.

### 2. Asset-level vulnerability

Public data may not reveal detailed operational characteristics or adaptation measures.

### 3. Composite scoring 

Combining different indicators into a single risk score introduces methodological assumptions and therefore requires sensitivity analysis.


## 2 Physical Climate Risk Framework

This project follows the conceptual relationship:
Hazard > Exposure > Vulnerability > Risk

### Hazard

The climate-related physical event or condition that may cause harm.
For this project, the primary hazards are:

1. Extreme Heat
2. Extreme Precipitation

### Exposure

The presence of commercial and industrial assets in locations affected by these hazards.

### Vulnerability

The degree to which an exposed asset may be susceptible to operational disruption or damage.

### Risk

Risk is treated as a function of hazard, exposure and vulnerability.

This project produces a relative physical climate-risk screening rather than a quantitative functional-loss model.

## Asset Verification Protocol

### Objective

To convert source records into a defensible physical-asset exposure
dataset while preserving uncertainty and source provenance.

### Verification sequence

#### Step 1 — Record identification

Confirm that the source record identifies a commercial/industrial
facility or activity relevant to the study.

#### Step 2 — Physical-site reconciliation

Determine whether multiple source records refer to the same physical
site.

#### Step 3 — Geographic assignment

Assign or verify latitude and longitude using the strongest available
location evidence.

#### Step 4 — Location verification

Where necessary, compare the assigned location with independent
geographic sources.

#### Step 5 — Currentness assessment

Assess whether there is reasonable evidence that the facility is
currently operational or physically present.

#### Step 6 — Confidence classification

Assign a location/data-confidence category to the asset.

### Proposed confidence levels

High:  
Facility identity and physical site can be established with strong
evidence; geographic location is supported by reliable coordinates or
independent spatial verification; no major unresolved duplication or
currentness concern is present.

Medium:  
The facility and physical site can be reasonably established, but one
or more aspects such as coordinate precision, independent verification,
duplication or currentness remain uncertain.

Low:  
The facility cannot be reliably linked to a physical site, or major
uncertainties remain regarding location, identity, duplication or
current physical presence.

### Provenance rule

Every derived or supplemented field must retain information about its
source and verification method.

### Exclusion principle

Records that cannot be reasonably linked to a physical commercial or
industrial site should not automatically enter the final exposure
dataset.


## OCMMS Data Profiling and Integrity Assessment

Initial profiling was conducted before data cleaning or spatial processing to assess the structure, completeness and potential limitations of the OCMMS dataset. 

The dataset contains 1,421 records with unique serial numbers. Industry Type contains substantial categorical variation, while Category is dominated by WHITE, ORANGE and GREEN classifications. 

Repeated industry names and addresses were identified, including cases where similar addresses may represent different activities or floor-level locations. 

Registration dates range from 2019 to 2024 within the analysed dataset. 

Three records contain notable missing or malformed fields: one missing industry name, one missing address, and one record with an incomplete-looking industry-type value and missing category. 

These records will be retained during the profiling stage and assessed during subsequent data-cleaning and validation rather than being removed solely because of missing values.

## Asset Selection and Deduplication Principles

1. S.No. will be treated as a source-record identifier, not a physical-asset identifier.

2. Matching industry names alone will not be sufficient to remove records.

3. Matching addresses alone will not automatically indicate duplicates.

4. Records sharing an address will be investigated for:

  industry/activity

  entity name

  floor/unit information

  registration information

  other available identifiers

5. Where multiple registrations correspond to the same physical location but different activities, they will not automatically be collapsed into one activity.

6. Where multiple records clearly represent the same physical asset and same activity/entity, they may be consolidated at the physical-asset level while preserving the original OCMMS records.

7. Records lacking sufficient evidence to associate them with a physical commercial/industrial location will be flagged for further validation rather than automatically included.

8. Every derived location or consolidation decision should retain its source/provenance and confidence.



## Asset–Activity Distinction
A pilot assessment of the initial OCMMS records indicated that an OCMMS registration record should not automatically be treated as equivalent to a unique physical asset.

Multiple registration records may correspond to the same or similar addresses while representing different activities, entities, or, in some cases, different floors within the same building. 

Therefore, the analysis distinguishes between OCMMS registration records, activities/entities associated with those records, and physical assets/locations. 

Potential duplicate records will be assessed using identifiers, industry names, addresses, and activity information rather than being removed solely on the basis of matching fields. 

Where multiple activities are found to occupy the same physical asset, their common geographic climate-hazard exposure will be assessed at the asset level, while activity-specific vulnerability and potential business consequences will be differentiated where sufficient information is available. 

This approach prevents both double-counting of physical assets and the inappropriate assumption that co-located activities experience identical climate-related impacts.
