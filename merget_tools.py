import os
import json

# Path to the CMSeeK results folder
results_dir = "Result"
output_file = "merged_results.json"

merged_data = []

# Loop through each subfolder in the Result directory
for folder in os.listdir(results_dir):
    cms_json_path = os.path.join(results_dir, folder, "cms.json")

    # Check if cms.json exists in the subfolder
    if os.path.isfile(cms_json_path):
        try:
            with open(cms_json_path, "r") as json_file:
                data = json.load(json_file)
                merged_data.append(data)  # Append data to list
        except json.JSONDecodeError:
            print(f"Error reading {cms_json_path}, skipping.")

# Save merged data into a single JSON file
with open(output_file, "w") as output_json:
    json.dump(merged_data, output_json, indent=4)

print(f"✅ Merged all results into {output_file}")
