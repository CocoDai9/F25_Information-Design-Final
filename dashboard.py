import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. DATA INGESTION
# ==========================================
# Recreating the dataset from your image manually to ensure accuracy
data = {
    'Category': [
        'Forest Resource', 'Forest Resource', 'Forest Resource',
        'Biodiversity', 'Biodiversity', 'Biodiversity', 'Biodiversity', 'Biodiversity',
        'Wetlands', 'Wetlands', 'Wetlands',
        'Desertification', 'Desertification', 'Desertification', 'Desertification'
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

# ==========================================
# 2. DATA SEGMENTATION
# ==========================================
# We must split the data because the units (Hectares vs Species vs %) 
# cannot be plotted on the same axis without distortion.

# Group A: Land Area (Unit: 10,000 ha)
area_df = df[df['Unit'] == '10,000 ha'].sort_values('Value', ascending=False)

# Group B: Biodiversity (Unit: Species)
bio_df = df[df['Unit'] == 'Species'].sort_values('Value', ascending=False)

# Group C: Percentages (Unit: %)
pct_df = df[df['Unit'] == '%'].sort_values('Value', ascending=False)

# ==========================================
# 3. VISUALIZATION CONFIGURATION
# ==========================================
# Using a dark grid style to match a modern VS Code aesthetic
sns.set_theme(style="whitegrid", context="talk")
fig, axes = plt.subplots(3, 1, figsize=(12, 18))
plt.subplots_adjust(hspace=0.4) # Add space between charts

# --- Chart 1: Land Area Comparison (The Scale of the Environment) ---
sns.barplot(ax=axes[0], x='Value', y='Indicator', data=area_df, palette='magma')
axes[0].set_title('Major Land Area Metrics (10,000 ha)', fontsize=16, fontweight='bold')
axes[0].set_xlabel('Area (10,000 hectares)')
axes[0].set_ylabel('')
# Add labels to bars
for container in axes[0].containers:
    axes[0].bar_label(container, padding=5, fmt='%.1f')

# --- Chart 2: Biodiversity Count ---
sns.barplot(ax=axes[1], x='Value', y='Indicator', data=bio_df, palette='viridis')
axes[1].set_title('Biodiversity Richness (Species Count)', fontsize=16, fontweight='bold')
axes[1].set_xlabel('Count')
axes[1].set_ylabel('')
for container in axes[1].containers:
    axes[1].bar_label(container, padding=5, fmt='%.0f')

# --- Chart 3: Environmental Ratios ---
sns.barplot(ax=axes[2], x='Value', y='Indicator', data=pct_df, palette='coolwarm')
axes[2].set_title('Key Environmental Ratios (%)', fontsize=16, fontweight='bold')
axes[2].set_xlabel('Percentage')
axes[2].set_xlim(0, 110) # Fix scale to 100%
axes[2].set_ylabel('')
for container in axes[2].containers:
    axes[2].bar_label(container, padding=5, fmt='%.2f%%')

# ==========================================
# 4. RENDER
# ==========================================
print("Generating Dashboard...")
plt.show()