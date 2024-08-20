import pandas as pd
from ucimlrepo import fetch_ucirepo

# Fetch the dataset
cdc_diabetes_health_indicators = fetch_ucirepo(id=891)

# Extract features and targets
X: pd.DataFrame = cdc_diabetes_health_indicators.data.features
y: pd.DataFrame = cdc_diabetes_health_indicators.data.targets

combined_df = pd.concat([X, y], axis=1)
combined_df.to_csv('data/diabetes.csv', index=False)
