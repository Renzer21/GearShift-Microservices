@echo off
echo Starting GearShift Project Microservices...

:: API Gateway
echo Starting API Gateway (Port 8000)...
start "API Gateway" cmd /k "cd api_gateway && uvicorn main:app --port 8000 --reload"

:: Parts Service
echo Starting Parts Service (Port 8001)...
start "Parts Service" cmd /k "cd parts_service && uvicorn main:app --port 8001 --reload"

:: Customer Service
echo Starting Customer Service (Port 8002)...
start "Customer Service" cmd /k "cd customer_service && uvicorn main:app --port 8002 --reload"

:: Order Service
echo Starting Order Service (Port 8003)...
start "Order Service" cmd /k "cd order_service && uvicorn main:app --port 8003 --reload"

:: Supplier Service
echo Starting Supplier Service (Port 8004)...
start "Supplier Service" cmd /k "cd supplier_service && uvicorn main:app --port 8004 --reload"

echo All services are starting up! 
echo API Gateway is available at http://localhost:8000/docs
pause