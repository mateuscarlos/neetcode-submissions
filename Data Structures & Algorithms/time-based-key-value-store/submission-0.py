class TimeMap:

    def __init__(self):
        self.store = {} #key: lista de [valores, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        start, end = 0, len(values) - 1
        while start <= end:
            mid = (start + end) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                start = mid + 1
            else:
                end = mid - 1
        return res