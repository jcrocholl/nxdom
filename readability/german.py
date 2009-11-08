VOWELS = 'aeiouy'
TRIPLE_SCORES = {}

for triple in """
^abg ^ang ^aufg ^ausg ^ba ^be ^bei ^bi ^bu ^da ^de ^di ^du ^eing ^fa
^fe ^fi ^fo ^fu ^ga ^ge ^ha ^hau ^he ^hei ^hi ^ho ^ka ^ke ^ki ^ko ^ku
^la ^le ^lo ^ma ^me ^mi ^mo ^na ^pa ^po ^pro ^ra ^re ^rei ^sa ^scha
^schu ^se ^si ^so ^sta ^ste ^ta ^te ^to ^tra ^ueb ^umg ^un ^unb ^ung
^unt ^ve ^vo ^wa ^we ^wei ^wi ^wie ^wo ^wu ^ze ^zi ^zu abe abge ache
achte ade aege aehi aende aenge aessi aft$ afte age ahre ale ali alle
alte ame amme and$ ande ange ani anke ara arbei are arte asse aste ate
ati atio atte aufe aufge ausge bel ben bend ber bes che$ chem chen
chend cher ches chte$ chten chter chtet chtig cken ckend den der ebe
eche ecke ede edi efa efue ege eha ehe ehre eibe eiche eide eife eige
eile eine einge eise eiste eit$ eite eko el$ ela ele eli elle eln$
elnde els$ elt$ elte em$ eme en$ ena end$ ende ene enge ens$ ente er$
era erau erbe ere erei erfa erge erha eri erke erle erli ern$ ernde
erre ers$ ert$ erte eru erwa es$ esa eschae ese esse est$ esta este
et$ ete ette ewa ewe ewi fen fend ften ge$ geb gef geh gel gem gen
gend ger ges gesch gew gkeit gung hen hend her hren ich$ iche ichste
ichte ichti icke ide iebe iede iefe iege ien$ iere iert$ ierte ieru
ig$ ige igkei igste igte igu ik$ imme in$ ina inde ine inge inne inte
ion$ ione isch$ ische isie isse iste itae itte itze ive komm le$ len
lend ler lig lis lit lle$ llen llend ller llig lte$ lten lter mmen
nde$ ndem nden nder ndes ndet ndig ne$ nem nen ner nes ngen ngend nger
nnen obe oche ode oge oli olle omme orge ose osse ote rat rbeit re$
rem ren rend rer res rig rin risch rlich rte$ rtem rten rter rtes
rtest rtet rtig rung samm sche$ schen scher sches se$ sen send ser
sest sier siert sse$ ssen ssend ssig ste$ stem sten ster stes te$ tem
ten tend ter tes test tet tig tion tisch tten tzend uebe uecke uege
uge unbe unde une ung$ unge unte urue usa ver verb verd verf verh verk
verl vers verw wied zug zur zus
""".split(): TRIPLE_SCORES[triple] = 20

for triple in """
^abs ^abw ^arb ^bau ^bo ^bue ^die ^do ^einz ^entw ^erf ^erw ^flu ^frei
^fue ^gei ^glei ^go ^gro ^gru ^gu ^hu ^ind ^int ^ja ^ju ^kla ^klei
^kue ^lei ^li ^lie ^lu ^mu ^ne ^neu ^nie ^no ^pe ^pla ^ri ^ro ^ru ^rue
^schi ^schla ^schwa ^schwe ^see ^spa ^spe ^sti ^stra ^stu ^su ^tau ^ti
^tie ^tro ^tu ^unv ^vie ^wae ^wue ^za ^zei ^zwei achge acke aeche
aechti aendi aere aesse aete aetze aeufe aeume afe affe ag$ agte ahle
ahme al$ altu ami ana ane ang$ anla anne annte ante api appe ar$ ari
arste arti asche ase at$ ato atu atze aube ause aute auto be$ bed bef
beh berl bers besch best bet betr bew bund chkeit chste$ chsten chstes
chtend chtes cke$ de$ dem dend det dig durchg ebra ebu echse echte
eckte eda efae efe efo ega egge egie egte ehei ehme eili ein$ eina
eini eisse eitu elde elei ellte ellu ema emei emi emo enbe endste enha
enke enne eno enste enswe enta erae erba erde erfe erfo erhae erie
erla erma ermi ernd$ erne ero ersa erse ersi ersta erste erti ertra
erue erve erwe erwi erzi eschi esi esti esu eta eti etrie etze etzte
eute ewo fe$ fer ffen fte$ fter ftest ged geg gest get gier glich
gste$ gstem gsten gster gstes gte$ gten gter gtes halt hig hin hlen
hlend hmen hrend ichkei icht$ iehe iele ierst$ iese iesse iete iffe
ika ike ilde ili ille illi indu ini inie irtscha is$ ischste isti ita
ite iti izie kap kat ktion leb leg les llung log ltem ltend ltes ltest
ltet ltig lung mat me$ men ment mer mil min mmend mmeng nal nat ndend
ndlich ndung nge$ ngeb ngef ngeh ngel nges nhaft nier niert nig nisch
nist nken nkend nlag nlos nnend nswert nte$ nten nter ocke odu offe
ogra ole olo ona onde one onne or$ ora orde ore ori orte os$ osi oste
oto otte pit pol rad reg richt rinn rnde$ rnden rnder rndes rueckg
schaeft schem ses sser sses stand stellt stet stig stisch taet tal tel
tier tik tiv tor tte$ tter ttert ttet tung tze$ tzen uche ucke ude
ueche uechti ueckge uehre uelle uende uesse ueste uete uette ufe ula
ulie ume umge umme una unke uppe urchge ure us$ uss$ uste ute verg
verm verr versch verst vertr verz vor vorg wass wid zier
""".split(): TRIPLE_SCORES[triple] = 19

for triple in """
^ab ^abl ^abr ^abst ^abz ^akt ^all ^an ^anf ^anl ^anz ^aus ^ausl ^auss
^aut ^bea ^bra ^eig ^einf ^el ^entg ^entl ^er ^erh ^erl ^exp ^fei ^fra
^gra ^hoe ^id ^kae ^kau ^kra ^kre ^lae ^ni ^ob ^off ^prae ^prei ^pri
^pu ^rau ^schae ^schau ^sche ^schei ^schie ^sei ^sie ^spi ^spie ^spo
^staa ^stei ^steue ^sue ^sy ^tei ^tre ^tri ^unr ^uns ^vi ^zie ^zue
^zwi achse acht$ aede aefte aefti aelle aelli aempfe aerte aet$ aeti
aette aeuse ahlu ake akte ala all$ alti an$ anda andlu anti anze apie
artei aschi assu ata atz$ auche aus$ beg bek bem berg berh berr biet
bil bild bracht bung chern chlich chstem chster chtest chtigst chtigt
chtlich cker ckte$ ckten ckter dent derg dern des dit dukt ebi ebie
ebo ebte echne effe egra egu ehle eho ehoe ehrte eich$ eichte eidi
eien$ eihe eilte eis$ eistu eka eke eku elha elie elli elnd$ elo elu
emae enba enhei eni enlo enscha ent$ entge enti entie entwi enu enue
enve epa erbi erbo erfue erga erhe erhei erko erlei erlo erna erra
errei erri erscha erso erst$ ersu ertei ervo erwei erze erzie escha
eschla escho eso estae esto euge evo ewae ewu ezi ezo fahr fall fert
ffend fin form fried ftes ftet ftig gang gek gelt getr gez gramm graph
gtem gtest hand he$ hint hmend hrer hrung hung ickte iene ier$ ieri
ifi ifte ildu ile ilie imi inau indi ing$ inke inni inse iona ionie
isa ise itio ivi kal kan kind kons ktiv lag lass lat lder ldet lhaft
lich lier liert list liz lnde$ lnden lnder lndes ltung macht maess met
mitt mmer nachg nand ndern ndert ndustr neb nend ngesch ngest ngew
nglich ngslos nheit nied nis nnig ntern oege oerde oere oermi oerte
ohle olge ollste oma ome omi on$ oni onie onze oppe orga orie orma oze
par part ppen prod ral rausg rbar rder rdig recht rei$ rein reit rfahr
rgan rger rhaft rhalt ris rmig rstell rteil ruf sat schend schin
schlag sem setz setzt sond staend stell stend tern tiert tlich trag
trieb ttel tzes tzung ube uch$ uchte uechte ueckte uehle uehrte uendi
uerdi uerge ueti ug$ uktio ule um$ ungsa ungsbe ungsge ungslo ungsvo
uni unve ur$ usi usti ustrie utte verbr vern verschl vert wand wechs
wegg weit werb wirtsch wiss wund yste zahl ziert zog zwisch
""".split(): TRIPLE_SCORES[triple] = 18

