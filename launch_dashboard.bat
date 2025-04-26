@echo off
cd /d C:\Users\Thomas\Downloads\quant-projects-github-ready
set PYTHONPATH=.
streamlit run streamlit_app/dashboard.py --server.runOnSave true
pause
