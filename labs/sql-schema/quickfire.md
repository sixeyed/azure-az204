# SQL Schema Management - Quickfire Questions

## Question 1
What is a database schema?

- A) Physical structure
- B) Logical organization of database objects (tables, views, procedures)
- C) Color scheme
- D) Backup plan

**Answer: B**
Schema defines database structure: tables, columns, relationships, constraints, indexes, stored procedures.

---

## Question 2
What is a migration in database context?

- A) Moving servers
- B) Changing database schema or moving data between systems
- C) User migration
- D) Network change

**Answer: B**
Migrations evolve schema over time (add tables, alter columns) or move databases between systems.

---

## Question 3
What is Entity Framework Core?

- A) Database service
- B) .NET ORM (Object-Relational Mapper) for database access
- C) Monitoring tool
- D) Backup tool

**Answer: B**
EF Core maps C# objects to database tables, providing LINQ queries and change tracking.

---

## Question 4
What are EF Core Migrations?

- A) Database backups
- B) Code-first approach to evolve database schema from model changes
- C) Data imports
- D) User migrations

**Answer: B**
Migrations track model changes and generate SQL to update database schema incrementally.

---

## Question 5
How do you create an EF Core migration?

- A) Manual SQL only
- B) dotnet ef migrations add <name>
- C) No command
- D) Visual Studio only

**Answer: B**
`dotnet ef migrations add InitialCreate` generates migration code from model changes.

---

## Question 6
How do you apply migrations to database?

- A) Copy files
- B) dotnet ef database update
- C) Manual execution only
- D) Automatic

**Answer: B**
`dotnet ef database update` applies pending migrations to update database schema.

---

## Question 7
What is database seeding?

- A) Backup creation
- B) Populating database with initial/test data
- C) Indexing
- D) Encryption

**Answer: B**
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

- A) Table of contents
- B) Data structure improving query performance on specific columns
- C) Backup copy
- D) Primary key only

**Answer: B**
Indexes speed up SELECT queries but add overhead to INSERT/UPDATE/DELETE operations.

---

## Question 10
What is a foreign key constraint?

- A) Primary key
- B) Enforces referential integrity between tables
- C) Encryption key
- D) Access key

**Answer: B**
Foreign keys ensure values in one table reference valid values in another, maintaining data integrity.
