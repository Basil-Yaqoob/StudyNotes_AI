### Super Key
- **Definition**: A super key is a set of one or more attributes (columns) of a table that can uniquely identify a record in a database table. 
- **Characteristics**:
  - A super key may consist of a single attribute or a combination of multiple attributes.
  - Every table in a database is guaranteed to have at least one super key.
  - Super keys can contain additional attributes that are not necessary for unique identification.

### Candidate Key
- **Definition**: A candidate key is a minimal super key, meaning it is a super key with no redundant attributes. It can uniquely identify each row in a table.
- **Characteristics**:
  - A table can have more than one candidate key.
  - Each candidate key can potentially serve as the primary key for the table.
  - Candidate keys must be minimal; removing any attribute from a candidate key will mean that it no longer uniquely identifies each row.

### Primary Key
- **Definition**: A primary key is a specific candidate key selected by the database designer to uniquely identify each row in a table.
- **Characteristics**:
  - A table can have only one primary key.
  - The primary key must contain unique values. No part of the primary key can be null.
  - It is used to enforce entity integrity, ensuring that every row is unique and identifiable.

### Key Points for Note Preparation
- **Hierarchy and Relationship**: It's crucial to understand the hierarchy and relationship between super key, candidate key, and primary key. A super key includes any combination of columns that can uniquely identify a row. A candidate key is a minimal subset of a super key, and the primary key is one of the candidate keys chosen to uniquely identify rows in a table.
- **Uniqueness and Minimality**: The uniqueness and minimality aspects of candidate keys as compared to super keys are essential. Candidate keys are minimal super keys that do not contain any redundant information.
- **Importance of Primary Keys**: The role of primary keys in database design and integrity cannot be overstated. They ensure that each row in a table is unique and identifiable, which is crucial for relationships between tables and database normalization.
- **Examples**: Including examples in the notes will help illustrate how a set of attributes can be considered as super key, candidate key, or primary key. For instance, in a table with attributes (StudentID, StudentName, CourseID), both StudentID and CourseID can be super keys if they uniquely identify a student record. However, if StudentID alone can uniquely identify a student, then it is a candidate key and can be chosen as the primary key.

### Additional Tips
- **Diagrams and Visual Aids**: Incorporating diagrams or visual aids can help in better understanding the concepts of super key, candidate key, and primary key.
- **Quiz Questions or Exercises**: At the end of the notes, including quiz questions or exercises for self-assessment can be beneficial for exam preparation and reinforcing the learned concepts.

This comprehensive set of notes covers the core concepts of Super Key, Candidate Key, and Primary Key in DBMS, structured for easy understanding and exam preparation.