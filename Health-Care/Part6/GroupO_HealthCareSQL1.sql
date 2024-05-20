-- Problem Statement 1 (by Shabbir Ahmed Hasan)
-- number of treatments each age category of patients has gone through
SELECT
  	CASE
		WHEN (YEAR(CURDATE()) - YEAR(p.dob)) < 15 THEN 'Children'
		WHEN (YEAR(CURDATE()) - YEAR(p.dob)) BETWEEN 15 AND 24 THEN 'Youth'
		WHEN (YEAR(CURDATE()) - YEAR(p.dob)) BETWEEN 25 AND 64 THEN 'Adults'
		ELSE 'Seniors'
  	END AS age_category,
  	COUNT(*) AS treatment_count
FROM Patient p
INNER JOIN Treatment t ON p.patientID = t.patientID
WHERE YEAR(t.date) = 2022
GROUP BY age_category
ORDER BY age_category;


-- Problem Statement 2 (by Shabbir Ahmed Hasan)
-- each disease the male-to-female ratio
SELECT
	d.diseaseName AS disease,
	ROUND(SUM(CASE WHEN p.gender = 'male' THEN 1 ELSE 0 END) / 
		SUM(CASE WHEN p.gender = 'female' THEN 1 ELSE 0 END), 2) AS male_to_female_ratio,
	CONCAT(
		(SELECT COUNT(*) FROM Person WHERE gender = 'male'),
		' Males / ',
		(SELECT COUNT(*) FROM Person WHERE gender = 'female'),
		' Females'
  	) AS gender_counts
FROM Disease d
INNER JOIN Treatment t ON d.diseaseID = t.diseaseID
INNER JOIN Person p ON t.patientID = p.personID
WHERE p.gender IN ('male', 'female')
GROUP BY d.diseaseName
ORDER BY male_to_female_ratio DESC;


-- Problem Statement 3 (by Chilaka Nikhitha)
-- for each gender the number of treatments, number of claims, and treatment-to-claim ratio
WITH TreatmentCounts AS (
  	SELECT
    	per.gender,
    	COUNT(DISTINCT t.treatmentid) AS total_treatments
  	FROM treatment AS t
  	JOIN patient AS p ON t.patientID = p.patientID
  	JOIN person AS per ON p.patientID = per.personID
  	GROUP BY per.gender
),
ClaimCounts AS (
  	SELECT
    	per.gender,
    	COUNT(DISTINCT c.claimid) AS total_claims
  	FROM treatment AS t
  	JOIN patient AS p ON t.patientID = p.patientID
  	JOIN claim AS c ON t.claimID = c.claimID
  	JOIN person AS per ON p.patientID = per.personID
  	GROUP BY per.gender
)
SELECT
  	tc.gender,
  	tc.total_treatments,
  	cc.total_claims,
  	tc.total_treatments / cc.total_claims AS treatment_to_claim_ratio
FROM TreatmentCounts AS tc
JOIN ClaimCounts AS cc ON tc.gender = cc.gender
ORDER BY tc.gender;


-- Problem Statement 4 (by Harshitha P)
-- units of medicine in each pharmacy inventory, total maximum retail price, and total price of all the medicines post discount
SELECT 
	ph.pharmacyName,
	SUM(c.quantity) AS total_units,
	SUM(c.quantity * m.maxPrice) AS total_max_retail_price,
	SUM(c.quantity * m.maxPrice * (1 - k.discount / 100)) AS total_price_after_discount
FROM contain AS c
JOIN prescription AS p ON p.prescriptionID = c.prescriptionID
JOIN pharmacy AS ph ON p.pharmacyID = ph.pharmacyID
JOIN keep AS k ON k.pharmacyID = ph.pharmacyID AND k.medicineID = c.medicineID
JOIN medicine AS m ON m.medicineID = c.medicineID
GROUP BY ph.pharmacyID, ph.pharmacyName;


-- Problem Statement 5 (by Amrit Sutradhar)
-- for each pharmacy the maximum, minimum and average number of medicines prescribed
SELECT
	pharm.pharmacyName AS PharmacyName,
	MAX(medicine_count) AS MaxMeds,
	MIN(medicine_count) AS MinMeds,
	AVG(medicine_count) AS AvgMeds
FROM (
	SELECT
		presc.pharmacyID,
		COUNT(cont.medicineID) as medicine_count
	FROM Prescription presc
	JOIN Contain cont ON presc.prescriptionID = cont.prescriptionID
	GROUP BY presc.prescriptionID
) AS medicine_count
JOIN Pharmacy pharm ON medicine_count.pharmacyID = pharm.pharmacyID
GROUP BY pharm.pharmacyID, pharm.pharmacyName;
