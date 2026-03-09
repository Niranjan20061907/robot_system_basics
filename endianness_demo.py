import struct

packet = b"\x78\x56\x34\x12"

depth = struct.unpack("<I", packet)[0]

print("Depth:", depth)
