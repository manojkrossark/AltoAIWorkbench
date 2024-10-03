import google.generativeai as genai
import pandas as pd
from sklearn.linear_model import LinearRegression

genai.configure(api_key="AIzaSyDUUsTEvKKRya7u46jEJw4OMwFZ3dRKIRs")

class DemandForecast:
    def __init__(self):
        self.model = LinearRegression()
        self.load_data()

    def load_data(self):
        self.data = pd.read_csv('data/sales_data.csv')
        self.prepare_data()

    def prepare_data(self):
        self.X = self.data[['feature1', 'feature2']]  # Replace with actual features
        self.y = self.data['demand']

    def predict(self, input_data):
        input_df = pd.DataFrame(input_data)
        self.model.fit(self.X, self.y)
        predictions = self.model.predict(input_df)
        
        # Use Google Generative AI to enhance predictions
        enhanced_predictions = genai.generate_text(
            prompt=f"Improve the demand prediction results based on {predictions.tolist()}",
            max_output_tokens=256
        )
        
        return {"predictions": predictions.tolist(), "enhanced": enhanced_predictions.candidates[0]["output"]}
