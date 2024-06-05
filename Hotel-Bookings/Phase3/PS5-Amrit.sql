-- By Amrit Sutradhar
-- Calculating number of guests per month by hotel each year.

USE capstone;

CREATE TABLE bookings_copy AS
SELECT *
FROM bookings;

SELECT
    hotel,
    arrival_date_year,
    arrival_date_month,
    sum(total_visitors)
FROM bookings_copy
GROUP BY
    hotel,
    arrival_date_year,
    arrival_date_month;
