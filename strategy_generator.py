import numpy as np
from sklearn.ensemble import RandomForestClassifier

class StrategyGenerator:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    def train(self, features, labels):
        """
        Train the AI model on historical data to predict outcomes.

        :param features: numpy array of features
        :param labels: numpy array of corresponding outcomes
        """
        self.model.fit(features, labels)
    
    def predict(self, user_data):
        """
        Predict the best strategy based on user's current data.

        :param user_data: numpy array of user's current state
        :return: Predicted strategy
        """
        prediction = self.model.predict(user_data.reshape(1, -1))
        # Example strategy mapping
        strategies = {0: "Conservative", 1: "Moderate", 2: "Aggressive"}
        return strategies[prediction[0]]
    
    def generate_investment_strategy(self, user_profile):
        """
        Generate a detailed investment strategy based on user profile.

        :param user_profile: dictionary containing user's financial profile
        :return: string describing the investment strategy
        """
        risk_tolerance = user_profile.get('risk_tolerance', 'moderate')
        capital = user_profile.get('capital', 1000)
        
        if risk_tolerance == 'low':
            return f"Invest {capital*0.7:.2f} in stablecoins, {capital*0.3:.2f} in low-risk assets."
        elif risk_tolerance == 'high':
            return f"Invest {capital*0.6:.2f} in volatile assets, {capital*0.4:.2f} in growth stocks."
        else:
            return f"Balanced approach: {capital*0.5:.2f} in stable assets, {capital*0.5:.2f} in diversified portfolio."

    def gambling_strategy(self, game_type, user_history):
        """
        Suggest a gambling strategy based on game type and user's past performance.

        :param game_type: string indicating the game (e.g., 'slots', 'blackjack')
        :param user_history: list of past game outcomes
        :return: string describing gambling strategy
        """
        win_rate = sum(user_history) / len(user_history) if user_history else 0.5
        
        if game_type == 'slots':
            if win_rate > 0.55:
                return "Increase bet size slightly; current strategy seems effective."
            else:
                return "Reduce bet size or switch to a different slot machine."
        elif game_type == 'blackjack':
            if win_rate > 0.6:
                return "Continue with current strategy; consider increasing bet on strong hands."
            else:
                return "Adopt a more conservative betting strategy or learn basic strategy better."
        else:
            return "General advice: manage your bankroll carefully; don't chase losses."

# Example usage
if __name__ == "__main__":
    generator = StrategyGenerator()
    # Hypothetical training data
    features = np.random.rand(100, 10)
    labels = np.random.randint(0, 3, 100)
    generator.train(features, labels)
    
    user_data = np.random.rand(10)
    print("Predicted Strategy:", generator.predict(user_data))
    
    user_profile = {'risk_tolerance': 'high', 'capital': 10000}
    print("Investment Strategy:", generator.generate_investment_strategy(user_profile))
    
    user_history = [0, 1, 1, 0, 1]  # 1 for win, 0 for loss
    print("Gambling Strategy for Blackjack:", generator.gambling_strategy('blackjack', user_history))
