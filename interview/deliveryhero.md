Only solutions 

# Q1
```
from typing import List, Text


class NoAgentFoundException(Exception):
    pass


class Agent(object):
    def __str__(self):
        # return "<Agent: {}>".format(self._name)
        return f"Agent: {self.name}, {self.skills}, {self.load}"
        
    def __init__(self, name, skills, load):
        self.name = name
        self.skills = skills
        self.load = load
        
        
class Ticket(object):
    def __init__(self, id, restrictions):
        self.id = id
        self.restrictions = restrictions
        
    def __str__(self):
        # return "<Agent: {}>".format(self._name)
        return f"Ticket: {self.id}, {self.restrictions}"
                

class FinderPolicy(object):
    # remove all agenrs with load 3 and above
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        return list(filter(lambda agent: agent.load < 3, agents))
            
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented
        

    def _check_agents_input(self, agents: List[Agent]) -> None:
        if len(agents) == 0:
            raise NoAgentFoundException
            
    def print_agents(self, agents):
        for a in agents:
            print(a)

    def get_avail_agent(self, agents: List[Agent]) -> Agent:
        if len(agents) > 0:
            return agents[0]  
        else:
            raise NoAgentFoundException


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        self._check_agents_input(agents)

        avail_agents = self._filter_loaded_agents(agents)
        #disregard skill matching and only sort by load 
        avail_agents.sort(key=lambda x: x.load)
        return self.get_avail_agent(avail_agents)


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        self._check_agents_input(agents)

        avail_agents = self._filter_loaded_agents(agents)
        avail_agents = list(filter(lambda agent: 
            set(ticket.restrictions).issubset(agent.skills), avail_agents))
        #sort by skills count
        avail_agents = sorted(avail_agents, key=lambda x: (len(x.skills), x.load))
        return self.get_avail_agent(avail_agents)
            
```


# Q2
```
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import logging

Pattern = ['AB','BA','CD','DC']

def solution(S):
    mem = ""
    
    
    #use DFA for efficiency
    
    while mem != S:
        mem = f"{S}"
        for r in Pattern:
            S = S.replace(r,"")
    return S        
```              

# Q3
```
import json
import logging


class SearchByTag:

    def __init__(self, data_file, query_tag, data_type="json"):
        if data_type == "json":
            self._load_json(data_file)
        else:
            raise Exception("file type not supported")
        self.query = query_tag
    
    def _load_json(self, data_file):
        with open(data_file) as data_file:
            try:
                self._data = json.load(data_file)
            except ValueError:
                raise Exception("only json file is supported")

    def search(self):
        # return generator 
        if len(self._data['items']) == 0:
            return
        for l in self._data['items']:
            # logging.info(type(l),l)

            if 'tags' in l and self.query in l['tags']:
                yield l
        
            

    def first(self):
        # return first
        gen = self.search()
        return next(gen)
```

