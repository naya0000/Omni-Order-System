# Omni Order System

This is a Django-based API for managing and tracking orders. 

This project provides a robust system for importing orders, tracking their status over time, and ensuring secure access through token validation.

## Setup Environment
* Download [docker](https://www.docker.com/get-started) and Install

* Clone **pretest** project from your own repository
    ```
    git clone https://github.com/naya0000/pretest.git
    ```

* Checkout **pretest** directory
    ```
    cd pretest
    ```

* Start docker container
    ```
    docker-compose up
    ```

* Enter activated **pretest-web-1** container
    ```
    docker exec -it pretest-web-1 bash
    ```
    Note:

    * This container codebase is connected to **pretest** project local codebase
    * If you need to migrate migration files or test testcases, make sure do it in **pretest-web-1** container
* Install dependencies
      ```
      pip install -r requirements.txt
      ```
## Configuration
* Update database settings in settings.py

* Apply migrations:
    ```
    python manage.py migrate
    ```
  
---
## Features

- **Order Import:** Import orders with details such as order number, total price, payment status, and shipping address.

- **Order Status Tracking:** Track the status of orders over time, capturing progress and changes.

- **Access Token Validation:** Secure the import endpoint with an access token to ensure data integrity.

- **Django REST Framework Integration:** Utilize the Django REST Framework for efficient API development.

## API Endpoints

### Import Order

- **Endpoint:** `/api/import_order/`
- **Method:** `POST`
- **Parameters:**
  - `access_token` (string): Your access token for authentication.
  - `order_number` (string): Order number for the imported order.
  - `total_price` (decimal): Total price of the order.
  - `created_time` (datetime): Timestamp indicating when the order was created.
  - `payment_status` (string, optional): Payment status of the order (default: 'pending').
  - `shipping_address` (string, optional): Shipping address for the order.
- **Response:** 200 OK if the order is successfully imported, 400 Bad Request for invalid data or access token.

## Testing

### Unit Tests

- **Import Order Test:**
  - Create a test order using the import endpoint.
  - Validate that the order and initial status are correctly created.
  - Test with both valid and invalid access tokens.

- **Order Item Test:**
  - Create an order item and validate its creation and string representation.

- **Order Status Test:**
  - Create an order status and validate its creation and association with an order.

### Integration Tests

- **API Integration Test:**
  - Test the overall functionality of the API by simulating requests and checking responses.
  - Include scenarios with valid and invalid data.

### Running Tests

Run the tests using the following command:

```bash
python manage.py test
```
---
