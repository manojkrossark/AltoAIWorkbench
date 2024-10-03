import google.generativeai as genai
import pandas as pd

class InventoryManagement:
    def __init__(self):
        self.inventory_data = pd.read_csv('data/inventory_data.csv')

    def adjust_inventory(self, sales_data):
        sales_df = pd.DataFrame(sales_data)
        for index, row in sales_df.iterrows():
            product = row['product']
            sold_quantity = row['quantity']
            self.inventory_data.loc[self.inventory_data['product'] == product, 'quantity'] -= sold_quantity
        
        # Use Google Generative AI to enhance inventory adjustments
        enhanced_adjustments = genai.generate_text(
            prompt=f"Provide suggestions to optimize inventory management based on {sales_df.to_dict(orient='records')}",
            max_output_tokens=256
        )

        self.inventory_data.to_csv('data/inventory_data.csv', index=False)
        return {"adjusted_inventory": self.inventory_data.to_dict(orient='records'), "enhanced": enhanced_adjustments.candidates[0]["output"]}

