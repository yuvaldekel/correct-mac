A = ord("A")
F = ord("F")
_0 = ord('0')
_9 = ord('9')

def check_address(address):
    if not isinstance(address, str):
        return False
    
    address = address.strip()
    bytes = address.split(":")
    
    if len(bytes) != 6:
        return False
    
    for byte in bytes:
        if len(byte) != 2:
            return False
        byte = byte.upper()
        
        for char in byte:
            char = ord(char)

            if not ((A <= char <= F) or (_0 <= char <= _9)):
                return False
        
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
    print(assert_result("11-22-33-44-55-66", False))
    print(assert_result("11:22:33:44:55", False))
    print(assert_result("H:22:33:44:55:661", False))



def main():
    mac_address = input("Please enter a mac address that you want to check. ")

    ok = check_address(mac_address)

    if ok:
        print(mac_address[:8])

if __name__ == "__main__":
    main()