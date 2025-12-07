import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. DATA PREPARATION
# ==========================================
data = {
    'Category': [
        'Forest', 'Forest', 'Forest',
        'Biodiversity', 'Biodiversity', 'Biodiversity', 'Biodiversity', 'Biodiversity',
        'Wetlands', 'Wetlands', 'Wetlands',
        'Desert', 'Desert', 'Desert', 'Desert'
    ],
    'Indicator': [
        'Forest Area', 'Forest Stock Volume', 'Forest Coverage',
        'Higher Plant Species', 'Algae Species', 'Fungi Species', 'National Key Protected', 'CITES Appendix',
        'Total Wetland Area', 'Wetland Share of Area', 'Natural Wetland Rate',
        'Desertified Land', 'Sandified Land Area', 'Reduction in Desertification', 'Reduction in Sandification'
    ],
    'Value': [
        1490.99, 22.83, 12.14,
        6600, 2376, 878, 38, 300,
        652.9, 5.31, 99.92,
        4325.62, 2158.36, 1.36, 3.5
    ],
    'Unit': [
        '10,000 ha', '100 million m³', '%',
        'Species', 'Species', 'Species', 'Species', 'Species',
        '10,000 ha', '%', '%',
        '10,000 ha', 'ha', '10,000 ha', 'ha'
    ]
}

df = pd.DataFrame(data)

# --- 2. DATA SEGMENTATION & STYLING ---

# Filter Group A: Land Area
area_df = df[df['Unit'] == '10,000 ha'].copy()
# Sort for better visualization
area_df = area_df.sort_values('Value', ascending=False)

# Define specific colors based on Category for the Area Chart
def get_area_color(category):
    if category == 'Desert': return '#E3C565'  # Sand Yellow
    if category == 'Forest': return '#2E7D32'  # Forest Green
    if category == 'Wetlands': return '#0288D1' # Water Blue
    return '#999999'

area_df['Color'] = area_df['Category'].apply(get_area_color)


# Filter Group B: Biodiversity
bio_df = df[df['Unit'] == 'Species'].sort_values('Value', ascending=False).copy()

# Add Icons to Labels directly in the dataframe
icon_map = {
    'Higher Plant Species': '🌳 Higher Plants',
    'Algae Species': '🌿 Algae',
    'Fungi Species': '🍄 Fungi',
    'CITES Appendix': '📜 CITES Listed',
    'National Key Protected': '🐼 Key Protected'
}
bio_df['Label_With_Icon'] = bio_df['Indicator'].map(icon_map).fillna(bio_df['Indicator'])

# ==========================================
# 3. VISUALIZATION
# ==========================================
sns.set_theme(style="whitegrid", context="talk")

# Changed to 2 rows instead of 3
fig, axes = plt.subplots(2, 1, figsize=(12, 14))
plt.subplots_adjust(hspace=0.3) 

# --- Chart 1: Land Area (Custom Colors) ---
# Note: We use 'Value' for x, 'Indicator' for y. 
# We explicitly pass the colors list derived from the dataframe.
sns.barplot(
    ax=axes[0], 
    x='Value', 
    y='Indicator', 
    data=area_df, 
    palette=area_df['Color'].tolist() # Apply the custom color mapping
)
axes[0].set_title('Major Land Area Metrics (10,000 ha)', fontsize=16, fontweight='bold')
axes[0].set_xlabel('Area (10,000 hectares)')
axes[0].set_ylabel('')

# Add bar labels
for container in axes[0].containers:
    axes[0].bar_label(container, padding=5, fmt='%.1f')


# --- Chart 2: Biodiversity (With Icons in Labels) ---
# Using a specific palette for biology (Greens/Teals/Browns)
bio_palette = ['#4CAF50', '#009688', '#795548', '#FF9800', '#D32F2F']

sns.barplot(
    ax=axes[1], 
    x='Value', 
    y='Label_With_Icon', # Using the new column with icons
    data=bio_df, 
    palette=bio_palette
)
axes[1].set_title('Biodiversity Richness (Species Count)', fontsize=16, fontweight='bold')
axes[1].set_xlabel('Count')
axes[1].set_ylabel('')

for container in axes[1].containers:
    axes[1].bar_label(container, padding=5, fmt='%.0f')

# ==========================================
# 4. RENDER
# ==========================================
print("Generating Dashboard...")
plt.show()