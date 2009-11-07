VOWELS = 'aeiouy'
TRIPLE_SCORES = {}

for triple in """
^afl ^agl ^agn ^aim ^aiml ^airs ^alch ^antl ^artf ^artl ^asthm ^atl
^bei ^boyi ^brou ^buoya ^chao ^coy ^cue ^cui ^dua ^ear ^earw ^ebb
^eccl ^egg ^elf ^endl ^es ^euc ^eul ^foe ^fria ^gay ^ghou ^glee ^glue
^gno ^gray ^hey ^hue ^iamb ^ick ^iff ^inm ^inw ^ion ^irk ^joyou ^kle
^mue ^myo ^noe ^nua ^oak ^oar ^offsh ^oh ^oink ^onc ^onr ^ons ^ostr
^outsp ^outspr ^paye ^playe ^plie ^pneu ^praye ^pseu ^queue ^rha ^scle
^slue ^sly ^soy ^spraye ^spree ^spry ^spy ^sve ^sway ^thee ^throe
^throu ^trau ^trui ^ub ^um ^unstr ^unth ^upw ^urn ^wooe ^wry ^yacht
^yank ^yaw ^yawn ^yearl ^yelp ^yours ^youthf ^yowl ^yumm abdo abia
abla abste accrue achy ackbe acksla acly actle actly adioi adoe aeolo
affie afflue aggy agro ahi aica aightfo aimle ainclo ainde ainsai
ainty aipse aircu airdre airly airvoya ais$ aisle aithle aiths$ aito
aize aka aky alai alche alei aleo alf$ alfhea alfo alfpe algo alleye
alnu alta amboya amia ammie amna amoe amphi amsha amstri ancrea andme
andsha andsto andu andyi angue ankly anky antu anua anxiou anyo aordi
apeu apne apso arb$ arbli arbs$ archaeo arcti arda ardba ardshi arduou
arfs$ argle argoe argue argy arl$ arley arls$ armie arqui arshe artee
artfu arthe arthri artly arva aryi ashfu asma assee asthma asui atchfu
atchy atroo attooi atuou atwa aube aucou audu aughts$ auma aundry
auntie auri autu auxi auze avy awkie ayal$ ayba ayfu ayoff$ ayoffs$
aype azz$ ba$ bags bait bandw bard barf bashf bawl bbag bdom beans
bedd bee$ beek bees beis belt bend bent berc berth bests bets bhead
bied bienn bier bigh bilk bim bins bioph biq bir biz bjects bjoin blah
bleak bleat blec bleep blight blintz blissf bloat blond bloods bloodst
blowz blurt bmiss bnail bo$ boastf bobs bold boll bolt boodl bookk
boor bounds boy$ braid brash bratt bread breaks breathl brev brick
brickl brious brom brook brow brunt brupt bscond bscript bsoil bstrat
buckt bullh burp bux bvert byr cadd cantl cards cask cattl caulk ccabl
cceed cci$ ccinct cclaim ccles ccost ccul ccumb ccurs cdot ceans ceipt
ceitf cen cents cep cerv cey$ chain chair chairm cheep chess chest
chief childb childl chimp chink chirp chism chnocr choan chock chomp
chondr chord chords chow chuck churn cidl ciet cinct cion cisms citn
ckball ckberr ckboard ckboards ckies ckil ckish ckjack cklier ckliest
ckmark ckold cktrack ckwis ckyard ckyards clack clairv clamp clang
clank clasp claw cleft clerk clew clich click client cliq clist clists
clit cloak clock clomp clot clout cluck clump coats cochl coed cogr
cold comr conch conk coons coot cords cork corm cornfl corns cornst
corps cough couns cquer crafts craftsm cragg cramp crap crass crawl
crayon creel cres crest crew cribb crid cries cril crimp croak crock
crom croph croq crowd crown crudd cruel crumm cry$ ctac ctag ctanc
ctant ctment ctments ctrod ctuar ctus cud cue$ cued cues cuff cuing
cuit cull cumm cuum cyl daft dan dank darkl dart daunt dauntl dawn
dblock dcutt ddend ddish ddly$ dean dear debt deed deft deign dept
dersh desh dext dextr dful dgin dgings dhes dia$ diabl diac diacr diag
dicr dics dicts dientl dients digg dimw dio$ diocr diom dioth diox dip
diphth dishw disk dists diums djoin djourn dland dlessl doff dog doing
donn doom door dosc dott dought dound downh downst downw drang dras
drawl dread dreaml dren dressm dripl dripp drons drool drubb dsling
duck duff dug dulc dunk duod dverb dways dwink dwork dyg dysf dysl
dysp eacle eadfa eadth$ eadths$ eafa eafte ealie eamble eance eanly
eapi eaps$ earchi earmi eartbrea earthi earti eartie eartle earwa
eaux$ eavie eawo eb$ ebble eble ebroa ebru ebs$ eby ec$ eccle ecdo
ecie ecree ectiou ectra ectru ecue edhea edio ediou ediu edoe eece
eedfu eedli eekee eeklie eelie eera eest$ eeth$ eetle eetli eetly eeto
eeway ef$ efia eflie efly efs$ eftie egiou egma egri egro egue ehoo
eido eige eighti eightli eigle eigni eil$ eils$ einou eir$ eirde eire
eirs$ eisa eissue eitfu eiti eize elaye elayi elfle ellae ellhea
elliou elm$ elms$ elp$ elpi elple elrie elry emcee emme emne employa
emptio empts$ enchma endie endle endue eneou eneu ength$ engths$ enhea
enio enma enpo enro ensue ensuou enth$ enths$ entrie envia enviou eny
enzie enzy eocla eocra eof$ eonto eopo eosta eousne equie equiou erbea
erbrai erbree erche erclo ercou ereu erfee erfoo erg$ ergie ergree
ergs$ ermou eroe erryi ersea ersia erslee ersprea erstru ertia ertie
ertz$ ervou eryi esai esbia eshme eshoe eshri eski espea esple essayi
estli estrie estroye etiou etoe etraye etty euca euce euda eudo eulo
eupo eura eure ewhe ewly ewoo ewswo excla exie expla exta extrao exts$
extu extua eyance eyes$ eyor$ eyors$ eze ezoi fab fabl faith faithl
farc fart faun fawn fear fearl feas feast feign feint feist felt ffaw
ffest ffeur ffian ffies fib fich fics fid fields fiend fights fink
fisc fiss fiv flail flamm flank flaunt flaw fle$ fleck flects fles
fleshl flet flig flock flogg floor flout fness foal fog fogs foils
foist folds fopp ford fork forth forthr fortn fours frail frain
fraught freed freeth freew fretf friends fronts frown frowz frug
fruitl fties ftly$ ftness furt gadg gait galv gang gaol garg gasp gear
geth gew geys ggan ggar ggards ggie$ ggings ghett ghneck ghost ghtail
ghtedn ghtforw ghtheart ghties ghtil ghtlift ghtmar gia$ giant gift
gild gimp giousl girl girt gladl glean glect glint glio$ glios gloat
glut gly$ glyph gmas gnabl gnan gnantl gnaw gnpost goad godf gong good
goodl goons gown grabb granc grands grasp great greeing grisl groan
gron grooms grot grout growl grunt gsaw guan gubr gueing guild gulp
gun gunr gus hagg hail hairc hairdr hairl halfh halfp handsh hardb
hardl hardt hardw hark harmf harml harps harsh hays headr healthf heap
heartb heats heed heedl heel hein heir heist helpf helpl herd hertz
high hinds hitt ho$ hogg hogs hoist honk hoof hool hoop horm hugg hump
humpb hunchb iabe iaca iacri iad$ iads$ iago iaise iannua iars$ iasi
ibia ibli icrou icue iddy idli idshi ieba ien$ iencie iendi iens$
ientiou ierci ierie iery ieti ieto ieute ieze iffy iggly ighbo ighs$
ighteou ightli ightma ightni ighty ilch$ ilio ilki imbue imia impy
imwi imy inbo inbree incia inctly incts$ indro infre ingma ingne ingti
inho inle instri invio invu inwa inx$ iode ionme ionth$ ionths$ iophy
iose iosy iouse ioxi ipbui ipco ipie ipma ippy ipre iprea ipsi ipso
iptoe iptu irch$ irchi irco irdi irdie irdle irst$ irsti irtuo irtuou
iscue isdo isee isfyi ishee ishwa islea isloya isp$ isps$ issfu issu
istie istrie ithho ithie ithme itli itru ittli itzi iumpha iwo ixtie
jab jag jah jahs jan jaw jets jilt joint jolt jott joust jov jug juj
jumps kayak keel keeps keout keouts kesp ketch kfast ki$ kie$ kiln
kirk kith kked kkeep kking klept klies kmak kmark knell knobb kul laam
labr laid lamm larc larv lasc lawf lawl layed layer lboard lbow lbum
lcast lchem ldbrick lderm ldew ldproof leap leew leid leis leont leps
lesb lesm leum lewd lfed lfheart lfill lfing lform lful lgent lgic
lgor lgrim liant lidl lied liefs lieut lignm lilt limn limps lint lio$
lious liph lipr lips lishn lisp liss listl lken llant llants llast
llback llbacks llects llhead llick lligr llionth llionths llipt llium
llmark llon llons llots llout llov llown lluv lmet lmier lmiest lmistr
lmol lmy$ loed logn loh loing loom loons lord lordl lors loudl loudm
lout lows lphin lroad lsam lsom lsor ltant lthin ltier ltiest ltreat
ltruist luabl lucr lugg lums lurk lusc lustr lying lysts maim maind
mands mank marks marksm mars matchm maul maw mayor mba$ mbas mbent
mbfound mbil mbiv mbran mbroil mbryol mburg mbus meek megr meld mels
melt mends menf mewl mia$ midd midl mids midsh midt miff milks mindf
mindl mins mitr mium mmac mmal mmel mmels mmogr mnamb mnast mnes mnit
mniv moat moeb moir morb moult mound mounts mouthw mpacts mpad mpern
mphib mphlet mphon mpion mplais mpler mployabl mployed mploym mpness
mpon mpoon mprint mptuous mpud mpugn mrad mshaw msic msier msiest
mstant mston msy$ muc mund murr murs myop nabr nabs nachr nae$ naed
naing nalg nantl naps nart nauts nays nbolt nbon nburn ncamp ncand
ncav nceal ncent nchal nchantm nchants ncial ncient nciest ncils nciv
nclasp nclean ncleanl nclear nco$ ncoh ncoil ncomb nconsp nconst ncork
ncos ncrypt ncter nctly$ ndab ndals ndan ndard ndbag ndbags ndburn
ndcraft ndcuff ndentl ndfold ndful ndied ndiff ndim ndisc ndlin ndmaid
ndmill ndous ndousl ndpick ndproof ndries ndshak ndstands ndston
ndsurf nducts ndue$ ndum nears nearth necd necks nect nees neigh neit
nempl neocl nep nept nert newl newsw newt ney$ neys nfair nfaithf nfel
nfern nfield nfight nfir nflow nfluent nfolds nfolk nforms nfort
nfrock nfuls nfurl ngbird ngbirds ngef ngentl ngents ngeon nghead ngic
nglem nglet nglor ngodl ngoes ngoing ngrain ngsong ngster ngsters
ngue$ ngues nguist ngulf nguor nhealth nhood nhook nient nientl nift
nigh nightm nimp ninh ninj nior nits nkag nken nkets nkfull nkie$
nkindl nkroll nkrupt nload nlock nman nmanl nmann nmask nmit nneal
nnual nnul nochr nodd noint nonch nonf nonm nonsm nonst nont nown
npack npeck npleas nprick nprov nquet nquir nreal nref nreg nrest
nrestr nrip nris nrunn nrush nsack nsaf nsaw nsciousl nsciousn nscrew
nscrup nseal nseat nself nsets nshin nships nshroud nsig nsill nsinc
nsmiss nsmok nsnarl nsomn nsoms nsound nstab nsters nstill nstinct
nstopp nstrain nstream nstrip nstructs nsual nsuit nsumpt nsvest
ntaint ntang ntank ntant ntasm nteb ntee$ nteel nteer ntees ntends
ntful ntfull nthem nthink nthlies nthly$ ntied ntifr ntist ntists
ntler ntlessl ntlessn ntomb ntoon ntouch ntous ntrac ntrast ntrepr
ntril ntrit ntrust ntual ntwist ntying nu$ nuend nuin nuousn nup nuts
nveigh nveil nvents nviabl nvuln nward nwards nwheel nwill nwork nyl
nyt oacha oachme oacti oaf$ oafe oam$ oana oare oastfu oastie obblie
obei obla oblo oboe oboi obsti obviou ocha ocho ochro ocie ockey ocksu
ockwi ocs$ octe oddie oddli oddy odyi oebe oele oenai oerce offse ofli
ofti oftie ofts$ ogle oica oigna oilie ointle ois$ oism$ oit$ oita ok$
olea olf$ olfi olks$ olme oloi olye ombre omey omna omnia omplia omra
oncha onchi ondle ondria onfla onflue ongfu onghea ongruou ongue onk$
onks$ onru onry onsmo onthlie onthly onwa oobe oochi oodooi oodshe
oodstai oodwo oogie oohi ookkee ooky oollie oonie oopy oorma ooty
oozle oozy opco ophre opoeia opple opto oqui oquy ordu orei orkma
orldly ormle ornea ornsta orny orphou orque orsi orswea orthri ortli
ortni ortsi oryi osce ossbo ossbree ossy ostdo ostli ostly ostmo otle
otro ottli oubli ouchy oudmou oughly oughtfu oughtle ould$ oulfu ouli
oundly oundwo ounse ourci ourge ourly ourma ourn$ ourns$ ousle ousse
ousy outbi outbrea outbu outca outru outshi outspo outsprea outwa
outwea ovia owbi owdy oxiou oyal$ oyally oyalty oyers$ oyle ozo pa$
pab paid pain pancr pang pastr pats paup pawn pay$ paying pays pbraid
pbuild pchuck peak pect peds peel pelt penc penl pesk peut phall phapp
phe$ phics phlegm phom picc pidl pids pient pigm pigr pins pinstr pint
pism pkeep plaid plaincl plait plank plaus playact playf pleat plectr
ploy$ ploym ploys plunk pments pness pneum pods pogl poign pointl pons
pooh pool poop poor porr portm posth posts pour ppall ppanc ppears
pperm ppest ppie$ pplant pplaud ppoints pprob pran prawn preem preen
pregn prick priest priestl primp prints proar profl proofs proud prox
psalm pseud psies psis psod psom pstart psticks pstream ptab ptain
pters ptist ptoc pturn pudg pult pung punk purr pwreck quaff quail
quaint quals quan queath queen queenl quell quen quests quets queur
quial quicks quies quins quitt quoit ragt rails rantl raph rapl rarm
rast ratr rats rauc rax rbag rball rbic rbiv rboil rborn rbroil rbug
rbugs rbul rby$ rcem rchaeol rchant rchet rchiefs rchist rcials rcil
rclaim rcoats rcock rcond rcook rcours rcrowd rcup rcur rcut rcuts
rcutt rdains rdanc rdep rdhead rdheart rdial rdil rdiol rdle$ rdled
rdles rdless rdo$ rdroom rdrooms rdship rdsman rdsmen rea$ reaft reag
rear rearms reckl rectl rectn redh reds reek reens reer rens reof
respl resq restl reup rfboard rfects rfeits rfid rfuck rgans rgast
rgeons rgetf rgist rglar rgle$ rgled rgles rgling rgoing rgos rgrad
rhaul rheat rhod rianc riant riats ricks riet riffs rift rightf rink
rips rishl ritz rjacks rkill rkscrew rlain rlard rlay$ rlays rldly$
rler rlers rlessl rlessn rlick rlink rload rlocks rloins rlook rlorn
rlough rmaid rmaids rmail rmaphr rmeabl rmest rmezz rmind rmint rmoil
rmong rmouth rmur rnals rnier rniest rnip rnist rnith rnments rnrow
rnstorm rnums rny$ roads roar rocc roes roff roil ront roof rousn
royal rpinn rplay$ rpoon rports rprets rpus rquet rraign rral rrals
rran rrants rrest rrets rril rsault rshal rshot rspac rstock rtail
rtals rte$ rtedn rthern rthly$ rthog rthogr rthrit rthwest rtill
rtless rtlessl rtling rto$ rtogr rtook rtsight rtuos rturn rtwheel
rtyr rund rut ruthl rvants rvel rvert rvier rviest rvit rvy$ rwaul
rweav rworks rworth ryb ryl ryll sagg saic sak sandst santl santr sap
saps sars saurs sbands scaff scals scard scarf scell scends scens scet
schew schief schiev schism scind sciss sciv scoff scoop scorn scort
scounts scout scowl scraggl scrawl scrawn scream scrimp scripts scroll
scuff scurv scuzz sdain sear sects sedl see$ seech seen sek selfl serg
sfied sfunct sfying sha$ shaft shark shawl shbuckl sheet shield shirt
shoal shop shops shorth showm shrewd shriek shrimp shroud shrunk
shtail shuck shunt sigh silt sioth sium skein skel skiff skit skulk
skunk skywr slaph slatt sleev sleigh slew slex slier sliest slitt slog
sloth slough slumm slump slurp sma$ smansh smarm smear smirk smit
smock smog smogg smogr smos smount smutt snack snail snarl snazz sniff
snort snout snows snowsh soar sobr sodd softw soil sols sombr soms
soon sooths sop sos sott sough soulf soundl sounds spark spawn spear
sperms spew sphalt spiel spier spiest spinst splay$ splayed splaying
splays splitt spont spoof spool spoons spoor sportsw spout sprain
sprawl sprout spurn spurt squall squawk squeam squiet squirt sread
ssals sscheck ssee$ ssees ssels sserts ssest ssets ssfull ssingl
ssists ssmak ssments sso$ ssock ssocks ssoon ssort ssos ssue$ ssues
stabb stacks staid stals stan staph stats stav stcoat steadf steb
steem stein stend step stial stib stid stingl stint stir stless stmark
stomp stoon stoop stout stproof straightf stral strand straw streat
streetw stren strew strials stricts strong strum strums strustf stunn
stunt stying styp such sudd suic sultr svelt swam swarm swarth swashb
swellh swill swimm swims swin swoon swoop sword symph syncr tacl tactl
taff taill taint tards taunt tbell tcall tchets tchfork tchin tcom
tcropp teak team tects teem teens teh tells tels teous terl tesq tests
teurs tfall tfalls tfield tflank tfoot tform tfuls thank tharg thaw
thball theast thel theocr theos therb therf thies third thistl thlessl
thlessn thmet thnic thog thold thons thoughtf thoughtl thrall thread
threes thren throb throng thsom thstand thumb thump thwack thwart thym
tial tie$ tied tienc tiff tifs tilt timp tind tio$ tios tiousn tland
tlast tlaw tlessl tlights tlock tlook tod toff toing toj told toms
took toon toot topm topp torn tosph touts towh town towns tplac tproof
trabl tracks trains tranc trank trar traum trig trist trists trod
tromp trous truant trunk trustf truthf tryst tshin tsmart tspok ttals
ttant ttee$ tteer ttees ttempt tterbr tterm tterns ttingl ttoes tuar
tubb tuft tuous tups turf twalk twang tweak tweigh twit twits twos
tying tzier tziest tzy$ uabble uana uant$ uardia uaria uarre uasio
ubcu ubdue ubiou ubstra ubte udy udyi ueale ueami ueegee ueere uencie
uery uesti uffoo ufti ugga ugly uh$ uies$ uiggle uild$ uilds$ uilte
uilti uino uism$ uitle uito uitte uizzi ulbe ulche umblie umni umpba
umpli umpti unchba uncoo unctuou unfla ungu unhe unia unle unmo unna
unno unplea unpri unscru unsmi unsou unsui unthi untie untle unto
untou untrue unwe uode uppie upply upplyi upse uptuou upwa upyi urble
urbu urche urchi urd$ urdli urea urfi urfs$ urki urly urp$ urpli urps$
ursui urva urve usciou usky ussle ustli ustly uthle uths$ utts$ utty
utua utz$ utze uxo uzz$ vagr vails vain vall vand vars vaunt veb veer
veil vein verspr verv viatr vich vidl views viousn vishl vix voids
vour vout vows voyeur vvied vvy$ vvying waft wagg waif waist wardl
watchf wayw wbeat wboard wdier wdies wdiest wdin wdown wdust wean webs
weeds weft weir wend werl wetl wett whack what whats whead wheat
wheels whelp whew whid whiff whizz wield wight wildf wilt wink wintr
wist wistf wiv wkward wnload womb worms worn worsh worst wov wow wplow
wrap wrath wreak wrest writt wrongf wrongh wrot wry$ wse$ wsworth wtow
wwow xabl xcerpt xclaim xclam xia$ xier xiest xill xins xiv xom xorb
xpert xplan xpound xswain xtern xtraord xub yache ychoa yde year$
yest$ yhoo yieldi yings$ ylli yllo ymbio ymie ymou yncra ynx$ yolo
yon$ youthfu yr$ yrs$ yru ysfu ysle ysm$ ysms$ ysy ythmi ywhe zards
zarr ziers zies zirc zod zoid zont zoom zophr zzard zzards zzer zzin
zzler zzlers
""".split(): TRIPLE_SCORES[triple] = 1

