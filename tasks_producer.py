import random
from faker.providers import BaseProvider
from faker import Faker
import config
import time
import requests
import json
import uuid
from typing import Self, Dict, Any

class TaskProvider(BaseProvider):
    def task_priority(self:Self) -> str:
        severity_levels = [
            'Low', 'Moderate', 'Major', 'Critical'
        ]
        return severity_levels[random.randint(0, len(severity_levels) - 1)]

# Create a Faker instance and seeding to have the same results every time we execute the script
fakeTasks = Faker('en_US')
# Seed the Faker instance to have the same results every time we run the program
fakeTasks.seed_instance(0)
# Assign the TaskProvider to the Faker instance
fakeTasks.add_provider(TaskProvider)

# Generate a Fake Task
def produce_task(batchid: int, taskid: int) -> Dict[str, Any]:
    message = {
        'batchid': batchid,
        'taskid': taskid,
        'owner': fakeTasks.unique.name(),
        'priority': fakeTasks.task_priority(),
        # 'description': fakeTasks.text(max_nb_chars=200),
        # 'raised_date': fakeTasks.date_time_this_year(),
    }
    return message

def send_webhook(msg) -> int:
    """
    Send a webhook to a specified URL
    :param msg: task details
    :return:
    """
    try:
        #Post a webhook message
        # default is a function applied to objects that are not serializable = it converts them to str
        resp = requests.post(config.WEBHOOK_RECEIVER_URL, data=json.dumps(msg, sort_keys=True,default=str), headers={'Content-Type': 'application/json'}, timeout=1.0)
        # Returns an HTTPError if an error has occured during the process (used for debugging)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        #print("An HTTP Error occurred:", repr(e))
        pass
    except requests.exceptions.ConnectionError as e:
        #print("An Error connecting to the API occurred", repr(e))
        pass
    except requests.exceptions.Timeout as e:
        #print("A Timeout error occurred", repr(e))
        pass
    except requests.exceptions.RequestException as e:
        #print("An Unknown error occurred", repr(e))
        pass
    except:
        pass
    else:
        return resp.status_code


# Generate a Bunch of fake tasks
def produce_bunch_of_tasks():
    """
    Generate a Bunch of fake tasks
    """
    n = random.randint(config.MIN_NBR_TASKS, config.MAX_NBR_TASKS)
    batchid = str(uuid.uuid4())
    for i in range(n):
        msg = produce_task(batchid, i)
        resp = send_webhook(msg)
        time.sleep(config.WAIT_TIME)
        print(f"{i} out of {n} -- Status {resp} -- Message = {msg}")
        yield resp, n, msg

if __name__=="__main__":
    for resp, total, msg in produce_bunch_of_tasks():
        pass

