# LinkSaver

This is a simple Python script that tracks the website you're on and records any changes to the URL in a tracked_url.txt file. I created this because I play a video game where it has a "seed" feature. This "seed" changes depending on what actions I take during specific parts of the game. I use this linksaver script on a website that tracks every change to my seed. [one random seed of the website I'm talking about is https://bc.godfat.org/?seed=2863890737&event=2025-02-22_959]

To use:

1. clone the repo into an empty folder
1.b (optional) insert a link you want into the txt file, if you don't it will default to the apple website
2. enter the folder from step 1 using command prompts in a terminal
3. copy paste "python webExtract.py" and press enter
4. The site you entered or the default apple site will appear in a new edge browser, you can click around until you want to close it
5. Close the browser and in the terminal press "ctrl + c" to stop the script, then to double check that your last visited link is saved, you can run the file again(step 3) or open the "tracked_url.txt" file to confirm it's been updated 
