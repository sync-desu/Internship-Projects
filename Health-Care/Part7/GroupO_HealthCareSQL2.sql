-- Problem Statement 6 (by Amrit Sutradhar)
-- lowest pharmacy-to-prescription ratio with prescriptions > 100
SELECT 
    addr.city AS City,
    COUNT(DISTINCT ph.pharmacyID) AS PharmacyCount,
    COUNT(pr.prescriptionID) AS PrescriptionCount,
    (COUNT(pr.prescriptionID) / COUNT(DISTINCT ph.pharmacyID)) AS PrescriptionToPharmacyRatio
FROM address addr
JOIN pharmacy ph ON addr.addressID = ph.addressID
JOIN prescription pr ON ph.pharmacyID = pr.pharmacyID
GROUP BY addr.city
HAVING PrescriptionCount > 100
ORDER BY PrescriptionToPharmacyRatio ASC
LIMIT 3;


-- Problem Statement 7 (by Amrit Sutradhar)
-- for each state in Alabama, find disease with highest number of treatments
SELECT 
    city, 
    diseaseName, 
    MAX(disease_count) AS max_treatments
FROM (
    SELECT 
        addr.city AS city, 
        ds.diseaseName AS diseaseName, 
        COUNT(*) AS disease_count
    FROM disease ds
    JOIN treatment tmt ON ds.diseaseID = tmt.diseaseID
    JOIN prescription psc ON tmt.treatmentID = psc.treatmentID
    JOIN pharmacy ph ON psc.pharmacyID = ph.pharmacyID
    JOIN address addr ON ph.addressID = addr.addressID
    WHERE addr.state = 'AL'
    GROUP BY addr.city, ds.diseaseName
) AS city_disease_counts
GROUP BY city
ORDER BY city;


-- Problem Statement 8 (by Harshitha P)
-- insurance plans for most claims and least disease
WITH DiseaseInsuranceClaimCount AS (
    SELECT 
        d.diseaseName,
        ip.planName,
        COUNT(c.claimID) AS claimCount
    FROM 
        Claim c
        JOIN InsurancePlan ip ON c.UIN = ip.UIN
        JOIN Treatment t ON c.claimID = t.claimID
        JOIN Disease d ON t.diseaseID = d.diseaseID
    GROUP BY 
        d.diseaseName, ip.planName
),
MaxClaimsPerDisease AS (
    SELECT
        diseaseName,
        planName AS maxClaimPlan,
        claimCount AS maxClaimCount,
        ROW_NUMBER() OVER (PARTITION BY diseaseName ORDER BY claimCount DESC) AS rn_max
    FROM
        DiseaseInsuranceClaimCount
),
MinClaimsPerDisease AS (
    SELECT
        diseaseName,
        planName AS minClaimPlan,
        claimCount AS minClaimCount,
        ROW_NUMBER() OVER (PARTITION BY diseaseName ORDER BY claimCount ASC) AS rn_min
    FROM DiseaseInsuranceClaimCount
)
SELECT
    max.diseaseName,
    max.maxClaimPlan,
    max.maxClaimCount,
    min.minClaimPlan,
    min.minClaimCount
FROM MaxClaimsPerDisease max
JOIN MinClaimsPerDisease min ON max.diseaseName = min.diseaseName
WHERE max.rn_max = 1 AND min.rn_min = 1;


-- Problem Statement 9 (by Shabbir Ahmed Hasan)
-- households with more than 1 patient having the same disease
SELECT
	d.diseaseName,
	a.address1,
	COUNT(DISTINCT p.patientID) AS num_patients
FROM patient p
JOIN treatment t ON p.patientID = t.patientID
JOIN disease d ON t.diseaseID = d.diseaseID
JOIN person pe ON p.patientID = pe.personID
JOIN Address a ON pe.addressID = a.addressID
GROUP BY d.diseaseName, a.address1
HAVING COUNT(DISTINCT p.patientID) > 1;


-- Problem Statement 10 (by Chilaka Nikhitha)
-- state wise treatments to claim ratio between 1st April 2021 and 31st March 2022
SELECT
    A.state,
    COUNT(DISTINCT T.treatmentID) AS treatment_count,
    COUNT(DISTINCT C.claimID) AS claim_count,
    CAST(COUNT(DISTINCT T.treatmentID) AS DECIMAL) / COUNT(DISTINCT C.claimID) AS treatment_to_claim_ratio
FROM Address A
JOIN Pharmacy P ON A.addressID = P.addressID
JOIN Prescription R ON P.pharmacyID = R.pharmacyID
JOIN Treatment T ON R.treatmentID = T.treatmentID
LEFT JOIN Claim C ON T.claimID = C.claimID
LEFT JOIN InsurancePlan IP ON C.uin = IP.uin
WHERE T.date BETWEEN '2021-04-01' AND '2022-03-31'
GROUP BY A.state
ORDER BY A.state;