for triple in """
^abf ^absch ^alt ^am ^anb ^anr ^anst ^ant ^aufr ^aufw ^ausr ^blu ^boe
^bre ^bru ^cha ^co ^drei ^due ^eh ^eins ^eis ^empf ^erk ^erm ^err ^ers
^erst ^erz ^ex ^fla ^fre ^frie ^gi ^gre ^hae ^inf ^inn ^kna ^koe ^kri
^krie ^lau ^mae ^mue ^nae ^pi ^pra ^pre ^saeu ^sau ^schme ^schue
^schwae ^schwei ^schwi ^sto ^stue ^tae ^und ^unf ^unw ^zo ^zwa ^zwe
abi able abri abwe abzu ackte aedi aegli aehle aehri aehru aelte aelti
aendle aengli aenke aerme aese aftli akti aktie aktio alo alt$ ama
amm$ amste andte anzu arbe arie arke arre as$ assi asste auende auf$
auge auli ausse begr bens berm bern bersch berst bert bertr berw bez
bgew big blich bot brik chert chnet chtem chtung chung ckelt ckig
cktes dat del delt dert dlich drig dung eba ebli ebue echni echt$ egi
ehae eichne eichste eidu eilu eime einhei einze eiti ekla ekte elau
ellscha elst$ empe emue enau endu enfa enla ensche ensi entli entra
enze eraeu erbre erda erdu erfae erho erhoe erka erkau erlae erlie
erme ermoe ernse erschie erschla erstae ertre erwae erzei esche espa
espe esprae estie estri eto etra etre etz$ euchte ewei expo eza ezei
ferns ffe$ fiz ftlich fuehr gebr geist geng gens gent geschm gesp gig
gisch gtet herv hing hle$ hnen hnend hoer hre$ hrig hrlich hrten iali
ichtli ichtu idri ieb$ iel$ igt$ ima ime indli inei ingli inha ippe
ire ismu ist$ itie itu itzte ium$ iva kart kass ken ker kont konz kost
kred kul lad land last lauf ldung legt leit lem lisch lles llte$ llten
los mal man mass mend mess misch mit mme$ mmelt mmert mod mon nanz
ndel ndelt nderg nderl nform ngebr ngem nne$ nner nomm nterg nterh
nterl ntest ntgeg ntier ntiert nzen obi oegli oepfe oese oeste oete
ogi oka olte olu ono onta ope opfe orbe orme orste ort$ ortge ot$ oti
ozia pass pfend pier ppe$ priv raet rarb rben rden rechn red reich
rfen rgeh rgew rier riert rke$ rken rmat rmen rnehm rrend rsten rsuch
rtrag rtret rtschaft rwalt rzig seh sein sel sellsch sern sger sich
sik sit sitz smus sonn soz ssion sslich ssung steh stung such sung tag
teil ters tis tret ttelt ttend ttern tternd tur tzig tzte$ tzten uehe
uehru uere uessi uetze uhe unau undi ungsve unkte usse ut$ utze ven
verbl verdr verp vis weg wett zentr zial
""".split(): TRIPLE_SCORES[triple] = 17

for triple in """
^abb ^and ^anh ^anm ^ann ^ans ^at ^auff ^aufh ^aufl ^aufz ^ausb ^ausf
^ausst ^bli ^dra ^dre ^dru ^ehr ^einh ^eink ^einl ^einw ^entz ^erb
^erd ^erg ^ern ^fae ^feue ^flie ^flue ^fro ^frue ^gae ^gla ^glue ^grue
^gue ^hue ^imp ^kei ^kli ^mei ^nu ^qua ^sae ^schle ^schli ^schlu
^schma ^schne ^scho ^schoe ^schrei ^spra ^spre ^stae ^stau ^stoe
^strei ^tru ^tue ^umr ^ums ^umw ^unm ^va abbe abo ach$ ad$ adi aechte
aehe aemme aene aengte aesi aeste aeube ahe ahl$ ahlte ahne alls$
allte am$ andi ank$ ann$ anspo ansta antwo anzie arge arme aro asie
assie asti auen$ aum$ ausei ausga ausha ausla aut$ befr beig belt berb
berf berz bestr bev bgest boers bte$ bter chelt chig chnung chsen
cktem derl dest deut dier diert digt earbei echnu edie edu eere efi
efu ehnte ehr$ eil$ einde einfa einsa ekti ekto ekue elae elfe elge
eloe emde empfi endi enko enku ensa enwa enz$ eque erbli erbu erdie
erdo ereie erfi ergi eria erk$ erlau erlu ermae ernae erni eroe erstue
ertrae ertu ervie erwue erzae erzu eschei eschrie eschue esie essi
estue etei etro etu etzu euerte euro eve ewoe exe ezie faell fam fang
farb fehl fgel flich ftem ftend fuehrt fussb gbar geln genh genst gern
gers gert geschl geschw gespr gestr giert glichk gnet griff heim herb
hler hlung hme$ hnlich iale icklu ielle ielte ienste ierba iga ilfe
ilo immu impo info ionae irke irku ischte itge ivste izi jahr jug kar
kett kleid komp kte$ ktor ldern ldes lektr licht lief llem llos
llschaft llter mensch mes mind mitg mmern mot mter naer nber nbes nbew
ndest ndlung nehm nell nfoerm ngek ngez ngsfaeh nke$ nkomm nkte$ nkten
nlich nom nschaft nstalt nste$ nstell nsten nster nstes nterr ntes
ntlich ntwickl ntwort nueb oble ochte oebe oecke oede oelke oeni oerpe
oerse oesse ohlge ohne onfe onte ontro opa orau ordnu orre orschu per
pers ppelt ppend press progr rang rber rde$ reien reing reis rekt ress
rfend rgen rges rit rleg rlichst rmoeg rreg rren rricht rsich rson
rstand rste$ rsteh rtend rzieh schoss schrieb schwind seg serv sgel
sigk sinn spez ssensch ssest ssigst stat stern stert stimm stlich tan
tar tat tent tigst tom tot transp tzer tzter tztes uali uede uefte
uehne uellte uemme uerfe uero uerze ugzeu ulde uldi und$ ungsfae use
ussba usste uti vat ve$ verfl verschw viert vorb wandt wert will winn
wohlg wusst zeit zerst zess
""".split(): TRIPLE_SCORES[triple] = 16

for triple in """
^abh ^ank ^ansch ^anw ^aufs ^aufst ^beu ^bie ^brau ^bro ^brue ^einr
^einst ^eintr ^emp ^ent ^entf ^entsch ^ersch ^ertr ^eur ^fau ^fle ^fli
^foe ^freu ^fri ^hy ^imm ^ins ^inv ^kle ^loe ^mie ^op ^pfli ^rea
^schmu ^schna ^schni ^schri ^spei ^spri ^stie ^stro ^toe ^trau ^true
^ty ^umf ^unsch ^unz abse abte abtei adie adio aefe aeft$ aehlte
aeltni aemte aendli aenze aerke aeumte affte ahn$ ahrt$ ahru albe alie
anfa anie ano ant$ anta apa arkt$ art$ asi ass$ atie auchte aude aufzu
aume auste azi baut begl berfl bgel bges blem blieb bten cherh chnend
chnik chtern ckert cklich cktest dank dernd ders derst dopp eamte ebau
ebrau edeu edue eglei ego egri ehi ehrli eifte eima einli eins$
einscha einzu eira eitli eize ektio eld$ ell$ ello empo endie enei
enfoe enie enka enkte enma enntni enre enrei ense enwe epo eppe epu
erbei erklae erkra erku ermue ernte erpa erro erru erschu erschue
erschwe erspa ersto erzeu erzo eschwe eschwi espie ess$ essio estra
estre etie ett$ euer$ eure ewie eze ezia felt fern fest ffer fgew fig
fisch foerd folg fortg fund fung gal gefl gelnd genw gep hel herg herr
herz higst hind hne$ hob hrte$ hrter ieg$ iehu ienst$ iers$ iff$ ift$
igst$ ila immte inve ioese irche irme irre isto itglie itt$ iv$ izei
kam klass kohl koll konf kontr kten kult kund lden ldig legr leist
lieb lien ligst lligst lltes lzen mag mar masch mein meinsch mmand
mmernd mper mpfend mput mten mus must nart nausg ndernd nders ndigst
ndisch nett nfaeh ngeg ngeschl ngetr ngsvoll nhalt nie$ nigt nik nit
nktion nkung nnten nnter norm nreich nstaend nung nzend nzier oeche
oehne oeri ogie ohe olde olie oll$ ollte ombe omma omo onse onsu orfe
ors$ orta ortu pap pfen port praes rakt rant rantw rband rbest rbrech
rdert rdnet rek renz rett rfass rfolg rgeb rhaeltn rie$ rien rigst rik
riss rist rkehr rkend rkomm rlag rlass rmend rnen rob rop rschlag
rsetz rsorg rster rstes ruest ruh rungs runt rweis schicht schneid
seit sens sgab sgeb sgeh sgew sid sieg sol spiel spraech ssert sster
stest strass strie$ stud ton tteln ttes tut typ tzlich tztem ucht$
uck$ uckte ueck$ uegte uerste uerte ultu uma ungspro ura urtei utzte
uzie verkl vid vier vit voll vorh vorst wachs waehr waff wahrh welt
wend wicht wies wohl wohn zit zuck zust zweif
""".split(): TRIPLE_SCORES[triple] = 15

