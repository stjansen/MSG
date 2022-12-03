 # Convert string binary representation to digit.
def convertToDigit(output):
    digit = 0
    idx = 0
    for i in output[::-1]:
        digit += int(i) * 2 ** idx
        idx += 1
    
    return digit

# Check if hostile enemy is detected
def isHostile(entry_digits, verbose = 0):
    even = 0
    odd = 0
    for entry_digits_single in entry_digits:
        if entry_digits_single % 2 == 0:
            even += 1
        else:
            odd += 1
    
    if verbose >= 2:
        print(f"detected entries: {even} even, {odd} odd")

    return even < odd

# Convert a full entry to digits
def convertToDigitFullEntry(entry, verbose = 0):
    entry_digits = []
    for e in entry:
        entry_digit = convertToDigit(e)
        entry_digits.append(entry_digit)

    if verbose >= 2:
        print(f"Detected numbers: {entry_digits}")
        
    return entry_digits

# Identification Friend or Foe (IFF)
def iff(entry, verbose = False):
    if verbose >= 1:
        print("-- IFF --")
    entry_digits = convertToDigitFullEntry(entry, verbose)
    is_hostile = isHostile(entry_digits, verbose)
    if verbose >= 1:
        print(f"Hostile object detected: {is_hostile}")
    
    return is_hostile