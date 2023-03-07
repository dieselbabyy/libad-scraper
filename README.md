# libad-scraper
A simple Python web scraper using BeautifulSoup to collect/archive Libad5343 token metadata

To use this, you must have python installed on your computer, if you are on Windows you can do this on Windows but honestly the best way to do it (on Windows) would be via WSL2 (Windows Subsystem for Linux).  I know it probably sounds complicated, but it's actually insanely easy to install.

## Installation

All you have to do to install WSL (which will allow you to run Python and all kinds of other cool stuff natively as if it were on an actual linux OS, while never having to leave Windows or bother with any kind of virtual machines or complicated partitioning/dual booting).  There are two ways to do this.

### The first (and easier) way:
*Note: for users on Windows 10 v.2004 or later and Windows 11*
- Click on "Start" in Windows and search for **"Command Prompt"**
- Right-click on the result and select **"Run as administrator"
- In the command prompt window that opens, type in the following text, then hit enter:
`wsl --install -d Ubuntu-20.04`

This will download the Windows Subsystem for Linux packages and install a build of Ubuntu on your machine.  Restart your computer and *that's it.*

### The second way:
*Note: This used to be the main method but is unnecessarily complicated and dumb now*
- Click on "Start" and search for **Turn Windows features on or off** and select the top result.
- Make sure that you have the **Enable virtual machine platform** selected and enabled.  Click to restart your machine if it wasn't enabled. 
- Open the Microsoft Store app
- Search for "Windows Subsystem for Linux" or alternatively [click here](https://www.microsoft.com/store/productId/9P9TQF7MRM4R) and install the WSL base app.
- Once the WSL base app is installed, install [Ubuntu 20.04.5 LTS](https://www.microsoft.com/store/productId/9MTTCL66CPXJ)
- Restart your machine and all that other goodness.  In the rare event you have to update the WSL kernel, run the **Command Prompt** as administrator and enter `wsl --update`

## Once you have WSL2 Ubuntu installed on your machine

Once you have Ubuntu installed on your machine, you'll see an Ubuntu app icon just like any other app in your taskbar/start menu...it should be an orange icon.  Click on it and follow any prompts it gives you to set up an administrator username and password.  

Once you're done, you'll be at a blank terminal window.  

We're going to update apt (Ubuntu's package manager) and make sure your repositories are up-to-date.  To do this, type in `sudo apt-get update && apt-get upgrade -y` and hit enter.  You'll be asked to enter in the password you set just earlier and then it'll run on it's own, should take a minute or two.

Now we're ready to install Python and pip (a Python package manager). Type `apt-get install python3 && apt-get install pip3` and hit enter.  It may ask you to **press Y** for yes to confirm, then let it install.  This should take a few minutes.

### Adding BeautifulSoup to Python

Last step, I promise.  Just type in `pip3 install BeautifulSoup4` and hit enter.  That's it.

## How to use this script

To use this script, download the file to your computer and save it locally to your hard drive.  I would suggest creating a folder at the base of your C:\ drive, like C:\linux or whatever you want to call it, to make it easy to work with files in WSL2.  You can edit any of the variables in the script, they are all commented for ease of use and to make it easy for configuring to your use. 

For example, to change the parameters so that it will yield the results from token ID number 50,000 through 55,000 you will just have to change the numbers in the parantheses of `for i in range(1, 1000):` to instead be `for i in range(50000, 55000):`  To edit this file, you should use a proper text editor or IDE -- do **not** use Notepad, it will mess with the file formatting.  I suggest [Sublime Text](https://sublimetext.com) which you can download for free.  Save the file to your C:\linux folder.

Now to run the script, open your **Ubuntu** terminal window back up.

We'll need to change your working directory.  By default, this is set to be `/home/username` so, for me it'd be `/home/dieselbaby`.  You can always see what directory you are in by typing in `pwd` and hitting enter.  This will **p**rint the **w**orking **d**irectory.  To change you're going to type `cd /mnt/c/linux` and hit enter.  (Change directory, to your mounted C drive and then the linux folder mentioned earlier.)

You can check you're in the right place by typing in `ls -lah` and hit enter.  This will list all of the files in your current directory.  You should see the `getdata.py` file you downloaded from this repository in there.

## And finally, some magic

Now that you're in the right directory, all you need to do is type in `python3 getdata.py` and hit enter.

The script is set to automatically print the current URL of the page/token ID being scraped.  IF you want to check and see what the current token ID is up to, [here's a link to the contract address for LIBAD5343 on Polygonscan](https://polygonscan.com/token/0xc57c718cd35265fbe225d09384ad824b6c976ae0)

The results will be automatically put into a CSV (excel spreadsheet) document when it's done, saved in your C:\linux folder as `metadata-results.csv`  

*Note: it's best to do this in smaller batches, I would recommend limiting this to several thousand at once to not overwhelm the server and get rate-limited.  Then you should **move** the metadata-results.csv file to another folder on your hard drive or rename your existing file(s) because otherwise it will get overwritten if you change the range parameters and run the script again.*

Happy hunting!
<3 Dieselbaby