for triple in """
^abk ^abm ^abschl ^abtr ^auf ^auftr ^ausdr ^aush ^brei ^bri ^brie ^ca
^che ^daue ^ein ^einb ^en ^flei ^flo ^haa ^inh ^inst ^je ^kie ^kno
^krae ^krei ^lue ^moe ^org ^pha ^rie ^schlue ^schmie ^trae ^umh ^uml
^ungl ^unk ^unn ^unp aate aba absa abso achtu ada adre aehne aehrte
aehte aele aenne aerkte aerzte aessli aeufi aga agie agt$ agu ahrte
allge als$ alste altsa aly ammte ampe ampfe amt$ andge angri angs$
anste antie anu anz$ anzei ape aphi arkei assa aubte auer$ auerte
aufna aune ausa ausbe ausche ausste avo bad bell bensw beschl beschw
bgef bger bgesch bteil btes buerg char chers ckes dacht delnd derb
derh disch disk dress eali eblie echti echtli efle eflo efte egli egne
egt$ ehau ehne ehte eibu eier$ eihei einko einste einu eisu eitge ekle
eklei ekt$ ektie ektro elbe ella emie emme enfe enle ennu ensio ensti
entha entri entu erbrau erbri erdi erdrue ergae ergie ergnue erhi
erkue erloe ermei ermo ermu erpu erschei erstei erta erwu esae eschle
eschrae eschu essie esteue estge estrei etzt$ eude evi ewue exi expe
ezue fes ffiz fgeh flieg fnahm freih gefr gie$ gleit graf gross gruend
gsam gzeug haupt haush hbar heit hinw hinz hmer hrbar hrers hten ibe
iebi ief$ iente iet$ iko iku ilbe ild$ ingu iri it$ itz$ kab kad kern
kirch kol korr krat kter ktiert laend lang lar ldend lehr lfe$ lltem
mark meist mier mmelnd mmenh mmun mmung mont mpfindl nag nah nbeh nbel
ndbar ndelnd ndiert ndigt ndler neing nent nerg ners nfer nged ngung
nhand nien nker nlass nleg nmaess nnung not nstig nteil nterb nters
ntersch nterst ntert ntral nweis nze$ nzeig nzug odi oeffe oene ofe
ohre oko ola olla ommu ompu onku ordne orhe orm$ ormu ortie oss$ ota
pat pos preis prof prot prov ras rbel rbend rbot rdnung rel rent rep
rfall rgek rgel rgest rhol rial rkeit rkund rlegt rlos rmal rme$ rne$
rreich rschaft rteid rtier rtik rtlich rtung rzeichn rzend rzeug sagt
samt schaed schatt scheid schloss schste$ schsten schster schstes
schuett schuld seel sent sgef sges sig sion sisch sitt slich spitz
ssenh ssern ssers ssier ssiert ssiv sste$ ssten stalt sters stimmt
stoss strich taer techn temp terg tert tigt traeg ttelnd ttlich ttung
ubli uchs$ udie uele uerme uerzte umfa umpe unfae ungsre ungsu unkt$
unktio unre unsi unwi upe urge uri urse urze uta utie vergr verkr
versp voelk vord wart weis well wes wint zahlt zeichn zerr zig zirk
zuf zuk zul zuw
""".split(): TRIPLE_SCORES[triple] = 14

for triple in """
^ad ^al ^anspr ^beei ^bla ^blo ^dia ^dri ^dro ^ed ^enth ^entr ^erbl
^glau ^glo ^gri ^haeu ^heu ^irr ^kni ^opt ^ordn ^prue ^schnee ^schnei
^schre ^spae ^spu ^the ^troe ^umsch ^umst ^unh ^unl abko aechli aegi
aehrli aengi aeru aeubi aeute affne agba agi ags$ ahr$ ahrzeu alko
alku allei ampf$ amte anbe ands$ ankte annt$ ansa antei anzte apfe
aphie appa astro athi att$ attu atzte aufte auftra aule ausbi ausschu
auszu axi azie bank bedr bekl berd bett bgeh bill bin bjekt bomb btem
btest buehr buer chsel ckung dam dav dens derspr derw dez dien dienst
dir duz eate ebni echa echli edrue eg$ egrue eht$ eichli eifa einfue
einha einte eitsge ekre elba ellt$ elste elze emu enhae enmae ennba
ensie ensta entla entzue enzu eordne erbae erbie erblue erbrei erflue
erhue erkaeu erkscha ersae erschae erschwi erspre erstau erstre
ertraue eschlo esge estu etae etau etri etru etrue etste etzba etzli
euche eudi eugu eur$ explo ezae fabr festg fgeb fgef fger fgest forsch
freig fuehl gar gart gat geld geschn glichst gniss grund haus hlte$
hnung hoch hoerd hrtes hund ial$ ida iebte igna ingt$ inste insti inu
inzu ira irge isi iso issio ittli itzi ize kaelt kannt ket klam konk
krank kum lbar lebt lef lett lfen lfoerm lgend lger lif lin lleg llier
llste$ llsten llster lock lon ltern lut lys ma$ mem mill mist mitl
mlich mmig mmten mob mor mpfe$ mpfen mte$ nam nannt nbar nbest ndels
nderb ndier ndigk ndlichst ndste$ nfaell nfuehr ngekl ngesp ngig nhab
niv nnbar nnigst nnte$ nntest nricht nschaftl nspiel nsport nstit ntag
nterv nterw nterz ntisch ntroll nunt nver oba oehe oeru oeti of$ offi
ofi ohnu okra olke oly olze ommi ompe ontie opo ormie orsi osti otie
pflicht phisch ppar proz rab raend rbe$ rbew rbiet rbring resp ret rev
rgef rgeg rgend rgesch rhandl rium rkaeuf rkehrs rkenn rles rlust
rmitt rmon rnat rom ros rschied rtigst rueb rueck sal san sbild schaff
schalt scheit schnitt schstem schte$ senb senh sicht sign silb spannt
spekt ssag ssbar sschuss ssel sselt sstell stieg stier stor sucht tab
teg terl term terr tglied tions tit tod triebs ttels ttest tzbar
tztest uechi ueckve uefu ueme uendu uensche uensti uerli uese uestu
uetzte ugge uhi uhr$ undu unei ungsma ungsmi ungswe unvo upfe vergl
vergn verkn verschm vil vorl vors vorz war werksch wirk worf wuch
xport zaub zent zerf zerm zieh zueg zutr zuv
""".split(): TRIPLE_SCORES[triple] = 13

for triple in """
^abbr ^aff ^ag ^angr ^ankl ^anp ^ansp ^antr ^ap ^ar ^aug ^ausk ^aussch
^ausw ^bae ^bee ^dae ^deu ^einsch ^em ^erfr ^ergr ^erkl ^erschl ^et
^feu ^fie ^fraue ^jae ^klo ^leu ^ol ^or ^pau ^pfe ^pho ^roe ^schru
^schwu ^spru ^spue ^trei ^treu ^trie ^ur ^woe ^zae ^zeu ^zwie ab$ abla
abschie abste achli ado adt$ aebe aedte aehnli aehre aer$ agge ahrhei
aise aka akze alli alze amkei anni annscha annu anse ansi anwe anzue
apu arbi arde arla armo arschie arto asa assna ast$ ats$ auke auschte
ausdru aussi ave avie azu bar beln berk bkomm blas bler bor broch
chernd ckelnd comp dar def dekl denk derr dicht ding dlos drueckt
durchl durchs ebae ebro echtge eck$ eckt$ ecku edro edru eele egre ehu
eigne eihna einba eisi eispie eist$ eleu elfoe elmae emmte empfa enae
enbi enga engte enhe enieu enpa enspie enstae entschei entwe enwi epla
erbrue erbue ergrei erklei erleu erpre erschi erschlu ersoe erspie
erspru ersti erstoe erwo eschau eschma eschmie eschni etho etrae
euern$ eug$ eunde euti eva ezu fed fenst fers ffekt fieb firm ford
fueg fuellt funkt gedr gekl gekn gernd grenz grupp guet handl heft
heil hlich hlig hlten hnte$ holt hres hrtest hte$ idea idee idie ied$
iegte ilme ind$ ingte inn$ ino insta instru inwe ipli irkli irma isku
itzu ivie just kalk kast kel kom kompl kond konstr kor kret ktier lern
lge$ lgen lid lieg lker lliert llstes loest lust miert mig mkeit mmiss
mtes nachb nachr nang narb nbed nbesch ndsten ndster neid nerf nerw
nfall nflat ngeschr nget nglos ngte$ ngten nktes nnahm nntes nor noss
npass nschlag nserv nsion nstrum ntem nterbr ntrag ntscheid nverk
nvest oestli oje onto ophe orche orgu orsche ortei ove ovi pan path
patr pen pfig plan prob publ ram ranst raufg rbeits rbind rbrauch
rbreit rdernd rdin rech reist repr rfuehr rgang rgebr rient ries
rischst rklaer rksam rkte$ rleit rmer rmin rmittl rndem rnend rner rot
rschein rschuett rse$ rteilt rtigt rtraeg rtschaftl rueckb ruecks
rueckv ruehrt satt satz schad schenk schickt schluess schten sieb sied
spieg spielt sprech sserst ssnahm sstest stach steckt stein stens
sterh steuer stiert stik stit tad thod tigk trock tschend tul ubi
ueckbe ueckli uegli uehlte uehte uelti uenge ufue ukti ulae ulte ums$
umsa umwe ungsau ungse unse urre urte ust$ usta uve verschn walt weihn
woch wonn wuerf zend zeug zimm ziv zuecht
""".split(): TRIPLE_SCORES[triple] = 12

