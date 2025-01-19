import pandas as pd
import warnings
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore", category=FutureWarning)


trends = TrendReq(hl='en-US', tz=360)

trends.build_payload(kw_list=["Machine Learning"])

region_data = trends.interest_by_region()
top_regions = region_data.sort_values(by="Machine Learning", ascending=False).head(10)

print(top_regions)

plt.style.use('fivethirtyeight')
top_regions.reset_index().plot(
    x="geoName",
    y="Machine Learning",
    figsize=(15, 12),
    kind="bar"
)
plt.title('Top 10 Regions for "Machine Learning"', fontweight='bold')
plt.xlabel('Region')
plt.ylabel('Interest Level')
plt.show()

time_data = trends.interest_over_time()

plt.figure(figsize=(15, 12))
time_data['Machine Learning'].plot() 
plt.title('Total Google Searches for "Machine Learning" Over Time', fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()
