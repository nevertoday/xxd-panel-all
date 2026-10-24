<div align="center">

# XXD Panel All｜스타일 총목록

**354가지 사진 스타일의 입구. 사진과 용도를 알려 주면 스타일을 고르고, 비교하고, 한꺼번에 만들어 줍니다.**

<a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <a href="README.ja.md">日本語</a> · <strong>한국어</strong> · <a href="README.ar.md">العربية</a>

</div>

<table>
  <tr>
    <td width="33%"><a href="https://github.com/nevertoday/xxd-panel-001"><img src="./assets/roster/001.jpg" alt="XXD Panel 001 · 레트로 천진 수첩"></a></td>
    <td width="33%"><a href="https://github.com/nevertoday/xxd-panel-062"><img src="./assets/roster/062.jpg" alt="XXD Panel 062 · 영리하고 서툰 선"></a></td>
    <td width="33%"><a href="https://github.com/nevertoday/xxd-panel-350"><img src="./assets/roster/350.jpg" alt="XXD Panel 350 · 네온 정령"></a></td>
  </tr>
</table>

## 무엇인가요

XXD Panel은 사진을 포스터, 일러스트, 배경화면으로 다시 그리는 AI Skill 모음으로, 번호마다 스타일이 하나씩 있고 지금 354개가 서로 독립돼 있습니다. `xxd-panel-all`은 그 입구이며 Claude Code, Codex 등 Skills를 지원하는 에이전트에서 씁니다:

- **골라 줍니다:** 사진이나 주제를 주면 설치된 스타일 가운데 하나 또는 세 개를 추천하고, 왜 이 사진에 맞는지 알려 줍니다.
- **비교해 줍니다:** 같은 사진을 여러 스타일로 한 장씩 만들어 나란히 볼 수 있습니다.
- **한꺼번에 만듭니다:** 폴더를 주면 전부 같은 스타일로, 또는 사진마다 가장 맞는 스타일로 만듭니다.
- **직접 그리지는 않습니다:** 실제로 그리는 것은 번호가 붙은 스타일 Skill입니다. 총목록은 고르고 넘겨줄 뿐, 스타일을 섞지 않습니다.

## 세 단계로 시작하기

**1. 총목록과 마음에 드는 스타일 몇 개를 설치.** 설치하지 않은 스타일도 소개하고 추천할 수 있지만, 이미지는 설치한 스타일로만 만듭니다:

```bash
npx skills add https://github.com/nevertoday/xxd-panel-all --skill xxd-panel-all
npx skills add https://github.com/nevertoday/xxd-panel-001 --skill xxd-panel-001
```

여러 개를 한 번에:

```bash
for n in 001 062 350; do npx skills add https://github.com/nevertoday/xxd-panel-$n --skill xxd-panel-$n; done
```

설치 후 에이전트 세션을 다시 시작하세요.

**2. 에이전트가 이미지를 생성할 수 있는지 확인.** 이 Skill에는 자체 이미지 모델이 없고, 에이전트의 이미지 생성(GPT Image 2 권장)을 사용합니다.