for triple in """
^ackn ^addl ^airbr ^airdr ^airf ^aisl ^alp ^ambl ^andr ^angr ^anx
^archb ^arts ^bau ^bay ^bayo ^bloa ^blou ^boui ^cai ^chry ^clau ^clie
^cloi ^clue ^coau ^crayo ^crie ^croa ^diu ^doi ^dwi ^eagl ^earthq ^eb
^ecst ^edd ^eid ^ek ^emc ^ensc ^ensn ^entw ^erg ^eur ^ew ^eyeb ^eyes
^flui ^gao ^gha ^ghe ^gia ^gly ^groa ^hoi ^iv ^kaya ^kha ^layo ^lieu
^lla ^mae ^nay ^ogl ^onl ^ooz ^ophth ^oth ^outcl ^outfl ^outg ^outn
^outsh ^outsm ^outv ^owl ^phia ^phle ^phoe ^pio ^plia ^prou ^psa ^pue
^quoi ^schlo ^schma ^schmoo ^schu ^screa ^scy ^shei ^shoa ^shrie
^shrou ^skei ^skie ^slei ^smea ^snai ^snou ^sphi ^sprai ^sprou ^sque
^stei ^trie ^twea ^ul ^unbr ^undr ^unj ^untw ^unz ^upch ^upgr ^upstr
^uv ^vea ^voyeu ^yamm ^yearn ^yeast ^yest ^yield ^yipp ^young abbli
abno absce absco acca acclai aceou ach$ achme achro ackba ackboa ackfi
ackja acklo ackpo acksa ackspa acksto ackstro ackto acktra acku acou
acsi actme actne actre acuu addu adee adje adjoi adlo adly admou adne
aeria aerie aggli agglie aggrie agia agio aglio agreea agua aho aigne
ailga aille ailroa ailsto ainle ainma ainsa ainstrea ainy airdro airma
airmai airne airsty aissa aistcoa aith$ aitja akeo akeou akeu alaa
alba albu alfu algi alkie allma alma almie aloi altie alty alui alvi
amie amoo amphle ampie anbe anch$ andcra andcu andho andmai andou
andsli andwa anee angio angua anguo angy ankne ankro annea anoe anspa
anthei antho antme antrie anya apboa aphra aplai applie appri appu
aproo apt$ apta apto aqui arao arboi arbroi archai archbi ardli ardy
area arf$ argu arn$ arns$ arnsto arpo arpoo array arru arsa arsha
arshi artri artu artwhee asco ashba ashboa ashca ashy aspha asseu
assle assma assoo assua astly astne atboa atcha atchba atfi atfo atfoo
atha athei athlo atla atna attu atui auci aucu audie auffeu aughi aul$
auls$ auna aunch$ aunchie aundi aupe aur$ aureo aurs$ auvi avea avie
avio avvie awai awbrea awdu awk$ awks$ awny awo awye axie ayable ayday
ayfa azoo azy azze azzie azzli bacch bach backd backtr ballp bang banj
banq barm barnst batch bathr bayon bberg bbern bbet bblier bbliest
bbly$ bbyh beach beagl beak beam beard beastl beav beel beetl befr
belch bench berd beth bhorr bick bigg binn biops birch birth birthr
bish blabb blackj blackl blackt blad blanch blar blarn blear bleas
blench blesp blew blindf bliq bliss blist blith blitz bliv blockh
bloodth bloss blott blous blubb bludg bluepr boats bobbl bobsl boggl
boist bolst boo$ boog booksh botch bouill bould bov boyc bpoen brainst
brainw brais branch brar breach breakf breast breed brett bridl brin
briq brittl broach broc bronch bront bronz browb brun brunch bscess
bsist bsolv bster bsum bted btitl btrud bucc bucks bugs buk bulb
bullsh bunch bundl bunt burbl burs busb butl buttr bviat byp byw cabb
cackl calv camps cartwh casc catb catc cauc caust caw ccal ccan cced
ccessf cchan cclud cco$ cec ceed cesh cest chaf chagr charbr chauff
chauv checkm chel chets chi$ chiatr chich chid childpr chintz chipp
chirr chitch chments choic chortl chot choth chowd chrys chsaf chubb
chuckl church churl cients cind ciol citl cits ckax ckdat ckel cketf
ckfir ckhamm ckhand ckknif ckleb ckless cklist ckmat cknam ckout
ckouts ckpil cksaw ckspac ckster ckstrok claims clapb clash clatt clav
cleanl clect clem clench cliv clobb clockw cloist clop clust clutch
clutt cnick coauth coax coch cockl cok combs conds corkscr cornr cosp
costl couch courtl cous coust cowb cowh cowl coxsw cquis cquitt cradl
crann creos crep crev crims crin crippl cris crisscr crist crossbr
crossch crouch crumpl crush csim ctab ctal ctedl ctful ctfull ctress
ctroenc ctrol ctrom ctron ctropl ctrosc cturn ctyl cumb cuousl curdl
curts cuss cutt dach dad daddl dandl dangl dapp dappl daz ddens ddin
ddler ddlers ddock dduc ddying deac deact deadb deadp deej deesc delv
denh denz deod deogr deot desm desw deuc dgep dgier dgiest dgy$ dhous
diap dib dibbl diddl dimpl dink diousn dipp dips disch ditch dith divv
dject djudg dlands dlight dman dmen dod dodd dogtr dons doorm doorst
dork dorn douch dough dous dowb downgr downl downpl downsc downt
draggl drench droit drom drov drown drugg drumm dryw dthirst duch
dumbf dund dusk dway$ dwindl eably eacha eadle eadpa eadwi eaffi eakfa
eakne ealth$ ealthfu ealthi ealthy eamy eanlie eanne eano eants$ eanu
eap$ eapfro earga earhea earke earle earm$ earme earms$ earn$ earns$
earsi earth$ earthe earthqua earths$ earthwo eary easpoo eassi easts$
eastwa eathle eatme eaty eava eavy ebee eboo ebri ebro ebui ecau eckma
eclea ecoa ecoi ecs$ ecsta ectroe eeable eeba eechi eedba eedo eefe
eeho eekie eelba eema eemlie eenli eente eerle eesa eesca eetie eeva
eewhee eexa eexi eezie effo efoo efou efrai efrau efrie efy efyi egai
eggie egla egoa egroo egy eide eightee eigns$ eili eimpo eina eini
einse eity elai eldi elds$ ellho ellio ellya elpe elpfu elva embi emli
emma emmi emoa empha emptie emsti encla encry endri endro enee enfee
engo engro engu enjoi enjoy enlie enni enny enpe ensco enshri enshrou
ensna ensua entai enthou entme entru entwi enty enui enwa enza eode
eona eonho eope eophy eorde eoro epee ephra eplay eprie equea erboo
erbru erbs$ erclai ercoo ercro eree erfro ergra erhau erja erkie erks$
erlay erloa erloo ermai ernmo erpay ersau ersna erthro ertne ertwi
erty ervo erwau erwea esau eschoo esha eshu esio esli esmi espoi espoo
essee essie essu esswo estau estee estme estoo estry estuou estwa eswi
eswo etchie ethni ethno etproo etrai ettli eup$ euphe eups$ eutra evai
ewai ewde ewee ewhi ewy exclai expou eyba eyco eyeba eyeli eyno eypu
eystro ezvou facs faithf fann farmh farr farth fax faz feedb fett
ffects ffick fford ffront ffur fibb fickl fict filch finn fisht fist
fizzl flagst flapp flar flashb flatb fled flimfl flinch flint flood
floss flot flounc flound flumm flurr flust flux flysp folks foolh
footb footh footl footn footst forl forml fortr fost fourt fowl foxh
foxtr fragr frazzl fread freckl freest freewh frenz freshm friez fring
fritt friv frizzl frump fterb ftersh ftil ftin fudg fust futz gabbl
gamb gangl gaph garbl garch gargl gars gash gauz geabl geek geld geod
geon geonh geous geousl gerr gett ggedl ggedn ggriev ggyb ghastl
ghhous ghly$ ghness ghostl ghtfull ghtless giar giml gingl gins gions
girdl glac glanc glimps glist glitz glott glov gmir gnac gnash gnes
gnett gnments gobl god goggl going goldbr goldf gond goss gott gourm
grandd grandf grandm grandp grandst grappl graz greeabl greem greenh
greet gren gric grid griddl gridl grind gripp gris gristl groc grop
grounds grous grov grow grown grues grung guardr guards guesst guest
guill guous gurgl guss guts gyps ha$ hackn hailst hairbr hairp hairst
hallm hamp hamstr handcr handp harl harn has hassl hatt haunch haunt
haws headb headm heark hedr heeh heml hemst henc henn henp hep hight
highw hills hiss hitch hoar hobbl hoed hok holst hoodw hoor hopp hopsc
hord hound hubb huckst huddl hul humb hunch hungr hurtl hush huss
hutch iabo iano iape iathlo iats$ ibbli ibo ibre icea ichi icio ickba
icklie ickly ickna icko icku icli idlo iduou iega ieldi iels$ iene
iera iese iesta ifli ifs$ iftee ifty igee igh$ ightai ightclu ighthea
ightlie ignpo igri igsa igua igza ihe ildproo ilgri ilhoue iliou ilks$
illbi illbo illfu illne ilou imeo imfla imle imly immie implau implie
imply impou impra imro imsha imso inai inbou inchoa indbrea indbu
indfo indfu indly indmi indne indsto indsu infie inga ingbi ingbo
inglie ingoi ingrai ingre ingso ingsto inhea inky innue inpoi inpri
inpu inth$ inths$ intie inuou invoi inwhee inxe ionle ionnai iophi
iotee ipboa ipla ipme ippo iptea ipto ipwre iqueu iquo irea irki irms$
iroue irro irstie irta irte irtee iscui isdea isgru ishbo ishea ishtai
isju iskie isli ismou isno isphe isplay ispri isquie isrea isro isscro
isste istlie isua itchfo itchie itee ithsta ittee itto itz$ itzie ivie
ivoua iwee ixtee izzli izzy jackh jacks jad jangl jaund jawb jeal
jects jeer jew jiggl jimm jing jingl jinx jiv jobb jogg joggl josh
jostl jounc jugg jumbl junct kag kang kaz kerch keyn keyp keystr kies
kipp knack knav kneec knif knight knitt knowl kosh kowt lacq ladl lae$
lagg lain lak landf landm landsl lantl latch latr laws lbas lbox lcan
lched lching lcif lcin ldier leach leapfr leash lects lee$ leech lees
leh lemn lepr lept lfunct lgebr lged lging lhard lhouett liab lids
lie$ lienn lightn ligr lind lindr lios lipst lishl lkin llae$ llain
llbind lleag llenn lletpr llfight lli$ llib llips llist lliv llous
llpap llston llur llurg llyach llyb llyc llyd llyf lmat lmen lments
loam lobst lol loph losh loud loung lox lpabl lsed lses lsing lsions
lsters ltil ltry$ lued luing lul lurch lush lvan lvers lwom lygr lypt
lyst madr mainstr malt mam mamb mandr mangl maph mapp marbl matchb
maund mayfl mbal mbarg mbib mbitt mblanc mblaz mblings mbob mbold mbon
mboozl mboss mbow mbrac mbrag mbranc mbrell mbush meand measl medl mef
mek meogr mep merm mesh mewh mfit midg milkm mipr mirr misj misn misph
mizz mlet mme$ mmerh mmingl mmock mmor mmort mmur mnat mniat mning
mois molt momm mont moonsh moor moot mopp mord morn morr mosq mothb
motl mottl moufl mouss mouth mpag mpair mpecc mperm mpets mphat mpin
mplant mplaus mplish mplod mplor mpract mprob mptions mptiv mros
mscrib mson mstanc mstitch muddl mulc mulch murm muscl mushr muzzl
mvent nach nacl nactm nail nasc nass nball nblock nbos nbuckl nburd
nbutt ncak ncann nchar nchers nchier nchiest nchoat nchol nchron nchy$
ncier nclav ncond nconf ncongr ncord ncoupl ncov ncroach nculp ncurs
ndang ndbagg ndear ndeer nderbr nderch nderd nderpl nderr ndersc nderv
ndescr ndezv ndfath ndil ndin ndis ndler ndlers ndlessl ndoggl ndown
ndows ndpap ndpip ndry$ ndsid ndslid ndwich ndying nearl neckl nee$
nels neon nerd neth netw neut newb nexpl neyb neyc nfall nfant nfantr
nfast nfeebl nflam nflex nforg nfound nfreq nfriendl nfut ngainl ngbon
ngeabl ngeal ngend ngerpr ngings ngler nglers ngness ngorg ngos ngross
ngruit ngual nhead nheads nhing nhitch nhors niall nias nickn nid
nightsh nigm nih nik nins nippl nkabl nkin nkings nkness nknow nlac
nlatch nleash nloos nluck nments nmesh nnacl nnair nnects nnerv nnes
nnib nnied nnin nnonb nnos nnow nnuat nnuend nnying nob noes noids
nond nonpl nonv noodl noon nosh nost nostr notch npoint nquil nquot
nrag nrapt nreas nrich nrul nry$ nsabl nsaddl nscient nsconc nscot
nscrambl nseas nseeml nsep nsest nset nsettl nsfix nsheath nshrin
nsightl nsil nsnar nson nsplant nster nstorm nstranc nsubst nsupp
nsurr ntail ntanc nteg ntenc ntents nterb nterbr ntersp ntertw nthous
ntiar ntib ntics ntig ntih ntingl ntiousn ntith ntle$ ntled ntlem
ntles ntless ntling ntral ntranc ntrench ntress ntrus ntrym ntryw
ntwin nudg nuit nuk nuousl nurt nuzzl nveigl nvoc nwield nwis nworth
nymph oadblo oak$ oake oaki oaks$ oame oami oamie oani oapbo oari
oasti oautho obey obnai obsle obvia oc$ occo ockle ockma ockou ocky
ockya oclai ocoo octu odeo odlie oefu oence oeti ofou ogey ogga ogia
ogtro oiffu oire oisti olca oldbri oldfi olee oleu olfe ollea omeo
omia omou ompla ompri onai onba oncho oncla onfli onfou ongea ongo
ongrui onho oniu onke onpa onplu onqui ontie ontoo ontou onze oodoo
oodthi oody ooge ookou ookwo oolha oolo oomie oorste ootba ooths$
ootno oove ophtha opri opro opsco opse opyi orai oray orbea orca orch$
orchi ordai ordo orgo orio orkscre orlo ormie ornro orphe orpoi orrha
ortcha orthwe ortme ortoi ortre ortsma osai ospo ossba ossche ostda
osteo osthe ostlie osto ostri ostru otchie otgu otha othba othei othie
otli otsho ouchsa oudi ouds$ oufla ouga oughhou oughts$ ouls$ oundproo
ourtee ouste outcla outfie outfla outfo outhea outloo outnu outo outpe
outpu outrea outsma outsou outsta outstre outstri outvo outwei outwi
owbea owbo owgi owla owly owma owmo owngra ownloa ownsca ownsi owpa
owplo owroo owth$ owzie oxswai oxtro oyable oyali oyance oyco oyer$
ozi ozoa pad paddl padl painf paltr pamphl parb parch paths paw
pboards pbox peas pecc peck peek pels pelv pends penth peon pestl
pgrad phel phren phthalm phyt pia$ pickl pics piddl pif pigl pilgr pim
pinc pinch pinh pinp pinpr pinwh pion pipp pis pisc piss pitchf pitt
pix plain plasm platf pleb pledg plied plight plumm plying poc pockm
poes polk pooch porc porp portl postc postl potp pots potsh pouch
poult pounc pout poww ppabl ppag ppe$ ppeal ppen ppert ppes ppets ppil
ppliq ppris prat prattl preambl preex preord presch prest prid priev
primr proct proff prog proot pror prosth prun pscotch psiz pstag psurg
pteas ptest ptil puddl puk pum pump pyc pyx quack quagm quak quapl
quas quash quench quet quing quipp quy$ raffl ragl ragr raill railr
raj ramr rankl raphr rapt rarch ratch raunch ray$ rays razz rbec rbell
rberr rbik rbin rble$ rbled rbles rbling rbol rbons rbook rburd rcast
rceas rcel rcess rchand rchbish rcial rcif rclassm rcle$ rcles rcraft
rdess rdhous rdigr rdit rdlin rdling rdur readm reaff reappl reaw
rects redc reem reenl reent reest reex reff reimp reiss renn reol reop
rephr rept resch retch reuph rext rfar rfic rflow rgain rgar rgath
rgett rgoes rgum rhand rhang rhomb rhym ribb rich ridd riddl rieg
riffl rimp rio$ riph ripp rippl risc rkat rkin rlac rleav rlesq rlets
rlift rlud rmad rmanc rmand rmatt rmeat rmet rmhol rmier rmiest rmish
rmists rmitt rmly$ rmos rnac rnacl rneck rnel rnets rnfull rnings
rnly$ rnmost rnogr roadbl roadw rof roon ropr rors rost rouett roug
roughh rounds rphem rphic rpiec rpois rpric rreach rren rrents rreot
rrer rrestr rrhag rringb rrors rros rround rrup rryc rsell rsesh rsewh
rshad rshoot rsiz rsons rspers rspic rstepp rsting rstit rstud rstyl
rsuad rsuppl rtaint rtchang rtent rterb rthed rthquak rtibl rtied rtig
rtments rtner rtois rtrait rtress rtridg rtscast rtwin rubbl ruffl
rumb rumpl rums rup rusc rush russ rustpr rvad rvedl rver rvil rwards
rweights rwhelm ryng sa$ sach sack saintl salm sandw sarm sas saun
saunt saut sawd sbeh scald scann scarl schanc scharg schlock schmaltz
schmooz schoolb schuss scienc sco$ scold scomb scomm scond scord
scotch scourg scourt scrabbl screen screet scrimm scrimsh scruff
scrunch scrupl scub scuffl scupp scurf scyth sdropp seaf seash seek
seem seeml seep sents serm setr sfir sgorg sgov sgruntl shackl shambl
shamp shandl shangh sheart sheep shells shelt shelv shings shions
shipm shipp shirr shitt shoeh shon shopp shopr shortch shorts shotg
shout showc shredd shrew shroom shudd shush shut sickn sidl sied siev
sights signp silh simm sinh sinn siol siss sizzl sjoint sjudg sker
skirm skirt skivv skyr slak slal slamm slang slant slash slath sle$
sled slend sles slik slimm sliv slobb slodg slosh sludg sluic slush
smantl smash smatch smith smooch smoth smugg snaffl snar snatch sneer
sneez snick snid sniffl snift snitch snom snooz snowdr snowpl snuffl
snugg snuggl so$ soak soapb sobl soch sog soj sonn soot sors soundpr
sous sown spair spangl spank spann spearh speckl spectf speech spel
spill spis spitt splurg splutt sportsm spot sprightl spritz sprov spur
sputt squabbl squand squeeg squelch squit sreg srep srob srul ssacr
ssanc ssants ssault sscross ssel ssen ssenc sseng ssens ssessm ssev
ssings ssment ssolv ssom sspell sstim ssuad ssuag sswom ssyf stab stad
stairw stalg stants stard stars stash stast staur stbit stdat steer
stems stench stentl steop sterm sterns stfuln stickl sticks stillb
stions stippl stitch stmast sto$ stockp stodg stoic stop stos stound
stov straddl straf straitj streaml strept stripp stript striv strol
struggl strump stubbl stucc stum stym suall subb subp suds sulf suns
sunt surc surch surfb surl surt sut swaddl swash swear sweatsh sweetbr
swerv swing switchb swom sying synchr syph tabb tailg tangl tantl tapp
tapr targ tarm tarn task tass tastr tav tawdr tawn tback tbacks tbagg
tbal tcak tclass tdist tearg teasp tec templ terc terf terpr tesm teth
tfish tfitt tfox tfuln thdraw theism theists then thenc therc therh
therpr therw thesl thesp thest thiest thin thinks thlon thlons thnol
thorn thos throttl tients tinct tink tinkl tiol tionsh tipp tiss tith
titl tittl tjack tle$ tlegg tler tles tlight tlin tling tliv tments
tnumb toed toggl toolb toothp topl toppl torch torq torsh tperf trach
tracts traips trait tramm trampl tranq treacl treadl trebl trell
trembl trickl trik tril tris trix troch trof trol tromb trounc trud
trudg trundl trus truss trustw tsid tsourc tstretch ttas tterfl tterl
ttir ttish ttlec ttlef ttlen ttlers ttock ttonh ttor ttun tuals tums
tunn tush tussl tux tvot twaddl twear tweed twent twiddl twing twinkl
twitch twof typh tzed tzing uagmi uainte uande uapla uarde uashe uasi
ubblie ubhea ubjoi ublea ubpoe ubriou ubsoi ubsu ubti ucca uccee uche
ucko ucksa uckste ucky uddy uebe ueing$ uele uendo uente uepri uere
uerreo ueso uessti uffia uggli uglie uiete uietu uila uillo uisha
uist$ uisti uists$ uitca uitio uive ulae ulgi ulia ulk$ ulks$ ullba
ullo ullshi ulo ulpi ulso uly umbfou umbly umbo umbu umlo umnia umpki
umptuou unbi unclo uncoi uncu unfe unfrie unfro ungai ungeo ungs$
unhoo unju unloa unloo unlu unmi unpo unquo unscra unscre unshea unspo
unsta untee untwi unvei unwie unwra unzi uoti upbrai upchu upgra uppla
uprai upri uproa uproo upstrea upsu upy urb$ urbs$ urcea urdi urf$
urfboa urfei urgla urloi urlou urmi urmoi urno urnou urnu urou urpi
urple urplu urryi ursts$ urta urts$ urtu uru urvey urveyo ushroo usie
ussa ustee ustproo ustriou usua utch$ uth$ utt$ uttre uvu ux$ uzzi
uzzie uzzli vam vann vanq vans varn vatt vect vell vents verch verfl
verj verk vernm verns verpl versl vib vier viest vign vingl vious
viousl vip vists vitr volc vom vouchs vuln vur vvies waddl waffl waggl
waistc walks wallp waltz wangl wardr warh wass watchm wattl waw waxw
wayf wayl wball wberr wboat wbox wbreak wdy$ weakl weap wedd wedg wee$
wees weigh welc welsh werb wful whamm wheedl wheelb whimp whisp whith
whoosh whopp whor wig wigg wildc wimpl winc winch windbr windm wingl
wisp withh withst wiz wked wking wman wmen wmob wners wngrad wnscal
wnsiz woef wolv woodp wooz workb workh workm worksh worldl wpok wrench
wring writh wrongd wscast wsed wses wsing xalt xceed xcess xclud xculp
xerc xibl xiom xis xists xoph xot xpand xpat xplain xplod xpung xtemp
xtrov xtrud xuals xud xus yamme yarda ybu ychia ycla yda yes$ yfi yfoo
yga ygra ymi ynchro ythe ythei yto yx$ yxe zeb zigz zons zool zur
zvous zzic
""".split(): TRIPLE_SCORES[triple] = 2

