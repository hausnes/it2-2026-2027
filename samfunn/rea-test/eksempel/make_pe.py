"""Write a minimal x64 Windows PE: entry calls add(2, 3) and returns the result."""
import struct
import sys

code = bytes.fromhex(
    "4883ec28"      # sub rsp, 0x28
    "b902000000"    # mov ecx, 2
    "ba03000000"    # mov edx, 3
    "e80d000000"    # call add (0x1020)
    "4883c428"      # add rsp, 0x28
    "c3"            # ret
    "cccccccccccccccc"
    "8d0411"        # add: lea eax, [rcx+rdx]
    "c3"            # ret
)

FILE_ALIGN, SECT_ALIGN, TEXT_RVA = 0x200, 0x1000, 0x1000
dos = b"MZ" + b"\0" * 58 + struct.pack("<I", 0x40)
coff = struct.pack("<HHIIIHH", 0x8664, 1, 0, 0, 0, 240, 0x0022)
opt = struct.pack(
    "<HBBIIIIIQIIHHHHHHIIIIHHQQQQII",
    0x20B, 14, 0, FILE_ALIGN, 0, 0, TEXT_RVA, TEXT_RVA,
    0x140000000, SECT_ALIGN, FILE_ALIGN, 6, 0, 0, 0, 6, 0, 0,
    0x2000, FILE_ALIGN, 0, 3, 0x8160,
    0x100000, 0x1000, 0x100000, 0x1000, 0, 16,
) + b"\0" * (16 * 8)
section = struct.pack(
    "<8sIIIIIIHHI", b".text", len(code), TEXT_RVA, FILE_ALIGN, FILE_ALIGN,
    0, 0, 0, 0, 0x60000020,
)
headers = dos + b"PE\0\0" + coff + opt + section
image = headers.ljust(FILE_ALIGN, b"\0") + code.ljust(FILE_ALIGN, b"\0")
open(sys.argv[1], "wb").write(image)
