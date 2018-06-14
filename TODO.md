#To Do List

Set up C2 server with an administration client. That way the server can continue running while the administration program is not running. This isn't necessary for now as it can be used with tmux.

#Core
- job control
- multiple connections from multiple agents
- error handling

#CLI
- different commands
- run as Server
- connect to server running FALLOUT

#DNS Beaconing
- handle dns queries
- prepare DNS responses based off of command to be sent out to agents
- able to task all agents or interact with specific agents
- use AES encryption

#Databases
- log all agents in a database (Possibly sqlite?)
- add agents to the database as they come in
- sort by a unique identifier
- show ip's
- show user the agent is running as
- store any information from post modules in a separate table