for triple in """
^aesth ^aid ^ail ^altr ^amm ^amph ^and ^answ ^apr ^apt ^ard ^arthr
^ask ^ath ^athl ^atm ^ausp ^awf ^awkw ^bie ^chri ^deu ^doe ^drie ^duo
^eag ^earthl ^ecc ^eer ^elb ^emph ^enfr ^ensl ^esch ^flie ^frai ^hoe
^ib ^inbr ^iss ^jea ^klu ^kro ^ku ^lai ^leo ^lia ^lio ^nei ^obf ^odd
^oss ^oust ^outbr ^outc ^outpl ^ow ^plau ^playa ^quea ^rhe ^rue ^shy
^slui ^sple ^stoi ^stou ^sua ^sue ^trua ^true ^try ^unbl ^unct ^unfl
^unwr ^upd ^urb ^voo ^whea ^xe ^xy ^yard ^yog abje abstru acha ackie
ackkni ackno adou adri advo aesthe affa affei affs$ afo agle agno aidi
ainli ainsco aintie ainwa airme airwo aja aldi alds$ aloe alpe alry
alto altrea altrui alts$ amy anctio andlo andwi angre anque ansie
anspi anspla ansshi antee aphro applau apte arboa archie archy ardne
arfe argai arkle arlia armfu armle arrio ashbu asie asmi asms$ assau
assme astou asu ateau athle atmo atue audio auds$ aughti aughtie ault$
aults$ aunchi auntle aute autiou avu awbo awdle awke awkwa axio ayone
backsp bad badm baffl balm barn bars bawd bbit bborn bean beck beep
begr besp bestr bfusc bias bioch biot bjug bland bleed blen blend
blinds blit blunt blurr blust bmerg bmitt bneg bnorm boast bob bong
boob boond boos boost bos bott bount boys brad brawl brawn bred briat
brib brill broads broil brood brush brusq bstain bstetr bstin bstrus
bsurd btain btract btrus btus budd bumm bung bustl buts bvers byl caf
caff caj cank capr cars catn cats ccentr ccred ccust ceh ceous ceps
chaff chains chal cham cheat cheerf cheerl chment chop christ chunk
cibl cic cientl cings ckeys cklers ckmail cknowl ckpack clev clic
climb clink clipp clips clums coex coin concr conscr coon cops coq
cowp crif cring crof croon crossw crotch cruit ctrif cund cunn cuous
cusp cutl cyb dab daff dals darn daub ddied ddier ddiest ddings deathl
dedn deif dethr dgeon dgets diagr dians did dimm diot disfr disj
djustm dlocks dmiss dmouth dnapp doctr draft draul drog drop dropp
drudg dub dud dumb dumbr dun dunn dup dvoc dwell dyb eabi eabou eadba
eaf$ eafle eaky eallo eally eamli eanse eant$ eappo eappoi eard$ earma
earni easy eathi eaus$ ebrai ebria ebrie ecce ectne edre eeha eekly
eem$ eems$ eepy eerfu eesta efla efts$ egga egru egui eice eighe eighi
eighs$ eightie eign$ einsta eits$ eke elbo elco ellbi elme embly emna
employ employe empte emy enchme eniu enme enoi enri ensla enthe eole
eori eos$ eoso eout$ eouts$ eove eppie epsi eptua erb$ erbia ercei
erdre erflo ergo erk$ erke erplay ersco ersee erste erstu erwhe escue
espai espou esqui estia esy ethou etwo euma eums$ euti evea eviou
ewsca excee excha exio expia explai ext$ extro eyma fad fain faint
falc fearf feebl ferv fetch fev few ffac ffal ffein ffen ffend ffet
ffid ffins fflict ffor fianc fidg fierc fiest filt filth filtr find
flies flims fling floodl flunk foil fom fondl foots forf forn forsw
frat freeh freight friend frill frol frostb fruct fruitf fuck gabb
gaff ganc gangr garc gass gauch gaud gaunt gens ggish gher ghest
ghlight ghtful ghtin gid gidd gimm gird glar gleam gled glimm gling
gma$ gments gner gners gnets gnment goal godd golf goon graft grants
gree$ grees grett grill grip gritt grizzl grogg grom groom gruff grump
guff gumm gunf gurg gyn hack hacks had halv handm haught haul heal
hear heartbr heartl heath height helm hends hew highb hint hoard hoars
hob hock hoods hort hot howl hull hunk hunt hurl hymn iagra iale
iantly iase iat$ ich$ ideou idgi idu iel$ iend$ iendlie iends$ iennia
ieri ieta iete ietie ievou iewi iews$ if$ ighe igme ihoo iing$ ildca
ilk$ ilkie illai ilme ilti imba imbo impse imsi imsie indsi infra ingy
iniu inui ioche ioma iori iosi iot$ iots$ ippa ippli ipse irde irgi
irk$ irks$ irle irm$ irpa irti iru isdia isea isfie isfra isjoi isplea
issue istfu istrea isty itcha itly itty ivvie izi izzlie jackkn jagg
jail jamb joic jol joyf jun kas keen kenn kish kit kitt klutz knead
kness knott kron lamp lands lard laying lcat lches lcom lcon ldly$
ldness leafl leath lech lert lge$ lgenc liabl lian lians lias liers
lift lih lingl lions lior lix llac llaps llev llibl llid llingl llog
lloon llops llul lman lmon loads loaf loan lodr loll longh longs loot
lott lousn loyal lptur ltat lthier lthiest lthy$ luct lue$ lues lull
lun lung lupt lymph lynch lyps lyth mains mals maltr mantl marc marm
mbalm mbard mbec mberm mbrat mbust meat membr menc mesc minc misb
mless mma$ mmas mmif mmin mmol mnest mold mourn mournf mpaign mpeach
mpell mpend mperf mphom mposs mpot mpov mpow mprec mpting mudsl mulg
mum mums munch nadv nak nalt nann nappr naw nbound ncas ncef ncel
nceph ncestr ncipl ncircl ncoct nconsc ncop ncrem ncret nctif nctuat
nculc ncycl ndblast ndbreak nden ndep ndern ndex ndlier ndliest ndoctr
ndrom ndsom ndstand nebr necr nell nesc nettl newsc nexc nferr nfest
nfett nflamm nfur ngal ngenc ngov ngren ngress nhand nhapp nials nib
niggl nightcl nigr nill nimbl niums njust nkly$ nliv nmak nnas nnat
nne$ nnest nnets nnials nnil nnings nnobl nocl noct noid noph nors
nour now nox nread nroll nsact nscious nsem nsers nsett nsfig nslav
nsmigr nsolv nsors nsort nspar nspic nstabl nstall nstant nstip
nstruat nsuff nsvers nta$ ntedl ntempt ntercl nterst nthes ntiousl
ntir ntments ntors ntour ntrar ntrig ntum nvar nvex nvict nvig nviol
nvoic nvol nwash nxes nying nyms nzas oal$ oals$ oar$ oars$ obbli
obbyi obfu obtu ocee ocla odgi odiu odra oer$ oers$ oexi oft$ ogfi
ogna ogro ogu oici oir$ oirs$ oisi omai omfi omps$ ompte omu oncea
oncre onio onje onjoi only onscie onscri onste ooch$ oofrea oondo oosi
oozi oozie ophie oquia orfei orka orno orpe orpu orra orry ortcu orth$
orthi ortle ortrai ortsca oshi ossa ostbi otbe othea otty oul$ oulti
oundle ournfu ourni ourteou outcro outdi outhwa outri ovie owdi owdo
owhea owme owpo owy oyage oyfu pamp pans pants park parq pdat peep
peer peg peopl perl perw pess pew phar phem pherd phet phrod piers
pimp pimpl pinn piv plaint plann play$ plead plent pless plies plodd
plumb plump poch ports potb pov powd ppell ppointm ppur prearr precl
preempt pren preshr priss priz proach proofr prowl ptabl ptit ptly$
ptness ptogr ptor ptors pub pug pugn purpl pwalk queas queer quef quel
quentl quilt quip quizz quor racts raff raft raid rald rasc rash rath
raud rbear rbidd rboards rbor rcad rcas rceiv rchers rchief rchies
rciss rcuit rcumv rcuss rdant rdash rdest rdict reab reach ream reap
reck redn reef reins reinst rels reot restf rets reus rewr rex rfish
rgen rgeon rgies rgit rhaps rhet rhood rhythm riff riors riz rject
rkabl rkel rkier rkiest rky$ rlat rliam rlic rlock rloin rmall rmount
rne$ rnest rney$ rneys rniv rnov rnum roam roast roids romp roost root
rpen rphan rphos rpop rquis rrad rreact rreal rret rribl rriers rrings
rrod rsak rsals rscor rsect rsest rset rsev rsibl rsight rsom rsuas
rtains rtal rtend rtex rtheast rther rthin rthing rtiest rtim rtist
rtle$ rtled rtles rton rtoon rumbl rump rvest rvings saff sappl sbel
scad scern scert schiz sclaim scler scomp scoot scours scrapp scred
scret scumm scus scuttl sdiagn sdir sebr seeth segm selv sench send
senfr serp sfranch sguid sguis sgust shabb shant shatt shear sheer
shipb ships shirk shodd showb shwhack sicc sift signs simp sincl sink
skill skitt sleek slim slin slink slith slop slow slumb smack smal
smelt smemb smil smooth snoot snott snuff sock sogg somn sorc sour sov
sow sparr spasm sphor spinn spleas sportsc sposs spread spum spy$
squeal squint ssabl ssad ssant ssect ssem ssett stack stark startl
stealth steep stifl stink stler stlers stments stract stream strength
strip stroll stult sturd stut stworth stwrit sual suav substr suct
sunl sunr suppr swath swelt swift syb syc sympt synd synt tad tarp
tballs tchen tchmak teet tentl tet than thankf thead theol thfuln
thier thless thlet thmic thom thon thrill thriv thwest tib tickl tint
tips tled tmosph tnot toad toes tomb tong tout toz tpick transpl
transsh traps trawl tread trid troc truc truck trunc ttach ttain ttanc
ttom tuall tweet twigg twin twirl twist twork tym uable uato ubie uco
udsli ueeze uency uene uesse uffu uffy uggie ugle ugna ugu uibble uidi
uids$ uili uilt$ uini uitfu uiva uki ulke ulkie ullio ulptu umve
unchie uncla uncle ungo ungra unhea unky unlo unpi unplu unro unsi
unso unstea unsto untru upda uppi uppre uppu upts$ urbe uree urra
urrou ursio urst$ ursue urvie uscle uscu uski usks$ usque ustai ustwo
usy uthfu vad vault ventf vercr versp verthr verwh verwr viar vism
voic vood vort wabl wainsc wals wan wann warl warp watt wbon we$
wealth week weightl weights weld well whil whirl whoop wif wins wler
wlers wly$ wner wnier wniest wny$ wok wolf woods woodw woof wooll
words wors wound wrapp wreath wrong xac xag xasp xcell xchang xecr
xers xert xhil xhort xif xig xin xion xpatr xpiat xpon xten xter
xtinct xtirp xyl ybe yche ychi ydrau yers$ yeste yl$ yls$ ylu yly
ympto ynco yndi ynta yoke ys$ ywri zef zens
""".split(): TRIPLE_SCORES[triple] = 3

