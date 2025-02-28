from src.dict_tools import combine_and_sum_dicts

def test_combine_and_sum_dict_all_keys_overlap():
    #Arrange
    dict1 = {"Magnus Carlsen": 1, "Anish Giri": 1, "Wesley So": 5}
    dict2 = {"Magnus Carlsen": 0, "Anish Giri": 3, "Wesley So": 2}

    dict_list = [dict1, dict2]

    #Act
    combined_dict = combine_and_sum_dicts(dict_list)

    #Assert
    assert combined_dict == {"Magnus Carlsen": 1, "Anish Giri": 4, "Wesley So": 7}

def test_combine_and_sum_dict_one_key_overlaps():
    # Arrange
    dict1 = {"Magnus Carlsen": 1, "Anish Giri": 1, "Alexandra Botez": 5}
    dict2 = {"Magnus Carlsen": 0, "Peter Leko": 3, "Wesley So": 2}

    dict_list = [dict1, dict2]

    # Act
    combined_dict = combine_and_sum_dicts(dict_list)

    # Assert
    assert combined_dict == {"Magnus Carlsen": 1, "Anish Giri": 1, "Alexandra Botez": 5,
                             "Peter Leko": 3, "Wesley So": 2}

def test_combine_and_sum_dict_no_keys_overlap():
    dict1 = {"Magnus Carlsen": 1}
    dict2 = {"Peter Leko": 3, "Wesley So": 2}

    dict_list = [dict1, dict2]

    # Act
    combined_dict = combine_and_sum_dicts(dict_list)

    # Assert
    assert combined_dict == {"Magnus Carlsen": 1, "Peter Leko": 3, "Wesley So": 2}

def test_combine_and_sum_dict_one_empty_dict():
    dict1 = {}
    dict2 = {"Peter Leko": 3, "Wesley So": 2}

    dict_list = [dict1, dict2]

    # Act
    combined_dict = combine_and_sum_dicts(dict_list)

    # Assert
    assert combined_dict == dict2

def test_combine_and_sum_dict_two_empty_dicts():
    dict1 = {}
    dict2 = {}

    dict_list = [dict1, dict2]

    # Act
    combined_dict = combine_and_sum_dicts(dict_list)

    # Assert
    assert combined_dict == {}

def test_combine_and_sum_dict_one_dict():
    dict1 = {"Magnus Carlsen": 1, "Anish Giri": 1, "Wesley So": 5}
    dict_list = [dict1]

    # Act
    combined_dict = combine_and_sum_dicts(dict_list)

    # Assert
    assert combined_dict == dict1

def test_combine_and_sum_dict_ensure_keys_are_case_sensitive():
    dict1 = {"Magnus Carlsen": 1}
    dict2 = {"MAGNUS Carlsen": 3, "Wesley So": 2}

    dict_list = [dict1, dict2]

    # Act
    combined_dict = combine_and_sum_dicts(dict_list)

    # Assert
    assert combined_dict == {"Magnus Carlsen": 1, "MAGNUS Carlsen": 3, "Wesley So": 2}


def test_combine_and_sum_dict_three_dicts():
    dict1 = {"Peter Leko": 1}
    dict2 = {"Peter Leko": 3, "Wesley So": 2}
    dict3 = {"Wesley So": 1, "Vidit Gujrathi": 2}

    dict_list = [dict1, dict2, dict3]

    # Act
    combined_dict = combine_and_sum_dicts(dict_list)

    # Assert
    assert combined_dict == {"Peter Leko": 4, "Wesley So": 3, "Vidit Gujrathi": 2}

