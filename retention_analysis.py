
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# E-commerce Customer Retention Rate Analysis
# Email: 23ds2000044@ds.study.iitm.ac.in
# Date: August 2025

def load_and_analyze_retention_data():
    """
    Load and analyze e-commerce customer retention data for 2024
    Returns: DataFrame with quarterly retention rates
    """
    # Customer Retention Rate - 2024 Quarterly Data
    quarterly_data = {
        'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
        'Retention_Rate': [69.07, 74.58, 69.07, 74.65],
        'Month_Number': [1, 2, 3, 4]
    }

    df = pd.DataFrame(quarterly_data)
    return df

def calculate_key_metrics(df):
    """
    Calculate key performance metrics for retention analysis
    """
    metrics = {
        'average_retention': df['Retention_Rate'].mean(),
        'industry_target': 85,
        'min_retention': df['Retention_Rate'].min(),
        'max_retention': df['Retention_Rate'].max(),
        'volatility': df['Retention_Rate'].std()
    }

    metrics['gap_to_target'] = metrics['industry_target'] - metrics['average_retention']
    metrics['improvement_needed'] = (metrics['gap_to_target'] / metrics['average_retention']) * 100

    return metrics

def create_retention_visualization(df, metrics):
    """
    Create comprehensive visualization for retention analysis
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Quarterly Trend Chart
    ax1.plot(df['Quarter'], df['Retention_Rate'], 'o-', linewidth=3, markersize=8, color='#e74c3c', label='Actual Retention')
    ax1.axhline(y=metrics['industry_target'], color='#27ae60', linestyle='--', linewidth=2, label='Industry Target (85%)')
    ax1.axhline(y=metrics['average_retention'], color='#f39c12', linestyle=':', linewidth=2, label=f'Current Average ({metrics["average_retention"]:.2f}%)')

    ax1.set_title('Quarterly Customer Retention Rate - 2024', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Quarter', fontweight='bold')
    ax1.set_ylabel('Retention Rate (%)', fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_ylim(60, 90)

    # Gap Analysis Bar Chart
    gaps = [metrics['industry_target'] - rate for rate in df['Retention_Rate']]
    colors = ['#e74c3c' if gap > 10 else '#f39c12' for gap in gaps]

    bars = ax2.bar(df['Quarter'], gaps, color=colors, alpha=0.7)
    ax2.set_title('Gap to Industry Target by Quarter', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Quarter', fontweight='bold')
    ax2.set_ylabel('Gap to Target (%)', fontweight='bold')
    ax2.grid(True, alpha=0.3)

    # Add value labels on bars
    for bar, gap in zip(bars, gaps):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.2,
                f'{gap:.2f}%', ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()
    plt.savefig('retention_analysis_2024.png', dpi=300, bbox_inches='tight')
    plt.show()

    return fig

def generate_insights_and_recommendations(df, metrics):
    """
    Generate business insights and strategic recommendations
    """
    insights = {
        'key_findings': [
            f"Average retention rate of {metrics['average_retention']:.2f}% is {metrics['gap_to_target']:.2f} percentage points below industry target",
            f"High volatility ({metrics['volatility']:.2f}% std dev) indicates inconsistent customer experience",
            "Alternating pattern between ~69% (Q1, Q3) and ~74% (Q2, Q4) suggests seasonal or operational factors",
            f"Need {metrics['improvement_needed']:.1f}% relative improvement to reach industry benchmark"
        ],
        'business_implications': [
            "Declining customer loyalty directly impacts lifetime value and revenue growth",
            "High retention volatility suggests operational inefficiencies in customer service delivery",
            "Below-benchmark performance may indicate competitive disadvantages in market positioning",
            "Revenue loss estimated at 13+ percentage points of customer base annually"
        ],
        'strategic_recommendations': [
            "Implement targeted retention campaigns focusing on at-risk customer segments",
            "Develop personalized engagement strategies based on customer behavior patterns",
            "Invest in customer experience optimization across all touchpoints",
            "Create loyalty programs with tiered benefits to increase customer stickiness",
            "Implement predictive analytics to identify churn risk early",
            "Establish quarterly retention targets with monthly monitoring"
        ]
    }

    return insights

def main():
    """
    Main analysis function
    """
    print("E-commerce Customer Retention Analysis - 2024")
    print("=" * 60)
    print("Analyst Email: 23ds2000044@ds.study.iitm.ac.in")
    print("=" * 60)

    # Load and analyze data
    df = load_and_analyze_retention_data()
    metrics = calculate_key_metrics(df)

    # Display key metrics
    print(f"\nKEY PERFORMANCE METRICS:")
    print(f"Average Retention Rate: {metrics['average_retention']:.2f}%")
    print(f"Industry Target: {metrics['industry_target']}%")
    print(f"Gap to Target: {metrics['gap_to_target']:.2f} percentage points")
    print(f"Improvement Needed: {metrics['improvement_needed']:.1f}%")
    print(f"Volatility (Std Dev): {metrics['volatility']:.2f}%")

    # Quarterly breakdown
    print(f"\nQUARTERLY BREAKDOWN:")
    for idx, row in df.iterrows():
        gap = metrics['industry_target'] - row['Retention_Rate']
        print(f"{row['Quarter']}: {row['Retention_Rate']:.2f}% (Gap: {gap:.2f}%)")

    # Create visualizations
    fig = create_retention_visualization(df, metrics)

    # Generate insights
    insights = generate_insights_and_recommendations(df, metrics)

    print(f"\nKEY FINDINGS:")
    for finding in insights['key_findings']:
        print(f"• {finding}")

    print(f"\nBUSINESS IMPLICATIONS:")
    for implication in insights['business_implications']:
        print(f"• {implication}")

    print(f"\nSTRATEGIC RECOMMENDATIONS:")
    for recommendation in insights['strategic_recommendations']:
        print(f"• {recommendation}")

    # Save data
    df.to_csv('customer_retention_2024.csv', index=False)
    print(f"\nData saved to 'customer_retention_2024.csv'")
    print(f"Visualization saved to 'retention_analysis_2024.png'")

    return df, metrics, insights

if __name__ == "__main__":
    df, metrics, insights = main()