for triple in """
^abn ^abschr ^absp ^acht ^adr ^akz ^anschl ^app ^arr ^ausd ^ausz ^baue
^eff ^einm ^ents ^entst ^fru ^ill ^infl ^ost ^pfle ^rae ^schlei ^schnu
^tee ^theo ^traue ^um ^umschl ^unfr ^zy abhae achri aecke aedche
aenkte aenni aerge aerti aeuche aeusse agne alge amie amo anche anglo
ans$ anspru anwa apo appte archi arma arrte artne atue aufse aufwa
aufwe ausfue ausrei baend ball beitr belnd belst berdr beschr bgesp
bod buehn butt chbar chens chricht chsend chtbar chtfert chtigk chtlos
ckern cktet dah daz deck dek dell dev dikt duld durch eachte ebaeu
ebt$ echu ecki edrae ehru eigte eilha einla eitra eizte eizu eja ekae
ekau elta enki enme enpro enschli entei entue envo enzi enzie eoba
epfla epro erbau erbra erdre erdru erflu erglei ermie erpro erschrei
ersie erstrei ertie erza esau espo espro espru esve eueru eugni euli
eundli eutsche euze evoe fach faeh fasst felnd fernd fess ffes ffnet
fgebl find flugz frag ftigst gels genf geschr glied gnal goss hab hag
hest higk hilf hlbar hmbar hnten hochg hoert hot hrern hrlos hrtem
hter htes ichst$ ick$ iedli ielt$ igie imie imu infla ings$ ioni
ionsge irksa irte isio ista itlei jekt kehrt kell kelt kers kess kocht
krim ktur lab lde$ leid liebt lkul llbar llgem lligt llstem lmaess
lsten lster ltsam mach med meind mel mens miss mmens mmenst mmte$
mmter mpelt mpfer mueh mult nach nachw naeh nbek nbez nbild nderh neg
nein ngebl ngep ngern nglichst ngsmitt njunkt nkurr nnisch nschen nsen
nstrukt ntal ntin ntraeg nwaert obje ock$ ockne oefe oehnte oemmli
oesu off$ og$ ohlbe oke oku olli ongre ons$ opfte orne otge othe otze
ovo packt pfer pfleg phant phot pisch pot ppel ppelnd prop rabsch
rausb rbaend rbig rechtg reh rge$ rgebn rgem ring rkauf rkung rnaehr
rnier rnig roeffn rordn rrat rre$ rschung rsetzt rsichtl rsprech
rstaendl rstatt rsteig rstem rtiert rueckt rueckz rumg rven rver rvorg
rwart rzaehl rzigst sbar schreib seid sgek sgest sierst son speis spek
spend sproch ssenb sserl sstes steig sterb sternd steuert stift stigst
stin stlos suend tast teilt terb tin tischst tob togr treid trunk
tschaft ttiert uchu ueckt$ uegi uegsa uendli uenschte uenste uepfe
uerfti uesste ufa ufrie ufte ulti ulve umpfe umra undge unglue ungsko
unktu unna unrei unzu urchschni urs$ urste utge utio utz$ uwe verj
verschr vorm waffn wag witt wohlb wuerd xist zerl zif zis zub zuh zung
""".split(): TRIPLE_SCORES[triple] = 11

for triple in """
^abstr ^abt ^ak ^allg ^arm ^aufm ^ausm ^ausschl ^austr ^blei ^eindr
^einschl ^eint ^entm ^entspr ^erschw ^expl ^gea ^geo ^gli ^goe ^grau
^groe ^hie ^in ^ink ^jo ^kreu ^neue ^pfla ^psy ^scheu ^schro ^ska ^ski
^traeu ^umz ^unst ^zau ^zwoe aari abfa ablo abschlu absi abwa achba
adu aendni aesche aeude aeure affee afti agra ahi akt$ aku alla alu
ammlu andie ando anfae anga angie angte ankhei anlei anme anpa antra
ardi arf$ arka arle ars$ aspe athe atho auern$ auernde auffa aufga
aufre ausglei bacht baeud bas batt bent berbr bernd bersp berstr bess
bezw bgeb bgek bgez bhaeng bhaft bigst bisch biss blik blut bnis bniss
bonn bring chan chelnd chgem chger chhalt chlichst chnisch chstab
chteil ckel ckernd ckers cklung deal deckt deg dies dik disp div dreht
efrie egle ehmba eichge eichnu eils$ eim$ eimli eimni einfu einna
einsi eitsa eitsbe eldu eltu empfae enda engli enhau entio entlo entre
entru ents$ enwae enzei epae erbeu erflo ergru ergrue ergue erhau erhu
eriu erkle erkoe ernie ernue erpe erqui ersche erscho erstri ersue
ertrau ertrie erva erwie eschie eschwae estei etrei euende euere
euernde eugte eutu faehrl falt fel ffel fges fing fot freiz fremd genb
gepfl gger git gnend grab grundst gut haut heimn himm hlter hltes
hlungs ichts$ ickt$ ieche ies$ ilge immi immo impe ins$ inzi ionsbe
irbe iro ispo itbe ito ittlu iums$ jub kaempf kaff kant katz kauf
kauft keg klebt koen koerp konj kraeft kris ktien ktisch kuemm kut
laest leucht lib lichst liebl lind llern llion lndem lnehm lohn lom
losg lters ltert ltigst lux lymp lzend markt mbol meld mgeb mik mikr
mitb mitgl mmel mmenb mmlung mmob mpath mpet mpliz mues muet mul mutt
na$ nabs nar nbef nderw ndid ndit ndstes nenh nerk nerl nern nerr nerv
ngert ngriff ngsges ngsvollst nhaendl nhaeng nheitl nicht nim nism
nkel nnern nntem nser nsich nsiv nstand ntergr nterk nvers nzieh obie
ochge ochschu oeffne oeme oepfi oette ogno om$ onju onstru onve opi
opie opti orgte orti ortli orzu osge pfe$ piert post probl proj psych
pul ranl rbeig rbitt rblich rchen real rechtf rechts ref reign reinf
reins rern rfest rgerl rgreif rhand rhoeh ritt rkannt rkten rlauf rleb
rmach ro$ rrekt rsen rsitz rstaend rstig rweit rzen rzog rzte$ sag
sant schaefts schein schimm schlacht schob schraenk schwef sek selbst
sgeg sgem sgesch shalt sold somm spann spaz splitt sprung stab staff
statt steck still strat streich stroph stund sundh tall tasch teiln
thek therm thisch tok treff troff tterl tterst ttier ttig tuerl tztet
ub$ uchsta uebli uebu ueffe uegu uehrt$ uene uhre uierte ukte uku ummi
umpfte unda undhei undstue unfa unga ungsi ungsrei unsa unst$ unue
urme utsche val vem verfr verspr verstr verv ves vol wach waerm waess
weltm wolk woll wurz xpert xplos ympa zer zers zertr zusch
""".split(): TRIPLE_SCORES[triple] = 10

for triple in """
^abd ^agr ^ahn ^alk ^art ^aufn ^ausfl ^ausn ^ble ^eb ^entb ^erpr
^erstr ^ev ^inl ^klae ^lee ^nue ^ord ^pei ^phi ^que ^raeu ^schaue
^schlae ^schlo ^schra ^stri ^umb aatli abga abre abrei abru acha ack$
aengni aerbte aerche aetsche aeule aeusche agli ago ahnu ahrba ahrha
ahrschei aiso altge altlo andwe angrei anle anma anre anstae aria arm$
aru asst$ astu ateu attie auch$ aufhe augli ausch$ ausfa aust$ austau
auswa auswei azwi band bendst benz berschr berv bespr bier blon btet
buech chart chtlichst ckgew cklos darf dazw densch denst dep derv
dlichst dok doll draengt duerft ebla ebre echtfe echts$ edre ef$ efra
efre egrei ehba ehrs$ eicht$ eiende eifli eifri eihte eila eilt$ eimi
einbe eindli einga einkau einrei einve einwa eisti elbstve enbau endli
enfae enkli enli enmi enoe enschei enschi enstue enwei enzte eppte
eprae erble erfreu ergo ergoe ergri erkte erpfla errte errue erschoe
erspe ertoe erzue eschli eschlu eschmi eschna esei esso essu estli
estoe etreue ettbe eutli exa ezwi fahrb fass fens fett fgab fik flog
fon freud frig ftrag fuegt fuercht futt gab gebl gendst gepr gien
glaub gleich gleichg grat gul gungs haengt haf heg heir heiss hell
hner hntes hochsch hrzeug ichtsvo iebli iedri iegt$ ieht$ ientie ikro
il$ illa illio illu inkte inze iolo ionsa ippte iqui irkte iszi itta
itua kampf klapp klein kon krit ktes ktik kuend lant lanz lehrt leicht
lenk lent lges lste$ lstes ltlos ltniss ltur lum meng mgeh mie$ mild
mmenf mmenr mmlich mokr mol morg mport msten nacht nad naufg nbahn
nbegr nbet nbetr nbring ndlers ndter nert nfahr ngelt ngers ngeschw
ngsber ngter ngtes nhaus nkbar nkert nklich nkter nlang nleit nlichst
nnes noet non nord npreis nrein nruh nsel nsetz nstem ntakt ntar ntat
ntell ntens nterf ntet nthalt ntig ntil ntim ntrum ntwick nverb nwend
nwill nzahl nzelt nzern obu odie oehu oesche oesli ohei ohnte oho
ollge ollie omple onnta opf$ ord$ orni orts$ osio ossa osta otzi ovie
pag paz pens pferd pfte$ pften phil plin ppert ppten praez prom ptim
racht raeumt rass rbes rblend rdigst rehr reicht reinb rfe$ rfind
rftig rguet rhebl rif rkes rlad rlam rlist rma$ rmeist rmiert rmul
rmut rnseh rpflicht rpreis rrig rseh rstet rstreb rtag rtraegl rueckw
rwend rwert rwund rze$ rzten rzug sam schabl schafft schlicht schnell
schraenkt schtes schuetz selbstv sell selt serl sonnt sorgt spalt
speich ssem staats stigt stil stoch stueck sup szipl tam tastr tbar
thol tionsg tist tleid tlos totg tracht trans tromm trueg trupp tschen
tterh tters tug tzigst tzlos uatio uecksi uehli uenstle uerchte uerde
uerfni uf$ ugs$ uko umlau umschla umse ungsme ungso ungswi upfte usche
ussrei utzi uwa uxu var vent vog vollg vorf vork vorr vorw wacht wack
weiss wick wind wirkl wurst ycho ysie zaehlt zeich zerbr zieg ziell
zuz
""".split(): TRIPLE_SCORES[triple] = 9

