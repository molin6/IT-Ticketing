# Group 1 API Project - IT Ticket System

- [Group 1 API Project - IT Ticket System](#group-1-api-project---it-ticket-system)
  - [Getting Started](#getting-started)
  - [Creating the database](#creating-the-database)
  - [Running the API](#running-the-api)
  - [Using the API](#using-the-api)
    - [`/Technicians`](#technicians)
    - [`/Technicians/Names`](#techniciansnames)
    - [`/TicketLines`](#ticketlines)
    - [`/Tickets`](#tickets)
    - [`/Tickets`](#tickets-1)
    - [`/Tickets/<ticket_id>`](#ticketsticket_id)
    - [`/Users`](#users)
    - [`/Users/<user_id>`](#usersuser_id)
    - [`/Organizations`](#organizations)
    - [`/Departments`](#departments)
    - [`/Technicians/AvgTicketTimes`](#techniciansavgtickettimes)
    - [`/Technicians/TicketsInfo`](#techniciansticketsinfo)
    - [`/Technicians/Manager`](#techniciansmanager)
    - [`/Technicians/Update`](#techniciansupdate)
    - [`/Users/TicketCounts`](#usersticketcounts)
    - [`/Departments/AvgResolutionTimes`](#departmentsavgresolutiontimes)
    - [`/Organizations/TicketCounts`](#organizationsticketcounts)


## Getting Started
To get started, you'll need to install the dependencies.

You can do this by navigating to the directory where the 'Group 1 Ticketing System API' folder is located and running the following command in GIT CMD:
```bash
pip install -r requirements.txt
```

## Creating the database
You can create/recreate the database at any time, navigate to the directory where the 'Group 1 Ticketing System API\API Database Creator' folder is located and run the following command in GIT CMD:

```bash
python create_database.py
```

## Running the API
To run the API, navigate to the directory where the 'Group 1 Ticketing System API\API Project' folder is located and run the following command in GIT CMD:

```bash
python app.py
```

## Using the API
Once the API is running, you can use the following commands to interact with it.

### `/Technicians`

|METHOD|`GET`|
|---|---|
|**Description**|Returns all technicians from the database|
|**Params**|*limit* (optional) parameter to limit the number of results returned, default is 10|

**Example Request**
http://localhost:5000/Technicians

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

### `/Technicians/Names`

|METHOD|`GET`|
|---|---|
|**Description**|Returns the first and last names of all the technicians|

**Example Request**
http://localhost:5000/Technicians/Names

**Example Response**
```json
[
    "Joseph Perez",
    "Michelle Reynolds",
    "Mary Patterson"
]
```
---

### `/TicketLines`

### `/Tickets`
|METHOD|`GET`|
|---|---|
|**Description**|Returns # of records in the Ticket table based on the optional parameter|
|**Params**|*limit* (optional) parameter to limit the number of results returned, default is 10|

**Example Request**
http://localhost:5000/Tickets

**Example Response**
```json

```
<a id="add-ticket"></a>
### `/Tickets`
|METHOD|`POST`|
|-------|-----|
|**Description**|Adds a new ticket|
|**Body**|Takes a json object with the following attributes: `user_id`, `department_id`, `prior_ticket_id`, `ticket_category`, `open_date_time`, `close_date_time`, `status`, `description`,`subject`|

**Example Request**
http://localhost:5000/Tickets

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
<a id="update-ticket"></a>
### `/Tickets/<ticket_id>`
|METHOD|`PUT`|
|-------|-----|
|**Description**|Updates a ticket|
|**Body**|Takes a json object with the following attributes: `user_id`, `department_id`, `prior_ticket_id`, `ticket_category`, `open_date_time`, `close_date_time`, `status`, `description`,`subject`|

**Example Request**
http://localhost:5000/Tickets/1

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
### `/Users`

<a id="delete-user"></a>
### `/Users/<user_id>`

|METHOD|`DELETE`|
|-------|-----|
|**Description**|Deletes a user|

**Example Request**
http://localhost:5000/Users/1

**Example Response**
```json
"Sucessfully removed the user"
```

### `/Organizations`

### `/Departments`

### `/Technicians/AvgTicketTimes`

### `/Technicians/TicketsInfo`

### `/Technicians/Manager`

### `/Technicians/Update`

### `/Users/TicketCounts`

### `/Departments/AvgResolutionTimes`

### `/Organizations/TicketCounts`




