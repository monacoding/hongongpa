from pathlib import Path

WORK_DIR = Path(__file__).parent #부모 디렉토리를 가리 킨다. 
print(WORK_DIR)
OUT_DIR = WORK_DIR/"output" #본 파일이 속한 부모 폴더아래 폴더를 생성한다.

if __name__ == "__main__":
    OUT_DIR.mkdir(exist_ok=True) #
    
    