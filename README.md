<h1 align="center"> :computer: Hack_The_Word (HTW) </h1>
<p align="center">
  <img src="https://raw.githubusercontent.com/RickDeckcard/Hack_The_Word/main/INFOGRAFIAS/hack_the_word_logo.png" width="350" title="Hack The Word logo create with Midjourney AI" alt="Image created with Midjourney AI">
</p>
<p align="center">
<a href="https://www.midjourney.com/">Midjourney AI creation</a>
</p>
<div>
<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/RickDeckcard/Hack_The_Word">
<img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/rickdeckard23">
</div>
<h2>:hourglass: Project functionalities</h2>
<ul>
  <li>Intelligence Wordlist: create wordlists about different methods of creating passwords.</li>
  <li>OSINT: help in the cyber-investigation process.</li>
  <li>El_espabilao: wordlist create with a lot of online example strongs passwords.</li>
  <li>Strongs passwords: help to create strongs passwords.</li>
</ul>
<h2>:white_check_mark: About the technology used.</h2>
<ul>
  <li>Operating system: Windows 10.</li>
  <li>Where work: cmd or powershell.</li>
  <li>Language: Python v.3.9.</li>
  <li>Others: Git, Dependencies.</li>
</ul>
<h2>:raising_hand: What is Hack The Word?</h2>
<p>
  It is a program created with the programming language Python 3.9 for the creation of wordlists intelligently for
use with password cracking programs. Its purpose is to exploit the attack vector related to the human factor. There are people
that use mnemonic rules or logical methods to create passwords, although these are stronger, they have a duty: they are predictable.
</p>
<h2>:ok_hand: Installation.</h2>
<p>
You must to download the repository to your harddisk using git or download the zip file.
</p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="git clone https://github.com/RickDeckcard/Hack_The_Word"><pre class="notranslate"><code>git clone https://github.com/RickDeckcard/Hack_The_Word</code></pre></div>
<p>
Access to the main folder and install requirements.(NOTE: if don??t work wit pip or python then try with pip3 or python3).
</p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="cd HACK_THE_WORD
pip install -r requirements
python HTW.py"><pre class="notranslate"><code>cd HACK_THE_WORD
pip install -r requirements
python HTW.py
</code></pre></div>
<h2>:key: Starting.</h2>
<p>
In the main menu you have options to start creating intelligence wordlists. You must understand before the passwords methods that a human could use to create a password. To understand how works the tool I recommended watch our videos.
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/RickDeckcard/Hack_The_Word/main/INFOGRAFIAS/main_menu_HTW.png" width="950" title="HTW main menu" alt="HTW main menu screenshot">
</p>
<p align="center">
<p>
The DATA.txt is the main file that use HTW to work. That file is in the HACK_THE_WORD folder. You can configurate it and add new lines. The correct format is the next:
</p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="Your_description:The_information"><pre class="notranslate"><code>Your_description:the_information</code></pre></div>
<p>
NOTE: It??s important that you don??t use spaces between Your_description the colon and The_information. You must use spaces in The_information, for example if the information is a letter song but you can??t use spaces in Your_description.
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/RickDeckcard/Hack_The_Word/main/INFOGRAFIAS/DATA_txt_screenshot.png" width="950" title="DATA_TXT content" alt="DATA_TXT content test screenshot">
</p>
<p align="center">
<h2>:passport_control: Create_my_pass.py</h2>
<p>
Create_my_pass.py is a script that help you to create an strong password. You must choose the lowercases, uppercases, symbols and numbers that you want. Then the script say you if that password is strong or not. After that you can select if the random number (entropy) would be automatic (A) or your selection (S).
To execute the script you must be in the folder HACK_THE_WORD and write:
<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="python Create_my_pass.py"><pre class="notranslate"><code>python Create_my_pass.py</code></pre></div>
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/RickDeckcard/Hack_The_Word/main/INFOGRAFIAS/Create_my_password_screenshot.png" width="950" title="Create_my_pass script" alt="Create_my_pass.py screenshot">
</p>
<p align="center">


Hack The Word (HTW) is a software to create intelligence wordlists to use in Pentesting brute force attacks
