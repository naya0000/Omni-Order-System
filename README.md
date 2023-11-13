# Omni Order System

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
---
## Project Structure
* **Order** Model in **api** app: 
    * Order-number
    * Total-price
    * Created-time
* **Product** model
    * Relationships between **Order** and **Product** model
* **import_order** api: 
    * Validate access token from request data
        ( accepted token is defined in **api/views.py** )
    * Parse data and Save to corresponding fields
* Api unittest
---

* Feel free to let us know if there is any question: shelby.xiao@omniscientai.com
