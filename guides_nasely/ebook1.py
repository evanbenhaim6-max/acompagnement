import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-acompagnement/add46904-4241-51c5-837a-9d7b561d32e5/scratchpad/scripts')
from ebook_common import *
T='Mieux dormir en 14 jours'
P=[]
P.append(cover2('14','Programme guidé · 14 jours','Mieux dormir<br><em>en 14 jours</em>','Une méthode simple, jour après jour, pour retrouver des nuits plus continues et des matins plus clairs.','Guide offert'))

P.append(f'''<div class="page"><div class="kicker">Bienvenue</div><h2>Tes nuits méritent <em>mieux</em>.</h2><div class="rule"></div>
<p class="lead">Si tu tiens ce guide, c'est probablement que tes nuits ne ressemblent plus à ce qu'elles étaient. Endormissement long, réveil à 3 h du matin, réveil fatigué… Tu n'es pas seule : c'est l'une des plaintes les plus fréquentes après 40 ans.</p>
<p>Ce programme de 14 jours rassemble des habitudes simples, recommandées par les spécialistes du sommeil. Chaque jour, une seule action. Pas de bouleversement, pas de règles impossibles. Juste de petits réglages qui, mis bout à bout, aident ton corps à retrouver son rythme naturel.</p>
<div class="box"><h3 style="margin-top:0">Comment utiliser ce guide</h3>
<ul class="ch"><li><b>Lis la page du jour le matin</b> : l'action est pensée pour être faite dans la journée ou le soir même.</li>
<li><b>Garde les acquis</b> : chaque nouvelle habitude s'ajoute aux précédentes.</li>
<li><b>Remplis ton journal de sommeil</b> (page 11) chaque matin, en 1 minute.</li>
<li><b>Sois indulgente</b> : une mauvaise nuit ne fait pas échouer le programme. C'est la régularité qui compte.</li></ul></div>
<h3>Ce que tu vas trouver</h3>
<div class="toc"><a><span>Comprendre ton sommeil</span><span>3</span></a><a><span>Les 5 piliers d'une bonne nuit</span><span>4</span></a><a><span>Semaine 1 : poser les bases</span><span>5</span></a><a><span>Semaine 2 : consolider</span><span>7</span></a><a><span>Ton rituel du soir en 30 minutes</span><span>9</span></a><a><span>Que faire quand tu te réveilles à 3 h ?</span><span>10</span></a><a><span>Ton journal de sommeil</span><span>11</span></a><a><span>Bilan du jour 14</span><span>12</span></a></div>
<p class="small" style="margin-top:14px">Ce guide propose des conseils d'hygiène de vie et ne remplace pas un avis médical. Si tes troubles du sommeil durent depuis plus de 3 mois, s'accompagnent de ronflements importants, de pauses respiratoires ou d'une grande fatigue dans la journée, parles-en à ton médecin.</p>
{foot(T,2)}</div>''')

P.append(f'''<div class="page"><div class="kicker">Les bases</div><h2>Comprendre <em>ton sommeil</em></h2><div class="rule"></div>
<p class="lead">Une nuit n'est pas un long bloc uniforme. C'est une succession de cycles d'environ 90 minutes, qui se répètent 4 à 6 fois.</p>
<div class="grid3" style="margin:14px 0">
<div class="card"><div class="n">1</div><h3>Sommeil léger</h3><p class="small">La transition. On se réveille facilement, on entend encore les bruits autour de soi.</p></div>
<div class="card"><div class="n">2</div><h3>Sommeil profond</h3><p class="small">Le plus réparateur. Le corps récupère et le cerveau fait son « ménage ». Il est surtout présent en début de nuit.</p></div>
<div class="card"><div class="n">3</div><h3>Sommeil paradoxal</h3><p class="small">La phase des rêves. Elle s'allonge en fin de nuit et participe à la mémoire et aux émotions.</p></div></div>
<h3>Pourquoi se réveille-t-on vers 3 h du matin ?</h3>
<p>Vers le milieu de la nuit, le sommeil devient naturellement plus léger : les phases de sommeil profond se raréfient et l'on passe plus souvent près de l'éveil. Si, à ce moment-là, le corps est en alerte (stress, pensées qui tournent, chambre trop chaude, repas tardif, alcool, besoin d'aller aux toilettes…), le micro-réveil devient un vrai réveil.</p>
<p>Avec l'âge, la production de <b>mélatonine</b>, l'hormone qui signale au corps que c'est la nuit, a aussi tendance à diminuer. Le sommeil devient plus fragile, plus sensible aux perturbations.</p>
<div class="box dark"><h3 style="margin-top:0">La bonne nouvelle</h3><p style="margin:0">Ton horloge interne se règle chaque jour grâce à des signaux simples : la lumière, les horaires, la température, les repas. En ajustant ces signaux, tu peux aider ton corps à retrouver un sommeil plus profond et plus continu. C'est exactement l'objectif des 14 prochains jours.</p></div>
<h3>Ce qu'il faut retenir</h3>
<ul class="ch"><li>Le sommeil profond se joue surtout en <b>début de nuit</b> : bien préparer l'endormissement est essentiel.</li><li>Un réveil nocturne bref est <b>normal</b>. Le but est de se rendormir facilement.</li><li>La <b>régularité</b> compte plus que la durée.</li></ul>
{foot(T,3)}</div>''')

