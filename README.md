# Score Distribution Analyzer - Streamlit Web App

## 📋 What You'll Need

1. Python 3.7 or higher installed on your computer
2. The three files from this project:
   - `streamlit_app.py` (the web app)
   - `score_analysis.py` (the analysis functions)
   - `requirements.txt` (the dependencies)

---

## 🚀 Step-by-Step Setup Instructions

### Step 1: Install Streamlit

Open your terminal or command prompt and run:

```bash
pip install streamlit
```

Or if you're using pip3:

```bash
pip3 install streamlit
```

**Note**: If you get a permission error, try:
```bash
pip install streamlit --user
```

---

### Step 2: Organize Your Files

Make sure all three files are in the same folder:
```
your-project-folder/
├── streamlit_app.py
├── score_analysis.py
└── requirements.txt
```

---

### Step 3: Navigate to Your Project Folder

Open your terminal/command prompt and navigate to the folder containing your files:

```bash
cd path/to/your-project-folder
```

For example:
- Windows: `cd C:\Users\YourName\Documents\score-analyzer`
- Mac/Linux: `cd ~/Documents/score-analyzer`

---

### Step 4: Run the Streamlit App

Run this command:

```bash
streamlit run streamlit_app.py
```

---

### Step 5: Access the Web App

After running the command, you should see output like:

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.x:8501
```

Your default web browser should automatically open to `http://localhost:8501`

If it doesn't open automatically, just copy the Local URL and paste it into your browser.

---

## 🎯 How to Use the App

1. **Enter Number of Respondents**: Type the total number of people providing ratings (e.g., 10)

2. **Enter From Average Score**: Type your starting average (e.g., 3.0)

3. **Enter To Average Score**: Type your target average (e.g., 3.5)

4. **Click "Analyze Distribution"**: The app will show you:
   - How many of each score (1-5) you'd expect on average
   - The percentages for each score
   - The differences between the two averages

---

## 🛑 Stopping the App

To stop the app, go back to your terminal and press:
- **Ctrl + C** (Windows/Linux)
- **Cmd + C** (Mac)

---

## 💡 Tips

- **Try different values**: Experiment with different respondent counts and averages
- **Impossible averages**: The app will tell you when an average isn't mathematically possible and suggest alternatives
- **Refresh**: If you update the code, save your changes and the app will automatically reload

---

## ⚠️ Troubleshooting

### "Command not found: streamlit"
- Make sure you've installed streamlit: `pip install streamlit`
- Try using the full path: `python -m streamlit run streamlit_app.py`

### "ModuleNotFoundError: No module named 'score_analysis'"
- Make sure `score_analysis.py` is in the same folder as `streamlit_app.py`

### Port already in use
- If port 8501 is busy, streamlit will automatically try the next available port (8502, 8503, etc.)
- Or you can specify a different port: `streamlit run streamlit_app.py --server.port 8502`

---

## 📱 Sharing Your App

Want to share your app with others?

1. **Local network**: Share the Network URL with others on your wifi
2. **Deploy online**: Use Streamlit Community Cloud (free) at https://streamlit.io/cloud
3. **Save results**: Take screenshots of the results to share

---

## 🎓 Next Steps

Once you're comfortable with the basic app, you can:
- Add charts and visualizations
- Export results to CSV
- Add more comparison options
- Customize the styling with Streamlit themes

Explore the Streamlit documentation: https://docs.streamlit.io/

---

Enjoy analyzing your score distributions! 📊
