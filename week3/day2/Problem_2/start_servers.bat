@echo off
echo Starting Multimodal QA Agent...
echo.

echo Starting Flask Backend...
start "Flask Backend" cmd /k "cd /d "d:\misogiai week2\week3\day2\Problem_2\backend" && python app.py"

timeout /t 3 /nobreak >nul

echo Starting React Frontend...
start "React Frontend" cmd /k "cd /d "d:\misogiai week2\week3\day2\Problem_2\frontend" && npm run dev"

echo.
echo Both servers are starting...
echo Backend will be available at: http://localhost:5000
echo Frontend will be available at: http://localhost:3000
echo.
echo Make sure you have set up your .env file in the backend directory with your OpenAI API key!
pause
