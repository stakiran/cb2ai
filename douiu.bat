@echo off
pushd %~dp0
call tokens.bat
python cb2ai.py --prompt douiu.md --model gpt-5.2
