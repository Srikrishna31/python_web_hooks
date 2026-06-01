This repo showcases a sample implementation of a simple webhook, following this page: [Webhooks in Python](https://thepythoncode.com/article/webhooks-in-python-with-flask)

## How to Run

### 1. Prerequisites
- **Redis Server**: Ensure Redis is installed and running.
  - On Ubuntu/Debian: `sudo apt install redis-server`
  - Start it: `sudo systemctl start redis`
  - Verify: `redis-cli ping` (should return `PONG`)
- **Python Dependencies**: Install the required packages using pip:
  ```bash
  pip install flask flask-socketio requests faker redis
  ```

### 2. Start the Consumer
The consumer listens for webhooks and displays updates in real-time via Socket.IO.
```bash
python app_consumer.py
```
- The consumer will be running at `http://localhost:5001`.

### 3. Start the Producer
The producer generates tasks and sends them to the consumer via webhooks.
```bash
python app_producer.py
```
- The producer will be running at `http://localhost:5000`.

### 4. Check the Results
1. Open your browser and go to `http://localhost:5001` (Consumer page).
2. Open another tab or window and go to `http://localhost:5000` (Producer page).
3. Click the **"Produce Tasks"** button on the Producer page.
4. **Observe the results**:
   - On the **Producer page**, you will see a list of generated tasks and their HTTP response status (200 for success).
   - On the **Consumer page**, you will see the tasks appearing in real-time in the message list and the bar chart updating based on task priority.
