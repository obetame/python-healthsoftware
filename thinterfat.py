# -*- coding: utf-8 -*-

import Tkinter as tk
import math
import SimpleDialog as sd
import tkSimpleDialog as tksd
import tkMessageBox as tkb
import re

__author__ = {	'name' : 'zhouyuexie',
				'Email' : 'zhouyuexie@hotmail.com',
				'Blog' : 'www.quietboy.net',
				'QQ' : '897415618',
				'Created' : '2015-5-28',
				'verson':'1.3'}

def BMI():						#菜单BMI,计算BMI值
	'计算人体BMI,以菜单的形式出现,点击菜单BMI执行函数BMI,出现一个子窗口计算'
	def bmicalculate():
		try:
			textareabmi.delete(1.0,tk.END)
			height=float(text1.get())/100
			weight=float(text2.get())
		except:
			print tkb.showerror(title='输入错误!',message='请输入数字!')
		else:
			index=round(weight/pow(height,2))
			advise='你身体指数是:'+str(index)
			textareabmi.insert(tk.END,advise)
			if index<18.5:
				textareabmi.insert(tk.END,'\n评价:体重过轻,要多吃读锻炼!')
			elif index>=18.5 and index<24:
				textareabmi.insert(tk.END,'\n评价:真羨慕你,繼續保持下去!可以去做模特兒了!!')
			elif index>=24 and index<27:
				textareabmi.insert(tk.END,'\n评价:重了一点,你需要多运动!')
			elif index>=27 and index<30:
				textareabmi.insert(tk.END,'\n评价:轻度肥胖,你还有机会的!')
			elif index>=30 and index<35:
				textareabmi.insert(tk.END,'\n评价:中度肥胖,找不到女朋友吧?')
			elif index>=35:
				textareabmi.insert(tk.END,'\n评价:重度肥胖....你在等死吗?')

			textareabmi.insert(tk.END,'\n*学习:最有利于健康与寿命的理想值是22,+10%内都是符合理想的范围,男友皆同,通常年轻者适用较低的BMI值,年长者适用较高的BMI值.')


	root=tk.Tk()
	root.geometry('250x300')
	root.title('BMI计算')
	root.iconbitmap('C:\\Users\\zhouyuexie\\fat.ico')
	root.attributes("-alpha",0.95)
	root.resizable(width=False,height=False)

	frame=tk.Frame(root)
	label=tk.Label(frame,fg='blue',wraplength=220,justify='left',text='*BMI是常用的衡量人体胖瘦程度以及是否健康的一个标准.')
	label.pack(fill=tk.BOTH,expand=1,padx=5,pady=5)
	frame.pack(fill=tk.BOTH,expand=1,padx=5)

	frame1=tk.Frame(root)
	label1=tk.Label(frame1,text='1.身高(厘米):')
	heightbmi=tk.IntVar()
	text1=tk.Entry(frame1,textvariable=heightbmi)
	label1.pack(fill=tk.X,expand=0,side=tk.LEFT,padx=3)
	text1.pack(fill=tk.X,expand=1,padx=3)
	frame1.pack(fill=tk.BOTH,expand=0,pady=5)

	frame2=tk.Frame(root)
	label2=tk.Label(frame2,text='2.体重(公斤):')
	weightbmi=tk.IntVar()
	text2=tk.Entry(frame2,textvariable=weightbmi)
	label2.pack(fill=tk.X,expand=0,side=tk.LEFT,padx=3)
	text2.pack(fill=tk.X,expand=1,padx=3)
	frame2.pack(fill=tk.BOTH,expand=0,pady=5)

	button=tk.Button(root,text='开始',command=bmicalculate,width=10,height=1,relief=tk.GROOVE)
	button.pack()

	textareabmi=tk.Text(root)
	textareabmi.pack()
	root.mainloop()


