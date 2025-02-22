# LinkSaver

LinkSaver is a simple Python script that tracks the website you're on and records any changes to the URL in a `tracked_url.txt` file. This script is designed for Microsoft Edge so if you want to use a different browser, you will need to modify the script accordingly.  

## Why I Made This  

I created this for a video game that uses a "seed" system, where the seed value changes based on my actions. The website I use tracks these changes, allowing me to analyze and influence outcomes.  

For example, one seed-tracking link looks like this:  
[https://bc.godfat.org/?seed=2863890737&event=2025-02-22_959](https://bc.godfat.org/?seed=2863890737&event=2025-02-22_959)  
(The seed updates whenever you click on a cat.)  

---

## How to Use  

### 1. Clone the Repository  
Open a terminal and run:  

```sh
git clone https://github.com/frankierong101/LinkSaver.git
cd LinkSaver
```

### 2. (Optional) Set a Custom Starting URL  
- Open `tracked_url.txt` in a text editor.  
- Paste the URL you want to start from.  
- If left empty, the script defaults to the Apple website.  

### 3. Run the Script  
Run the following command in the terminal:  

```sh
pip install selenium webdriver-manager
python webExtract.py
```

### 4. Browse as Needed  
- The specified website (or the default Apple site) will open in Microsoft Edge.  
- Click around as needed—the script will track URL changes.  

### 5. Stop the Script  
- Close the browser.  
- In the terminal, press `Ctrl + C` to stop the script.  

### 6. Verify the Last Tracked URL  
To confirm that the last visited link was saved, you can:  
- Run:
```sh
notepad tracked_url.txt
```
  <br>  
  **OR**  
  <br>  
  
- Re-run:
```sh
python webExtract.py
```
