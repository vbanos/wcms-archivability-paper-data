SELECT cms_id, AVG(wa), STDDEV(wa), AVG(accessibility), STDDEV(accessibility), AVG(metadata), STDDEV(metadata),
AVG(cohesion), STDDEV(cohesion), AVG(standards), STDDEV(standards), COUNT(*)
FROM websites
WHERE status=200
GROUP BY cms_id;
