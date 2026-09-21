# XXD Panel All · 장군 Skill

<a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md"><strong>한국어</strong></a> · <a href="README.ar.md">العربية</a>

`xxd-panel-all`은 XXD Panel 시리즈의 장군급 Skill입니다. 먼저 현재 환경에 설치된 `xxd-panel-NNN` 병사 Skills를 확인한 뒤 다음 작업을 맡습니다.

사진은 많은데 어떤 스타일을 써야 할지 모르겠고, 하나씩 시험하기에는 너무 느리며 감으로 고르자니 후회하기 쉬운 순간이 있습니다. 이 Skill은 그 첫 판단을 대신합니다. 이미지나 폴더를 건네면 요구를 이해하고 설치된 Panel 중 적임자를 고른 뒤 작업을 배분하고 결과를 모읍니다. 번호를 먼저 외울 필요가 없습니다.

### 30초 안에 이해하기

- **이미지 한 장 만들기:** 주제를 말하거나 사진을 주면 알맞은 Panel을 추천합니다.
- **스타일 비교하기:** 여러 Panel을 지정해 같은 이미지로 각각 시안을 만듭니다.
- **일괄 처리하기:** 폴더를 주고 공통 설정을 쓰거나 이미지마다 Panel을 배정합니다.

가장 간단한 시작 문장은 다음과 같습니다.

> 이것이 제 이미지입니다. 먼저 어떤 Panel을 추천하는지, 각각 왜 잘 맞는지 알려 주세요.

아래에는 설치, 일괄 처리, 환경설정에 관한 전체 설명이 있습니다. 먼저 사용한 뒤 필요할 때 세부 내용을 확인하는 편이 대개 더 빠릅니다.

- 이미지나 주제에 따라 Panel을 지능적으로 추천
- 소재, 시각적 느낌, 용도에 따라 스타일 탐색
- Panel 번호를 지정해 바로 제작
- 같은 입력을 여러 Panel로 시안 제작
- 폴더 안의 각 이미지를 알맞은 Panel에 배정

이 Skill은 질문, 선택, 배정만 담당합니다. 새로운 시각 스타일이 되지 않으며, 설치되지 않은 Panel을 카탈로그 요약만으로 흉내 내지 않습니다.

## 한 명의 장군과 계속 확장되는 미감의 병사 부대