- Codex는 내장 이미지 생성이 켜져 있으면 바로 쓸 수 있습니다.
- Claude Code처럼 내장 이미지 생성이 없는 에이전트는 OpenAI 호환 이미지 API가 필요합니다. 5분 정도면 됩니다: [이미지 생성 설정](#이미지-생성-설정).

잘 모르겠다면 그냥 써 보세요. 생성할 수 없으면 작업을 시작하기 전에 Skill이 멈추고 알려 줍니다.

**3. 사진을 보내고 한 문장으로 말하기:**

> xxd-panel-all로 이 사진에 맞는 스타일 세 개를 이유와 함께 추천해 줘.

고르고 나면 사진은 그 스타일의 Skill로 넘어가고, 레이아웃·비율·글자는 그쪽에서 묻습니다. 결과물은 `~/Desktop/xxd/xxd-panel-NNN/`에 저장됩니다.

## 이렇게 말하면 됩니다

파라미터를 외울 필요 없이 그대로 말하세요:

| 원하는 것 | 이렇게 말하기 |
|---|---|
| 추천받기 | 이 사진에 맞는 스타일은? 세 개 추천하고 이유도 |
| 느낌으로 찾기 | 검은 선에 여백이 많은 스타일 있어? |
| 용도로 찾기 | 휴대폰 배경화면에 어울리는 스타일은? |
| 번호 지정 | 062로 이 사진을 만들어 줘 |
| 비교 | 001, 062, 350으로 한 장씩 만들어 비교하게 해 줘 |
| 폴더, 같은 스타일 | 이 폴더 전부 014로 위아래 비교로 만들어 줘 |
| 폴더, 자동 배정 | 이 폴더의 사진마다 가장 맞는 스타일을 골라 줘 |
| 지난번과 같이 | 지난번 설정 그대로 |

## 전체 스타일

모두 354개. 각 이미지는 그 스타일의 좌우 비교 샘플 한 장입니다(왼쪽 사진, 오른쪽 디자인). 누르면 저장소가 열려 더 많은 샘플과 사용법을 볼 수 있습니다.

<!-- xxd-soldier-roster:start -->

<details open>
<summary><strong>001–050</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-001"><img src="./assets/roster/001.jpg" alt="XXD Panel 001 · 레트로 천진 수첩" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-001"><strong>001</strong> · 레트로 천진 수첩</a><br><sub>사진을 가볍고 종이 질감이 살아 있으며 조금 서툴고 유머러스한 레트로 손그림 일러스트로 바꿉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-002"><img src="./assets/roster/002.jpg" alt="XXD Panel 002 · 장난스러운 바우하우스" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-002"><strong>002</strong> · 장난스러운 바우하우스</a><br><sub>사진을 바우하우스풍 기하와 흔들리는 윤곽, 인쇄 어긋남이 있는 레트로 편집 일러스트로 바꿉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-003"><img src="./assets/roster/003.jpg" alt="XXD Panel 003 · 긴장감 있는 선의 언어" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-003"><strong>003</strong> · 긴장감 있는 선의 언어</a><br><sub>사진 속 방향, 연결, 압박, 전환을 고요하지만 팽팽한 검은 연속선 하나로 묶습니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-004"><img src="./assets/roster/004.jpg" alt="XXD Panel 004 · 도시 원라인 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-004"><strong>004</strong> · 도시 원라인 저널</a><br><sub>실제 도시나 장소의 풍경을 정확한 단선과 기하학적 원근의 소장용 선화 포스터로 정리합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-005"><img src="./assets/roster/005.jpg" alt="XXD Panel 005 · 어두운 동화 에디션" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-005"><strong>005</strong> · 어두운 동화 에디션</a><br><sub>사진을 커다란 어두운 형태가 감싸고 중요한 곳에만 밝은 색이 반짝이는 동화 판화로 바꿉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-006"><img src="./assets/roster/006.jpg" alt="XXD Panel 006 · 여백의 소극장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-006"><strong>006</strong> · 여백의 소극장</a><br><sub>사진을 작은 주인공 하나로 줄여 넓은 종이 여백에 두어 아트북 표지처럼 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-007"><img src="./assets/roster/007.jpg" alt="XXD Panel 007 · 손그림 관찰 페이지" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-007"><strong>007</strong> · 손그림 관찰 페이지</a><br><sub>사진을 작은 그림, 단면도, 손글씨 짧은 말로 엮은 생활 관찰 노트 한 페이지로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-008"><img src="./assets/roster/008.jpg" alt="XXD Panel 008 · 파스텔 몽환경" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-008"><strong>008</strong> · 파스텔 몽환경</a><br><sub>사진 속 사람과 이야기를 밝고 고요한, 모뉴먼트 밸리 같은 파스텔 불가능 공간으로 바꿉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-009"><img src="./assets/roster/009.jpg" alt="XXD Panel 009 · 하프톤 앵커 프린트" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-009"><strong>009</strong> · 하프톤 앵커 프린트</a><br><sub>사진을 아주 작은 기준점 하나로 줄여 넓은 종이 위에, 촘촘함에서 성김으로 사라지는 망점으로 거리와 공기를 찍어 냅니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-010"><img src="./assets/roster/010.jpg" alt="XXD Panel 010 · 흑백 옛 그림책" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-010"><strong>010</strong> · 흑백 옛 그림책</a><br><sub>사진을 흰 종이 위에 굵은 검은 크레용으로 칠한 그림책 실루엣으로 바꿉니다. 색은 검정과 흰색뿐입니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-011"><img src="./assets/roster/011.jpg" alt="XXD Panel 011 · 명상하는 선의 시" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-011"><strong>011</strong> · 명상하는 선의 시</a><br><sub>사진을 천천히 바라보게 되는 검은 가는 연속선으로 정리하고, 의미 있는 색 하나만 남깁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-012"><img src="./assets/roster/012.jpg" alt="XXD Panel 012 · 생명의 기하학" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-012"><strong>012</strong> · 생명의 기하학</a><br><sub>사진의 주인공을 한 가지 색의 촘촘한 선의 장에서 모여 드러나게 하고, 둘레에 기하학적인 가는 선을 펼칩니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-013"><img src="./assets/roster/013.jpg" alt="XXD Panel 013 · 여행 티켓 앨범" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-013"><strong>013</strong> · 여행 티켓 앨범</a><br><sub>사진을 왼쪽은 수채화, 오른쪽은 티켓 꼭지로 된, 소중히 간직한 여행 티켓 한 장으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-014"><img src="./assets/roster/014.jpg" alt="XXD Panel 014 · 종이 부조 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-014"><strong>014</strong> · 종이 부조 저널</a><br><sub>사진을 접힌 자국과 자른 면, 종이 섬유까지 보이는 현대 종이접기 조각으로 다시 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-015"><img src="./assets/roster/015.jpg" alt="XXD Panel 015 · 추상 회고록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-015"><strong>015</strong> · 추상 회고록</a><br><sub>사진을 해체하고 골라 몇 개의 기하 형태와 섬세한 편집 글자로 다시 짜서 아트북의 한 페이지처럼 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-016"><img src="./assets/roster/016.jpg" alt="XXD Panel 016 · 운동감 판화" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-016"><strong>016</strong> · 운동감 판화</a><br><sub>사진에서 실제로 일어나는 일을 아주 작은 주인공 하나와 그를 둘러싼 하나의 움직임으로 압축합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-017"><img src="./assets/roster/017.jpg" alt="XXD Panel 017 · 천진 그래픽 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-017"><strong>017</strong> · 천진 그래픽 저널</a><br><sub>사진을 거친 검은 선과 밝은 단색 면으로 그린 한국식 천진한 편집 일러스트로 바꿉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-018"><img src="./assets/roster/018.jpg" alt="XXD Panel 018 · 손 종이오리기 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-018"><strong>018</strong> · 손 종이오리기 저널</a><br><sub>종이 주인공 하나와 앞·중간·뒤 종이 몇 겹, 정밀한 작은 글자로 사진을 손으로 오린 겹종이 작품으로 다시 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-019"><img src="./assets/roster/019.jpg" alt="XXD Panel 019 · 레트로 그래픽 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-019"><strong>019</strong> · 레트로 그래픽 저널</a><br><sub>사진 속 주인공과 관계를 여전히 알아볼 수 있는 레트로 모더니즘 평면 일러스트로 다시 짭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-020"><img src="./assets/roster/020.jpg" alt="XXD Panel 020 · 임파스토 미니 풍경" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-020"><strong>020</strong> · 임파스토 미니 풍경</a><br><sub>사진 속 주인공과 이야기를 두꺼운 임파스토 물감 덩어리에서 자라나는, 만질 수 있을 듯한 입체 미니어처 장면으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-021"><img src="./assets/roster/021.jpg" alt="XXD Panel 021 · 검은 영역 넘기" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-021"><strong>021</strong> · 검은 영역 넘기</a><br><sub>사진의 주인공이 새까만 직사각형에서 몸을 내밀게 하고, 떨리는 검은 선과 흰 형태로 그립니다. 색은 흑백과 회색뿐입니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-022"><img src="./assets/roster/022.jpg" alt="XXD Panel 022 · 색점의 경계 넘기" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-022"><strong>022</strong> · 색점의 경계 넘기</a><br><sub>사진의 주인공이 매끄러운 선으로 새까만 직사각형 밖으로 넘어 나오게 하고, 가장 중요한 한 곳에만 색을 둡니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-023"><img src="./assets/roster/023.jpg" alt="XXD Panel 023 · 동양의 창밖 풍경" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-023"><strong>023</strong> · 동양의 창밖 풍경</a><br><sub>사진을 주인공에 맞춰 고른 중국식 창 안에 담아, 창살 사이로 든 햇빛이 연한 벽에 떨어진 듯한 장면으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-024"><img src="./assets/roster/024.jpg" alt="XXD Panel 024 · 감정의 창" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-024"><strong>024</strong> · 감정의 창</a><br><sub>사진 속 실제 대상이 가늘고 긴 연한 기하학 창을 통과하게 하여, 미니멀한 고급 광고 포스터로 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-025"><img src="./assets/roster/025.jpg" alt="XXD Panel 025 · 보이지 않는 심상" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-025"><strong>025</strong> · 보이지 않는 심상</a><br><sub>사진을 한눈에는 주인공이, 두 번째 볼 때는 숨은 다른 그림이 보이는 모란디 톤 실크스크린 판화로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-026"><img src="./assets/roster/026.jpg" alt="XXD Panel 026 · 기하학적 질서" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-026"><strong>026</strong> · 기하학적 질서</a><br><sub>사진 속 사실을 조용하고 온화하면서도 한눈에 알아볼 수 있는 기하학적 질서로 옮깁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-027"><img src="./assets/roster/027.jpg" alt="XXD Panel 027 · 종이 위 부조" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-027"><strong>027</strong> · 종이 위 부조</a><br><sub>사진을 두꺼운 유백색 종이에 눌러 낸 동양 박물관풍 얕은 부조로 만들고, 핵심에만 무광 금색을 둡니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-028"><img src="./assets/roster/028.jpg" alt="XXD Panel 028 · 아이소메트릭 미니 풍경" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-028"><strong>028</strong> · 아이소메트릭 미니 풍경</a><br><sub>사진을 원래 색으로 그린 종이 위 아이소메트릭 미니어처 모형, 작은 건축 디오라마처럼 놓아 둡니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-029"><img src="./assets/roster/029.jpg" alt="XXD Panel 029 · 종이 위 느린 스케치" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-029"><strong>029</strong> · 종이 위 느린 스케치</a><br><sub>사진을 가로로 놓인 저채도 색면 위에 그린 느긋한 왁스 파스텔 그림으로 만들고, 무심하게 쓴 한 줄을 곁들입니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-030"><img src="./assets/roster/030.jpg" alt="XXD Panel 030 · 자연의 경계 넘기" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-030"><strong>030</strong> · 자연의 경계 넘기</a><br><sub>진짜 잎, 꽃잎, 잔가지, 열매, 씨앗, 풀줄기, 나무껍질로 사진의 주인공을 다시 짜 맞춥니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-031"><img src="./assets/roster/031.jpg" alt="XXD Panel 031 · 우의적 탁본" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-031"><strong>031</strong> · 우의적 탁본</a><br><sub>먼저 사진 뒤에 담긴 뜻을 읽고, 기하학적으로 엄밀하고 탁본의 거친 질감을 지닌 핵심 모티프 하나로 정리합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-032"><img src="./assets/roster/032.jpg" alt="XXD Panel 032 · 그래픽 워드마크" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-032"><strong>032</strong> · 그래픽 워드마크</a><br><sub>사진 주인공의 결정적인 특징을 맞춤 워드마크의 글자 구조 안에 넣습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-033"><img src="./assets/roster/033.jpg" alt="XXD Panel 033 · 선명한 콜라주 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-033"><strong>033</strong> · 선명한 콜라주 저널</a><br><sub>한 장의 사진을 선명하고 진하며 층이 분명한 현대 잡지 표지 콜라주로 바꿉니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-034"><img src="./assets/roster/034.jpg" alt="XXD Panel 034 · 여행 스탬프 마크" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-034"><strong>034</strong> · 여행 스탬프 마크</a><br><sub>사진을 작은 다색 고무도장 하나로 줄이고, 조용한 현장 기록을 곁들입니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-035"><img src="./assets/roster/035.jpg" alt="XXD Panel 035 · 블록 재구성" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-035"><strong>035</strong> · 블록 재구성</a><br><sub>사진의 주인공을 선명하고 한눈에 알아볼 수 있는 복셀 블록 컬렉터블로 다시 조립합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-036"><img src="./assets/roster/036.jpg" alt="XXD Panel 036 · 유선형 그림책" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-036"><strong>036</strong> · 유선형 그림책</a><br><sub>사진 속 관계를 몇 줄의 이어진 가는 선으로 그리고, 투명한 색이 종이 위를 천천히 흐르게 합니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-037"><img src="./assets/roster/037.jpg" alt="XXD Panel 037 · 흐르는 금빛 엠블럼" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-037"><strong>037</strong> · 흐르는 금빛 엠블럼</a><br><sub>여행지의 사진을 수집하고 싶은 유금 에나멜 배지 하나로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-038"><img src="./assets/roster/038.jpg" alt="XXD Panel 038 · 직물 생활 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-038"><strong>038</strong> · 직물 생활 저널</a><br><sub>사진과 사진이 말하지 않은 감정을 따뜻한 손바느질 패치워크 그림으로 꿰맵니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-039"><img src="./assets/roster/039.jpg" alt="XXD Panel 039 · 자수 심상" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-039"><strong>039</strong> · 자수 심상</a><br><sub>사진에서 가장 남길 만한 이미지 하나만 골라 생생한 비단 광택 속에 수놓습니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-040"><img src="./assets/roster/040.jpg" alt="XXD Panel 040 · 낙서 친구" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-040"><strong>040</strong> · 낙서 친구</a><br><sub>사진에서 가장 기억할 만한 실제 대상을 남기고, 검은 선 낙서 사람들이 그 주위에서 작은 연극을 펼칩니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-041"><img src="./assets/roster/041.jpg" alt="XXD Panel 041 · 아이소메트릭 연구실" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-041"><strong>041</strong> · 아이소메트릭 연구실</a><br><sub>사진의 주인공과 사진에서 길어 올린 하나의 주제를 맑은 아이소메트릭 연구도로 짜 맞춥니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-042"><img src="./assets/roster/042.jpg" alt="XXD Panel 042 · 해체된 수채 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-042"><strong>042</strong> · 해체된 수채 저널</a><br><sub>사진의 주인공을 실제 구조를 따라 층층이 펼쳐, 다시 조립할 수 있는 수채 연구도로 그립니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-043"><img src="./assets/roster/043.jpg" alt="XXD Panel 043 · 하얀 거품" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-043"><strong>043</strong> · 하얀 거품</a><br><sub>진짜 하얀 비누 거품으로 짙고 젖은 평면 위에 사진의 주인공을 다시 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-044"><img src="./assets/roster/044.jpg" alt="XXD Panel 044 · 플랫 퓨어 골드" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-044"><strong>044</strong> · 플랫 퓨어 골드</a><br><sub>사진 주인공의 결정적인 형태를 짙은 바탕 위 얇은 순금 한 겹으로 눌러 담습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-045"><img src="./assets/roster/045.jpg" alt="XXD Panel 045 · 힐링 블록 도시" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-045"><strong>045</strong> · 힐링 블록 도시</a><br><sub>사진의 주인공을 둥글고 만지고 싶은, 부드러운 색의 블록 조각으로 다시 쌓습니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-046"><img src="./assets/roster/046.jpg" alt="XXD Panel 046 · 임파스토 미니 월드" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-046"><strong>046</strong> · 임파스토 미니 월드</a><br><sub>사진을 밝고 생기 있으며 물감 두께가 느껴지는 임파스토 미니어처 풍경으로 다시 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-047"><img src="./assets/roster/047.jpg" alt="XXD Panel 047 · 아이소메트릭 임파스토 풍경" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-047"><strong>047</strong> · 아이소메트릭 임파스토 풍경</a><br><sub>사진의 주인공을 정교한 아이소메트릭 미니어처로 만들어 살아 있는 임파스토 색면 안에 세웁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-048"><img src="./assets/roster/048.jpg" alt="XXD Panel 048 · 투명 구조 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-048"><strong>048</strong> · 투명 구조 저널</a><br><sub>사진의 주인공을 반투명하게 만들고, 그 구조의 논리를 맑은 설계도로 그립니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-049"><img src="./assets/roster/049.jpg" alt="XXD Panel 049 · 목판 각인" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-049"><strong>049</strong> · 목판 각인</a><br><sub>사진에서 가장 마음에 남는 부분을 맑고 부드러운 제한색 목판화로 새깁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-050"><img src="./assets/roster/050.jpg" alt="XXD Panel 050 · 여행 엽서" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-050"><strong>050</strong> · 여행 엽서</a><br><sub>사진 한 장 한 장을 그곳만을 위한 에어리 블루 미니멀 여행 포스터로 그립니다.</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>051–100</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-051"><img src="./assets/roster/051.jpg" alt="XXD Panel 051 · 수제 미니어처 섬" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-051"><strong>051</strong> · 수제 미니어처 섬</a><br><sub>사진의 주인공을 가볍고 만지고 싶은 수제 종이공예 미니어처로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-052"><img src="./assets/roster/052.jpg" alt="XXD Panel 052 · 종이공예 미니어처 섬" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-052"><strong>052</strong> · 종이공예 미니어처 섬</a><br><sub>사진 속 세계를 손으로 만든 종이 미니어처로 바꿔 하나의 풍경선 위에 살며시 띄웁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-053"><img src="./assets/roster/053.jpg" alt="XXD Panel 053 · 펜 담채 기록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-053"><strong>053</strong> · 펜 담채 기록</a><br><sub>관찰한 펜 선과 몇 군데의 담채로 사진을 기록하고, 가장 알맞은 곳에서 붓을 멈춥니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-054"><img src="./assets/roster/054.jpg" alt="XXD Panel 054 · 추억 스티커 앨범" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-054"><strong>054</strong> · 추억 스티커 앨범</a><br><sub>하나의 기억을 주된 그림 하나와 크기가 다른 스티커 조각 여섯 개로 나눕니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-055"><img src="./assets/roster/055.jpg" alt="XXD Panel 055 · 회화적 기억의 장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-055"><strong>055</strong> · 회화적 기억의 장</a><br><sub>사진 속 한 줄기 빛, 하나의 동작, 하나의 공간 관계를 부드러운 그림 한 장으로 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-056"><img src="./assets/roster/056.jpg" alt="XXD Panel 056 · 여백의 기억 그림" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-056"><strong>056</strong> · 여백의 기억 그림</a><br><sub>사진에서 핵심 이미지 하나만 남기고, 거대한 여백 속에 서툰 붓결과 따뜻하고 차가운 색의 도약으로 다시 그립니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-057"><img src="./assets/roster/057.jpg" alt="XXD Panel 057 · 기하학적 기억의 장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-057"><strong>057</strong> · 기하학적 기억의 장</a><br><sub>기하 색면과 질서 있는 모자이크로 사진을 고요하고 따뜻한 현대 콜라주로 다시 짭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-058"><img src="./assets/roster/058.jpg" alt="XXD Panel 058 · 시적 개념 풍경" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-058"><strong>058</strong> · 시적 개념 풍경</a><br><sub>사진이 암시하는 것을 읽어 내고, 엄격한 기하로 시적인 개념 풍경을 짜 올립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-059"><img src="./assets/roster/059.jpg" alt="XXD Panel 059 · 손그림 우화집" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-059"><strong>059</strong> · 손그림 우화집</a><br><sub>사진이 말하지 않은 이야기를 따뜻하고 천진하며 은근히 영리한 우화 그림책의 한 페이지로 그립니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-060"><img src="./assets/roster/060.jpg" alt="XXD Panel 060 · 선(禪) 미니멀 시" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-060"><strong>060</strong> · 선(禪) 미니멀 시</a><br><sub>사진을 한 개에서 세 개의 검은 형태와 거대한 여백으로 응축해, 고요한 울림이 남는 시각적 사유로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-061"><img src="./assets/roster/061.jpg" alt="XXD Panel 061 · 시각 기억 노트" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-061"><strong>061</strong> · 시각 기억 노트</a><br><sub>사진을 종이 위에 흩어져 서로 울리는 몇 개의 시각적 기억 조각으로 다시 짭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-062"><img src="./assets/roster/062.jpg" alt="XXD Panel 062 · 영리하고 서툰 선" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-062"><strong>062</strong> · 영리하고 서툰 선</a><br><sub>서툰 검은 선과 사진 속 한 가지 색만으로 사진에서 가장 기억할 만한 순간을 그립니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-063"><img src="./assets/roster/063.jpg" alt="XXD Panel 063 · 픽셀 은유 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-063"><strong>063</strong> · 픽셀 은유 저널</a><br><sub>사진을 큰 픽셀 윤곽 하나와 부드러운 색면 몇 개가 만드는 조용한 은유로 다시 짭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-064"><img src="./assets/roster/064.jpg" alt="XXD Panel 064 · 인디 콜라주 페이지" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-064"><strong>064</strong> · 인디 콜라주 페이지</a><br><sub>사진을 조용하고 이지러졌으며 시간의 흔적이 느껴지는 옛 종이 콜라주 한 장으로 바꿉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-065"><img src="./assets/roster/065.jpg" alt="XXD Panel 065 · 투 라인 에디토리얼 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-065"><strong>065</strong> · 투 라인 에디토리얼 저널</a><br><sub>검은 선으로 뼈대를 세우고, 사진 속 두 가지 색 선을 어긋나게 겹쳐 옛 이색 인쇄 같은 손그림으로 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-066"><img src="./assets/roster/066.jpg" alt="XXD Panel 066 · 천진한 서사의 선" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-066"><strong>066</strong> · 천진한 서사의 선</a><br><sub>사진 속 동작과 관계를 느슨한 검은 선과 부드러운 평면 채색으로 천진한 작은 이야기로 다시 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-067"><img src="./assets/roster/067.jpg" alt="XXD Panel 067 · 일상 유머 그림" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-067"><strong>067</strong> · 일상 유머 그림</a><br><sub>빨강과 파랑 두 가지 손그림 잉크만으로 사진 속 재미있는 순간을 사적인 관찰 노트 한 장으로 기록합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-068"><img src="./assets/roster/068.jpg" alt="XXD Panel 068 · 동양 사의(寫意) 화첩" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-068"><strong>068</strong> · 동양 사의(寫意) 화첩</a><br><sub>사의 먹선과 담채, 넓은 여백으로 사진을 동양의 시선으로 다시 그립니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-069"><img src="./assets/roster/069.jpg" alt="XXD Panel 069 · 선명한 붓칠 창" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-069"><strong>069</strong> · 선명한 붓칠 창</a><br><sub>굵은 붓 몇 번으로 그림 창을 칠하고, 사진 속 주인공이 선명한 색을 입고 그 밖으로 걸어 나오게 합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-070"><img src="./assets/roster/070.jpg" alt="XXD Panel 070 · 임파스토 힐링 섬" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-070"><strong>070</strong> · 임파스토 힐링 섬</a><br><sub>사진 속 주인공을 넓은 따뜻한 흰 바탕 위에 떠 있는 작고 밝은 섬처럼 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-071"><img src="./assets/roster/071.jpg" alt="XXD Panel 071 · 파스텔 시정 노트" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-071"><strong>071</strong> · 파스텔 시정 노트</a><br><sub>사진을 거의 흰 종이 위에 떠다니는 파스텔 기억 몇 조각으로 바꾸고, 느슨한 손글씨 시를 곁들입니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-072"><img src="./assets/roster/072.jpg" alt="XXD Panel 072 · 밝은 색채 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-072"><strong>072</strong> · 밝은 색채 저널</a><br><sub>사진을 어떤 곳은 선명하고 어떤 곳은 흐릿한 밝은 반투명 유리 기하로 추상화합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-073"><img src="./assets/roster/073.jpg" alt="XXD Panel 073 · 기하학 도시 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-073"><strong>073</strong> · 기하학 도시 저널</a><br><sub>사진을 비계로 둘러싸인 절단형 아이소메트릭 미니어처 건축 모형으로 다시 짓습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-074"><img src="./assets/roster/074.jpg" alt="XXD Panel 074 · 감정 아이콘 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-074"><strong>074</strong> · 감정 아이콘 저널</a><br><sub>사진의 주인공과 분위기를 정면에서 본, 무광의 입체감 있는 둥근 정사각형 아이콘 하나로 압축합니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-075"><img src="./assets/roster/075.jpg" alt="XXD Panel 075 · 어두운 크레용 스케치" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-075"><strong>075</strong> · 어두운 크레용 스케치</a><br><sub>사진에서 가장 기억할 만한 한 획을 미색 한지 위에 짙은 크레용으로 남깁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-076"><img src="./assets/roster/076.jpg" alt="XXD Panel 076 · 마카롱 크레용" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-076"><strong>076</strong> · 마카롱 크레용</a><br><sub>사진을 거친 짙은 크레용과 밝은 마카롱 색으로 사람 냄새 나는 여행의 기억으로 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-077"><img src="./assets/roster/077.jpg" alt="XXD Panel 077 · 여행 잡지 일러스트" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-077"><strong>077</strong> · 여행 잡지 일러스트</a><br><sub>사진을 종이 층과 부드러운 그림자, 영문 조판이 있는 종이 오리기 여행 잡지 한 장으로 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-078"><img src="./assets/roster/078.jpg" alt="XXD Panel 078 · 금박 압인 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-078"><strong>078</strong> · 금박 압인 저널</a><br><sub>사진의 핵심 윤곽을 가는 선으로 그려 샴페인 골드 금박으로 아이보리 코튼지에 깊이 눌러 넣습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-079"><img src="./assets/roster/079.jpg" alt="XXD Panel 079 · 펜 담채 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-079"><strong>079</strong> · 펜 담채 저널</a><br><sub>기하학적 직선과 자유로운 먹선, 몇 군데 담채로 사진을 현장에서 그리다 만 듯한 스케치로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-080"><img src="./assets/roster/080.jpg" alt="XXD Panel 080 · 유기적 과슈의 장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-080"><strong>080</strong> · 유기적 과슈의 장</a><br><sub>부드러운 유기적 형태와 식물색 과슈로 사진의 감정과 작은 은유 하나를 넓은 여백 속에 놓습니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-081"><img src="./assets/roster/081.jpg" alt="XXD Panel 081 · 색실 기념 앨범" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-081"><strong>081</strong> · 색실 기념 앨범</a><br><sub>사진 속 두세 가지에서 네 가지 색으로 굵기가 같은 선을 그어, 사진을 제한색으로 찍은 개인 기념 포스터로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-082"><img src="./assets/roster/082.jpg" alt="XXD Panel 082 · 종이를 뛰쳐나온 수채" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-082"><strong>082</strong> · 종이를 뛰쳐나온 수채</a><br><sub>사진 속 단 하나의 주인공이 불규칙한 수채 색면에서 천진한 입체가 되어 일어섭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-083"><img src="./assets/roster/083.jpg" alt="XXD Panel 083 · 못생기고 귀여운 캐릭터 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-083"><strong>083</strong> · 못생기고 귀여운 캐릭터 저널</a><br><sub>사진에서 주인공 하나만 남기고, 그 가장 웃긴 성격을 일부러 못생기고 서툴게, 하지만 한눈에 알아보게 그립니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-084"><img src="./assets/roster/084.jpg" alt="XXD Panel 084 · 점묘와 선 구성 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-084"><strong>084</strong> · 점묘와 선 구성 저널</a><br><sub>기하학적인 가는 선과 밀도가 다른 작은 점으로 사진을 조용한 도시 수필로 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-085"><img src="./assets/roster/085.jpg" alt="XXD Panel 085 · 수제 모형 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-085"><strong>085</strong> · 수제 모형 저널</a><br><sub>사진을 점토, 펠트, 오린 종이, 실로 만든 작은 수제 무대로 꾸며 넓은 여백 속에 놓습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-086"><img src="./assets/roster/086.jpg" alt="XXD Panel 086 · 여백의 판화 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-086"><strong>086</strong> · 여백의 판화 저널</a><br><sub>사진에서 핵심 정보 서너 개에서 다섯 개만 남겨, 여백이 먼저인 제한색 스크린 판화로 찍어 냅니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-087"><img src="./assets/roster/087.jpg" alt="XXD Panel 087 · 붉은 실 관계도" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-087"><strong>087</strong> · 붉은 실 관계도</a><br><sub>사진을 압정 하나하나로 나누고 주홍 실로 이어, 부분들의 관계가 보이는 지도로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-088"><img src="./assets/roster/088.jpg" alt="XXD Panel 088 · 문자 조형 시" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-088"><strong>088</strong> · 문자 조형 시</a><br><sub>글자와 문장부호, 점으로 사진 속 주인공을 짜 맞춥니다. 멀리서는 그림, 가까이서는 전부 글자입니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-089"><img src="./assets/roster/089.jpg" alt="XXD Panel 089 · 일상 소품 노트" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-089"><strong>089</strong> · 일상 소품 노트</a><br><sub>사진을 주인공 하나와 일상의 작은 조각 몇 개로 나눠, 여유로운 개인 다이어리 한 장으로 배치합니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-090"><img src="./assets/roster/090.jpg" alt="XXD Panel 090 · 시각적 사고 지도" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-090"><strong>090</strong> · 시각적 사고 지도</a><br><sub>사진 속 대상을 그리는 대신, 그 뒤에 있는 관계와 의미를 시각적 사고 지도로 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-091"><img src="./assets/roster/091.jpg" alt="XXD Panel 091 · 블루 라인 여행 앨범" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-091"><strong>091</strong> · 블루 라인 여행 앨범</a><br><sub>파란 펜 한 자루만으로, 충분히 보았으면 펜을 멈추는 여행 스케치로 사진을 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-092"><img src="./assets/roster/092.jpg" alt="XXD Panel 092 · 표현적 선묘 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-092"><strong>092</strong> · 표현적 선묘 저널</a><br><sub>사진을 느슨한 윤곽선과 겹친 해칭, 넓은 여백의 흑백 펜 드로잉으로 바꿉니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-093"><img src="./assets/roster/093.jpg" alt="XXD Panel 093 · 현대 기하 회화" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-093"><strong>093</strong> · 현대 기하 회화</a><br><sub>사진을 밝고 무광이며 가장자리에 손맛이 살짝 남은 모더니즘 기하 색면으로 압축합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-094"><img src="./assets/roster/094.jpg" alt="XXD Panel 094 · 고전 2색 책" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-094"><strong>094</strong> · 고전 2색 책</a><br><sub>사진을 가는 먹선과 별색 하나, 넓은 여백으로 된 옛 책 삽화로 바꿉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-095"><img src="./assets/roster/095.jpg" alt="XXD Panel 095 · 적흑 도해 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-095"><strong>095</strong> · 적흑 도해 저널</a><br><sub>검은 기술 선과 빨간 별색, 작은 도해 몇 장으로 사진 속 대상을 알기 쉽게 풀어냅니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-096"><img src="./assets/roster/096.jpg" alt="XXD Panel 096 · 민간 서신 카드" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-096"><strong>096</strong> · 민간 서신 카드</a><br><sub>사진을 정말로 타자 치고 복사해 부친 것 같은 옛 QSL 카드로 바꿉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-097"><img src="./assets/roster/097.jpg" alt="XXD Panel 097 · 레트로 설명 카드" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-097"><strong>097</strong> · 레트로 설명 카드</a><br><sub>사진을 쓸모 있고 조금 우스운, 옛 설명 카드 같은 2색 도해로 압축합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-098"><img src="./assets/roster/098.jpg" alt="XXD Panel 098 · 소박한 수채 책" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-098"><strong>098</strong> · 소박한 수채 책</a><br><sub>사진을 밝고 느슨하며 일부러 불완전한 그림책 한 페이지로 다시 들려줍니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-099"><img src="./assets/roster/099.jpg" alt="XXD Panel 099 · 서체 마스코트" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-099"><strong>099</strong> · 서체 마스코트</a><br><sub>사진의 주인공을 기억에 남는 마스코트로 디자인하고, 뒤에 초대형 글자 한 줄을 둡니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-100"><img src="./assets/roster/100.jpg" alt="XXD Panel 100 · 민예 서사화" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-100"><strong>100</strong> · 민예 서사화</a><br><sub>사진을 크레용 입자와 생활의 온기가 있는 소박한 민예 이야기로 바꿉니다.</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>101–150</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-101"><img src="./assets/roster/101.jpg" alt="XXD Panel 101 · 아홉 칸 기억 노트" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-101"><strong>101</strong> · 아홉 칸 기억 노트</a><br><sub>사진 한 장을 아홉 개의 작은 낙서로 나눠 나만의 다이어리 한 페이지처럼 배치합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-102"><img src="./assets/roster/102.jpg" alt="XXD Panel 102 · 치유 기하학 저널" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-102"><strong>102</strong> · 치유 기하학 저널</a><br><sub>사진을 맑고 고요하며 은은하게 생기 있는 기하 도형 하나로 정제합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-103"><img src="./assets/roster/103.jpg" alt="XXD Panel 103 · 선명한 추상 조합" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-103"><strong>103</strong> · 선명한 추상 조합</a><br><sub>사진을 선명한 큰 색면과 거친 손그림 선으로 나눠 추상화로 다시 조합합니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-104"><img src="./assets/roster/104.jpg" alt="XXD Panel 104 · 망점 선의 기록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-104"><strong>104</strong> · 망점 선의 기록</a><br><sub>사진을 망점으로 된 형태와 몇 줄의 색선, 고요한 여백으로 정제합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-105"><img src="./assets/roster/105.jpg" alt="XXD Panel 105 · 시적 여백집" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-105"><strong>105</strong> · 시적 여백집</a><br><sub>사진에서 가장 아름다운 한 장면만 골라 고요한 미니멀 종이 콜라주로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-106"><img src="./assets/roster/106.jpg" alt="XXD Panel 106 · 소프트 컬러 픽셀 기록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-106"><strong>106</strong> · 소프트 컬러 픽셀 기록</a><br><sub>사진을 두세 개의 핵심 형태만 남기고 깎아낸 뒤, 부드러운 파스텔 픽셀로 다시 기억합니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-107"><img src="./assets/roster/107.jpg" alt="XXD Panel 107 · 이미지 낱말 시" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-107"><strong>107</strong> · 이미지 낱말 시</a><br><sub>사진 속 꽃, 창, 길, 바람을 작은 그림으로 그려 문장의 낱말을 대신하게 하고, 읽을 수 있는 짧은 시로 엮습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-108"><img src="./assets/roster/108.jpg" alt="XXD Panel 108 · 신민예 종이 오리기 기록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-108"><strong>108</strong> · 신민예 종이 오리기 기록</a><br><sub>사진에서 가장 알아보기 쉬운 형태를 고요하고 민예 맛이 나는 색종이 콜라주로 오려 냅니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-109"><img src="./assets/roster/109.jpg" alt="XXD Panel 109 · 부드러운 기하 해체 기록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-109"><strong>109</strong> · 부드러운 기하 해체 기록</a><br><sub>사진을 몇 개의 크고 온전한 블록으로 나눈 뒤, 부드러운 색으로 알아보기 쉬운 모습을 다시 조립합니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-110"><img src="./assets/roster/110.jpg" alt="XXD Panel 110 · 일본풍 생활 장면 도감" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-110"><strong>110</strong> · 일본풍 생활 장면 도감</a><br><sub>사진 속 기억하고 싶은 작은 물건들을 동선과 여백이 있는 생활 지도로 정리합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-111"><img src="./assets/roster/111.jpg" alt="XXD Panel 111 · 텍스타일 콜라주 기록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-111"><strong>111</strong> · 텍스타일 콜라주 기록</a><br><sub>사진에서 가장 기억하고 싶은 관계를 따뜻한 작은 천 콜라주로 꿰매 냅니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-112"><img src="./assets/roster/112.jpg" alt="XXD Panel 112 · 금선 종이 기록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-112"><strong>112</strong> · 금선 종이 기록</a><br><sub>불규칙한 종이 색띠 하나가 금빛이 살짝 도는 작고 고요한 기억을 받쳐 줍니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-113"><img src="./assets/roster/113.jpg" alt="XXD Panel 113 · 조개껍데기 픽셀 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-113"><strong>113</strong> · 조개껍데기 픽셀 콜라주</a><br><sub>이백 개가 안 되는 조개껍데기 조각으로 사진의 주인공을 짓고, 가장자리부터 천천히 여백으로 흩어지게 합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-114"><img src="./assets/roster/114.jpg" alt="XXD Panel 114 · 레트로 파스텔 스크랩북 낙서" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-114"><strong>114</strong> · 레트로 파스텔 스크랩북 낙서</a><br><sub>사진을 종이가 숨 쉬는 듯한 파스텔 다이어리 낙서 콜라주로 다시 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-115"><img src="./assets/roster/115.jpg" alt="XXD Panel 115 · 파스텔 인장 콜라주 기록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-115"><strong>115</strong> · 파스텔 인장 콜라주 기록</a><br><sub>사진의 핵심 기억을 옛 종이 위 작은 파스텔 낙서 도장으로 그립니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-116"><img src="./assets/roster/116.jpg" alt="XXD Panel 116 · 옅은 종이 파스텔 낙서 기록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-116"><strong>116</strong> · 옅은 종이 파스텔 낙서 기록</a><br><sub>아주 옅은 종이 위에 입자가 굵은 색 크레용 선으로 사진의 또렷한 윤곽을 남깁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-117"><img src="./assets/roster/117.jpg" alt="XXD Panel 117 · 가는 선 담채 여백 기록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-117"><strong>117</strong> · 가는 선 담채 여백 기록</a><br><sub>사진에서 시각적 중심 하나를 골라, 가는 선과 옅은 채색으로 여백 많은 한 장을 다시 짭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-118"><img src="./assets/roster/118.jpg" alt="XXD Panel 118 · 흑연 여백 스케치 기록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-118"><strong>118</strong> · 흑연 여백 스케치 기록</a><br><sub>사진 속 기억할 만한 관계를 남기고, 연필과 여백으로 구도를 새로 짭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-119"><img src="./assets/roster/119.jpg" alt="XXD Panel 119 · 손바느질 직물과 여백 기록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-119"><strong>119</strong> · 손바느질 직물과 여백 기록</a><br><sub>천 몇 조각과 바늘땀에 사진 속 가장 따뜻한 기억을 담습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-120"><img src="./assets/roster/120.jpg" alt="XXD Panel 120 · 건축 개념 손그림 기록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-120"><strong>120</strong> · 건축 개념 손그림 기록</a><br><sub>사진 속 공간의 기억을 여백이 넉넉한 건축 개념 스케치로 바꿉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-121"><img src="./assets/roster/121.jpg" alt="XXD Panel 121 · 라이프스타일 두들 편집지" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-121"><strong>121</strong> · 라이프스타일 두들 편집지</a><br><sub>일상 사진 속 작은 감정을 여백이 넉넉하고 그림과 글이 영리하게 어우러진 생활 일러스트로 바꿉니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-122"><img src="./assets/roster/122.jpg" alt="XXD Panel 122 · 단색 하프톤 손글씨" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-122"><strong>122</strong> · 단색 하프톤 손글씨</a><br><sub>사진의 주인공을 검정·회색 망점으로 찍어 낸 작은 그림으로 바꾸고 빨간 손글씨 한 줄만 남깁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-123"><img src="./assets/roster/123.jpg" alt="XXD Panel 123 · 빨강·파랑 각진 색연필" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-123"><strong>123</strong> · 빨강·파랑 각진 색연필</a><br><sub>빨강과 파랑 색연필, 각진 선으로 사진의 주인공을 작고 긴장감 있는 손그림으로 다시 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-124"><img src="./assets/roster/124.jpg" alt="XXD Panel 124 · 천 콜라주의 여백" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-124"><strong>124</strong> · 천 콜라주의 여백</a><br><sub>큰 천 조각 몇 장과 바느질 몇 땀으로 사진의 주인공을 따뜻한 아플리케 그림으로 꾸밉니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-125"><img src="./assets/roster/125.jpg" alt="XXD Panel 125 · 소박한 크레용의 여백" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-125"><strong>125</strong> · 소박한 크레용의 여백</a><br><sub>서툰 크레용과 오일 파스텔로 사진의 주인공을 밝은 포인트 색 하나가 있는 그림책 속 작은 그림으로 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-126"><img src="./assets/roster/126.jpg" alt="XXD Panel 126 · 시적인 미니어처 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-126"><strong>126</strong> · 시적인 미니어처 콜라주</a><br><sub>사진을 우표만 한 수채·찢은 종이 콜라주로 줄여 넓은 수제 종이 여백 위에 놓습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-127"><img src="./assets/roster/127.jpg" alt="XXD Panel 127 · 혼합 매체 건축 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-127"><strong>127</strong> · 혼합 매체 건축 콜라주</a><br><sub>사진을 건축가의 연구 노트 같은 작은 콜라주로 만들고 구조선 몇 개와 손글씨 메모를 더합니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-128"><img src="./assets/roster/128.jpg" alt="XXD Panel 128 · 에나멜 메달 여행" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-128"><strong>128</strong> · 에나멜 메달 여행</a><br><sub>사진을 둥근 에나멜 기념 메달에 담고 우아한 세리프 글자 몇 줄을 더해 미니멀한 여행 포스터로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-129"><img src="./assets/roster/129.jpg" alt="XXD Panel 129 · 동양 확산 여백" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-129"><strong>129</strong> · 동양 확산 여백</a><br><sub>사진을 동양적인 실루엣 기호로 바꾸고 가장자리가 부드럽게 번지며 빛나는 큰 순색 도형을 곁들입니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-130"><img src="./assets/roster/130.jpg" alt="XXD Panel 130 · 하드에지 기하 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-130"><strong>130</strong> · 하드에지 기하 콜라주</a><br><sub>사진의 주인공을 검정·흰색·회색의 하드에지 기하 면으로 자르고 강한 포인트 색을 한두 개 넣습니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-131"><img src="./assets/roster/131.jpg" alt="XXD Panel 131 · 사진 낙서 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-131"><strong>131</strong> · 사진 낙서 콜라주</a><br><sub>사진을 작은 조각 묶음으로 오려 흰 종이에 붙이고, 거친 검은 테두리와 낙서 몇 개를 그려 넣습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-132"><img src="./assets/roster/132.jpg" alt="XXD Panel 132 · 펜 담채 여행" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-132"><strong>132</strong> · 펜 담채 여행</a><br><sub>손떨림이 남은 펜 선과 따뜻한 담채 몇 번으로 사진을 우표만 한 도시 스케치로 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-133"><img src="./assets/roster/133.jpg" alt="XXD Panel 133 · 점각 투명 겹침 인쇄" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-133"><strong>133</strong> · 점각 투명 겹침 인쇄</a><br><sub>같은 색의 반투명 형태를 여러 겹 겹쳐 찍어 사진의 주인공을 만들고, 겹칠수록 진해지며 가는 점각으로 입체를 냅니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-134"><img src="./assets/roster/134.jpg" alt="XXD Panel 134 · 그림책 색역 이야기" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-134"><strong>134</strong> · 그림책 색역 이야기</a><br><sub>위에는 넓은 여백, 가운데에는 작은 이야기 주인공, 아래에는 섞인 색면 한 판을 두어 그림책 한 장처럼 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-135"><img src="./assets/roster/135.jpg" alt="XXD Panel 135 · 스트리트 별색 손그림" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-135"><strong>135</strong> · 스트리트 별색 손그림</a><br><sub>거친 손그림 선, 부딪치는 별색 몇 가지, 인쇄 입자로 사진을 스트리트 진 포스터로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-136"><img src="./assets/roster/136.jpg" alt="XXD Panel 136 · 시적 초현실 여백" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-136"><strong>136</strong> · 시적 초현실 여백</a><br><sub>사진을 소박한 초현실주의 캔버스 소품으로 다시 쓰고, 엉뚱하지만 정확한 장면 관계 하나를 남깁니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-137"><img src="./assets/roster/137.jpg" alt="XXD Panel 137 · 에칭 질감 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-137"><strong>137</strong> · 에칭 질감 콜라주</a><br><sub>가는 에칭 선으로 아주 작은 주인공을 그리고 거친 인쇄 색면을 한두 장 겹칩니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-138"><img src="./assets/roster/138.jpg" alt="XXD Panel 138 · 동양 종이 부조" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-138"><strong>138</strong> · 동양 종이 부조</a><br><sub>수제 면지를 접고 돋을새김하고 잘라 겹쳐서, 사진을 흰 종이 위의 작은 얕은 부조로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-139"><img src="./assets/roster/139.jpg" alt="XXD Panel 139 · 문자 인코딩 선장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-139"><strong>139</strong> · 문자 인코딩 선장</a><br><sub>사진을 아주 가는 가로세로 선의 작은 선장으로 인코딩합니다. 멀리서는 추상 구조, 가까이서야 원래 모습이 어렴풋이 보입니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-140"><img src="./assets/roster/140.jpg" alt="XXD Panel 140 · 건식 손그림 시각 섬" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-140"><strong>140</strong> · 건식 손그림 시각 섬</a><br><sub>사진을 흰 종이 한가운데의 작은 과슈·오일 파스텔 그림으로 압축해, 소중히 간직한 기억처럼 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-141"><img src="./assets/roster/141.jpg" alt="XXD Panel 141 · 미니멀 손그림 선묘" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-141"><strong>141</strong> · 미니멀 손그림 선묘</a><br><sub>가늘고 살짝 떨리는 손그림 선 몇 개로 사진의 주인공을 그리고 주변은 거의 여백으로 둡니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-142"><img src="./assets/roster/142.jpg" alt="XXD Panel 142 · 확장 글자–이미지 마스크" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-142"><strong>142</strong> · 확장 글자–이미지 마스크</a><br><sub>사진에서 단어 하나를 뽑아 길게 늘인 글자 안에 주인공을 넣어 글자와 이미지를 하나로 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-143"><img src="./assets/roster/143.jpg" alt="XXD Panel 143 · 문자 조형 시각시" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-143"><strong>143</strong> · 문자 조형 시각시</a><br><sub>사진에서 길어 올린 글자로 주인공의 윤곽과 명암을 쌓아 올립니다. 멀리서는 그림, 가까이서는 모두 글자입니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-144"><img src="./assets/roster/144.jpg" alt="XXD Panel 144 · 기하 백색 반전 선묘" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-144"><strong>144</strong> · 기하 백색 반전 선묘</a><br><sub>가는 선묘와 기하 색면 하나로 사진의 주인공을 다시 그리고, 색면 안에서는 흰색으로 반전, 밖에서는 선으로 돌아옵니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-145"><img src="./assets/roster/145.jpg" alt="XXD Panel 145 · 빈티지 제한색 판화" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-145"><strong>145</strong> · 빈티지 제한색 판화</a><br><sub>판각풍 해칭, 점묘, 망점으로 사진을 별색 몇 가지로 겹쳐 찍은 빈티지 소경으로 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-146"><img src="./assets/roster/146.jpg" alt="XXD Panel 146 · 박물학 스카프 삽화" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-146"><strong>146</strong> · 박물학 스카프 삽화</a><br><sub>섬세한 판각 선과 밝은 평면 색 몇 가지로 사진의 주인공을 스카프 프린트 같은 박물학 문양으로 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-147"><img src="./assets/roster/147.jpg" alt="XXD Panel 147 · 도시락 식재료 패키징" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-147"><strong>147</strong> · 도시락 식재료 패키징</a><br><sub>사진 속 모든 것을 식재료로 바꿔 투명한 편의점 반찬 용기에 담고 위에서 찍은 상품 사진으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-148"><img src="./assets/roster/148.jpg" alt="XXD Panel 148 · 시각 일기 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-148"><strong>148</strong> · 시각 일기 콜라주</a><br><sub>사진 조각, 메모지, 테이프, 영수증, 손글씨로 사진을 여백 넉넉한 개인 일기 한 장으로 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-149"><img src="./assets/roster/149.jpg" alt="XXD Panel 149 · 손그림 질감 플랫 아트" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-149"><strong>149</strong> · 손그림 질감 플랫 아트</a><br><sub>종이 결과 파스텔 질감이 있는 큰 색면으로 종이 오려 붙이기처럼 사진의 주인공을 다시 짜 맞춥니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-150"><img src="./assets/roster/150.jpg" alt="XXD Panel 150 · 레트로 모던 페이퍼 컷" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-150"><strong>150</strong> · 레트로 모던 페이퍼 컷</a><br><sub>색종이로 오린 실루엣과 기하·유기적 형태로 사진을 미드센추리 모던풍의 작은 종이 오리기 그림으로 만듭니다.</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>151–200</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-151"><img src="./assets/roster/151.jpg" alt="XXD Panel 151 · 소박한 플랫 손그림" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-151"><strong>151</strong> · 소박한 플랫 손그림</a><br><sub>평면 색면과 삐뚤빼뚤한 손그림 선으로 사진에서 가장 개성 있는 부분만 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-152"><img src="./assets/roster/152.jpg" alt="XXD Panel 152 · 색면 바탕 페이퍼 아트" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-152"><strong>152</strong> · 색면 바탕 페이퍼 아트</a><br><sub>사진 속 주인공을 종이 몇 장으로 오려 아래를 가로지르는 단색 띠 위에 붙입니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-153"><img src="./assets/roster/153.jpg" alt="XXD Panel 153 · 단색 다이어리 두들" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-153"><strong>153</strong> · 단색 다이어리 두들</a><br><sub>모눈종이 위에 초록 수성펜 하나로 사진 속 주인공을 쓱 그린 듯한 그림입니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-154"><img src="./assets/roster/154.jpg" alt="XXD Panel 154 · 레트로 픽셀 여백" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-154"><strong>154</strong> · 레트로 픽셀 여백</a><br><sub>사진 속 주인공을 16비트 풍 레트로 픽셀 그림으로 만들어 넓은 여백에 둡니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-155"><img src="./assets/roster/155.jpg" alt="XXD Panel 155 · 1점 투시 담채" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-155"><strong>155</strong> · 1점 투시 담채</a><br><sub>사진을 1점 투시 펜 선화로 그리고 아주 옅은 수채를 살짝 입힙니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-156"><img src="./assets/roster/156.jpg" alt="XXD Panel 156 · 두 별색 판맞춤 어긋남 삽화" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-156"><strong>156</strong> · 두 별색 판맞춤 어긋남 삽화</a><br><sub>사진 속 주인공을 잉크 두 가지만으로, 판이 살짝 어긋난 리소그래프 풍 작은 삽화로 찍어 냅니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-157"><img src="./assets/roster/157.jpg" alt="XXD Panel 157 · 유물 먹 탁본과 여백" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-157"><strong>157</strong> · 유물 먹 탁본과 여백</a><br><sub>사진 속 주인공을 얼룩지고 이지러진 옛 석각 탁본으로 바꿔 넓은 종이 위에 조용히 둡니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-158"><img src="./assets/roster/158.jpg" alt="XXD Panel 158 · 종이 혼합 재료 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-158"><strong>158</strong> · 종이 혼합 재료 콜라주</a><br><sub>찢은 책장, 신문 조각, 느슨한 연필선으로 사진 속 주인공을 작은 종이 작품으로 엮습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-159"><img src="./assets/roster/159.jpg" alt="XXD Panel 159 · 문자 망점 실험 포스터" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-159"><strong>159</strong> · 문자 망점 실험 포스터</a><br><sub>문자, 도트, 망점으로 사진 속 주인공을 다시 쌓고, 그림과 맞물린 비트맵 제목을 붙입니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-160"><img src="./assets/roster/160.jpg" alt="XXD Panel 160 · 느슨한 펜선과 담채 여백" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-160"><strong>160</strong> · 느슨한 펜선과 담채 여백</a><br><sub>느슨한 스케치 먹선과 투명 수채 몇 붓으로 사진 속 주인공을 작은 펜 담채화로 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-161"><img src="./assets/roster/161.jpg" alt="XXD Panel 161 · 회화적 색면과 경계 넘기" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-161"><strong>161</strong> · 회화적 색면과 경계 넘기</a><br><sub>흰 종이 한가운데 손으로 칠한 색면을 두 번째 캔버스처럼 두고, 주인공이 그 경계 밖으로 살짝 나옵니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-162"><img src="./assets/roster/162.jpg" alt="XXD Panel 162 · 흰 오려낸 종이 받침의 그림책" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-162"><strong>162</strong> · 흰 오려낸 종이 받침의 그림책</a><br><sub>사진 속 주인공을 크레용 질감의 천진한 그림책 그림으로 그리고, 손으로 오린 흰 종이를 받칩니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-163"><img src="./assets/roster/163.jpg" alt="XXD Panel 163 · 중앙 단색 면 스탬프 구도" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-163"><strong>163</strong> · 중앙 단색 면 스탬프 구도</a><br><sub>깔끔한 단색 면 몇 개로 사진 속 주인공을 화면 정중앙의 작은 도장으로 압축합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-164"><img src="./assets/roster/164.jpg" alt="XXD Panel 164 · 수묵 건축 선묘 미니어처" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-164"><strong>164</strong> · 수묵 건축 선묘 미니어처</a><br><sub>사진을 옅은 수묵 산수 속 작은 건축 풍경으로 바꾸고, 건축가의 스케치 같은 선에 주황 한 점을 찍습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-165"><img src="./assets/roster/165.jpg" alt="XXD Panel 165 · 중앙 찢긴 틈의 종이 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-165"><strong>165</strong> · 중앙 찢긴 틈의 종이 콜라주</a><br><sub>연한 종이 한가운데를 세로로 찢고, 그 틈으로 사진 속 주인공이 기하학적 색면으로 드러납니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-166"><img src="./assets/roster/166.jpg" alt="XXD Panel 166 · 등각 투영 조각적 부조 디오라마" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-166"><strong>166</strong> · 등각 투영 조각적 부조 디오라마</a><br><sub>사진 속 주인공을 등각 투영 미니어처 모형으로 만들어, 얕은 부조처럼 층층이 떠오르게 합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-167"><img src="./assets/roster/167.jpg" alt="XXD Panel 167 · 중앙 파형과 두꺼운 잉크 부조" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-167"><strong>167</strong> · 중앙 파형과 두꺼운 잉크 부조</a><br><sub>사진 속 주인공을 가운데 추상적인 파도 위에 올리고, 두껍게 올린 잉크로 찍은 부조처럼 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-168"><img src="./assets/roster/168.jpg" alt="XXD Panel 168 · 종이 흰색을 남긴 겹붓질 색면" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-168"><strong>168</strong> · 종이 흰색을 남긴 겹붓질 색면</a><br><sub>흰 종이에 따뜻한 색면을 겹겹이 칠하고, 사진 속 주인공은 칠할 때 남겨 둔 종이의 흰 부분이 됩니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-169"><img src="./assets/roster/169.jpg" alt="XXD Panel 169 · 따뜻한 황토색 작은 잉크 삽화" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-169"><strong>169</strong> · 따뜻한 황토색 작은 잉크 삽화</a><br><sub>느슨한 숯검정 먹선과 황토색 담채로 사진 속 주인공을 작은 독립 삽화로 그리고, 핵심을 그리면 붓을 멈춥니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-170"><img src="./assets/roster/170.jpg" alt="XXD Panel 170 · 검정과 녹슨 빨강의 거친 작은 삽화" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-170"><strong>170</strong> · 검정과 녹슨 빨강의 거친 작은 삽화</a><br><sub>숯검정과 약간의 녹슨 빨강만으로, 거친 크레용 몇 획에 사진 속 주인공을 아주 작은 삽화로 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-171"><img src="./assets/roster/171.jpg" alt="XXD Panel 171 · 세로 골격과 작은 분산 장면" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-171"><strong>171</strong> · 세로 골격과 작은 분산 장면</a><br><sub>넓은 따뜻한 흰 바탕에 가늘고 옅은 세로선 몇 개를 세우고, 사진 속 사람과 물건을 작은 섬처럼 흩어 둡니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-172"><img src="./assets/roster/172.jpg" alt="XXD Panel 172 · 중앙 피사체와 반투명 기하 레이어" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-172"><strong>172</strong> · 중앙 피사체와 반투명 기하 레이어</a><br><sub>사진 속 주인공을 화면 정중앙에 작게 두고, 그 뒤에 옅은 반투명 기하 색 조각 몇 개를 띄웁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-173"><img src="./assets/roster/173.jpg" alt="XXD Panel 173 · 상아색 종이와 문자 미니 풍경" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-173"><strong>173</strong> · 상아색 종이와 문자 미니 풍경</a><br><sub>사진을 오래된 책장과 글자로 쌓은 작은 종이 풍경으로 줄여, 넓은 따뜻한 흰 바탕에 띄웁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-174"><img src="./assets/roster/174.jpg" alt="XXD Panel 174 · 투박한 손그림 스티커 집합" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-174"><strong>174</strong> · 투박한 손그림 스티커 집합</a><br><sub>사진 속 주인공을 굵은 붓의 손그림 스티커 여러 장으로 나눈 뒤, 화면 가운데에 다시 하나로 모읍니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-175"><img src="./assets/roster/175.jpg" alt="XXD Panel 175 · 호박빛 역광의 상아색 종이 조각" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-175"><strong>175</strong> · 호박빛 역광의 상아색 종이 조각</a><br><sub>사진을 겹겹이 쌓은 작은 상아색 종이 조각으로 만들고, 종이층 사이로 따뜻한 호박빛이 새어 나오게 합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-176"><img src="./assets/roster/176.jpg" alt="XXD Panel 176 · 정교한 손그림 의식 도형 부조" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-176"><strong>176</strong> · 정교한 손그림 의식 도형 부조</a><br><sub>사진 속 주인공을 공필 세선으로 그린 정교한 진법 도형의 중심에 앉히고, 층층이 띄우며 바깥으로 성기게 펼칩니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-177"><img src="./assets/roster/177.jpg" alt="XXD Panel 177 · 이형 실루엣 판화 미니 섬" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-177"><strong>177</strong> · 이형 실루엣 판화 미니 섬</a><br><sub>사진의 핵심을 작은 이형 판화 섬 하나에 눌러 담고, 먹감색, 회올리브, 주홍 한 점으로 새깁니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-178"><img src="./assets/roster/178.jpg" alt="XXD Panel 178 · 수첩 먹기록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-178"><strong>178</strong> · 수첩 먹기록</a><br><sub>사진을 낡은 잉크로 쓱 그린 작은 표시 하나로 줄입니다. 오래된 다이어리 귀퉁이의 한 획처럼.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-179"><img src="./assets/roster/179.jpg" alt="XXD Panel 179 · 리본형 미니어처 전시 풍경" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-179"><strong>179</strong> · 리본형 미니어처 전시 풍경</a><br><sub>사진의 핵심을 미니어처 전시품 몇 점으로 만들어, 떠 있는 상아색 리본 위에 드문드문 진열합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-180"><img src="./assets/roster/180.jpg" alt="XXD Panel 180 · 빈티지 원형 여행 기념 스탬프" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-180"><strong>180</strong> · 빈티지 원형 여행 기념 스탬프</a><br><sub>사진 속 주인공과 주변 단서 한두 가지를 낡은 상아색 종이 위 둥근 빈티지 기념 스탬프로 새깁니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-181"><img src="./assets/roster/181.jpg" alt="XXD Panel 181 · 문인 수묵담채 소품" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-181"><strong>181</strong> · 문인 수묵담채 소품</a><br><sub>먹을 뼈대로, 옅은 색을 곁들여 사진을 여백 많은 작은 문인화 소품으로 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-182"><img src="./assets/roster/182.jpg" alt="XXD Panel 182 · 미니어처 픽셀 그래픽" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-182"><strong>182</strong> · 미니어처 픽셀 그래픽</a><br><sub>사진의 주인공을 경계가 또렷한 작은 픽셀 그래픽으로 줄여 넓은 여백에 조용히 놓습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-183"><img src="./assets/roster/183.jpg" alt="XXD Panel 183 · 짙은 녹색 모서리 유기 그래픽" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-183"><strong>183</strong> · 짙은 녹색 모서리 유기 그래픽</a><br><sub>사진의 주인공을 한쪽 모서리의 작은 자연 형태로 모으고, 크림색 바탕을 짙은 녹색으로 눌러 줍니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-184"><img src="./assets/roster/184.jpg" alt="XXD Panel 184 · 정사각형 일상 손그림 소품" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-184"><strong>184</strong> · 정사각형 일상 손그림 소품</a><br><sub>사진 속 생활의 디테일을 작은 정사각형 장면에 담아 느슨한 선과 색연필, 수채로 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-185"><img src="./assets/roster/185.jpg" alt="XXD Panel 185 · 옅은 강조색의 흑백 스티커 소품" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-185"><strong>185</strong> · 옅은 강조색의 흑백 스티커 소품</a><br><sub>사진의 주인공을 옅은 색 한 점만 더한 작은 흑백 손그림 스티커 그래픽으로 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-186"><img src="./assets/roster/186.jpg" alt="XXD Panel 186 · 부드러운 색의 아홉 칸 기하학 기억" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-186"><strong>186</strong> · 부드러운 색의 아홉 칸 기하학 기억</a><br><sub>사진을 아홉 개의 기억 조각으로 나눠 부드러운 평면 기하 색면으로 3×3 격자에 배열합니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-187"><img src="./assets/roster/187.jpg" alt="XXD Panel 187 · 대형 타이포 아카이브 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-187"><strong>187</strong> · 대형 타이포 아카이브 콜라주</a><br><sub>사진의 주인공을 사진 조각과 제도선의 아카이브 콜라주로 만들고 뒤에 거대한 글자를 깝니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-188"><img src="./assets/roster/188.jpg" alt="XXD Panel 188 · 베이지와 금빛 건축 아카이브" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-188"><strong>188</strong> · 베이지와 금빛 건축 아카이브</a><br><sub>사진의 주인공을 작은 건축 표본처럼 줄여 오래된 종이색 여백에 두고 샌드 골드 제목을 붙입니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-189"><img src="./assets/roster/189.jpg" alt="XXD Panel 189 · 이중 프레임과 사이드바 성냥갑 소품" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-189"><strong>189</strong> · 이중 프레임과 사이드바 성냥갑 소품</a><br><sub>사진을 옛 성냥갑 라벨 속 작은 삽화로 그리고 이중 테두리와 좁은 사이드바로 감쌉니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-190"><img src="./assets/roster/190.jpg" alt="XXD Panel 190 · 차가운 파스텔과 따뜻한 강조색" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-190"><strong>190</strong> · 차가운 파스텔과 따뜻한 강조색</a><br><sub>사진을 차가운 회색조의 작은 소박한 파스텔 그림으로 그리고 따뜻한 색을 한 점만 더합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-191"><img src="./assets/roster/191.jpg" alt="XXD Panel 191 · 부드러운 사각 파스텔 색면" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-191"><strong>191</strong> · 부드러운 사각 파스텔 색면</a><br><sub>사진을 가장자리가 보풀처럼 풀린 작은 사각 파스텔 색면에 그려 넓은 여백에 띄웁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-192"><img src="./assets/roster/192.jpg" alt="XXD Panel 192 · 제한된 색의 빈티지 그래픽 소품" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-192"><strong>192</strong> · 제한된 색의 빈티지 그래픽 소품</a><br><sub>사진을 실루엣과 색면의 작은 그래픽으로 줄여 두 가지에서 네 가지 빈티지 색으로 종이에 찍어 냅니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-193"><img src="./assets/roster/193.jpg" alt="XXD Panel 193 · 낮은 받침 위 차분한 수채 소품" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-193"><strong>193</strong> · 낮은 받침 위 차분한 수채 소품</a><br><sub>사진을 옅은 낮은 받침 위에 놓인 차분한 수채 소형체로 그리고 둘레에 종이 여백을 넓게 남깁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-194"><img src="./assets/roster/194.jpg" alt="XXD Panel 194 · 밝은 대지 받침 축측 모형" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-194"><strong>194</strong> · 밝은 대지 받침 축측 모형</a><br><sub>사진의 주인공을 평평한 대지 받침에서 솟아오른 밝은 색의 축측 블록 모형으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-195"><img src="./assets/roster/195.jpg" alt="XXD Panel 195 · 하나의 밝은 강조색을 둔 역사 몽타주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-195"><strong>195</strong> · 하나의 밝은 강조색을 둔 역사 몽타주</a><br><sub>사진을 흑백과 따뜻한 회색의 아카이브 사진 몽타주로 다시 엮고, 원본의 밝은 색 하나만 남깁니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-196"><img src="./assets/roster/196.jpg" alt="XXD Panel 196 · 탑뷰 기하학 인물 소품" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-196"><strong>196</strong> · 탑뷰 기하학 인물 소품</a><br><sub>사진 속 사람들을 바로 위에서 내려다보며 원과 캡슐 모양으로 된 평면 기하 인물로 다시 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-197"><img src="./assets/roster/197.jpg" alt="XXD Panel 197 · 새장 속 세계 민예 일러스트" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-197"><strong>197</strong> · 새장 속 세계 민예 일러스트</a><br><sub>사진의 주제를 새장 안에 담아 평면적이고 따뜻한 신민예 손그림으로 작은 세계를 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-198"><img src="./assets/roster/198.jpg" alt="XXD Panel 198 · 제한 팔레트 부유 패션 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-198"><strong>198</strong> · 제한 팔레트 부유 패션 콜라주</a><br><sub>사진의 주인공을 무중력으로 떠다니는 개념 패션 일러스트로 그려 콜라주, 망점, 제한된 색으로 찍어 냅니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-199"><img src="./assets/roster/199.jpg" alt="XXD Panel 199 · 밝고 여백이 넓은 미니 패션 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-199"><strong>199</strong> · 밝고 여백이 넓은 미니 패션 콜라주</a><br><sub>사진의 주인공을 떠다니는 작은 패션 일러스트 형상 몇 개로 줄여 밝고 따뜻한 흰 여백에 놓습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-200"><img src="./assets/roster/200.jpg" alt="XXD Panel 200 · 청회색 단색 손그림 선화" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-200"><strong>200</strong> · 청회색 단색 손그림 선화</a><br><sub>청회색 한 가지 색의 느슨한 선으로 사진을 스케치 흔적이 남은 작은 선화로 그립니다.</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>201–250</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-201"><img src="./assets/roster/201.jpg" alt="XXD Panel 201 · 크림색 수공예 미니어처" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-201"><strong>201</strong> · 크림색 수공예 미니어처</a><br><sub>사진의 주인공을 크림색 수공예 미니어처 장식품으로 만들어 넓은 여백에 조용히 놓습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-202"><img src="./assets/roster/202.jpg" alt="XXD Panel 202 · 구조 축을 가진 기하학 선도" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-202"><strong>202</strong> · 구조 축을 가진 기하학 선도</a><br><sub>사진에서 몇 개의 구조선을 뽑아내고 주인공을 그 선에 걸린 청회색 기하 선도로 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-203"><img src="./assets/roster/203.jpg" alt="XXD Panel 203 · 여백을 살린 임파스토 엽서" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-203"><strong>203</strong> · 여백을 살린 임파스토 엽서</a><br><sub>사진을 두껍게 칠한 유화 소품으로 그려 넓은 여백에 두고, 아트 엽서처럼 꾸밉니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-204"><img src="./assets/roster/204.jpg" alt="XXD Panel 204 · 부드러운 빛과 기억 소품" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-204"><strong>204</strong> · 부드러운 빛과 기억 소품</a><br><sub>사진의 주인공을 소프트 포커스 빛과 흐린 실루엣의 작은 덩어리로 바꿔, 빛이 남긴 기억처럼 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-205"><img src="./assets/roster/205.jpg" alt="XXD Panel 205 · 따뜻한 유기형 사진 선화 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-205"><strong>205</strong> · 따뜻한 유기형 사진 선화 콜라주</a><br><sub>사진을 둥근 유기형으로 잘라 가는 손그림 선을 겹치고, 따뜻한 색에 테라코타 한 점을 더합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-206"><img src="./assets/roster/206.jpg" alt="XXD Panel 206 · 부드러운 색의 겹종이 미니 풍경" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-206"><strong>206</strong> · 부드러운 색의 겹종이 미니 풍경</a><br><sub>사진의 주인공을 겹겹이 쌓은 종이로 만든 얕은 부조 풍경으로 만들고, 부드러운 종이색과 넓은 여백으로 마무리합니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-207"><img src="./assets/roster/207.jpg" alt="XXD Panel 207 · 연한 청백색 혼합 매체 삽화" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-207"><strong>207</strong> · 연한 청백색 혼합 매체 삽화</a><br><sub>사진을 가운데에 놓인 작은 사진과 선화의 콜라주로 만들어 연한 파랑과 흰 바탕의 잡지 삽지처럼 꾸밉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-208"><img src="./assets/roster/208.jpg" alt="XXD Panel 208 · 파랑 분홍 모더니즘 추상" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-208"><strong>208</strong> · 파랑 분홍 모더니즘 추상</a><br><sub>사진을 파랑과 분홍 색면, 검은 선 질감으로 된 작은 모더니즘 추상 그래픽으로 정리합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-209"><img src="./assets/roster/209.jpg" alt="XXD Panel 209 · 종이 질감의 미니멀 이미지 아카이브" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-209"><strong>209</strong> · 종이 질감의 미니멀 이미지 아카이브</a><br><sub>사진을 종이 위의 작은 이미지로 줄이고 아카이브식 작은 글자를 더해, 정성껏 보관한 사진집의 한 페이지처럼 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-210"><img src="./assets/roster/210.jpg" alt="XXD Panel 210 · 차가운 색의 가벼운 개념 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-210"><strong>210</strong> · 차가운 색의 가벼운 개념 콜라주</a><br><sub>사진의 주인공을 작은 사진 콜라주 조각으로 줄이고, 차가운 파랑의 손그림 선과 작은 말풍선, 기호를 더합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-211"><img src="./assets/roster/211.jpg" alt="XXD Panel 211 · 의미 기반 배색 기하학 소품" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-211"><strong>211</strong> · 의미 기반 배색 기하학 소품</a><br><sub>사진을 기하 색면의 작은 그래픽으로 줄이고, 색은 주인공의 정체, 재질, 계절에 맞춰 고릅니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-212"><img src="./assets/roster/212.jpg" alt="XXD Panel 212 · 준단색 조각적 형태 연구" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-212"><strong>212</strong> · 준단색 조각적 형태 연구</a><br><sub>사진의 주인공을 넓은 빈 공간에 놓인 작은 흰색 개념 모형으로 바꿉니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-213"><img src="./assets/roster/213.jpg" alt="XXD Panel 213 · 따뜻한 종이 위 차가운 단색 개념화" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-213"><strong>213</strong> · 따뜻한 종이 위 차가운 단색 개념화</a><br><sub>사진 속 감정과 관계를 따뜻한 옛 종이 위 차가운 단색 선의 작은 시적 그림으로 거둡니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-214"><img src="./assets/roster/214.jpg" alt="XXD Panel 214 · 고유색을 살린 거친 오려내기 소품" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-214"><strong>214</strong> · 고유색을 살린 거친 오려내기 소품</a><br><sub>사진을 넓은 흰 종이 위, 실제 색을 살린 거친 종이 오리기 작은 일러스트로 바꿉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-215"><img src="./assets/roster/215.jpg" alt="XXD Panel 215 · 황토색 강조가 있는 회색조 축측도" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-215"><strong>215</strong> · 황토색 강조가 있는 회색조 축측도</a><br><sub>사진의 주인공을 황토색 하나만 더한 흰색과 회색의 정밀한 축측 도해 소품으로 그립니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-216"><img src="./assets/roster/216.jpg" alt="XXD Panel 216 · 거대한 여백 속 극소 인쇄 섬" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-216"><strong>216</strong> · 거대한 여백 속 극소 인쇄 섬</a><br><sub>사진을 넓은 따뜻한 종이 위의 아주 작은 단색 인쇄 블록으로 압축합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-217"><img src="./assets/roster/217.jpg" alt="XXD Panel 217 · 밝은 디지털 혼합 매체 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-217"><strong>217</strong> · 밝은 디지털 혼합 매체 콜라주</a><br><sub>사진의 주인공을 오려내 손그림 낙서와 종이 조각을 더해 밝은 잡지풍 콜라주로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-218"><img src="./assets/roster/218.jpg" alt="XXD Panel 218 · 미니멀 그림책 양모 펠트 일러스트" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-218"><strong>218</strong> · 미니멀 그림책 양모 펠트 일러스트</a><br><sub>사진을 아주 간결한 그림책 한 장면으로 정리한 뒤 부드러운 수제 양모 펠트로 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-219"><img src="./assets/roster/219.jpg" alt="XXD Panel 219 · 색연필 포인트 여행 스케치" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-219"><strong>219</strong> · 색연필 포인트 여행 스케치</a><br><sub>사진을 여행 다이어리 속 검은 펜 스케치로 그리고 색연필로 몇 군데만 색을 더합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-220"><img src="./assets/roster/220.jpg" alt="XXD Panel 220 · 둥글고 소박한 손그림 두들" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-220"><strong>220</strong> · 둥글고 소박한 손그림 두들</a><br><sub>사진을 둥글고 느슨한 선에 군데군데만 색을 더한 귀여운 손그림 두들로 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-221"><img src="./assets/roster/221.jpg" alt="XXD Panel 221 · 신중식 별색 판화와 여백" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-221"><strong>221</strong> · 신중식 별색 판화와 여백</a><br><sub>사진을 낙관처럼 작은 신중식 별색 판화로 거두고, 주변에 동양적인 여백을 넓게 둡니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-222"><img src="./assets/roster/222.jpg" alt="XXD Panel 222 · 건축적 타이포그래피 설치물" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-222"><strong>222</strong> · 건축적 타이포그래피 설치물</a><br><sub>사진의 주인공을 글자와 기하 블록으로 쌓아 올린 작고 다채로운 랜드마크로 바꿉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-223"><img src="./assets/roster/223.jpg" alt="XXD Panel 223 · 레트로 판화 미니 도감" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-223"><strong>223</strong> · 레트로 판화 미니 도감</a><br><sub>사진을 서로 이어지지 않는 작은 판화 그림 여러 개로 나누어 옛 도감의 한 페이지처럼 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-224"><img src="./assets/roster/224.jpg" alt="XXD Panel 224 · 도자기 파편 재구성" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-224"><strong>224</strong> · 도자기 파편 재구성</a><br><sub>사진의 주인공을 중국 도자기 파편으로 다시 맞추고, 틈과 금, 넓은 자기 흰색을 남깁니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-225"><img src="./assets/roster/225.jpg" alt="XXD Panel 225 · 사무용품 손그림 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-225"><strong>225</strong> · 사무용품 손그림 콜라주</a><br><sub>메모지, 클립, 테이프, 종이 조각으로 사진을 한 페이지의 시각 일기로 다시 씁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-226"><img src="./assets/roster/226.jpg" alt="XXD Panel 226 · 아이싱 쿠키 얕은 부조" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-226"><strong>226</strong> · 아이싱 쿠키 얕은 부조</a><br><sub>사진의 주인공과 장면을 함께 무광의 둥근 아이싱 쿠키 작은 부조로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-227"><img src="./assets/roster/227.jpg" alt="XXD Panel 227 · 자수 미션 패치" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-227"><strong>227</strong> · 자수 미션 패치</a><br><sub>사진을 오버록 테두리와 새틴 자수 글자, 짧은 번호가 있는 기계 자수 미션 패치 한 장으로 압축합니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-228"><img src="./assets/roster/228.jpg" alt="XXD Panel 228 · 작가가 만든 종이 오브제" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-228"><strong>228</strong> · 작가가 만든 종이 오브제</a><br><sub>사진을 독립 서점에서 볼 법한 손수 만든 종이 작품으로 다시 만듭니다. 서툰 종이 오리기와 몇 가지 별색.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-229"><img src="./assets/roster/229.jpg" alt="XXD Panel 229 · 신민예 여백" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-229"><strong>229</strong> · 신민예 여백</a><br><sub>사진의 영혼을 둥글고 파스텔빛인, 조용하고 향수 어린 신민예 작은 삽화로 담습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-230"><img src="./assets/roster/230.jpg" alt="XXD Panel 230 · 네거티브 스페이스 기념비" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-230"><strong>230</strong> · 네거티브 스페이스 기념비</a><br><sub>촘촘한 손그림 짧은 선 속에 주인공을 거대한 흰 음형으로 남기고, 옆에 아주 작은 인물 하나만 둡니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-231"><img src="./assets/roster/231.jpg" alt="XXD Panel 231 · 네오 나이브 손그림" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-231"><strong>231</strong> · 네오 나이브 손그림</a><br><sub>사진을 흔들리는 색선, 마커, 색연필로 그린 작고 느슨한 손그림으로 담고 여백을 넉넉히 둡니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-232"><img src="./assets/roster/232.jpg" alt="XXD Panel 232 · 가로 층의 민예 풍경" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-232"><strong>232</strong> · 가로 층의 민예 풍경</a><br><sub>사진을 조용히 옆으로 펼쳐지는 띠 모양 풍경으로 압축합니다. 사람은 아주 작은 문장 부호일 뿐입니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-233"><img src="./assets/roster/233.jpg" alt="XXD Panel 233 · 터프팅 섬유 벽장식" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-233"><strong>233</strong> · 터프팅 섬유 벽장식</a><br><sub>사진을 옅은 단색 바탕 위에 흩어진 밝은 루프 파일 실 벽장식 몇 점으로 다시 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-234"><img src="./assets/roster/234.jpg" alt="XXD Panel 234 · 디지털 에디토리얼 키 비주얼" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-234"><strong>234</strong> · 디지털 에디토리얼 키 비주얼</a><br><sub>사진을 평평한 색면, 둥근 모듈, 가는 선, 넓은 여백으로 이루어진 젊은 키 비주얼로 담습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-235"><img src="./assets/roster/235.jpg" alt="XXD Panel 235 · 민트 픽셀 요리" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-235"><strong>235</strong> · 민트 픽셀 요리</a><br><sub>사진을 민트빛 꿈속의 픽셀 요리 배지로 담습니다. 중심은 선명하고 주변은 흰색으로 스며듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-236"><img src="./assets/roster/236.jpg" alt="XXD Panel 236 · 흑백 기하 기호" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-236"><strong>236</strong> · 흑백 기하 기호</a><br><sub>사진을 끊기지 않는 흰 바탕 한가운데의 아주 작은 흑백 기하 기호로 압축합니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-237"><img src="./assets/roster/237.jpg" alt="XXD Panel 237 · Y2K 스티커 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-237"><strong>237</strong> · Y2K 스티커 콜라주</a><br><sub>같은 주인공을 흰 테두리 스티커 여러 장으로 나누어 옅은 회보라색 neo-Y2K 진 페이지에 흩뿌립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-238"><img src="./assets/roster/238.jpg" alt="XXD Panel 238 · 고딕 그림책 소품" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-238"><strong>238</strong> · 고딕 그림책 소품</a><br><sub>사진을 거의 빈 종이 위의 작고 연약하며 조금 어두운 과슈 그림책 형상으로 담습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-239"><img src="./assets/roster/239.jpg" alt="XXD Panel 239 · 별색 어긋남 포스터" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-239"><strong>239</strong> · 별색 어긋남 포스터</a><br><sub>사진을 글자가 그림이 되는 별색 공판 실험 포스터로 만듭니다. 망점, 판 어긋남, 따뜻한 종이.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-240"><img src="./assets/roster/240.jpg" alt="XXD Panel 240 · 크레용 시각 일기" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-240"><strong>240</strong> · 크레용 시각 일기</a><br><sub>사진을 다 그리지 않은 크레용 시각 일기 한 장으로 담습니다. 작은 주인공, 따뜻한 흙색, 넓은 빈칸.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-241"><img src="./assets/roster/241.jpg" alt="XXD Panel 241 · 시적인 표본 도감" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-241"><strong>241</strong> · 시적인 표본 도감</a><br><sub>주인공을 시적인 표본 한 페이지로 만듭니다. 일부는 정밀한 흑백 사진, 빈 부분은 여백 속 연약한 손그림 윤곽.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-242"><img src="./assets/roster/242.jpg" alt="XXD Panel 242 · 천진한 부적 일러스트" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-242"><strong>242</strong> · 천진한 부적 일러스트</a><br><sub>사진 속 평범한 물건을 짙은 무광 바탕 위 사탕색 실루엣의 천진한 부적으로 그립니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-243"><img src="./assets/roster/243.jpg" alt="XXD Panel 243 · 파란 볼펜 줄노트 스케치" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-243"><strong>243</strong> · 파란 볼펜 줄노트 스케치</a><br><sub>사진을 파란 볼펜으로 그린 줄노트 한 페이지로 바꿉니다. 빗금은 촘촘하다 성글고, 그린 과정이 남습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-244"><img src="./assets/roster/244.jpg" alt="XXD Panel 244 · 멈춘 펜 노트" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-244"><strong>244</strong> · 멈춘 펜 노트</a><br><sub>사진을 개인 노트에 무심히 그은 한 획으로 바꿉니다. 작은 주인공, 끊기는 먹선, 얇은 수채 몇 군데.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-245"><img src="./assets/roster/245.jpg" alt="XXD Panel 245 · 기억의 여백" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-245"><strong>245</strong> · 기억의 여백</a><br><sub>사진을 조용한 기억 한 페이지로 바꿉니다. 둥글게 단순화한 작은 주인공 둘레로 넓은 흰 종이.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-246"><img src="./assets/roster/246.jpg" alt="XXD Panel 246 · 신구성주의 콜라주" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-246"><strong>246</strong> · 신구성주의 콜라주</a><br><sub>사진 속 주인공 하나를 기하학 색면, 구조선, 넓은 여백으로 된 개념 포스터로 바꿉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-247"><img src="./assets/roster/247.jpg" alt="XXD Panel 247 · 부드러운 그림책" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-247"><strong>247</strong> · 부드러운 그림책</a><br><sub>사진 속 한 장면을 색연필과 수채로 그린 작은 그림책 한 컷으로 바꿉니다. 둘레는 넓은 여백입니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-248"><img src="./assets/roster/248.jpg" alt="XXD Panel 248 · 오래된 여행 수첩" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-248"><strong>248</strong> · 오래된 여행 수첩</a><br><sub>사진의 전부가 아니라 보고 난 뒤 남은 인상을 그립니다. 옅은 먹과 수채로 된 여행 수첩 한 페이지.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-249"><img src="./assets/roster/249.jpg" alt="XXD Panel 249 · 분위기 픽셀" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-249"><strong>249</strong> · 분위기 픽셀</a><br><sub>사진 속 한순간을 레트로 게임 세계의 조용한 한 칸으로 압축합니다. 저해상도, 부드러운 색면, 넓은 여백.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-250"><img src="./assets/roster/250.jpg" alt="XXD Panel 250 · 건축 기하의 시" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-250"><strong>250</strong> · 건축 기하의 시</a><br><sub>사진 속 장면을 추상적인 건축 윤곽, 기하학 색면, 조용한 여백으로 정리합니다.</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>251–300</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-251"><img src="./assets/roster/251.jpg" alt="XXD Panel 251 · 픽셀 생명 기록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-251"><strong>251</strong> · 픽셀 생명 기록</a><br><sub>사진의 주인공을 격자 위 픽셀 생명 기호로 압축합니다. 미래 문명이 보관한 자연 표본처럼.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-252"><img src="./assets/roster/252.jpg" alt="XXD Panel 252 · 힐링 스티커" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-252"><strong>252</strong> · 힐링 스티커</a><br><sub>사진 속 주인공을 둥글고 말랑한 다이어리용 작은 스티커로 바꿉니다. 둘레는 조용한 여백입니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-253"><img src="./assets/roster/253.jpg" alt="XXD Panel 253 · 플랫 열쇠" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-253"><strong>253</strong> · 플랫 열쇠</a><br><sub>사진의 주제를 맑은 색면의 플랫 기호 하나로 압축합니다. 이야기가 담긴 시각적 열쇠처럼.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-254"><img src="./assets/roster/254.jpg" alt="XXD Panel 254 · 동양 기하 기록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-254"><strong>254</strong> · 동양 기하 기록</a><br><sub>사진 속 주인공을 반투명한 기하학 조각으로 해체해 넓은 빈 공간에 띄웁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-255"><img src="./assets/roster/255.jpg" alt="XXD Panel 255 · 여행 기념 우표" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-255"><strong>255</strong> · 여행 기념 우표</a><br><sub>사진 속 한순간을 작은 여행 기념 우표 안에 담습니다. 둘레는 넓은 빈 종이입니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-256"><img src="./assets/roster/256.jpg" alt="XXD Panel 256 · 천진한 민예" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-256"><strong>256</strong> · 천진한 민예</a><br><sub>사진을 가운데 놓인 작은 천진한 민예 그림으로 바꿉니다. 주인공 하나, 감정 하나, 금박 조금.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-257"><img src="./assets/roster/257.jpg" alt="XXD Panel 257 · 고요한 단선" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-257"><strong>257</strong> · 고요한 단선</a><br><sub>사진 속 주인공을 아주 가늘고 조금 불규칙한 선 하나로 줄여 넓은 여백에 띄웁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-258"><img src="./assets/roster/258.jpg" alt="XXD Panel 258 · 크림 꿈결" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-258"><strong>258</strong> · 크림 꿈결</a><br><sub>사진 속 주인공을 크림처럼 말랑한 아주 작은 조각으로 다시 빚어, 크림색의 빈 공간에 띄웁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-259"><img src="./assets/roster/259.jpg" alt="XXD Panel 259 · 고전 시 원고" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-259"><strong>259</strong> · 고전 시 원고</a><br><sub>사진 속 주인공을 불완전한 먹선으로 그린 고전 시 원고 한 장으로 바꿉니다. 오랜 뒤 기억으로 다시 그린 한순간처럼.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-260"><img src="./assets/roster/260.jpg" alt="XXD Panel 260 · 기하의 기억" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-260"><strong>260</strong> · 기하의 기억</a><br><sub>사진을 기하학 기호로 이루어진 기억의 지도로 바꿉니다. 주인공은 작고 둘레는 넓은 여백입니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-261"><img src="./assets/roster/261.jpg" alt="XXD Panel 261 · 크레용 기억" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-261"><strong>261</strong> · 크레용 기억</a><br><sub>그곳을 그리지 않고 그곳이 남긴 느낌을 그립니다. 색연필과 크레용으로 그린 작은 기억.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-262"><img src="./assets/roster/262.jpg" alt="XXD Panel 262 · 필름 잔상" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-262"><strong>262</strong> · 필름 잔상</a><br><sub>사진 속 주인공을 채도 낮은 옛 영화 한 컷의 잔상으로 남겨, 넓은 여백에 조용히 띄웁니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-263"><img src="./assets/roster/263.jpg" alt="XXD Panel 263 · 기념 인장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-263"><strong>263</strong> · 기념 인장</a><br><sub>사진 속 주인공을 작은 기념 인장으로 압축합니다. 소중히 보관된 문화 기념품처럼.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-264"><img src="./assets/roster/264.jpg" alt="XXD Panel 264 · 원고 낙서" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-264"><strong>264</strong> · 원고 낙서</a><br><sub>사진을 개인 스케치북 한 페이지의 천진한 선화로 바꿉니다. 덜 그렸지만 감정은 가득합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-265"><img src="./assets/roster/265.jpg" alt="XXD Panel 265 · 식물 휘장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-265"><strong>265</strong> · 식물 휘장</a><br><sub>사진 속 주인공을 꽃과 잎에 둘러싸인 작은 휘장으로 만듭니다. 오래 간직해 온 개인의 표식처럼.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-266"><img src="./assets/roster/266.jpg" alt="XXD Panel 266 · 상징 마크" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-266"><strong>266</strong> · 상징 마크</a><br><sub>사진 속 주인공을 작은 미니멀 기호 하나로 걸러 냅니다. 문화 기관이나 브랜드의 마크처럼.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-267"><img src="./assets/roster/267.jpg" alt="XXD Panel 267 · 패브릭 배지" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-267"><strong>267</strong> · 패브릭 배지</a><br><sub>사진 속 주인공을 작은 천 배지로 만듭니다. 데님, 바느질, 패치워크, 올이 풀린 가장자리.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-268"><img src="./assets/roster/268.jpg" alt="XXD Panel 268 · 고요한 기호" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-268"><strong>268</strong> · 고요한 기호</a><br><sub>사진 속 주인공을 개인 소장품에 찍은 도장 같은, 아주 작고 조용한 기호로 압축합니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-269"><img src="./assets/roster/269.jpg" alt="XXD Panel 269 · 실험 수첩" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-269"><strong>269</strong> · 실험 수첩</a><br><sub>사진 속 주인공을 실험 노트에 기록된 작은 개념 기호로 바꿉니다. 먹선, 망점, 약간의 색면.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-270"><img src="./assets/roster/270.jpg" alt="XXD Panel 270 · 동양 토템" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-270"><strong>270</strong> · 동양 토템</a><br><sub>사진 속 주인공을 동양 인장 같은 작은 토템으로 걸러 냅니다. 작고 장중하게, 둘레는 넓은 여백.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-271"><img src="./assets/roster/271.jpg" alt="XXD Panel 271 · 나만의 휘장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-271"><strong>271</strong> · 나만의 휘장</a><br><sub>사진 속 주인공을 민예 판화 느낌의 개인 휘장으로 만듭니다. 윤곽 하나, 별색 몇 가지, 종이 위의 잉크.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-272"><img src="./assets/roster/272.jpg" alt="XXD Panel 272 · 단색 영혼" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-272"><strong>272</strong> · 단색 영혼</a><br><sub>사진 속 주인공을 약간의 표정과 성깔이 있는 흑백 손그림 캐릭터 하나로 바꿉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-273"><img src="./assets/roster/273.jpg" alt="XXD Panel 273 · 아르누보 문장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-273"><strong>273</strong> · 아르누보 문장</a><br><sub>사진 속 주인공을 색 하나만 얹은 아르누보풍 가는 선 문장으로 줄입니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-274"><img src="./assets/roster/274.jpg" alt="XXD Panel 274 · 밤빛 크레용" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-274"><strong>274</strong> · 밤빛 크레용</a><br><sub>검은 종이 위에 빛나는 듯한 크레용 색선으로 사진 속 주인공을 작은 마크로 그립니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-275"><img src="./assets/roster/275.jpg" alt="XXD Panel 275 · 소박한 배지" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-275"><strong>275</strong> · 소박한 배지</a><br><sub>사진 속 주인공을 둥글고 조금 서툰 손으로 만든 작은 배지로 바꿉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-276"><img src="./assets/roster/276.jpg" alt="XXD Panel 276 · 공간 아카이브" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-276"><strong>276</strong> · 공간 아카이브</a><br><sub>사진 속 구조를 해체해 아주 가는 선의 미완성 공간 연구로 겹쳐 놓습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-277"><img src="./assets/roster/277.jpg" alt="XXD Panel 277 · 기하학 마크" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-277"><strong>277</strong> · 기하학 마크</a><br><sub>사진 속 주인공을 기하학 실루엣과 평면 색면으로 짠 모더니즘 작은 심벌로 줄입니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-278"><img src="./assets/roster/278.jpg" alt="XXD Panel 278 · 문화 실루엣" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-278"><strong>278</strong> · 문화 실루엣</a><br><sub>사진 속 주인공을 기하학 색면으로 짠, 실크스크린 느낌의 종이 오리기 작은 인장으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-279"><img src="./assets/roster/279.jpg" alt="XXD Panel 279 · 시스템 유전자" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-279"><strong>279</strong> · 시스템 유전자</a><br><sub>사진 속 주인공을 기하학 모듈, 가는 선, 작은 번호로 이루어진 포스트디지털 추상 마크로 압축합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-280"><img src="./assets/roster/280.jpg" alt="XXD Panel 280 · 픽셀 표본" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-280"><strong>280</strong> · 픽셀 표본</a><br><sub>사진 속 주인공을 신호색 하나만 켜진 저해상도 픽셀 휘장으로 기록 페이지에 담습니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-281"><img src="./assets/roster/281.jpg" alt="XXD Panel 281 · 살아 있는 상형" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-281"><strong>281</strong> · 살아 있는 상형</a><br><sub>사진 속 주인공을 납작하고 어두운, 무표정하지만 조금 살아 있는 작은 상형으로 바꿉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-282"><img src="./assets/roster/282.jpg" alt="XXD Panel 282 · 소프트 포커스 유기체" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-282"><strong>282</strong> · 소프트 포커스 유기체</a><br><sub>사진 속 주인공을 반투명한 겹침과 우윳빛 파스텔로 된 작은 추상 마크로 부드럽게 바꿉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-283"><img src="./assets/roster/283.jpg" alt="XXD Panel 283 · 시대의 휘장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-283"><strong>283</strong> · 시대의 휘장</a><br><sub>사진 속 주인공을 우주 시대의 어느 기관이 정식으로 발행한 듯한 휘장으로 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-284"><img src="./assets/roster/284.jpg" alt="XXD Panel 284 · 문명 엠블럼" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-284"><strong>284</strong> · 문명 엠블럼</a><br><sub>사진 속 주인공을 기하학 틀에 넣어, 차가운 색과 따뜻한 색이 부딪히는 작은 기념비로 찍어 냅니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-285"><img src="./assets/roster/285.jpg" alt="XXD Panel 285 · 과학 기념장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-285"><strong>285</strong> · 과학 기념장</a><br><sub>사진 속 주인공을 굵은 윤곽과 망점 잉크의 우표 같은 과학 기념장으로 찍어 냅니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-286"><img src="./assets/roster/286.jpg" alt="XXD Panel 286 · 파스텔 토템" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-286"><strong>286</strong> · 파스텔 토템</a><br><sub>사진에서 가장 남기고 싶은 이미지 하나를 가볍고 조금 기묘한 파스텔 작은 토템으로 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-287"><img src="./assets/roster/287.jpg" alt="XXD Panel 287 · 종이 위 작은 메모" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-287"><strong>287</strong> · 종이 위 작은 메모</a><br><sub>사진 속 주인공을 넓은 빈 종이 위에 그려 넣은 아주 작은 생명체 같은 표시로 남깁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-288"><img src="./assets/roster/288.jpg" alt="XXD Panel 288 · 소장 문장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-288"><strong>288</strong> · 소장 문장</a><br><sub>사진 속 주인공을 옛 학자가 기록한 듯, 양피지 색 위에 가는 조각 선으로 그린 연구 문장으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-289"><img src="./assets/roster/289.jpg" alt="XXD Panel 289 · 민예 표식" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-289"><strong>289</strong> · 민예 표식</a><br><sub>사진 속 주인공을 특징을 살짝 키운, 손으로 찍어 낸 듯한 소박한 민예 작은 심벌로 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-290"><img src="./assets/roster/290.jpg" alt="XXD Panel 290 · 옛 그림책 부호" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-290"><strong>290</strong> · 옛 그림책 부호</a><br><sub>사진 속 주인공을 옛 그림책에 나올 법한, 선이 떨리고 색이 바랜 민간 작은 부호로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-291"><img src="./assets/roster/291.jpg" alt="XXD Panel 291 · 다정한 토템" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-291"><strong>291</strong> · 다정한 토템</a><br><sub>사진 속 주인공을 동화 속 캐릭터 표식 같은, 둥글고 부드러운 작은 토템으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-292"><img src="./assets/roster/292.jpg" alt="XXD Panel 292 · 다이어리 영혼" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-292"><strong>292</strong> · 다이어리 영혼</a><br><sub>사진 속 주인공을 기억에 기대어 재빨리 그린 듯한, 다이어리 표시 같은 작은 감정 아이콘으로 남깁니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-293"><img src="./assets/roster/293.jpg" alt="XXD Panel 293 · 시 같은 작은 도장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-293"><strong>293</strong> · 시 같은 작은 도장</a><br><sub>사진 속 주인공을 옛 종이에 찍은, 조금 서툴고 작은 표정이 있는 시적인 도장으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-294"><img src="./assets/roster/294.jpg" alt="XXD Panel 294 · 아주 작은 사적 부호" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-294"><strong>294</strong> · 아주 작은 사적 부호</a><br><sub>사진에서 아주 작은 흑백 사적 부호 하나만 남기고, 화면 대부분을 여백으로 둡니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-295"><img src="./assets/roster/295.jpg" alt="XXD Panel 295 · 따뜻하고 서툰 심벌" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-295"><strong>295</strong> · 따뜻하고 서툰 심벌</a><br><sub>사진 속 주인공을 둥글고 살짝 균형이 어긋난, 따뜻하고 조금 서툰 사적인 심벌로 줄입니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-296"><img src="./assets/roster/296.jpg" alt="XXD Panel 296 · 몸짓의 흔적" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-296"><strong>296</strong> · 몸짓의 흔적</a><br><sub>사진 속 주인공을 속도와 방향이 있는 목탄이나 먹의 한 획 흔적으로 남깁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-297"><img src="./assets/roster/297.jpg" alt="XXD Panel 297 · 닫히는 암호" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-297"><strong>297</strong> · 닫히는 암호</a><br><sub>사진 속 주인공을 윤곽이 끊겨 있어, 보는 사람이 스스로 채워 완성하는 시각 암호로 남깁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-298"><img src="./assets/roster/298.jpg" alt="XXD Panel 298 · 목탄 인장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-298"><strong>298</strong> · 목탄 인장</a><br><sub>사진 속 주인공을 목탄, 흑연, 먹이 남긴 반추상의 작은 표식으로 줄입니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-299"><img src="./assets/roster/299.jpg" alt="XXD Panel 299 · 복사본 잔해" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-299"><strong>299</strong> · 복사본 잔해</a><br><sub>사진 속 주인공을 여러 번 복사된 듯, 알아볼 수는 있어도 완전히 되돌릴 수 없는 흑백 잔해로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-300"><img src="./assets/roster/300.jpg" alt="XXD Panel 300 · 이진 잔인" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-300"><strong>300</strong> · 이진 잔인</a><br><sub>순수한 검정과 흰색만으로 사진 속 주인공을 빈 공간에서 파내어, 가장자리가 스러지는 작은 인장으로 만듭니다.</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>301–350</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-301"><img src="./assets/roster/301.jpg" alt="XXD Panel 301 · 디지털 유물" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-301"><strong>301</strong> · 디지털 유물</a><br><sub>사진에서 가장 강한 특징을 오래된 컴퓨터에 남겨진 듯한 익명의 흑백 디지털 토템으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-302"><img src="./assets/roster/302.jpg" alt="XXD Panel 302 · 민예 뉴 엠블럼" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-302"><strong>302</strong> · 민예 뉴 엠블럼</a><br><sub>원래 사진은 그대로 두고, 주인공을 따뜻하고 살짝 유머러스한 네오 나이브 수제 엠블럼으로 압축합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-303"><img src="./assets/roster/303.jpg" alt="XXD Panel 303 · 기하 심벌" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-303"><strong>303</strong> · 기하 심벌</a><br><sub>원래 사진은 그대로 두고, 주인공을 사진 없이도 성립하는 기하학 마크로 추상화합니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-304"><img src="./assets/roster/304.jpg" alt="XXD Panel 304 · 구성 토템" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-304"><strong>304</strong> · 구성 토템</a><br><sub>원래 사진은 그대로 두고, 주인공의 기운을 유기적인 것과 기하학이 서로 당기는 추상 토템으로 압축합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-305"><img src="./assets/roster/305.jpg" alt="XXD Panel 305 · 종이 오림 토템" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-305"><strong>305</strong> · 종이 오림 토템</a><br><sub>원래 사진은 그대로 두고, 주인공을 작게 줄여도 알아볼 수 있는 종이 오림 실크스크린 민예 심벌로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-306"><img src="./assets/roster/306.jpg" alt="XXD Panel 306 · 민예 실루엣" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-306"><strong>306</strong> · 민예 실루엣</a><br><sub>원래 사진은 그대로 두고, 넓게 빈 종이 위에 아주 작은 민예 실루엣 하나만 남깁니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-307"><img src="./assets/roster/307.jpg" alt="XXD Panel 307 · 일상의 작은 기록" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-307"><strong>307</strong> · 일상의 작은 기록</a><br><sub>원래 사진은 그대로 두고, 기억에 남은 한 순간을 따뜻한 생활의 작은 심벌로 담습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-308"><img src="./assets/roster/308.jpg" alt="XXD Panel 308 · 종이 컷 배지" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-308"><strong>308</strong> · 종이 컷 배지</a><br><sub>원래 사진은 그대로 두고, 주인공을 어느 곳에서 가져온 듯한 종이 문화 배지로 오려 냅니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-309"><img src="./assets/roster/309.jpg" alt="XXD Panel 309 · 콘셉트 미니 마크" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-309"><strong>309</strong> · 콘셉트 미니 마크</a><br><sub>원래 사진은 그대로 두고, 주인공을 딱 한 곳만 바꿔 두 번째 볼 때 새 뜻이 보이는 작은 배지로 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-310"><img src="./assets/roster/310.jpg" alt="XXD Panel 310 · 정신의 장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-310"><strong>310</strong> · 정신의 장</a><br><sub>원래 사진은 그대로 두고, 커다란 유기적 형태로 아주 작은 밝은 초점을 감싸 사진 속 감정을 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-311"><img src="./assets/roster/311.jpg" alt="XXD Panel 311 · 옛 책 상형" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-311"><strong>311</strong> · 옛 책 상형</a><br><sub>원래 사진은 그대로 두고, 주인공을 옛 책이나 손도장 속 작은 상형 무늬로 담습니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-312"><img src="./assets/roster/312.jpg" alt="XXD Panel 312 · 동화책 기억" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-312"><strong>312</strong> · 동화책 기억</a><br><sub>원래 사진은 그대로 두고, 주인공을 옛 동화책에 떠 있는 듯한 조용한 기억의 작은 도장으로 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-313"><img src="./assets/roster/313.jpg" alt="XXD Panel 313 · 수첩 속 개인 표식" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-313"><strong>313</strong> · 수첩 속 개인 표식</a><br><sub>원래 사진은 그대로 두고, 주인공을 수첩에 여러 번 다시 그린 듯한 개인 기호로 남깁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-314"><img src="./assets/roster/314.jpg" alt="XXD Panel 314 · 어린 날의 기억 도장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-314"><strong>314</strong> · 어린 날의 기억 도장</a><br><sub>원래 사진은 그대로 두고, 주인공을 옛 그림책에 남은 작은 기억의 도장으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-315"><img src="./assets/roster/315.jpg" alt="XXD Panel 315 · 민예 표지" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-315"><strong>315</strong> · 민예 표지</a><br><sub>원래 사진은 그대로 두고, 윤곽 하나나 자세 하나, 일부분 하나를 종이 오림 실크스크린 민예 표지로 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-316"><img src="./assets/roster/316.jpg" alt="XXD Panel 316 · 촉감 미니 조각" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-316"><strong>316</strong> · 촉감 미니 조각</a><br><sub>원래 사진은 그대로 두고, 주인공을 펠트나 점토로 손수 빚은 듯한 작은 소장용 조각으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-317"><img src="./assets/roster/317.jpg" alt="XXD Panel 317 · 둥글고 소박한 토템" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-317"><strong>317</strong> · 둥글고 소박한 토템</a><br><sub>원래 사진은 그대로 두고, 주인공을 둥글고 조금 서툴며 오래 써 온 듯한 민예 토템으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-318"><img src="./assets/roster/318.jpg" alt="XXD Panel 318 · 생활의 흔적" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-318"><strong>318</strong> · 생활의 흔적</a><br><sub>원래 사진은 그대로 두고, 사진 속 일상의 분위기를 따뜻한 그림책풍 작은 마크로 담습니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-319"><img src="./assets/roster/319.jpg" alt="XXD Panel 319 · 시적인 기호" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-319"><strong>319</strong> · 시적인 기호</a><br><sub>원래 사진은 그대로 두고, 흰 종이 위에 시적인 작은 기호 하나와 희미한 두 번째 의미를 남깁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-320"><img src="./assets/roster/320.jpg" alt="XXD Panel 320 · 개성 실루엣" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-320"><strong>320</strong> · 개성 실루엣</a><br><sub>원래 사진은 그대로 두고, 주인공을 실루엣이 먼저이고 윤곽이 끊겨도 되는 캐릭터 마크로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-321"><img src="./assets/roster/321.jpg" alt="XXD Panel 321 · 먹 블록 옛 도장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-321"><strong>321</strong> · 먹 블록 옛 도장</a><br><sub>원래 사진은 그대로 두고, 주인공을 옛 식물 도감이나 민속 도감 속 작은 그림 한 장처럼 먹으로 찍어 냅니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-322"><img src="./assets/roster/322.jpg" alt="XXD Panel 322 · 기하 구성" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-322"><strong>322</strong> · 기하 구성</a><br><sub>원래 사진은 그대로 두고, 주인공을 먼저 형태로 성립하고 나중에 알아보게 되는 미드센추리 모던 기하 심벌로 재구성합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-323"><img src="./assets/roster/323.jpg" alt="XXD Panel 323 · 흰 선 엠블럼" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-323"><strong>323</strong> · 흰 선 엠블럼</a><br><sub>원래 사진은 그대로 두고, 주인공을 질감 있는 바탕 위에 흰 선 하나로 그려 작은 가게 간판처럼 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-324"><img src="./assets/roster/324.jpg" alt="XXD Panel 324 · 작은 사물의 심상" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-324"><strong>324</strong> · 작은 사물의 심상</a><br><sub>원래 사진은 그대로 두고, 커다란 감정을 부적 같은 아주 작은 물건 하나에 담습니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-325"><img src="./assets/roster/325.jpg" alt="XXD Panel 325 · 개인 신화 도장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-325"><strong>325</strong> · 개인 신화 도장</a><br><sub>원래 사진은 그대로 두고, 주인공을 시간의 무게가 느껴지는 개인 신화의 토템으로 봉인합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-326"><img src="./assets/roster/326.jpg" alt="XXD Panel 326 · 거친 토템" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-326"><strong>326</strong> · 거친 토템</a><br><sub>원래 사진은 그대로 두고, 마른 붓과 분필로 만든 절제된 거친 토템을 여백에 띄웁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-327"><img src="./assets/roster/327.jpg" alt="XXD Panel 327 · 어린이 잡지 유물 기호" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-327"><strong>327</strong> · 어린이 잡지 유물 기호</a><br><sub>원래 사진은 그대로 두고, 주인공을 옛 어린이 잡지에서 오려 낸 듯한 작은 인쇄 표식으로 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-328"><img src="./assets/roster/328.jpg" alt="XXD Panel 328 · 레트로 스티커 배지" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-328"><strong>328</strong> · 레트로 스티커 배지</a><br><sub>원래 사진은 그대로 두고, 주인공을 모양대로 오린 스티커 같은 레트로 진(zine) 배지로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-329"><img src="./assets/roster/329.jpg" alt="XXD Panel 329 · 느긋한 가는 선" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-329"><strong>329</strong> · 느긋한 가는 선</a><br><sub>원래 사진은 그대로 두고, 살짝 흔들리는 가는 선으로 조용하고 느긋한 작은 아이콘을 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-330"><img src="./assets/roster/330.jpg" alt="XXD Panel 330 · 나만의 소장품" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-330"><strong>330</strong> · 나만의 소장품</a><br><sub>원래 사진은 그대로 두고, 다이어리 귀퉁이에 누군가 한 사람만의 것이었을 듯한 작은 개인 표식을 남깁니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-331"><img src="./assets/roster/331.jpg" alt="XXD Panel 331 · 이야기책 테두리" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-331"><strong>331</strong> · 이야기책 테두리</a><br><sub>원래 사진은 그대로 두고, 가장자리가 이야기를 하고 가운데는 조용히 비어 있는 옛 이야기책 한 페이지로 다시 씁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-332"><img src="./assets/roster/332.jpg" alt="XXD Panel 332 · 이야기 유물 인장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-332"><strong>332</strong> · 이야기 유물 인장</a><br><sub>사진 속 주인공을 오래된 이야기책에서 남겨진 듯한 작은 인장으로 압축합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-333"><img src="./assets/roster/333.jpg" alt="XXD Panel 333 · 성스러운 기술 유물" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-333"><strong>333</strong> · 성스러운 기술 유물</a><br><sub>사진 속 주인공을 사라진 문명이 남긴 듯한 회로 부조의 작은 인장으로 압축합니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-334"><img src="./assets/roster/334.jpg" alt="XXD Panel 334 · 신화 장서표" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-334"><strong>334</strong> · 신화 장서표</a><br><sub>사진 속 주인공을 가운데 기호 하나와 이를 둘러싼 같은 문양으로 된 신화풍 장서표로 바꿉니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-335"><img src="./assets/roster/335.jpg" alt="XXD Panel 335 · 언더그라운드 스탬프" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-335"><strong>335</strong> · 언더그라운드 스탬프</a><br><sub>사진 속 주인공을 아주 작게 줄여도 알아볼 수 있는 언더그라운드 스트리트 배지로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-336"><img src="./assets/roster/336.jpg" alt="XXD Panel 336 · 중축 신인" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-336"><strong>336</strong> · 중축 신인</a><br><sub>사진을 중심축과 겹겹의 틀 안에 놓인 고요하고 신비로운 형이상학적 작은 인장으로 만듭니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-337"><img src="./assets/roster/337.jpg" alt="XXD Panel 337 · 픽셀 잔해" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-337"><strong>337</strong> · 픽셀 잔해</a><br><sub>사진 속 주인공을 오래된 인터넷에서 파낸 뒤 표본 상자에 넣은 듯한 로파이 픽셀 조각으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-338"><img src="./assets/roster/338.jpg" alt="XXD Panel 338 · 래스터 잔해 휘장" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-338"><strong>338</strong> · 래스터 잔해 휘장</a><br><sub>사진 속 주인공을 강한 실루엣, 적은 정보, 단 하나의 이상점만 남긴 래스터 휘장으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-339"><img src="./assets/roster/339.jpg" alt="XXD Panel 339 · 미래 성물" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-339"><strong>339</strong> · 미래 성물</a><br><sub>사진의 기운을 시간에 닳은 미래의 얕은 부조 기념 메달 하나로 담아냅니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-340"><img src="./assets/roster/340.jpg" alt="XXD Panel 340 · 시각적 특이점" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-340"><strong>340</strong> · 시각적 특이점</a><br><sub>사진을 거의 전부가 여백인 화면 속 아주 작은 흑백 표식 하나로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-341"><img src="./assets/roster/341.jpg" alt="XXD Panel 341 · 두 번째 세계" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-341"><strong>341</strong> · 두 번째 세계</a><br><sub>사진 속 가장 영리한 계기 하나가 중앙선을 넘어 종이 위에서 계속 일어나게 합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-342"><img src="./assets/roster/342.jpg" alt="XXD Panel 342 · 펀칭의 여운" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-342"><strong>342</strong> · 펀칭의 여운</a><br><sub>하나의 틀로 사진에 구멍을 내고, 빼낸 조각들을 단색 여백에 다시 모읍니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-343"><img src="./assets/roster/343.jpg" alt="XXD Panel 343 · 떠 있는 픽셀 그림 조각" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-343"><strong>343</strong> · 떠 있는 픽셀 그림 조각</a><br><sub>사진 속 주인공을 가운데 떠 있고 오른쪽 아래에 부드러운 그림자가 진 파스텔 픽셀 소품으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-344"><img src="./assets/roster/344.jpg" alt="XXD Panel 344 · 미니어처 받침대" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-344"><strong>344</strong> · 미니어처 받침대</a><br><sub>사진 속 주인공을 발밑 땅 한 조각과 함께 잘라 둥근 받침대 위 미니어처 모형으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-345"><img src="./assets/roster/345.jpg" alt="XXD Panel 345 · 어두운 바탕의 실루엣" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-345"><strong>345</strong> · 어두운 바탕의 실루엣</a><br><sub>사진 속 주인공과 곁의 몇 가지를 평면 실루엣으로 눌러 어두운 바탕 위에 한 무리로 겹쳐 세웁니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-346"><img src="./assets/roster/346.jpg" alt="XXD Panel 346 · 골유리 표지" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-346"><strong>346</strong> · 골유리 표지</a><br><sub>사진 속 주인공을 촘촘한 세로 골유리 너머로 찍은 잡지 표지 같은 화면 가득한 클로즈업으로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-347"><img src="./assets/roster/347.jpg" alt="XXD Panel 347 · 의상 입은 작은 입상" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-347"><strong>347</strong> · 의상 입은 작은 입상</a><br><sub>사진 속 주인공을 정면으로 세우고 작은 의상을 입혀 길 떠나는 그림책 인물로 만듭니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-348"><img src="./assets/roster/348.jpg" alt="XXD Panel 348 · 도감 점묘" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-348"><strong>348</strong> · 도감 점묘</a><br><sub>사진 속 주인공을 오래된 박물 도감에 들여 한 가지 잉크 점만으로 표본화를 그립니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-349"><img src="./assets/roster/349.jpg" alt="XXD Panel 349 · 조각 사각 섬" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-349"><strong>349</strong> · 조각 사각 섬</a><br><sub>사진 속 주인공과 발밑 땅 한 조각을 둥근 사각 블록으로 나눠 흰 바탕 위 작은 섬처럼 띄웁니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-350"><img src="./assets/roster/350.jpg" alt="XXD Panel 350 · 네온 정령" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-350"><strong>350</strong> · 네온 정령</a><br><sub>사진 속 한구석을 옅은 선화로 그리고, 주인공을 빛나는 무지개색 통통한 정령으로 바꿉니다.</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>351–354</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-351"><img src="./assets/roster/351.jpg" alt="XXD Panel 351 · 마커 큰 글씨" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-351"><strong>351</strong> · 마커 큰 글씨</a><br><sub>사진의 은유를 삐뚤빼뚤한 굵은 마커 글씨로 쓰고, 주인공을 낙서로 만들어 글자 속에서 놀게 합니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-352"><img src="./assets/roster/352.jpg" alt="XXD Panel 352 · 검은 선 작은 풍경" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-352"><strong>352</strong> · 검은 선 작은 풍경</a><br><sub>사진 속 주인공과 곁의 작은 물건들을 큰 구름 아래 고요한 검은 선의 작은 풍경으로 그립니다.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-353"><img src="./assets/roster/353.jpg" alt="XXD Panel 353 · 점묘 빛의 원뿔" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-353"><strong>353</strong> · 점묘 빛의 원뿔</a><br><sub>사진 속 주인공을 땅 위의 작은 각선 실루엣으로 누르고, 머리 위로 거대한 점묘 빛의 원뿔을 세웁니다.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-354"><img src="./assets/roster/354.jpg" alt="XXD Panel 354 · 굵은 먹선 낙서" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-354"><strong>354</strong> · 굵은 먹선 낙서</a><br><sub>사진 속 주인공을 굵은 먹선으로 두른 통통한 간단한 형태로 그려 굵은 땅선 하나 위에 세웁니다.</sub></td>
  </tr>
</table>

</details>

<!-- xxd-soldier-roster:end -->

## 자주 묻는 질문

**스타일을 전부 설치해야 하나요?** 아니요. 마음에 드는 것만 설치하면 됩니다. 설치하지 않은 스타일도 "미설치"로 표시해 소개·추천하며, 설치하면 이미지를 만들 수 있습니다.

**어떤 스타일이 맞는지 어떻게 판단하나요?** 사진에 무엇이 있는지(주인공, 장면, 색, 글자)와 말해 준 용도·느낌을 각 스타일의 설명과 비교해 고르고, 이유를 알려 줍니다. 사람의 외모로 국적이나 취향을 추측하지 않습니다.

**스타일이 섞이지 않나요?** 섞이지 않습니다. 이미지 한 장은 스타일 하나에만 넘어가고, 그 스타일의 원본 프롬프트로 그려집니다.

**스타일을 바로 쓰는 것과 무엇이 다른가요?** 원하는 스타일이 정해져 있다면 그 번호의 Skill을 바로 쓰는 게 가장 빠릅니다. 아직 못 정했거나 비교하고 싶거나 폴더 전체를 처리할 때 총목록을 쓰세요.

**여러 장을 한꺼번에 하면 섞이지 않나요?** 섞이지 않습니다. 사진마다 따로 생성하고 다른 사진의 색, 글자, 구도를 빌리지 않습니다. 설정은 한 번만 묻습니다.

**제 사진은 어디로 가나요?** 에이전트가 쓰는 이미지 모델로만 갑니다. Skill은 다른 곳에 올리지 않고 접속 주소나 키도 표시하지 않습니다.

## 이미지 생성 설정

`gpt-image-2`(또는 호환 모델)를 제공하는 OpenAI 호환 API와 그 API 키가 필요합니다. 아래 방법은 별도 설정을 만들어 Codex 자체 설정에는 영향을 주지 않습니다:

```bash
mkdir -p ~/.xxd-imagegen
cat > ~/.xxd-imagegen/config.toml <<'EOF'
model_provider = "image"

[model_providers.image]
base_url = "https://api.openai.com/v1"   # 또는 호환 엔드포인트
env_key = "XXD_IMAGE_API_KEY"
EOF

# ~/.zshrc 또는 ~/.bashrc에 넣어 에이전트도 읽을 수 있게
echo 'export XXD_IMAGEGEN_CODEX_DIR=~/.xxd-imagegen' >> ~/.zshrc
echo 'export XXD_IMAGE_API_KEY=내-키' >> ~/.zshrc
```

터미널과 에이전트를 다시 연 뒤, 이 Skill 폴더에서 한 번 확인하세요:

```bash
python3 scripts/canonical/configured_imagegen.py probe
```

`"ok":true`가 나오면 성공입니다. 사용 가능 여부만 보여 주고 주소나 키는 출력하지 않습니다. Codex가 이미 호환 API로 이미지를 만들고 있다면 이 단계는 필요 없습니다.

## 파라미터

총목록은 개별 스타일과 같은 생성 파라미터(`--mode` `--size` `--text` `--locale` `--wallpaper` `--out`)를 받아 각 스타일에 그대로 넘깁니다. 자세한 내용은 아무 스타일 README의 "파라미터 목록"을 보세요. `--prefs last|edit|new|off|clear`로 지난번 설정을 쓰거나, 고치거나, 무시할 수도 있습니다. 레이아웃, 크기, 글자 방식과 언어만 기억하고 사진, 문구, 고른 스타일, 키는 저장하지 않습니다.

## 관리자용

이 저장소에는 전체 시리즈가 함께 쓰는 규칙과 스크립트도 있으며, 각 스타일 저장소에 사본이 있습니다.

| 파일 | 용도 |
|---|---|
| `references/soldier-runtime.md` | 모든 스타일이 함께 쓰는 생성 규칙. 각 스타일 저장소로 동기화 |
| `references/panel-catalog.md` | 추천과 검색을 위한 번호 목록. 이미지 생성 프롬프트가 아님 |
| `references/readme-profile-guide.md` | 스타일의 `readme-profile.json` 작성법 |
| `scripts/build_soldier_readme.py` | 프로필로 5개 언어 README, SKILL 설명, `openai.yaml` 생성 |
| `scripts/build_general_readme.py` | 이 페이지와 스타일 목록 생성 |
| `scripts/soldier_runtime.py` | 공통 규칙과 스크립트를 모든 스타일 저장소에 동기화하고 검사 |
| `scripts/readme_ads.py` | 스타일 README의 광고 블록 검사 |
| `scripts/brief_intake.py` | 새 스타일을 만들기 전에 원본 프롬프트 검사(알려 주기만 하고 고치지 않음) |
| `scripts/unsplash_sample_sources.py` | 샘플용 Unsplash 사진 고르기 |

<!-- xxd-general-ads:start -->
## 광고 정보｜XXD 유료 서비스 및 멤버십

> **광고 및 상업 정보 고지:** 아래 QR 코드, 멤버십, 유료 서비스 링크는 샤오샤오둥의 광고 정보입니다. 스캔이나 구매는 전적으로 자율이며 이 오픈 소스 프로젝트의 접근과 사용에 영향을 주지 않습니다.

### 샤오샤오둥 통합 제어 · 장군 총지휘 Skill · 100위안

100위안을 한 번 결제하면 모든 병사 Skills를 중앙 제어하고 추천·지명·일괄 배정하는 장군 총지휘 Skill(`xxd-panel-all`)과 설치, 버전 업데이트, 부대 구성, 배정 방식에 관한 안내를 받을 수 있습니다. [샤오샤오둥 WeChat](https://xiaoxiaodong.pages.dev/assets/wechat-qr.png)으로 연락하면서 “장군 총지휘 Skill”이라고 적어 주세요.

## 지식성구＋회원 프롬프트 라이브러리＋모든 장군 Skills 멤버십 · 연 699위안

[지식성구](https://wx.zsxq.com/group/15554814142882), [샤오샤오둥 회원 프롬프트 라이브러리](https://vip.xiaoxiaodong.ai/), 모든 장군 Skills 멤버십은 하나로 묶인 동일한 혜택입니다. **한 번의 연회비로 세 가지가 모두 활성화되며 중복 결제할 필요가 없습니다.** 지식성구에서 가입한 뒤 샤오샤오둥에게 WeChat으로 연락하면 회원 프롬프트 라이브러리 교환 코드를 받을 수 있습니다. 회원 프롬프트 라이브러리에서 직접 가입한 뒤에는 WeChat으로 연락해 지식성구에 들어가고 모든 장군 Skills 멤버십 혜택을 활성화할 수 있습니다.
<!-- xxd-general-ads:end -->

## 라이선스

이 프로젝트(Skill, 프롬프트, 스크립트, 문서, 함께 제공되는 샘플 이미지 포함)는 **PolyForm Noncommercial License 1.0.0**을 따릅니다. 전체 법률 문구는 [LICENSE](LICENSE), 공식 페이지는 <https://polyformproject.org/licenses/noncommercial/1.0.0>에서 확인하세요.

쉽게 말하면 다음과 같습니다.

- 개인은 학습, 연구, 실험, 테스트, 취미 프로젝트, 사적 오락에 사용할 수 있습니다. 자선 단체, 교육 기관, 공공 연구·안전·보건 기관, 환경보호 단체, 정부 기관도 사용할 수 있습니다.
- **비상업적 목적**이라면 사용, 복사, 수정, 파생 작업 제작, 공유가 가능합니다. 공유할 때는 이 라이선스(또는 위 링크)와 저자가 제공한 모든 `Required Notice:` 문구를 함께 제공해야 합니다.
- 상업 제품이나 서비스, 유료 납품, 접근권 또는 라이선스 판매, 상업적 적용으로 이어질 것으로 예상되는 용도에는 사용할 수 없습니다. 상업적으로 사용하려면 저작권자에게 별도의 서면 허가를 받아야 합니다.
- 이 계약은 명시된 저작권 라이선스와 제한된 특허 라이선스만 부여합니다. 상표, 브랜드명 또는 명시되지 않은 다른 권리를 부여하지 않으며 라이선스를 제3자에게 재허여할 수도 없습니다.
- 서면으로 위반 통지를 받으면 32일 안에 준수 상태로 돌아가고 실질적인 시정 조치를 해야 하며, 그렇지 않으면 라이선스가 즉시 종료됩니다. 특허 침해를 서면으로 주장해도 특허 라이선스가 종료됩니다.
- 콘텐츠는 법이 허용하는 범위에서 어떠한 보증도 없이 “있는 그대로” 제공됩니다. 사용에 따른 위험과 잠재적 손실은 사용자가 부담합니다.