for triple in """
^abbr ^abh ^affr ^airm ^airw ^ald ^alk ^alm ^ankl ^arc ^archd ^ars
^ascr ^auct ^augm ^aust ^az ^broi ^choi ^choo ^cloa ^creo ^crui ^due
^dye ^earm ^earthw ^ech ^egr ^eld ^enm ^enn ^estr ^flai ^flau ^floa
^flue ^frei ^gloa ^gloo ^grai ^grue ^inp ^kne ^knea ^knu ^laye ^lei
^liai ^mayo ^obd ^occl ^offs ^orph ^ott ^own ^pli ^poa ^roe ^schle
^scie ^scrou ^shie ^soi ^sphe ^spie ^spou ^thei ^tree ^umb ^ungr ^unkn
^unsh ^up ^upbr ^ush ^vai ^vee ^voya ^wie ^yok ^yuck ^zea abba abbre
abby abdi abho abju abne abro abru abstai absu accha acho achu ackda
ackmai ackpa acksli ackwa acque acquie acra acty acua addie addo adiu
adjou adle adroi aff$ affro afi agga agglo agglu aggra agme agoo aic$
ailboa ailo ainee ainly ainsto airbru airway aje akie ald$ alloo allpa
allyi ambo amboo ampai ampio ampo ampoo amro anca andbla andca andee
andfa andli andpi andsca ankru anlie ansfu ansli ansmu anza aphie
approa aptai aptio arau arbu arcoa ardhea arlo arp$ arpa arps$ arrai
artie artle arvi ascri astri asua atca atchie atchma atchwo ateu athy
atiou atoo attli atzo auctio aud$ augme aurea auru ausea auspi auts$
awne awnie awns$ aybe aydrea ayma bacc backf backh backstr badg balk
bamb bank bann bart bauch baz bbies bbish bbrev bcontr bdic bdiv bdur
bead beef bels beq bers besm bev bidd bip birds bisc bitz biv bjur
blackm bleach blet blets bliogr bloom bluff blush bobb bonn books borr
both bowl brack bragg brak bruis bscen bscrib bsent bstit buckl bug
bugl bungl burb burd bushwh cadg camb cans castl castr casts ccomm
ccurr chalk chall chapl chat cho$ choos ciabl cials ciar cig cinch
citr ckens ckest ckey$ ckings ckler ckrak ckslid ckup ckups clamb
clamm clapp cler clerg clinch clown clus coach coerc coiff coil congl
coph copt cort counc coupl coz cquaint cquiesc cquir crash crats cre$
creak cresc croch cropp crosc cruis crumb crus cryst ctuall cuat cuck
culm cyt dabbl dac daint dais dams dang dant dawdl daydr days dcast
ddest ddict debr deck dedl deic dej dels dendr deol derr diam dient
dinn dioc disd disf dits ditt djur dlier dliest dmitt dodg does dogf
dont doodl dopt dour dowd doz drain drap drear dredg dribbl drift
drink droop dropl duk dut dvanc dwif eactio eada eadju eado eande
eappea eapprai earlie early eashe eaths$ eatie eaucra eawa ebau eciou
ecle ecri ectfu edy eeca eech$ eela eeloa eepwa eethe eethi eezi efau
efti egme egoi egua ehy eigh$ eigne eimbu einca eine einfo eins$ eismo
eisti eloa elti elts$ elvi embli embryo emea emoi empi empli empt$
enclo encroa encru endou enea enthro entrea entry eome eoni eopa eota
eplo epra ercoa erd$ erda erdra erds$ erei erfei ergro erje erlai
erlea erlu ernme ernu erple ersha ershoo ersti ersu ertly esdro esea
eshoo essfu estea estly estre estria estro etoo ettee euse eute ewie
exha exho exhu expi expro extru eyboa eymoo ezzle fail falt fant feed
feel feg fen fenc feud ffabl fferv ffoc fleet flight float fluct flush
flut flutt foam fragm frank freez fric friendl froth frustr ftest
ftier ftiest fulm fumbl funk furc gains gambl gantl gastr gav geom
ggard ggies gglier ggliest gglom gglut ggly$ ggon ggrav ggreg ggress
ghen ghtest ghtier ghtiest gics gien ginn gladd glaz gle$ gles glid
gloom gnanc gnarl goat godl gods goof goos gorg gos goug gout grain
grin gross grubb grumbl guer guerr guilt gum guzzl haggl hardh harv
haw health heckl hed heft help herr hier hik hind hing hitchh hiv hoax
hoot how howd hug hung hurdl hustl hyg iants$ iar$ ibbi ibbo icca icka
ickey ickli icni icuou iddli idia iefi ieni iew$ ifa igga iggli igglie
iggy ighli ightie ightne ighway igree igue igui iguou igwa ildi ildre
ilfe illia imbi imne increa incri inct$ incti inctio inctu indli
indlie infri inghou ingu ingua inhu inia inklie inny inscri inste iote
iothe iplie ipsti irche irke isbu isclai iscree isdai isfa isgra isgu
isle isme ispi ispie isqua isquo issie issta issua itchhi ithdra itpi
itue iviou ivu ixtu izza jac jal jayw jigg jigs juggl jul juxt ka$ kab
kal kar keb kend kettl keyb kill kink kiss knuckl ladd lanch landsc
lanthr larm launch laund laundr law lay$ lays ldren ledg legg lents
lfer lfish liais lighth lil lins lir lisms lkal lkers lkier lkiest
lky$ llars lldoz lley$ lleys llor llos logg loit loon loop lopm loss
lowl lped lping lries lsat lse$ ltic ltit ltras lym mack maids mash
mask match matz mav mbast mbell mberl mbly$ mbroid mburs mcis mec meet
might mik mingl mint misq mix mmabl mmet mmier mmiest mmis mmons mmox
mnav mnif moan mog monthl mooch mood moos mop moph morrh mow mplim
mpound mprom mpted mpus muck muckr muffl mumbl murk musc mutt nagl
naught nbath nberr ncaps ncarc ncens ncest ncheon ncit nclos ncod
ncompr ncontr ncor ncorp ncount ncred ncrim ncur ndal ndas nderh nderm
nderw ndes ndies ndign ndir ndless ndom ndos ndow ndress ndscap neal
neb nentl nestl nfam nfisc nflect nfluenc nfring nfront nghous ngibl
ngit nglom ngthen niat nibbl nicl nied niousl nisms nitp nix njoin
nkind nnels nnet noff northw nprof nres nsan nsec nsecr nsfer nsfus
nsin nslit nsmut nspos nstat nstead nsumm nsurg nsus nswer ntan ntas
ntel ntemp nterch nterj nthet nthol nthron ntiest ntings ntrans ntrat
ntreat ntrud ntupl ntus nucl nuf nufl nund nutm nvad nvass nvolv nza$
oachi oadsi oali oan$ oane oans$ oast$ oasts$ oathe oaxe obdu obia
obno obsce obso occi occlu ochi ocio ockpi ocrea ocy odiou oeho oeve
oggli oggo oggy ogly ogni olk$ olley omp$ ompro onfa ongho onglo onkey
onna onnie onpro onstrai onstrue oodcu oolma oonfu oopie oore ooste
oothi opha opia ople opme opou oppa oppy orcy ordia ormo ormou ornie
orpha orthe orthea oscri osio osme ospho osso ostpo ostwri otchi othou
otru oubte ouchie ouette oughi ounda ourie ourne ourney ousti outba
outfi outgro outhwe outse outsi owca ownie owo owto owwo oxie oyri
panh pann partm partn paus pboard peal pearl peddl perpl perst picn
pierc pik pilf piq pitch pizz playb pleg plor plott plum plund plung
plur plush plut pnot poach poet popl porn posh pound pperc ppin pplem
pplied pplies pply$ pplying pprent pproach pragm pranc prav prel
preocc prepp probl proscr prostr pstick pud punt pup quac quav questr
quibbl quil quirk racl rais ranch rank rapp rasp rass raz rback rcef
rcher rchit rchiv rcin rcom rconn rcumc rcumn rcumscr rcycl rdiest
rdiogr rdness rdos readj rean reappr rearr reaucr reav ree$ rees reimb
rein reinc reinf reint reit reth rfor rfum rgo$ rgon rhin riabl ridg
rifl riol rios risms rken rlet rmam rmarr rmingl rmist rmor rmut rmy$
rnabl rnet robb roid roist roughn rov rowd rox rpat rpers rpetb rplex
rpol rport rpow rprint rprod rrag rrass rreg rrels rrend rriest rris
rriv rrug rsar rsens rsid rsign rsimpl rsist rsiv rsor rtar rtedl
rtest rtial rticl rtier rtor rugg ruin rustl rval rvesc rway$ rways
rweight rwork rym sadd sail sailb samb sampl sandbl sandp sang santhr
sard sash savv sax sburs scalc scamp scand scarc scav sce$ sced sces
scient scin scing sconstr scorch scrambl screw scribbl scroung scurr
seab seg seiz sels seng sext sfact sfig sgrac shagg sheath shen sheph
shill shinn shipwr shock shopl should shrill shrink sia$ sight sits
siz skiest skinn skipp skyd skyj sleet slic slick slight sling sloc
slov smell smuggl snobb snor snork snow snowm sopp soup span sparkl
spatch spatt speck spects spellb spiff splatt splic spook spoonf spor
spring spron spruc squeak squeez sques squir squirm squot srepr sresp
srupt ssers sset ssful ssid ssman ssmen ssol sson sstat sta$ staff
stagg stagn stalk stamm stapl starl starv staunch steps stess stigm
stings stment stocr stod stok stors stort stpon streak strust stumbl
stump stutt stward subh subtl suckl sunn surpl surpr sust swall swamp
swell swindl swirl swish switch synth syr tackl tails tanc tchet
tchhik teeth tents teur thern thfull thiev thimbl thinn thought thrift
throat tibl timb tinn tippl tipt titt toddl tog toll tonn tool torb
torr toss tott tourn traff tresp tress trics trif trifl trimm trin
triot trip triumph trons trott troup truckl tta$ ttag ttens ttil
ttings ttlem ttler ttos ttress turg turm turtl tyl tzes uade uake
uatte ubdi ubsti ubtle uch$ ucia ucta uctua ucu uddli udgie udia uely
ueri uests$ ufa uffli uffo ufle uici uicke uid$ uilde uin$ uins$ uintu
uiri ulfi ulie umba umbre umci umple umscri unbea unblo undle unds$
unga unkno unme unque unri unsee uoro upt$ urbo urca urgle urio url$
urlie urls$ urmou urmu urpa urpe urrea urt$ urti ushio ushwha usk$
ustme ustria utme uttie uxta uzze valv veh vesdr vets vils vog voll
vorc vouch voyag wack wail waiv walls warbl wart washb watch wcas weav
weekl wes wfull whinn whisk whistl whittl wigw wimp windb wint wip
witn works wrangl wreck wrestl xagg xcis xclus xcomm xcor xempt xhal
xhum xiat xies xil xpens xpir xplos xport xpost xpropr xtap xtend
xtens xtrad xtrap xtrav xult xyg ybo ygie yja ym$ ymbo yms$ ynthe yphi
ypti ypto yre yse yst$ ysts$ ythi yway ywei zeal zil zill
""".split(): TRIPLE_SCORES[triple] = 4