P.append(f'''<div class="page"><div class="kicker">La méthode</div><h2>Les 5 piliers <em>d'une bonne nuit</em></h2><div class="rule"></div>
<p class="lead">Tout le programme repose sur ces cinq leviers. Tu vas les activer un par un.</p>
<div class="tip" style="margin:14px 0"><b class="ic">1</b><div><h3 style="margin:0 0 3px">La lumière</h3><p>La lumière du matin règle ton horloge interne pour la journée entière. La lumière forte du soir (écrans, plafonniers) retarde la sécrétion de mélatonine.</p></div></div>
<div class="tip" style="margin:14px 0"><b class="ic">2</b><div><h3 style="margin:0 0 3px">La régularité</h3><p>Se lever à la même heure chaque jour, week-end compris, est l'habitude la plus efficace pour stabiliser le sommeil.</p></div></div>
<div class="tip" style="margin:14px 0"><b class="ic">3</b><div><h3 style="margin:0 0 3px">La température</h3><p>Pour s'endormir, le corps doit baisser légèrement sa température. Une chambre fraîche, autour de 17 à 19 °C, l'y aide.</p></div></div>
<div class="tip" style="margin:14px 0"><b class="ic">4</b><div><h3 style="margin:0 0 3px">Le calme mental</h3><p>Les pensées qui tournent sont la première cause des réveils prolongés. Il faut les « déposer » avant d'aller au lit.</p></div></div>
<div class="tip" style="margin:14px 0"><b class="ic">5</b><div><h3 style="margin:0 0 3px">L'assiette et la tasse</h3><p>Caféine, alcool, dîner trop lourd ou trop tardif : ce que l'on consomme dans la journée se ressent la nuit. Notre guide de recettes t'accompagne sur ce point.</p></div></div>
<div class="box"><b>À savoir :</b> la caféine reste active plusieurs heures dans l'organisme. Un café à 16 h peut encore agir au moment du coucher. Et si l'alcool aide parfois à s'endormir, il fragmente la seconde partie de la nuit.</div>
{foot(T,4)}</div>''')

W1=[("Fixe ton heure de lever","Choisis une heure de lever que tu peux tenir 7 jours sur 7, et programme ton réveil. C'est ton ancre : on ne la touche plus, même après une mauvaise nuit.","Action : note ton heure de lever ici → ____ h ____"),
("La lumière du matin","Dans l'heure qui suit ton lever, expose-toi 15 à 20 minutes à la lumière du jour : balcon, fenêtre ouverte, petite marche.","Action : café ou petit-déjeuner près d'une fenêtre."),
("Le couvre-feu caféine","Plus de café, thé, cola ni boisson énergisante après 14 h. Remplace-les par une infusion ou de l'eau citronnée.","Action : prépare une infusion pour l'après-midi."),
("La chambre fraîche et sombre","Baisse le chauffage de la chambre (17-19 °C), occulte la lumière, éloigne les sources de bruit et de lumière (veilles, réveil lumineux).","Action : aère la chambre 10 minutes avant le coucher."),
("Le couvre-feu des écrans","Coupe téléphone, tablette et télévision 45 minutes avant le coucher. Si c'est difficile, commence par 20 minutes.","Action : laisse ton téléphone en charge hors de la chambre."),
("Dîner plus tôt, plus léger","Termine ton dîner 2 à 3 heures avant le coucher. Privilégie légumes, protéines légères et féculents complets ; limite le gras et l'alcool.","Action : choisis une recette du guide Nasely."),
("Ton premier rituel du soir","Assemble les habitudes des jours précédents en un rituel de 30 minutes (voir page 9). Le même chaque soir, dans le même ordre.","Action : écris ton rituel sur un post-it près du lit.")]
W2=[("Le lit, c'est pour dormir","Ne travaille pas, ne regarde pas de séries et ne fais pas défiler ton téléphone au lit. Ton cerveau doit associer le lit au sommeil.","Action : déplace la lecture « active » dans un fauteuil."),
("Vider sa tête","En début de soirée, écris en 5 minutes tout ce qui te préoccupe et ce que tu dois faire demain. Ferme le carnet : c'est noté, ton cerveau peut lâcher prise.","Action : garde un carnet dédié sur ta table de nuit."),
("La respiration 4-7-8","Inspire par le nez 4 secondes, retiens 7 secondes, expire lentement par la bouche 8 secondes. Répète 4 fois au lit.","Action : pratique-la ce soir, puis à chaque réveil nocturne."),
("Bouger, mais au bon moment","30 minutes d'activité physique dans la journée (marche rapide, vélo, natation) favorisent un sommeil plus profond. Évite le sport intense dans les 3 heures avant le coucher.","Action : une marche de 30 minutes aujourd'hui."),
("Le bain tiède du soir","Une douche ou un bain tiède 1 h à 1 h 30 avant le coucher aide le corps à amorcer la baisse de température qui précède l'endormissement.","Action : intègre-le à ton rituel."),
("Gérer la sieste","Si tu as besoin d'une sieste, limite-la à 20 minutes, avant 15 h. Une sieste longue ou tardive « vole » du sommeil à la nuit.","Action : programme une alarme de 20 minutes."),
("Ton bilan","Relis ton journal de sommeil. Qu'est-ce qui a changé ? Quelles habitudes ont le plus aidé ? Garde-les : ce sont tes nouvelles fondations.","Action : complète la page « Bilan du jour 14 ».")]
def week(title,kick,items,start,n,intro):
    days=''.join(f'<div class="day"><div class="d"><small>JOUR</small><b>{start+i}</b></div><div><h4>{a}</h4><p>{b}</p><div class="act">{c}</div></div></div>' for i,(a,b,c) in enumerate(items))
    return days
