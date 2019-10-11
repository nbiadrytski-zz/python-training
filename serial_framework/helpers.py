LOG_DEBUG_INFO = False


def debug_print(prefix, string, suffix):
    global LOG_DEBUG_INFO
    if LOG_DEBUG_INFO:
        print("DEBUG: ", prefix, string, suffix)


def debug_dump_hex(prefix, byte_array, suffix):
    debug_print(prefix, ''.join('{:02x} '.format(x) for x in byte_array), suffix)