def normal():				#菜单标准体重
	def normalcalculate():
		try:
			textareanormal.delete(1.0,tk.END)
			weight=int(text3.get())
			sex=sexvalue.get()
			height=int(text2.get())
		except:
			print tkb.showerror(title='输入错误!',message='请正确输入!')
		else:
			if sex==1:
				normalweight=round((height-80)*0.7,2)
				advise='你的标准体重是:'+str(normalweight)
				textareanormal.insert(tk.END,advise)
			else:
				normalweight=round((height-70)*0.6,2)
				advise='你的标准体重是:'+str(normalweight)
				textareanormal.insert(tk.END,advise)

			minweight=normalweight*(1-0.1)
			manweight=normalweight*(1+0.1)
			normalare='\n你的体重合理范围:'+str(minweight)+'~'+str(manweight)
			textareanormal.insert(tk.END,normalare)

			if weight<=manweight and weight>=minweight:
				textareanormal.insert(tk.END,'\n你的体重是正常的')
			elif weight>manweight:
				textareanormal.insert(tk.END,'\n不好意思你超重了...')
			elif weight<minweight:
				textareanormal.insert(tk.END,'\n你太轻了,刮风时候请多加小心!')

	def click1(event):
		sexvalue.set(1)
	def click0(event):
		sexvalue.set(0)

	root=tk.Tk()
	root.geometry('250x300')
	root.title('标准体重计算')
	root.iconbitmap('C:\\Users\\zhouyuexie\\fat.ico')
	root.attributes("-alpha",0.95)
	root.resizable(width=False,height=False)

	frame=tk.Frame(root)
	label=tk.Label(frame,fg='blue',wraplength=220,justify='left',text='*标准体重的计算因人种地区不同而异,如果你想减肥,最好要有理想体重的概念.')
	label.pack(fill=tk.BOTH,expand=1,padx=1,pady=1)
	frame.pack(fill=tk.BOTH,expand=1,padx=5)

	frame1=tk.Frame(root)
	label1=tk.Label(frame1,text='1.性别:')
	label1.pack(fill=tk.X,expand=0,side=tk.LEFT,padx=3)
	sexvalue=tk.IntVar()
	sex1=tk.Radiobutton(frame1,text='男',variable=sexvalue,value=1)
	sex0=tk.Radiobutton(frame1,text='女',variable=sexvalue,value=0)
	sexvalue.set(1)
	sex1.bind('<Button-1>',click1)		#绑定函数使单选按钮sexbalue可用
	sex0.bind('<Button-1>',click0)
	sex1.pack(expand=0,side=tk.LEFT,padx=30)
	sex0.pack(expand=0,side=tk.LEFT,padx=30)
	frame1.pack(fill=tk.BOTH,expand=0,pady=5)

	frame2=tk.Frame(root)
	label2=tk.Label(frame2,text='2.身高(cm):')
	label2.pack(fill=tk.X,expand=0,side=tk.LEFT,padx=3,pady=1)
	heightnormal=tk.IntVar()
	text2=tk.Entry(frame2,textvariable=heightnormal)
	text2.pack(fill=tk.X,expand=1,padx=3)
	frame2.pack(fill=tk.BOTH,expand=0,pady=5)

	frame3=tk.Frame(root)
	label3=tk.Label(frame3,text='2.体重(kg):')
	label3.pack(fill=tk.X,expand=0,side=tk.LEFT,padx=3,pady=1)
	weightnormal=tk.IntVar()
	text3=tk.Entry(frame3,textvariable=weightnormal)
	text3.pack(fill=tk.X,expand=1,padx=3)
	frame3.pack(fill=tk.BOTH,expand=0,pady=5)

	button=tk.Button(root,text='开始',command=normalcalculate,width=10,height=1,relief=tk.GROOVE)
	button.pack(expand=0,side=tk.TOP,padx=5,pady=1)

	label4=tk.Label(root,text='结果:')
	label4.pack(fill=tk.X,expand=0,side=tk.LEFT,padx=3,pady=1)

	textareanormal=tk.Text(root)
	textareanormal.pack(fill=tk.BOTH,expand=0,padx=5,pady=1)

	root.mainloop()


