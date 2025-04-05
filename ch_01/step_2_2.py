from pathlib import Path
from step_2_1 import WORK_DIR

def get_total_filesize (base_dir : Path , pattern : str = "*") -> int : #path 타입, str 타입 
    total_bytes = 0
    for fullpath in base_dir.glob(pattern): # "*"패턴에 맞는 모든 파일을 찾는다.
        if fullpath.is_file():
            total_bytes += fullpath.stat().st_size
        return total_bytes
if __name__ == "__main__":
    base_dir = WORK_DIR
    filesize = get_total_filesize(base_dir, pattern="*")
    print(f"{base_dir.as_posix()=},{filesize=}bytes")
            
            
    """
    글로브 패턴 (glob pattern)
    글로브 패턴은 와일드카드 (Wild card) 문자를 활용 하여 특정 조건을 만족 하는 파일의 집합을 표현한 것 이다. 
    흔한 와일드 카드 문자는 '*' 로, 모든 문자를 의미 한다. 
    / 를 혼합하면 경로를 확장시킬 수도 있다. 예를 들어, 
    **/* 의 경우 현재 경로와 하위 경로를 의미 한다.     
    
    """