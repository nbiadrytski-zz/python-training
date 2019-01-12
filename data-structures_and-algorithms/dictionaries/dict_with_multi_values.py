from collections import defaultdict
from collections import OrderedDict
import json

# map key to multi values
dd = defaultdict(list)
dd['a'].append(1)
dd['a'].append(2)
dd['b'].append(3)
dd['b'].append(4)
print(dd)  # {'a': [1, 2], 'b': [3, 4]})

# keep the order of dict items as they were inserted
# then turn it into json
od = OrderedDict()
od['foo'] = 1
od['bar'] = 2
od['spam'] = 3
od['grok'] = "test"
print(od)  # ([('foo', 1), ('bar', 2), ('spam', 3), ('grok', "test")])

print(json.dumps(od))  # {"foo": 1, "bar": 2, "spam": 3, "grok": "test"}