for triple in """
^addr ^alc ^cea ^chie ^dwe ^earl ^east ^ell ^embl ^enh ^etch ^euph
^exch ^feu ^ink ^inl ^ny ^obtr ^oft ^oil ^orb ^outcr ^outgr ^phra ^rau
^rheu ^rio ^roya ^scho ^slea ^sprea ^spru ^stau ^thie ^three ^throa
^thy ^tie ^toe ^ugl ^ump ^urg ^woe ^wou accre acquai acs$ addre adre
aera afa agea agma aila ailme ainie ainme aisa aithfu aiti alge allou
alm$ aloo ambli andso anga ango aniu anli annua anny ansio answe anty
apie arco arfi arga arja arla arso arto artoo aski asm$ asphy assy
astle asty atee atto atua auche aude aught$ aulti auste aut$ babbl bac
backl backs backst backw bapt bduct beds begg bert bia$ bitch blast
blat blesh blind blink blotch bmers boil bond bootl born bow brac brew
bright brisk bristl bubbl bulg bulk bullf bun bys candl carj carv ccat
ccol ccord cerb chart cheap chier chiest child chim chir chiv chnol
chumm chy$ cient ckbit ckly$ ckon cloud clov co$ coag coast coat coord
copp cour crabb crackl cram cran crapp crast crick crook croup ctest
ctics cuddl cush cyn da$ dark das dash dead deaf deep dgers dher diab
diol dios diousl djud dless doct dop draw drizzl droll dron ducts dump
dwarf eady eafe eagle ealo earse eassu eata eatu eaway ebou ebrea
eckli ecrui eeble eedu eedy eeki eenths$ eerie eevi effa effu efra
eft$ efte egle egli eing$ einte eism$ eist$ eists$ eit$ eiva eivi emia
endea engra enna enno enstrua entfu entou enve eore eploy eproa epts$
ercla erfa erhoo erpi erpro esee esh$ essma estfu estie estio estrai
ethro eupho euri fair farm fens ffens ffrag firm fits fizz flamb flatf
fleec flesh flick flirt flopp fluff fluk fly$ forms fount fox fraud
freak frizz fuls fun fur ga$ gabl gac gain gals gand gap garb gath
gee$ gentr geogr geol ggin ggler gglers ghostwr ghtens ghtness gig
glig glitt glutt gnant gobbl green groov guess guit het hick hij hill
hobb hog holds hosp huff hurr husb iddie idna idy ieing$ iena ienne
ienti iffie iffle iffu iggie ignme ija ika ilke imou impai impea incte
infli influe ingli inhi inka inkli inque insa iodi ionshi ircui irli
irme irths$ irtie ischie isclo isk$ isks$ ismi izzi jazz jock jok joyr
jub juv kest kib kingl kitch kly$ know lack landl lank lants lark laud
lcoh ldings lead leaf learn leer lemm lgam lgar lief lights lker llad
llan lleng lliat llip llish llo$ lment lner loath lodg look lops lots
lphab lpit lry$ ltan ltin lub lubl lvet lyg mainl mbass mbezzl mbit
mbo$ mead meddl menstr mild mits mmar mmigr mned mness mocr monk moonl
mpal mpart mpert mply$ mpost mpur mroll mudd muff muls naiv napp naus
nbel ncap ncern ncher nchor ncom nconc ncont ncour ncrust ndants
ndergr nderwr ndict ndier ndiest ndingl ndiscr ndish ndist ndur near
neas neck need nen nfiltr nflict nfold nfull ngar ngent ngrav ngreg
nguin nhanc nhib nhum niacs nienc night nisc nishm nitr njug nket
nkies nkled nnab nnial nnih nonpr nquest nquis nrel nsect nsent nseq
nsform nsib nsic nsif nspect nsport nstig ntains ntempl ntenn nterw
ntials ntier ntious ntis ntitl ntness ntort ntriv ntrod ntuit nuanc
nue$ nues null nuous nvas nvel nverg nwar oagu obby octa oeing$ ogui
oha ojou okie oldie olie ompou onfro ongra onno oodli oodwi ookma
oonli oori ootie opra opsi orphi orpho orrie ossu ostle ostma ostra
otta oud$ oude oughne oup$ oupie oups$ ourte ousie ouths$ owsi pabl
panc pard paunch pebbl pee$ pees peev perh perk pez phas phes phist
phol pith plets pluck pocr popp postd pprox prescr prickl prior prompt
prost psed psid psing psy$ purch purl purv puzzl pying quarr qued rail
rambl rbid rbing rbox rcen rcent rchas rchic rchy$ rcoat rcol rcomp
rcumst rdens rdier rdress rdy$ redd reev reign renth rents rests rfed
rfing rful rgent rget rgic rheum riall rias rienc rins riod rion rithm
rits riw rlands rmis rnment ronm rooms rop rosc rott rpetr rproof rrac
rres rrym rsal rspir rtag rtebr ruff rumm rvant sanc sans sband scabb
scalp scents scer schol scint sclos sconn screech scrubb scull seal
sees self senc sert sets shav shiv shortc shriv shrubb shutt sickl
sinc sitt sketch skets skier skimp skin sky$ sleaz sleepw slid slopp
slouch smen smet smic smiss smudg snip snipp soap spad spars spat
spectr sperm sphyx spid spik spindl sping splash splend splint splotch
spoon spotl spous sprinkl sprop spunk squash squatt squer squiggl
squish ssal ssat ssib ssil ssip ssum stain stamp stant starch starr
steel steepl stef stis stlier stliest subv suck suffr sun swagg sweat
sweep symp tach talk tank tans tars tball teach tedl tee$ tees tep
terw tess thatch thirst thrash threat thron ti$ tiabl tient tight tins
tiq tment torp tramp trash tref trend tries trigg trill triv troop
ttabl ttal ttin ttons tuck tund uage uard$ uards$ uarie ubble ubju
ubve ucci uccu uckra udgeo udie uel$ uels$ uentia uents$ uera uers$
uffra uiesce uildi uishi ulki ullfi umb$ umbs$ umo umpy umsta uncou
uncti undo unfu ungle unho unu unwo uore uota upie upo upre urfe urpri
usba usci ushy uskie utre vass veal verts verw vex virg warn weak
weird whal wheez wings withdr wretch xampl xcus xpend xploit xpurg
xtort xtract xtric yello yer$ yge ygo ypa ysa yspe ytho yxia zan zzier
zziest
""".split(): TRIPLE_SCORES[triple] = 5

for triple in """
^abb ^ah ^angl ^bia ^brui ^chau ^dry ^dwa ^eav ^empt ^encl ^enshr
^enthr ^ethn ^eyel ^fia ^frea ^inb ^inch ^inscr ^isl ^itch ^jai ^jay
^jee ^lay ^loya ^moa ^outst ^outstr ^prai ^prio ^rhi ^rho ^rui ^scro
^slau ^splo ^splu ^spoi ^spra ^swoo ^thwa ^troo ^twa ^two ^ult ^umbr
^unk ^unsn ^unsp ^unv ^upl ^upt ^vei abdu ac$ ackha ackli ageou aggie
ahe ainfu aintai airie alka alley alms$ alou alsa alt$ ancti andma
andpa andsta angea anio anly annu anqui anscri ansfo ansgre ansve
anthe apha apprai appy apri apu arch$ aroo arpi arque arryi artia
artme arty asha ask$ asks$ asp$ asps$ asque atrio aty aule aunt$
aunts$ autio awki awli awni backp bact bak bald balls bals bant bath
bbin bbler bblers bear bem biogr biol blam blow blueb blund boat bog
bom boom bottl bra$ brain braz brig broad broadc brut bseq bsorb
bstract bump burgl butch byt cach calm carc ccel ccid ccompl ccum
centl chamb chang charm cheek cheer chers chew chick chut cienc circl
cleans cleav clud clunk cobbl cocks coddl cours creas crinkl crisp
cron crow crumbl crunch crypt ctil ctit cun dact dair damn dapt ddit
deq dgeh dian diar diatr dienc dign dirt dizz dogm dors dov downs
drunk dsid eadlo eadmi ealou ealthie eamro eapo earche easie eath$
ecea ectly ecy edro eeni eenth$ eepie eeple efea eg$ eggi ehu eighte
einve eki elay eld$ elfi emou engthe enla enra enue eople eordai epay
epli eproo epte erai erboa erchie ercia ergy erhou erju erle ermea
ermu erno ersto ertio esche esia esme essme estu etchi etre etrea
ettie etua eum$ ewspa exca exploi fak ferm ffier ffiest ffil ffix
fiddl field fift flabb flipp fors fram franch freeb fright frisk fruit
ften fuddl fung furth gees gel gend ghty$ gion gold grap grass griev
grouch gunn gymn hair handc handl hank hatch headw hedg hobn hor hov
humm hundr hypn hyst iasti iatu iblio icho ictu idie idwi iente ierce
ieth$ ieths$ ightfu igiou imie impie impla inclu ingra inje inspe
intui invei ioce ionai ipts$ irth$ ischa isdi isgo iss$ istry istu
ithi itou ittie ivia jabb jap jett jitt join joll kens kind kings
knock lamb lash laugh laur leak lean lend lep lges lip litt littl llen
llianc llic lliest llud lmed lming lobb lom lsion ltif luck lug lump
lyr madd malf malg march marq masq math mbarr mbig mbol mbos meal meb
memb milk misl mispl mly$ mmag mmem mmest mmies mob mogr moist mons
moon mors mortg moss mpath mpest mplain mpregn mption mush myth naug
ncell ncentr ncess ncin ncloth nclud ncompl ncreas ndag ndam ndents
ndet ndo$ needl neousl nerg neutr newsp nfat nfed nflat nful ngat ngo$
nigg ningl nkle$ nkles nkling nlarg nnex nnoc nnon noth nquish nscrib
nsert nsgress nsmitt nstanc nstrict nte$ nticl ntox ntroll nutt nvir
nvok nvuls oadca oadi obbie obio obtai ockie ocri ofu ogo oide oings$
oini ointme oists$ olio olte olti olvi onau onda onts$ onva onvu oodi
ooka oordi oors$ ooth$ ootle opte orbe orda ortga ortie ospi otch$
otho ouge ounge ountry oupi ouple ousa outli ovu owba owdie oyme padd
pair panth paq patch paym perj phosph phyl pian pings plag ply$ pment
pom postp pox ppeas ppet ppled ppling priet procl propr ptibl ptics
puck pulp putr quiet quis rabb rain rbish rboard rchang rcis reinv rek
reocc reogr reord rgers rgiv rgy$ ri$ rib rics riousn rjack rjur rkers
rlier rliest rmers rmic ror row rping rrent rrig rrob rrot rsat rtax
rtens rtgag rthier rthiest rties rtil rtit rtment rtness rviv rwrit
saddl sadv sagr sam sant sarc scarr school schoolm scratch scuss seaw
sef seism sembl shall shar shingl shments shuttl siast sieg sins sixt
skew skyl slaught sledg small smirch smol snapp sneak snoop southw
spass speak sped spoil spott sprint squar ssass ssies stanch star
start steamr sthet stip stlin stness strait strangl strial stries supr
sus swatt swip sync tack tact tain tann taph tattl taut tear teb teers
tfull thal theist thful thirt thod thogr thresh throw tiousl tless toc
tooth transcr transgr transv trapp treach trem triarch trick troph
trosp troth ttack ttent ttern ttis tuit uare uary ubbo ubtra uckie
uckli uently ueste uets$ uffa ugi uice uinte ulsa ults$ ummy umna
umptio uncha uncheo unctua undu unfa unpa unpre unru unsna uppli
upplie uptu urdle ureau urfa urgeo uro urso urte urthe usia uspi ussie
ustfu usty utle uve uxe vacc vant velv ventr vergr volt wait wheel
whims wier wiest winds winn wness wobbl worm wrinkl wspap xact xcav
xen xorc xterm yce ydi ymna ympa ympho yni ypno ysta ywa zard zett
zzed zzing zzy$
""".split(): TRIPLE_SCORES[triple] = 6

