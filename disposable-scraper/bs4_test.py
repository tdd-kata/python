from bs4 import BeautifulSoup

tbody_html = """<html>
<body>
<tbody>
    <tr>
        <th>연식</th>
        <td>2018.04</td>
        <th>배기량</th>
        <td>1,995 cc (190마력)</td>
    </tr>
    <tr>
        <th>주행거리</th>
        <td>45,000 km</td>
        <th>색상</th>
        <td>진회색</td>
    </tr>
    <tr>
        <th>변속기</th>
        <td>자동</td>
        <th>
            <div class="help-icon-wrap">
                <button type="button" data-layer="#layer" class="help-btn js-layer">
                    <b>보증정보</b><span class="btn-comm i-help">도움말 열기</span>
                </button>
                <div class="layer-popup js-layer-popup" id="layer" style="width:400px" tabindex="0">
                    <div class="layer-title">
                        보증정보
                    </div>
                    <div class="layer-cont">
                        <dl class="text-type-01 mbnon">
                            <dd class="cont">해당 기간은 제조사 보증 중 엔진 및 동력 부품 기준입니다.  차체 및 일반부품은 제원을 확인해주세요.
                            <br>보증기간은 신차구입부터 계산되며, 기간 또는 주행거리 중 먼저 도래한 것을 보증기간 만료로 간주합니다.</dd>
                        </dl>
                    </div>
                    <button type="button" class="layer-close js-layer-close">
                        <span class="btn-comm btn-close">레이어팝업 닫기</span>
                    </button>
                </div>
            </div>
        </th>
        <td>불가</td>
    </tr>
    <tr>
        <th>연료</th>
        <td>디젤</td>
        <th>확인사항</th>
        <td></td>
    </tr>
</tbody>
</body>
</html>"""

soup = BeautifulSoup(tbody_html)
tbody_children = soup.find_all('tbody')[0].find_all(recursive=True)
for node in tbody_children:
    if node.text == "연식":
        print(node.find_next_siblings("td")[0].text)
    elif node.text == "배기량":
        print(node.find_next_siblings("td")[0].text)

