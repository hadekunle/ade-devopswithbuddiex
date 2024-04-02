import pytest
from your_script_name import find_valid_mac_addresses  # Adjust 'your_script_name' to the name of your Python script file

# Mock data for testing
VALID_MAC_DATA = """
s01 3D:A0:EA:A3:A7:91 07/31/2020
s02 CF:FD:D4:1C:C3:74 07/31/2020
s07 EC:DD:B5:AE:E2:DA 07/31/2020
"""

INVALID_MAC_DATA = """
s03 B7:75:A7:1D:4B:D2G 07/31/2020
s04 57:6E:EF:FB:FF;8C 07/31/2020
s05 39:8FC0:47:7B:C1 07/31/2020
"""

PARTIAL_INVALID_MAC_DATA = """
s06 2D:F6:0C:9E:4F:C2 07/31/2020
s08 21:29:CE:BE:CA:55 07/31/2020
s09 6E:3A:D0:DB:CA:97 07/31/2020
"""

# Function to simulate file reading from strings (used for testing)
def create_temp_file(data_str, tmpdir):
    temp_file = tmpdir.join("temp_mac.txt")
    temp_file.write(data_str)
    return temp_file

# Test cases
def test_valid_mac_addresses(tmpdir):
    temp_file = create_temp_file(VALID_MAC_DATA, tmpdir)
    result = find_valid_mac_addresses(str(temp_file))
    assert len(result) == 3  # Expecting three valid entries
    assert result[0] == ('s01', '3D:A0:EA:A3:A7:91')  # Checking specific valid entry

def test_no_valid_mac_addresses(tmpdir):
    temp_file = create_temp_file(INVALID_MAC_DATA, tmpdir)
    result = find_valid_mac_addresses(str(temp_file))
    assert len(result) == 0  # Expecting no valid entries

def test_partial_invalid_mac_addresses(tmpdir):
    temp_file = create_temp_file(PARTIAL_INVALID_MAC_DATA, tmpdir)
    result = find_valid_mac_addresses(str(temp_file))
    assert len(result) == 3  # Expecting three valid entries out of mixed valid and invalid data
    assert ('s06', '2D:F6:0C:9E:4F:C2') in result  # Checking one of the valid entries