#以下是各种食物分类,foodclass是种类
wugu={'白饭1碗':263,'米粉100g':360,'蛋面100g':372,'河粉100g':203,'通心粉100g':368,'意大利粉100g':363,'公仔面100g':250,'一面1个':404,'乌冬100g':100,'上海面100g':356,'面线100g':330,'粉丝100g':350,'燕麦片100g':289}
zhifan={'牛油loz':216,'猪油loz':270,'植物牛油loz':216,'植物油loz':265,'花生油loz':270,'粟米油loz':270,'葵花籽油loz':240,'芝士loz':96,'脱脂芝士loz':11,'鲜奶油loz':85}
haichan={'鱼柳100g':95,'三文鱼100g':130,'鳗鱼100g':340,'比目鱼100g':90,'秋刀鱼100g':240,'黄花鱼100g':62,'虾肉100g':90,'蚬肉100g':50,'龙虾100g':100,'带子100g':100,'墨鱼100g':50,'蟹肉100g':90,'虾米100g':195,'罐头沙丁鱼':335,'罐头吞拿鱼(油浸)100g':200,'罐头吞拿鱼(盐水)100g':200}
roulei={'牛肉100g':114,'牛肉(净瘦肉)100g':450,'牛肉(半肥半瘦)100g':260,'汉堡牛扒100g':300,'撸牛肉100g':240,'烧鸡100g':195,'白切鸡100g':198,'猪肉100g':123,'猪肉100g':123,'煎猪扒100g':451,'烧猪脾100g':317,'香肠100g':326,'煎腌肉100g':674,'火腿100g':389,'午餐肉100g':335,'烧羊脾100g':355}
shucai={'葱100g':47,'洋葱100g':35,'大蒜100g':40,'马蹄100g':68,'菜心100g':20,'白菜100g':17,'通菜100g':20,'大芥菜100g':20,'椰菜(熟)100g':15,'西兰花(熟)100g':18,'椰菜花(熟)100g':29,'苋菜(熟)100g':40,'露笋(熟)100g':15,'番茄(熟)100g':20,'苦瓜(熟)100g':12,'青豆(熟)100g':68,'荷兰豆(熟)100g':32,'青椒(熟)100g':14,'西芹(熟)100g':5,'红萝卜(熟)100g':37,'白萝卜(熟)100g':20,'青萝卜(熟)100g':23,'薯仔(熟)100g':72,'番薯(熟)100g':115,'美国南瓜100g':73,'日本南瓜100g':35,'生菜100g':14,'菠菜100g':19,'芽菜100g':20,'雪菜100g':60,'A菜100g':40,'豆苗100g':40,'番茄100g':14,'青瓜100g':12,'茄瓜100g':26,'丝瓜100g':17,'冬瓜100g':40,'冬瓜100g':40,'芋头100g':94,'美国南瓜100g':73,'皮蛋1隻':160,'番茄100g':14,'苦瓜(熟)100g':12,'露笋(熟)100g':15,'椰菜(熟)100g':15,'椰菜花(熟)100g':29,'菠菜100g':19,'红萝卜(熟)100g':37,'芽菜100g':20,'白萝卜(熟)100g':20,'草菰(罐头)100g':30,'粟米粒(罐头)100g':76,'莲藕100g':52,'马蹄100g':68,'西芹(熟)100g':5,'薯仔(熟)100g':72,'番茄(熟)100g':20,'青瓜100g':12,'丝瓜100g':17}
kuaican={'焗薯烟肉芝士1个':590,'麦乐鸡酱1盒':60,'芝士汉堡1个':320,'汉堡饱1个':236,'早晨全餐1份':640,'鱼柳饱1个':360,'吉士布甸1杯':190,'脆薯饼1件':130,'炸鸡脾1隻':600,'雪糕新地1杯':310,'麦香鸡1个':510,'酸忌廉焗薯1个':460,'麦乐鸡1块':50,'巨无霸1个':530,'鬆饼1件':269,'煎猪扒1件':225,'蛋沙律三文治1份':300,'猪柳蛋汉堡1个':430,'煎香肠1条':220,'照烧猪柳堡1个':460,'牛油焗薯1个':460,'炸鸡翼1隻':350,'烟肉蛋汉堡1个':280,'炸洋葱圈1份':355,'罐头杂果薯仔沙律1碟':350,'热香饼3件':1320}
shengguo={'枇杷1个':17,'皇帝蕉1隻':85,'葡萄1粒':4,'甜柿1个':80,'荔枝1粒':7,'蓝梅1粒':6,'沙田柚1片':20,'水蜜桃1个':70,'车厘子1粒':3,'木瓜1片':50,'西梅1粒':10,'番石榴1个':140,'柠檬1个':20,'杨桃1个':55,'西柚1个':40,'西瓜1片':40,'哈蜜瓜1片':60,'士多啤梨1粒':3,'龙眼1粒':3,'蜜瓜1片':60,'香蕉1隻':90}
chacanting={'菜远排骨饭1碟':524,'粟米肉粒饭1碟':560,'炒蛋1隻':95,'西多士1份':1175,'鸡蛋三文治1份':343,'热狗1隻':255,'火腿蛋三文治1份':420,'公司三文治1客':480,'奶油多士1片':218,'荷包蛋1隻':80,'火腿通粉1碗':270,'海鲜炒乌冬1碟':580,'火腿煎双蛋1份':300,'奶酱多士1片':194,'炸鸡脾饭1碟':800,'煎蛋1隻':105,'沙爹牛肉麵1碗':605,'猪扒饭1碟':548,'西炒饭1碟':710,'餐肉肠公仔麵1碗':770}
jiulou={'菜远牛肉炒河1碟':751,'鱼翅饺1件':39,'芝麻煳1碗':305,'排骨1件':37,'焗西米布甸1杯':280,'牛肉肠粉1条':79,'干烧伊麵1碟':1272,'鲜虾肠粉1条':120,'炸馒头1件':100,'烧卖1件':42,'鸳鸯炒饭1碟':740,'蒸馒头1件':60,'皮蛋瘦肉粥1碗':260,'白灼油菜1碟':140,'珍珠鸡1隻':140,'星州炒米1碟':513,'叉烧包1件':94,'春卷1件':136,'咸肉粽1隻':573,'鲜虾粉果1件':44,'厦门炒米1碟':490,'糯米鸡1隻':400,'乾炒牛河1碟':696,'火鸭丝炆米1碟':588,'马拉糕1件':100,'潮州粉果1件':113,'莲蓉包1件':90,'虾饺1件':37,'瘦叉烧饭1碗':518,'鸡扎1件':45,'小笼饱1件':120,'福建炒饭1碟':645,'鲜竹卷1件':60,'炒米粉1碟':911,'酿青椒1件':180,'山竹牛肉1件':96,'扬州炒饭1碟':620,'芋角1件':113,'煎萝卜糕1件':80,'凤爪1件':25}
zhoumian={'炒麵1碟':911,'碎肉粥1碗':165,'及第粥1碗':270,'牛腩捞麵1碗':670,'潮州粥1碗':132,'油条1条':70,'艇仔粥1碗':260,'牛腩麵1碗':480,'粢饭1条':310,'皮蛋瘦肉粥1碗':260,'灼油菜1碟':140,'白粥1碗':88,'云吞麵1碗':400,'墨丸麵1碗':316,'牛肉麵1碗':470,'鱼片粥1碗':234,'肉丝麵1碗':400,'水饺麵1碗':360,'鲜牛肉粥1碗':247,'牛丸麵1碗':426,'柴鱼花生猪肉粥1碗':300,'鱼蛋粉1碗':320,'排骨麵1碗':480,'淨米粉1碗':173,'淨水饺1碗':535}
zhongshi={'烧鸡100g':195,'烧肉100g':420,'瘦叉烧100g':300,'青椒鸡肉1份':137,'白灼中虾1隻':11,'白切鸡100g':198,'梅菜蒸大鱼腩1份':76,'葱爆猪肉1份':536,'去皮白切鸡100g':148,'烧鸭100g':297,'麻婆豆腐1份':349,'清炒芥兰6棵':20,'蒸酿豆腐1件':65,'半肥瘦叉烧100g':400,'豉汁蒸鱼仓鱼1份':113,'炒三鲜1份':427,'甜酸排骨1份':600,'蚝油金菰1份':130,'青椒炒牛肉1份':228,'青豆虾仁1份':133,'金银蛋苋菜1份':140,'半肥瘦烧肉100g':331,'炒鲜鱿1份':159,'薯仔煮牛肉1份':232}
mianbao={'栗子忌廉蛋糕1件':240,'提子蛋糕1片':320,'芝士蛋糕1件':267,'朱古力冬甩1件':268,'丹麦酥1个':160,'合桃方包1片':130,'芝麻麦包1个':94,'午餐肉包1个':213,'红豆包1个':335,'鲜果挞1件':350,'芝士火腿粟米包1个':295,'软猪仔包1个':169,'纸包蛋糕1件':120,'大理石包1个':150,'肠仔包1个':160,'法国麵饱1片':44,'椰挞1件':280,'鸡尾包1个':221,'水果忌廉蛋糕1件':240,'麦包1个':94,'蛋挞1件':220,'意大利麵饱1片':83,'白麵饱1片':75,'牛角包1个':160,'黑森林蛋糕1件':275,'吞拿鱼包1个':134,'葡挞1件':240,'苹果批1件':269,'蜜糖冬甩1件':186,'菠萝包1个':235,'朱古力榛子包1个':151,'咖喱酥角1个':385,'花生包1个':300,'餐包1个':150,'鸡批1件':300,'叉烧包1个':194,'全麦麵饱1片':65,'合桃蛋糕1片':320,'芝麻包1个':169,'提子包1个':169}
xican={'烧牛肉三文治1份':400,'粟米鸡粒饭1份':383,'咖喱鸡粉1份':764,'公司三文治1份':447,'番茄鸡丝意粉1份':220,'烟三文鱼100g':130,'煎蛋1隻':136,'炸鸡蓝1份':780,'生蠔100g':14,'烧牛肉100g':18,'意式肉酱意粉1份':599,'粟米忌廉汤1碗':157,'焗鸡皇饭1份':483,'汉堡牛扒1份':698,'豌豆虾沙律1份':70,'酥皮汤1碗':450,'焗猪扒意粉1份':363,'吞拿鱼炒律1份':220,'杂菌意粉1份':462,'吞拿鱼三文治1份':330,'鸡蛋饭1份':896,'罗宋汤1碗':126,'薯仔沙律1份':430}
zhongxi={'脆皮雪条1枝':160,'果汁雪条1枝':100,'士多啤梨厚片多士1件':286,'黑糯米1碗':220,'芝麻糊1碗':305,'芝麻雪糕批1枝':200,'合桃糊1碗':211,'低脂乳酪1杯':70,'香蕉班戟1件':403,'喳喳1碗':240,'杏仁糊1碗':221,'日式草饼1个':110,'朱古力曲奇1块':75,'绿豆沙1碗':148,'杏仁豆腐1碗':200,'什果西米捞1碗':300,'芒果布甸1杯':280,'朱古力芭菲1杯':648,'云呢拿雪榚1杯':205,'牛油曲奇1块':70,'雪糕梳打1杯':158,'鲜奶燉蛋1碗':260,'豆腐花1碗':124,'豆沙烧饼1件':256,'朱古力布甸1杯':260,'雪莓娘1件':435,'椰汁西米露1碗':180,'红豆沙1碗':148}
riben={'刺身定食1份':529,'吞拿鱼寿司2件':130,'蟹籽寿司2件':106,'日式冷麵1碗':260,'京烧银鱈鱼1份':326,'天妇罗1份':350,'炸虾汤麵1碗':595,'酱汁猪肉串烧1串':220,'烧秋刀鱼1份':226,'三文鱼刺身100g':160,'甜蛋寿司2件':85,'炸猪扒定食1份':818,'日式海鲜炒饭1份':540,'麵豉汤麵1碗':360,'八爪鱼刺身100g':94,'京风炸豆腐1件':166,'麵豉汤1碗':80,'鰻鱼饭1份':602,'中华拉麵1碗':449,'铁板炒乌冬1份':622,'带子寿司2件':102,'炸豆腐1件':128,'九州拉麵1碗':583,'海胆寿司2件':126,'三文鱼寿司2件':175,'金菇牛肉卷1件':118,'枝豆1份':88,'日式叉烧拉麵1碗':605,'明虾寿司2件':104,'三文鱼子寿司2件':100,'八爪鱼寿司2件':100,'薑汁猪肉定食1份':707,'天妇罗丼1份':767,'盐烧鱼定食1份':425,'赤贝寿司2件':100,'海胆刺身100g':145,'咖喱猪扒饭1份':764,'煎饺子1件':48,'茶碗蒸1碗':93,'酱汁鸡串烧1串':180}
lingshi={'话梅1粒':15,'黑瓜子100g':534,'牛奶朱古力1粒':45,'鸡蛋仔1底':240,'碗仔翅1碗':240,'薯片100g':555,'开心果100g':600,'夏威夷果仁100g':667,'魷鱼丝100g':330,'提子乾100g':320,'茉莉茶冻1粒':97,'咖啡冻1粒':100,'瑞士糖1粒':13,'肉鬆100g':467,'芝士饼1片':90,'消化饼1片':70,'甜全麦饼1片':41,'甜饼1片':27,'鱼蛋1串':100,'薄荷朱古力1粒':31,'蒟蒻椰果1粒':40,'纯味百力滋1盒':250,'牛肉乾100g':475,'凤梨酥1个':160,'杏仁100g':572,'朱古力条1条':1108,'朱古力夹心饼1片':55,'三角朱古力1粒':42,'加钙营养饼1片':31,'合桃100g':667,'万乐珠1粒':9,'白瓜子100g':572,'甘脆朱古力1粒':52,'腰果100g':554,'乐天熊仔饼1盒':350,'茶叶蛋1隻':73,'爆谷100g':459,'士多啤梨百力滋1盒':575,'花生100g':370,'克力架1片':32,'罐头粟米汤1碗':260,'热狗肠1条':189}
jianyou={'方糖1粒':14,'沙律酱1茶匙':34,'生油1茶匙':7,'叉烧酱1茶匙':29,'果酱1茶匙':18,'蕃茄酱1茶匙':5,'蜜糖1茶匙':25,'花生酱1茶匙':24,'老抽1茶匙':5,'糖浆1茶匙':20,'白糖1茶匙':14,'辣椒油1茶匙':19,'蠔油1茶匙':11}
yinliao={'健怡可乐1罐':39,'芬达1罐':190,'炼奶1茶匙':23,'鲜甘蔗汁1杯':100,'朱古力奶昔1杯':364,'淡奶1茶匙':8,'浓缩菠萝汁1杯':500,'生啤1罐':151,'有汽梅酒1罐':165,'黑咖啡1杯':5,'阿华田1杯':45,'茶1杯':1,'鲜柠檬汁1杯':60,'鲜提子汁1杯':140,'脱脂即溶奶粉1杯':356,'云呢拿奶昔1杯':323,'鲜番茄汁1杯':45,'低脂奶1盒':125,'蜂蜜绿茶1罐':52,'香檳1杯':190,'全脂即溶奶粉1杯':506,'无糖乌龙茶1罐':0,'黑啤1罐':160,'苹果梳打1罐':147,'鲜菠萝汁1杯':140,'宝矿力1罐':88,'甜豆浆1杯':120,'浓缩提子汁1杯':395,'鲜西梅汁1杯':180,'红豆冰1杯':350,'啤酒1罐':95,'雪碧1罐':147,'西班牙咖啡1杯':226,'蜜糖1杯':90,'好立克1杯':59,'菊花茶1盒':90,'沙示1罐':128,'珍珠奶茶1杯':180,'苹果梳打酒1罐':167,'清水':0,'清酒1杯':106,'红酒1杯':83,'士多啤梨奶昔1杯':345,'果菜汁1罐':72,'维他奶1盒':120,'鲜苹果汁1杯':120,'鲜奶1盒':143,'餐后酒1杯':140,'鲜橙汁1杯':165,'白酒1杯':83,'低脂即溶奶粉1杯':397,'可乐1罐':178,'益力多1支':100,'浓缩苹果汁1杯':445,'冻柠檬茶1杯':58,'酸梅汤1杯':190,'鲜西柚汁1杯':100}

