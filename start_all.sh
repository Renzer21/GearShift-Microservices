#!/bin/bash

echo "Starting Hospital Management System Microservices..."

# Gateway එක start කිරීම
echo "Starting Gateway..."
cd gateway && python main.py &
cd ..

# අනිත් services start කිරීම
echo "Starting Appointment Service..."
cd appointment-service && python main.py &
cd ..

echo "Starting Doctor Service..."
cd doctor-service && python main.py &
cd ..

echo "Starting Patient Service..."
cd patient-service && python main.py &
cd ..

echo "Starting Prescription Service..."
cd prescription-service && python main.py &
cd ..

echo "All services started! Press [CTRL+C] to stop them all."

# terminal එක close වීම වැලැක්වීමට
wait