# Command Line Interface
## '.'의 역할
- '.' : 현재 디렉토리
- '..' : 현재의 상위 디렉토리 (부모 폴더)

## 기초 문법
- `touch`
    - 파일 생성
- `mkdir x`
    - 새 디렉토리 생성 (make directory)
- `ls`
    - 현재 작업 중인 디렉토리 내부의 폴터/파일 목록 출력 (list)
    - `ls -a` : 숨김 파일, 리스트 파일 탐색 등
- `cd`
    - 현재 작업 중인 디렉토리 변경 (위치 이동)
    - `cd ..` : 상위 폴더로 이동
    - `cd ../01_git/` : 상위 폴더의 특정 폴더로 이동
    - [Tab] 키 누르면 자동완성
- `start`
    - 폴더/파일 열기
    - `code .` : vscode로 열어줌
- `rm`
    - 파일 삭제 (휴지통에 안남음, 복구 불가)
    - `rm file1 file2` : 여러개 한 번에 삭제
    - `rm -r  folder_name/` : 폴더 삭제 (디렉토리 삭제)

- 절대 경로
    - root 디렉토리부터 목적 지점까지 거치는 모든 경로 전부 작성
    - 예 : C:/User/ssafy/Desktop
- 상대 경로
    - 현재 작업하고 있는 디렉토리 기준으로 계산된 상대적 위치 작성
    - 예 : 현재 작업 위치가 C:/User일 때,
    바탕화면 상대 경로 = ssafy/Desktop

