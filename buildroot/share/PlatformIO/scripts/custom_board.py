#
# custom_board.py
#
# - For build.address replace VECT_TAB_ADDR to relocate the firmware
# - For build.ldscript use one of the linker scripts in buildroot/share/PlatformIO/ldscripts
#
import pioutil
if pioutil.is_pio_build():
	import marlin
	board = marlin.env.BoardConfig()

	if address := board.get("build.address", ""):
		marlin.relocate_firmware(address)

	if ldscript := board.get("build.ldscript", ""):
		marlin.custom_ld_script(ldscript)
