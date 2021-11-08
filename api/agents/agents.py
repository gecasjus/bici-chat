from api.agents.agents_iterator import AgentsIterator

class Agents:
    
    def __init__(self):
        print(self)

        self._agents = {}
        self._classified = []

    def add_agent(self, name, number, classified = False):

        self._agents[number] = name
        if classified:
            self._classified.append(name)

    def lookup_agents(self):
        print('agents boy', self._agents)

    def __iter__(self):
        return AgentsIterator(self)