foodclass={'五谷类':wugu,'肉类':roulei,'脂肪类':zhifan,'海产类':haichan,'蔬菜/蛋类':shucai,
	'快餐店类':kuaican,'生果类':shengguo,'茶餐厅类':chacanting,'酒楼类':jiulou,'粥面类':zhoumian,'中式食肆类':zhongshi,'面包/蛋糕类':mianbao,'西餐类':xican,'中西甜品类':zhongxi,'日本料理类':riben,'即食食品/零食类':lingshi,'酱油/调味料':jianyou,'饮品/酒类':yinliao}
def foodcalculate():
	#使用到上面的食物字典,放全局是为了不用每次点击都创建
	'此函数使菜单计算食物卡路里'
	def searchfood():
		#一个个的查找然后计算卡路里,第一个大循环是查找输入的食物名字有没有数据,如果有就查找这个数据的卡路里增加到文本区域
		textfood.delete(1.0,tk.END)
		food=foodentry.get().encode('utf8')
		if food!='':
			pattern=re.compile('[\x80-\xff]+')
			for a in foodclass:
				for b in foodclass[a]:
					n=re.search(pattern,b)
					if n.group()==food:
						food3.insert(tk.END,b)
						a=1
						break
					else:
						a=0
				if a==1:break
			if a==1:
				foodsum=0
				for i in range(food3.size()):
					foodname=food3.get(i).encode('utf8')
					for a in foodclass:
						for b in foodclass[a]:
							if str(foodname)==b:
								foodnumber=foodclass[a][b]
								foodsum+=foodnumber
				textfood.insert(1.0,'结果:')
				textfood.insert(tk.END,foodsum)
			else:
				print tkb.showerror(title='未找到食物!',message='换个食物名字试试?!')
		else:
			print tkb.showerror(title='输入错误!',message='请输入食物名字!')
		

	def food1click(event):
		global index
		food2.delete(0,tk.END)
		index=food1.get(food1.curselection()).encode('utf8')	#中文不是字符串,转化成字符串会出错,所以必须先由python内部中间unicode编码转换成utf8
		foodclass2=foodclass.get(index)
		for i in foodclass2:
			food2.insert(tk.END,i)

	def food2click(event):
		try:
			global foodsum
			textfood.delete(1.0,tk.END)
			index1=food2.get(food2.curselection()).encode('utf8')
			food3.insert(tk.END,index1)
			foodsum=0
			for i in range(food3.size()):
				food=food3.get(i).encode('utf8')
				for a in foodclass:
					for b in foodclass[a]:
						if food==b:
							foodnumber=foodclass[a][b]
							foodsum+=foodnumber

			textfood.insert(1.0,'结果:')
			textfood.insert(tk.END,foodsum)
		except:
			food3.insert(tk.END,'没有项目可以增加')

		
	def food3click(event):
		try:
			textfood.delete(1.0,tk.END)
			index1=food3.curselection()
			food3.delete(index1)
			food3index=food3.size()
			foodsum=0
			for i in range(food3index):
				food=food3.get(i).encode('utf8')
				for a in foodclass:
					for b in foodclass[a]:
						if food==b:
							foodnumber=foodclass[a][b]
							foodsum+=foodnumber

			textfood.insert(1.0,'结果:')
			textfood.insert(tk.END,foodsum)
		except:
			food3.insert(tk.END,'没有项目可以删除')


	root=tk.Tk()
	root.geometry('350x360')
	root.title('食物卡路里计算')
	root.iconbitmap('C:\\Users\\zhouyuexie\\fat.ico')
	root.attributes("-alpha",0.95)
	root.resizable(width=True,height=True)

	tk.Label(root,text='1.搜索食物:',width=15).grid(row=0,column=0,columnspan=1,sticky=tk.E)				#N是上,W是左,S是下,E是下
	foodsearch=tk.StringVar()
	foodentry=tk.Entry(root,textvariable=foodsearch,width=25,background = '#EFFFD7')
	foodentry.grid(row=0,column=1,columnspan=2,sticky=tk.W)
	tk.Button(root,text='搜索',height=1,width=7,command=searchfood).grid(row=0,column=3,columnspan=1,sticky=tk.W)

	food1=tk.Listbox(root,selectmode=tk.EXTENDED,width=15,height=18,bg='#FFFFCE')
	
	for i in foodclass:
		food1.insert(tk.END,i)
	food1.grid(row=1,column=0,columnspan=1,rowspan=2,sticky=tk.W)
	food1.selection_set(0)
	food1.bind('<Double-Button-1>',food1click)

	food2=tk.Listbox(root,selectmode=tk.EXTENDED,width=16,height=18,bg='#FFFFCE')
	food2.grid(row=1,column=1,columnspan=1,rowspan=2,sticky=tk.W)
	food2.bind('<Double-Button-1>',food2click)

	food3=tk.Listbox(root,selectmode=tk.EXTENDED,width=16,height=12,bg='#FFFFCE')
	food3.grid(row=1,column=2,columnspan=2,rowspan=1,sticky=tk.N)
	food3.bind('<Double-Button-1>',food3click)

	textfood=tk.Text(root,width=16,height=7,bg='#FFFFCE')
	textfood.grid(row=2,column=2,columnspan=2,rowspan=1)
	textfood.insert(1.0,'结果:0\n')
	root.mainloop()




