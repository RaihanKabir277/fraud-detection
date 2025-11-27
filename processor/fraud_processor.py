import faust

app = faust.App(
    'fraud-detector',
    broker='kafka://localhost:9092',
)

class Transaction(faust.Record):
    user_id: int
    amount: float
    timestamp: str

transactions_topic = app.topic('transactions', value_type=Transaction)
fraud_topic = app.topic('fraud_alerts')

# Table to store user transactions in last 5 sec
user_history = app.Table('user_history', default=list)

@app.agent(transactions_topic)
async def process_transaction(stream):
    async for tx in stream:
        user = tx.user_id
        history = user_history[user]

        history.append(tx)

        # keep only last 5 seconds (simulated for static timestamp)
        if len(history) > 5:
            history.pop(0)

        # RULE 1: High amount
        if tx.amount > 700:
            await fraud_topic.send(value=f"[ALERT] User {user} spent {tx.amount}!")

        # RULE 2: Too many transactions rapidly
        if len(history) >= 3:
            await fraud_topic.send(value=f"[ALERT] User {user} made 3 quick transactions!")

        user_history[user] = history

if __name__ == "__main__":
    app.main()
