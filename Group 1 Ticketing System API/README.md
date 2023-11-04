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
  - [PUT Calls](#put-calls)
    - [`/Tickets`](#tickets-1)
  - [DELETE Calls](#delete-calls)
    - [`/Users`](#users-1)


</br>

# Getting Started
To get started, you'll need to install the dependencies.

You can do this by navigating to the directory where the 'Group 1 Ticketing System API' folder is located and running the following command in GIT CMD:
```bash
pip install -r requirements.txt
```
---

**Sending Requests:**

The **Example Request** sections will contain references in the style of 'GET /Departments?limit={limit}'. You will need to add the address where the API is running to the front of the example.

**Example:**\
http://localhost:5000/Technicians

---

</br>

# Creating the database
You can create/recreate the database at any time, navigate to the directory where the 'Group 1 Ticketing System API\API Database Creator' folder is located and run the following command in GIT CMD:

```bash
python create_database.py
```

</br>

# Running the API
To run the API, navigate to the directory where the 'Group 1 Ticketing System API\API Project' folder is located and run the following command in GIT CMD:

```bash
python app.py
```

</br>

# Using the API
Once the API is running, you can use the following commands to interact with it.

</br>

## GET Calls

### `/Departments`

|METHOD|`GET`|
|---|---|
|**Description**|Returns all departments from the database|
|**Params**|*limit* (optional) parameter to limit the number of results returned, default is 10|

**Example Requests**\
GET /Departments\
GET /Departments?limit={limit}

**Example Params**
|Key|Value|
|---|---|
|limit|1|


**Example Response:**
```json
[
    {
        "Department ID": 1,
        "Email Address": "ghill@ward.com",
        "Name": "Human Resources",
        "Organization ID": 1,
        "Phone Number": "+1-956-557-2067"
    }
]
```

---

### `/Departments/AvgResolutionTimes`

|METHOD|`GET`|
|---|---|
|**Description**|Returns average ticket resolution time by departments from the database|

**Example Request**\
GET /Departments/AvgResolutionTimes


**Example Response:**
```json
[
    {
        "Average Resolution Time": "2:46:09.230769",
        "Department Name": "Administration"
    },
    {
        "Average Resolution Time": "-1 day, 14:34:17.142857",
        "Department Name": "Customer Service"
    },
    {
        "Average Resolution Time": "6:51:25.714286",
        "Department Name": "Facilities Management"
    }
]
```
---

### `/Organizations`

|METHOD|`GET`|
|---|---|
|**Description**|Returns all organizations from the database|
|**Params**|*limit* (optional) parameter to limit the number of results returned, default is 10|

**Example Request**\
GET /Organizations\
GET /Organizations?limit={limit}

**Example Params**
|Key|Value|
|---|---|
|limit|1|


**Example Response:**
```json
[
    {
        "City": "Deanside",
        "Email Address": "richardsoncarolyn@coleman.com",
        "Name": "Tech Solutions Inc.",
        "Organization ID": 1,
        "Phone Number": "217.599.4048x926",
        "State": "NE",
        "Street Adress": "465 Kevin Ports",
        "ZipCode": 64664
    }
]
```
---

### `/Organizations/TicketCounts`
|METHOD|`GET`|
|---|---|
|**Description**|Returns number of tickets by organizations from the database|

**Example Request**\
GET /Organizations/TicketCounts

**Example Response:**
```json
[
    {
        "Organization Name": "Acme Corporation",
        "Ticket Count": "1"
    },
    {
        "Organization Name": "Global Enterprises",
        "Ticket Count": "0"
    }
]
```
---


### `/Technicians`

|METHOD|`GET`|
|---|---|
|**Description**|Returns all technicians from the database|
|**Params**|*limit* (optional) parameter to limit the number of results returned, default is 10|

**Example Request**\
GET /Technicians\
GET /Technicians?limit={limit}

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

|METHOD|`GET`|
|---|---|
|**Description**|Returns the first and last names of all the technicians, along with their technician id and the average time it takes them to complete a ticket|

**Example Request**\
GET /Technicians/AvgTicketTimes

**Example Response**
```json
[
    {
        "average_ticket_time": "2 days, 9:43:15.435567",
        "first_name": "Jorge",
        "last_name": "Rocha",
        "technician_id": 1
    }
]
```
---




### `/Technicians/Manager`

|METHOD|`GET`|
|---|---|
|**Description**|Retrieves the first name, last name, and user id of the technician's manager, as well as the first name, last name, and technician id of the technician whose id is passed to in the parameters|
|**Params**|technician_id - The id of the technician whose manager is getting retrieved|

**Example Request**\
GET /Technicians/Manager?technician_id={technician_id}

**Example Params**
|Key|Value|
|---|---|
|technician_id|1|

**Example Response**
```json
{
    "manager_first_name": "Megan",
    "manager_last_name": "Brown",
    "manager_user_id": 5,
    "technician_first_name": "Tony",
    "technician_id": 2,
    "technician_last_name": "Hamilton"
}
```
---

### `/Technicians/Names`

|METHOD|`GET`|
|---|---|
|**Description**|Returns the first and last names of all the technicians|

**Example Request**\
GET /Technicians/Names

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
|METHOD|`GET`|
|---|---|
|**Description**|Retrieves ticket information for each technician based on technician Id|
|**Params**|technician_id - The id of the technician whose tickets are being retrieved|

**Example Request**\
GET /Technicians/TicketsInfo?technician_id={technician_id}

**Example Params**
|Key|Value|
|---|---|
|technician_id|1|

**Example Response**
```json
[
    {
        "close_date_time": "Wed, 18 Oct 2023 22:10:17 GMT",
        "notes": "Country outside smile bad space form option. Only reflect score marriage. Increase account stay Democrat spend benefit lay system. Dog fly benefit return.",
        "open_date_time": "Wed, 18 Oct 2023 20:10:17 GMT",
        "prior_ticket_id": 5,
        "status": "Active",
        "subject": "Server connection problem",
        "ticket_category": "Non-Emergency",
        "ticket_id": 1
    }
]
```
---


### `/Tickets`
|METHOD|`GET`|
|---|---|
|**Description**|Returns ticket records from the Ticket table|
|**Params**|*limit* (optional) parameter to limit the number of results returned, default is 10|

**Example Requests**\
GET /Tickets\
GET /Tickets?limit={limit}

**Example Params**
|Key|Value|
|---|---|
|limit|1|

**Example Response**
```json
[
    {
        "Close Date Time": "Wed, 18 Oct 2023 22:10:17 GMT",
        "Department ID": 2,
        "Description": "I can't connect to the server",
        "Open Date Time": "Wed, 18 Oct 2023 20:10:17 GMT",
        "Prior Ticket ID": 5,
        "Status": "Active",
        "Subject": "Server connection problem",
        "Ticket Category": "Non-Emergency",
        "Ticket ID": 1,
        "User ID": 1
    }
]
```
---
### `/TicketLines`

|METHOD|`GET`|
|---|---|
|**Description**|Returns all ticketlines from the database|
|**Params**|*limit* (optional) parameter to limit the number of results returned, default is 10|

**Example Requests**\
GET /TicketLines\
GET /TicketLines?limit={limit}

**Example Params**
|Key|Value|
|---|---|
|limit|1|


**Example Response:**
```json
[
    {
        "Assignment Date Time": "Thu, 09 Jan 2020 05:56:20 GMT",
        "Completion Date Time": "Mon, 30 Jan 2023 10:32:27 GMT",
        "Notes": "No west strong bill. Consider realize poor thus these. None teacher sometimes thousand necessary.\nAgain door cost challenge determine enjoy course. Board people chair close. Bag expert remain sound.",
        "Technician ID": 2,
        "Ticket ID": 1
    },
    {
        "Assignment Date Time": "Fri, 30 Jul 2021 06:30:29 GMT",
        "Completion Date Time": "Mon, 21 Aug 2023 22:02:04 GMT",
        "Notes": "Person boy focus idea old politics. Evening five find nor include or. Away so tough when spring.\nKnowledge since mouth course TV. Section yes star will someone always note.",
        "Technician ID": 2,
        "Ticket ID": 1
    }
]
```
---

### `/Users`

|METHOD|`GET`|
|---|---|
|**Description**|Returns all users from the database|
|**Params**|*limit* (optional) parameter to limit the number of results returned, default is 10|

**Example Requests**\
GET /Users\
GET /Users?limit={limit}

**Example Params**
|Key|Value|
|---|---|
|limit|1|


**Example Response:**
```json
[
    {
        "Department ID": 1,
        "Email Address": "brittanywilson@example.net",
        "First Name": "Vernon",
        "Last Name": "Thompson",
        "Organization ID": 1,
        "Phone Number": "+1-800-321-5258x31825",
        "Title": "Buyer, retail"
    },
    {
        "Department ID": 1,
        "Email Address": "ylittle@example.com",
        "First Name": "Anthony",
        "Last Name": "Freeman",
        "Organization ID": 1,
        "Phone Number": "+1-212-815-0992x2826",
        "Title": "Paediatric nurse"
    }
]
```
---

### `/Users/TicketCounts`

|METHOD|`GET`|
|---|---|
|**Description**|Returns numbers of tickets by users from the database|

**Example Request**\
GET /Users/TicketCounts

**Example Response:**
```json
[
    {
        "First Name": "Vernon",
        "Last Name": "Thompson",
        "Ticket Count": "2"
    },
    {
        "First Name": "Anne",
        "Last Name": "Alvarez",
        "Ticket Count": "5"
    },
    {
        "First Name": "Ashley",
        "Last Name": "Livingston",
        "Ticket Count": "3"
    }
]
```
---

</br>

## POST Calls

### `/Technicians`
|METHOD|`POST`|
|-------|-----|
|**Description**|Updates the manager of a technician|
|**Params**|technician_id - The id of the technician whose manager is getting updated|
| |manager_user_id - The user id of the new manager |

**Example Request**\
POST /Technicians?technician={technician_id}&manager_user_id={manager_user_id}

**Example Params**
|Key|Value|
|---|---|
|technician_id|1|
|manager_user_id|2|

**Example Response**
```json
{
    "manager_user_id": 2,
    "technician_id": 1,
    "technician_user_id": 80
}
```
---

</br>

## PUT Calls

<a id="update-ticket"></a>
### `/Tickets`
|METHOD|`PUT`|
|-------|-----|
|**Description**|Updates a ticket|
|**Body**|Takes a json object with the following attributes: `user_id`, `department_id`, `prior_ticket_id`, `ticket_category`, `open_date_time`, `close_date_time`, `status`, `description`,`subject`|
|**Params**|ticket_id - The id of the ticket to update|

**Example Request**\
PUT /Tickets\
PUT /Tickets?ticket_id={ticket_id}

**Example Params**
|Key|Value|
|---|---|
|ticket_id|1|

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
---

</br>

## DELETE Calls

### `/Users`

|METHOD|`DELETE`|
|-------|-----|
|**Description**|Deletes a user|
|**Params**|user_id - The id of the user to delete|

**Example Request**\
DELETE /Users?user_id={user_id}

**Example Params**
|Key|Value|
|---|---|
|user_id|1|

**Example Response**
```json
"User deleted Successfully!"
```
---