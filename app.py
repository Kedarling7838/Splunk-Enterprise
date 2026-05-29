import logging
import time
logging.basicConfig( filename='/var/log/my_python_app.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s' 
                   ) 
while True: 
  logging.info("Application is running successfully") 
  time.sleep(10)
