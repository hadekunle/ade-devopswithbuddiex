import pytest
from datetime import timedelta
from clear_things_up_solution_Obi import calculate_pt  


# Helper function to create a log file
def create_log_file(tmp_path, content):
    log_file = tmp_path / "process_log.txt"
    log_file.write_text(content)
    return str(log_file)

@pytest.mark.parametrize("log_content,expected_output", [
    # Single process starts and ends
    ("2:12:00 9/12/2020 000001 start\n6:42:45 9/16/2020 000001 end", {"000001": timedelta(days=4, hours=4, minutes=30, seconds=45)}),
    # Multiple processes start and end
    ("2:12:00 9/12/2020 000002 start\n5:44:55 9/15/2020 000002 end\n3:22:15 9/13/2020 000003 start\n16:42:45 9/26/2020 000003 end", 
     {"000002": timedelta(days=3, hours=3, minutes=32, seconds=55), "000003": timedelta(days=13, hours=13, minutes=20, seconds=30)}),
    # Process starts but does not end
    ("7:32:25 9/17/2020 000004 start", {}),
    # Invalid log entry (should be handled gracefully)
    ("invalid log entry\n2:12:00 9/12/2020 000006 start\n6:42:45 9/16/2020 000006 end", {"000006": timedelta(days=4, hours=4, minutes=30, seconds=45)}),
])
def test_calculate_pt(tmp_path, log_content, expected_output):
    # Create a temporary log file
    log_file_path = create_log_file(tmp_path, log_content)
    # Calculate process times
    actual_output = calculate_pt(log_file_path)
    # Convert output to total seconds for comparison
    actual_output_seconds = {pid: actual_output[pid].total_seconds() for pid in actual_output}
    expected_output_seconds = {pid: expected_output[pid].total_seconds() for pid in expected_output}
    assert actual_output_seconds == expected_output_seconds