for triple in """
^abdr ^abfl ^akk ^anbr ^anstr ^auft ^ausbr ^beau ^beo ^chi ^eng ^ert
^feie ^gau ^gie ^grae ^graue ^ir ^is ^kai ^keu ^klu ^kne ^knu ^krau
^nei ^noe ^oel ^saue ^scheue ^schmae ^schmei ^schmi ^schnue ^spli
^thro ^triu ^umsp ^voe abma abrue abu achfo achs$ achtei achu aechste
aedli aegt$ aegte aeke aeme aengt$ aerbe aermte aesti aetti aezi affie
affu andscha andu angsa anhae anko anku anrei anschau anschla anschlu
anza anzi arfe ark$ arkte armhe arne arze arzte atsche auere aufla
aufs$ aufsta augte aulte aums$ ausde ausfu ausra aussta avi back bal
bast beb beisp belg beng benst beob bergl berschw bgebr bgem binn
blaett bog brannt brat brech bruest bsicht buch burt chnen ckenh dakt
darl derk derstr derz digst dingt dram druck druckt duerfn durchschn
echno edae eflue efoe egba ehmi ehrba eichni eid$ eilba eilne eimte
einma einri einse eische eisge eisli eisste eita eki elda ellba ellste
elme enbu enbue enfo enho enra enro entbe entfe eolo epe epra epre
erbla erdae erdau erdoe erdue erfei ergu erio erja erkni erks$ ernei
ernge ernu erpla erprei erque errie errli errscha errsche erschme
erstaa erstie erstu ertru ertue ervoe erzau erzli esaeu espre essa
essli estau etaeu etue eugne eule eutra ex$ fachg fas fecht fels ferst
ffelt ffens floss flueg fortb freib ftigt funk gant gekr genk genl
gepl gezw grad guenst gumm gur gutg habt haelt haeus handw heb heilt
heimg held herrsch hlern hltem hoh hol hrhaft hrlichst hrungs htet hum
iane ibi ibu ichu iebsa iefge ielge iels$ ieme ieni iessba iessli
iesst$ ife igge inko innte ioti isvo kas kenn kil klaert klag klamm
kok kompr konst konv kop kuenstl kuest kurs lanc larm lbig led lernt
lism lkoh llert lligk llkomm lme$ lok lstem maecht mand mant mask mdet
ments merk merkt mgel mgest miet mis mmeln mmers mmerz mos mpfind mpon
mste$ mster mtest mut nachf nachz ndeln ndenz nderf ndesb ndienst
ndlern nenb nerh nerm neug neutr nfach nftig ngab ngaeng ngbar ngelnd
ngeschm ngestr ngiert ngsmoegl ngsrecht nigst nkheit nkund nmach nmeld
nnehm nnschaft nntniss nogr nov nreg nreis nschaul nschein nschlaeg
nschreib nspruch nsteh nstet nstreich ntas nterm nterpr ntion nutzt
nverst nvertr nzer nzert nziert nzip nzueg nzung obte ockte oehnli
oenne oepfte offnu ollstre ombi ompa ompli ompo ondie onge onti oote
orko orra orri ost$ otscha oxe panz perf pet pflanz pper ppte$ prakt
prallt preisg prim pruef qual quent raeum rausz rbef rbeitsl rbet
rbild rdnend rdrueckt reb reif reinl reng rerz rez rfaell rford rgaeng
rgnueg rheb rheir rheiss rheit rioes rktes rlang rlaub rletz rlieg
rmaess rmass rmherz rmiet rnis rnte$ rol ron rrte$ rsam rschiess
rsicht rspiel rtner rtoff rueckf rungsb rungsv rvat rwand rwandt
rwirtsch rztes saeub schaut schig schmiert schtem schter schung schwer
sess sged sinnt sorg spart spenst spon sseln ssenk ssens ssenst ssernd
sslichst sstem staerk staet stap stemp stent strahl stritt stuerzt
symp taus tekt tenb tenl tenst ternd terst terv teur text tgeb tgeh
tgem theat tont tral transf tron trop tsche$ ttbew ttelm tterf turg
turn twill uefe uehrli uemli uenfti uer$ ufli ufu uiere uktu ulle ulta
umhe umu un$ unae undie ungs$ ungsmoe unpa unste unze urei urg$ urm$
ursa uschla utzu veg verpfl vort wald wasch web wegf wegl weltb weltr
wirkt witz wohnh wohnt wort wucht ympia ypi yra zerkn zin zufr zugr
zun
""".split(): TRIPLE_SCORES[triple] = 8

for triple in """
^abbl ^aerg ^alp ^arch ^arg ^aufkl ^aufsch ^aufschl ^aufsp ^aussp
^ausstr ^boo ^cho ^chri ^einsp ^erdr ^ernt ^extr ^glae ^knau ^koa ^mau
^plu ^schnau ^schwie ^stre ^teu ^thea ^umschw ^urt aat$ absti abwi
achbe achgie achi achsi achstu achtsa aech$ aerli aetzte affi afi afie
afri ahnte akle alke ammie amms$ ampfte anchie ancie andha andschu
anoe arko artu arve asta atla atsa auend$ aufko aufle aufma aufsi auri
ausko ausloe ausschla bat beamt beif beil berbl bergr berschl bind
bitt blend blichst blum breit bruech buchst bueg chel chenb cherst
chnol chse$ chters chtert chtungsv ckenl ckerb ckerst ckhaft dag darst
deb deln delst densw dom donn dos drueck durchf eaktio eblae ebrue
edaue ehaeu ehnli ehri eidli eift$ eigt$ eihu eilna eimge eintrae
einwi eisa eissge eklae ektri elfa ellie eltbe elue elwe ems$ emse
enbo enfi enfreu enkla enlie enna enni enpla enpo ensae ensbe ensei
ensto ensu entle entste erbro erdeu erflie erfri erfu erg$ ergla
ergroe erki erkli erkrue erksa erkzeu ernste erpfli erprue ersaeu
erschle erschlei erschro erzwei eschleu eschoe eschwei espri espu
espue etai etti euri exte fahrl fahrz faul feln fenth festl feucht
ffenh ffentl ffnend ffte$ ffung fgeg fgek fix folt fricht frik frist
ftraeg ftung gabt geldm gell gelm genm genn gfaeh ggest gion gnad
grenzt grossh haend haeng halb harm hern herst herzl hitz hmig hnter
hoeh hoffn hon hrenh hrscheinl htem htest huet ickli iegsa iera iffa
ifti ildli ilia ilste immt$ impfe infi inla innu iru issa issi issve
ittle kais kaltg kamm kand kath kehr kenntn kin klim koal kord ktivst
laeuf laun lben ldert lei$ lers lgew ligt lik lken llar llenl lltest
lor ltier ltlich lueck mann mben mischt mmenbr mment mmtest mporg
mprom mstes muend nbem nbestr nbrech ndal ndesl ndiv ndlichk ndstem
ndte$ nehr nenn nentw nerz nfabr ngedr nghaft ngier ngtem nhoer nieur
nif nischst nkes nmut nnem npol nruf nsat nsatz nschlich nschluess
nsend nseq nsinn nstimm nsul nterschl nterschr nthalts num nverd nverm
nvoll nzentr nzig nzul oali oeffnu oefli oele oenli oente oesba ohn$
ol$ olfe olgte ollbe ollko ompro ondi ont$ optio orda orha orke orsta
ortbe ortrae oso ostue owje parl passt pflanzt pflegt phon plast pok
poth quid ra$ rabs rag ran rann rbess rblick rbrenn rchend rchlaess
rdern rdicht rdienst refl rell rers rfert rglich rgruend rhaeng rhuet
riod rker rkleid rlaend rlaessl rmaecht rman rmes rmess rod rost rper
rraet rrechn rred rreiss rrisch rrsinn rrten rschlaeg rschloss rsoenl
rstaendn rstend rstueck rtis rueckh rverk rwuenscht rzaehlt rzeit
saeur salz schauf schauk schieb schlaf schliess schmier schnuert
schoepf schuetzt schul schult schwein seif senk sex sgestr sgetr sgez
sim sis slos smaess soph sowj spritz sselnd ssigk ssisch stamm stausch
stischst strier stuf sud syst tak tenz theor tief tivst tlichst truebs
tsam tschig tschrift tuat tyr tzern uartie ubri uebte uechse uechtli
uenfte uente uepfte uerso uetli umga umo umpte unbea unko uote urchei
urchlae urku urve ustae utre uts$ uwi verzw vok vollb vollstr waehl
wehr weid willk wimm wink wuehl ype ypo zerb zist zum zweck
""".split(): TRIPLE_SCORES[triple] = 7

