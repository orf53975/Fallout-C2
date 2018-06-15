#!/usr/bin/python

# imports
import argparse
import os
import signal
import sys
import threading
import time
import queue

from modules import dns, tasker
from termcolor import colored, cprint

# variables
PROMPT = 'FALLOUT:> '

host = ''
port = 53

q = queue.Queue()
SocketThread = []
Agents = {}

COMMANDS = {
    'help':['Shows The help menu']
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
        AgentName = threading.current_thread().getName()
        cprint(("\n[+] Agent " + self.ip + ":" + str(self.port) + " connected with Thread_ID: ", AgentName), "green")
        Agents[AgentName] = self.agent_address
        




# defs
