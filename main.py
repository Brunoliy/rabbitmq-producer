from fastapi import FastAPI
import pika
import json

app = FastAPI()

def send_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='my_queue')
    channel.basic_publish(exchange='', routing_key='my_queue', body=json.dumps(message))
    connection.close()

@app.post("/send/")
def send(message: dict):
    send_message(message)
    return {"status": "Message sent"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