for triple in """
^abgr ^andr ^anpr ^anschw ^aufb ^aufdr ^aufp ^ausgl ^bio ^eg ^ehrl
^eif ^eiw ^ek ^elt ^entschl ^flae ^impr ^mee ^my ^obj ^plau ^sai
^schno ^schrau ^umkl aal$ ablie abne absu achtlo achwei aechtli aehli
aehnte aeische aelde aengsti aenku aerfe aeri af$ ahlt$ ahnde akto
aldi allo alpe altba althe alve anspi antrie anwei apse argu arra aske
assge atzu aub$ aubi auchba auffue aufme aufri aufste auscha ausru ava
awi barb begn benh berq berspr bgab bgetr bleib braucht brig brueck
bschluss chselt chslos ckeln cknet diot dium durchw ebeu eeigne eerte
efei efli egio eglie ehrlo ehrt$ ehue eibli einka einle eits$ eitschri
eitsve eiwei eiwi ekna elaeu elbstge eltge enhaeu enlei enschla enschu
ensge ensve entbra entfa entschlo epfle epi erdro erkae erkrie erno
ernspre erschlo erspri esbe eschri esli etoe etto etts$ ettu euerli
eufe euni eurs$ ezwei faehrd faerbt fein ffenst fgetr fil fkomm flott
fluecht fmerks fragt freist fris fseh fuers gaz gegn gelb gelst germ
gerst ggef ggel gin ginn gkraeft gog gor hall haltl handg heiz hem
hlges hnlichst hntem hom hrtet ible ichta ideo idio ieli iello iesi
iess$ imma ingst$ iplo iskre ispe jud ka$ klar kleinb komb kongr ktlos
ktors ktron kur laech lbe$ lchen liq lkraeft llstaend lmen loes lueft
lver lze$ lzes malt mbin meint mges mhaft missv mmerl mmtem mmtes moeb
mpel mpelnd mpfaeng mpfung mtlich ndeg ndens ndesg ndesv ndhaft ndicht
ndschaft neig nfert ngang ngeld ngeschn ngsprogr ngsproz nierst nkauf
nkenl nkleid nlauf nnens nnuetz nrechn nseit nspar ntbrannt ntif
ntraecht ntret ntschloss nutz nvent nwag nwand nwirk nwuerd och$ oehle
oelle oelpe ohnhei ollstae olste olz$ omba onsta onu ordi orsa orschri
orto oru osa osie ossi phys platz putzt rak rar rchges rdaecht rdes
rdient reib reinh rfluess rgab rgetr rgisch rgriff rgroess rieb rkaufs
rklich rland rleicht rloes rmier rnes rsach rsag rschuld rschwend
rstoff rtel rtern rtigk rueckst rum rzeugn rzlich sab saugt schaud
schaul schelt schest schiess schiff schleppt schleun schluss schmied
schmutz schoen schreck selbstg senl sin spir ssant ssenl sset sshand
ssreich staatsb stechl stelt sterl steuerb stief stiz straft strahlt
stspiel sugg sult sund taenz taf takt tang tap tell tens tionsl to$
tol tors traeum traul treuh trisch triumph trotz tschelt tusch tzest
uchha uchslo uebri uedli uendni uergte uermte uga uha ultie ungsmae
ungspo ungszei unne unschae unsta urbe urlau urne ursti uspe utzlo
visch vollm vortr waehlt weltg wen werk widr wirb wohlt wortg wuensch
xek ymbo yna ysi zen zerfl zersp
""".split(): TRIPLE_SCORES[triple] = 6

for triple in """
^abschw ^aeuss ^aggr ^angl ^as ^ass ^aufk ^ausbl ^aust ^blae ^doe
^einfl ^entfl ^ep ^erq ^es ^grei ^hee ^instr ^knei ^knie ^mai ^neua
^pfa ^schleu ^taeu ^tou aare aatsa abei abfue abho abscheue absto
abwei achlae acki aedie aemie aempfte aeppe aess$ aetzu aeumi aftle
aggre ahie ahmte ahrlo ald$ alka allt$ amha andfe anfe anscha anstre
antri anzle arni arzt$ aubha aues$ aufa aufloe auftrae ausbau ausdrue
ausie ausku ausschue austra bahn baum beacht beist belh bels benb
bensm beschm bgedr bgen bgeschl bgeschr biert birg blass branch bstimm
buerst chgeb chgieb chner chseln dab darg dersp dew diff dipl dist
drigst dringl durchbr eabsi eanspru eauftra edli edo eeinflu efla
efreu ehli ehnba eiern$ eies$ eifi eigni einflu einsti eissi eitslo
eizei eizi ekli ekni eknue ekrie ekta ektvo elsi eltli empla enfue
engru enntli enso enstrei entfae entfre entschu entse entvo enza epfli
erbaue erdrie ereo erfra erkla erpo erschli erschlie erschnei erschra
erschrie erstra erwoe erzte eschnue eschrau eschrei euen$ eugs$ fachm
fad festst ffeng ffig fgesp fgez flaech fleisch fluechtl fluest freim
freit friedl fwand fwend gall garn gas gast gbarst gelf gendh gensch
gist gnier gniert gott gramms greif haert helf herrscht hers hllos
hltest hndet hochz horcht hrensw iani ienge igi ignie ilbi inae infa
inrei iode ip$ ipfe ipu ischle ischu isko islo iss$ istie itschi itzt$
kard ke$ kleb klett knall kriegt ktvoll la$ laengl lgesch lierst llekt
llisch llmaecht lob lod lot ltiert ltnis maedch maerch magn mak mang
mannsch meing metr mfass mgesch mgew missg missl mmenl mmenz mniss
mpe$ mpften msatz mschlag mstem mtern nabh nachl nbeschr nbuerg nche$
ndelb nderr nderv ndgel ndruck nempf net nfiz ngefl ngekn ngress
ngsstell ngsunf ngsvers ngswidr nhaeus nheil nind nkass nkelm nkernd
nkreis nktest nktet nleih nlief nnlich nprod nschiff nsehnl nsicht
nsiert nsmitt nstall nswuerd ntfremd ntiq ntwortl ntzuend nzel nzelnd
ocha ockie oerri oert$ oertli oga ohli ohrte okto olt$ omfo ommt$ onni
ontra oot$ orbie orchte orla orle oro ortio owe pack pal past pell
pend phen ppell ppig punkt rabg rabr raed raff rall ranschl ranz rausr
rauss rbetr rbuch rdaul rdisch rdross rdruck rdrueck reinst rfer
rfuett rgelt rgeschl rgestr rhaert rigk ril rim rjahr rkelt rklein
rklichk rkuend rkul rlaess rleih rlief rmlos rniert rollt rpflanz
rpret rrang rrit rrlich rrschaft rruf rrung rsamml rschieb rschier
rschiert rschnitt rschreib rtei$ rtion rtrieb ruecksch ruehmt rund
rungsm rurt rwind saub schild schlich schmeich schmett schmiss
schnallt schraub schraubt schtest schwert schwest selbstb seng sez
sgesp sgleich skand skret skut sor sperrt spion sreich sstet ssverst
staat staedt stlichst stoer stoerr streb striert strukt stuem stuerm
stutz summ taucht tax terw ther tierst train treib trockn truebt ttenl
tterb tterw tum tzgeb uaele ubsta uchsvo uckt$ ueckga uecki uegt$
uehl$ uellt$ uenktli ueri uesti ugte ungea unhei unta uppie ussbe
utschte utu verpl viel vollst vste$ vster vstes watt weissh wirks
wischt woehnl wog wohlf wollt xen xper zeil zerk zerkl zerschm zerspr
zerstr zitt zorn zuend zuschl zuschn zweist zweit
""".split(): TRIPLE_SCORES[triple] = 5

for triple in """
^ack ^anschn ^aufschr ^ausp ^chro ^eil ^eingr ^einschr ^end ^entgl
^entk ^gee ^glaeu ^im ^jue ^knoe ^krue ^laeu ^pae ^pflue ^quae ^schmo
^schnoe ^schrae ^spio ^spoe ^trai ^uebr ^umgr ^unschl ^untr ^zoe
abdrue abscheu abschrei abstei achma acho achst$ achste achve achzu
ackha aehrde aetse aetzli aeubte aeufte aeumt$ afa afft$ ah$ alde alme
alzi ambo ammle ance andli angsve ankla anlo anna anrue aphe appt$
armee armlo artie atei atri aufstei auftre aunte aushe ausle ausna
auspa ausre ausri aussa baerd bagg beim belf bergb berkl besp bgekl
bien ble$ bnehm brief brill broeck bsond bucht chfolg chlaess chmaess
chol chschul chsels chtsvoll chwert ckgef cksicht dal deng derm dient
din dox drung durchdr durchz eansta eckli eckmae efrei egue ehl$ ehlu
einbi einbue eindri einhe einke einre eisst$ eitscha ekoe ekra ekrae
elche eleie elka elve elwei elwi embe enaue enbei endba enhi enkba
enkt$ enlae enlau enprei enrau ensmi enstu entae enteue eore eorga
eppi erblei erbte erflae erglie ergra erhaeu erkna erlaeu errae
erschni erschri erspo ersprue erstreu ertrei ertri ertste eschmu
eschwo espi essba estste etsche etzge euert$ euse extre fasch fbar
ferng ffenl ffter fgesch fget filt flatt fortf fortschr freil fress
freund fsicht gegr gehr glaeub glas gleichm gne$ gnos gress grundb
grunds gsamst gstell gungsm haar hackt haft heer heiml hev hier hlers
hnbar hntest holf hors hos hrerb icks$ iedi ierli iktie illkue illte
ilte indo ingba ionsve ips$ irrte ischge iska ituie itve ixie jagt
kaempft kaus ketz klagt klappt klav klin kling knoch knuepft krieg
ktions kuehlt kuerz kug kzept laeut langw laut lber lekt lenkt lie$
lied llenf llon llstreck lspiel ltat ltigt lvoll massg max mgek mmentr
mpen mpens mpfehl mpfte$ mpos mtem muetl nachh nakt nals nangr ncier
ndard ndgeb ndin ndstueck ndtest neinh neng nfass nfest nfluss nfuehl
ngepfl ngespr nglichk ngsbew ngsmaess ngsverf nkeln nkelt nkurs nlaend
nmal nnehmb nnert nop nordn npap nsag nschuld nseh nsform nspir nstern
nsum nsyst ntegr ntel nternd ntiell ntik nuegs nverl nwerf nwert nwes
nwohn nzeit nzte$ oehni oehre oelbe oelze oerba oermli offha ohla olme
onds$ onfi onia ony opaei oppo opu orbei oriu orschla orschlae ospe
otio ots$ ottge otwe ourna owie paeisch pausch pe$ pflast pftem pfter
pftes piers platzt polst ppeln praed quar radsch rafft rank rap rarm
rasch rausf rbarst rbindl rbroch rbund rbung rdend rderb rdien reimt
reinn reitsch renh rest rfekt rfuellt rgebl rgeld rgern rglied rgnuegt
rgrab rgung rherg rhoert rkrank rlaubt rletzt rlichk rmigst rmlich
rmord rmued rnicht rnuenft rrechtl rreicht rror rsatz rschrift
rschwingl rsend rsit rstellt rstoer rteilh rtert rtlos ruecht rueckk
ruehr rufl rungl rvers rviert rwerf rwies rzes rzicht sais salb sandt
schaetz schick schied schien schmar schtet schwaech sert sgebr sgegl
sgekl sinnl skizz skop sort sped spoett sprach spring spritzt spuelt
sserh ssgeb ssigt ssivst sstatt stanz stems stoeb stol stopp straf
strebt subst sued svoll symb tabl teng tenn them tim tionsb tionsr
tischl tmach tos tour trink tschlag tslos tuecht tzbarst tzers ueckzu
uellu uendba ueppe uetzi uft$ ugru uh$ ultra umi umri umtau unfoe
ungsgru ungska ungste ungswue unio unme unwue urchse urie urnie uschie
uschte uzu verq viol vollz vong waehrt wegr wein wieg wundg xempl xim
ygie zapp zerw zioes zoeg zud zudr
""".split(): TRIPLE_SCORES[triple] = 4

