from pathlib import Path
from step_2_1 import WORK_DIR # 작성한 모듈 불러오기 

def get_total_filesize(base_dir : Path, pattern: str = "*") -> int : #함수 를 정의 한다. 매개 변수 base_dir은 Path객체를, pattern은 글로브 패턴 문자열을 저장한다.
    total_bytes = 0 # 변수 초기화 
    for fullpath in base_dir.glob(pattern): # 함수 glob는 입력값으로 전달 된 글로브 패턴과 일치 하는 파일명을 리스트로 반환 한다. 
        if fullpath.is_file():# is_file함수를 이용하여 파일이 유효한지 검사 한다 
            total_bytes += fullpath.stat().st_size #바이트 단위로 저장 
    return total_bytes

if __name__ == "__main__":
    base_dir = WORK_DIR
    filesize = get_total_filesize(base_dir, pattern="*")
    print(f"{base_dir.as_posix()=},{filesize=} bytes")##
        