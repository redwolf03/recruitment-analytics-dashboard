import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read Candidate Data
df = pd.read_excel('candidate_data.xlsx')

# Step 2: Create Summary Report by Status
status_summary = df['Status'].value_counts().reset_index()
status_summary.columns = ['Status', 'Count']

# Step 3: Save Summary to Excel
status_summary.to_excel('summary_report.xlsx', index=False)

# Step 4: Create Visualization (Bar Chart)
plt.figure(figsize=(6, 4))
plt.bar(status_summary['Status'], status_summary['Count'], color=['green', 'red', 'orange'])
plt.title('Candidate Status Summary')
plt.xlabel('Status')
plt.ylabel('Number of Candidates')
plt.savefig('status_chart.png')

print("Recruitment Analytics Dashboard Generated Successfully!")
