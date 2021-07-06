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