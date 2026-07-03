# test_solution.py
import os

def test_file_exists():
    """1. solution.py 파일이 제대로 존재하는지 체크합니다."""
    assert os.path.exists("solution.py") == True, "solution.py 파일이 존재하지 않습니다."

def test_add_numbers():
    """2. add_numbers 함수의 연산이 올바른지 체크합니다."""
    # solution.py에서 함수를 가져옴
    from solution import add_numbers
    
    # 다양한 케이스 테스트
    assert add_numbers(2, 3) == 5, "2 + 3은 5여야 합니다."
    assert add_numbers(-1, 1) == 0, "-1 + 1은 0이어야 합니다."
    assert add_numbers(0, 0) == 0, "0 + 0은 0이어야 합니다."