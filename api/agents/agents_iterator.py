

class AgentsIterator:

     def __init__(self, container):
         self._roster = list(container._agents.items())
         self._classified = container._classified
         self._max = len(self._roster) - len(self._classified)
         self._index = 0
         print('roster', container._agents)


     def __next__(self):
          if self._index == self._max:
            raise StopIteration

          else:
              r = self._roster[self._index]
              self._index += 1
              return r
