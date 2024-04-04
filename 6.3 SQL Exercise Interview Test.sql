-- I create a running total so it's easier to calculate all rows. It's sorted by business rules
WITH cte AS (
    SELECT
        position,
        salary,
        SUM(salary) OVER (PARTITION BY position ORDER BY salary, id) AS running_total
    FROM
        candidates
    WHERE salary >= 0 -- defensive code
),
senior_totals AS (
    SELECT
        COUNT(*) AS seniors, -- for the final resultset
        COALESCE(MAX(running_total), 0) AS senior_total -- coalease in case there is 0. To reduce from junior budget
    FROM
        cte
    WHERE
        position = 'senior'
        AND running_total <= 50000 -- my initial budget
),
junior_totals AS (
    SELECT
        COUNT(*) AS juniors -- remaining budget
    FROM
        cte
    WHERE
        position = 'junior'
        AND running_total <= (50000 - COALESCE((SELECT senior_total FROM senior_totals), 0))
)
SELECT
    juniors,
    seniors
FROM
    junior_totals
    CROSS JOIN senior_totals; -- cross join since it's only 1 row so performance shouldn't be an issue

/*
List of edge scenarios to test:
no juniors, no seniors: good
asdf as position: good
tie salaries: fixed adding id in the running_total
all salaries exceeding budget: good
negative salaries maybe?: added defensive code
duplicate in ids: error in insert test so I'm good
null values: error in insert test so I'm good
*/