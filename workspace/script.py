# Example: calculate annual stock turns and GMROI from raw inputs
# Assume:
#   weekly_units_sold = 5000
#   on_hand_units     = 150
#   avg_daily_price   = ₹125,000 (full inventory value per unit)
#   wholesale_cost    = ₹95,000 (cost per unit)
#   target_gross_margin = 40%

weekly_units_sold = 5000          # units/week
on_hand_units     = 150           # units currently in stock
daily_price       = 125_000      # ₹ per full inventory value (for illustration)
wholesale_cost    = 95_000        # ₹ per unit cost
margin_pct         = 0.40         # 40% gross margin target

# Stock turns (annual)
annual_units_sold = weekly_units_sold * 52
stock_turns = annual_units_sold / on_hand_units

# Revenue per unit (target list price)
list_price = 125_000               # example high-end price
gross_profit_per_unit = list_price * margin_pct
total_inventory_value = on_hand_units * list_price
annual_revenue = annual_units_sold * list_price
annual_cogs = annual_units_sold * wholesale_cost
gmroi_one_month = (annual_revenue - annual_cogs) / (on_hand_units * list_price)  # rough
gmroi_annual = (annual_revenue - annual_cogs) / (on_hand_units * list_price) * 12

print(f"Stock turns: {stock_turns:.1f}x/yr")
print(f"GMROI (annual): {gmroi_annual:.2f}")