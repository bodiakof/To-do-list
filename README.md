# To-do-list

A simple to-do list application built with Django. This project allows users to manage tasks and tags, demonstrating CRUD operations, many-to-many relationships, and query optimization using Django’s ORM.

## Features

- **Task Management**  
  - **Create Tasks:** Add new tasks with a description, optional deadline, and associated tags.  
  - **Update Tasks:** Edit task details.  
  - **Delete Tasks:** Remove tasks from the list.  
  - **Toggle Task Status:** Mark tasks as done or not done.  
  - **Ordering:** Tasks are ordered by their completion status and creation date.  
 

- **Tag Management**  
  - **Create Tags:** Add new tags to categorize tasks.  
  - **Update Tags:** Edit existing tags.  
  - **Delete Tags:** Remove tags from the system.  
  - **Many-to-Many Relationship:** Each task can have multiple tags, and each tag can be linked to multiple tasks.  


- **Efficient Database Queries**  
  - Uses `prefetch_related` to optimize queries for many-to-many relationships, reducing the number of database hits when retrieving tasks along with their tags.
