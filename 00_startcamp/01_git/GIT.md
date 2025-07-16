# git : 분산 버전 관리 시스템
## 분산 구조의 장점
- 중앙 서버에 의존하지 않고 동시에 다양한 작업 수행
    - 작업 충돌 줄임, 개발 생산성 향상
- 중앙 서버 장애나 손실에 대비하여 백업 & 복구 용이
- 인터넷 환경 아니어도 작업 가능
    - 변경 이력 & 코드를 로컬 저장소에 기록, 나중에 중앙 서버와 동기화
## git의 역할
- 코드의 버전 관리
- 개발되어 온 과정 파악
- 이전 버전과의 변경 사항 비교

# git의 영역
- Working Directory
    - 실제 파일들이 위치하는 영역
- Staging Area
    - working directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
- Repository
    - 버전 이력과 파일들이 영구적으로 저장되는 영역
    - 모든 버전과 변경 이력이 기록됨
    - commit : 버전 (변경된 파일 저장)

# git의 동작
- `git init`
    - 로컬 저장소 설정 (초기화)
    - git의 버전 관리 시작할 디렉토리에서 진행
- `git add`
    - **변경 사항**이 있는 파일을 staging area에 추가
- `git status`
    - 현재 상태 설명
- `git commit`
    - staging area에 있는 파일들을 저장소에 기록
    - 해당 시점의 버전을 생성하고 변경 이력을 남기는 것
    - user 정보 입력
        - `git config --global user.email "e-mail"`
        - `git config --global user.name "name"`
        - `code ~ /. gitconfig` : 정보 수정
    - `git commit -m "name"`
    - `git log` : log 보기 (Author, Date)
