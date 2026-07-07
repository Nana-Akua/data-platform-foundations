
class RecordManager:

    def __init__(self, record_list):
        self.record_list = record_list
        self.record_num = 0

    def validate(self):
        record = self.record_list[self.record_num]
        if record.text == "" or record.id == "" or record.label == "":
            print("You are missing a  value in this record")
            return False
        else:
            print("Everything looks good for this record")
            return True

