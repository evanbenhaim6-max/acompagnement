import sys, math
from PIL import Image, ImageDraw, ImageFont
F='/tmp/claude-0/-home-user-acompagnement/add46904-4241-51c5-837a-9d7b561d32e5/scratchpad/fonts/'
OUT='/home/user/acompagnement/logo_nasely/'
CH=(140,28,47); CREAM=(248,241,233); LEAF=(62,95,58); WHITE=(255,255,255)
SS=4

def bez(p0,p1,p2,n=60):
    return [((1-t)**2*p0[0]+2*(1-t)*t*p1[0]+t*t*p2[0],(1-t)**2*p0[1]+2*(1-t)*t*p1[1]+t*t*p2[1]) for t in [i/n for i in range(n+1)]]

def icon(size, fg=CH, leaf=LEAF, hl=True):
    """cerise + croissant de lune, fond transparent"""
    S=size*SS; im=Image.new('RGBA',(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
    r=S*0.185; cy=S*0.68; lx=S*0.285; rx=S*0.715; top=(S*0.53,S*0.14)
    w=int(S*0.028)
    # tiges
    d.line(bez((lx+r*0.1,cy-r*0.92),(S*0.34,S*0.32),top),fill=leaf,width=w,joint='curve')
    d.line(bez((rx-r*0.25,cy-r*0.93),(S*0.66,S*0.36),top),fill=leaf,width=w,joint='curve')
    # feuille
    lf=Image.new('RGBA',(S,S),(0,0,0,0)); ld=ImageDraw.Draw(lf)
    ld.ellipse([S*0.53,S*0.08,S*0.80,S*0.19],fill=leaf)
    lf=lf.rotate(-18,center=(S*0.53,S*0.14),resample=Image.BICUBIC); im.alpha_composite(lf)
    d=ImageDraw.Draw(im)
    # cerise gauche
    d.ellipse([lx-r,cy-r,lx+r,cy+r],fill=fg)
    if hl: d.ellipse([lx-r*0.55,cy-r*0.6,lx-r*0.15,cy-r*0.2],fill=(255,255,255,70))
    # croissant de lune (droite)
    m=Image.new('L',(S,S),0); md=ImageDraw.Draw(m)
    md.ellipse([rx-r,cy-r,rx+r,cy+r],fill=255)
    md.ellipse([rx-r*0.45,cy-r*1.15,rx+r*1.35,cy+r*0.65],fill=0)
    moon=Image.new('RGBA',(S,S),(*fg,255)); im.paste(moon,(0,0),m)
    # petite étoile
    sx,sy,sr=rx+r*0.75,cy-r*0.95,r*0.12
    pts=[(sx+math.cos(a)*(sr if k%2==0 else sr*0.4),sy+math.sin(a)*(sr if k%2==0 else sr*0.4)) for k,a in enumerate([i*math.pi/4-math.pi/2 for i in range(8)])]
    d.polygon(pts,fill=fg)
    return im.resize((size,size),Image.LANCZOS)

def text_img(txt,font,size,color,track=0):
    f=ImageFont.truetype(font,size*SS)
    tmp=ImageDraw.Draw(Image.new('RGBA',(1,1)))
    ws=[tmp.textlength(c,font=f) for c in txt]; tw=int(sum(ws)+track*SS*(len(txt)-1))+10
    a,dd=f.getmetrics(); im=Image.new('RGBA',(tw,a+dd),(0,0,0,0)); dr=ImageDraw.Draw(im); x=0
    for c,w in zip(txt,ws): dr.text((x,0),c,font=f,fill=color); x+=w+track*SS
    bb=im.getbbox(); im=im.crop(bb)
    return im.resize((max(1,im.width//SS),max(1,im.height//SS)),Image.LANCZOS)

def horizontal(fg,bg,name):
    W,H=2000,640
    im=Image.new('RGBA',(W,H),bg)
    ic=icon(520,fg,LEAF if fg==CH else (255,255,255),hl=(fg==CH)); im.alpha_composite(ic,(60,50))
    t=text_img('Nasely',F+'Cormorant-600.ttf',300,fg); im.alpha_composite(t,(620,150))
    tg=text_img('EXTRAIT DE CERISE GRIOTTE',F+'Montserrat-500.ttf',44,fg,track=9)
    im.alpha_composite(tg,(632,150+t.height+50))
    im=im.crop(im.getbbox() if bg[3]==0 else (0,0,W,H))
    im.save(OUT+name)

def square(fg,bg,name,with_name=True,size=1080):
    im=Image.new('RGBA',(size,size),bg)
    if with_name:
        ic=icon(620,fg,LEAF if fg==CH else (255,255,255),hl=(fg==CH)); im.alpha_composite(ic,((size-620)//2,70))
        t=text_img('Nasely',F+'Cormorant-600.ttf',210,fg); im.alpha_composite(t,((size-t.width)//2,680))
        tg=text_img('EXTRAIT DE CERISE GRIOTTE',F+'Montserrat-500.ttf',30,fg,track=7); im.alpha_composite(tg,((size-tg.width)//2,700+t.height+30))
    else:
        ic=icon(760,fg,LEAF if fg==CH else (255,255,255),hl=(fg==CH)); im.alpha_composite(ic,((size-760)//2,(size-760)//2+20))
    im.convert('RGB').save(OUT+name,quality=95) if name.endswith('.jpg') else im.save(OUT+name)

horizontal(CH,(0,0,0,0),'nasely_logo_horizontal_transparent.png')
horizontal(WHITE,(0,0,0,0),'nasely_logo_horizontal_blanc_transparent.png')
horizontal(CH,(*CREAM,255),'nasely_logo_horizontal_creme.png')
square(CH,(*CREAM,255),'nasely_photo_profil_icone.png',with_name=False)
square(WHITE,(*CH,255),'nasely_photo_profil_icone_rouge.png',with_name=False)
square(CH,(*CREAM,255),'nasely_logo_carre_creme.png')
square(WHITE,(*CH,255),'nasely_logo_carre_rouge.png')
icon(1024).save(OUT+'nasely_icone_transparente.png')
print('ok')
