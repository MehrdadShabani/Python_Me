@echo off
cd /d "C:\Users\ASUS\Desktop\python_Me"
git add .
git commit -m "Auto backup on %date% %time%"
git push origin main
