-- Problem Statement 16 (by Harshitha P)
-- quantity of medicine perscribed by "Ally Scripts" pharmacy per prescription
SELECT
    pre.prescriptionID,
    sum(c.quantity) AS totalQuantity,
    CASE 
        WHEN sum(c.quantity) < 20 THEN "Low Quantity"
        WHEN sum(c.quantity) > 20 AND sum(c.quantity) < 50 THEN "Medium Quantity"
        WHEN sum(c.quantity) >= 50 THEN "High Quantity"
    end AS Tag
FROM prescription AS pre
JOIN contain c ON c.prescriptionID = pre.prescriptionID
JOIN pharmacy ph ON ph.pharmacyID = pre.pharmacyID
WHERE ph.pharmacyName = "Ally Scripts" 
GROUP BY pre.prescriptionID;


-- Problem Statement 17 (by Chilaka Nikhitha)
-- finding LowQuantity-HighDiscount and HighQuantity-NoDiscount medicine for pharmacy "Spot Rx"
SELECT
    k.medicineID,
    m.productName,
    k.quantity,
    CASE
        WHEN k.quantity > 7500 THEN "HIGH QUANTITY"
        WHEN k.quantity < 1000 THEN "LOW QUANTITY"
        ELSE "MEDIUM QUANTITY"
    END AS QuantityStatus,
    k.discount,
    CASE
        WHEN k.discount >= 30 THEN "HIGH"
        WHEN k.discount = 0 THEN "NONE"
        ELSE "LOW" 
    END AS DiscountStatus
FROM Keep k
JOIN Medicine m ON k.medicineID = m.medicineID
JOIN Pharmacy p ON k.pharmacyID = p.pharmacyID
WHERE (k.quantity < 1000 AND k.discount >= 30) OR (k.quantity > 7500 AND k.discount = 0)
AND p.pharmacyName = "Spot Rx";


-- Problem Statement 18 (by Shabbir Ahmed Hasan)
-- list of affordable and costly HospitalExclusive medicine from "HealthDirect" pharmacy
SELECT
    productName AS medicine_name,
    CASE
        WHEN maxPrice <= (SELECT AVG(maxPrice) * 0.5 FROM medicine) THEN "Affordable"
        WHEN maxPrice >= (SELECT AVG(maxPrice) * 2 FROM medicine) THEN "Costly"
        ELSE "Uncategorized"
    END AS price_category
FROM medicine m
JOIN keep k ON m.medicineID = k.medicineID
JOIN pharmacy p ON k.pharmacyID = p.pharmacyID
WHERE
    p.pharmacyName = "HealthDirect"
    AND hospitalExclusive = "Y";


-- Problem Statement 19 (by Amrit Sutradhar)
-- categorize patients into Young(male/female), Adult(male/female), MidAge(male/female) and Elder(male/female)
SELECT
    psn.personName AS Name,
    psn.gender AS Gender,
    pt.dob AS DoB,
    CASE
        WHEN (pt.dob > "2005-01-01") AND (psn.gender = "Male") THEN "YoungMale"
        WHEN (pt.dob > "2005-01-01") AND (psn.gender = "Female") THEN "YoungFemale"
        WHEN (pt.dob < "2005-01-01" AND pt.dob > "1985-01-01") AND (psn.gender = "Male") THEN "AdultMale"
        WHEN (pt.dob < "2005-01-01" AND pt.dob > "1985-01-01") AND (psn.gender = "Female") THEN "AdultFemale"
        WHEN (pt.dob < "1985-01-01" AND pt.dob > "1970-01-01") AND (psn.gender = "Male") THEN "MidAgeMale"
        WHEN (pt.dob < "1985-01-01" AND pt.dob > "1970-01-01") AND (psn.gender = "Female") THEN "MidAgeFemale"
        WHEN (pt.dob < "1970-01-01") AND (psn.gender = "Male") THEN "ElderMale"
        WHEN (pt.dob < "1970-01-01") AND (psn.gender = "Female") THEN "ElderFemale"
    END AS Category
FROM person psn 
JOIN patient pt ON psn.personID = pt.patientID
ORDER BY DoB -- for convenience;
