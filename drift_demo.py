from agents.intent_tracker import IntentTracker
tracker=IntentTracker()
tracker.add('pricing_query',0.82)
tracker.add('refund_request',0.9)
drift,info=tracker.detect_drift()
print(drift,info)
