# Branch
- `git branch -c viktor/login` : 브랜치 생성
- `git branch` : 브랜치 목록 확인
- `git switch viktor/login` : 브랜치 바꾸기
- `git merge viktor/login` : 불러오기
    - Fast Foward
    - three way merge
- `git branch -d viktor/login` : 브랜치 삭제
- `git push origin 브랜치명` : 원격저장소에 push
    - origin은 공유 원격저장소(clone 해온 곳)

## 순서
1. 원격 저장소에서 clone
2. 개인 브랜치 생성 + 스위치
3. 개인 작업 + 커밋
4. 원격 저장소에 push
5. merge request 생성
6. local에서 master에서 pull
7. 개인 브랜치 삭제

## conflict
- 다른 브랜치에서 같은 파일, 같은 줄 수정해서 동시에 merge하면 commit 충돌
- 해결 방법 1
    - local에서 master로 pull
    - master에서 충돌난 branch에 merge
    - conflict 해결
- 해결 방법 2
    - 내 branch에 바로 pull
    - conflict 해결
- 해결 후 원격 저장소에 push
- merge 성공
- local에서 master로 pull

## 주의사항
1. master 브랜치는 아무도 수정하지 않는다.
2. master 브랜치는 최초 설정 (모든 팀원이 함께 쓸 내용 생성시만 사용)
    - git add . git commit, push까지 진행
3. 

# etc
- 파일 생성 : `touch 파일명.`