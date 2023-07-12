# common msg
BEGIN_MSG = b"BEGIN"
DONE_MSG = b"DONE"

# send recv msg
READY_MSG = b"READY"
WRITE_DONE = b"WRITE"
READ_DONE = b"READ"

# file msg
# PUSH_FILE_MSG = b"PUSH_FILE"
# FILE_BEGIN_MSG = b"FILE_BEGIN"
# FILE_READY_MSG = b"FILE_READY"
# FILE_DONE_MSG = b"FILE_DONE"
PUSH_FILE_MSG = b"PUSH_FILE"
PULL_FILE_MSG = b"PULL_FILE"
FILE_BEGIN_MSG = bytes([1])
FILE_READY_MSG = bytes([2])
FILE_DONE_MSG = bytes([3])
FILE_ERR_MSG = bytes([4])
