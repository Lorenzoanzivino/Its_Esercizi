from datetime import datetime, timedelta
from typing import Self, Any

class TimeRange(tuple):
    #Tipo dato composto Periodo
    # rappresenta un periodo di tempo compreso tra due istanti

	_start: datetime|None # [0..1]
	_end: datetime|None # [0..1]
       
	# subject to constraint: _start <= _end

	def __new__(cls, start:datetime|str|None, end:datetime|str|None)->Self:	
		# We accept _start == None or _end == None (unbounded time periods)
              
        values = [ datetime.fromisoformat(x) if isinstance(x, str) else x for x in [start, end] ]
        if values[0] and values[1] and values[0] > values[1]:
            raise ValueError(f"Invalid TimeRange(from={start}, to={end}): 'from' must be <= 'to'")
        
        return tuple.__new__(cls, values)   

    def start(self) -> datetime:
        return self._start
    
    def end(self) -> datetime:
        return self._end
    
    def duration(self) -> timedelta:
        return self.end() - self.start()
    
#    def __hash__(self) -> int:
#        return hash((self.start(), self.end()))
#    
#    def __eq__(self, other: any) -> bool:
#        if not isinstance(other, type(self)) or hash(self) != hash(other):
#            return False
#        return self.start() == other.start() and self.end() == other.end()
    
    def is_disjoint(self, other: Self) -> bool:
        """
        se self e other sono intervalli che non si sovrappongono restituisce True
        
                    start                   end
                self: |----------------------|
                
        start     end
        |----------|
                                        start   end
                                          |------|
                                          
        """

        return self.start() > other.end() or self.end() < other.start()