for triple in """
^abkl ^abspr ^aerzt ^allt ^amts ^anbl ^aufpr ^chau ^drue ^einbr ^einkl
^entzw ^erbr ^ersp ^glie ^gy ^impl ^intr ^kaeu ^kloe ^laie ^opp ^pfi
^phy ^plae ^qui ^reue ^schlie ^stru ^uebl ^ultr ^umd ^umfl ^umk abfae
abfo abha abkue ablau ablei abloe abscha abschni abschue absta abstra
abwae aby abza achkrie achku achschu achwi achwu ackt$ adioa adiu
adscha aebi aehlt$ aellt$ aemi aense aermste aersche aetzi aeuschte
agna agsge agst$ ahnho ahrge ahrne ahte aille ainie aki albu allie
aloe alta amtli amue andba andwi anfte anfue angi angst$ anhe ankie
ankt$ anns$ anru anspa apri ard$ armte arri arsch$ atrio atro atti
atza aucht$ aufbau auffae auffi auffo aufha aufklae aufrue aufzei aumi
auni aupta aupte ausflue ausi auspie ausrue bdrueck beeinfl bej bekr
benf beq berpr berschn bget bildsch blad blig block boes brand bruet
brut bstant bus cherw chgel chgest chgew chigst chkund chler chniss
chtslos ckeng cklichst ckmaess da$ dehnt delm dels denb destr diz dor
dreh dreif droh droht durchsch dyn eantwo echslu ecks$ een$ eer$ efro
eglue eheue eichba eidge eiem$ eiere eigu eimtue einfae einspa einstu
einwe eiss$ eitsi ektu elbi elbstbe elke elmue elsta eltre empfe empfu
enbae enbla enbli enmo ennt$ enpu enru enschwe enspe enstra enswue
ensy entde entrae entrie entschae entwei eplae erb$ erbea erche erfro
erglue erklu ermaue erneue errschte erto ertraeu ertro ervi eschnei
eschwoe estme estreu esue eswe eubau eundscha eurtei euste euzte evie
ezwu fahrt fakt fat fault fernspr feuert ffenb ffhalt ffiert ffnung
fften fgekl fgem fklaer freundsch fror ftigk fuell fuett gand gatt
gegl geiz genbl gendr ggeb giess gigst gner gnost gold graus greis
groess grundl gungsf haendl hebr heid heimt heizt hemm herl hinf hinr
hist hochw hrens hrheitsg hrungsm hrungsw ialste iate iba ichs$ ichtba
ichtslo iebha iebs$ iebu iefte iehba ielfae ienli ieti ieur$ iffte ifo
iftu igno ilm$ ilze impfte inns$ irdi irie irne irsche ischo issbe
itwe ixte jan jur kaes kampfb kav kels kies kitt kler krankh kratzt
kriegs ktat kteur kuenst kzent lacht laer laerm landw langl leien leih
lfaelt lfend lkig llens llenst lltet llustr loescht lopp lpunkt luftf
lwerk lzig mas meer mgef mger mien missb mkomm mlos mmes mmier moegl
mort mpfter mpfund mplar mplex mtet munt nachkr nachs naeht nanst
nbau$ nbruech nciert ndant ndeck nderst ndesm ndesw ndeut ndex ndniss
ndschuh ndten nersch neub nfalls nfang nfekt ngearb ngeln ngrupp
ngsbef ngsger ngsmassn ngsschein ngstigt ngtest ngvoll nheft nip nkels
nktem nland nlieg nmarsch nnaeh nntet nntlich nplatz nrat nrecht nsam
nsber nschalt nsier nsist nstat nstueck nszen ntad ntast nto$ ntrieb
ntritt ntwert nuetzt nut nverz nvestm nzten nzuf ob$ ocks$ oemte oerke
oeschte oesste ohr$ ohte olgsa ollmae onfli onstruie orn$ orpe ortho
orve otzte ouve paus plom pop portr ppernd ppier ppter proph ption
ptisch pulv rabl raecht raest raets rand ratschl raub rauf raussch
rbiss rche$ rchein rchest rdamm rdeck rdentl rdigt reakt rechtl regl
reizt rfilm rfuell rgedr rgeist rgert rgift rgleich rgter rind rlaeuf
rlangt rlebt rleumd rlin rmann rmel rmeld rmte$ rmten rnahm rnal rniss
rnten rntet roest roh rpol rresp rring rrtest rsand rschen rschneid
rschoss rschul rsinn rspring rstaatl rstech rstellb rstoss rsucht
rteig rud ruht rungspr rungsw rvier rwaehnt rwerb rzter rzuck saeng
saett sarb sart schbar scheh schelm scheng schert schind schmael
schmerzl schmueckt schoenh schritt schust schutz seem senst setzl
sfall sgeschl skuss slauf spitzb spond sprachl ssball ssendst ssenm
ssim ssist start sterk sterr stersch steur streckt streift stub
stuermt suedl supp tacht taets tauch taum tauscht tenh tenv terh terz
tionsf tkraeft tlant tlicht toer toet traenk trakt tramp triot troest
trott trueb ttent tterfr tuiert tungsv turb twend ucks$ uebsche ueckha
uecks$ uehmte uerfte uerzu uetu umrei umschi umspa umstri undli
undscha unfue unglei ungli ungsku ungspa ungsste unso unsy urchdri
urchfue urf$ ussio ustie utma uvo verpr vierz wagt wahr wahrn walz
wank wat weckt wegt werkst werkz wettb wich word wuenscht wuerz ymna
ze$ zeigt zell zerdr zersch zerschr zielt zins zufl zwung
""".split(): TRIPLE_SCORES[triple] = 3

