-- By Shabbir Ahmed Hasan
-- Analyze guest demographics and booking behaviours using PowerBI and MySQL.

USE capstone;

-- Guest Demographics
SELECT
    customer_type,
    country,
    AVG(adr) AS avg_adr,
    COUNT(*) AS total_bookings,
    SUM(total_visitors) AS total_visitors
FROM bookings
GROUP BY
    customer_type,
    country
ORDER BY total_bookings DESC;

-- Booking Behaviors
SELECT
    arrival_date_year,
    arrival_date_month,
    market_segment,
    booking_changes,
    COUNT(*) AS total_bookings,
    SUM(stays_in_weekend_nights) AS total_weekend_nights,
    SUM(stays_in_week_nights) AS total_weekday_nights
FROM bookings
WHERE is_canceled = 0
GROUP BY
    arrival_date_year,
    arrival_date_month,
    market_segment,
    booking_changes
ORDER BY total_bookings DESC;
