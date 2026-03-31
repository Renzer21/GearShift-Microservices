# GearShift - Motorbike Spare Parts Management System
**IT4020 - Modern Topics in IT | Group Assignment**

### Domain: Automobile / Spare Parts

## Microservices Overview

| Service | Port | Swagger UI (Direct Access) |
| :--- | :--- | :--- |
| **API Gateway** | 8000 | [http://localhost:8000/docs](http://localhost:8000/docs) |
| **Parts Service** | 8001 | [http://localhost:8001/docs](http://localhost:8001/docs) |
| **Customer Service** | 8002 | [http://localhost:8002/docs](http://localhost:8002/docs) |
| **Order Service** | 8003 | [http://localhost:8003/docs](http://localhost:8003/docs) |
| **Supplier Service** | 8004 | [http://localhost:8004/docs](http://localhost:8004/docs) |

---

## Setup Instructions

**1. Install Dependencies**
First, ensure you have MongoDB running on your local machine. Then, install the required Python packages:
```bash
pip install fastapi uvicorn motor httpx pydantic

2. Run All Services
Open 5 separate terminals in your VS Code (in the main project folder) and run the following commands:

Terminal 1 - API Gateway:

Bash

uvicorn api_gateway.main:app --port 8000 --reload
Terminal 2 - Parts Service:

Bash

uvicorn parts_service.main:app --port 8001 --reload
Terminal 3 - Customer Service:

Bash

uvicorn customer_service.main:app --port 8002 --reload
Terminal 4 - Order Service:

Bash

uvicorn order_service.main:app --port 8003 --reload
Terminal 5 - Supplier Service:

Bash

uvicorn supplier_service.main:app --port 8004 --reload
Testing the Application
Direct Access: You can test each individual microservice by visiting its specific Swagger UI URL (e.g., http://localhost:8001/docs).

Via API Gateway (The Correct Architecture): Visit http://localhost:8000/docs to interact with all four microservices through a single entry point.

Architecture Diagram
Plaintext

       [ Client / Frontend Application ]
                        │
                        ▼
            [ API Gateway (Port 8000) ]
                        │
      ┌─────────┬───────┴───────┬─────────┐
      │         │               │         │
      ▼         ▼               ▼         ▼
  [ Parts ] [Customer]      [ Orders ] [Supplier]
(Port 8001) (Port 8002)     (Port 8003) (Port 8004)
Why an API Gateway?
The API Gateway eliminates the need for the frontend client to memorize or manage multiple ports. All requests are securely routed through a single entry point (http://localhost:8000), demonstrating a proper industry-standard microservices architecture.

## Running the Application (Windows)

To start all microservices and the API Gateway simultaneously, you can use the provided batch script.

1.  Make sure you have installed all dependencies:
    ```bash
    pip install fastapi uvicorn motor httpx pydantic
    ```
2.  Ensure your **MongoDB** server is running.
3.  Run the following command in the root directory:
    ```powershell
    .\start_all.bat
    ```

This will launch 5 separate terminal windows for each service (Gateway, Parts, Customer, Order, and Supplier).