for triple in """
^abkn ^abv ^aehnl ^aend ^altm ^amp ^anfr ^anschr ^aufschn ^auskl ^bloe
^dei ^dy ^einn ^entd ^entsp ^erschr ^erzw ^ess ^floe ^froe ^grie ^ign
^ing ^insp ^irg ^knue ^koo ^kru ^meu ^opf ^orth ^pfei ^pue ^quo ^rui
^schlau ^schwue ^seu ^sou ^umkr ^umn ^umstr ^umt abae abgie abkoe
abstrei abtre abve achmi admi aeda aehlba aehmte aelschte aelt$ aeltee
aerste aesthe aeufli aeune aftspo aftsve agd$ ahlbe aini aite ako akro
alse alts$ ampa ampfbe andle andma andre andse andslo andt$ angwei
anha ankba anlae anmu annae anno anto anwae arfsi armu arnie arnte
arro aschte aska askie aszi athle atschla attli atzfae atzt$ aubt$
aubwue auert$ aufbe aufdri aufei aufrei aufru aufsa auft$ aufwi aumwo
aure ausflu ausgea ausgie aushae auslau ausma awa ban baumw bbel bein
bgebl bged bgeg bgeschm bgeschw bhalt bkoemml blen blickt brutt
bschnitt bsetzb bstoss buendn bungsv bwand bwehr bwuerd ce$ chbez
cherz chges chisch chmach chstell chthab chtmaess chtsam ckendst
ckgest ckier ckiert ckisch dchen degr denkl depr die$ dieb diskr dopt
draeng dreist drog dross dte$ duft dunk durchm eagie eble ebraeu
eeilte eelle efri egia ehst$ eichmae eichs$ eichu eidsa eif$ eifu
eifue eiko einbu einschla einwei einwo eissu eistrei eitba eitma eitri
eitsvo ekru elki ellve elmi eltste emmu enblei enbre enbrie enfro
engae enkoe enkre enkrei enswi entfue entne entspa entspre entwa
entwue entzwei eoty epflue erfreie erfrie ergbau ergei erkma erpfle
erschlue ersei erspi ertae ertau ertroe erzwi esba eschmae eschmo eske
espei esste estru etreu euda euerbe eumde eut$ exo ezau fachk fachl
faehrt fahnd fdringl fegt felh fell feud ffaell ffeln ffier fftes
fgebr figst film fischt flach flag flasch flecht flekt flex fluess
frank frecht freg frev frueh frustr fsteig ftragt ftspol fuenfz fuerst
gaens geig genv gerl ggress gift glock glueckw gnis gnor grav greifl
grossz gruess gutm haemm haeuf haeuft hagl has hast hausb hells hemmt
herk heuch hex hltet hmef holz hyp ibt$ ice ichtbe icksa iedlu iefa
iegst$ ielbe iellste ienrei ierge iesste iessu ieste iffi iffs$ igfa
igtste ikta impli impu inkli innbi iose ipie ischt$ isrei istli itee
itli itti ittsa izo kaltbl kalth kampfg kanntg kaufm kaut keln kelnd
kennz klarg ko$ koff kogn kreis kreuz kreuzt krob ktest ktuell kuehl
lack laess lbes ldigst ldlich leck lehnt lehrb let leugn lfer lgeb
lgung lian lkend llenb llers llit llkuerl ltbar ltipl machtv maeld
marm marsch math mech mfort mgaengl misstr mitf mmenk mmenw mmiert
mmtet mmungsl mog monstr mpagn mpfang mpfes nabw naehnl naehrt nahr
nanl narch naussch naut nbaend nben nbind nbleib nbrief nbruch nchron
ndat ndef ndenk nderj nderm nderz ndger ndik ndnis ndslos nens nfahrt
nfrag nfreundl nfuhr ngefr ngegr ngels ngsanl ngsbed ngsbest ngspol
ngswert ngswuerd ngszeit ngtet nheb nheim niedr nint nkind nklag nkorr
nmin nmus nntnis noev norg npart nred nrent nrot nsaetz nsche$
nschluss nsgesch nsteck nstler nstoss nstreng ntan nterdr ntlass
ntreff ntsprech ntur nueg nverh nwachs nzust nzutr obo ocki oecki
oelbte oenhei oeve oha ohsto ohu olche olg$ omoe omte op$ orei orf$
orgli ormo ormte orstae ortra ossge ossha paed pak papp ped pein perm
pfaend pfiff phe$ phie$ phiert pid pien pil plaud ppet pptes progn
protz pult pumpt quetscht quot ragt ralt rarzt rast rats raubt rbaut
rbeh rbelt rbrannt rchgew rchit rchschnittl rdreh reinbr rentw reot
rerb rerl rflueg rfreul rfrisch rgesp rgessl rget rgum rhaetsch rhoeht
rhoer rhund richts risk riv rkant rkass rkennb rknitt rkreis rleh
rling rmarkt rmter rmuerb rmund rnacht roert rpart rrer rrier rrter
rsche$ rschiff rschreit rschrieb rstaedt rstein rstreich rstreut rterb
rtlichst rton rtraut rtreib rtungsv ruin rutscht rve$ rverb rverh
rvertr rvielf rvoll rvollst rvorr rwachs rweg rwerk rwes rwid rwort
rzahl rzelt saeumt samtb sar sbest schal scharfs schenb schenf schenkt
schenst schichtl schicks schief schlack schlang schlecht schliff
schmugg schnappt schnitz schrift schuecht schwaetz schweiss schweisst
schwenkt schwerf schwing schwoer segn seln set sev sgebl sil sinf siv
siz skont slaend slig sloes smen snahm spass spert spiell spitzt
sreiss ssenr ssenv ssenw sserb ssersch ssett ssungsv stadtb stall
stammt stan stech steil steng sthet stich streit stroemt stungs subtr
sunk sweis synchr ta$ taill tant tenk tgef tiefbl tiefs tionsk tipp
tnehm tow traecht tranch trenn treuer trik troed tschte$ ttelst tteng
ttenst ttler tupft tzfaeh uale ubve uchtba uchti ucksvo udi udiu
ueckse ueckste ueckza uehlt$ uehrba uell$ uelte uengli uenze uetsche
uetschte uftfa ugae uhte uldsa ulei uli ult$ ulu umgae umkla umle
ummte umre umsi umwa umzu ungsla ungsle ungspla ungsschei ungsta unru
unwa urde urt$ uru usio uske ussa ustria utrae utzt$ verpf vielg viers
vorn vorv waermt waesch wahlb wegw weichl weicht werkt west wetzt widm
wild win wirt woehn woert wohlw wuest wut xer xis ynchro zeitl zem
zens zerz zierst zisch zte$ zut zwangsv zweid zykl
""".split(): TRIPLE_SCORES[triple] = 2

for triple in """
^abschm ^add ^antw ^att ^ce ^drae ^dreie ^eign ^engl ^entn ^entt ^geae
^rhei ^ulk ^unq ^urspr ^vu achla achsa achtvo aechtni aengstli aeto
afge aftsa aftsge aftwe ahmslo akku akteu alb$ allfa allu andeu andsa
anlie anmae anntwei ansti apfte arsa arteii atli aubni auchs$ auerli
aufae auptge ausblei baeck baer beauftr bensb bepfl beugt beut bgefl
blind bliz botsch braust bsatz bschreib bsichtl bsteig bvent chmitt
christ chsicht chsvoll chtensw chweis ckenb ckens ckgang dankt deh
derf dim disz dueng dues durchschl durchst ebrie echtmae echzi egei
eglau egna egs$ egsa ehlte ehmu ehrsa eibt$ eibte eifba eig$ eike
eims$ einbre einbri eindru eingae einschrei eintre eisba eitrae eitsre
ekreu elbstae ells$ elma elsge elspie elstue eltmae elvo engu enia
enkra enmu ennue ennzei enri entia entsta enzfae enzioe eorie erblu
erdrei erfau erfli ergrae erhee erkru erschwo erspra ersteue ertha
eschmue euja exti ezeu falls fasz feilt ferl festz fleck floet folgt
franz freundl fuehlt fuerw fugt gard geistl genz gik gnung grossm
gungsl gymn hamm hann hauptg heimd hlgef hmlich hmslos hochb hochm
hoefl huehn hust iagno iblio id$ ielsi iensta ient$ ikte ilaeu illie
inkt$ insze iogra ionsko iote ipse irtli ittei itts$ izioe jamm jap
kaufkr kippt klemmt komf krut kuerzt lam langt lbild lbstaend leichtf
lenz lgel lla$ llehr lleng lmuet lsam ltgew ltsamst ltungs mad mehr
mmelw mmenkl mpuls mse$ muehs murm nabk nachm nahm nans nas nbefr
ndenb ndersch ndesr ndfest ndlos ndoss ndringl ndungsr ndwirtsch neh
nenm neuj ngenh ngernd ngleich nglisch ngsgem ngslag ngstig ngsunt
ngsweis nin nkenh nkett nklig nkrieg nktur nmass nmess nprob nreiss
nrenn nschrift nschwer nse$ nseln nspol nstift nstruiert ntaugl
ntbehrl ntial ntlichst ntlos ntschaed nwerk nzimm nzioes nzter oehte
oerni oessi ohl$ ohnli olgu ollue onfu onzi opha orfue oria orrae
orsti ortle ostbe ott$ ottie ozie pfeff phez platt pluend pptem praem
quael quem raeuss ramb rart rbeitsfr rbeug rbrechl rdacht rderbl rdet
reink rerst rfolgt rform rgaengl rgaenz rgers rging rglas rhab rhaengt
rhalts rholt riat rienr riums rkast rkenntn rlaeng rlaubn rled rleid
rlicht rmtest rmung rohst rotz rpress rquickl rrag rrschend rrtes
rschaetz rschluess rschuss rsetzb rsetzl rspieg rstaerk rstrich
rstuetz rsuecht rtraet rtrags rtraul rtum rueckl rueckschr ruett runs
rurs rverw rvoelk rwach rzust sald sbez schalld schleud schlos
schmackl schmerz schminkt schmirg schnoerk schreckt schrull schuel
schuerft schwerv sentl sep sfuhr sgep spaet spielh spuckt sruest
sshaft sslos ssungsf starrs stenz stoert stopft storb streitb streut
strial stron subv suess szin taend taeub taeuscht talg tankt tann tapf
taub taut teig teilb telt tgel tgest thlet tiefg tir tism top torp
tort trad traur tscher ttenb tungs tungsl tzenh tzpunkt uadra ueckwue
uenne uetzli uhl$ uickli uidi uittie ulau ulli umdi ungsfo unk$ unmi
unmu uno unsti untau uose urchzu uschaue uspri usst$ usstsei utwi vaet
vielf wahrsch weich weltl wisch woehnt wuerg wussts xe$ yse yti zei$
zern zett zim zon zuschr zweis
""".split(): TRIPLE_SCORES[triple] = 1


def word_groups(word):
    """
    >>> list(word_groups('weight'))
    ['w', 'ei', 'ght']
    >>> list(word_groups('eightyfive'))
    ['ei', 'ght', 'y', 'f', 'i', 'v', 'e']
    """
    index = 0
    while index < len(word):
        # Find some consonants.
        start = index
        while index < len(word) and word[index] not in VOWELS:
            index += 1
        if index > start:
            yield word[start:index]
        # Find some vowels.
        start = index
        while index < len(word) and word[index] in VOWELS:
            index += 1
        if index > start:
            yield word[start:index]


def word_triples(word):
    """
    >>> list(word_triples('weight'))
    ['^wei', 'weight', 'eight$']
    >>> list(word_triples('eightyfive'))
    ['^eight', 'eighty', 'ghtyf', 'yfi', 'fiv', 'ive', 've$']
    """
    groups = ['^'] + list(word_groups(word)) + ['$']
    for start in range(len(groups) - 2):
        yield ''.join(groups[start:start + 3])


def score_readability(word):
    """
    >>> score_readability('xxyhcwx')
    0
    >>> score_readability('schlomo')
    600
    >>> score_readability('schuhkarton')
    742
    >>> score_readability('produkte')
    1683
    >>> score_readability('bezirksschornsteinfegermeister')
    964
    >>> score_readability('bin')
    1766
    >>> score_readability('interessant')
    1537
    """
    result = 0
    triples = list(word_triples(word))
    for triple in triples:
        result += TRIPLE_SCORES.get(triple, 0)
    return result * 100 / len(triples)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
