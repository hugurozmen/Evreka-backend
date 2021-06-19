# Evreka Backend

Hi! Thats a repo for Evreka's backend intern questions.


# Q1

The function which is requested for question 1 is in  here. [function](https://github.com/hugurozmen/Evreka-backend/blob/main/Q1/navRecords/records/views.py)

## For getting this data in a more efficient way

As a second better alternative, I thought of using nosql. A **mongodb** or **elasticsearch** style database will produce faster results than normal databases in storing incoming records and processing data.
normal databases are fast only in querying and consistency of data. If there is too much incoming data traffic, a backend design can be made by putting a nosql on the front and a sql database on the back for backup and other works.

# Q2

The Execution model is added to solve the many to many problem and to store collection
frequency and last collection time of bins by operation.

![ER Diagram](https://github.com/hugurozmen/Evreka-backend/blob/main/ER-Diagram.png)

## Requested Function
The function which is requested for question 2 is in  here. [function](https://github.com/hugurozmen/Evreka-backend/blob/main/Q2/binOperation/binOperation/bin/views.py)

