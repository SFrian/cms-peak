CMSeeK Results Merger

This repository contains CMSeeK scan results and a Python script to merge all cms.json files into a single JSON file for easier analysis.

📂 Repository Structure

📂 cmseek-results
 ├── 📂 Result/              # CMSeeK scan results (each target has its own folder)
 ├── 📜 merge_cmseek_results.py  # Script to merge JSON results
 ├── 📜 .gitignore           # Ignore unnecessary files
 ├── 📜 README.md            # Documentation
 ├── 📜 merged_results.json  # Final merged result (after running script)

🚀 How to Use

Run the Python script to merge results:

python merge_cmseek_results.py

This will generate merged_results.json, which contains all scan results in one file.

Upload the results to GitHub:

git add .
git commit -m "Updated scan results"
git push origin main

📌 Notes

Make sure all CMSeeK scan results are inside the Result/ folder before running the script.

merged_results.json will be overwritten each time you run the script.

📧 Contact

If you have any questions or issues, feel free to open an issue or reach out!

✅ Simplify your CMSeeK results analysis with this script!

