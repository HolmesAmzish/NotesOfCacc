# PostgreSQL

## Basic

```bash
psql -U postgres
```

### Loading from Saved Database

```bash
\password [USERNAME]        # securely change the password for a user
\c[onnect]                  # connect to the database
\l                          # list databases
\dt                         # list tables
```

## Querying Data

### SELECT

```sql
SELECT 
    select_list
FROM
    table_name;
```

**Example**

```sql
SELECT
    first_name || ' '  || last_name AS full_name,
    email
FROM
    customer;
```

We used the concatenation operator `||` to concatenate the first name, space and last name of every customer.

To assign a name to a column temporarily in the query, you can use a ccolumn alias:

```sql
expression AS column_alias
```

The AS keyword is optional.

The `FROM` clause of the `SELECT` statement is optional. Therefore, you can omit it in the SELECT statement. Typically, you use the `SELECT` clause with a function to retreive the function result. For example:

```sql
SELECT now();
```

It'll return the current date and time of the PostgreSQL server.