def my():
	'菜单关于绑定的函数,弹出确认和一些作者信息'
	dlg=sd.SimpleDialog(root,text='本软件(版本v1.3)仅供测试交流学习之用,请勿修改用于商业用途.由本软件引发的一切问题都与本人无关,请谨慎使用.联系方式:1241031@163.com',buttons=['同 意','不同意'])
	if dlg.go()==1:
		root.quit()

root=tk.Tk()							#主程序口
root.geometry('400x500')
root.title('营养计算')
root.iconbitmap('C:\\Users\\zhouyuexie\\fat.ico')
root.attributes("-alpha",0.95)
root.resizable(width=False,height=False)


menubar=tk.Menu(root)
menubar.add_command(label='营养计算')
menubar.add_command(label='BMI',command=BMI)
menubar.add_command(label='标准体重',command=normal)
menubar.add_command(label='食物卡路里计算',command=foodcalculate)
menubar.add_command(label='关于',command=my)
root['menu']=menubar


frame1=tk.Frame()			#第一行第一个框架
label1=tk.Label(frame1,text=' 1.您的体脂率%:')
text1e=tk.StringVar()
text1=tk.Entry(frame1,bg='#DEFFAC',textvariable=text1e)
text1e.set('14')
label1.pack(fill=tk.X,expand=0,side=tk.LEFT,padx=3)
text1.pack(fill=tk.X,expand=1,padx=3)
frame1.pack(fill=tk.BOTH,expand=0,pady=5)

