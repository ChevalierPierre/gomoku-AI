import os
import sys

os.system("pip install pyinstaller --user")
os.system("pyinstaller *.py --name pbrain-gomoku-ai.exe --onefile")
if sys.platform == 'linux':
    os.system('cp ./dist/pbrain-gomoku-ai.exe .')
else:
    os.system('copy .\\dist\\pbrain-gomoku-ai.exe .')
