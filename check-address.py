A = ord("A")
F = ord("F")
_0 = ord('0')
_9 = ord('9')

def check_address(address):
    if not isinstance(address, str) or address == '':
        return False
    
    address = address.strip()
    if (':' in address) and ('-' not in address):
        bytes = address.split(":")
    elif ('-' in address) and (':' not in address):
        bytes = address.split("-")

    if len(bytes) != 6:
        return False
    
    for byte in bytes:
        if len(byte) != 2:
            return False
        byte = byte.upper()
        
        for char in byte:
            char = ord(char)
            if not ((A <= char <= F) or (_0 <= char <= _9)): return False
        
    return True

def assert_result(address, result):
    try:
        assert check_address(address) == result
        return True
    except AssertionError:
        return False

def assert_function():
    print(assert_result("11:22:33:44:55:66", True))
    print(assert_result("FF:FF:FF:FF:FF:FF", True))
    print(assert_result("AB:12:cd:34:31:21", True))
    print(assert_result("11:22:33:44:55:66:77", False))
    print(assert_result("11-22-33-44-55-66", True))
    print(assert_result("11:22:33:44:55", False))
    print(assert_result("H:22:33:44:55:661", False))

def check_cast(address):
    first_byte = int(address[:2], base =16)
    first_byte_bin = bin(first_byte)

    if first_byte_bin[-1] == '0':
        return "Unicast"
    else: 
        return "Multicast"


def main():
    assert_function()

    mac_address = input("Please enter a mac address that you want to check. ")

    ok = check_address(mac_address)
    print(ok)

    if ok:
        print(f"valid mac address {mac_address[:8]}, the address is {check_cast(mac_address)}")
    else:
        print(f"invalid mac address {mac_address}")

if __name__ == "__main__":
    main()