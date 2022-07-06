# Leetcode SQL

## 180. Consecutive Numbers
Medium
SQL Schema

***Table: Logs***

    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | id          | int     |
    | num         | varchar |
    +-------------+---------+
    id is the primary key for this table.
    id is an autoincrement column.

 

Write an SQL query to find all numbers that appear at least three times consecutively.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
***Logs table:***

    +----+-----+
    | id | num |
    +----+-----+
    | 1  | 1   |
    | 2  | 1   |
    | 3  | 1   |
    | 4  | 2   |
    | 5  | 1   |
    | 6  | 2   |
    | 7  | 2   |
    +----+-----+
***Output:***

    +-----------------+
    | ConsecutiveNums |
    +-----------------+
    | 1               |
    +-----------------+
    Explanation: 1 is the only number that appears consecutively for at least three times.  

***SQL code*** 

    SELECT DISTINCT(num) AS ConsecutiveNums
    FROM (
    SELECT num,
           LEAD(num) over(order by id) as lead_num,
           Lag(num) over(order by id) as lag_num
    FROM Logs) tmp
    WHERE num=lead_num and num=lag_num


## 178. Rank Scores
Medium
***SQL Schema***

    Table: Scores

    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | id          | int     |
    | score       | decimal |
    +-------------+---------+
    id is the primary key for this table.
    Each row of this table contains the score of a game. Score is a floating point value with two decimal places.

 

Write an SQL query to rank the scores. The ranking should be calculated according to the following rules:

    The scores should be ranked from the highest to the lowest.
    If there is a tie between two scores, both should have the same ranking.
    After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.

Return the result table ordered by score in descending order.

The query result format is in the following example.

 

Example 1:

***Input:***

    Scores table:
    +----+-------+
    | id | score |
    +----+-------+
    | 1  | 3.50  |
    | 2  | 3.65  |
    | 3  | 4.00  |
    | 4  | 3.85  |
    | 5  | 4.00  |
    | 6  | 3.65  |
    +----+-------+
***Output:***

    +-------+------+
    | score | rank |
    +-------+------+
    | 4.00  | 1    |
    | 4.00  | 1    |
    | 3.85  | 2    |
    | 3.65  | 3    |
    | 3.65  | 3    |
    | 3.50  | 4    |
    +-------+------+

***SQL code***

    SELECT
        score,
        DENSE_RANK() OVER (
            ORDER BY score DESC
        ) 'rank'
    FROM
        Scores

