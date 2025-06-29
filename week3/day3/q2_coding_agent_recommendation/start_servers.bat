@echo off
echo Starting AI Coding Agent Recommendation System...
echo.

echo Installing backend dependencies...
cd backend 2>nul || echo Backend directory not found, using current directory
pip install -r requirements.txt

echo.
echo Starting Flask Backend...
start "Flask Backend" cmd /k "cd /d "d:\misogiai week2\week3\day3\q2_coding_agent_recommendation" && python app.py"

timeout /t 3 /nobreak >nul

echo Installing frontend dependencies...
cd frontend
call npm install

echo.
echo Starting React Frontend...
start "React Frontend" cmd /k "cd /d "d:\misogiai week2\week3\day3\q2_coding_agent_recommendation\frontend" && npm run dev"

echo.
echo Both servers are starting...
echo Backend will be available at: http://localhost:5000
echo Frontend will be available at: http://localhost:3000
echo.
pause
