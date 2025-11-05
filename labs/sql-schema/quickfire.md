# SQL Schema Management - Quickfire Questions

## Question 1
What is a database schema?


- A) Physical structure
- B) Logical organization of database objects (tables, views, procedures)
- C) Backup plan
- D) Color scheme

**Answer: B**
Schema defines database structure: tables, columns, relationships, constraints, indexes, stored procedures.
---
## Question 2
What is a migration in database context?


- A) User migration
- B) Network change
- C) Changing database schema or moving data between systems
- D) Moving servers

**Answer: C**
Migrations evolve schema over time (add tables, alter columns) or move databases between systems.
---
## Question 3
What is Entity Framework Core?


- A) Backup tool
- B) Database service
- C) .NET ORM (Object-Relational Mapper) for database access
- D) Monitoring tool

**Answer: C**
EF Core maps C# objects to database tables, providing LINQ queries and change tracking.
---
## Question 4
What are EF Core Migrations?


- A) User migrations
- B) Data imports
- C) Database backups
- D) Code-first approach to evolve database schema from model changes

**Answer: D**
Migrations track model changes and generate SQL to update database schema incrementally.
---
## Question 5
How do you create an EF Core migration?


- A) Manual SQL only
- B) No command
- C) Visual Studio only
- D) dotnet ef migrations add <name>

**Answer: D**
`dotnet ef migrations add InitialCreate` generates migration code from model changes.
---
## Question 6
How do you apply migrations to database?


- A) Automatic
- B) dotnet ef database update
- C) Manual execution only
- D) Copy files

**Answer: B**
`dotnet ef database update` applies pending migrations to update database schema.
---
## Question 7
What is database seeding?


- A) Backup creation
- B) Indexing
- C) Populating database with initial/test data
- D) Encryption

**Answer: C**
Seeding inserts initial data (lookup tables, test data) during database creation or migration.
---
## Question 8
What is a stored procedure?


- A) Storage method
- B) Precompiled SQL code stored in database for reuse
- C) Backup procedure
- D) Network procedure

**Answer: B**
Stored procedures encapsulate SQL logic, improving performance and security through parameterization.
---
## Question 9
What is an index in a database?


- A) Backup copy
- B) Table of contents
- C) Data structure improving query performance on specific columns
- D) Primary key only

**Answer: C**
Indexes speed up SELECT queries but add overhead to INSERT/UPDATE/DELETE operations.
---
## Question 10
What is a foreign key constraint?


- A) Encryption key
- B) Primary key
- C) Enforces referential integrity between tables
- D) Access key

**Answer: C**
Foreign keys ensure values in one table reference valid values in another, maintaining data integrity.