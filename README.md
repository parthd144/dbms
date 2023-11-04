# dbms
1) Consider the relation employee (emp_id,e_name,salary ,Date of Joining,Dapt_no,Designation) perform basic SQL operations.
Create table employee.
Insert 10 records in table.
Create a view emp_vl of table employee which  has emp_id , name and dept-attributes.
Create view of table.
Update dept of any employee in view. Check whether it  gets updated or not.
Create emp_id as primary key and show indices on table employee.
Show indices on table.
Create user defined index on any column. 

2) Consider the relation employee (emp_id,e_name,salary ,Date of Joining,Dapt_no,Designation) perform basic SQL operations.
Display employees whose name contains letter ‘e’.
Display different types of designation
Display name and salary of employee whose location is Mumbai
Display name and department of employee working in Manager or Marketing department
Display the department name whose employees are more than one
Rename employee table as emp1
Add a new column city in the employee table.

3)Consider the relation employee(emp_id,e_name,salary ,Date of Joining,Dapt_no,Designation) perform basic SQL operations.
Find department in which maximum employees work.
 Display name, designation and department no of employees whose name starts with either ‘A’ or ‘P’.
 Display max. salary from department 2 and min. salary from department 4.
 Display employee data where salary is less than average salary from department 3.
 Display employees who were hired earliest or latest.
Display name and department no of employees who are manager, market analysts. Use prediactes
List employees hired in August.
 List employees who are hired after 31/12/2006.
 Find average annual salary per department.

4)Consider  two tables Customer(c_id, c_name , email , city , pincode)Order(order_id , date , amount , cust_id.
Create both the tables with primary key and foreign key constraints. 
insert 10 records each.
Find all orders placed by customers with cust_id 2
Find list of customers who placed their order and details of order
List of customers who haven’t placed order
List all orders and append to customer table
Display all records
Display customer that are from same city8


5) Consider tables Borrower (RollNo, Name, DateofIssue, NameofBook, Status) and 
Fine (Roll_no,Date,Amt). Status is either Issued or Returned.
1. Create both the tables with primary key.
2. Insert 10 records each.
3. Find count of books with Issued status.
4. Display all records.
5. Display RollNo whose date of issue is same.

6) Consider student (roll_no, name, marks, class) table. Column roll_no is primary key. Perform any 3 DLL and any 3 DML operations on the table.

7) Write a SQL statement to create a table job_history including columns employee_id, start_date, end_date, job_id and department_id and make sure that, the employee_id column does not contain any duplicate value at the time of insertion and the foreign key column job_id contain only those values which are exists in the jobs table. Consider table Job (job_id,job_title.min_sal,max_sal)


8) For the given relation schema: employee(employee-name, street, city) 
works (employee-name, company-name, salary) 
company (company-name, city) 
manages (employee-name, manager-name)
 Give an expression in SQL for each of the following queries: 
a) Find the names, street address, and cities of residence for all employees who work for same company and earn more than $10,000.
b) Find the names of all employees in the database who live in the same cities as the companies for which they work.
c) Find the names of all employees who earn more than the average salary of all employees of their company. Assume that all people work for at most one company.

9) For the given relation schema: employee(employee-name, street, city) 
works (employee-name, company-name, salary) 
company (company-name, city) 
manages (employee-name, manager-name)
 Give an expression in SQL for each of the following queries: 
Find the name of the company that has the smallest payroll.
Find the names of all employees in the database who live in the same cities and on the same streets as do their managers.