w1=week('','',W1,1,5,'')
w2=week('','',W2,8,7,'')
d1=w1.split('<div class="day">'); d2=w2.split('<div class="day">')
def part(lst,a,b): return ''.join('<div class="day">'+x for x in lst[1:][a:b])
P.append(f'''<div class="page"><div class="kicker">Semaine 1</div><h2>Poser <em>les bases</em></h2><div class="rule"></div>
<p class="lead">Cette semaine, on règle l'horloge interne : lumière, horaires, caféine et environnement.</p>{part(d1,0,4)}{foot(T,5)}</div>''')
P.append(f'''<div class="page"><div class="kicker">Semaine 1 · suite</div><h2>Poser <em>les bases</em></h2><div class="rule"></div>{part(d1,4,7)}
<div class="box"><b>Fin de semaine 1 :</b> ne t'inquiète pas si tes nuits ne sont pas encore parfaites. Ton horloge interne a besoin de quelques jours de régularité pour se recaler. Continue : la semaine 2 est souvent celle où l'on sent la différence.</div>{foot(T,6)}</div>''')
P.append(f'''<div class="page"><div class="kicker">Semaine 2</div><h2>Consolider <em>et apaiser</em></h2><div class="rule"></div>
<p class="lead">Cette semaine, on travaille le calme mental et l'association « lit = sommeil ».</p>{part(d2,0,4)}{foot(T,7)}</div>''')
P.append(f'''<div class="page"><div class="kicker">Semaine 2 · suite</div><h2>Consolider <em>et apaiser</em></h2><div class="rule"></div>{part(d2,4,7)}
<div class="box dark"><h3 style="margin-top:0">Bravo !</h3><p style="margin:0">Tu as mis en place, en deux semaines, les habitudes que les spécialistes recommandent en premier. Garde-les dans la durée : c'est leur régularité qui fait la différence sur plusieurs mois.</p></div>{foot(T,8)}</div>''')

steps=[("−2 h 30","Fin du dîner","Repas léger, sans alcool. Une infusion si tu le souhaites."),("−1 h 30","Douche ou bain tiède","Pour amorcer la baisse de température du corps."),("−1 h","Vider sa tête","5 minutes de carnet : soucis, tâches de demain, 3 choses positives de la journée."),("−45 min","Couvre-feu des écrans","Téléphone en charge hors de la chambre. Lumières tamisées dans la maison."),("−30 min","Moment calme","Lecture papier, musique douce, étirements légers. Tes 2 gélules Nasely avec un verre d'eau."),("−10 min","Chambre prête","Fraîche, sombre, silencieuse. Pyjama confortable."),("Au lit","Respiration 4-7-8","4 cycles, puis laisse venir le sommeil, sans le forcer.")]
rows=''.join(f'<div class="day" style="grid-template-columns:80px 1fr"><div class="d" style="font-weight:800;font-size:10.5pt;padding:9px 0">{a}</div><div><h4>{b}</h4><p>{c}</p></div></div>' for a,b,c in steps)
P.append(f'''<div class="page"><div class="kicker">Chaque soir</div><h2>Ton rituel du soir <em>en 30 minutes</em></h2><div class="rule"></div>
<p class="lead">Le même enchaînement, chaque soir, envoie à ton cerveau un signal clair : la journée est finie. Adapte les horaires à ton heure de coucher.</p>{rows}{foot(T,9)}</div>''')

