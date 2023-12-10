from typing import Tuple
# 주의사항 1. 각 파일 간의 함수, 혹은 로직을 공유하지 마세요
# 주의사항 2. 함수 이름은 변경하지 마세요
# 주의사항 3. 함수명이 test_로 시작하는 함수를 만들지 마세요
# 위를 위반하면 채점이 제대로 되지 않아 0점 처리됩니다.

import csv

# 아래에서 pass를 지우고 로직을 작성하세요(10점)
# 아래 함수를 실행하면, assets.csv파일에서 자산 평가액(est_asset_dollar)값이 가장 큰 사람의 이름과 자산 평가액의 값이 리턴되어야 합니다.
# 아래 함수를 실행하면 Tuple 값이 리턴되며, 자산 평가액이 가장 많은 사람의 이름과 자산 평가액이 리턴되어야 합니다.
# 리턴 값의 예) ("Donald", 1023014)
def find_richest_and_asset() -> Tuple:
    with open("hw_data/assets.csv","r") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        # header 날림
        next(csv_data)

        # data의 5번째 컬럼을 str->int로 변경
        data = [(i[0], int(i[4])) for i in csv_data]

        # data에서 asset값이 최대인 경우만 출력
        max_asset = max(data, key=lambda x: x[1]) # 최대값을 표현할 수 있음

    # max_asset 리턴
    return max_asset


# 아래 함수를 실행하면, assets.csv파일에서 도시별(city) 자산 평가액(est_asset_dollar)의 평균을 내고,
# 상위 3개 도시를 리턴해야 합니다.(상위 3개의 순서는 무관합니다.)(20점)
# 아래 함수를 실행하면 list 값이 리턴되며, 평균 자산 평가액이 많은 상위 3개 도시를 리턴합니다.
# 리턴 값의 예) ["Dublin", "Seoul", "New York"]
def find_top3_richest_city() -> list:
    with open("hw_data/assets.csv","r") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        # header 날림
        next(csv_data)

        #평균 자산액 계산
        city_assets = {}
        for row in csv_data:
            city, asset = row[2], int(row[4])

            if city not in city_assets:
                city_assets[city] = []
            city_assets[city].append(asset)

        avg_assets = {city:sum(asset)/len(asset) for (city, asset) in city_assets.items()}

        # 정렬 후 top3 도출
        sorted_lists = sorted(avg_assets.items(), key=lambda x:x[1], reverse=True)
        top3 = [city[0] for city in sorted_lists[:3]]

    return top3
