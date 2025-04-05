import json
from pathlib import Path
from step_2_1 import OUT_DIR

OUT_2_3 = OUT_DIR/ f"{Path(__file__).stem}.json" #.stem 은 확장자는 뺀거임 

def dump_dirnames(base_dir:Path) -> None : #아무것도 반환하지 않고 파일만 저장함 
    dirs = [] # 폴더 들을 담을 빈 리스트 
    for path in base_dir.iterdir(): # base_dir에 있는 것을 하나씩 꺼내서 path에 담음 
        if path.is_dir():
            dirs.append(path.as_posix()) #as_posix 는 폴더/이름 형식으로 바꿔줌
        dirs_sorted = sorted(dirs) #sorted 는 가나다 순으로 정렬 해줌 
        with open (OUT_2_3,"w",encoding = "utf-8") as fp:
            json.dump (dirs_sorted,fp,ensure_ascii=False, indent=2)

def load_dirnames() -> list[str]: # list 를 반환 
    if OUT_2_3.is_file(): # 파일이 존재하면, 
        with open(OUT_2_3,encoding ="utf-8") as fp :# 꺼내서 
            return json.load(fp) # json 파일로 반환하라 
    return [] # json 파일이 없으면 그냥 빈 리스트로 반환하라 

if __name__ == "__main__" :
    dump_dirnames(Path.home())
        