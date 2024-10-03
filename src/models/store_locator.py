import google.generativeai as genai
import geopandas as gpd
import pandas as pd

class StoreLocator:
    def __init__(self):
        self.store_data = gpd.read_file('data/store_data.csv')

    def get_optimal_locations(self, demand_data):
        demand_df = pd.DataFrame(demand_data)
        # Find stores closest to high-demand areas
        recommended_stores = self.store_data[self.store_data['location'].isin(demand_df['optimal_locations'])]
        
        # Use Google Generative AI to enhance store recommendations
        enhanced_stores = genai.generate_text(
            prompt=f"Recommend optimal store locations based on competition and demand: {recommended_stores.to_dict(orient='records')}",
            max_output_tokens=256
        )

        return {"recommended_stores": recommended_stores.to_dict(orient='records'), "enhanced": enhanced_stores.candidates[0]["output"]}
