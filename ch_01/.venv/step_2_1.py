from pathlib import Path # pathlib 패키지의 Path 클래스를 불러 온다

WORK_DIR = Path(__file__).parent #변수 WORK_DIR에 소스 코드의 절대 경로를 지정한다. Path(__file__)은 파일의 경로를 Path 객체로 저장하며 parent 속성은 현재 파일의 상위 디렉터리를 불러온다. 
OUT_DIR = WORK_DIR / "output" #소스 코드의 절대 경로에 output을 붙여 저장 한다. 

if __name__ == "__main__": #이 파일이 메인 프로그램으로 실행될 때만 아래 코드를 실행한다.
    OUT_DIR.mkdir(exist_ok = True) # 함수 mkdir()은 디렉터리를 생성한다. exist_ok=True로 지정하면 디렉터리가 이미 존재해도 에러를 발생시키지 않는다.
