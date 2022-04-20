def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring
    if substring in full_string:
        print(f"expected {substring} to be substring of {full_string}")