frame2=tk.Frame()
label2=tk.Label(frame2,text=' 2. 代谢强度:')
label2.pack(fill=tk.BOTH,side=tk.LEFT)
radiov=tk.IntVar()
radiov.set(1)
radio2text=['1:慢速代谢,不管你吃什么都很容易长肉.','2:中速代谢,不吃太多垃圾食品不会长胖.','3:快速代谢,吃很多体重却好像没有长过.']
for i in range(3):
	tk.Radiobutton(frame2,text=radio2text[i],variable=radiov,value=i).pack(expand=0)
frame2.pack(fill=tk.BOTH,expand=0,pady=5)

frame3=tk.Frame()
label3=tk.Label(frame3,text='3. 您的年龄: ')
text3e=tk.StringVar()
text3=tk.Entry(frame3,bg='#DEFFAC',textvariable=text3e)
text3e.set('20')
label3.pack(fill=tk.X,expand=0,side=tk.LEFT,padx=6)
text3.pack(fill=tk.X,expand=1,side=tk.RIGHT,padx=3)
frame3.pack(fill=tk.BOTH,expand=0,pady=5)

frame4=tk.Frame()
label4=tk.Label(frame4,text='4. 您的体重/kg:')
text4e=tk.StringVar()
text4=tk.Entry(frame4,bg='#DEFFAC',relief=tk.GROOVE,textvariable=text4e)
text4e.set('60')
label4.pack(fill=tk.X,expand=0,side=tk.LEFT,padx=6)
text4.pack(fill=tk.X,expand=1,side=tk.RIGHT,padx=3)
frame4.pack(fill=tk.BOTH,expand=0,pady=5)

