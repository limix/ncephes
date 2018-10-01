call ci\set-win-path.bat

powershell -Command "(New-Object Net.WebClient).DownloadFile('https://raw.githubusercontent.com/limix/hcephes/master/install.bat', 'install-hcephes.bat')"