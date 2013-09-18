import os
from iron_worker import *

worker = IronWorker(project_id=os.environ.get('IRON_PROJECT_ID'), token=os.environ.get('IRON_TOKEN'))
for i in range(20):
    response = worker.queue(code_name="hello")
