-- find all the pairs (actor_id, director_id)
-- where the actor has cooperated with the director at least three time

SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(timestamp) >= 3