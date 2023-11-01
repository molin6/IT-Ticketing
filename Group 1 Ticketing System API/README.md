# Group 1 API Project - IT Ticket System<!-- omit from toc -->

- [Getting Started](#getting-started)
- [Creating the database](#creating-the-database)
- [Running the API](#running-the-api)
- [Using the API](#using-the-api)
  - [GET Calls](#get-calls)
    - [`/Departments`](#departments)
    - [`/Departments/AvgResolutionTimes`](#departmentsavgresolutiontimes)
    - [`/Organizations`](#organizations)
    - [`/Organizations/TicketCounts`](#organizationsticketcounts)
    - [`/Technicians`](#technicians)
    - [`/Technicians/AvgTicketTimes`](#techniciansavgtickettimes)
    - [`/Technicians/Manager`](#techniciansmanager)
    - [`/Technicians/Names`](#techniciansnames)
    - [`/Technicians/TicketsInfo`](#techniciansticketsinfo)
    - [`/Tickets`](#tickets)
    - [`/TicketLines`](#ticketlines)
    - [`/Users`](#users)
    - [`/Users/TicketCounts`](#usersticketcounts)
  - [POST Calls](#post-calls)
    - [`/Technicians`](#technicians-1)
    - [`/Tickets`](#tickets-1)
  - [PUT Calls](#put-calls)
    - [`/Tickets`](#tickets-2)
  - [DELETE Calls](#delete-calls)
    - [`/Users`](#users-1)


# Getting Started
To get started, you'll need to install the dependencies.

You can do this by navigating to the directory where the 'Group 1 Ticketing System API' folder is located and running the following command in GIT CMD:
```bash
pip install -r requirements.txt
```
---

**Sending Requests:**

The **Example Request** sections will contain references in the style of http://*{host}*/Technicians. You will need to replace {host} with the address where the API is running.

**Example:**\
http://localhost:5000/Technicians

---

# Creating the database
You can create/recreate the database at any time, navigate to the directory where the 'Group 1 Ticketing System API\API Database Creator' folder is located and run the following command in GIT CMD:

```bash
python create_database.py
```

# Running the API
To run the API, navigate to the directory where the 'Group 1 Ticketing System API\API Project' folder is located and run the following command in GIT CMD:

```bash
python app.py
```

# Using the API
Once the API is running, you can use the following commands to interact with it.

## GET Calls

### `/Departments`

### `/Departments/AvgResolutionTimes`

### `/Organizations`

### `/Organizations/TicketCounts`

### `/Technicians`

|METHOD|`GET`|
|---|---|
|**Description**|Returns all technicians from the database|
|**Params**|*limit* (optional) parameter to limit the number of results returned, default is 10|

**Example Request**\
http://*{host}*/Technicians

**Example Params**
|Key|Value|
|---|---|
|limit|1|


**Example Response:**
```json
[
  {
    "manager_id": 3,
    "technician_id": 1,
    "user_id": 100
  },
  {
    "manager_id": 100,
    "technician_id": 2,
    "user_id": 79
  },
  {
    "manager_id": 100,
    "technician_id": 3,
    "user_id": 8
  }
]
```
---

### `/Technicians/AvgTicketTimes`

### `/Technicians/Manager`

### `/Technicians/Names`

|METHOD|`GET`|
|---|---|
|**Description**|Returns the first and last names of all the technicians|

**Example Request**\
http://*{host}*/Technicians/Names

**Example Response**
```json
[
    "Joseph Perez",
    "Michelle Reynolds",
    "Mary Patterson"
]
```
---

### `/Technicians/TicketsInfo`

### `/Tickets`
|METHOD|`GET`|
|---|---|
|**Description**|Returns # of records in the Ticket table based on the optional parameter|
|**Params**|*limit* (optional) parameter to limit the number of results returned, default is 10|

**Example Request**\
http://*{host}*/Tickets

**Example Response**
```json

```

### `/TicketLines`

### `/Users`

### `/Users/TicketCounts`









## POST Calls

### `/Technicians`

<a id="add-ticket"></a>
### `/Tickets`
|METHOD|`POST`|
|-------|-----|
|**Description**|Adds a new ticket|
|**Body**|Takes a json object with the following attributes: `user_id`, `department_id`, `prior_ticket_id`, `ticket_category`, `open_date_time`, `close_date_time`, `status`, `description`,`subject`|

**Example Request**\
http://*{host}*/Tickets

**Example Body**
```json
{
        "user_id":1,
        "department_id":2,
        "prior_ticket_id":3,
        "ticket_category":"Non-Emergency",
        "open_date_time":"Wed, 18 Oct 2023 20:10:17 GMT",
        "close_date_time":"Wed, 18 Oct 2023 22:10:17 GMT",
        "status":"Active",
        "description":"I can't connect to the server",
        "subject":"Server connection problem"
}
```

**Example Response**
```json
"Sucessfully added a new ticket"
```

## PUT Calls

<a id="update-ticket"></a>
### `/Tickets`
|METHOD|`PUT`|
|-------|-----|
|**Description**|Updates a ticket|
|**Body**|Takes a json object with the following attributes: `user_id`, `department_id`, `prior_ticket_id`, `ticket_category`, `open_date_time`, `close_date_time`, `status`, `description`,`subject`|
|**Params**|ticket_id - The id of the ticket to update|

**Example Params**
|Key|Value|
|---|---|
|ticket_id|1|

**Example Request**\
http://*{host}*/Tickets

**Example Body**
```json
{
        "user_id":1,
        "department_id":2,
        "prior_ticket_id":5,
        "ticket_category":"Non-Emergency",
        "open_date_time":"Wed, 18 Oct 2023 20:10:17 GMT",
        "close_date_time":"Wed, 18 Oct 2023 22:10:17 GMT",
        "status":"Active",
        "description":"I can't connect to the server",
        "subject":"Server connection problem"
}
```

**Example Response**
```json
"Successfully updated the ticket"
```

## DELETE Calls

<a id="delete-user"></a>
### `/Users`

|METHOD|`DELETE`|
|-------|-----|
|**Description**|Deletes a user|
|**Params**|user_id - The id of the user to delete|

**Example Params**
|Key|Value|
|---|---|
|user_id|1|

**Example Request**\
http://*{host}*/Users

**Example Response**
```json
"Sucessfully removed the user"
```







