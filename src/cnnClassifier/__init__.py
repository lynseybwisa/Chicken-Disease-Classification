#setup logging

import os
import sys  # provides access to some variables used or maintained by the interpreter
import logging  #for emitting log messages 

#format for the log messages that includes the timestamp (asctime), log level (levelname), module name (module), and the actual log message (message).
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#directory and file path for the log files.
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

#configures the logging system
logging.basicConfig(
    #sets the logging level to INFO
    level= logging.INFO,
    #uses the previously defined logging_str as the format for log messages
    format= logging_str,

    handlers=[
        #writes log messages to the file specified by log_filepath
        logging.FileHandler(log_filepath),
        #writes log messages to the console (stdout).
        logging.StreamHandler(sys.stdout)
    ]
)

#creates a logger object named "cnnClassifierLogger." The logger is what you use to emit log messages in your program.
logger = logging.getLogger("cnnClassifierLogger")