import pandas as pd
import matplotlib.pyplot as plt

## Matplotlib 한글 깨짐 수정 코드
from matplotlib import font_manager, rc
font_path = "./malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family = font_name)





df = pd.read_excel("시도별 전출입 인구수.xlsx", fillna=0, header = 0)
df = df.fillna(method = 'ffill')
mask = (df["전출지별"]=="서울특별시") & (df['전입지별']!="서울특별시")
df_seoul = df[mask]
df_seoul = df_seoul.drop(["전출지별"], axis = 1)
df_seoul.rename({"전입지별":"전입지"}, axis = 1, inplace = True)
df_seoul.set_index("전입지", inplace = True)


sr_one = df_seoul.loc['경기도']

'''

#서식 지정
plt.style.use('ggplot')

plt.figure(figsize=(14,5))

plt.xticks(rotation = 'vertical', size = 10)  #size는폰트 사이즈

plt.plot(sr_one.index, sr_one.values, marker = 'o', markersize = 10)

plt.title("seoul -> 경기")
plt.xlabel("duration")
plt.ylabel("number")

#범례 표시
plt.legend(labels=['서울 -> 경기'], loc='best', fontsize = 15)


# y축 범위 지정 (최소값, 최대값)
plt.ylim(50000, 800000)


########이 부분은 참고만! 아직은 여기까지 하기에는 어려움 

# 주석 표시 - 화살표
plt.annotate('',
             xy=(20, 620000),       #화살표의 머리 부분(끝점)
             xytext=(2, 290000),    #화살표의 꼬리 부분(시작점)
             xycoords='data',       #좌표체계
             arrowprops=dict(arrowstyle='->', color='skyblue', lw=5), #화살표 서식
             )

plt.annotate('',
             xy=(47, 450000),       #화살표의 머리 부분(끝점)
             xytext=(30, 580000),   #화살표의 꼬리 부분(시작점)
             xycoords='data',       #좌표체계
             arrowprops=dict(arrowstyle='->', color='olive', lw=5),  #화살표 서식
             )

# 주석 표시 - 텍스트
plt.annotate('인구이동 증가(1970-1995)',  #텍스트 입력
             xy=(10, 550000),            #텍스트 위치 기준점
             rotation=25,                #텍스트 회전각도
             va='baseline',              #텍스트 상하 정렬
             ha='center',                #텍스트 좌우 정렬
             fontsize=15,                #텍스트 크기
             )

plt.annotate('인구이동 감소(1995-2017)',  #텍스트 입력
             xy=(40, 560000),            #텍스트 위치 기준점
             rotation=-11,               #텍스트 회전각도
             va='baseline',              #텍스트 상하 정렬
             ha='center',                #텍스트 좌우 정렬
             fontsize=15,                #텍스트 크기
             )

plt.show()
'''

#axe 객체 활용
fig = plt.figure(figsize = (10,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(sr_one, 'o', markersize = 10)
ax2.plot(sr_one, marker = 'o', markerfacecolor = "green", markersize = 10, color = 'olive', linewidth=2, label = "s->g")
ax2.legend(loc="best")
ax1.set_ylim(50000,800000)
ax2.set_ylim(50000,800000)


ax2.set_title("s->g")
ax2.set_xlabel('duration', size = 12)
ax2.set_ylabel("number", size = 12)

ax1.set_xticklabels(sr_one.index, rotation = 75)
ax2.set_xticklabels(sr_one.index, rotation = 75)

plt.show()

