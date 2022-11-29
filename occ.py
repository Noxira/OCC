import sys

class transaction:
    def __init__(self, transaction_number: int):
        self._transaction_number = transaction_number
        self._start_ts = -1
        self._finish_ts = -1
        self._read = []
        self._write = []
    
    def write(self, data_item):
        if data_item not in self._write:
            self._write.append(data_item)
    
    def read(self, data_item):
        if data_item not in self._read:
            self._read.append(data_item)

    def get_write(self):
        return self._write

    def get_read(self):
        return self._read

    def set_start(self, timestamp):
        self._start_ts = timestamp
    
    def set_finish(self, timestamp):
        self._finish_ts = timestamp
    
    def get_start(self):
        return self._start_ts

    def get_finish(self):
        return self._finish_ts

    def get_transaction_number(self):
        return self._transaction_number

    def check_conflicts(self, write_data):
        # if transaction hasn't finished yet, it's not this transaction's job to check for conflicts
        if self._finish_ts == -1:
            return False
        for data in write_data:
            if data in self._read:
                print("--> Conflict found between transactions on data " + str(data))
                return True
        return False

class manager:
    def __init__(self):
        self._transactions = []
        self._planned_transactions = []
    
    def add_planned_transaction(self, transaction):
        self._planned_transactions = transaction

    def _is_in_transactions(self, transaction_num):
        for transaction in self._transactions:
            if transaction.get_transaction_number() == transaction_num:
                return True
        return False

    def _write_to_transaction(self, transaction_num, data_set):
        for transaction in self._transactions:
            if transaction.get_transaction_number() == transaction_num:
                transaction.write(data_set)
                return
    
    def _read_to_transaction(self, transaction_num, data_set):
        for transaction in self._transactions:
            if transaction.get_transaction_number() == transaction_num:
                transaction.read(data_set)
                return
    
    def _commit_to_transaction(self, transaction_num, timestamp):
        for transaction in self._transactions:
            if transaction.get_transaction_number() == transaction_num:
                # set finish timestamp
                transaction.set_finish(timestamp)
                # check for conflicts
                for transaction2 in self._transactions:
                    # if transaction2 is not the same as transaction, and transaction2 check for conflicts
                    if transaction2.get_transaction_number() != transaction_num and not(transaction2.get_finish() < transaction.get_start()):
                        if transaction.check_conflicts(transaction2.get_write()) is True:
                            print("Transaction " + str(transaction_num) + " is invalid, aborted")
                            return False
                print("Transaction " + str(transaction_num) + " is valid, committed")
                return True

    def start_check(self):
        timestamp = 0
        while (timestamp < len(self._planned_transactions)):
            # if the transaction being checked is not added in the transactions list, add it
            if self._is_in_transactions(self._planned_transactions[timestamp][1]) is False:
                temp_transaction = transaction(self._planned_transactions[timestamp][1])
                temp_transaction.set_start(timestamp)
                self._transactions.append(temp_transaction)

            # if transaction is set to write, write to the transaction
            # W1(X)
            if self._planned_transactions[timestamp][0] == 'W':
                self._write_to_transaction(self._planned_transactions[timestamp][1], self._planned_transactions[timestamp][3])
            elif self._planned_transactions[timestamp][0] == 'R':
                self._read_to_transaction(self._planned_transactions[timestamp][1], self._planned_transactions[timestamp][3])
            elif self._planned_transactions[timestamp][0] == 'C':
                if not self._commit_to_transaction(self._planned_transactions[timestamp][1], timestamp):
                    break
            
            timestamp += 1

class file_reader:
    def __init__(self, filename):
        self._filename = filename
        self._transactions = []
    
    def read(self):
        with open(self._filename, 'r') as file:
            for line in file:
                if len(line) > 1:
                    self._transactions.append(line.replace('\n', ''))
    
    def get_transactions(self):
        return self._transactions

if len(sys.argv) != 2:
    print("Usage: python occ.py <transaction.txt>")
else:
    reader = file_reader(sys.argv[1])
    reader.read()
    manager = manager()
    manager.add_planned_transaction(reader.get_transactions())
    manager.start_check()