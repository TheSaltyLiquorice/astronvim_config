import re
import os
import json

grlib = os.environ['GRLIB']

if not grlib:
    print("GRLIB env var not specified")
    exit()

# This could probably be changed
print("This script must be run from a build directory in order for the makefile to include the correct files, eg. designs/noelv-generic")
print("Enter design directory relative to GRLIB")

design_dir = grlib+input()+"/"
print(f"Chosen design directory is {design_dir}")

print(f"Changing directory to {design_dir}")
os.chdir(design_dir)

stat = os.system("make scripts")

if stat == 1:
    print("Makefile doesn't contain the recipie scripts")
    exit()


regex = re.compile("(?P<TYPE>vcom|vlog).*(?P<VHD_V>-\d+)\s-work\s(?P<LIB>\w+)\s(?P<PATH>\./.*?\.\S*)")

file_list = []

with open("make.vsim", "r") as f:
    text = f.read().splitlines()

for line in text:
    pot_match = re.search(regex,line)
    if pot_match:
        path = pot_match.group("PATH")
        print(path)
        if ".." in path:
            path = path.replace("./../../", grlib)
        else:
            path = path.replace("./",design_dir)

        type = "vhdl" if "vcom" in pot_match.group("TYPE") else "verilog"
        version = pot_match.group("VHD_V")
        file_list.append({"file":path, "language":type})


opts = {
    "ghdl_analysis": [
      "-fexplicit",
      "--ieee=synopsys",
      "--work=work",
      "--mb-comments",
      "--warn-no-binding",
      f"-P{design_dir}gnu",
      f"-P{design_dir}gnu/grlib",
      f"-P{design_dir}gnu/techmap",
      f"-P{design_dir}gnu/eth",
      f"-P{design_dir}gnu/opencores",
      f"-P{design_dir}gnu/gaisler",
      f"-P{design_dir}gnu/work",
      f"--workdir={design_dir}gnu/work"
    ]
}

json_obj = {"options":opts,"files":file_list}


fname = "hdl-prj.json"
with open(fname, "w") as json_f:
    json_f.write(json.dumps(json_obj))
    print(f"wrote config to {fname}")

# GHDL needs to have done the import for the LSP to work
os.system("make -f make.ghdl ghdl-import ")

#move file to root dir
os.rename(design_dir+fname, grlib+fname)

