# import livrary
from datetime import datetime

# What is the average lot size (rounded to nearest integer)?
avg_lot_size = round(home_data['LotArea'].mean())
avg_lot_size = int(avg_lot_size)

# As of today, how old is the newest home (current year - the date in which it was built)
current_year = datetime.now().year
newest_year_built = home_data['YearBuilt'].max()
newest_home_age = current_year - newest_year_built

# Checks your answers
print ("Average Lot Size:", avg_lot_size)
print ("Most recent Batch Age:", newest_home_age)
