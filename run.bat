rem this comment line, only one command  line run at a time, run multiple command 
rem ========= CHORME browser command ===================================

pytest -s -v -m "sanity" --capture=tee-sys --html=./Reports/reportsChrome.html testCases/ --browser chrome
rem pytest -s -v -m "sanity or regression" --capture=tee-sys --html=./Reports/reportsChrome.html testCases/ --browser chrome
rem pytest -s -v -m "sanity and regression" --capture=tee-sys --html=./Reports/reportsChrome.html testCases/ --browser chrome
rem pytest -s -v -m "regression" --capture=tee-sys --html=./Reports/reportsChrome.html testCases/ --browser chrome

rem ========= Firefox browser command ===================================

rem pytest -s -v -m "sanity" --capture=tee-sys --html=./Reports/reportsFirefox.html testCases/ --browser firefox
rem pytest -s -v -m "sanity or regression" --capture=tee-sys --html=./Reports/reportsFirefox.html testCases/ --browser firefox
rem pytest -s -v -m "sanity and regression" --capture=tee-sys --html=./Reports/reportsFirefox.html testCases/ --browser firefox
rem pytest -s -v -m "regression" --capture=tee-sys --html=./Reports/reportsFirefox.html testCases/ --browser firefox




