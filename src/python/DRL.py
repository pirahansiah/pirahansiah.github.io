# Farshid Pirahansiah
## DRL
import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Fetch stock data for Gold and Euro
gold_data = yf.download("GC=F", start="2024-05-01", end="2024-07-01")
euro_data = yf.download("EURUSD=X", start="2024-05-01", end="2024-07-01")

# Prepare the data
def prepare_data(gold_data, euro_data):
    data = pd.DataFrame({
        'Gold_Close': gold_data['Close'],
        'Euro_Close': euro_data['Close']
    })
    data = data.dropna()
    
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)
    
    X = scaled_data[:-1]
    y = scaled_data[1:, 0]  # Next day's gold price
    
    return X, y, scaler

X, y, scaler = prepare_data(gold_data, euro_data)

# Define the DRL agent
class DRLAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = []
        self.gamma = 0.95  # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential([
            Dense(24, input_dim=self.state_size, activation='relu'),
            Dense(24, activation='relu'),
            Dense(self.action_size, activation='linear')
        ])
        model.compile(loss='mse', optimizer=Adam(learning_rate=0.001))
        return model

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return np.random.randint(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])

    def train(self, state, action, reward, next_state, done):
        target = reward
        if not done:
            target = reward + self.gamma * np.amax(self.model.predict(next_state)[0])
        target_f = self.model.predict(state)
        target_f[0][action] = target
        self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

# Train the agent
state_size = X.shape[1]
action_size = 3  # buy, hold, sell
agent = DRLAgent(state_size, action_size)

episodes = 5 #100
batch_size = 32

for e in range(episodes):
    state = X[0].reshape(1, -1)
    for time in range(len(X) - 1):
        action = agent.act(state)
        next_state = X[time + 1].reshape(1, -1)
        reward = y[time] - y[time - 1] if time > 0 else 0
        done = time == len(X) - 2
        agent.train(state, action, reward, next_state, done)
        state = next_state

    print(f"Episode {e + 1}/{episodes} completed")

# Make predictions
predictions = []
state = X[-1].reshape(1, -1)
for _ in range(5):  # Predict next 5 days
    action = agent.act(state)
    prediction = scaler.inverse_transform(state)[0][0]
    predictions.append(prediction)
    
    # Update state for next prediction
    next_state = np.roll(state, -1)
    next_state[0][-1] = prediction
    state = next_state

print("Predicted Gold prices for the next 5 days:")
for i, price in enumerate(predictions, 1):
    print(f"Day {i}: ${price:.2f}")