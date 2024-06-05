-- Problem Statement 25 (by Harshitha P)
-- pharmacy details, total medicine prescribed, total hospital-exclusive medicine prescribed, and percentage of hospital-exclusive to total prescribed all in the year 2022
SELECT
    p.pharmacyID,
    p.pharmacyName,
    SUM(c.quantity) AS totalPrescribed2022,
    SUM(CASE WHEN m.hospitalExclusive = 'Y' THEN c.quantity ELSE 0 END) AS prescribedHospitalExclusive,
    ROUND((SUM(CASE WHEN m.hospitalExclusive = 'Y' THEN c.quantity ELSE 0 END) / SUM(c.quantity)) * 100, 2) AS percentagePrescribedHospitalExclusive
FROM prescription pr
JOIN pharmacy p ON pr.pharmacyID = p.pharmacyID
JOIN treatment t ON pr.treatmentID = t.treatmentID
JOIN contain c ON pr.prescriptionID = c.prescriptionID
JOIN medicine m ON c.medicineID = m.medicineID
WHERE YEAR(t.date) = 2022
GROUP BY p.pharmacyID, p.pharmacyName
ORDER BY percentagePrescribedHospitalExclusive DESC;


-- Problem Statement 26 (by Amrit Sutradhar)
-- state-wise percentage of treatments for which insurance was not claimed
SELECT
    ad.state,
    COUNT(t.treatmentID) AS totalTreatments,
    COUNT(CASE WHEN t.claimID = 0 THEN 1 END) AS totalUnclaimed,
    ROUND(( COUNT(CASE WHEN t.claimID = 0 THEN 1 END) / COUNT(t.treatmentID) ) * 100, 2) AS percentageUnclaimed
FROM treatment t
JOIN patient pt ON t.patientID = pt.patientID
JOIN person p ON pt.patientID = p.personID
JOIN address ad ON p.addressID = ad.addressID
GROUP BY ad.state


-- Problem Statement 27 (by Amrit Sutradhar)
-- diseases for which most and least number of patients were treated for in the year 2022, state wise
WITH DiseaseCounts AS (
    SELECT
        ad.state,
        tmt.diseaseID,
        d.diseaseName,
        count(d.diseaseID) as treatmentCount
    FROM disease d
    JOIN treatment tmt ON d.diseaseID = tmt.diseaseID
    JOIN patient pt ON tmt.patientID = pt.patientID
    JOIN person p ON pt.patientID = p.personID
    JOIN address ad ON p.addressID = ad.addressID
    WHERE YEAR(tmt.date) = 2022
    GROUP BY
        ad.state,
        tmt.diseaseID
), RankedDiseases AS (
    SELECT
        state,
        diseaseID,
        diseaseName,
        treatmentCount,
        RANK() OVER (PARTITION BY state ORDER BY treatmentCount DESC) AS rank_desc,
        RANK() OVER (PARTITION BY state ORDER BY treatmentCount ASC) AS rank_asc
    FROM DiseaseCounts
)
SELECT
    state,
    MAX(CASE WHEN rank_desc = 1 THEN diseaseName ELSE NULL END) AS mostTreatedDisease,
    MAX(CASE WHEN rank_desc = 1 THEN treatmentCount ELSE NULL END) AS mostTreatedCount,
    MAX(CASE WHEN rank_asc = 1 THEN diseaseName ELSE NULL END) AS leastTreatedDisease,
    MAX(CASE WHEN rank_asc = 1 THEN treatmentCount ELSE NULL END) AS leastTreatedCount
FROM RankedDiseases
GROUP BY state
ORDER BY state;

-- Problem Statement 28 (by Chilaka Nikhitha)
-- percentage of patient with registered people for cities with more than 10 registered people
SELECT 
    a.city,
    COUNT(DISTINCT p.personID) AS registered_people,
    COUNT(DISTINCT pa.patientID) AS registered_patients,
    COUNT(DISTINCT pa.patientID) * 100.0 / COUNT(DISTINCT p.personID) AS patient_percentage
FROM Address a
JOIN Person p ON a.addressID = p.addressID
LEFT JOIN Patient pa ON p.personID = pa.patientID
GROUP BY a.city
HAVING COUNT(DISTINCT p.personID) >= 10
ORDER BY a.city;


-- Problem Statement 29 (by Shabbir Ahmed Hasan)
-- top 3 companies using medicine with the substance "ranitidine"
SELECT 
    companyName,
    COUNT(*) AS MedicineCount
FROM medicine
WHERE substanceName = 'ranitidine'
GROUP BY companyName
ORDER BY MedicineCount DESC
LIMIT 3;
