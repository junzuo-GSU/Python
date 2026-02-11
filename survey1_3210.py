import matplotlib.pyplot as plt
import numpy as np

# Survey data
questions = [
    "Q1: Python First Language?",
    "Q2: Shell Scripting Knowledge",
    "Q3: Full-time Student?",
    "Q4: Textbook Plans",
    "Q5: Meeting Preference",
    "Q6: Operating System",
    "Q7: Linux/Unix Experience",
    "Q8: VS Code Experience"
]

# Response categories for each question
response_labels = [
    ["Yes", "No"],
    ["Neither", "Both", "Linux Only", "Windows Only"],
    ["Yes", "No (Part-time)"],
    ["Plan to Get", "Don't Plan"],
    ["Yes (Weekly)", "No (Async)", "Less Frequent"],
    ["Windows", "macOS", "Both"],
    ["Yes", "No"],
    ["Yes", "No"]
]

# Response percentages for each question
response_percentages = [
    [50.0, 50.0],
    [56.25, 12.5, 12.5, 18.75],
    [93.75, 6.25],
    [87.5, 12.5],
    [18.75, 43.75, 37.5],
    [50.0, 12.5, 37.5],
    [56.25, 43.75],
    [50.0, 50.0]
]

# Colors for the bars
colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#6A994E', 
          '#BC4B51', '#5B8E7D', '#F4A259']

# Create figure and subplots
fig, axes = plt.subplots(4, 2, figsize=(16, 20))
fig.suptitle('IT-3310 Course Survey Results Analysis\n(16 Students)', 
             fontsize=20, fontweight='bold', y=1.02)

# Flatten axes array for easy iteration
axes = axes.flatten()

# Plot each question
for idx, (ax, question, labels, percentages, color) in enumerate(zip(
    axes, questions, response_labels, response_percentages, colors)):
    
    # Create horizontal bar chart
    y_pos = np.arange(len(labels))
    bars = ax.barh(y_pos, percentages, color=color, edgecolor='black', alpha=0.8)
    
    # Add percentage labels on bars
    for bar, percentage in zip(bars, percentages):
        width = bar.get_width()
        ax.text(width + 1, bar.get_y() + bar.get_height()/2, 
                f'{percentage}%', va='center', fontweight='bold')
    
    # Set labels and titles
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlabel('Percentage (%)', fontsize=11)
    ax.set_title(f'{question}', fontsize=13, fontweight='bold', pad=10)
    ax.set_xlim([0, 105])  # Allow space for labels
    
    # Add grid for better readability
    ax.grid(True, axis='x', alpha=0.3, linestyle='--')
    
    # Remove spines for cleaner look
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('survey_analysis_chart.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("Chart saved as 'survey_analysis_chart.png'")

# Show the chart
plt.show()

# Create a summary pie chart for key metrics
fig2, axes2 = plt.subplots(2, 2, figsize=(14, 12))

# Key metrics to visualize
key_metrics = [
    ("Python Experience", ["New to Python", "Has Python Experience"], [50, 50], ['#FF6B6B', '#4ECDC4']),
    ("Shell Scripting Experience", ["No Experience", "Some Experience"], [56.25, 43.75], ['#FFD166', '#06D6A0']),
    ("Meeting Preference", ["Weekly", "Async/Infrequent"], [18.75, 81.25], ['#118AB2', '#EF476F']),
    ("VS Code Experience", ["Experienced", "New to VS Code"], [50, 50], ['#073B4C', '#FFD166'])
]

# Plot each key metric
for idx, (ax, title, labels, values, colors) in enumerate(zip(
    axes2.flatten(), 
    [m[0] for m in key_metrics],
    [m[1] for m in key_metrics],
    [m[2] for m in key_metrics],
    [m[3] for m in key_metrics]
)):
    wedges, texts, autotexts = ax.pie(
        values, 
        labels=labels, 
        colors=colors, 
        autopct='%1.1f%%', 
        startangle=90,
        textprops={'fontsize': 11}
    )
    
    # Make autotexts bold and white for better visibility
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax.set_title(f'{title}\n(n=16)', fontsize=14, fontweight='bold', pad=20)
    
    # Equal aspect ratio ensures pie is drawn as circle
    ax.axis('equal')

plt.suptitle('Key Survey Insights - IT-3310 Course', fontsize=18, fontweight='bold', y=1.02)
plt.tight_layout()

# Save the pie chart
plt.savefig('survey_key_insights.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("Pie chart saved as 'survey_key_insights.png'")

plt.show()

print("\n" + "="*60)
print("ANALYSIS INSIGHTS:")
print("="*60)
print("1. CLASS IS SPLIT: 50% are new to Python, 50% have experience")
print("2. SHELL SCRIPTING: 56% have NO experience with Linux/PowerShell")
print("3. MEETING PREFERENCE: Only 19% want weekly sync meetings")
print("4. VS CODE: 50% are new to the IDE (consider setup tutorials)")
print("5. TEXTBOOK: 88% plan to get the textbook")
print("6. OS PREFERENCE: 50% Windows, 38% comfortable with both")
print("="*60)