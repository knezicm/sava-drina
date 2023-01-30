#-----------------------------------------------------------------------------
#--  % Name        : run.py         %                                       --                                      --
#--  % Version     : 1.0            %                                       --
#--  % Created_By  : SAVA - DRINA %                                       --
#--  % Date_Created: 2023-01-28    %                                       --
#--                                                                         --
#--  Description:                                                           --
#--  python script file to execute testbench via Vunit.                     --
#--                                                                         --
#-----------------------------------------------------------------------------

from pathlib import Path
from vunit import VUnit

# ROOT
ROOT = Path(__file__).resolve().parent

# Sources path for DUT
DUT_PATH = ROOT / "design"

# Sources path for TB
TEST_PATH = ROOT / "testbench"

# create Vunit instance
VU = VUnit.from_argv()
VU.enable_location_preprocessing()

# create design library
design_lib = VU.add_library("design_lib")
# add design source files to design_lib
design_lib.add_source_files([DUT_PATH / "*.vhdl"])
    
# create testbench library
tb_lib = VU.add_library("tb_lib")
# add testbench source files to tb_lib
tb_lib.add_source_files([TEST_PATH / "*.vhdl"])

VU.set_sim_option("modelsim.vsim_flags", ["+notimingchecks"])
for tb in tb_lib.get_test_benches():
  tb.set_sim_option("modelsim.init_file.gui", str(ROOT) + "/waves/" + tb.name + "_wave.do")

VU.main()