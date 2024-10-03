import google.generativeai as genai
import pandas as pd

class DeliveryScheduler:
    def __init__(self):
        self.schedule_data = pd.read_csv('data/schedule_data.csv')

    def get_optimal_schedule(self, delivery_data):
        delivery_df = pd.DataFrame(delivery_data)
        
        # Use historical data to suggest times
        optimal_times = self.schedule_data.loc[self.schedule_data['time_available'] == True]
        
        # Enhance delivery times using Google Generative AI
        enhanced_schedule = genai.generate_text(
            prompt=f"Suggest optimal delivery and installation times based on {optimal_times.to_dict(orient='records')}",
            max_output_tokens=256
        )

        return {"optimal_times": optimal_times.to_dict(orient='records'), "enhanced": enhanced_schedule.candidates[0]["output"]}