frame5=tk.Frame()
label5=tk.Label(frame5,text='  5. 您的目标是: ')
label5.pack(fill=tk.BOTH,side=tk.LEFT)
radioe=tk.IntVar()
radioe.set(1)
radio5text=['1:保重/燃脂/增肌','2:减重/燃脂/雕刻','3:增重/燃脂/增肌']
for i in range(3):
	tk.Radiobutton(frame5,text=radio5text[i],variable=radioe,value=i).pack(expand=0)

frame5.pack(fill=tk.BOTH,expand=0,pady=5)


factors1={'0':'35','1':'45','2':'55'}	#age<18
factors2={'0':'30','1':'40','2':'50'}	#age>18 and age<30
factors3={'0':'25','1':'35','2':'45'}	#age>30 and age<40
factors4={'0':'20','1':'30','2':'40'}	#age>40


def start():
	try:
		textarea.delete(1.0,tk.END)
		fat=float(text1e.get())/100
		rate=str(radiov.get())
		age=float(text3e.get())
		weight=float(text4e.get())
	except:
		print tkb.showerror(title='输入错误!',message='请确保输入正确数字!')
	else:
		if age<18:
			metabolic=float(factors1[rate])/100
		elif age>=18 and age<=30:
			metabolic=float(factors2[rate])/100
		elif age>30 and age<=40:
			metabolic=float(factors3[rate])/100
		elif age>40:
			metabolic=float(factors4[rate])/100
		line1=weight*2.2
		line2=line1*11
		line3=line2*metabolic
		line4=line2+line3			#维持活动必须的卡路里
		line5=fat
		line6=line1*(1-fat)			
		line7=line6*1.14			#所需蛋白质
		line8=line7*4 				
		line9=line4-line8
		ka1='每天基本所需卡路里(卡):'+str(round(line4,2))+'\n'
		ka2='每天所需蛋白质(克):'+str(round(line7,2))+'\n'
		ka3='碳水化合物(克):'+str(round(line9/13,2))+'\n'
		ka4='油脂(克):'+str(round(line9/13,2))+'\n'
		textarea.insert(tk.END,ka1)
		textarea.insert(tk.END,ka2)
		textarea.insert(tk.END,ka3)
		textarea.insert(tk.END,ka4)
		textarea.insert(tk.END,'********************\n')

		number=radioe.get()
		if number==0:
			minka=line9
			maxka=line4
			textarea.insert(tk.END,'保持体重所以卡路里摄入只需要维持每天需要,因此您每天需要所需营养如下:\n')
		elif number==1:
			minka=line9-500
			maxka=line4-500
			textarea.insert(tk.END,'减重所以卡路里摄入需要比正常的少,所以您每天需要所需营养如下:\n')
		elif number==2:
			minka=line9+500
			maxka=line4+500
			textarea.insert(tk.END,'增重所以卡路里摄入需要比正常的多,所以您每天需要所需营养如下:\n')

		ka5=str(round(maxka,2))+'卡/每天\n'
		ka6=str(round(minka/2,2))+'卡/每天(来自碳水)\n'
		ka7=str(round(minka/2,2))+'卡/每天(来自油脂)\n'
		ka8=str(round(minka/2/4,2))+'克/每天(来自碳水)\n'
		ka9=str(round(minka/2/9,2))+'克/每天(来自油脂)\n'
		textarea.insert(tk.END,ka5)
		textarea.insert(tk.END,ka6)
		textarea.insert(tk.END,ka7)
		textarea.insert(tk.END,ka8)
		textarea.insert(tk.END,ka9)


button=tk.Button(root,text='开始',command=start,width=10,height=1,relief=tk.GROOVE)
button.pack()


textarea=tk.Text(root,bg='#FFFFDF')
textarea.pack()


root.mainloop()
