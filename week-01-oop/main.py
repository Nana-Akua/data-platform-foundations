from models import DataRecords
from data import sample
from recordbrain import RecordManager

x = 0
data_record = []

for item in sample:
    record_id = sample[x]["id"]
    record_text = sample[x]["text"]
    record_label = sample[x]["label"]
    record_confidence = sample[x]["confidence"]
    x += 1
    new_record = DataRecords(record_id, record_text, record_label, record_confidence, data_record)
    data_record.append(new_record)

checker = RecordManager(data_record)
for item in sample:
    checker.validate()
    checker.record_num += 1


