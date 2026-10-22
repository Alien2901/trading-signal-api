from fastapi import FastAPI
import random

app = FastAPI(title="Trading Signal API")

@app.get("/health")
def health_check():
    return {"status": "OK", "message": "Trading API is running smoothly"}

@app.get("/version")
def get_version():
    return {"version": "1.0.0", "author": "Alyona"}

@app.get("/signal/{ticker}")
def get_trading_signal(ticker: str):
    signals = ["BUY", "SELL", "HOLD"]
    random_signal = random.choice(signals)
    random_price = round(random.uniform(10, 50000), 2)
    
    return {
        "ticker": ticker.upper(),
        "recommendation": random_signal,
        "entry_price": random_price,
        "strategy": "Technical Analysis Simulation"
    }