for triple in """
^abn ^adr ^affl ^air ^airl ^alg ^amn ^blee ^bui ^clai ^crue ^drai
^earth ^eat ^eight ^eth ^frau ^glea ^hie ^idl ^obv ^old ^ost ^out ^peo
^proo ^quai ^rhy ^snea ^snee ^stoo ^stree ^triu ^unch ^unfr ^unpl ^via
acea acre addli adie admo afti aighte aints$ aits$ alga alki alpi alse
alsi alva angie ankfu ankie anoi ansfe ansla anso antry apro apsi apy
ardie ardo arka arry atty auda aura ausi austi axa axo aywa azzle
backsl bagg bail barg bark bask bind blank bler blest block boards
bogg bookm boot booz bort bounc brass breez brid brows bscur bsess
bumbl bunk burg burl buzz cag cants catt ccent ccomp ceabl cean ceb
chan chant chap chis chok chos cill cipr cled clon coars coinc confl
confr cors countr crank cros crossb crust ctar ctibl ctric danc dav
day$ dazzl ddress deg dentl dern diagn dick dious dipl dmon dock doubt
dows drag drill drows dung dur dust dvers eamie earfu east$ eatio eclo
ecro edee edgi eeche eemi eena eese efre efri eja ellie elt$ embra
empti ennia entee entre eone eoty ephe erm$ erms$ erpa erproo ersho
ersua esci esho etha euni evou extri fasc fec film flak flor fond foul
freq fters fty$ furl fuss fuzz gad gant gawk gell gents giggl gious
giv glow glyc grand grant greas guid guing gull gush gutt halt hash
hawk hect hell highl hir hoth humbl iabi ib$ ibs$ ickne idiou idne
iege ielde ienta iftie ild$ ilie ilt$ ilts$ ilu ingo inspi iors$ iplo
ipt$ ipti irl$ irls$ irra irru isba isspe itro ixa izzie jaunt jerk
jest joc jor judg jump kidn kook lan lap larg larl lath latt lcer
ldest lel leth lgat lick link lion llerg lles llness lloq llot lob
lunt lur lvag mail main maint marsh mbark mbat mbod meas mech merr mi$
middl mind missp mlin mmens mmetr mo$ mong mousl mplac mplat mpled
mpol mugg muss nact nants natt ncurr nda$ ndem ndens ndercl ndersh
ndesc ndig ndisp ndon neers nents nex neym nhab nipp njunct nlier nlin
nlist nnel nniv nnounc nnov nonp nquer nscript nsing nslat ntact ntess
ntid nto$ ntom ntos ntrad ntrav ntrib ntries ntuat nul oach$ oale
obscu obtru occa ocea ociou odia ogma oida oinci oist$ onca onre
onstri ontai ontu ooche oor$ opli oppre optio orea orsa osh$ otra
ottie ouch$ oulde oule pals pern pewr phed phies phing pied pig pink
pists plift plom ppies preach prej proof ptim ptom purg quer quick
ragg ramb ramp rbar rbed rchestr rdain rderl rearm reel rexp rfer rgin
rheads rind rint rmark rnall rnic rnit roc rook rpass rpent rror rsec
rstand rtes rtiv rturb rudd rupt rvent rview rward sarr saw scatt scit
scomf scrap seam seat seed shift shor silk sket slugg smart smat snowb
sooth sord spend spong ssic ssit stas steam stest stful stfull stirr
stopp storm straggl strid strik stuff subtr sulk sull sumpt surm susc
swank symb symm tamp tart tas tchier tchiest tchy$ teas tempt tful
things tiz tough tour track trail trench ttend tties ttract tumbl
twitt uadra uance uave ubby ubje uddi uida uiti uitou ulca ullie unce
unch$ unchi ungi unhi unio unlea unny uote upu urtle urvi ussio valr
vap vast vif vinc wal wand wards wax weep welt whin wiggl wil wish
witch witt wledg wond woodc wriggl wy$ xcret xempl xer xhaust xon
xpans xting xtur xy$ yba ymme ysio ziest zin zipp zzes
""".split(): TRIPLE_SCORES[triple] = 7

for triple in """
^absc ^adh ^af ^anth ^aur ^earn ^enth ^foi ^gea ^grie ^jui ^knee ^koo
^loi ^nou ^obst ^obt ^osc ^phe ^pia ^preo ^roi ^schi ^scoo ^shou ^sie
^squee ^twe ^ulc ^ups ^utt ^voi ^vou ^whoo ^wrea ^yell ^zoo abie abse
ackbi adhe affli agree agri aim$ aimi aims$ aint$ aisi ait$ allio amne
ankle annou anse ansfi antie apple aree argo ariu artne ascu asphe
astra attai auce aulte aunde aunti ausa authe avoi awfu awl$ awls$
ayme babl bag bankr bast bies big bik bits blasph bless blood boss
bouts box brief brog bsid build bulld bund cak cash ccas ccin ccount
ccur chabl check chic chnic ciest cim clam coal cocc cog cogn concl
cool coup craft craz creep crud ctness ctom ctrin ctroc ctual curv
damp dand degr dial disgr djust dorm dot drupl duat dull dupl eaco
eague eaka eakie eavi ecca echno eclai eddi eene egge egia egio egrou
egs$ ein$ embla embroi emni encu enfra enha entie enua enuou epha epho
eppi eriou erlie eroo errea erspe erwei erwri espa esty eurs$ exclu
exhau extre fash feath ffy$ flat flour fol fool forc funct funn furr
gans garl gib gisl glad greed handb hands harr hat herm hex horn hyph
iame iari icky idua iefe iency igeo imble immu implo inch$ inchi intru
ioli ionee ippie iqua irmi irts$ isbe iscri isgui islo ispla itne itze
juic jur kidd lass lden leav left length lex li$ liar limp linq llif
llings llustr llyh loft lties lubr luc lunch lust macr manh marg maz
mblers merch mif mings mispr misst mmenc mmerc mock mpen mplex mpling
mpris mull mumm murd naut nclus nctiv ndanc nderf nderg ndings ndors
neat neq news nexp nfig nfranch nhandl niq niv nkest nliest nna$
nniest nobl nog nonr nscend nsed nsel nser nsom nstrum nsum nterd
ntment ntol nurs oardi octri offee ofo olt$ olts$ onclu onga onni ont$
onvo oodie oothe oppie oprie osau ossie othi outh$ outla owboa owie
paint peat phant piest pled plin pok pomp ppar prais prud psul puff
pus quar quett quir rban rber rbitr rbrush reas reat rech reen rentl
rett rform rhous rials risk rker rlies rments rmiss rnam rpris rrul
rsif rsions rtabl rthod rven rvers rvis sandb saur sched scill scour
scrim sculpt seh ship shov slack sland slipp spell sphem splac sport
squal ssail sse$ ssign ssist stam stem stepp stew stling stow strain
subd subscr sugg surp syst tarr tchers teor tew thent tiest tish toast
torc torm triat trogr trump ttic ttif tto$ tup uanti ubscri ubse ubu
ud$ uds$ uet$ uette uffie uile uine uivo ulla ulldo ulpa ult$ unclea
unfai unha unnie unpro unwa uori upa upho upple upsta upte uptio urry
ursi urtai ussy va$ vamp vang venl verm vial vies virt vist vy$ wad
wder wels worr xcept xplor xtrem xual yclo ylo ymo yphe yti ywo zy$
""".split(): TRIPLE_SCORES[triple] = 8

for triple in """
^abj ^abl ^abst ^alph ^anthr ^aph ^ash ^asph ^atr ^boi ^dio ^droo ^edg
^engr ^enj ^ess ^fei ^foa ^gee ^groo ^lie ^od ^omn ^oppr ^sci ^scre
^shoo ^slou ^thre ^thru ^ultr ^unq ^unscr ^upst ^vau ^za ^zo abbie
aboo accli actu aina ainte ainti airi airy alci alme alpha ammo andy
ansce antle aque arble ardio ardly arms$ arsi asa asca ashio astie
athi avia awn$ bash bec bedr bern bibl bird bitt blackb blaz breath
brok broth by$ ca$ caut cclim champ chas chol chopp cier ciph cists
civ ckin consc consp cook cost cream crob croc deem deh dget diet dium
dled dlin dling dlock doll driv dual eace eachi eape earie earra ecko
ecou eddle eeks$ eeve efro egna ejoi elde elf$ enchi encou erlo esco
esma esque etch$ eteo etou fanc fatt fell fem ffers ffirm fold foll
forw fum furb gas ghtly$ gim gistr glor gloss gnom gnor gons group
grudg guil gust harp heads herb hos husk iddi ields$ iety ightly igre
imp$ imps$ inau incli incre infle ingie inio inkie intri ior$ ircle
irs$ irt$ isho iski isru istru itta iwi iza jell kabl kick leag lebr
lessn lien limb llel llier llut lo$ lons ltiv maid mamm matt mean mell
mew mig misch misf misg mment mmitt mples nab nair nap narc ncept
nchant nclin nconv ncorr ncub nderb ndid ndness nduc ndustr ndy$ neous
netr nfess ngier ngiest ngy$ ni$ niac nil nions nious nless nlik nons
ntals ntes ntions ntrif nvinc nvis nvit obste oddle ohi oine oiso oite
ombs$ ombu omni onsciou onsta oomi oopi oriu orthy osie osy oughs$
outhe outra ovo owli owse pand pav pef perch phal pharm phob pholst
piec plant plen pling pont portr ppend pple$ pples proh pse$ pter
punch pupp putt quin quint rack rak rand rans ratt rattl rces reall
reed reun rfull rhead rick rie$ riot riums rket rland rless rons rrenc
rrev rrid rsem rud runn rust sar scall scen schem scipl secl sell
shell shest shimm sics snak soft sold sorr sound sourc sque$ sterl
sties stinct stled stretch subt suit tals tants teen tenc text theor
thic think tick tob tok tousl train treas treat triev troll tterb
ttrib uadri uble uddie uide uish$ ulce ultra ulu umbra unba unbe unbo
unctu und$ unli unsea unt$ unts$ upti urcha uss$ ussi usu vanc versh
vind want weed weight whipp xhib yne yno zers
""".split(): TRIPLE_SCORES[triple] = 9

for triple in """
^accr ^aggl ^alb ^aug ^ax ^boy ^brie ^eas ^ecl ^ej ^ench ^ens ^gre
^hay ^inq ^joi ^kna ^ko ^mau ^may ^mee ^moi ^nai ^obstr ^oct ^ol ^orch
^outd ^prie ^quie ^sce ^ska ^sku ^sme ^smoo ^swo ^thra ^threa ^tria
^twee ^unn ^untr ^upp ^ut abstra accou acta adua ady aero affle afts$
aggre agna agni ahs$ airli aive alde alks$ allia allie almi almo alpa
amba angli angu anha anna annie ansa anva appa appo apsu arba arly
arm$ arta ashie asio assai attra attri auli aunche autho auti avai
ayer$ ayers$ aza azie azo backb bass battl bbers bbier bbiest bett bif
black blic bout brand bras brav bridg brown bsol buck budg bugg burr
bush bust canc canv capp carn catch cath ccept cef cenc cew charg
chees chet chill chrom ciall cist ckness clean clear clim comf corp
crav crem cross ctif ctly$ curt cust dabl dall ddies ddy$ deadl deal
defl dens dew dibl digr dings discl dispr disq dle$ dles dmir doubl
down dox drat dream dvant dying each$ eacti eadli eauti ecrea ectua
edou eek$ eeti eets$ efie eite ekee elia elio ellu emie ench$ endu
enga engi enthu entiou entua epta epto erci erde erdo erfi erga erha
erki ershi erspi erto esie esou etba etfu etho etry eur$ ewri exco
excre excu expli expu fabr fault feat fend fers fes ffin ffled ffling
fiabl fight fitt flam flash flex foc foot forb found freel fug furn
genc germ ggest ghed ghing ghters gibb glass glob gnos go$ grim ground
guar guard gued gyr hang happ harm hast headl hears heat hipp hook hop
iably iacs$ iani idio iefs$ ield$ iently ieva ievi iewe ifia ifle iggi
igns$ ihi iltra ilve impri inju inta intra iny iole iora ioti ipro ir$
ird$ irds$ irma iscre ispu itho iths$ ixi izo izze izzle just kel kil
kindl labl lact laps last laz lef legr leph lets lia$ lings llabl lle$
llets llis lluc llying lmin lock logr loos loq lpat lsif lsiv ltern
lters ltrat lud lux lver lys mabl mang manl mans mbin mbler mbul mfort
midw mir mists mmand mmend mom mpact mpier mpiest mpil mpir mple$ mpy$
mur must ncarn ncat ncem ncers nciat ncip ncomm ncons nctions ncumb
ndant ndar ndef nderc nderp ndert ndest ndul ndulg nec neff nenc nets
nett nfirm ngag ngem ngin nhal nia$ nint nject nkier nkiest nky$
nlight nnier noc nousl nsens nsign nsult ntall ntert ntiall ntill ntit
nud nutr nvert nym oaste obstru obu oddi ofa off$ offs$ oggie oho oin$
oins$ ointe ointi olia olly omb$ ombe ombo oncu onfo onfu oniou onme
onque oode ooed$ ooing$ ophy oreo orgi orki ormu orna orthie oru orwa
osci ottle oty ouchi ounta ounti ounts$ ource oure ourna owde owls$
oying$ palp pant patt pec penn perb petr phor pigg pip pir plex pock
point postm pott ppings ppoint pprec pprov preh prer prett pris procr
progn proj protr pull pun push puss quant quenc quid quot rann rants
raw rbal rbon rcat rched rching rcing rdon redr resh rfac rfeit rgan
rgat rill rled rmac rmen rmer rmost rmul rners ro$ rout rped rpet
rrant rresp rric rrier rrif rsel rships rsit rthy$ rtions rtly$ rty$
rum run rve$ rvic rwom rying sab sals salt sand sconc scor scount
search segr semb sept settl shabl shap sharp shoot shuffl sib silv
skat slav sleep sman sod sons sort sot south speed spin spok ssag stak
stall stanc stand stel stenc stens stiff stit straight strok stron
stroph stul sturb sug sult sum sweet tatt teg them therl thick thous
thy$ tier toil tops tous tow trap tron trust ttest tual uadru ubme
ubmi ubo ubri ucce ucte uest$ uitie ulga ulls$ ulmi ulse ulsio umbi
umbli ummie unca uncia undre unea unfi unla unrea unse unwi uousne
urga urns$ urro ury usca uske usta utche utri uttle uxu vail vals veg
verdr verg vings void vok vul vulg wag warm wel whol wick win xcit xid
xit xplic xur yca yco yho yla ysti zen zier zzle$ zzled zzles zzling
""".split(): TRIPLE_SCORES[triple] = 10

