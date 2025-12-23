@echo off
call tokens.bat
python cb2ai.py --prompt aism.md --model gpt-4.1
