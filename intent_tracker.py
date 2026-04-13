from datetime import datetime

class IntentSnapshot:
    def __init__(self,intent,confidence,time):
        self.intent=intent
        self.confidence=confidence
        self.time=time

class IntentTracker:
    def __init__(self):
        self.history=[]

    def add(self,intent,confidence):
        self.history.append(IntentSnapshot(intent,confidence,datetime.utcnow()))

    def detect_drift(self):
        if len(self.history)<2: return False,None
        prev=self.history[-2]
        curr=self.history[-1]
        drift=prev.intent!=curr.intent and abs(curr.confidence-prev.confidence)>0.15
        return drift,(prev.intent,curr.intent)