P.append(f'''<div class="page"><div class="kicker">La nuit</div><h2>Que faire quand tu te réveilles <em>à 3 h</em> ?</h2><div class="rule"></div>
<p class="lead">Le pire réflexe : regarder l'heure, puis son téléphone, puis calculer combien de temps il reste à dormir. Voici quoi faire à la place.</p>
<div class="tip" style="margin:12px 0"><b class="ic">1</b><div><h3 style="margin:0 0 3px">Ne regarde pas l'heure</h3><p>Tourne ton réveil vers le mur. Connaître l'heure déclenche le stress du « je ne vais jamais me rendormir ».</p></div></div>
<div class="tip" style="margin:12px 0"><b class="ic">2</b><div><h3 style="margin:0 0 3px">Respire</h3><p>4 cycles de respiration 4-7-8, puis une respiration lente et naturelle. Relâche les épaules, la mâchoire, les mains.</p></div></div>
<div class="tip" style="margin:12px 0"><b class="ic">3</b><div><h3 style="margin:0 0 3px">Occupe ton esprit, sans le stimuler</h3><p>Choisis un mot (par exemple « CERISE »). Pour chaque lettre, imagine tranquillement des objets qui commencent par cette lettre : C… cahier, citron, colline… Ce petit jeu calme les pensées qui tournent.</p></div></div>
<div class="tip" style="margin:12px 0"><b class="ic">4</b><div><h3 style="margin:0 0 3px">Si rien ne vient après 20 minutes environ, lève-toi</h3><p>Va dans une autre pièce, lumière tamisée, et fais une activité calme (lecture papier, tricot, musique douce). Reviens au lit dès que tu sens la somnolence. Cette règle aide ton cerveau à ne plus associer le lit à l'éveil.</p></div></div>
<div class="box"><b>À éviter :</b> le téléphone (lumière + stimulation), manger, fumer, regarder la télévision, ou rester au lit à lutter pendant des heures.</div>
{foot(T,10)}</div>''')

days=''.join(f'<tr><td>J{i}</td>'+'<td></td>'*6+'</tr>' for i in range(1,15))
P.append(f'''<div class="page"><div class="kicker">Ton suivi</div><h2>Journal <em>de sommeil</em></h2><div class="rule"></div>
<p>Chaque matin, en 1 minute. Note tes estimations sans regarder l'heure la nuit, l'idée est de voir la tendance, pas d'être précise à la minute.</p>
<table><tr><th>Jour</th><th>Coucher</th><th>Lever</th><th>Réveils<br>la nuit</th><th>Qualité<br>(1 à 5)</th><th>Forme au<br>réveil (1 à 5)</th><th>Remarque</th></tr>{days}</table>
{foot(T,11)}</div>''')

P.append(f'''<div class="page"><div class="kicker">Jour 14</div><h2>Ton <em>bilan</em></h2><div class="rule"></div>
<div class="grid2"><div class="box line"><h3 style="margin-top:0">Ce qui a changé</h3><p class="small">Endormissement, réveils, forme au réveil, humeur…</p><div style="height:46mm"></div></div>
<div class="box line"><h3 style="margin-top:0">Mes 3 habitudes clés</h3><p class="small">Celles qui t'ont le plus aidée, et que tu gardes.</p><div style="height:46mm"></div></div></div>
<h3>Et maintenant ?</h3>
<ul class="ch"><li><b>Garde ton heure de lever fixe</b>, c'est la base de tout.</li><li><b>Recommence le programme</b> à tout moment si tes nuits se dégradent (voyage, période de stress, changement d'heure).</li><li><b>Prends soin de ton assiette</b> avec notre guide « Recettes du soir pour mieux dormir ».</li><li><b>Sois patiente :</b> un sommeil qui a été perturbé pendant des années peut demander plusieurs semaines pour se stabiliser.</li></ul>
<div class="box"><h3 style="margin-top:0">Quand consulter ?</h3><p style="margin:0">Parles-en à ton médecin si tes difficultés persistent malgré ces habitudes, si elles durent depuis plus de 3 mois, en cas de ronflements forts, de pauses respiratoires pendant le sommeil, de jambes agitées le soir, ou si la fatigue retentit fortement sur ta journée. Ne modifie jamais un traitement sans son avis.</p></div>
{foot(T,12)}</div>''')

P.append(back2('Belles nuits <em>à toi</em>.',"Merci de faire confiance à Nasely. Une question ? Notre équipe est là pour toi.","Ce guide est fourni à titre informatif et ne remplace pas une consultation médicale. Nasely est un complément alimentaire : il ne remplace pas une alimentation variée et équilibrée ni un mode de vie sain. © Nasely. Reproduction interdite."))
open(sys.argv[1],'w').write(doc('Mieux dormir en 14 jours · Nasely',P))
