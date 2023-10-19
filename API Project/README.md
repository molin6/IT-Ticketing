
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
---------------------
<a id="update-ticket"></a>
### `/Tickets/{ticket_id}`

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
"Sucessfully updated the ticket"
```
---------------------
<a id="delete-user"></a>
### `/Users/{user_id}`

|METHOD|`DELETE`|
|-------|-----|
|**Description**|Deletes a user|

#### Example Request
http://localhost:5000/Users/1

#### Example Response:
```json
"Sucessfully removed the user"
```