for triple in """
^ampl ^anc ^bai ^chlo ^clou ^croo ^crou ^day ^empl ^enr ^esp ^et ^excr
^gai ^gho ^grea ^infr ^ing ^insp ^jau ^neo ^noi ^noo ^obj ^obsc ^om
^orn ^orth ^outf ^outp ^ox ^pau ^pay ^poe ^quee ^sei ^shoe ^shru ^thou
^toi ^ung ^uph ^vie ^way abra acci adge advi affo ague ah$ aids$ aime
ajo alk$ alti alue ampa ampli ampu anche andba aneou angs$ anie anshi
appoi aptu arci arle arria arse asci assu asy aths$ atie aunte ause
beat berr bid bin blem blim book bstant bstruct bur caps caus ccus
cers chanc chin chlor ckad ckag claim cling cloth coc coff conq coop
cot court crac crack cruc cub curl dar dders defr dents derm descr
detr died dill disg dmin doc dogg dos dram dvent dvert dvis eara earne
easse easte eche echni ecki eckle eclu ectri edra eedie eedle eeke
eeps$ ehi ehou eights$ elea elly empla enly enso eoccu epai epea eple
ept$ erbo erca ereo ergi eroi estri ethi etie etta etto evie eway exto
fan fast fect ffle$ ffles fiers fig flag fogg frig front frost gab
gard garn garr gem ggier ggiest ggy$ gnet gov grac gran hamm hard hend
hes hid hil hist hood horr iac$ iagno iant$ iarie iatri idea idle ief$
iff$ iffi iffs$ igma ign$ illy ilte imma ims$ infu inna innie intro
inue invo iphe isci iscu isfi iske isla istre itch$ jud junk lang
lentl lked lking llag llied llin llit llum lor lot low lster lumb lumn
lus lving mah maj mall manc mann masc merc miest misr mitt mmy$ moll
mpar mpat mplem mplet mpor mpreh musk nacc narch ndabl ndemn ndenc
ndiv ndle$ ndled ndles ndling ndly$ negl nfer nforc nfus ngen nhol
nick nip nium njur nod nois norm north nsions ntangl ntegr nthus nties
ntip ntiq nton ntor ntric ntrov nunc nur oarse oati oche ofte oggle
ogno oice oints$ oje oldi omfo omie omplai ond$ onds$ onspi oofi oofs$
ookie ool$ ools$ oop$ oops$ ooze opla orci oriou orpo osa osmo osphe
oss$ oths$ otia ount$ owl$ owni oxy oyed$ palm parl parr pars peac
persp pict pier pies plast ples pod pois pond pow ppear pprais ppreh
ppress pract print pron pting purp ques rbat rce$ rcer rcul rders
rdly$ react rebr rfect rgenc ria$ ried right rior roll room rough rpor
rpos rriag rrows rsen rser rstat rtat rub rved rves rving sad sall
salv sauc scant scov scul sest shak shiest shion shment siest sill
sinf sings sking slat spers sput ssar ssent ssert ssors stag ste$
stead stes stibl stick stiv stol stom strib string stry$ stubb sunb
surg surv syn tac tard teer tists tocr tos touch trac trag transc trim
tripl trit troubl tton turb tyr uara uba ubbie ubco ubsi udde uent$
uer$ uge uita ull$ umma umpie unfo unkie unsa unsu upi uple uria urie
urle urli urn$ urna urpo urrie ushie ustle vend verp verpr vibr vict
vir visc vish volv warr wear weath wild will with word worth xam xim
xper xpress yard$ yards$ yro zer zon
""".split(): TRIPLE_SCORES[triple] = 11

for triple in """
^abd ^abstr ^accl ^ach ^anch ^arg ^arm ^bre ^bree ^broo ^chea ^dau ^eg
^emp ^encr ^enf ^err ^excl ^flee ^frie ^gna ^hee ^imb ^incl ^ingr ^joy
^nau ^oc ^opp ^outb ^outw ^pree ^pru ^quo ^reo ^scou ^scree ^shea
^shre ^spea ^spla ^squea ^stai ^strea ^sui ^tau ^unst ^upr ^vu achi
acqui actua adio aed$ aha aing$ aite alve ample andie ang$ angui anspo
antia appli apse aqua arbe arca argi ario ariou arli arne aso assie
assio astu atchi ath$ attie awle beaut best betr bew bis blig bling
bord bot bound cand ceas cell centr chast chatt ciousn clin cow ctabl
ctuat cum cup dag dam desc dger disl displ do$ dress dult eadie eage
eami eane edde eels$ eeme eeze effi eight$ eju emai enca enco enia
enne ensu entle envi eons$ ep$ eps$ erbi erdi erpri erru ervie eshi
estle estra estru ethe etrie euro exhi exua eying$ ffus flatt fresh
fuln fund gan gers gment gnost gog greg hav heart hel holl iage iary
icte iere ifti ifts$ illie inea inee infla inie inqui insta inua iola
ipple iptio ipu ispa ispro itchi ith$ itiou itle itra kin lant leas
lessl libr lics lign lith llar llas llions lloc llop load lousl ltim
lty$ luat lve$ lved mad mart mbing mens meth mistr mmiss mmon mpens
mprov mpuls mun nan nast nceiv ncert ncis nctur ndel ndol nerv nfin
ngel niest nis nistr nnies nnot nogr nop nses nsor nstrat ntabl ntell
nten ntend ntens ntern nterv ntiat ntract ntry$ nty$ numb oache oarde
obbi obje ocka octo oda odie ods$ ogre ohe oint$ ollie olls$ ols$ ompi
ongi ongre ongs$ onvi oodle oofe ooki ooli oome opie oque orche orshi
osts$ otche ough$ ounci ountai oupe our$ ours$ ourse pall pell pent
pepp pest pett phras plet pogr por ppropr pric princ proph prosp pses
pted punct purs que$ quent rbit rced rcept rches reapp refl ress rger
rient rim rium rling rmit round rrying rtak rtur rubb rul sanct sass
scont seas seb set sham short shy$ sier smok solv ssiest ssin ssoc
stent still stle$ stles stud stup stur subc sund surf tag tant till
tisf tism transl trav trop ttling tun uct$ ucto ucts$ udgi uence
uestio uggle uishe ump$ unbu urbi uriou uspe usto ustra utu uzzle van
vas vem vens view vill vow walk wast wled wling wned wning wood xec
xpect ycli ydra ylla
""".split(): TRIPLE_SCORES[triple] = 12

for triple in """
^acr ^agr ^amp ^arb ^as ^attr ^beau ^blea ^cree ^cry ^dei ^ec ^embr
^fau ^floo ^fluo ^fly ^fru ^frui ^glu ^gou ^gue ^inj ^is ^it ^kee ^lee
^nea ^nee ^on ^org ^outs ^pie ^prea ^reu ^sche ^shee ^snoo ^soo ^spli
^swe ^swea ^theo ^thri ^toa ^ur ^wro abble abou abri acia acka ackle
acri acro addi adva aggle agne agra alco alcu alie alke alua ammi amp$
ampi amps$ ancho ando ansmi aple appie apti arce arche arna arve aske
aspe asta asto atch$ atia aughte augu away ax$ batt bbled bbles bbling
bby$ bled bomb break burn cac carr cart cass ceiv cens cert cet chem
chron cism ckier ckiest ckled ckling coh crim curs cus decr disb eaki
eams$ eans$ easa echa ecli eede eel$ eeli eep$ eje encha enche enci
encie enfo eously epla epri erbu ertu espi essa etee etio exci explo
expre exu fall fals fath fel fet fit flect flow fract fter fut gentl
get ggers ggle$ ggled ggles ggling gibl gil gning gram grams graphs
gue$ gues hal hall haz heav iato iba ibble ickie ict$ icta icto icts$
icy idde ideo ift$ ig$ igno igs$ imbe impi inche indo ingui inhe inkle
inso ipo isha ishme isre istle istri isu ittle ix$ journ keep kier
kiest ky$ land lav lax lcul lded len lies lis llig llows lod lum lyt
mach marr matr max mbed mem mend merg mess mier mies mish mism mmut
moth mpass mplic myst nant narr ncid ncil ncomp ndat ndec nderl nev
nfect nfid ngest ngrat ngul nher nial nier nings nion nkers nment
nners no$ nonc nse$ nserv nsist nsul ntam nterf nterp ntiv nuat nut
nven nvers nvest oade oads$ oate oci odge oili oils$ oki oll$ ollu
olste ombi omma omy oncei onto ontri oof$ oole ooti ophi oppo opti opy
orni orru ortho oshe ostu osu otu oughe ought$ oura ousne oze pack
pens perp phen ple$ pleas poll pon poth ppier ppiest pplic ppy$ pret
progr prol pyr qual quat quiv rach ran rcharg real rend resc rip rism
rists rmal rob rock rog rpret rried rrit rrupt rsion rters saf sapp
sappr scend sep shier shin show sibl sick sies simpl singl sint sir
sked sob spens spit spond spos sser ssibl ssier ssor ssy$ stal stern
stier stiest stif stock strang stress strict styl subj susp syll tail
tang tax tcher tern thet thund tingl tings tious tly$ to$ togr tort
tox ttier ttiest ttled tum tus ubsta ucki ucks$ uctu uddle uffs$ uire
uise uit$ uite uits$ ulta ummo umps$ umu ung$ unki unks$ unni uno uns$
unta unte upli ur$ urgi urne urs$ ustie usts$ vels veng verc verd verh
verst viat vor wash wid wind wir wis xat xped xpos yle yma yme ypi
""".split(): TRIPLE_SCORES[triple] = 13

for triple in """
^aggr ^ang ^aq ^asc ^astr ^at ^auth ^blue ^by ^chai ^chro ^coe ^dai
^die ^dy ^expr ^fee ^flou ^gau ^goa ^hau ^hei ^hoa ^ign ^instr ^jou
^kni ^ly ^ob ^outr ^plai ^ple ^plo ^poo ^py ^ske ^sle ^smi ^soa ^spee
^sty ^tho ^unp ^unpr ^whee ^wra ^ze ab$ abli abs$ abso aby achie adia
ads$ aft$ aide airs$ alia ambe ambi ambu amou amu ancie ania anki
anks$ anno ansi anthro anto any aph$ apho aphs$ arbi arbo arki armo
asce aspi astro atri atria awa bble$ bef beg beh blish bon bric bserv
buff cab calc camp ccess ccup cept che$ chiev chor cian cians cis
ckets ckle$ ckles cky$ clos cock cong cord corn cos cosm cott cred
cret crit ctat cter dal destr diest dig discr dish dol don dow dyn
eaks$ eale eals$ eam$ ean$ eani eas$ ebe ebi eboa ebra eck$ ecke ecks$
ecla ectu eedi eele eens$ eet$ eete efle elve em$ embo empo ems$ endo
enie enli enou entra eogra eolo eon$ erbe ercu erfo erfu erhea erli
erns$ erpo erpre erro ersio erta erwo evia exo expa exti eyed$ fam fe$
ferr fess fier fill fish fluor fort fted fting gaz gent ghten ghter
gmat gned gnit gramm har head hem hens hib host ibbe iche ickle ido
ients$ ifo ifte iggle iki ilde im$ immi immo indle inds$ infa inha
inni inno inou insti instru int$ into ints$ inva invi iogra ios$ iple
ipli iqui isce ishne issa isso jack lag lars las lett liest liev light
lla$ llus los lov ltipl mant mass mbers mbling meg mics migr mim misd
mmers mmod morph mort mos mpers mport nac nav nchis neur new ngled
ngling nguish nness nny$ nounc nship nsibl nsol nspir ntain ntent
nthrop nval oad$ ob$ obble oble obs$ occu od$ odde oggi ogie oids$
oil$ oise oiste ol$ omba ompli onci ondo onia onju onstra onstru ontro
onu ooni oos$ oots$ ophe opria orbi orga orke orks$ orns$ orri osco
oso osta oth$ otto ouble ouche ousi outi owle pel phers pick pist
priat prob pros ptic ptur puls put quart ra$ rab read recl rej restr
ringl riousl rman rmon rnal rner rness rousl rrang rrect rrog rship
rsing rtain rten rtin rtis sabl sacr san scap scar scat scrib script
seq sett sew shers shness sist soph spar sper spic spons ssif ssim
ssur stig stil stion stly$ struct sub subl subst ta$ tak tall tast
techn tef tell tem tens the$ therm thol tig tness tol tons tot tract
trad transm trib try$ ttles tuat tub uals$ uarte uati ub$ ubbi ubs$
uca uck$ uff$ uity uke ulge ulli ulsi ulte ummi umpi un$ unche undi
unge unk$ unma unti uppe urri usa ushi ust$ utti utto vern vest wak
wav west wher writ xist ycle ydro yra yri
""".split(): TRIPLE_SCORES[triple] = 14

