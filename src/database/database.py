import cassandra

# template


class Database:
    def __init__(self):
        self.cluster = cassandra.Cluster(['localhost'], port=9042)
        self.session = self.cluster.connect()

    def close(self):
        self.cluster.shutdown()
