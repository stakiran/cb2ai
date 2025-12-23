@echo off
call tokens.bat
python cb2ai.py --prompt douiu.md --model gpt-4o
