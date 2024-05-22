-- Problem Statement 11 (by Amrit Sutradhar)
-- pharmacies who prescribe hospital-exclusive medicine more often in year 2021-2022
SELECT
	pharmacyName,
	count(med.medicineID) as hospitalExclusiveMedicine
FROM pharmacy ph
JOIN prescription psc ON ph.pharmacyID = psc.pharmacyID
JOIN contain cont ON psc.prescriptionID = cont.prescriptionID
JOIN treatment tmt ON psc.treatmentID = tmt.treatmentID
JOIN medicine med ON cont.medicineID = med.medicineID
WHERE (med.hospitalExclusive <> "N") AND (tmt.date BETWEEN "2021-01-01" AND "2022-12-31")
GROUP BY pharmacyName
ORDER BY hospitalExclusiveMedicine DESC;


-- Problem Statement 12 (by Chilaka Nikhitha)
--  insurance plan, company issuing the plan, and number of treatments the plan was claimed for
SELECT
	IP.planName,
	IC.companyName,
	COUNT(T.treatmentID) AS numTreatments
FROM InsurancePlan IP
JOIN InsuranceCompany IC ON IP.companyID = IC.companyID
JOIN Claim CL ON IP.UIN = CL.UIN
JOIN Treatment T ON CL.claimID = T.claimID
GROUP BY IP.planName, IC.companyName
ORDER BY numTreatments DESC;


-- Problem Statement 13 (by Chilaka Nikhitha and Amrit Sutradhar)
-- insurance company with their least and most claimed insurance plan
WITH ClaimCounts AS (
	SELECT
		ic.companyID,
		companyName,
		planName,
		count(claimID) as claimCounts
	FROM insuranceplan ip
	LEFT JOIN insurancecompany ic ON ip.companyID = ic.companyID
	LEFT JOIN claim cl ON ip.uin = cl.uin
	GROUP BY ip.uin
), MinMaxClaims AS (
	SELECT
		companyID,
		MIN(claimCounts) as minClaims,
		MAX(claimCounts) as maxClaims
	FROM ClaimCounts
	GROUP BY companyID
), MinClaims AS (
	SELECT
		cc.companyID,
		planName as leastClaimedPlan,
		claimCounts as leastClaimedClaims
	FROM ClaimCounts cc
	JOIN MinMaxClaims mmc on cc.companyID = mmc.companyID
	WHERE mmc.minClaims = cc.claimCounts
), MaxClaims AS (
	SELECT
		cc.companyID,
		planName as mostClaimedPlan,
		claimCounts as mostClaimedClaims
	FROM ClaimCounts cc
	JOIN MinMaxClaims mmc on cc.companyID = mmc.companyID
	WHERE mmc.maxClaims = cc.claimCounts
)
SELECT
	cc.companyID,
	companyName,
	leastClaimedPlan,
	leastClaimedClaims,
	mostClaimedPlan,
	mostClaimedClaims
FROM ClaimCounts cc
JOIN MinClaims minc ON cc.companyID = minc.companyID
JOIN MaxClaims maxc ON cc.companyID = maxc.companyID
GROUP BY companyID;


-- Problem Statement 14 (by Shabbir Ahmed Hasan)
-- state name, number of people in the state, number of patients in the state, and the people-to-patient ratio
SELECT 
	p.state,
	COUNT(ps.personID) AS num_people,
	COUNT(pa.patientID) AS num_patients,
	CAST(COUNT(ps.personID) AS FLOAT) / NULLIF(COUNT(pa.patientID), 0) AS people_to_patient_ratio
FROM person ps
LEFT JOIN address p ON ps.addressID = p.addressID
LEFT JOIN patient pa ON pa.patientID = ps.personID
GROUP BY p.state
ORDER BY people_to_patient_ratio;


-- Problem Statement 15 (by Harshitha P and Amrit Sutradhar)
-- quantity of medicine prescribed by each pharmacy state AZ, falls under tax criteria I for treatments that took place in 2021
SELECT
	ph.pharmacyID,
	ph.pharmacyName,
	COUNT(med.medicineID) prescribedUnderCriteria
FROM pharmacy ph
JOIN address ad ON ph.addressID = ad.addressID
JOIN prescription psc ON ph.pharmacyID = psc.pharmacyID
JOIN treatment tmt ON psc.treatmentID = tmt.treatmentID
JOIN contain cont ON psc.prescriptionID = cont.prescriptionID
JOIN medicine med ON cont.medicineID = med.medicineID
WHERE
	(ad.state = "AZ") AND
	(tmt.date BETWEEN "2021-01-01" AND "2021-12-31") AND
	(med.taxCriteria = "I")
GROUP BY ph.pharmacyName
ORDER BY prescribedUnderCriteria DESC;
