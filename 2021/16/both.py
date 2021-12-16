class PacketType:
    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    LITERAL = 4
    GREATERTHAN = 5
    LESSTHAN = 6
    EQUALTO = 7

class Mode:
    TOTAL_BITS = 0
    TOTAL_SUB_PACKETS = 1

class BitReader:
    bits: str
    index: int

    def __init__(self, data):
        self.bits = data
        self.index = 0

    def read_bits(self, count):
        ret = self.bits[self.index:self.index + count]
        self.index += count
        return ret

    def read_int(self, length):
        return int(self.read_bits(length), 2)

    def __str__(self):
        return self.bits[self.index:]

def read_packet(reader):
    version = reader.read_int(3)
    type_id = reader.read_int(3)

    packet = {
        'version': version,
        'type': type_id,
        'sub_packets': [],
        'value': 0,
    }
    
    if type_id == PacketType.LITERAL:  # literal packet; read number
        last_group_found = False
        number_bin = ''
        while not last_group_found:
            last_group_found = reader.read_int(1) != 1
            number_bin += reader.read_bits(4)
        number = int(number_bin, 2)
        packet['value'] = number
        return packet

    # operator packet; read sub-packets
    mode = reader.read_int(1)

    if mode == Mode.TOTAL_BITS:
        num_bits = reader.read_int(15)
        start_index = reader.index
        while reader.index < start_index + num_bits:
            sub_packet = read_packet(reader)
            packet['sub_packets'].append(sub_packet)

    elif mode == Mode.TOTAL_SUB_PACKETS:
        num_sub_packets = reader.read_int(11)
        for i in range(num_sub_packets):
            sub_packet = read_packet(reader)
            packet['sub_packets'].append(sub_packet)

    # apply operation
    if type_id == PacketType.SUM:
        packet['value'] = sum(p['value'] for p in packet['sub_packets'])
    elif type_id == PacketType.PRODUCT:
        product = 1
        for p in packet['sub_packets']:
            product *= p['value']
        packet['value'] = product
    elif type_id == PacketType.MINIMUM:
        packet['value'] = min(p['value'] for p in packet['sub_packets'])
    elif type_id == PacketType.MAXIMUM:
        packet['value'] = max(p['value'] for p in packet['sub_packets'])
    elif type_id == PacketType.GREATERTHAN:
        packet['value'] = int(packet['sub_packets'][0]['value'] > packet['sub_packets'][1]['value'])
    elif type_id == PacketType.LESSTHAN:
        packet['value'] = int(packet['sub_packets'][0]['value'] < packet['sub_packets'][1]['value'])
    elif type_id == PacketType.EQUALTO:
        packet['value'] = int(packet['sub_packets'][0]['value'] == packet['sub_packets'][1]['value'])

    return packet

def hex_to_bin(hex):
    binary_str = format(int(hex, 16), 'b')
    to_add = - (len(binary_str) % -4)
    return '0' * to_add + binary_str

# for part 1
def sum_versions(packet):
    return packet['version'] + sum(sum_versions(p) for p in packet['sub_packets'])

input_bin = hex_to_bin(open('input.txt').read().strip())
packet = read_packet(BitReader(input_bin))

print('sum of version numbers:', sum_versions(packet))
print('output value:', packet['value'])
