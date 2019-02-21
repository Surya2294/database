def test_dump_file_name_without_timestamp():

    assert pgdump.dump_file_name(url) == "db_one.sql"

def test_dump_file_name_with_timestamp():

    timestamp = "2017-12-03T13:14:10"
    assert pgdump.dump_file_name(url, timestamp) == "db_one-2017-12-03T13:14:10.sql"