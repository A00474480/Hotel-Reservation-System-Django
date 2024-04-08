# Django REST API for Hotel Reservation

## Overview

This Django REST API facilitates hotel reservations, allowing users to view a list of hotels and add new hotels to the system. It demonstrates the use of Django REST Framework for building RESTful APIs.

## Endpoints

### Get List of Hotels

- **Endpoint:** `GET /hotelreservation/gethotelslist/`
- **Description:** Fetches a list of all hotels available in the database.
- **CURL Example:**
  ```
  curl --location 'http://127.0.0.1:8000/hotelreservation/gethotelslist/'
  ```

### Add a New Hotel

- **Endpoint:** `POST /hotelreservation/addhotel/`
- **Description:** Adds a new hotel to the database.
- **CURL Example:**
  ```
  curl --location 'http://127.0.0.1:8000/hotelreservation/addhotel/' \
  --header 'Content-Type: application/json' \
  --data '{
      "hotelName": "Taj",
      "availability": true,
      "price": "800.00"
  }'
  ```
