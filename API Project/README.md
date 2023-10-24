# Group 1 API Project - IT Ticket System

## Getting Started
To get started, you'll need to install the dependencies.

You can do this by navigating to the directory where 'API Project' is located and running the following command in GIT CMD:
```bash
pip install -r requirements.txt
```

## Running the API
To run the API, you can run the following command:
```bash
python app.py
```

## Using the API
Once the API is running, you can use the following commands to interact with it.

### Technicians

https://localhost:5000/Technicians

### `/Technicians`

|METHOD|`GET`|
|---|---|
|**Description**|Adds a new ticket|
|**Params**|*limit* (optional) parameter to limit the number of results returned, default is 10|

#### Example Request
http://localhost:5000/Tickets

#### Example Params
|Key|Value|
|---|---|
|limit|1|


#### Example Response:
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

#### Example Request
http://localhost:5000/Technicians/Names

#### Example Response:
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

#### Example Request
http://localhost:5000/Tickets

#### Example Response:
```json

```
<a id="add-ticket"></a>
### `/Tickets`
|METHOD|`POST`|
|-------|-----|
|**Description**|Adds a new ticket|
|**Body**|Takes a json object with the following attributes: `user_id`, `department_id`, `prior_ticket_id`, `ticket_category`, `open_date_time`, `close_date_time`, `status`, `description`,`subject`|

#### Example Request
http://localhost:5000/Tickets

#### Example Body
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

#### Example Response:
```json
"Sucessfully added a new ticket"
```
<a id="update-ticket"></a>
### `/Tickets/<ticket_id>`
|METHOD|`PUT`|
|-------|-----|
|**Description**|Updates a ticket|
|**Body**|Takes a json object with the following attributes: `user_id`, `department_id`, `prior_ticket_id`, `ticket_category`, `open_date_time`, `close_date_time`, `status`, `description`,`subject`|

#### Example Request
http://localhost:5000/Tickets/1

#### Example Body
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

#### Example Response:
```json
"Successfully updated the ticket"
```
### `/Users`

<a id="delete-user"></a>
### `/Users/<user_id>`

|METHOD|`DELETE`|
|-------|-----|
|**Description**|Deletes a user|

#### Example Request
http://localhost:5000/Users/1

#### Example Response:
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




