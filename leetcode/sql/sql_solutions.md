# LeetCode SQL tasks solutions

### https://leetcode.com/problems/combine-two-tables/
`
select FirstName, LastName, City, State
from Person left join Address on Person.PersonId = Address.PersonId
`

### https://leetcode.com/problems/duplicate-emails/
`
select Email from
(select Email, count(Email) as Counter from Person group by Email) as kek
where Counter > 1
` 

### https://leetcode.com/problems/second-highest-salary/
`
if (select count (distinct Salary) from Employee) > 1
select top 1 Salary as SecondHighestSalary from 
(select top 2 Salary from Employee order by Salary desc) as kek
order by Salary asc
else 
select null as SecondHighestSalary
`