| 계층 | Skill | 담당 업무 |
|---|---|---|
| **장군급** | [`xxd-panel-all`](https://github.com/nevertoday/xxd-panel-all) | 사용 가능한 병사 확인, 이미지·주제·용도에 따른 추천, 번호로 지명, 같은 이미지의 다중 스타일 시안 구성, 이미지 폴더를 항목별로 배정하고 전달. |
| **병사급** | `xxd-panel-NNN` | 각 번호는 독립된 자신의 원본 프롬프트와 미감만 실행하며, 장군이 전달한 개별 작업을 완성품으로 제작. |

장군은 부대를 조직할 뿐 병사를 대신해 그리지 않습니다. 병사의 원본 미감을 고쳐 쓰거나 섞거나 덮어쓰지 않으며, 모든 완성 이미지는 선택된 번호 Skill이 독립적으로 제작합니다.

<!-- xxd-soldier-roster:start -->

## 전체 병사 · 16:9 좌우 대조 샘플

각 칸은 해당 병사의 16:9 좌우 대조 샘플 한 장입니다(왼쪽 실제 사진, 오른쪽 해당 번호의 전역). 이미지를 클릭하면 그 병사의 GitHub 저장소로 이동합니다.

<table>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-001"><img src="./assets/roster/001.jpg" alt="XXD Panel 001 · 레트로 천진 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-001"><strong>001</strong> · 레트로 천진 저널</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-002"><img src="./assets/roster/002.jpg" alt="XXD Panel 002 · 장난스러운 바우하우스" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-002"><strong>002</strong> · 장난스러운 바우하우스</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-003"><img src="./assets/roster/003.jpg" alt="XXD Panel 003 · 긴장감 있는 선의 언어" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-003"><strong>003</strong> · 긴장감 있는 선의 언어</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-004"><img src="./assets/roster/004.jpg" alt="XXD Panel 004 · 도시 원라인 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-004"><strong>004</strong> · 도시 원라인 저널</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-005"><img src="./assets/roster/005.jpg" alt="XXD Panel 005 · 어두운 동화 에디션" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-005"><strong>005</strong> · 어두운 동화 에디션</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-006"><img src="./assets/roster/006.jpg" alt="XXD Panel 006 · 여백의 소극장" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-006"><strong>006</strong> · 여백의 소극장</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-007"><img src="./assets/roster/007.jpg" alt="XXD Panel 007 · 손그림 관찰 페이지" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-007"><strong>007</strong> · 손그림 관찰 페이지</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-008"><img src="./assets/roster/008.jpg" alt="XXD Panel 008 · 파스텔 몽환경" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-008"><strong>008</strong> · 파스텔 몽환경</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-009"><img src="./assets/roster/009.jpg" alt="XXD Panel 009 · 하프톤 앵커 프린트" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-009"><strong>009</strong> · 하프톤 앵커 프린트</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-010"><img src="./assets/roster/010.jpg" alt="XXD Panel 010 · 흑백 옛 그림책" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-010"><strong>010</strong> · 흑백 옛 그림책</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-011"><img src="./assets/roster/011.jpg" alt="XXD Panel 011 · 명상하는 선의 시" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-011"><strong>011</strong> · 명상하는 선의 시</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-012"><img src="./assets/roster/012.jpg" alt="XXD Panel 012 · 생명의 기하학" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-012"><strong>012</strong> · 생명의 기하학</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-013"><img src="./assets/roster/013.jpg" alt="XXD Panel 013 · 여행 티켓 앨범" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-013"><strong>013</strong> · 여행 티켓 앨범</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-014"><img src="./assets/roster/014.jpg" alt="XXD Panel 014 · 종이 부조 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-014"><strong>014</strong> · 종이 부조 저널</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-015"><img src="./assets/roster/015.jpg" alt="XXD Panel 015 · 추상 회고록" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-015"><strong>015</strong> · 추상 회고록</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-016"><img src="./assets/roster/016.jpg" alt="XXD Panel 016 · 운동감 판화" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-016"><strong>016</strong> · 운동감 판화</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-017"><img src="./assets/roster/017.jpg" alt="XXD Panel 017 · 천진 그래픽 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-017"><strong>017</strong> · 천진 그래픽 저널</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-018"><img src="./assets/roster/018.jpg" alt="XXD Panel 018 · 손 종이오리기 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-018"><strong>018</strong> · 손 종이오리기 저널</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-019"><img src="./assets/roster/019.jpg" alt="XXD Panel 019 · 레트로 그래픽 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-019"><strong>019</strong> · 레트로 그래픽 저널</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-020"><img src="./assets/roster/020.jpg" alt="XXD Panel 020 · 임파스토 미니 풍경" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-020"><strong>020</strong> · 임파스토 미니 풍경</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-021"><img src="./assets/roster/021.jpg" alt="XXD Panel 021 · 검은 영역 넘기" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-021"><strong>021</strong> · 검은 영역 넘기</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-022"><img src="./assets/roster/022.jpg" alt="XXD Panel 022 · 색점의 경계 넘기" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-022"><strong>022</strong> · 색점의 경계 넘기</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-023"><img src="./assets/roster/023.jpg" alt="XXD Panel 023 · 동양의 창밖 풍경" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-023"><strong>023</strong> · 동양의 창밖 풍경</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-024"><img src="./assets/roster/024.jpg" alt="XXD Panel 024 · 감정의 창" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-024"><strong>024</strong> · 감정의 창</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-025"><img src="./assets/roster/025.jpg" alt="XXD Panel 025 · 보이지 않는 심상" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-025"><strong>025</strong> · 보이지 않는 심상</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-026"><img src="./assets/roster/026.jpg" alt="XXD Panel 026 · 기하학적 질서" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-026"><strong>026</strong> · 기하학적 질서</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-027"><img src="./assets/roster/027.jpg" alt="XXD Panel 027 · 종이 위 부조" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-027"><strong>027</strong> · 종이 위 부조</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-028"><img src="./assets/roster/028.jpg" alt="XXD Panel 028 · 아이소메트릭 미니 풍경" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-028"><strong>028</strong> · 아이소메트릭 미니 풍경</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-029"><img src="./assets/roster/029.jpg" alt="XXD Panel 029 · 종이 위 느린 스케치" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-029"><strong>029</strong> · 종이 위 느린 스케치</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-030"><img src="./assets/roster/030.jpg" alt="XXD Panel 030 · 자연의 경계 넘기" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-030"><strong>030</strong> · 자연의 경계 넘기</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-031"><img src="./assets/roster/031.jpg" alt="XXD Panel 031 · 우의적 탁본" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-031"><strong>031</strong> · 우의적 탁본</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-032"><img src="./assets/roster/032.jpg" alt="XXD Panel 032 · 그래픽 워드마크" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-032"><strong>032</strong> · 그래픽 워드마크</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-033"><img src="./assets/roster/033.jpg" alt="XXD Panel 033 · 선명한 콜라주 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-033"><strong>033</strong> · 선명한 콜라주 저널</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-034"><img src="./assets/roster/034.jpg" alt="XXD Panel 034 · 여행 스탬프 마크" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-034"><strong>034</strong> · 여행 스탬프 마크</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-035"><img src="./assets/roster/035.jpg" alt="XXD Panel 035 · 블록 재구성" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-035"><strong>035</strong> · 블록 재구성</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-036"><img src="./assets/roster/036.jpg" alt="XXD Panel 036 · 유선형 그림책" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-036"><strong>036</strong> · 유선형 그림책</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-037"><img src="./assets/roster/037.jpg" alt="XXD Panel 037 · 흐르는 금빛 엠블럼" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-037"><strong>037</strong> · 흐르는 금빛 엠블럼</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-038"><img src="./assets/roster/038.jpg" alt="XXD Panel 038 · 직물 생활 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-038"><strong>038</strong> · 직물 생활 저널</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-039"><img src="./assets/roster/039.jpg" alt="XXD Panel 039 · 자수 심상" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-039"><strong>039</strong> · 자수 심상</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-040"><img src="./assets/roster/040.jpg" alt="XXD Panel 040 · 낙서 친구" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-040"><strong>040</strong> · 낙서 친구</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-041"><img src="./assets/roster/041.jpg" alt="XXD Panel 041 · 아이소메트릭 연구실" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-041"><strong>041</strong> · 아이소메트릭 연구실</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-042"><img src="./assets/roster/042.jpg" alt="XXD Panel 042 · 해체된 수채 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-042"><strong>042</strong> · 해체된 수채 저널</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-043"><img src="./assets/roster/043.jpg" alt="XXD Panel 043 · 하얀 거품" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-043"><strong>043</strong> · 하얀 거품</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-044"><img src="./assets/roster/044.jpg" alt="XXD Panel 044 · 플랫 퓨어 골드" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-044"><strong>044</strong> · 플랫 퓨어 골드</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-045"><img src="./assets/roster/045.jpg" alt="XXD Panel 045 · 힐링 블록 도시" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-045"><strong>045</strong> · 힐링 블록 도시</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-046"><img src="./assets/roster/046.jpg" alt="XXD Panel 046 · 임파스토 미니 월드" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-046"><strong>046</strong> · 임파스토 미니 월드</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-047"><img src="./assets/roster/047.jpg" alt="XXD Panel 047 · 아이소메트릭 임파스토 풍경" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-047"><strong>047</strong> · 아이소메트릭 임파스토 풍경</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-048"><img src="./assets/roster/048.jpg" alt="XXD Panel 048 · 투명 구조 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-048"><strong>048</strong> · 투명 구조 저널</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-049"><img src="./assets/roster/049.jpg" alt="XXD Panel 049 · 목판 각인" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-049"><strong>049</strong> · 목판 각인</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-050"><img src="./assets/roster/050.jpg" alt="XXD Panel 050 · 여행 엽서" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-050"><strong>050</strong> · 여행 엽서</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-051"><img src="./assets/roster/051.jpg" alt="XXD Panel 051 · 수제 미니어처 섬" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-051"><strong>051</strong> · 수제 미니어처 섬</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-052"><img src="./assets/roster/052.jpg" alt="XXD Panel 052 · 종이공예 미니어처 섬" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-052"><strong>052</strong> · 종이공예 미니어처 섬</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-053"><img src="./assets/roster/053.jpg" alt="XXD Panel 053 · 펜 담채 기록" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-053"><strong>053</strong> · 펜 담채 기록</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-054"><img src="./assets/roster/054.jpg" alt="XXD Panel 054 · 추억 스티커 앨범" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-054"><strong>054</strong> · 추억 스티커 앨범</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-055"><img src="./assets/roster/055.jpg" alt="XXD Panel 055 · 회화적 기억의 장" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-055"><strong>055</strong> · 회화적 기억의 장</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-056"><img src="./assets/roster/056.jpg" alt="XXD Panel 056 · 여백의 기억 그림" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-056"><strong>056</strong> · 여백의 기억 그림</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-057"><img src="./assets/roster/057.jpg" alt="XXD Panel 057 · 기하학적 기억의 장" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-057"><strong>057</strong> · 기하학적 기억의 장</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-058"><img src="./assets/roster/058.jpg" alt="XXD Panel 058 · 시적 개념 풍경" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-058"><strong>058</strong> · 시적 개념 풍경</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-059"><img src="./assets/roster/059.jpg" alt="XXD Panel 059 · 손그림 우화집" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-059"><strong>059</strong> · 손그림 우화집</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-060"><img src="./assets/roster/060.jpg" alt="XXD Panel 060 · 선(禪) 미니멀 시" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-060"><strong>060</strong> · 선(禪) 미니멀 시</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-061"><img src="./assets/roster/061.jpg" alt="XXD Panel 061 · 시각 기억 노트" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-061"><strong>061</strong> · 시각 기억 노트</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-062"><img src="./assets/roster/062.jpg" alt="XXD Panel 062 · 영리하고 서툰 선" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-062"><strong>062</strong> · 영리하고 서툰 선</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-063"><img src="./assets/roster/063.jpg" alt="XXD Panel 063 · 픽셀 은유 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-063"><strong>063</strong> · 픽셀 은유 저널</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-064"><img src="./assets/roster/064.jpg" alt="XXD Panel 064 · 인디 콜라주 페이지" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-064"><strong>064</strong> · 인디 콜라주 페이지</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-065"><img src="./assets/roster/065.jpg" alt="XXD Panel 065 · 투 라인 에디토리얼 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-065"><strong>065</strong> · 투 라인 에디토리얼 저널</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-066"><img src="./assets/roster/066.jpg" alt="XXD Panel 066 · 천진한 서사의 선" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-066"><strong>066</strong> · 천진한 서사의 선</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-067"><img src="./assets/roster/067.jpg" alt="XXD Panel 067 · 일상 유머 그림" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-067"><strong>067</strong> · 일상 유머 그림</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-068"><img src="./assets/roster/068.jpg" alt="XXD Panel 068 · 동양 사의(寫意) 화첩" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-068"><strong>068</strong> · 동양 사의(寫意) 화첩</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-069"><img src="./assets/roster/069.jpg" alt="XXD Panel 069 · 선명한 붓칠 창" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-069"><strong>069</strong> · 선명한 붓칠 창</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-070"><img src="./assets/roster/070.jpg" alt="XXD Panel 070 · 임파스토 힐링 섬" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-070"><strong>070</strong> · 임파스토 힐링 섬</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-071"><img src="./assets/roster/071.jpg" alt="XXD Panel 071 · 파스텔 시정 노트" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-071"><strong>071</strong> · 파스텔 시정 노트</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-072"><img src="./assets/roster/072.jpg" alt="XXD Panel 072 · 밝은 색채 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-072"><strong>072</strong> · 밝은 색채 저널</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-073"><img src="./assets/roster/073.jpg" alt="XXD Panel 073 · 기하학 도시 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-073"><strong>073</strong> · 기하학 도시 저널</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-074"><img src="./assets/roster/074.jpg" alt="XXD Panel 074 · 감정 아이콘 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-074"><strong>074</strong> · 감정 아이콘 저널</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-075"><img src="./assets/roster/075.jpg" alt="XXD Panel 075 · 어두운 크레용 스케치" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-075"><strong>075</strong> · 어두운 크레용 스케치</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-076"><img src="./assets/roster/076.jpg" alt="XXD Panel 076 · 마카롱 크레용" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-076"><strong>076</strong> · 마카롱 크레용</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-077"><img src="./assets/roster/077.jpg" alt="XXD Panel 077 · 여행 잡지 일러스트" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-077"><strong>077</strong> · 여행 잡지 일러스트</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-078"><img src="./assets/roster/078.jpg" alt="XXD Panel 078 · 금박 압인 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-078"><strong>078</strong> · 금박 압인 저널</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-079"><img src="./assets/roster/079.jpg" alt="XXD Panel 079 · 펜 담채 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-079"><strong>079</strong> · 펜 담채 저널</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-080"><img src="./assets/roster/080.jpg" alt="XXD Panel 080 · 유기적 과슈의 장" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-080"><strong>080</strong> · 유기적 과슈의 장</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-081"><img src="./assets/roster/081.jpg" alt="XXD Panel 081 · 색실 기념 앨범" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-081"><strong>081</strong> · 색실 기념 앨범</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-082"><img src="./assets/roster/082.jpg" alt="XXD Panel 082 · 종이를 뛰쳐나온 수채" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-082"><strong>082</strong> · 종이를 뛰쳐나온 수채</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-083"><img src="./assets/roster/083.jpg" alt="XXD Panel 083 · 못생기고 귀여운 캐릭터 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-083"><strong>083</strong> · 못생기고 귀여운 캐릭터 저널</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-084"><img src="./assets/roster/084.jpg" alt="XXD Panel 084 · 점묘와 선 구성 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-084"><strong>084</strong> · 점묘와 선 구성 저널</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-085"><img src="./assets/roster/085.jpg" alt="XXD Panel 085 · 수제 모형 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-085"><strong>085</strong> · 수제 모형 저널</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-086"><img src="./assets/roster/086.jpg" alt="XXD Panel 086 · 여백의 판화 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-086"><strong>086</strong> · 여백의 판화 저널</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-087"><img src="./assets/roster/087.jpg" alt="XXD Panel 087 · 붉은 실 관계도" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-087"><strong>087</strong> · 붉은 실 관계도</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-088"><img src="./assets/roster/088.jpg" alt="XXD Panel 088 · 문자 조형 시" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-088"><strong>088</strong> · 문자 조형 시</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-089"><img src="./assets/roster/089.jpg" alt="XXD Panel 089 · 일상 소품 노트" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-089"><strong>089</strong> · 일상 소품 노트</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-090"><img src="./assets/roster/090.jpg" alt="XXD Panel 090 · 시각적 사고 지도" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-090"><strong>090</strong> · 시각적 사고 지도</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-091"><img src="./assets/roster/091.jpg" alt="XXD Panel 091 · 블루 라인 여행 앨범" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-091"><strong>091</strong> · 블루 라인 여행 앨범</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-092"><img src="./assets/roster/092.jpg" alt="XXD Panel 092 · 표현적 선묘 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-092"><strong>092</strong> · 표현적 선묘 저널</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-093"><img src="./assets/roster/093.jpg" alt="XXD Panel 093 · 현대 기하 회화" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-093"><strong>093</strong> · 현대 기하 회화</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-094"><img src="./assets/roster/094.jpg" alt="XXD Panel 094 · 고전 2색 책" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-094"><strong>094</strong> · 고전 2색 책</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-095"><img src="./assets/roster/095.jpg" alt="XXD Panel 095 · 적흑 도해 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-095"><strong>095</strong> · 적흑 도해 저널</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-096"><img src="./assets/roster/096.jpg" alt="XXD Panel 096 · 민간 서신 카드" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-096"><strong>096</strong> · 민간 서신 카드</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-097"><img src="./assets/roster/097.jpg" alt="XXD Panel 097 · 레트로 설명 카드" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-097"><strong>097</strong> · 레트로 설명 카드</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-098"><img src="./assets/roster/098.jpg" alt="XXD Panel 098 · 소박한 수채 책" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-098"><strong>098</strong> · 소박한 수채 책</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-099"><img src="./assets/roster/099.jpg" alt="XXD Panel 099 · 서체 마스코트" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-099"><strong>099</strong> · 서체 마스코트</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-100"><img src="./assets/roster/100.jpg" alt="XXD Panel 100 · 민예 서사화" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-100"><strong>100</strong> · 민예 서사화</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-101"><img src="./assets/roster/101.jpg" alt="XXD Panel 101 · 아홉 칸 기억 노트" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-101"><strong>101</strong> · 아홉 칸 기억 노트</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-102"><img src="./assets/roster/102.jpg" alt="XXD Panel 102 · 치유 기하학 저널" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-102"><strong>102</strong> · 치유 기하학 저널</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-103"><img src="./assets/roster/103.jpg" alt="XXD Panel 103 · 선명한 추상 조합" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-103"><strong>103</strong> · 선명한 추상 조합</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-104"><img src="./assets/roster/104.jpg" alt="XXD Panel 104 · 망점 선의 기록" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-104"><strong>104</strong> · 망점 선의 기록</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-105"><img src="./assets/roster/105.jpg" alt="XXD Panel 105 · 시적 여백집" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-105"><strong>105</strong> · 시적 여백집</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-106"><img src="./assets/roster/106.jpg" alt="XXD Panel 106 · 소프트 컬러 픽셀 기록" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-106"><strong>106</strong> · 소프트 컬러 픽셀 기록</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-107"><img src="./assets/roster/107.jpg" alt="XXD Panel 107 · 이미지 낱말 시" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-107"><strong>107</strong> · 이미지 낱말 시</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-108"><img src="./assets/roster/108.jpg" alt="XXD Panel 108 · 신민예 종이 오리기 기록" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-108"><strong>108</strong> · 신민예 종이 오리기 기록</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-109"><img src="./assets/roster/109.jpg" alt="XXD Panel 109 · 부드러운 기하 해체 기록" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-109"><strong>109</strong> · 부드러운 기하 해체 기록</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-110"><img src="./assets/roster/110.jpg" alt="XXD Panel 110 · 일본풍 생활 장면 도감" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-110"><strong>110</strong> · 일본풍 생활 장면 도감</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-111"><img src="./assets/roster/111.jpg" alt="XXD Panel 111 · 텍스타일 콜라주 기록" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-111"><strong>111</strong> · 텍스타일 콜라주 기록</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-112"><img src="./assets/roster/112.jpg" alt="XXD Panel 112 · 금선 종이 기록" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-112"><strong>112</strong> · 금선 종이 기록</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-113"><img src="./assets/roster/113.jpg" alt="XXD Panel 113 · 조개껍데기 픽셀 콜라주" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-113"><strong>113</strong> · 조개껍데기 픽셀 콜라주</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-114"><img src="./assets/roster/114.jpg" alt="XXD Panel 114 · 레트로 파스텔 스크랩북 낙서" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-114"><strong>114</strong> · 레트로 파스텔 스크랩북 낙서</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-115"><img src="./assets/roster/115.jpg" alt="XXD Panel 115 · 파스텔 인장 콜라주 기록" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-115"><strong>115</strong> · 파스텔 인장 콜라주 기록</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-116"><img src="./assets/roster/116.jpg" alt="XXD Panel 116 · 옅은 종이 파스텔 낙서 기록" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-116"><strong>116</strong> · 옅은 종이 파스텔 낙서 기록</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-117"><img src="./assets/roster/117.jpg" alt="XXD Panel 117 · 가는 선 담채 여백 기록" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-117"><strong>117</strong> · 가는 선 담채 여백 기록</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-118"><img src="./assets/roster/118.jpg" alt="XXD Panel 118 · 흑연 여백 스케치 기록" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-118"><strong>118</strong> · 흑연 여백 스케치 기록</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-119"><img src="./assets/roster/119.jpg" alt="XXD Panel 119 · 손바느질 직물과 여백 기록" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-119"><strong>119</strong> · 손바느질 직물과 여백 기록</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-120"><img src="./assets/roster/120.jpg" alt="XXD Panel 120 · 건축 개념 손그림 기록" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-120"><strong>120</strong> · 건축 개념 손그림 기록</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-121"><img src="./assets/roster/121.jpg" alt="XXD Panel 121 · 라이프스타일 두들 편집지" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-121"><strong>121</strong> · 라이프스타일 두들 편집지</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-122"><img src="./assets/roster/122.jpg" alt="XXD Panel 122 · 단색 하프톤 손글씨" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-122"><strong>122</strong> · 단색 하프톤 손글씨</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-123"><img src="./assets/roster/123.jpg" alt="XXD Panel 123 · 빨강·파랑 각진 색연필" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-123"><strong>123</strong> · 빨강·파랑 각진 색연필</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-124"><img src="./assets/roster/124.jpg" alt="XXD Panel 124 · 천 콜라주의 여백" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-124"><strong>124</strong> · 천 콜라주의 여백</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-125"><img src="./assets/roster/125.jpg" alt="XXD Panel 125 · 소박한 크레용의 여백" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-125"><strong>125</strong> · 소박한 크레용의 여백</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-126"><img src="./assets/roster/126.jpg" alt="XXD Panel 126 · 시적인 미니어처 콜라주" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-126"><strong>126</strong> · 시적인 미니어처 콜라주</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-127"><img src="./assets/roster/127.jpg" alt="XXD Panel 127 · 혼합 매체 건축 콜라주" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-127"><strong>127</strong> · 혼합 매체 건축 콜라주</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-128"><img src="./assets/roster/128.jpg" alt="XXD Panel 128 · 에나멜 메달 여행" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-128"><strong>128</strong> · 에나멜 메달 여행</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-129"><img src="./assets/roster/129.jpg" alt="XXD Panel 129 · 동양 확산 여백" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-129"><strong>129</strong> · 동양 확산 여백</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-130"><img src="./assets/roster/130.jpg" alt="XXD Panel 130 · 하드에지 기하 콜라주" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-130"><strong>130</strong> · 하드에지 기하 콜라주</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-131"><img src="./assets/roster/131.jpg" alt="XXD Panel 131 · 사진 낙서 콜라주" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-131"><strong>131</strong> · 사진 낙서 콜라주</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-132"><img src="./assets/roster/132.jpg" alt="XXD Panel 132 · 펜 담채 여행" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-132"><strong>132</strong> · 펜 담채 여행</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-133"><img src="./assets/roster/133.jpg" alt="XXD Panel 133 · 점각 투명 겹침 인쇄" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-133"><strong>133</strong> · 점각 투명 겹침 인쇄</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-134"><img src="./assets/roster/134.jpg" alt="XXD Panel 134 · 그림책 색역 이야기" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-134"><strong>134</strong> · 그림책 색역 이야기</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-135"><img src="./assets/roster/135.jpg" alt="XXD Panel 135 · 스트리트 별색 손그림" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-135"><strong>135</strong> · 스트리트 별색 손그림</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-136"><img src="./assets/roster/136.jpg" alt="XXD Panel 136 · 시적 초현실 여백" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-136"><strong>136</strong> · 시적 초현실 여백</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-137"><img src="./assets/roster/137.jpg" alt="XXD Panel 137 · 에칭 질감 콜라주" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-137"><strong>137</strong> · 에칭 질감 콜라주</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-138"><img src="./assets/roster/138.jpg" alt="XXD Panel 138 · 동양 종이 부조" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-138"><strong>138</strong> · 동양 종이 부조</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-139"><img src="./assets/roster/139.jpg" alt="XXD Panel 139 · 문자 인코딩 선장" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-139"><strong>139</strong> · 문자 인코딩 선장</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-140"><img src="./assets/roster/140.jpg" alt="XXD Panel 140 · 건식 손그림 시각 섬" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-140"><strong>140</strong> · 건식 손그림 시각 섬</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-141"><img src="./assets/roster/141.jpg" alt="XXD Panel 141 · 미니멀 손그림 선묘" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-141"><strong>141</strong> · 미니멀 손그림 선묘</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-142"><img src="./assets/roster/142.jpg" alt="XXD Panel 142 · 확장 글자–이미지 마스크" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-142"><strong>142</strong> · 확장 글자–이미지 마스크</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-143"><img src="./assets/roster/143.jpg" alt="XXD Panel 143 · 문자 조형 시각시" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-143"><strong>143</strong> · 문자 조형 시각시</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-144"><img src="./assets/roster/144.jpg" alt="XXD Panel 144 · 기하 백색 반전 선묘" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-144"><strong>144</strong> · 기하 백색 반전 선묘</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-145"><img src="./assets/roster/145.jpg" alt="XXD Panel 145 · 빈티지 제한색 판화" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-145"><strong>145</strong> · 빈티지 제한색 판화</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-146"><img src="./assets/roster/146.jpg" alt="XXD Panel 146 · 박물학 스카프 삽화" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-146"><strong>146</strong> · 박물학 스카프 삽화</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-147"><img src="./assets/roster/147.jpg" alt="XXD Panel 147 · 도시락 식재료 패키징" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-147"><strong>147</strong> · 도시락 식재료 패키징</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-148"><img src="./assets/roster/148.jpg" alt="XXD Panel 148 · 시각 일기 콜라주" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-148"><strong>148</strong> · 시각 일기 콜라주</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-149"><img src="./assets/roster/149.jpg" alt="XXD Panel 149 · 손그림 질감 플랫 아트" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-149"><strong>149</strong> · 손그림 질감 플랫 아트</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-150"><img src="./assets/roster/150.jpg" alt="XXD Panel 150 · 레트로 모던 페이퍼 컷" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-150"><strong>150</strong> · 레트로 모던 페이퍼 컷</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-151"><img src="./assets/roster/151.jpg" alt="XXD Panel 151 · 소박한 플랫 손그림" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-151"><strong>151</strong> · 소박한 플랫 손그림</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-152"><img src="./assets/roster/152.jpg" alt="XXD Panel 152 · 색면 바탕 페이퍼 아트" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-152"><strong>152</strong> · 색면 바탕 페이퍼 아트</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-153"><img src="./assets/roster/153.jpg" alt="XXD Panel 153 · 단색 다이어리 두들" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-153"><strong>153</strong> · 단색 다이어리 두들</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-154"><img src="./assets/roster/154.jpg" alt="XXD Panel 154 · 레트로 픽셀 여백" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-154"><strong>154</strong> · 레트로 픽셀 여백</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-155"><img src="./assets/roster/155.jpg" alt="XXD Panel 155 · 1점 투시 담채" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-155"><strong>155</strong> · 1점 투시 담채</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-156"><img src="./assets/roster/156.jpg" alt="XXD Panel 156 · 두 별색 판맞춤 어긋남 삽화" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-156"><strong>156</strong> · 두 별색 판맞춤 어긋남 삽화</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-157"><img src="./assets/roster/157.jpg" alt="XXD Panel 157 · 유물 먹 탁본과 여백" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-157"><strong>157</strong> · 유물 먹 탁본과 여백</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-158"><img src="./assets/roster/158.jpg" alt="XXD Panel 158 · 종이 혼합 재료 콜라주" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-158"><strong>158</strong> · 종이 혼합 재료 콜라주</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-159"><img src="./assets/roster/159.jpg" alt="XXD Panel 159 · 문자 망점 실험 포스터" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-159"><strong>159</strong> · 문자 망점 실험 포스터</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-160"><img src="./assets/roster/160.jpg" alt="XXD Panel 160 · 느슨한 펜선과 담채 여백" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-160"><strong>160</strong> · 느슨한 펜선과 담채 여백</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-161"><img src="./assets/roster/161.jpg" alt="XXD Panel 161 · 회화적 색면과 경계 넘기" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-161"><strong>161</strong> · 회화적 색면과 경계 넘기</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-162"><img src="./assets/roster/162.jpg" alt="XXD Panel 162 · 흰 오려낸 종이 받침의 그림책" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-162"><strong>162</strong> · 흰 오려낸 종이 받침의 그림책</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-163"><img src="./assets/roster/163.jpg" alt="XXD Panel 163 · 중앙 단색 면 스탬프 구도" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-163"><strong>163</strong> · 중앙 단색 면 스탬프 구도</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-164"><img src="./assets/roster/164.jpg" alt="XXD Panel 164 · 수묵 건축 선묘 미니어처" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-164"><strong>164</strong> · 수묵 건축 선묘 미니어처</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-165"><img src="./assets/roster/165.jpg" alt="XXD Panel 165 · 중앙 찢긴 틈의 종이 콜라주" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-165"><strong>165</strong> · 중앙 찢긴 틈의 종이 콜라주</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-166"><img src="./assets/roster/166.jpg" alt="XXD Panel 166 · 등각 투영 조각적 부조 디오라마" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-166"><strong>166</strong> · 등각 투영 조각적 부조 디오라마</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-167"><img src="./assets/roster/167.jpg" alt="XXD Panel 167 · 중앙 파형과 두꺼운 잉크 부조" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-167"><strong>167</strong> · 중앙 파형과 두꺼운 잉크 부조</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-168"><img src="./assets/roster/168.jpg" alt="XXD Panel 168 · 종이 흰색을 남긴 겹붓질 색면" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-168"><strong>168</strong> · 종이 흰색을 남긴 겹붓질 색면</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-169"><img src="./assets/roster/169.jpg" alt="XXD Panel 169 · 따뜻한 황토색 작은 잉크 삽화" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-169"><strong>169</strong> · 따뜻한 황토색 작은 잉크 삽화</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-170"><img src="./assets/roster/170.jpg" alt="XXD Panel 170 · 검정과 녹슨 빨강의 거친 작은 삽화" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-170"><strong>170</strong> · 검정과 녹슨 빨강의 거친 작은 삽화</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-171"><img src="./assets/roster/171.jpg" alt="XXD Panel 171 · 세로 골격과 작은 분산 장면" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-171"><strong>171</strong> · 세로 골격과 작은 분산 장면</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-172"><img src="./assets/roster/172.jpg" alt="XXD Panel 172 · 중앙 피사체와 반투명 기하 레이어" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-172"><strong>172</strong> · 중앙 피사체와 반투명 기하 레이어</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-173"><img src="./assets/roster/173.jpg" alt="XXD Panel 173 · 상아색 종이와 문자 미니 풍경" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-173"><strong>173</strong> · 상아색 종이와 문자 미니 풍경</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-174"><img src="./assets/roster/174.jpg" alt="XXD Panel 174 · 투박한 손그림 스티커 집합" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-174"><strong>174</strong> · 투박한 손그림 스티커 집합</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-175"><img src="./assets/roster/175.jpg" alt="XXD Panel 175 · 호박빛 역광의 상아색 종이 조각" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-175"><strong>175</strong> · 호박빛 역광의 상아색 종이 조각</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-176"><img src="./assets/roster/176.jpg" alt="XXD Panel 176 · 정교한 손그림 의식 도형 부조" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-176"><strong>176</strong> · 정교한 손그림 의식 도형 부조</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-177"><img src="./assets/roster/177.jpg" alt="XXD Panel 177 · 이형 실루엣 판화 미니 섬" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-177"><strong>177</strong> · 이형 실루엣 판화 미니 섬</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-178"><img src="./assets/roster/178.jpg" alt="XXD Panel 178 · 이형 실루엣 판화 미니 섬 (동일 원문)" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-178"><strong>178</strong> · 이형 실루엣 판화 미니 섬 (동일 원문)</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-179"><img src="./assets/roster/179.jpg" alt="XXD Panel 179 · 리본형 미니어처 전시 풍경" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-179"><strong>179</strong> · 리본형 미니어처 전시 풍경</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-180"><img src="./assets/roster/180.jpg" alt="XXD Panel 180 · 빈티지 원형 여행 기념 스탬프" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-180"><strong>180</strong> · 빈티지 원형 여행 기념 스탬프</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-181"><img src="./assets/roster/181.jpg" alt="XXD Panel 181 · 문인 수묵담채 소품" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-181"><strong>181</strong> · 문인 수묵담채 소품</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-182"><img src="./assets/roster/182.jpg" alt="XXD Panel 182 · 미니어처 픽셀 그래픽" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-182"><strong>182</strong> · 미니어처 픽셀 그래픽</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-183"><img src="./assets/roster/183.jpg" alt="XXD Panel 183 · 짙은 녹색 모서리 유기 그래픽" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-183"><strong>183</strong> · 짙은 녹색 모서리 유기 그래픽</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-184"><img src="./assets/roster/184.jpg" alt="XXD Panel 184 · 정사각형 일상 손그림 소품" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-184"><strong>184</strong> · 정사각형 일상 손그림 소품</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-185"><img src="./assets/roster/185.jpg" alt="XXD Panel 185 · 옅은 강조색의 흑백 스티커 소품" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-185"><strong>185</strong> · 옅은 강조색의 흑백 스티커 소품</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-186"><img src="./assets/roster/186.jpg" alt="XXD Panel 186 · 부드러운 색의 아홉 칸 기하학 기억" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-186"><strong>186</strong> · 부드러운 색의 아홉 칸 기하학 기억</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-187"><img src="./assets/roster/187.jpg" alt="XXD Panel 187 · 대형 타이포 아카이브 콜라주" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-187"><strong>187</strong> · 대형 타이포 아카이브 콜라주</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-188"><img src="./assets/roster/188.jpg" alt="XXD Panel 188 · 베이지와 금빛 건축 아카이브" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-188"><strong>188</strong> · 베이지와 금빛 건축 아카이브</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-189"><img src="./assets/roster/189.jpg" alt="XXD Panel 189 · 이중 프레임과 사이드바 성냥갑 소품" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-189"><strong>189</strong> · 이중 프레임과 사이드바 성냥갑 소품</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-190"><img src="./assets/roster/190.jpg" alt="XXD Panel 190 · 차가운 파스텔과 따뜻한 강조색" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-190"><strong>190</strong> · 차가운 파스텔과 따뜻한 강조색</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-191"><img src="./assets/roster/191.jpg" alt="XXD Panel 191 · 부드러운 사각 파스텔 색면" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-191"><strong>191</strong> · 부드러운 사각 파스텔 색면</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-192"><img src="./assets/roster/192.jpg" alt="XXD Panel 192 · 제한된 색의 빈티지 그래픽 소품" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-192"><strong>192</strong> · 제한된 색의 빈티지 그래픽 소품</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-193"><img src="./assets/roster/193.jpg" alt="XXD Panel 193 · 낮은 받침 위 차분한 수채 소품" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-193"><strong>193</strong> · 낮은 받침 위 차분한 수채 소품</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-194"><img src="./assets/roster/194.jpg" alt="XXD Panel 194 · 밝은 대지 받침 축측 모형" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-194"><strong>194</strong> · 밝은 대지 받침 축측 모형</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-195"><img src="./assets/roster/195.jpg" alt="XXD Panel 195 · 하나의 밝은 강조색을 둔 역사 몽타주" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-195"><strong>195</strong> · 하나의 밝은 강조색을 둔 역사 몽타주</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-196"><img src="./assets/roster/196.jpg" alt="XXD Panel 196 · 탑뷰 기하학 인물 소품" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-196"><strong>196</strong> · 탑뷰 기하학 인물 소품</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-197"><img src="./assets/roster/197.jpg" alt="XXD Panel 197 · 새장 속 세계 민예 일러스트" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-197"><strong>197</strong> · 새장 속 세계 민예 일러스트</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-198"><img src="./assets/roster/198.jpg" alt="XXD Panel 198 · 제한 팔레트 부유 패션 콜라주" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-198"><strong>198</strong> · 제한 팔레트 부유 패션 콜라주</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-199"><img src="./assets/roster/199.jpg" alt="XXD Panel 199 · 밝고 여백이 넓은 미니 패션 콜라주" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-199"><strong>199</strong> · 밝고 여백이 넓은 미니 패션 콜라주</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-200"><img src="./assets/roster/200.jpg" alt="XXD Panel 200 · 청회색 단색 손그림 선화" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-200"><strong>200</strong> · 청회색 단색 손그림 선화</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-201"><img src="./assets/roster/201.jpg" alt="XXD Panel 201 · 크림색 수공예 미니어처" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-201"><strong>201</strong> · 크림색 수공예 미니어처</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-202"><img src="./assets/roster/202.jpg" alt="XXD Panel 202 · 구조 축을 가진 기하학 선도" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-202"><strong>202</strong> · 구조 축을 가진 기하학 선도</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-203"><img src="./assets/roster/203.jpg" alt="XXD Panel 203 · 여백을 살린 임파스토 엽서" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-203"><strong>203</strong> · 여백을 살린 임파스토 엽서</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-204"><img src="./assets/roster/204.jpg" alt="XXD Panel 204 · 부드러운 빛과 기억 소품" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-204"><strong>204</strong> · 부드러운 빛과 기억 소품</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-205"><img src="./assets/roster/205.jpg" alt="XXD Panel 205 · 따뜻한 유기형 사진 선화 콜라주" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-205"><strong>205</strong> · 따뜻한 유기형 사진 선화 콜라주</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-206"><img src="./assets/roster/206.jpg" alt="XXD Panel 206 · 부드러운 색의 겹종이 미니 풍경" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-206"><strong>206</strong> · 부드러운 색의 겹종이 미니 풍경</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-207"><img src="./assets/roster/207.jpg" alt="XXD Panel 207 · 연한 청백색 혼합 매체 삽화" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-207"><strong>207</strong> · 연한 청백색 혼합 매체 삽화</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-208"><img src="./assets/roster/208.jpg" alt="XXD Panel 208 · 파랑 분홍 모더니즘 추상" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-208"><strong>208</strong> · 파랑 분홍 모더니즘 추상</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-209"><img src="./assets/roster/209.jpg" alt="XXD Panel 209 · 종이 질감의 미니멀 이미지 아카이브" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-209"><strong>209</strong> · 종이 질감의 미니멀 이미지 아카이브</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-210"><img src="./assets/roster/210.jpg" alt="XXD Panel 210 · 차가운 색의 가벼운 개념 콜라주" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-210"><strong>210</strong> · 차가운 색의 가벼운 개념 콜라주</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-211"><img src="./assets/roster/211.jpg" alt="XXD Panel 211 · 의미 기반 배색 기하학 소품" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-211"><strong>211</strong> · 의미 기반 배색 기하학 소품</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-212"><img src="./assets/roster/212.jpg" alt="XXD Panel 212 · 준단색 조각적 형태 연구" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-212"><strong>212</strong> · 준단색 조각적 형태 연구</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-213"><img src="./assets/roster/213.jpg" alt="XXD Panel 213 · 따뜻한 종이 위 차가운 단색 개념화" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-213"><strong>213</strong> · 따뜻한 종이 위 차가운 단색 개념화</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-214"><img src="./assets/roster/214.jpg" alt="XXD Panel 214 · 고유색을 살린 거친 오려내기 소품" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-214"><strong>214</strong> · 고유색을 살린 거친 오려내기 소품</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-215"><img src="./assets/roster/215.jpg" alt="XXD Panel 215 · 황토색 강조가 있는 회색조 축측도" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-215"><strong>215</strong> · 황토색 강조가 있는 회색조 축측도</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-216"><img src="./assets/roster/216.jpg" alt="XXD Panel 216 · 거대한 여백 속 극소 인쇄 섬" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-216"><strong>216</strong> · 거대한 여백 속 극소 인쇄 섬</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-217"><img src="./assets/roster/217.jpg" alt="XXD Panel 217 · 밝은 디지털 혼합 매체 콜라주" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-217"><strong>217</strong> · 밝은 디지털 혼합 매체 콜라주</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-218"><img src="./assets/roster/218.jpg" alt="XXD Panel 218 · 미니멀 그림책 양모 펠트 일러스트" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-218"><strong>218</strong> · 미니멀 그림책 양모 펠트 일러스트</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-219"><img src="./assets/roster/219.jpg" alt="XXD Panel 219 · 색연필 포인트 여행 스케치" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-219"><strong>219</strong> · 색연필 포인트 여행 스케치</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-220"><img src="./assets/roster/220.jpg" alt="XXD Panel 220 · 둥글고 소박한 손그림 두들" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-220"><strong>220</strong> · 둥글고 소박한 손그림 두들</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-221"><img src="./assets/roster/221.jpg" alt="XXD Panel 221 · 摄影与数码混合媒介拼贴海报" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-221"><strong>221</strong> · 摄影与数码混合媒介拼贴海报</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-222"><img src="./assets/roster/222.jpg" alt="XXD Panel 222 · 摄影与数码混合媒介拼贴海报" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-222"><strong>222</strong> · 摄影与数码混合媒介拼贴海报</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-223"><img src="./assets/roster/223.jpg" alt="XXD Panel 223 · 摄影与数码混合媒介拼贴海报" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-223"><strong>223</strong> · 摄影与数码混合媒介拼贴海报</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-224"><img src="./assets/roster/224.jpg" alt="XXD Panel 224 · 瓷器碎片拼合重构" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-224"><strong>224</strong> · 瓷器碎片拼合重构</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-225"><img src="./assets/roster/225.jpg" alt="XXD Panel 225 · 办公物件手绘拼贴" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-225"><strong>225</strong> · 办公物件手绘拼贴</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-226"><img src="./assets/roster/226.jpg" alt="XXD Panel 226 · 糖霜曲奇浅浮雕" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-226"><strong>226</strong> · 糖霜曲奇浅浮雕</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-227"><img src="./assets/roster/227.jpg" alt="XXD Panel 227 · 刺绣任务章" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-227"><strong>227</strong> · 刺绣任务章</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-228"><img src="./assets/roster/228.jpg" alt="XXD Panel 228 · 独立纸艺对象" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-228"><strong>228</strong> · 独立纸艺对象</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-229"><img src="./assets/roster/229.jpg" alt="XXD Panel 229 · 新民艺留白" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-229"><strong>229</strong> · 新民艺留白</a></p>
</td>
  </tr>
</table>

<!-- xxd-soldier-roster:end -->

## 광고 정보｜XXD 유료 서비스 및 멤버십

> **광고 및 상업 정보 고지:** 아래 QR 코드, 멤버십, 유료 서비스 링크는 샤오샤오둥의 광고 정보입니다. 스캔이나 구매는 전적으로 자율이며 이 오픈 소스 프로젝트의 접근과 사용에 영향을 주지 않습니다.

### 샤오샤오둥 통합 제어 · 장군 총지휘 Skill · 100위안

100위안을 한 번 결제하면 모든 병사 Skills를 중앙 제어하고 추천·지명·일괄 배정하는 장군 총지휘 Skill(`xxd-panel-all`)과 설치, 버전 업데이트, 부대 구성, 배정 방식에 관한 안내를 받을 수 있습니다. [샤오샤오둥 WeChat](https://xiaoxiaodong.pages.dev/assets/wechat-qr.png)으로 연락하면서 “장군 총지휘 Skill”이라고 적어 주세요.

## 지식성구＋회원 프롬프트 라이브러리＋모든 장군 Skills 멤버십 · 연 699위안

[지식성구](https://wx.zsxq.com/group/15554814142882), [샤오샤오둥 회원 프롬프트 라이브러리](https://vip.xiaoxiaodong.ai/), 모든 장군 Skills 멤버십은 하나로 묶인 동일한 혜택입니다. **한 번의 연회비로 세 가지가 모두 활성화되며 중복 결제할 필요가 없습니다.** 지식성구에서 가입한 뒤 샤오샤오둥에게 WeChat으로 연락하면 회원 프롬프트 라이브러리 교환 코드를 받을 수 있습니다. 회원 프롬프트 라이브러리에서 직접 가입한 뒤에는 WeChat으로 연락해 지식성구에 들어가고 모든 장군 Skills 멤버십 혜택을 활성화할 수 있습니다.

## 설치

```bash
git clone https://github.com/nevertoday/xxd-panel-all.git
mkdir -p ~/.claude/skills
ln -s "$(pwd)/xxd-panel-all" ~/.claude/skills/xxd-panel-all
```

`npx skills`로 바로 설치할 수도 있습니다.

```bash
npx skills add https://github.com/xiaoxiaodong-ai/xxd-panel-all --skill xxd-panel-all
```

이 명령은 GitHub에서 장군 저장소를 가져와 현재 Agent에 `xxd-panel-all`을 설치합니다. 사용자 수준 Codex Skills 디렉터리에 설치하려면 명령 끝에 `--global --agent codex --yes`를 추가합니다. 장군은 작업 배정만 담당하므로 실제 제작에는 필요한 `xxd-panel-NNN` 병사 Skills를 별도로 설치해야 합니다.

`~/.codex/skills`가 `~/.claude/skills`와 공유되지 않는다면 링크를 하나 더 만드세요.

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)/xxd-panel-all" ~/.codex/skills/xxd-panel-all
```

설치 후 Agent 세션을 다시 열고 다음과 같이 호출합니다.

```text
$xxd-panel-all
```

## 디렉터리 일괄 처리

호출할 때 이미지 디렉터리를 바로 제공할 수 있습니다.

```text
$xxd-panel-all /path/to/images
```

Skill은 즉시 일괄 모드로 들어가 디렉터리와 하위 디렉터리의 이미지를 스캔한 다음 하나의 배정 방식을 묻습니다.

1. 모든 이미지에 같은 Panel 사용
2. 이미지마다 가장 적합한 Panel 자동 매칭
3. 비슷한 이미지를 묶고 그룹마다 같은 Panel 사용
4. 지정한 몇 개 Panel 안에서만 자동 배정

공통 납품 설정은 한 번만 수집합니다. 그 뒤 각 이미지는 해당 `xxd-panel-NNN`에 독립된 작업으로 들어가며, 콜라주로 합쳐지거나 서로 오염되지 않습니다.

## 이전 환경설정 이어 쓰기 또는 새로 설정하기

이번 납품 설정이 아직 완전하지 않고 이전 XXD Panel 환경설정이 감지되면, 장군 또는 병사는 이전 모드, 크기, 문자와 언어, 배경화면 관계, 출력 위치를 먼저 보여 준 뒤 묻습니다.

1. **그대로 이어 쓰기:** 이전 설정을 사용하며 이번에 명시한 요구가 우선합니다.
2. **이어 쓰고 수정하기:** 이전 설정을 불러와 선택한 항목만 바꿉니다.
3. **새로 설정하기:** 기록을 무시하고 처음부터 선택합니다.

요구사항이 모두 명시된 호출은 불필요한 질문 없이 바로 실행합니다. `--prefs last|edit|new|off|clear`를 직접 사용할 수도 있습니다. 환경설정 기록에는 납품 설정만 저장하며 원본 이미지, 정확한 문안, Panel 선택, 생성 결과, 모델 경로, API 인증 정보나 그 밖의 민감한 정보는 저장하지 않습니다.

```text
$xxd-panel-all /path/to/images --prefs last
$xxd-panel-all /path/to/images --prefs edit
$xxd-panel-all /path/to/images --prefs new
```

## 설치 상태

실행 시 Panel은 세 가지 상태로 나뉩니다.

- `AVAILABLE`: 현재 설치되어 바로 호출 가능
- `KNOWN_BUT_MISSING`: 스타일 카탈로그에는 있지만 현재 미설치
- `UNKNOWN`: 카탈로그에 없음

추천, 일괄 배정, 직접 제작에는 설치된 Panel만 사용합니다. 설치되지 않은 스타일도 탐색하고 추천할 수 있지만, 제작하려면 해당 하위 Skill을 설치해야 합니다.

## 프로젝트 구조

```text
xxd-panel-all/
├── SKILL.md
├── assets/
│   └── roster/
├── agents/
│   └── openai.yaml
├── references/
│   ├── panel-catalog.md
│   ├── runtime-preferences.md
│   ├── soldier-runtime.md
│   ├── soldier-adapter.zh-CN.md
│   ├── soldier-adapter.en.md
│   └── sample-workflow.md
└── scripts/
    ├── panel_preferences.py
    ├── soldier_roster.py
    ├── soldier_runtime.py
    └── canonical/
```

- `SKILL.md`: 상호작용, 추천, 탐색, 일괄 라우팅 규칙
- `assets/roster/`: 병사마다 16:9 좌우 대조 샘플 한 장. README 이미지를 클릭하면 해당 GitHub 저장소로 이동
- `panel-catalog.md`: 번호 검색용 카탈로그이며 이미지 생성 프롬프트가 아님
- `soldier-runtime.md`: 가족 공통 병사 런타임 계약. 각 병사 저장소가 축자 사본을 유지함
- `runtime-preferences.md`: 이어 쓰기, 수정, 새 설정, 개인정보 경계
- `panel_preferences.py`: 안전한 납품 환경설정만 읽고 쓰는 로컬 보조 스크립트
- `soldier_roster.py`: 각 병사의 `sample-05.png`로 README 명부를 생성
- `openai.yaml`: Skill 인터페이스 메타데이터

## 라이선스

이 프로젝트(Skill, 프롬프트, 스크립트, 문서, 함께 제공되는 샘플 이미지 포함)는 **PolyForm Noncommercial License 1.0.0**을 따릅니다. 전체 법률 문구는 [LICENSE](LICENSE), 공식 페이지는 <https://polyformproject.org/licenses/noncommercial/1.0.0>에서 확인하세요.

쉽게 말하면 다음과 같습니다.

- 개인은 학습, 연구, 실험, 테스트, 취미 프로젝트, 사적 오락에 사용할 수 있습니다. 자선 단체, 교육 기관, 공공 연구·안전·보건 기관, 환경보호 단체, 정부 기관도 사용할 수 있습니다.
- **비상업적 목적**이라면 사용, 복사, 수정, 파생 작업 제작, 공유가 가능합니다. 공유할 때는 이 라이선스(또는 위 링크)와 저자가 제공한 모든 `Required Notice:` 문구를 함께 제공해야 합니다.
- 상업 제품이나 서비스, 유료 납품, 접근권 또는 라이선스 판매, 상업적 적용으로 이어질 것으로 예상되는 용도에는 사용할 수 없습니다. 상업적으로 사용하려면 저작권자에게 별도의 서면 허가를 받아야 합니다.
- 이 계약은 명시된 저작권 라이선스와 제한된 특허 라이선스만 부여합니다. 상표, 브랜드명 또는 명시되지 않은 다른 권리를 부여하지 않으며 라이선스를 제3자에게 재허여할 수도 없습니다.
- 서면으로 위반 통지를 받으면 32일 안에 준수 상태로 돌아가고 실질적인 시정 조치를 해야 하며, 그렇지 않으면 라이선스가 즉시 종료됩니다. 특허 침해를 서면으로 주장해도 특허 라이선스가 종료됩니다.
- 콘텐츠는 법이 허용하는 범위에서 어떠한 보증도 없이 “있는 그대로” 제공됩니다. 사용에 따른 위험과 잠재적 손실은 사용자가 부담합니다.
