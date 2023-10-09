# IT Ticketing System

## Overview

The IT Ticketing System is a robust and user-friendly platform designed to streamline the process of managing and resolving IT-related issues and requests within an organization. It serves as a centralized hub for IT teams and end-users to track and resolve IT incidents, problems, and service requests efficiently.

## Key Features

- **Ticket Creation:** Users can create IT tickets online to report issues, request support, or seek assistance.
- **Ticket Tracking:** Users can easily track the status and progress of their tickets within the system.
- **Status Modification:** Users have the ability to modify the status of their tickets, allowing for real-time updates.
- **Manager Access:** Technician managers can access their team members' tickets and monitor key performance indicators (KPIs) for better oversight.
- **Ticket History:** Technicians can view the complete history of tickets for individual users, departments, or the entire organization, aiding in issue resolution and analysis.
- **Ticket Transfer:** Technicians can transfer tickets to other team members if they are unable to resolve the problem, ensuring efficient problem-solving.


![Entity Relationship Diagram](images/Group%20Project%20ERD%20v2.png)

# Database Structure

## Tables

### fact_tickets Table

| Field Name    | Data Type       | Constraint  | Description                                    |
|---------------|-----------------|-------------|------------------------------------------------|
| ticket_id     | INT             | Primary Key | Unique identifier for each IT ticket.          |
| user_id       | INT             | Foreign Key | Identifier linking the ticket to a user.       |
| department_id | INT             | Foreign Key | Identifier linking the ticket to a department. |
| prior_ticket_id| INT            | Foreign Key | Unique identifier for each previous IT ticket. |
| ticket_category| VARCHAR(100)   | NOT NULL    | Identifier linking the ticket to a category.   |
| open_date_time | Date and Time  | NOT NULL    | Date and time when the ticket was opened.     |
| close_date_time| Date and Time  | NOT NULL    | Date and time when the ticket was closed.     |
| status        | VARCHAR(MAX)    |             | Current status of the ticket (e.g., open, closed, in-progress). |
| description   | VARCHAR(MAX)    | NOT NULL    | Detailed description of the IT issue or request. |
| subject       | VARCHAR(100)    | NOT NULL    | Subject Line of a ticket. |

### fact_ticket_lines Table

| Field Name   | Data Type       | Constraint  | Description                                    |
|--------------|-----------------|-------------|------------------------------------------------|
| ticket_line_id | INT           | Primary Key | Unique identifier for each ticket line.        |
| ticket_id    | INT             | Foreign Key | Identifier linking the line to a specific IT ticket. |
| technician_id| INT             | Foreign Key | Identifier of the technician responsible for the ticket line. |
| assignment_date_time | Date and Time |  NOT NULL     | Date and time when the ticket was assigned to a technician. |
| completion_date_time | Date and Time |  NOT NULL     | Date and time when the ticket was completed by a technician. |
| notes        | VARCHAR(MAX)    |             | Note a technician leaves.                     |

### dim_users Table

| Field Name    | Data Type       | Constraint  | Description                                    |
|---------------|-----------------|-------------|------------------------------------------------|
| user_id       | INT             | Primary Key | Unique identifier for each user.               |
| organization_id | INT           | Foreign Key | Identifier linking the user to an organization. |
| department_id | INT             | Foreign Key | Identifier linking the user to a department.   |
| last_name     | VARCHAR(100)    | NOT NULL    | Last name of the user.                        |
| first_name    | VARCHAR(100)    | NOT NULL    | First name of the user.                       |
| phone_number  | VARCHAR(20)     |             | Phone number of the user.                     |
| email_address | VARCHAR(100)    | NOT NULL    | Email address of the user.                    |
| title         | VARCHAR(100)    |             | Job title of the user.                        |


### dim_technicians Table

| Field Name    | Data Type       | Constraint  | Description                                    |
|---------------|-----------------|-------------|------------------------------------------------|
| technician_id | INT             | Primary Key | Unique identifier for each technician.         |
| user_id       | INT             | Foreign Key | Identifier linking the technician to a user.    |
| manager_id    | INT             | Foreign Key | Identifier of the manager of the technician.   |

### dim_organizations Table

| Field Name    | Data Type       | Constraint  | Description                                    |
|---------------|-----------------|-------------|------------------------------------------------|
| organization_id | INT           | Primary Key | Unique identifier for each organization.        |
| name          | VARCHAR(100)    | NOT NULL    | Name of the organization.                       |
| phone_number  | VARCHAR(20)     |             | Phone number of the organization.               |
| email_address | VARCHAR(100)    | NOT NULL    | Email address of the organization.              |
| state         | VARCHAR(2)      | NOT NULL    | State where the organization is located.        |
| city          | VARCHAR(30)     | NOT NULL    | City where the organization is located.         |
| zip_code      | INT             | NOT NULL    | Zip code of the organization.                   |
| street_address| VARCHAR(100)    | NOT NULL    | Street address of the organization.            |


### dim_departments Table

| Field Name    | Data Type       | Constraint  | Description                                    |
|---------------|-----------------|-------------|------------------------------------------------|
| department_id | INT             | Primary Key | Unique identifier for each department.            |
| organization_id | INT           | Foreign Key | Identifier linking the department to an organization. |
| name          | VARCHAR(100)    | NOT NULL    | Name of the department.                        |
| phone_number  | VARCHAR(20)     |             | Phone number of the department.                |
| email_address | VARCHAR(100)    | NOT NULL    | Email address of the department.               |