class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.last_times = dict()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        ans = message not in self.last_times or timestamp-self.last_times[message] >= 10
        if ans: self.last_times[message] = timestamp
        
        return ans


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
