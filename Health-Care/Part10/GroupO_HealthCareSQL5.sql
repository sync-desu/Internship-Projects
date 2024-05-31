-- Problem Statement 20 (by Harshitha P)
-- patient and their age who have gone through treatments more than once, sorting by treatment in descending
SELECT 
	p.personName AS PatientName,
    TIMESTAMPDIFF(YEAR, pat.dob, CURDATE()) AS Age,
	COUNT(t.treatmentID) AS NumberOfTreatments
FROM Person p
JOIN Patient pat ON p.personID = pat.patientID
JOIN Treatment t ON pat.patientID = t.patientID
GROUP BY p.personName, pat.dob
HAVING NumberOfTreatments > 1
ORDER BY NumberOfTreatments desc;


-- Problem Statement 21 (by Harshitha P)
-- for each and every disease, number of males and females undergoing treatment and the male-to-female ratio

-- Problem Statement 22 (by Shabbir Ahmed Hasan)
-- top 3 cities with the most number of treatments for every disease
SELECT
	d.diseaseName,
	subquery.city,
    subquery.treatment_count
FROM (
	SELECT
		t.diseaseID,
		a.city,
        COUNT(t.treatmentID) AS treatment_count,
        RANK() OVER (PARTITION BY t.diseaseID ORDER BY COUNT(t.treatmentID) DESC) AS city_rank
	FROM
		treatment t
        JOIN disease d ON t.diseaseID = d.diseaseID
        JOIN patient p ON t.patientID = p.patientID
        JOIN person per ON p.patientID = per.personID
        JOIN address a ON per.addressID = a.addressID
	GROUP BY
		t.diseaseID,
        a.city
) subquery
JOIN disease d ON subquery.diseaseID = d.diseaseID
WHERE subquery.city_rank <= 3
ORDER BY
    d.diseaseName,
    subquery.city_rank;


-- Problem Statement 23 (by Chilaka Nikhitha)
-- prescriptions prescribed by each pharmacy for every disease in the year 2021 and 2022
WITH PrescriptionCountsByYear AS (
	SELECT
		p.pharmacyID,
		ph.pharmacyName,
		t.diseaseID,
		SUM(IF(YEAR(t.date) = 2021, 1, 0)) AS prescriptions_2021,
		SUM(IF(YEAR(t.date) = 2022, 1, 0)) AS prescriptions_2022
	FROM Prescription p
	JOIN Treatment t ON p.treatmentID = t.treatmentID
	JOIN Pharmacy ph ON p.pharmacyID = ph.pharmacyID
	GROUP BY p.pharmacyID, ph.pharmacyName, t.diseaseID
)
SELECT
	pcby.pharmacyName,
	d.diseaseName,
	pcby.prescriptions_2021,
	pcby.prescriptions_2022
FROM PrescriptionCountsByYear pcby
JOIN Disease d ON pcby.diseaseID = d.diseaseID
ORDER BY pcby.pharmacyName, d.diseaseName;


-- Problem Statement 24 (by Amrit Sutradhar)
-- insurance company and their target state (patients claiming insurance most in that particular state)