for triple in """
^abr ^acq ^add ^aer ^aft ^appl ^asp ^ast ^aud ^ble ^brai ^broa ^coi
^dee ^dre ^drea ^eng ^enl ^esc ^est ^fie ^fle ^gree ^gy ^ic ^im ^incr
^ir ^ka ^key ^lou ^occ ^opt ^ord ^outl ^phy ^play ^pou ^que ^sai ^sau
^scru ^shri ^smu ^snu ^spoo ^stee ^stro ^stru ^tai ^tee ^tha ^thro
^trai ^uncl ^us ^vio ^wha acle affe aggi air$ aire aise alla alu amble
amma anchi ancy andle ank$ aphy appea ark$ arks$ arma arme armi arni
arou arrie art$ arts$ asso atho atro atta audi avo awi axe azi back
ban band bet bic bill bing bject board bol bull cals cann carb card
char cher cies cil ciousl cken clar cod congr creat curr dded dden
dder ddle$ ddled ddles ddling decl depl desp dging dier diff disr dor
eable eak$ eame ears$ earte easo easu ecei ecia ecra ecre edie eeds$
eeing$ eepi eere eeri eho eive ello elte emble empe ento eppe epro
eptio erfe ermo ern$ erni erpe errie erry ersa ersta ert$ erts$ escri
eshe etai etche ettle etu ews$ ex$ exce far fat fix fus gest ghted
gies git gnif got grav hand iance ibra iciou icti idly ids$ iece igge
igna igne igo ils$ imple impli impro impu inca ind$ infi info ingle
ink$ inki inks$ irri ishly ispo itua iums$ ixe ject la$ lad lders lec
lem lesc lier lig lik liq lish llab llect llers llest llet llies llion
ltur lves ma$ mand mark mble$ mbled mbles mill miss mmat monstr mount
mov mpan mplif nas ncer nction ndent nderst nduct neer nent ngle$
ngles nin nnect nov nsion nstit nsur ntar nterc nterpr ntest nus nvent
obbe obo oed$ ofe offi ogge ogs$ ogue oid$ olds$ omple ompre ompu ondu
oney ong$ onie onou onsti oods$ oone opho orce orge otti oundi ouri
oute owne pan path phy$ pid pill plan plat pop prim priv ptions ptiv
publ quest quit rang rar ras rden reass recr regr req rged rges rging
rians riat rlin rment rod rom rtun sag scenc scent secr sect sen sers
sev sex shad sim soc sor spac spher ssembl stabl stics subm succ summ
surr tan tap tend thor tid til tir tis tist transp trat ttle$ tty$
uckle uffle ug$ uggi ugs$ uls$ ultu unctio uously uppo urba urde ush$
vabl vic vig viol vot war ways whit xic ycho yli yna yste yte
""".split(): TRIPLE_SCORES[triple] = 15

for triple in """
^abs ^act ^ag ^alt ^amb ^arch ^aw ^bio ^boa ^bru ^doo ^dru ^env ^geo
^goo ^gua ^inn ^ke ^kno ^loa ^my ^neu ^obl ^pai ^pee ^pha ^phi ^plea
^poi ^schoo ^scri ^sky ^sma ^smo ^spri ^spu ^strai ^stre ^swee ^too
^trou ^unm ^unt ^unw ^wee ^wei ^who ^wre ^zi abbe abbi abe accu ache
acie aco act$ acts$ acu ad$ ada addle adju adu afe ag$ ags$ aid$ allu
aly amo angi anu appre archi ardi arpe arri ashi ass$ assa asts$ atti
attle awe aws$ axi bab bal barb barr bber be$ ben bod brat cabl cam
capt carp cas cast cav cel cem cial cin class cles comb compr conj
conn const cult dding denc dged dges diat dil dim din dism eache eadi
eali eare eari easi eats$ ebo ectro edia edne eds$ een$ eers$ effe
egra egre egu eha ehea elu emba embe enge ensa ensio entri entu eous$
equa erba ercha erea erio erla erly erra ertai eru esa esca espe esso
ety extra fact fest ffect ffed ffing fil forg gall gar ghting gnat gor
grad gress gul hab hol hold hon hors iable ias$ icie icle icro ictio
iddle ience iffe ifu ighti igu il$ illio illo illu impre imu incu ingi
insi iolo ipi ippi iro isca iscou isma isms$ ispe issio isto istra
itia ivo ize lab lac lding lenc lent lers lest liat lleg long lop lted
lting magn mak mas mers mest metr mid mous mpress mput na$ nad nam
nched nching ncies ndit nef nform nics nies nism nner nol nor nsat
nsid nsit nsiv nstruct ntag nterl nterm nterr ntial ntif ntil ntim
ntion ntur oards$ obli obse ocia ocra odo ody offe ofi og$ oile ommo
oms$ onco ondi onso ooke ooks$ ooms$ oope oose oot$ oote opa ord$
ords$ ormi orms$ orne orro ortu ospe ossi otio owa owns$ ox$ oys$ pag
pass past patr pend pert perv pet pher phic phot phys pic pil pin plic
poss post pot pport ppos pref prem prep press prev prod prom pur py$
quadr ract rall rals rant rav refr renc rge$ rian rier riest rig rings
rious ris riv rning rnish rol rrat rrel rries rrow rsed rses rter rtif
rus rvat sav scal shly$ sic sil spec ssess ssions sten ston sty$ subs
suff supp suppl sy$ tab tam tect temp thed thers thes top trans transf
tte$ tten ttes tul turn ually uatio ubbe ube ubi uga uisi ulou umpe
unda unke unne unre up$ ups$ urni urse usse ut$ uto uts$ verl verr vet
vin viv wall ward way$ wom ypo zed zes zing
""".split(): TRIPLE_SCORES[triple] = 16

for triple in """
^adj ^ar ^arr ^art ^bee ^bloo ^bou ^cau ^chee ^cle ^clea ^clu ^crea
^cy ^dou ^dri ^dro ^ed ^eff ^en ^end ^entr ^er ^exh ^expl ^fai ^fea
^fou ^fre ^gli ^gro ^grou ^gru ^gui ^hai ^ill ^impl ^infl ^inh ^inst
^intr ^je ^lau ^loo ^moo ^obs ^off ^pea ^pra ^psy ^rai ^roa ^roo ^scra
^see ^she ^slee ^slu ^sni ^squi ^stea ^thu ^trea ^tro ^unb ^unh ^unl
^wai ^whe ^wri acco aciou acki acte acto acy adde admi adve affi afte
aga aili aini alte ampe ams$ anci anda anni antly aphe aphi appi appro
arge arke arre arro ash$ ast$ auto aw$ ayed$ ball bar bed bel bell bor
bul bus butt cad can cant cess ched ching ciat cif cious cip ckers
cle$ con constr cop cov crat ctic ctors cycl depr ders dge$ dict dies
dif dir distr dness duct dul eake eal$ ear$ eat$ eathe ecta edge edo
eepe eer$ ego ehe ell$ ella ells$ emu ency enda entio epe epti epu
erce erco erge eria erme erne erou erre erri erso erte ervi espo essne
esto ests$ etri etro ew$ ewi expo exte eys$ fac fed ffer ffic fing gal
gam gger gin gists gon hydr iali icki icks$ idge ient$ igni igra ilia
ills$ imo impa indu infe inke inne inse insu inti inu inve ique isio
isse ista itche ithe ken lam lanc lder lect lectr let lib lim loc lon
lous mac mast micr mist mmed mming mmun mol mpet mping mpos mus mut
my$ nag nall nals nanc nches ndic neg nel nem nest net nge$ ngers nges
nif nists nked nker nly$ nned non nos nous nters num oard$ oat$ oats$
oba obe obi oce ocki oco oing$ old$ olla olli ollo olve om$ ommi ompo
onfe onfi onge onne onsu onta ook$ oom$ oon$ oons$ oppi opu orde ordi
oria ork$ orm$ orme orn$ oro orou orre ort$ orta ortio orts$ ost$ oste
osti ounce ounde ounds$ ova oxe pac pap perc perf perm phil plac ppers
proc prot psych ption ram ranc rap rded rder rdin rding rent repl resp
rew rid rif ril rish rist rked rking rmat rmed rming rnat rned ron rot
rred rry$ rse$ rson rtic rtion scop sec sens sher sin sions spect spir
ssness stim stin tched tching tent terr thing tiat tif tit tom tud tut
ubli ucke ucti uctio uffe uffi uing$ uli uma umme uous$ urge urre usio
usti vac vag var vent verb vil voc wat wers work xed xing ysi ze$
""".split(): TRIPLE_SCORES[triple] = 17

for triple in """
^ac ^adm ^adv ^aff ^al ^ann ^ap ^app ^appr ^att ^aut ^bli ^blo ^blu
^brea ^che ^cho ^chu ^cli ^coa ^coo ^cre ^dia ^dra ^emb ^enc ^ent ^ep
^eq ^ext ^extr ^fli ^flo ^flu ^foo ^fra ^free ^fri ^fro ^gla ^glo ^hoo
^hou ^id ^imm ^impr ^irr ^ji ^mai ^mea ^mou ^op ^or ^pho ^ree ^rei
^rou ^sco ^scu ^shu ^ski ^slo ^sna ^sno ^spo ^squa ^stra ^stri ^swi
^tea ^the ^thi ^tou ^tre ^twi ^ty ^unf ^unr ^wea ^woo aba abu aca acce
actio ado agge ago ail$ aile ails$ ain$ ains$ aki all$ alli alls$ alo
am$ amme ands$ angle anke anne ano anta ap$ apa apo aps$ arde ards$
aro arra arte asi at$ atche ats$ ava aying$ aze bas bat bbed bbing ber
bes but cap cent cer ches cid cing circ cket col com compl cor corr
ctur cur cut cy$ deb dep dest dist dom duc dy$ ead$ eade eads$ eati
eave eba ebu ect$ ecte ects$ eda edly edu eed$ efa efo ege elie end$
ends$ ense entia enu epi epre eque equi erma erna ersi erva esce eso
essly esta esu eto etra etti evo ewa ewe ewo exa exi fer fir form ful
full ged ger gging gic ging gist grat gur her hous hum hyp ially ials$
ians$ iati iatio ibly ibu icia ick$ ico ida iers$ ieve ify ige ight$
ighte ights$ igi ill$ illi ilo imme impo ince inci ino iousne ipa ips$
ircu iri irre ishi issi itti kers less lev lid lif lism lists liv llat
llow lness lter lut mag mal mar mber misc mit mmer mod mped mper mul
mult nabl nced ncing ners nged nging nim nish nking nning not ntal
ntat ntic ntin ny$ ock$ ocks$ ocu odi odu oes$ oga oge olde olle oly
omme ommu omo ompa ompe once onde onse onsi onte onti ontra onve ony
ood$ op$ opi oppe ops$ orie orma orse orti osse ota ots$ otte ound$
out$ outs$ ovi own$ oxi pal part pen phon port pper pred prof prop
prov pul rac reb rect reh rers rial rly$ rmin ros rring rting sat sel
sent serv sign sion sis siv som ssiv ssly$ stor strat sur tches term
test tim tin ton tric tters typ ual$ uali uate uce uci udge udi ued$
ugge ulne ulti umbe umble ums$ unco ushe uste utio vert vid vol ype
""".split(): TRIPLE_SCORES[triple] = 18

for triple in """
^ab ^acc ^ad ^all ^am ^an ^ant ^ass ^av ^bea ^bla ^boo ^bra ^bri ^bro
^chi ^ci ^cla ^clo ^cra ^cri ^cro ^cru ^dea ^em ^ev ^exc ^exp ^gi ^go
^gri ^gu ^hy ^inf ^ins ^inv ^ja ^jo ^ju ^lea ^na ^nu ^pla ^plu ^pri
^qua ^qui ^sca ^sea ^shi ^sho ^sla ^sli ^sou ^spa ^spe ^spi ^ste ^sti
^sto ^stu ^swa ^sy ^tri ^tru ^unc ^uns ^vo ^we ^whi abi ably abo aci
ack$ acke acks$ acti adi agi aine ala alle allo ama ami ana and$ ande
andi ane ange ans$ ante ants$ api appe ar$ ard$ aria arie ars$ arti
ary ase ashe asse assi asti ata athe atu avi ays$ bit bles car ced cit
cked cker cking coll conc cond conf cons cont contr conv count cted
cting ctions ctiv ctor cul dat def del dem den dent det dev dic disc
disp diss dit div dly$ ease eate eca ece eci ecti ectio ecto ecu ees$
efe efi efu ega egi el$ ela elle elli elo els$ endi eno ensi ente
ently epa epo erie ermi ero erse erti erve ery ese esi essi essio este
eta ette eva evi exe expe fied fies fin fy$ fying gen ges gged graph
gy$ hom ian$ ibe ibi ible icke icu id$ idi ife ifi ifyi iga ike ila
illa ille ily impe in$ inco inde indi inge ingly ins$ ione ioni iously
ip$ ipe ippe ira isa isco ishe isi iso iste it$ ito its$ itte itu ium$
iva ke$ ked ker kes king lar leg ler lic lin list lled ller lling me$
mel men ments mer mes met mic mil ming mis mon mor mot nar ncy$ nded
nders nding nger ngly$ nic nist nom nter nting oca ocke ode ogra ogy
oke ola olu ona ono opo orte ory ot$ othe oti oto ounte ously ow$ owi
ows$ pat pe$ ped pers pes ping pit pol pos pped pping prec pres rabl
rad rag ral ref reg rem ren rep repr rer rest ret retr rev ric rin
rous rted sal sem ser shed shing sid sness sol son ssed ssing ssion
stat sted sters sting sup tabl tal tar ten ters ther tics tors tted
tting tur ude ues$ ule ulle ully um$ ume umi una une upe ura uri us$
usi uta uti utte val vat ved ving vis vit wed wer wing xes
""".split(): TRIPLE_SCORES[triple] = 19

for triple in """
^ba ^be ^bi ^bo ^bu ^ca ^ce ^cha ^co ^cou ^cu ^da ^de ^di ^do ^du ^el
^ex ^fa ^fe ^fi ^fla ^fo ^fu ^ga ^ge ^gra ^ha ^he ^hea ^hi ^ho ^hu
^imp ^in ^inc ^ind ^int ^ki ^la ^le ^li ^lo ^lu ^ma ^me ^mi ^mo ^mu
^ne ^ni ^no ^ov ^pa ^pe ^pi ^po ^pre ^pro ^pu ^ra ^re ^rea ^ri ^ro ^ru
^sa ^se ^sha ^si ^so ^sta ^su ^ta ^te ^ti ^to ^tra ^tu ^un ^und ^va
^ve ^vi ^wa ^wi ^wo able ace ade age ake al$ ale ali ally als$ ame an$
ance ani ant$ anti ape ara are ari as$ aste ate ati atio ato atte ave
bil ble$ bly$ cal call cat ce$ ces comm comp ction de$ dec ded der des
ding dis eco ed$ ede edi ele eli ely ema eme emi emo en$ ena ence ende
ene eni ens$ ent$ enta enti ents$ er$ era ere eri ers$ es$ ess$ esse
est$ esti et$ ete eti ets$ eve fic for gat ge$ ial$ iate ic$ ica ice
ici ics$ ide ied$ ier$ ies$ iest$ ifie ile ili ima ime imi ina ine
ing$ ings$ ini inte ion$ iona ions$ ious$ ire is$ ise ish$ ism$ ist$
isti ists$ ita ite iti itie itio ity ive ivi lat le$ led les ling lit
lly$ log ly$ man mat med ment min nal nat nce$ nces nder ne$ ned ner
nes ness ning nit nted ntly$ ogi ole oli olo oma ome omi on$ one oni
ons$ ope or$ ora ore ori ors$ os$ ose osi ote ous$ ouse ove owe par
per rat re$ rec red rel res ries ring rit ry$ se$ sed ses shes sing
sit sly$ sses ster stic tat te$ ted tel ter tes tic ties ting tion
tions tiv tor tter ty$ ul$ ula unde uni ure use ute ve$ vel ven ver
vers ves ying$
""".split(): TRIPLE_SCORES[triple] = 20


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
    >>> score_readability('shlomo')
    625
    >>> score_readability('shoebox')
    700
    >>> score_readability('merchandise')
    1337
    >>> score_readability('antidisestablishmentarianism')
    1515
    >>> score_readability('are')
    1900
    >>> score_readability('interesting')
    1962
    """
    result = 0
    triples = list(word_triples(word))
    for triple in triples:
        result += TRIPLE_SCORES.get(triple, 0)
    result = result * 100 / len(triples)
    # logging.debug('%s.english = %d', word, result)
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
