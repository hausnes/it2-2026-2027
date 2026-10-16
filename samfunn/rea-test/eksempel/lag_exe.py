"""Lager en minimal 64-bits Windows-EXE (PE32+) uten kompilator.

Programmet tilsvarer omtrent denne C-koden:

    int add(int a, int b) { return a + b; }
    int main(void)        { return add(2, 3); }

Bruk:  python3 lag_exe.py hello.exe
"""
import struct
import sys

# Maskinkoden (x86-64) skrevet direkte som byte. Kommentarene viser
# hvilken instruksjon hver bytesekvens er.
kode = bytes.fromhex(
    "4883ec28"          # sub rsp, 0x28     ; gjør plass på stakken (Windows-krav)
    "b902000000"        # mov ecx, 2        ; 1. argument = 2
    "ba03000000"        # mov edx, 3        ; 2. argument = 3
    "e80d000000"        # call add          ; hopp 13 byte fram, til add
    "4883c428"          # add rsp, 0x28     ; rydd opp stakken
    "c3"                # ret               ; avslutt (svaret ligger i eax)
    "cccccccccccccccc"  # int3 ×8           ; utfylling så add starter på 0x20
    "8d0411"            # add: lea eax, [rcx+rdx]  ; eax = a + b
    "c3"                # ret
)

FIL_JUSTERING = 0x200   # seksjoner ligger på 512-byte-grenser i filen
MINNE_JUSTERING = 0x1000  # ... og på 4 KB-grenser i minnet
TEXT_RVA = 0x1000       # .text lastes 0x1000 byte etter image base

# DOS-header: "MZ" + peker (e_lfanew) til PE-headeren på posisjon 0x40.
dos_header = b"MZ" + b"\0" * 58 + struct.pack("<I", 0x40)

# COFF-header: maskin = x86-64 (0x8664), 1 seksjon, kjørbar fil.
coff_header = struct.pack("<HHIIIHH", 0x8664, 1, 0, 0, 0, 240, 0x0022)

# "Optional header" (PE32+): inngangspunkt, image base, versjoner,
# størrelser og subsystem 3 = konsollprogram.
optional_header = struct.pack(
    "<HBBIIIIIQIIHHHHHHIIIIHHQQQQII",
    0x20B, 14, 0, FIL_JUSTERING, 0, 0, TEXT_RVA, TEXT_RVA,
    0x140000000, MINNE_JUSTERING, FIL_JUSTERING, 6, 0, 0, 0, 6, 0, 0,
    0x2000, FIL_JUSTERING, 0, 3, 0x8160,
    0x100000, 0x1000, 0x100000, 0x1000, 0, 16,
) + b"\0" * (16 * 8)    # 16 tomme datakataloger (ingen import, ressurser osv.)

# Seksjonstabell: én seksjon, .text, som er lesbar og kjørbar kode.
seksjon = struct.pack(
    "<8sIIIIIIHHI", b".text", len(kode), TEXT_RVA, FIL_JUSTERING, FIL_JUSTERING,
    0, 0, 0, 0, 0x60000020,
)

headere = dos_header + b"PE\0\0" + coff_header + optional_header + seksjon
fil = headere.ljust(FIL_JUSTERING, b"\0") + kode.ljust(FIL_JUSTERING, b"\0")

with open(sys.argv[1], "wb") as f:
    f.write(fil)
print(f"Skrev {len(fil)} byte til {sys.argv[1]}")
