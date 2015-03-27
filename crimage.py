# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

x_im = 320
y_im = 195
im_size = (x_im, y_im)

bg_color = (0, 0, 0)

x_naming = 2
y1_naming = 10
y2_naming = y_im-10
naming_color = (255, 200, 10)

x_alg = 225
alg_color = (80, 240, 60)

x_cur = 180
cur_color = (0, 255, 255)

#naming = ["строка 1", "строка 2", "строка 3", "строка 4", "строка 5", "строка 6"]
#naming = 	["положение ключа управления", 
#			"выключатель РТСН вкл", 
#			"выключатель РТСН откл", 
#			"пружина не заведена", 
#			"аварийное снижение давл. элег."]
#alg =		["ДИСТ", 
#			"ВКЛ",
#			"ОТКЛ",
#			"НЕТ",
#			"НЕТ"]

naming = ["разъединитель ШР-1 включен", "разьединитель ШР-1 отключен", "выключатель В-110 включен", "выключатель В-110 включен", "заземлитель ЗН-1 включен", "заземлитель ЗН-1 отключен", "заземлитель ЗН-2 включен", "заземлитель ЗН-2 отключен", "ЗН ШР-1 110кВ АТ 3", "низкое давление элегаза", "пружины не заведены", "Положение ключа управления"]
alg = ["НЕТ", "ДА", "ДА", "НЕТ", "ДА", "НЕТ", "ДА", "НЕТ", "ОТКЛ", "НЕТ", "НЕТ", "ДИСТ"]

def inp_text(img, pos, text, font, size, color):
	text=text.decode("utf-8")
	font = ImageFont.truetype(font, size, encoding="unic")
	img.text(pos, text, font=font, fill=color)

def create_control(text, size, bg_color, textcolor):
	for i in text:
		img = Image.new('RGB', size, bg_color)
		imgDrawer = ImageDraw.Draw(img)
		inp_text(imgDrawer, (0, 0), i, "PTMono.ttc", 10, textcolor)
		img.save(i+".png")

#create_control(alg, (31, 11), bg_color, cur_color)

img = Image.new('RGB', im_size, bg_color)
imgDrawer = ImageDraw.Draw(img)

n = len(naming)
dy = y2_naming - y1_naming
d = dy/(n)
j = y1_naming + (d/2)

for i in naming:
	inp_text(imgDrawer, (x_naming, j), i, "PTMono.ttc", 10, naming_color)
	j = j+d

j = y1_naming + (d/2)
for i in alg:
	inp_text(imgDrawer, (x_alg, j), i, "PTMono.ttc", 10, alg_color)
	imgDrawer.rectangle((x_cur, j, x_cur+30, j+10), outline=(255,255,255))
#	imgDrawer.rectangle((x_alg, j, x_alg+30, j+10), outline=(255,255,255))
	j = j+d


imgDrawer.rectangle((270, 100, 310, 110), outline=(255,255,255))

#inp_text(imgDrawer, (270, 100), "БЛОКИР.", "PTMono.ttc", 10, (255, 0, 0))
#inp_text(imgDrawer, (270, 120), "РАЗБЛ.", "PTMono.ttc", 10, (0, 255, 0))
#imgDrawer.rectangle((270, 120, 310, 130), outline=(255,255,255))

inp_text(imgDrawer, (x_alg, 0), "условие", "PTMono.ttc", 10, alg_color)
inp_text(imgDrawer, (x_cur, 0), "факт.", "PTMono.ttc", 10, cur_color)

imgDrawer.line([x_cur-5,y1_naming+5,x_cur-5,y2_naming+5], fill=(255,255,255))
imgDrawer.line([x_alg-5,y1_naming+5,x_alg-5,y2_naming+5], fill=(255,255,255))
imgDrawer.line([x_alg+40,y1_naming+5,x_alg+40,y2_naming+5], fill=(255,255,255))

img.save("img.png")