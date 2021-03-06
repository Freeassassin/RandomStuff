import os
import time
import keyboard
from random import randint

enemy_loc = [True]
options = [">", " ", " "]
weaponds = [">", " "]
items = [">", " "]
flee_chance = randint(10, 30)
fleed = False
fighting = False

TITLE = [["W     W EEEE  L     CCC  OOO  M   M EEEE ",	"W     W E     L    C    O   O MM MM E    ",	"W  W  W EEE   L    C    O   O M M M EEE  ",	" W W W  E     L    C    O   O M   M E    ",	"  W W   EEEE  LLLL  CCC  OOO  M   M EEEE "],["		TTTTTT  OOO  ",	"		  TT   O   O ",	"		  TT   O   O ",	"		  TT   O   O ",	"		  TT    OOO  "],["M   M  AA   CCC BBBB  EEEE TTTTTT H  H ",	"MM MM A  A C    B   B E      TT   H  H ",	"M M M AAAA C    BBBB  EEE    TT   HHHH ",	"M   M A  A C    B   B E      TT   H  H ",	"M   M A  A  CCC BBBB  EEEE   TT   H  H " ]]
END_SCREEN = [	" GGG   OOO   OOO  DDD       J  OOO  BBBB   !!! ",	"G     O   O O   O D  D      J O   O B   B  !!! ",	"G  GG O   O O   O D  D      J O   O BBBB   !!! ",	"G   G O   O O   O D  D  J   J O   O B   B      ",	" GGG   OOO   OOO  DDD    JJJ   OOO  BBBB   !!! "]
SCENES = [["ACT","I,","SCENE","III.","A","heath","near","Forres."," \nThunder.","Enter","the","three","Witches"," \nFirst","Witch"," \nWhere","hast","thou","been,","sister?"," \nSecond","Witch"," \nKilling","swine."," \nThird","Witch"," \nSister,","where","thou?"," \nFirst","Witch"," \nA","sailor's","wife","had","chestnuts","in","her","lap,"," \nAnd","munch'd,","and","munch'd,","and","munch'd:--"," \n'Give","me,'","quoth","I:"," \n'Aroint","thee,","witch!'","the","rump-fed","ronyon","cries."," \nHer","husband's","to","Aleppo","gone,","master","o'","the","Tiger:"," \nBut","in","a","sieve","I'll","thither","sail,"," \nAnd,","like","a","rat","without","a","tail,"," \nI'll","do,","I'll","do,","and","I'll","do."," \nSecond","Witch"," \nI'll","give","thee","a","wind."," \nFirst","Witch"," \nThou'rt","kind."," \nThird","Witch"," \nAnd","I","another."," \nFirst","Witch"," \nI","myself","have","all","the","other,"," \nAnd","the","very","ports","they","blow,"," \nAll","the","quarters","that","they","know"," \nI'","the","shipman's","card."," \nI","will","drain","him","dry","as","hay:"," \nSleep","shall","neither","night","nor","day"," \nHang","upon","his","pent-house","lid;"," \nHe","shall","live","a","man","forbid:"," \nWeary","se'nnights","nine","times","nine"," \nShall","he","dwindle,","peak","and","pine:"," \nThough","his","bark","cannot","be","lost,"," \nYet","it","shall","be","tempest-tost."," \nLook","what","I","have."," \nSecond","Witch"," \nShow","me,","show","me."," \nFirst","Witch"," \nHere","I","have","a","pilot's","thumb,"," \nWreck'd","as","homeward","he","did","come."," \nDrum","within"," \nThird","Witch"," \nA","drum,","a","drum!"," \nMacbeth","doth","come."," \nALL"," "," \nThe","weird","sisters,","hand","in","hand,"," \nPosters","of","the","sea","and","land,"," \nThus","do","go","about,","about:"," \nThrice","to","thine","and","thrice","to","mine"," \nAnd","thrice","again,","to","make","up","nine."," \nPeace!","the","charm's","wound","up."," \nEnter","MACBETH","and","BANQUO"," \nMACBETH"," \nSo","foul","and","fair","a","day","I","have","not","seen."," \nBANQUO"," \nHow","far","is't","call'd","to","Forres?","What","are","these"," \nSo","wither'd","and","so","wild","in","their","attire,"," \nThat","look","not","like","the","inhabitants","o'","the","earth,"," \nAnd","yet","are","on't?","Live","you?","or","are","you","aught"," \nThat","man","may","question?","You","seem","to","understand","me,"," \nBy","each","at","once","her","chappy","finger","laying"," \nUpon","her","skinny","lips:","you","should","be","women,"," \nAnd","yet","your","beards","forbid","me","to","interpret"," \nThat","you","are","so."," \nMACBETH"," \nSpeak,","if","you","can:","what","are","you?"," \nFirst","Witch"," \nAll","hail,","Macbeth!","hail","to","thee,","thane","of","Glamis!"," \nSecond","Witch"," \nAll","hail,","Macbeth,","hail","to","thee,","thane","of","Cawdor!"," \nThird","Witch"," \nAll","hail,","Macbeth,","thou","shalt","be","king","hereafter!"," \nBANQUO"," \nGood","sir,","why","do","you","start;","and","seem","to","fear"," \nThings","that","do","sound","so","fair?","I'","the","name","of","truth,"," \nAre","ye","fantastical,","or","that","indeed"," \nWhich","outwardly","ye","show?","My","noble","partner"," \nYou","greet","with","present","grace","and","great","prediction"," \nOf","noble","having","and","of","royal","hope,"," \nThat","he","seems","rapt","withal:","to","me","you","speak","not."," \nIf","you","can","look","into","the","seeds","of","time,"," \nAnd","say","which","grain","will","grow","and","which","will","not,"," \nSpeak","then","to","me,","who","neither","beg","nor","fear"," \nYour","favours","nor","your","hate."," \nFirst","Witch"," \nHail!"," \nSecond","Witch"," \nHail!"," \nThird","Witch"," \nHail!"," \nFirst","Witch"," \nLesser","than","Macbeth,","and","greater."," \nSecond","Witch"," \nNot","so","happy,","yet","much","happier."," \nThird","Witch"," \nThou","shalt","get","kings,","though","thou","be","none:"," \nSo","all","hail,","Macbeth","and","Banquo!"," \nFirst","Witch"," \nBanquo","and","Macbeth,","all","hail!"," \nMACBETH"," \nStay,","you","imperfect","speakers,","tell","me","more:"," \nBy","Sinel's","death","I","know","I","am","thane","of","Glamis;"," \nBut","how","of","Cawdor?","the","thane","of","Cawdor","lives,"," \nA","prosperous","gentleman;","and","to","be","king"," \nStands","not","within","the","prospect","of","belief,"," \nNo","more","than","to","be","Cawdor.","Say","from","whence"," \nYou","owe","this","strange","intelligence?","or","why"," \nUpon","this","blasted","heath","you","stop","our","way"," \nWith","such","prophetic","greeting?","Speak,","I","charge","you."," \nWitches","vanish"," \nBANQUO"," \nThe","earth","hath","bubbles,","as","the","water","has,"," \nAnd","these","are","of","them.","Whither","are","they","vanish'd?"," \nMACBETH"," \nInto","the","air;","and","what","seem'd","corporal","melted"," \nAs","breath","into","the","wind.","Would","they","had","stay'd!"," \nBANQUO"," \nWere","such","things","here","as","we","do","speak","about?"," \nOr","have","we","eaten","on","the","insane","root"," \nThat","takes","the","reason","prisoner?"," \nMACBETH"," \nYour","children","shall","be","kings."," \nBANQUO"," \nYou","shall","be","king."," \nMACBETH"," \nAnd","thane","of","Cawdor","too:","went","it","not","so?"," \nBANQUO"," \nTo","the","selfsame","tune","and","words.","Who's","here?"," \nEnter","ROSS","and","ANGUS"," \nROSS"," \nThe","king","hath","happily","received,","Macbeth,"," \nThe","news","of","thy","success;","and","when","he","reads"," \nThy","personal","venture","in","the","rebels'","fight,"," \nHis","wonders","and","his","praises","do","contend"," \nWhich","should","be","thine","or","his:","silenced","with","that,"," \nIn","viewing","o'er","the","rest","o'","the","selfsame","day,"," \nHe","finds","thee","in","the","stout","Norweyan","ranks,"," \nNothing","afeard","of","what","thyself","didst","make,"," \nStrange","images","of","death.","As","thick","as","hail"," \nCame","post","with","post;","and","every","one","did","bear"," \nThy","praises","in","his","kingdom's","great","defence,"," \nAnd","pour'd","them","down","before","him."," \nANGUS"," \nWe","are","sent"," \nTo","give","thee","from","our","royal","master","thanks;"," \nOnly","to","herald","thee","into","his","sight,"," \nNot","pay","thee."," \nROSS"," \nAnd,","for","an","earnest","of","a","greater","honour,"," \nHe","bade","me,","from","him,","call","thee","thane","of","Cawdor:"," \nIn","which","addition,","hail,","most","worthy","thane!"," \nFor","it","is","thine."," \nBANQUO"," \nWhat,","can","the","devil","speak","true?"," \nMACBETH"," \nThe","thane","of","Cawdor","lives:","why","do","you","dress","me"," \nIn","borrow'd","robes?"," \nANGUS"," \nWho","was","the","thane","lives","yet;"," \nBut","under","heavy","judgment","bears","that","life"," \nWhich","he","deserves","to","lose.","Whether","he","was","combined"," \nWith","those","of","Norway,","or","did","line","the","rebel"," \nWith","hidden","help","and","vantage,","or","that","with","both"," \nHe","labour'd","in","his","country's","wreck,","I","know","not;"," \nBut","treasons","capital,","confess'd","and","proved,"," \nHave","overthrown","him."," \nMACBETH"," \n[Aside]","Glamis,","and","thane","of","Cawdor!"," \nThe","greatest","is","behind."," \nTo","ROSS","and","ANGUS"," \nThanks","for","your","pains."," \nTo","BANQUO"," \nDo","you","not","hope","your","children","shall","be","kings,"," \nWhen","those","that","gave","the","thane","of","Cawdor","to","me"," \nPromised","no","less","to","them?"," \nBANQUO"," \nThat","trusted","home"," \nMight","yet","enkindle","you","unto","the","crown,"," \nBesides","the","thane","of","Cawdor.","But","'tis","strange:"," \nAnd","oftentimes,","to","win","us","to","our","harm,"," \nThe","instruments","of","darkness","tell","us","truths,"," \nWin","us","with","honest","trifles,","to","betray's"," \nIn","deepest","consequence."," \nCousins,","a","word,","I","pray","you."," \nMACBETH"," \n[Aside]","Two","truths","are","told,"," \nAs","happy","prologues","to","the","swelling","act"," \nOf","the","imperial","theme.--I","thank","you,","gentlemen."," \nAside"," \nCannot","be","ill,","cannot","be","good:","if","ill,"," \nWhy","hath","it","given","me","earnest","of","success,"," \nCommencing","in","a","truth?","I","am","thane","of","Cawdor:"," \nIf","good,","why","do","I","yield","to","that","suggestion"," \nWhose","horrid","image","doth","unfix","my","hair"," \nAnd","make","my","seated","heart","knock","at","my","ribs,"," \nAgainst","the","use","of","nature?","Present","fears"," \nAre","less","than","horrible","imaginings:"," \nMy","thought,","whose","murder","yet","is","but","fantastical,"," \nShakes","so","my","single","state","of","man","that","function"," \nIs","smother'd","in","surmise,","and","nothing","is"," \nBut","what","is","not."," \nBANQUO"," \nLook,","how","our","partner's","rapt."," \nMACBETH"," \n[Aside]","If","chance","will","have","me","king,","why,","chance","may","crown","me,"," \nWithout","my","stir."," \nBANQUO"," \nNew","horrors","come","upon","him,"," \nLike","our","strange","garments,","cleave","not","to","their","mould"," \nBut","with","the","aid","of","use."," \nMACBETH"," \n[Aside]","Come","what","come","may,"," \nTime","and","the","hour","runs","through","the","roughest","day."," \nBANQUO"," \nWorthy","Macbeth,","we","stay","upon","your","leisure."," \nMACBETH"," \nGive","me","your","favour:","my","dull","brain","was","wrought"," \nWith","things","forgotten.","Kind","gentlemen,","your","pains"," \nAre","register'd","where","every","day","I","turn"," \nThe","leaf","to","read","them.","Let","us","toward","the","king."," \nThink","upon","what","hath","chanced,","and,","at","more","time,"," \nThe","interim","having","weigh'd","it,","let","us","speak"," \nOur","free","hearts","each","to","other."," \nBANQUO"," "," \nVery","gladly."," \nMACBETH"," "," \nTill","then,","enough.","Come,","friends.\n"],	["ACT","I,","SCENE","V.","Inverness.","Macbeth's","castle."," \nEnter","LADY","MACBETH,","reading","a","letter"," \nLADY","MACBETH"," \n'They","met","me","in","the","day","of","success:","and","I","have"," \nlearned","by","the","perfectest","report,","they","have","more","in"," \nthem","than","mortal","knowledge.","When","I","burned","in","desire"," \nto","question","them","further,","they","made","themselves","air,"," \ninto","which","they","vanished.","Whiles","I","stood","rapt","in"," \nthe","wonder","of","it,","came","missives","from","the","king,","who"," \nall-hailed","me","'Thane","of","Cawdor;'","by","which","title,"," \nbefore,","these","weird","sisters","saluted","me,","and","referred"," \nme","to","the","coming","on","of","time,","with","'Hail,","king","that"," \nshalt","be!'","This","have","I","thought","good","to","deliver"," \nthee,","my","dearest","partner","of","greatness,","that","thou"," \nmightst","not","lose","the","dues","of","rejoicing,","by","being"," \nignorant","of","what","greatness","is","promised","thee.","Lay","it"," \nto","thy","heart,","and","farewell.'"," \nGlamis","thou","art,","and","Cawdor;","and","shalt","be"," \nWhat","thou","art","promised:","yet","do","I","fear","thy","nature;"," \nIt","is","too","full","o'","the","milk","of","human","kindness"," \nTo","catch","the","nearest","way:","thou","wouldst","be","great;"," \nArt","not","without","ambition,","but","without"," \nThe","illness","should","attend","it:","what","thou","wouldst","highly,"," \nThat","wouldst","thou","holily;","wouldst","not","play","false,"," \nAnd","yet","wouldst","wrongly","win:","thou'ldst","have,","great","Glamis,"," \nThat","which","cries","'Thus","thou","must","do,","if","thou","have","it;"," \nAnd","that","which","rather","thou","dost","fear","to","do"," \nThan","wishest","should","be","undone.'","Hie","thee","hither,"," \nThat","I","may","pour","my","spirits","in","thine","ear;"," \nAnd","chastise","with","the","valour","of","my","tongue"," \nAll","that","impedes","thee","from","the","golden","round,"," \nWhich","fate","and","metaphysical","aid","doth","seem"," \nTo","have","thee","crown'd","withal."," \nEnter","a","Messenger"," \nWhat","is","your","tidings?"," \nMessenger"," \nThe","king","comes","here","to-night."," \nLADY","MACBETH"," \nThou'rt","mad","to","say","it:"," \nIs","not","thy","master","with","him?","who,","were't","so,"," \nWould","have","inform'd","for","preparation."," \nMessenger"," \nSo","please","you,","it","is","true:","our","thane","is","coming:"," \nOne","of","my","fellows","had","the","speed","of","him,"," \nWho,","almost","dead","for","breath,","had","scarcely","more"," \nThan","would","make","up","his","message."," \nLADY","MACBETH"," \nGive","him","tending;"," \nHe","brings","great","news."," \nExit","Messenger"," \nThe","raven","himself","is","hoarse"," \nThat","croaks","the","fatal","entrance","of","Duncan"," \nUnder","my","battlements.","Come,","you","spirits"," \nThat","tend","on","mortal","thoughts,","unsex","me","here,"," \nAnd","fill","me","from","the","crown","to","the","toe","top-full"," \nOf","direst","cruelty!","make","thick","my","blood;"," \nStop","up","the","access","and","passage","to","remorse,"," \nThat","no","compunctious","visitings","of","nature"," \nShake","my","fell","purpose,","nor","keep","peace","between"," \nThe","effect","and","it!","Come","to","my","woman's","breasts,"," \nAnd","take","my","milk","for","gall,","you","murdering","ministers,"," \nWherever","in","your","sightless","substances"," \nYou","wait","on","nature's","mischief!","Come,","thick","night,"," \nAnd","pall","thee","in","the","dunnest","smoke","of","hell,"," \nThat","my","keen","knife","see","not","the","wound","it","makes,"," \nNor","heaven","peep","through","the","blanket","of","the","dark,"," \nTo","cry","'Hold,","hold!'"," \nEnter","MACBETH"," \nGreat","Glamis!","worthy","Cawdor!"," \nGreater","than","both,","by","the","all-hail","hereafter!"," \nThy","letters","have","transported","me","beyond"," \nThis","ignorant","present,","and","I","feel","now"," \nThe","future","in","the","instant."," \nMACBETH"," \nMy","dearest","love,"," \nDuncan","comes","here","to-night."," \nLADY","MACBETH"," \nAnd","when","goes","hence?"," \nMACBETH"," \nTo-morrow,","as","he","purposes."," \nLADY","MACBETH"," \nO,","never"," \nShall","sun","that","morrow","see!"," \nYour","face,","my","thane,","is","as","a","book","where","men"," \nMay","read","strange","matters.","To","beguile","the","time,"," \nLook","like","the","time;","bear","welcome","in","your","eye,"," \nYour","hand,","your","tongue:","look","like","the","innocent","flower,"," \nBut","be","the","serpent","under't.","He","that's","coming"," \nMust","be","provided","for:","and","you","shall","put"," \nThis","night's","great","business","into","my","dispatch;"," \nWhich","shall","to","all","our","nights","and","days","to","come"," \nGive","solely","sovereign","sway","and","masterdom."," \nMACBETH"," \nWe","will","speak","further."," \nLADY","MACBETH"," \nOnly","look","up","clear;"," \nTo","alter","favour","ever","is","to","fear:"," \nLeave","all","the","rest","to","me.\n"],["ACT","II,","SCENE","I.","Court","of","Macbeth's","castle."," \nEnter","BANQUO,","and","FLEANCE","bearing","a","torch","before","him"," \nBANQUO"," \nHow","goes","the","night,","boy?"," \nFLEANCE"," \nThe","moon","is","down;","I","have","not","heard","the","clock."," \nBANQUO"," \nAnd","she","goes","down","at","twelve."," \nFLEANCE"," \nI","take't,","'tis","later,","sir."," \nBANQUO"," \nHold,","take","my","sword.","There's","husbandry","in","heaven;"," \nTheir","candles","are","all","out.","Take","thee","that","too."," \nA","heavy","summons","lies","like","lead","upon","me,"," \nAnd","yet","I","would","not","sleep:","merciful","powers,"," \nRestrain","in","me","the","cursed","thoughts","that","nature"," \nGives","way","to","in","repose!"," \nEnter","MACBETH,","and","a","Servant","with","a","torch"," \nGive","me","my","sword."," \nWho's","there?"," \nMACBETH"," \nA","friend."," \nBANQUO"," \nWhat,","sir,","not","yet","at","rest?","The","king's","a-bed:"," \nHe","hath","been","in","unusual","pleasure,","and"," \nSent","forth","great","largess","to","your","offices."," \nThis","diamond","he","greets","your","wife","withal,"," \nBy","the","name","of","most","kind","hostess;","and","shut","up"," \nIn","measureless","content."," \nMACBETH"," \nBeing","unprepared,"," \nOur","will","became","the","servant","to","defect;"," \nWhich","else","should","free","have","wrought."," \nBANQUO"," \nAll's","well."," \nI","dreamt","last","night","of","the","three","weird","sisters:"," \nTo","you","they","have","show'd","some","truth."," \nMACBETH"," \nI","think","not","of","them:"," \nYet,","when","we","can","entreat","an","hour","to","serve,"," \nWe","would","spend","it","in","some","words","upon","that","business,"," \nIf","you","would","grant","the","time."," \nBANQUO"," \nAt","your","kind'st","leisure."," \nMACBETH"," \nIf","you","shall","cleave","to","my","consent,","when","'tis,"," \nIt","shall","make","honour","for","you."," \nBANQUO"," \nSo","I","lose","none"," \nIn","seeking","to","augment","it,","but","still","keep"," \nMy","bosom","franchised","and","allegiance","clear,"," \nI","shall","be","counsell'd."," \nMACBETH"," \nGood","repose","the","while!"," \nBANQUO"," \nThanks,","sir:","the","like","to","you!"," \nExeunt","BANQUO","and","FLEANCE"," \nMACBETH"," \nGo","bid","thy","mistress,","when","my","drink","is","ready,"," \nShe","strike","upon","the","bell.","Get","thee","to","bed."," \nExit","Servant"," \nIs","this","a","dagger","which","I","see","before","me,"," \nThe","handle","toward","my","hand?","Come,","let","me","clutch","thee."," \nI","have","thee","not,","and","yet","I","see","thee","still."," \nArt","thou","not,","fatal","vision,","sensible"," \nTo","feeling","as","to","sight?","or","art","thou","but"," \nA","dagger","of","the","mind,","a","false","creation,"," \nProceeding","from","the","heat-oppressed","brain?"," \nI","see","thee","yet,","in","form","as","palpable"," \nAs","this","which","now","I","draw."," \nThou","marshall'st","me","the","way","that","I","was","going;"," \nAnd","such","an","instrument","I","was","to","use."," \nMine","eyes","are","made","the","fools","o'","the","other","senses,"," \nOr","else","worth","all","the","rest;","I","see","thee","still,"," \nAnd","on","thy","blade","and","dudgeon","gouts","of","blood,"," \nWhich","was","not","so","before.","There's","no","such","thing:"," \nIt","is","the","bloody","business","which","informs"," \nThus","to","mine","eyes.","Now","o'er","the","one","halfworld"," \nNature","seems","dead,","and","wicked","dreams","abuse"," \nThe","curtain'd","sleep;","witchcraft","celebrates"," \nPale","Hecate's","offerings,","and","wither'd","murder,"," \nAlarum'd","by","his","sentinel,","the","wolf,"," \nWhose","howl's","his","watch,","thus","with","his","stealthy","pace."," \nWith","Tarquin's","ravishing","strides,","towards","his","design"," \nMoves","like","a","ghost.","Thou","sure","and","firm-set","earth,"," \nHear","not","my","steps,","which","way","they","walk,","for","fear"," \nThy","very","stones","prate","of","my","whereabout,"," \nAnd","take","the","present","horror","from","the","time,"," \nWhich","now","suits","with","it.","Whiles","I","threat,","he","lives:"," \nWords","to","the","heat","of","deeds","too","cold","breath","gives."," \nA","bell","rings"," \nI","go,","and","it","is","done;","the","bell","invites","me."," \nHear","it","not,","Duncan;","for","it","is","a","knell"," \nThat","summons","thee","to","heaven","or","to","hell.\n"],["ACT","II,","SCENE","II.","The","same."," \nEnter","LADY","MACBETH"," \nLADY","MACBETH"," \nThat","which","hath","made","them","drunk","hath","made","me","bold;"," \nWhat","hath","quench'd","them","hath","given","me","fire."," \nHark!","Peace!"," \nIt","was","the","owl","that","shriek'd,","the","fatal","bellman,"," \nWhich","gives","the","stern'st","good-night.","He","is","about","it:"," \nThe","doors","are","open;","and","the","surfeited","grooms"," \nDo","mock","their","charge","with","snores:","I","have","drugg'd"," \ntheir","possets,"," \nThat","death","and","nature","do","contend","about","them,"," \nWhether","they","live","or","die."," \nMACBETH"," \n[Within]","Who's","there?","what,","ho!"," \nLADY","MACBETH"," \nAlack,","I","am","afraid","they","have","awaked,"," \nAnd","'tis","not","done.","The","attempt","and","not","the","deed"," \nConfounds","us.","Hark!","I","laid","their","daggers","ready;"," \nHe","could","not","miss","'em.","Had","he","not","resembled"," \nMy","father","as","he","slept,","I","had","done't."," \nEnter","MACBETH"," \nMy","husband!"," \nMACBETH"," \nI","have","done","the","deed.","Didst","thou","not","hear","a","noise?"," \nLADY","MACBETH"," \nI","heard","the","owl","scream","and","the","crickets","cry."," \nDid","not","you","speak?"," \nMACBETH"," \nWhen?"," \nLADY","MACBETH"," \nNow."," \nMACBETH"," \nAs","I","descended?"," \nLADY","MACBETH"," \nAy."," \nMACBETH"," \nHark!"," \nWho","lies","i'","the","second","chamber?"," \nLADY","MACBETH"," \nDonalbain."," \nMACBETH"," \nThis","is","a","sorry","sight."," \nLooking","on","his","hands"," \nLADY","MACBETH"," \nA","foolish","thought,","to","say","a","sorry","sight."," \nMACBETH"," \nThere's","one","did","laugh","in's","sleep,","and","one","cried"," \n'Murder!'"," \nThat","they","did","wake","each","other:","I","stood","and","heard","them:"," \nBut","they","did","say","their","prayers,","and","address'd","them"," \nAgain","to","sleep."," \nLADY","MACBETH"," \nThere","are","two","lodged","together."," \nMACBETH"," \nOne","cried","'God","bless","us!'","and","'Amen'","the","other;"," \nAs","they","had","seen","me","with","these","hangman's","hands."," \nListening","their","fear,","I","could","not","say","'Amen,'"," \nWhen","they","did","say","'God","bless","us!'"," \nLADY","MACBETH"," \nConsider","it","not","so","deeply."," \nMACBETH"," \nBut","wherefore","could","not","I","pronounce","'Amen'?"," \nI","had","most","need","of","blessing,","and","'Amen'"," \nStuck","in","my","throat."," \nLADY","MACBETH"," \nThese","deeds","must","not","be","thought"," \nAfter","these","ways;","so,","it","will","make","us","mad."," \nMACBETH"," \nMethought","I","heard","a","voice","cry","'Sleep","no","more!"," \nMacbeth","does","murder","sleep',","the","innocent","sleep,"," \nSleep","that","knits","up","the","ravell'd","sleeve","of","care,"," \nThe","death","of","each","day's","life,","sore","labour's","bath,"," \nBalm","of","hurt","minds,","great","nature's","second","course,"," \nChief","nourisher","in","life's","feast,--"," \nLADY","MACBETH"," \nWhat","do","you","mean?"," \nMACBETH"," \nStill","it","cried","'Sleep","no","more!'","to","all","the","house:"," \n'Glamis","hath","murder'd","sleep,","and","therefore","Cawdor"," \nShall","sleep","no","more;","Macbeth","shall","sleep","no","more.'"," \nLADY","MACBETH"," \nWho","was","it","that","thus","cried?","Why,","worthy","thane,"," \nYou","do","unbend","your","noble","strength,","to","think"," \nSo","brainsickly","of","things.","Go","get","some","water,"," \nAnd","wash","this","filthy","witness","from","your","hand."," \nWhy","did","you","bring","these","daggers","from","the","place?"," \nThey","must","lie","there:","go","carry","them;","and","smear"," \nThe","sleepy","grooms","with","blood."," \nMACBETH"," \nI'll","go","no","more:"," \nI","am","afraid","to","think","what","I","have","done;"," \nLook","on't","again","I","dare","not."," \nLADY","MACBETH"," \nInfirm","of","purpose!"," \nGive","me","the","daggers:","the","sleeping","and","the","dead"," \nAre","but","as","pictures:","'tis","the","eye","of","childhood"," \nThat","fears","a","painted","devil.","If","he","do","bleed,"," \nI'll","gild","the","faces","of","the","grooms","withal;"," \nFor","it","must","seem","their","guilt."," \nExit.","Knocking","within"," \nMACBETH"," \nWhence","is","that","knocking?"," \nHow","is't","with","me,","when","every","noise","appals","me?"," \nWhat","hands","are","here?","ha!","they","pluck","out","mine","eyes."," \nWill","all","great","Neptune's","ocean","wash","this","blood"," \nClean","from","my","hand?","No,","this","my","hand","will","rather"," \nThe","multitudinous","seas","in","incarnadine,"," \nMaking","the","green","one","red."," \nRe-enter","LADY","MACBETH"," \nLADY","MACBETH"," \nMy","hands","are","of","your","colour;","but","I","shame"," \nTo","wear","a","heart","so","white."," \nKnocking","within"," \nI","hear","a","knocking"," \nAt","the","south","entry:","retire","we","to","our","chamber;"," \nA","little","water","clears","us","of","this","deed:"," \nHow","easy","is","it,","then!","Your","constancy"," \nHath","left","you","unattended."," \nKnocking","within"," \nHark!","more","knocking."," \nGet","on","your","nightgown,","lest","occasion","call","us,"," \nAnd","show","us","to","be","watchers.","Be","not","lost"," \nSo","poorly","in","your","thoughts."," \nMACBETH"," \nTo","know","my","deed,","'twere","best","not","know","myself."," \nKnocking","within"," \nWake","Duncan","with","thy","knocking!","I","would","thou","couldst!\n"],["ACT","III,","SCENE","II.","The","palace."," \nEnter","LADY","MACBETH","and","a","Servant"," \nLADY","MACBETH"," \nIs","Banquo","gone","from","court?"," \nServant"," \nAy,","madam,","but","returns","again","to-night."," \nLADY","MACBETH"," \nSay","to","the","king,","I","would","attend","his","leisure"," \nFor","a","few","words."," \nServant"," \nMadam,","I","will."," \nExit"," \nLADY","MACBETH"," \nNought's","had,","all's","spent,"," \nWhere","our","desire","is","got","without","content:"," \n'Tis","safer","to","be","that","which","we","destroy"," \nThan","by","destruction","dwell","in","doubtful","joy."," \nEnter","MACBETH"," \nHow","now,","my","lord!","why","do","you","keep","alone,"," \nOf","sorriest","fancies","your","companions","making,"," \nUsing","those","thoughts","which","should","indeed","have","died"," \nWith","them","they","think","on?","Things","without","all","remedy"," \nShould","be","without","regard:","what's","done","is","done."," \nMACBETH"," \nWe","have","scotch'd","the","snake,","not","kill'd","it:"," \nShe'll","close","and","be","herself,","whilst","our","poor","malice"," \nRemains","in","danger","of","her","former","tooth."," \nBut","let","the","frame","of","things","disjoint,","both","the"," \nworlds","suffer,"," \nEre","we","will","eat","our","meal","in","fear","and","sleep"," \nIn","the","affliction","of","these","terrible","dreams"," \nThat","shake","us","nightly:","better","be","with","the","dead,"," \nWhom","we,","to","gain","our","peace,","have","sent","to","peace,"," \nThan","on","the","torture","of","the","mind","to","lie"," \nIn","restless","ecstasy.","Duncan","is","in","his","grave;"," \nAfter","life's","fitful","fever","he","sleeps","well;"," \nTreason","has","done","his","worst:","nor","steel,","nor","poison,"," \nMalice","domestic,","foreign","levy,","nothing,"," \nCan","touch","him","further."," \nLADY","MACBETH"," \nCome","on;"," \nGentle","my","lord,","sleek","o'er","your","rugged","looks;"," \nBe","bright","and","jovial","among","your","guests","to-night."," \nMACBETH"," \nSo","shall","I,","love;","and","so,","I","pray,","be","you:"," \nLet","your","remembrance","apply","to","Banquo;"," \nPresent","him","eminence,","both","with","eye","and","tongue:"," \nUnsafe","the","while,","that","we"," \nMust","lave","our","honours","in","these","flattering","streams,"," \nAnd","make","our","faces","vizards","to","our","hearts,"," \nDisguising","what","they","are."," \nLADY","MACBETH"," \nYou","must","leave","this."," \nMACBETH"," \nO,","full","of","scorpions","is","my","mind,","dear","wife!"," \nThou","know'st","that","Banquo,","and","his","Fleance,","lives."," \nLADY","MACBETH"," \nBut","in","them","nature's","copy's","not","eterne."," \nMACBETH"," \nThere's","comfort","yet;","they","are","assailable;"," \nThen","be","thou","jocund:","ere","the","bat","hath","flown"," \nHis","cloister'd","flight,","ere","to","black","Hecate's","summons"," \nThe","shard-borne","beetle","with","his","drowsy","hums"," \nHath","rung","night's","yawning","peal,","there","shall","be","done"," \nA","deed","of","dreadful","note."," \nLADY","MACBETH"," \nWhat's","to","be","done?"," \nMACBETH"," \nBe","innocent","of","the","knowledge,","dearest","chuck,"," \nTill","thou","applaud","the","deed.","Come,","seeling","night,"," \nScarf","up","the","tender","eye","of","pitiful","day;"," \nAnd","with","thy","bloody","and","invisible","hand"," \nCancel","and","tear","to","pieces","that","great","bond"," \nWhich","keeps","me","pale!","Light","thickens;","and","the","crow"," \nMakes","wing","to","the","rooky","wood:"," \nGood","things","of","day","begin","to","droop","and","drowse;"," \nWhile","night's","black","agents","to","their","preys","do","rouse."," \nThou","marvell'st","at","my","words:","but","hold","thee","still;"," \nThings","bad","begun","make","strong","themselves","by","ill."," \nSo,","prithee,","go","with","me.\n"],["ACT","III,","SCENE","IV.","The","same.","Hall","in","the","palace."," \nA","banquet","prepared.","Enter","MACBETH,","LADY","MACBETH,","ROSS,","LENNOX,","Lords,","and","Attendants"," \nMACBETH"," \nYou","know","your","own","degrees;","sit","down:","at","first"," \nAnd","last","the","hearty","welcome."," \nLords"," \nThanks","to","your","majesty."," \nMACBETH"," \nOurself","will","mingle","with","society,"," \nAnd","play","the","humble","host."," \nOur","hostess","keeps","her","state,","but","in","best","time"," \nWe","will","require","her","welcome."," \nLADY","MACBETH"," \nPronounce","it","for","me,","sir,","to","all","our","friends;"," \nFor","my","heart","speaks","they","are","welcome."," \nFirst","Murderer","appears","at","the","door"," \nMACBETH"," \nSee,","they","encounter","thee","with","their","hearts'","thanks."," \nBoth","sides","are","even:","here","I'll","sit","i'","the","midst:"," \nBe","large","in","mirth;","anon","we'll","drink","a","measure"," \nThe","table","round."," \nApproaching","the","door"," \nThere's","blood","on","thy","face."," \nFirst","Murderer"," \n'Tis","Banquo's","then."," \nMACBETH"," \n'Tis","better","thee","without","than","he","within."," \nIs","he","dispatch'd?"," \nFirst","Murderer"," \nMy","lord,","his","throat","is","cut;","that","I","did","for","him."," \nMACBETH"," \nThou","art","the","best","o'","the","cut-throats:","yet","he's","good"," \nThat","did","the","like","for","Fleance:","if","thou","didst","it,"," \nThou","art","the","nonpareil."," \nFirst","Murderer"," \nMost","royal","sir,"," \nFleance","is","'scaped."," \nMACBETH"," \nThen","comes","my","fit","again:","I","had","else","been","perfect,"," \nWhole","as","the","marble,","founded","as","the","rock,"," \nAs","broad","and","general","as","the","casing","air:"," \nBut","now","I","am","cabin'd,","cribb'd,","confined,","bound","in"," \nTo","saucy","doubts","and","fears.","But","Banquo's","safe?"," \nFirst","Murderer"," \nAy,","my","good","lord:","safe","in","a","ditch","he","bides,"," \nWith","twenty","trenched","gashes","on","his","head;"," \nThe","least","a","death","to","nature."," \nMACBETH"," \nThanks","for","that:"," \nThere","the","grown","serpent","lies;","the","worm","that's","fled"," \nHath","nature","that","in","time","will","venom","breed,"," \nNo","teeth","for","the","present.","Get","thee","gone:","to-morrow"," \nWe'll","hear,","ourselves,","again."," \nExit","Murderer"," \nLADY","MACBETH"," \nMy","royal","lord,"," \nYou","do","not","give","the","cheer:","the","feast","is","sold"," \nThat","is","not","often","vouch'd,","while","'tis","a-making,"," \n'Tis","given","with","welcome:","to","feed","were","best","at","home;"," \nFrom","thence","the","sauce","to","meat","is","ceremony;"," \nMeeting","were","bare","without","it."," \nMACBETH"," \nSweet","remembrancer!"," \nNow,","good","digestion","wait","on","appetite,"," \nAnd","health","on","both!"," \nLENNOX"," \nMay't","please","your","highness","sit."," \nThe","GHOST","OF","BANQUO","enters,","and","sits","in","MACBETH's","place"," \nMACBETH"," \nHere","had","we","now","our","country's","honour","roof'd,"," \nWere","the","graced","person","of","our","Banquo","present;"," \nWho","may","I","rather","challenge","for","unkindness"," \nThan","pity","for","mischance!"," \nROSS"," \nHis","absence,","sir,"," \nLays","blame","upon","his","promise.","Please't","your","highness"," \nTo","grace","us","with","your","royal","company."," \nMACBETH"," \nThe","table's","full."," \nLENNOX"," \nHere","is","a","place","reserved,","sir."," \nMACBETH"," \nWhere?"," \nLENNOX"," \nHere,","my","good","lord.","What","is't","that","moves","your","highness?"," \nMACBETH"," \nWhich","of","you","have","done","this?"," \nLords"," \nWhat,","my","good","lord?"," \nMACBETH"," \nThou","canst","not","say","I","did","it:","never","shake"," \nThy","gory","locks","at","me."," \nROSS"," \nGentlemen,","rise:","his","highness","is","not","well."," \nLADY","MACBETH"," \nSit,","worthy","friends:","my","lord","is","often","thus,"," \nAnd","hath","been","from","his","youth:","pray","you,","keep","seat;"," \nThe","fit","is","momentary;","upon","a","thought"," \nHe","will","again","be","well:","if","much","you","note","him,"," \nYou","shall","offend","him","and","extend","his","passion:"," \nFeed,","and","regard","him","not.","Are","you","a","man?"," \nMACBETH"," \nAy,","and","a","bold","one,","that","dare","look","on","that"," \nWhich","might","appal","the","devil."," \nLADY","MACBETH"," \nO","proper","stuff!"," \nThis","is","the","very","painting","of","your","fear:"," \nThis","is","the","air-drawn","dagger","which,","you","said,"," \nLed","you","to","Duncan.","O,","these","flaws","and","starts,"," \nImpostors","to","true","fear,","would","well","become"," \nA","woman's","story","at","a","winter's","fire,"," \nAuthorized","by","her","grandam.","Shame","itself!"," \nWhy","do","you","make","such","faces?","When","all's","done,"," \nYou","look","but","on","a","stool."," \nMACBETH"," \nPrithee,","see","there!","behold!","look!","lo!"," \nhow","say","you?"," \nWhy,","what","care","I?","If","thou","canst","nod,","speak","too."," \nIf","charnel-houses","and","our","graves","must","send"," \nThose","that","we","bury","back,","our","monuments"," \nShall","be","the","maws","of","kites."," \nGHOST","OF","BANQUO","vanishes"," \nLADY","MACBETH"," \nWhat,","quite","unmann'd","in","folly?"," \nMACBETH"," \nIf","I","stand","here,","I","saw","him."," \nLADY","MACBETH"," \nFie,","for","shame!"," \nMACBETH"," \nBlood","hath","been","shed","ere","now,","i'","the","olden","time,"," \nEre","human","statute","purged","the","gentle","weal;"," \nAy,","and","since","too,","murders","have","been","perform'd"," \nToo","terrible","for","the","ear:","the","times","have","been,"," \nThat,","when","the","brains","were","out,","the","man","would","die,"," \nAnd","there","an","end;","but","now","they","rise","again,"," \nWith","twenty","mortal","murders","on","their","crowns,"," \nAnd","push","us","from","our","stools:","this","is","more","strange"," \nThan","such","a","murder","is."," \nLADY","MACBETH"," \nMy","worthy","lord,"," \nYour","noble","friends","do","lack","you."," \nMACBETH"," \nI","do","forget."," \nDo","not","muse","at","me,","my","most","worthy","friends,"," \nI","have","a","strange","infirmity,","which","is","nothing"," \nTo","those","that","know","me.","Come,","love","and","health","to","all;"," \nThen","I'll","sit","down.","Give","me","some","wine;","fill","full."," \nI","drink","to","the","general","joy","o'","the","whole","table,"," \nAnd","to","our","dear","friend","Banquo,","whom","we","miss;"," \nWould","he","were","here!","to","all,","and","him,","we","thirst,"," \nAnd","all","to","all."," \nLords"," \nOur","duties,","and","the","pledge."," \nRe-enter","GHOST","OF","BANQUO"," \nMACBETH"," \nAvaunt!","and","quit","my","sight!","let","the","earth","hide","thee!"," \nThy","bones","are","marrowless,","thy","blood","is","cold;"," \nThou","hast","no","speculation","in","those","eyes"," \nWhich","thou","dost","glare","with!"," \nLADY","MACBETH"," \nThink","of","this,","good","peers,"," \nBut","as","a","thing","of","custom:","'tis","no","other;"," \nOnly","it","spoils","the","pleasure","of","the","time."," \nMACBETH"," \nWhat","man","dare,","I","dare:"," \nApproach","thou","like","the","rugged","Russian","bear,"," \nThe","arm'd","rhinoceros,","or","the","Hyrcan","tiger;"," \nTake","any","shape","but","that,","and","my","firm","nerves"," \nShall","never","tremble:","or","be","alive","again,"," \nAnd","dare","me","to","the","desert","with","thy","sword;"," \nIf","trembling","I","inhabit","then,","protest","me"," \nThe","baby","of","a","girl.","Hence,","horrible","shadow!"," \nUnreal","mockery,","hence!"," \nGHOST","OF","BANQUO","vanishes"," \nWhy,","so:","being","gone,"," \nI","am","a","man","again.","Pray","you,","sit","still."," \nLADY","MACBETH"," \nYou","have","displaced","the","mirth,","broke","the","good","meeting,"," \nWith","most","admired","disorder."," \nMACBETH"," \nCan","such","things","be,"," \nAnd","overcome","us","like","a","summer's","cloud,"," \nWithout","our","special","wonder?","You","make","me","strange"," \nEven","to","the","disposition","that","I","owe,"," \nWhen","now","I","think","you","can","behold","such","sights,"," \nAnd","keep","the","natural","ruby","of","your","cheeks,"," \nWhen","mine","is","blanched","with","fear."," \nROSS"," \nWhat","sights,","my","lord?"," \nLADY","MACBETH"," \nI","pray","you,","speak","not;","he","grows","worse","and","worse;"," \nQuestion","enrages","him.","At","once,","good","night:"," \nStand","not","upon","the","order","of","your","going,"," \nBut","go","at","once."," \nLENNOX"," \nGood","night;","and","better","health"," \nAttend","his","majesty!"," \nLADY","MACBETH"," \nA","kind","good","night","to","all!"," \nExeunt","all","but","MACBETH","and","LADY","MACBETH"," \nMACBETH"," \nIt","will","have","blood;","they","say,","blood","will","have","blood:"," \nStones","have","been","known","to","move","and","trees","to","speak;"," \nAugurs","and","understood","relations","have"," \nBy","magot-pies","and","choughs","and","rooks","brought","forth"," \nThe","secret'st","man","of","blood.","What","is","the","night?"," \nLADY","MACBETH"," \nAlmost","at","odds","with","morning,","which","is","which."," \nMACBETH"," \nHow","say'st","thou,","that","Macduff","denies","his","person"," \nAt","our","great","bidding?"," \nLADY","MACBETH"," \nDid","you","send","to","him,","sir?"," \nMACBETH"," \nI","hear","it","by","the","way;","but","I","will","send:"," \nThere's","not","a","one","of","them","but","in","his","house"," \nI","keep","a","servant","fee'd.","I","will","to-morrow,"," \nAnd","betimes","I","will,","to","the","weird","sisters:"," \nMore","shall","they","speak;","for","now","I","am","bent","to","know,"," \nBy","the","worst","means,","the","worst.","For","mine","own","good,"," \nAll","causes","shall","give","way:","I","am","in","blood"," \nStepp'd","in","so","far","that,","should","I","wade","no","more,"," \nReturning","were","as","tedious","as","go","o'er:"," \nStrange","things","I","have","in","head,","that","will","to","hand;"," \nWhich","must","be","acted","ere","they","may","be","scann'd."," \nLADY","MACBETH"," \nYou","lack","the","season","of","all","natures,","sleep."," \nMACBETH"," \nCome,","we'll","to","sleep.","My","strange","and","self-abuse"," \nIs","the","initiate","fear","that","wants","hard","use:"," \nWe","are","yet","but","young","in","deed.\n"],["ACT","IV,","SCENE","I.","A","cavern.","In","the","middle,","a","boiling","cauldron."," \nThunder.","Enter","the","three","Witches"," \nFirst","Witch"," \nThrice","the","brinded","cat","hath","mew'd."," \nSecond","Witch"," \nThrice","and","once","the","hedge-pig","whined."," \nThird","Witch"," \nHarpier","cries","'Tis","time,","'tis","time."," \nFirst","Witch"," \nRound","about","the","cauldron","go;"," \nIn","the","poison'd","entrails","throw."," \nToad,","that","under","cold","stone"," \nDays","and","nights","has","thirty-one"," \nSwelter'd","venom","sleeping","got,"," \nBoil","thou","first","i'","the","charmed","pot."," \nALL"," \nDouble,","double","toil","and","trouble;"," \nFire","burn,","and","cauldron","bubble."," \nSecond","Witch"," \nFillet","of","a","fenny","snake,"," \nIn","the","cauldron","boil","and","bake;"," \nEye","of","newt","and","toe","of","frog,"," \nWool","of","bat","and","tongue","of","dog,"," \nAdder's","fork","and","blind-worm's","sting,"," \nLizard's","leg","and","owlet's","wing,"," \nFor","a","charm","of","powerful","trouble,"," \nLike","a","hell-broth","boil","and","bubble."," \nALL"," \nDouble,","double","toil","and","trouble;"," \nFire","burn","and","cauldron","bubble."," \nThird","Witch"," \nScale","of","dragon,","tooth","of","wolf,"," \nWitches'","mummy,","maw","and","gulf"," \nOf","the","ravin'd","salt-sea","shark,"," \nRoot","of","hemlock","digg'd","i'","the","dark,"," \nLiver","of","blaspheming","Jew,"," \nGall","of","goat,","and","slips","of","yew"," \nSilver'd","in","the","moon's","eclipse,"," \nNose","of","Turk","and","Tartar's","lips,"," \nFinger","of","birth-strangled","babe"," \nDitch-deliver'd","by","a","drab,"," \nMake","the","gruel","thick","and","slab:"," \nAdd","thereto","a","tiger's","chaudron,"," \nFor","the","ingredients","of","our","cauldron."," \nALL"," \nDouble,","double","toil","and","trouble;"," \nFire","burn","and","cauldron","bubble."," \nSecond","Witch"," \nCool","it","with","a","baboon's","blood,"," \nThen","the","charm","is","firm","and","good."," \nEnter","HECATE","to","the","other","three","Witches"," \nHECATE"," \nO","well","done!","I","commend","your","pains;"," \nAnd","every","one","shall","share","i'","the","gains;"," \nAnd","now","about","the","cauldron","sing,"," \nLive","elves","and","fairies","in","a","ring,"," \nEnchanting","all","that","you","put","in."," \nMusic","and","a","song:","'Black","spirits,'","&","c"," \nHECATE","retires"," \nSecond","Witch"," \nBy","the","pricking","of","my","thumbs,"," \nSomething","wicked","this","way","comes."," \nOpen,","locks,"," \nWhoever","knocks!"," \nEnter","MACBETH"," \nMACBETH"," \nHow","now,","you","secret,","black,","and","midnight","hags!"," \nWhat","is't","you","do?"," \nALL"," \nA","deed","without","a","name."," \nMACBETH"," \nI","conjure","you,","by","that","which","you","profess,"," \nHowe'er","you","come","to","know","it,","answer","me:"," \nThough","you","untie","the","winds","and","let","them","fight"," \nAgainst","the","churches;","though","the","yesty","waves"," \nConfound","and","swallow","navigation","up;"," \nThough","bladed","corn","be","lodged","and","trees","blown","down;"," \nThough","castles","topple","on","their","warders'","heads;"," \nThough","palaces","and","pyramids","do","slope"," \nTheir","heads","to","their","foundations;","though","the","treasure"," \nOf","nature's","germens","tumble","all","together,"," \nEven","till","destruction","sicken;","answer","me"," \nTo","what","I","ask","you."," \nFirst","Witch"," \nSpeak."," \nSecond","Witch"," \nDemand."," \nThird","Witch"," \nWe'll","answer."," \nFirst","Witch"," \nSay,","if","thou'dst","rather","hear","it","from","our","mouths,"," \nOr","from","our","masters?"," \nMACBETH"," \nCall","'em;","let","me","see","'em."," \nFirst","Witch"," \nPour","in","sow's","blood,","that","hath","eaten"," \nHer","nine","farrow;","grease","that's","sweaten"," \nFrom","the","murderer's","gibbet","throw"," \nInto","the","flame."," \nALL"," \nCome,","high","or","low;"," \nThyself","and","office","deftly","show!"," \nThunder.","First","Apparition:","an","armed","Head"," \nMACBETH"," \nTell","me,","thou","unknown","power,--"," \nFirst","Witch"," \nHe","knows","thy","thought:"," \nHear","his","speech,","but","say","thou","nought."," \nFirst","Apparition"," \nMacbeth!","Macbeth!","Macbeth!","beware","Macduff;"," \nBeware","the","thane","of","Fife.","Dismiss","me.","Enough."," \nDescends"," \nMACBETH"," \nWhate'er","thou","art,","for","thy","good","caution,","thanks;"," \nThou","hast","harp'd","my","fear","aright:","but","one"," \nword","more,--"," \nFirst","Witch"," \nHe","will","not","be","commanded:","here's","another,"," \nMore","potent","than","the","first."," \nThunder.","Second","Apparition:","A","bloody","Child"," \nSecond","Apparition"," \nMacbeth!","Macbeth!","Macbeth!"," \nMACBETH"," \nHad","I","three","ears,","I'ld","hear","thee."," \nSecond","Apparition"," \nBe","bloody,","bold,","and","resolute;","laugh","to","scorn"," \nThe","power","of","man,","for","none","of","woman","born"," \nShall","harm","Macbeth."," \nDescends"," \nMACBETH"," \nThen","live,","Macduff:","what","need","I","fear","of","thee?"," \nBut","yet","I'll","make","assurance","double","sure,"," \nAnd","take","a","bond","of","fate:","thou","shalt","not","live;"," \nThat","I","may","tell","pale-hearted","fear","it","lies,"," \nAnd","sleep","in","spite","of","thunder."," \nThunder.","Third","Apparition:","a","Child","crowned,","with","a","tree","in","his","hand"," \nWhat","is","this"," \nThat","rises","like","the","issue","of","a","king,"," \nAnd","wears","upon","his","baby-brow","the","round"," \nAnd","top","of","sovereignty?"," \nALL"," \nListen,","but","speak","not","to't."," \nThird","Apparition"," \nBe","lion-mettled,","proud;","and","take","no","care"," \nWho","chafes,","who","frets,","or","where","conspirers","are:"," \nMacbeth","shall","never","vanquish'd","be","until"," \nGreat","Birnam","wood","to","high","Dunsinane","hill"," \nShall","come","against","him."," \nDescends"," \nMACBETH"," \nThat","will","never","be"," \nWho","can","impress","the","forest,","bid","the","tree"," \nUnfix","his","earth-bound","root?","Sweet","bodements!","good!"," \nRebellion's","head,","rise","never","till","the","wood"," \nOf","Birnam","rise,","and","our","high-placed","Macbeth"," \nShall","live","the","lease","of","nature,","pay","his","breath"," \nTo","time","and","mortal","custom.","Yet","my","heart"," \nThrobs","to","know","one","thing:","tell","me,","if","your","art"," \nCan","tell","so","much:","shall","Banquo's","issue","ever"," \nReign","in","this","kingdom?"," \nALL"," \nSeek","to","know","no","more."," \nMACBETH"," \nI","will","be","satisfied:","deny","me","this,"," \nAnd","an","eternal","curse","fall","on","you!","Let","me","know."," \nWhy","sinks","that","cauldron?","and","what","noise","is","this?"," \nHautboys"," \nFirst","Witch"," \nShow!"," \nSecond","Witch"," \nShow!"," \nThird","Witch"," \nShow!"," \nALL"," \nShow","his","eyes,","and","grieve","his","heart;"," \nCome","like","shadows,","so","depart!"," \nA","show","of","Eight","Kings,","the","last","with","a","glass","in","his","hand;","GHOST","OF","BANQUO","following"," \nMACBETH"," \nThou","art","too","like","the","spirit","of","Banquo:","down!"," \nThy","crown","does","sear","mine","eye-balls.","And","thy","hair,"," \nThou","other","gold-bound","brow,","is","like","the","first."," \nA","third","is","like","the","former.","Filthy","hags!"," \nWhy","do","you","show","me","this?","A","fourth!","Start,","eyes!"," \nWhat,","will","the","line","stretch","out","to","the","crack","of","doom?"," \nAnother","yet!","A","seventh!","I'll","see","no","more:"," \nAnd","yet","the","eighth","appears,","who","bears","a","glass"," \nWhich","shows","me","many","more;","and","some","I","see"," \nThat","two-fold","balls","and","treble","scepters","carry:"," \nHorrible","sight!","Now,","I","see,","'tis","true;"," \nFor","the","blood-bolter'd","Banquo","smiles","upon","me,"," \nAnd","points","at","them","for","his."," \nApparitions","vanish"," \nWhat,","is","this","so?"," \nFirst","Witch"," \nAy,","sir,","all","this","is","so:","but","why"," \nStands","Macbeth","thus","amazedly?"," \nCome,","sisters,","cheer","we","up","his","sprites,"," \nAnd","show","the","best","of","our","delights:"," \nI'll","charm","the","air","to","give","a","sound,"," \nWhile","you","perform","your","antic","round:"," \nThat","this","great","king","may","kindly","say,"," \nOur","duties","did","his","welcome","pay."," \nMusic.","The","witches","dance","and","then","vanish,","with","HECATE"," \nMACBETH"," \nWhere","are","they?","Gone?","Let","this","pernicious","hour"," \nStand","aye","accursed","in","the","calendar!"," \nCome","in,","without","there!"," \nEnter","LENNOX"," \nLENNOX"," \nWhat's","your","grace's","will?"," \nMACBETH"," \nSaw","you","the","weird","sisters?"," \nLENNOX"," \nNo,","my","lord."," \nMACBETH"," \nCame","they","not","by","you?"," \nLENNOX"," \nNo,","indeed,","my","lord."," \nMACBETH"," \nInfected","be","the","air","whereon","they","ride;"," \nAnd","damn'd","all","those","that","trust","them!","I","did","hear"," \nThe","galloping","of","horse:","who","was't","came","by?"," \nLENNOX"," \n'Tis","two","or","three,","my","lord,","that","bring","you","word"," \nMacduff","is","fled","to","England."," \nMACBETH"," \nFled","to","England!"," \nLENNOX"," \nAy,","my","good","lord."," \nMACBETH"," \nTime,","thou","anticipatest","my","dread","exploits:"," \nThe","flighty","purpose","never","is","o'ertook"," \nUnless","the","deed","go","with","it;","from","this","moment"," \nThe","very","firstlings","of","my","heart","shall","be"," \nThe","firstlings","of","my","hand.","And","even","now,"," \nTo","crown","my","thoughts","with","acts,","be","it","thought","and","done:"," \nThe","castle","of","Macduff","I","will","surprise;"," \nSeize","upon","Fife;","give","to","the","edge","o'","the","sword"," \nHis","wife,","his","babes,","and","all","unfortunate","souls"," \nThat","trace","him","in","his","line.","No","boasting","like","a","fool;"," \nThis","deed","I'll","do","before","this","purpose","cool."," \nBut","no","more","sights!--Where","are","these","gentlemen?"," \nCome,","bring","me","where","they","are.\n"],["ACT","V,","SCENE","I.","Dunsinane.","Ante-room","in","the","castle."," \nEnter","a","Doctor","of","Physic","and","a","Waiting-Gentlewoman"," \nDoctor"," \nI","have","two","nights","watched","with","you,","but","can","perceive"," \nno","truth","in","your","report.","When","was","it","she","last","walked?"," \nGentlewoman"," \nSince","his","majesty","went","into","the","field,","I","have","seen"," \nher","rise","from","her","bed,","throw","her","night-gown","upon"," \nher,","unlock","her","closet,","take","forth","paper,","fold","it,"," \nwrite","upon't,","read","it,","afterwards","seal","it,","and","again"," \nreturn","to","bed;","yet","all","this","while","in","a","most","fast","sleep."," \nDoctor"," \nA","great","perturbation","in","nature,","to","receive","at","once"," \nthe","benefit","of","sleep,","and","do","the","effects","of"," \nwatching!","In","this","slumbery","agitation,","besides","her"," \nwalking","and","other","actual","performances,","what,","at","any"," \ntime,","have","you","heard","her","say?"," \nGentlewoman"," \nThat,","sir,","which","I","will","not","report","after","her."," \nDoctor"," \nYou","may","to","me:","and","'tis","most","meet","you","should."," \nGentlewoman"," \nNeither","to","you","nor","any","one;","having","no","witness","to"," \nconfirm","my","speech."," \nEnter","LADY","MACBETH,","with","a","taper"," \nLo","you,","here","she","comes!","This","is","her","very","guise;"," \nand,","upon","my","life,","fast","asleep.","Observe","her;","stand","close."," \nDoctor"," \nHow","came","she","by","that","light?"," \nGentlewoman"," \nWhy,","it","stood","by","her:","she","has","light","by","her"," \ncontinually;","'tis","her","command."," \nDoctor"," \nYou","see,","her","eyes","are","open."," \nGentlewoman"," \nAy,","but","their","sense","is","shut."," \nDoctor"," \nWhat","is","it","she","does","now?","Look,","how","she","rubs","her","hands."," \nGentlewoman"," \nIt","is","an","accustomed","action","with","her,","to","seem","thus"," \nwashing","her","hands:","I","have","known","her","continue","in"," \nthis","a","quarter","of","an","hour."," \nLADY","MACBETH"," \nYet","here's","a","spot."," \nDoctor"," \nHark!","she","speaks:","I","will","set","down","what","comes","from"," \nher,","to","satisfy","my","remembrance","the","more","strongly."," \nLADY","MACBETH"," \nOut,","damned","spot!","out,","I","say!--One:","two:","why,"," \nthen,","'tis","time","to","do't.--Hell","is","murky!--Fie,","my"," \nlord,","fie!","a","soldier,","and","afeard?","What","need","we"," \nfear","who","knows","it,","when","none","can","call","our","power","to"," \naccount?--Yet","who","would","have","thought","the","old","man"," \nto","have","had","so","much","blood","in","him."," \nDoctor"," \nDo","you","mark","that?"," \nLADY","MACBETH"," \nThe","thane","of","Fife","had","a","wife:","where","is","she","now?--"," \nWhat,","will","these","hands","ne'er","be","clean?--No","more","o'"," \nthat,","my","lord,","no","more","o'","that:","you","mar","all","with"," \nthis","starting."," \nDoctor"," \nGo","to,","go","to;","you","have","known","what","you","should","not."," \nGentlewoman"," \nShe","has","spoke","what","she","should","not,","I","am","sure","of"," \nthat:","heaven","knows","what","she","has","known."," \nLADY","MACBETH"," \nHere's","the","smell","of","the","blood","still:","all","the"," \nperfumes","of","Arabia","will","not","sweeten","this","little"," \nhand.","Oh,","oh,","oh!"," \nDoctor"," \nWhat","a","sigh","is","there!","The","heart","is","sorely","charged."," \nGentlewoman"," \nI","would","not","have","such","a","heart","in","my","bosom","for","the"," \ndignity","of","the","whole","body."," \nDoctor"," \nWell,","well,","well,--"," \nGentlewoman"," \nPray","God","it","be,","sir."," \nDoctor"," \nThis","disease","is","beyond","my","practise:","yet","I","have","known"," \nthose","which","have","walked","in","their","sleep","who","have","died"," \nholily","in","their","beds."," \nLADY","MACBETH"," \nWash","your","hands,","put","on","your","nightgown;","look","not","so"," \npale.--I","tell","you","yet","again,","Banquo's","buried;","he"," \ncannot","come","out","on's","grave."," \nDoctor"," \nEven","so?"," \nLADY","MACBETH"," \nTo","bed,","to","bed!","there's","knocking","at","the","gate:"," \ncome,","come,","come,","come,","give","me","your","hand.","What's"," \ndone","cannot","be","undone.--To","bed,","to","bed,","to","bed!"," \nExit"," \nDoctor"," \nWill","she","go","now","to","bed?"," \nGentlewoman"," \nDirectly."," \nDoctor"," \nFoul","whisperings","are","abroad:","unnatural","deeds"," \nDo","breed","unnatural","troubles:","infected","minds"," \nTo","their","deaf","pillows","will","discharge","their","secrets:"," \nMore","needs","she","the","divine","than","the","physician."," \nGod,","God","forgive","us","all!","Look","after","her;"," \nRemove","from","her","the","means","of","all","annoyance,"," \nAnd","still","keep","eyes","upon","her.","So,","good","night:"," \nMy","mind","she","has","mated,","and","amazed","my","sight."," \nI","think,","but","dare","not","speak."," \nGentlewoman"," \nGood","night,","good","doctor.\n"],["ACT","V,","SCENE","V.","Dunsinane.","Within","the","castle."," \nEnter","MACBETH,","SEYTON,","and","Soldiers,","with","drum","and","colours"," \nMACBETH"," \nHang","out","our","banners","on","the","outward","walls;"," \nThe","cry","is","still","'They","come:'","our","castle's","strength"," \nWill","laugh","a","siege","to","scorn:","here","let","them","lie"," \nTill","famine","and","the","ague","eat","them","up:"," \nWere","they","not","forced","with","those","that","should","be","ours,"," \nWe","might","have","met","them","dareful,","beard","to","beard,"," \nAnd","beat","them","backward","home."," \nA","cry","of","women","within"," \nWhat","is","that","noise?"," \nSEYTON"," \nIt","is","the","cry","of","women,","my","good","lord."," \nExit"," \nMACBETH"," \nI","have","almost","forgot","the","taste","of","fears;"," \nThe","time","has","been,","my","senses","would","have","cool'd"," \nTo","hear","a","night-shriek;","and","my","fell","of","hair"," \nWould","at","a","dismal","treatise","rouse","and","stir"," \nAs","life","were","in't:","I","have","supp'd","full","with","horrors;"," \nDireness,","familiar","to","my","slaughterous","thoughts"," \nCannot","once","start","me."," \nRe-enter","SEYTON"," \nWherefore","was","that","cry?"," \nSEYTON"," \nThe","queen,","my","lord,","is","dead."," \nMACBETH"," \nShe","should","have","died","hereafter;"," \nThere","would","have","been","a","time","for","such","a","word."," \nTo-morrow,","and","to-morrow,","and","to-morrow,"," \nCreeps","in","this","petty","pace","from","day","to","day"," \nTo","the","last","syllable","of","recorded","time,"," \nAnd","all","our","yesterdays","have","lighted","fools"," \nThe","way","to","dusty","death.","Out,","out,","brief","candle!"," \nLife's","but","a","walking","shadow,","a","poor","player"," \nThat","struts","and","frets","his","hour","upon","the","stage"," \nAnd","then","is","heard","no","more:","it","is","a","tale"," \nTold","by","an","idiot,","full","of","sound","and","fury,"," \nSignifying","nothing."," \nEnter","a","Messenger"," \nThou","comest","to","use","thy","tongue;","thy","story","quickly."," \nMessenger"," \nGracious","my","lord,"," \nI","should","report","that","which","I","say","I","saw,"," \nBut","know","not","how","to","do","it."," \nMACBETH"," \nWell,","say,","sir."," \nMessenger"," \nAs","I","did","stand","my","watch","upon","the","hill,"," \nI","look'd","toward","Birnam,","and","anon,","methought,"," \nThe","wood","began","to","move."," \nMACBETH"," \nLiar","and","slave!"," \nMessenger"," \nLet","me","endure","your","wrath,","if't","be","not","so:"," \nWithin","this","three","mile","may","you","see","it","coming;"," \nI","say,","a","moving","grove."," \nMACBETH"," \nIf","thou","speak'st","false,"," \nUpon","the","next","tree","shalt","thou","hang","alive,"," \nTill","famine","cling","thee:","if","thy","speech","be","sooth,"," \nI","care","not","if","thou","dost","for","me","as","much."," \nI","pull","in","resolution,","and","begin"," \nTo","doubt","the","equivocation","of","the","fiend"," \nThat","lies","like","truth:","'Fear","not,","till","Birnam","wood"," \nDo","come","to","Dunsinane:'","and","now","a","wood"," \nComes","toward","Dunsinane.","Arm,","arm,","and","out!"," \nIf","this","which","he","avouches","does","appear,"," \nThere","is","nor","flying","hence","nor","tarrying","here."," \nI","gin","to","be","aweary","of","the","sun,"," \nAnd","wish","the","estate","o'","the","world","were","now","undone."," \nRing","the","alarum-bell!","Blow,","wind!","come,","wrack!"," \nAt","least","we'll","die","with","harness","on","our","back.\n"],["ACT","V,","SCENE","VI.","Dunsinane.","Before","the","castle."," \nDrum","and","colours.","Enter","MALCOLM,","SIWARD,","MACDUFF,","and","their","Army,","with","boughs"," \nMALCOLM"," \nNow","near","enough:","your","leafy","screens","throw","down."," \nAnd","show","like","those","you","are.","You,","worthy","uncle,"," \nShall,","with","my","cousin,","your","right-noble","son,"," \nLead","our","first","battle:","worthy","Macduff","and","we"," \nShall","take","upon","'s","what","else","remains","to","do,"," \nAccording","to","our","order."," \nSIWARD"," \nFare","you","well."," \nDo","we","but","find","the","tyrant's","power","to-night,"," \nLet","us","be","beaten,","if","we","cannot","fight."," \nMACDUFF"," \nMake","all","our","trumpets","speak;","give","them","all","breath,"," \nThose","clamorous","harbingers","of","blood","and","death.\n"],["I","have","no","spur"," \nTo","prick","the","sides","of","my","intent,","but","only"," \nVaulting","ambition,","which","o’erleaps","itself"," \nAnd","falls","on","th’other","(ACT","I,","SCENC","VII)"," \nThou","wouldst","be","great"," \nArt","not","without","ambition,","but","without"," \nThe","illness","should","attend","it","(ACT","I,","SCENC","V)"," \nThe","Prince","of","Cumberland!","That","is","a","step"," \nOn","which","I","must","fall","down,","or","else","o'erleap,"," \nFor","in","my","way","it","lies.","Stars,","hide","your","fires;"," \nLet","not","light","see","my","black","and","deep","desires."," \nThe","eye","wink","at","the","hand;","yet","let","that","be"," \nWhich","the","eye","fears,","when","it","is","done,","to","see.","(ACT","I,","SCENE","IV)"," \nMy","thought,","whose","murder","yet","is","but","fantastical,"," \nShakes","so","my","single","state","of","man"," \nThat","function","is","smother'd","in","surmise,"," \nand","nothing","is","but","what","is","not.","(ACT","I,","SCENC","III)\n"]]
LEVELS = ["		ACT I, SCENE III    1247\n","		ACT I, SCENE IV    637\n","		ACT II, SCENE I    568\n","		ACT II, SCENE II    686\n","		ACT III, SCENE II    478\n","		ACT III, SCENE IV    1320\n","		ACT IV, SCENE I    1244\n","		ACT V, SCENE I    643\n","		ACT V, SCENE V    460\n","		ACT V, SCENE VI    103\n","		ONLY IMPORTANT QUOTES\n"]

CHARACTER = "▼"
ENEMY = "▲"

INT_VALUES = [100,     35,          25,            20,        15,           5,         5,          0,          0,               0,             100,        100,     0,           0]
STR_VALUES = ["0","0","0","0","0","0","0"]

FIGHT_1V1 = "MACBETH  ENEMY {}\n o           o   \n/|\|       |/|\  \n/ \         / \  \n                 \n".format(INT_VALUES[10])
FIGHT_1V2 = "         ENEMY {}\n             o   \n           |/|\  \nMACBETH     / \  \n o               \n/|\|     ENEMY {}\/ \          o   \n           |/|\  \n            / \  \n".format(INT_VALUES[10],INT_VALUES[11])
FIGHT_2V1 = "MACBETH          \n o               \n/|\|             \n/ \      ENEMY {}\"BANQUO       o   \n o         |/|\  \n/|\|        / \  \n/ \              \n".format(INT_VALUES[10])
FIGHT_2V2 = "MACBETH  ENEMY {}\n o           o   \n/|\|       |/|\  \n/ \         / \  \nBANQUO   ENEMY {}\n o           o   \n/|\|       |/|\  \n/ \         / \  \n".format(INT_VALUES[10],INT_VALUES[11])

MENU = "=============================\n|            |              |\n|{}FIGHT      | HEALTH =  {} |\n|            |              |\n|{}ITEM       |              |\n|            |              |\n|{}FLEE       |              |\n|            |              |\n=============================\n".format(options[0],STR_VALUES[0],options[1],options[2])
FIGHT_MENU = "=============================\n|            |              |\n| FIGHT      |{}STAB         |\n|            | MISS CHANCE =|\n|            | {}           |\n|            | DAMAGE = {}  |\n|            |{}SLASH        |\n|            | MISS CHANCE =|\n|            | {}           |\n|            | DAMAGE = {}  |\n|            |              |\n=============================\n".format(weaponds[0],STR_VALUES[1],STR_VALUES[2],weaponds[1],STR_VALUES[3],STR_VALUES[4])
ITEM_MENU = "=============================\n|            |              |\n| ITEMS      |{}SMALL HEALTH |\n|            | = {}         |\n|            |{}LARGE HEALTH |\n|            | = {}         |\n|            |              |\n=============================\n".format(items[0],STR_VALUES[5],items[1],STR_VALUES[6])
FLEE_MENU = "=============================\n|            |              |\n|>FLEE       | FLEE CAHNCE =|\n|            |              |\n|            | {}           |\n|            |              |\n|            |              |\n=============================\n".format(flee_chance)

clear = lambda: os.system('cls')

def drawFight(fight_type, menu_type):

	if INT_VALUES[7] == 0:

		options = [">", " ", " "]
	
	elif INT_VALUES[7] == 1:

		options = [" ", ">", " "]
	
	elif INT_VALUES[7] == 2:

		options = [" ", " ", ">"]

	if INT_VALUES[8] == 0:
	
		weaponds = [">", " "]
	
	elif INT_VALUES[8] == 1:
	
		weaponds = [" ", ">"]

	if INT_VALUES[9] == 0:
	
		items = [">", " "]
	
	elif INT_VALUES[9] == 1:
	
		items = [" ", ">"]

	for i in range(0,len(INT_VALUES)-7):

		if INT_VALUES[i] >=100:

			STR_VALUES[i] = "\b100"
	
		elif 9 < INT_VALUES[i] < 100:

			STR_VALUES[i] = "{}".format(INT_VALUES[i])
	
		elif INT_VALUES[i] < 10:

			STR_VALUES[i] = " {}".format(INT_VALUES[i])

	clear()

	FIGHT_1V1 = "MACBETH  ENEMY {}\n o           o   \n/|\|       |/|\  \n/ \         / \  \n                 \n".format(INT_VALUES[10])
	MENU = "=============================\n|            |              |\n|{}FIGHT      | HEALTH =  {} |\n|            |              |\n|{}ITEM       |              |\n|            |              |\n|{}FLEE       |              |\n|            |              |\n=============================\n".format(options[0],STR_VALUES[0],options[1],options[2])
	FIGHT_MENU = "=============================\n|            |              |\n| FIGHT      |{}STAB         |\n|            | MISS CHANCE =|\n|            | {}           |\n|            | DAMAGE = {}  |\n|            |{}SLASH        |\n|            | MISS CHANCE =|\n|            | {}           |\n|            | DAMAGE = {}  |\n|            |              |\n=============================\n".format(weaponds[0],STR_VALUES[1],STR_VALUES[2],weaponds[1],STR_VALUES[3],STR_VALUES[4])
	ITEM_MENU = "=============================\n|            |              |\n| ITEMS      |{}SMALL HEALTH |\n|            | = {}         |\n|            |{}LARGE HEALTH |\n|            | = {}         |\n|            |              |\n=============================\n".format(items[0],STR_VALUES[5],items[1],STR_VALUES[6])

	if fight_type == 0:

		if menu_type == 0:

			print(FIGHT_1V1)
			print(MENU)

		elif menu_type == 1:

			print(FIGHT_1V1)
			print(FIGHT_MENU)

		elif menu_type == 2:

			print(FIGHT_1V1)
			print(ITEM_MENU)

		elif menu_type == 3:

			print(FIGHT_1V1)
			print(FLEE_MENU)

	elif fight_type == 1:

		if menu_type == 0:

			print(FIGHT_1V2)
			print(MENU)

		elif menu_type == 1:

			print(FIGHT_1V2)
			print(FIGHT_MENU)

		elif menu_type == 2:

			print(FIGHT_1V2)
			print(ITEM_MENU)

		elif menu_type == 3:

			print(FIGHT_1V2)
			print(FLEE_MENU)

	elif fight_type == 2:

		if menu_type == 0:

			print(FIGHT_2V1)
			print(MENU)

		elif menu_type == 1:

			print(FIGHT_2V1)
			print(FIGHT_MENU)

		elif menu_type == 2:

			print(FIGHT_2V1)
			print(ITEM_MENU)

		elif menu_type == 3:

			print(FIGHT_2V1)
			print(FLEE_MENU)

	elif fight_type == 3:

		if menu_type == 0:

			print(FIGHT_2V2)
			print(MENU)

		elif menu_type == 1:

			print(FIGHT_2V2)
			print(FIGHT_MENU)

		elif menu_type == 2:

			print(FIGHT_2V2)
			print(ITEM_MENU)

		elif menu_type == 3:

			print(FIGHT_2V2)
			print(FLEE_MENU)
	
	time.sleep(0.1)




while True:

	clear()
	selection = 0
	selected = False
	lineend = 0
	spacex = 0
	chunk = 100

	for i in TITLE:

		for j in i:

			print(j)
			time.sleep(0.125)
	
	input("Press Enter To Continue>")

	clear()
	print("SELECT A LEVEL")
	
	for i in range(0,len(LEVELS)):

		if i == selection:

			print(">",LEVELS[i])

		else:

			print(LEVELS[i])
	
	while not selected:
		
		if keyboard.is_pressed("enter"):

			selected = True
			time.sleep(0.125)

		elif keyboard.is_pressed("down"):

			selection += 1
			clear()
			print("SELECT A LEVEL")

			for i in range(0,len(LEVELS)):

				if i == selection:

					print(">",LEVELS[i])

				else:

					print(LEVELS[i])

		elif keyboard.is_pressed("up"):

			selection -= 1
			clear()
			print("SELECT A LEVEL")

			for i in range(0,len(LEVELS)):

				if i == selection:

					print(">",LEVELS[i])

				else:

					print(LEVELS[i])
		
		if selection ==11:

			selection = 0
			clear()
			print("SELECT A LEVEL")

			for i in range(0,len(LEVELS)):

				if i == selection:

					print(">",LEVELS[i])

				else:

					print(LEVELS[i])

		elif selection == -1:

			selection = 10 
			clear()
			print("SELECT A LEVEL")

			for i in range(0,len(LEVELS)):

				if i == selection:

					print(">",LEVELS[i])

				else:

					print(LEVELS[i])

		time.sleep(0.1)

	def drawMap(selection, lineend):

		global enemy_loc
		
		clear()
		if chunk < 120 and spacex > 0:
			print(SCENES[selection][0], end = " ")
		for i in range(chunk -100 -lineend ,chunk):

			if i == spacex:

				print(SCENES[selection][i], end = CHARACTER)

			else:

				if enemy_loc[0]:

					if randint(0,100) < 20:					

						print(SCENES[selection][i], end = ENEMY)
						enemy_loc.append(i)

					else:

						print(SCENES[selection][i], end = " ")

				else:

					for j in range(1,len(enemy_loc)):
						
						if i == enemy_loc[j]:

							print(SCENES[selection][i], end = ENEMY)

					if not i in enemy_loc:

						print(SCENES[selection][i], end = " ")						
							
		enemy_loc[0] = False
		print(" ")
		time.sleep(0.1)
		
	drawMap(selection,lineend)
	
	while selected:
		
		for i in range(1,len(enemy_loc)):

			if spacex == enemy_loc[i]:

				fighting = True
				spacex += 1
				drawFight(INT_VALUES[12], INT_VALUES[13])
		
		while fighting:

			if INT_VALUES[10] <= 0 or INT_VALUES[0] <= 0:

				fighting = False
				INT_VALUES = [100,     35,          25,            20,        15,           5,         5,          0,          0,               0,             100,        100,     0,           0]
				STR_VALUES = ["0","0","0","0","0","0","0"]
				drawMap(selection,lineend)
				break

			if keyboard.is_pressed("down"):

				if INT_VALUES[13] == 0:

					INT_VALUES[7] += 1
					INT_VALUES[13] = 0

					if INT_VALUES[7] >= 3:

						INT_VALUES[7] = 0
						INT_VALUES[13] = 0

				elif INT_VALUES[13] == 1:

					INT_VALUES[8] += 1

					if INT_VALUES[8] >= 2:

						INT_VALUES[8] = 0

				elif INT_VALUES[13] == 2:

					INT_VALUES[9] += 1

					if INT_VALUES[9] >= 2:

						INT_VALUES[9] = 0
				
				drawFight(INT_VALUES[12], INT_VALUES[13])	
			
			elif keyboard.is_pressed("up"):

				clear()

				if INT_VALUES[13] == 0:

					INT_VALUES[7] -= 1
					INT_VALUES[13] = 0

					if INT_VALUES[7] == -1:

						INT_VALUES[7] = 2
						INT_VALUES[13] = 0

				elif INT_VALUES[13] == 1:

					INT_VALUES[8] -= 1

					if INT_VALUES[8] == -1:

						INT_VALUES[8] = 1

				elif INT_VALUES[13] == 2:

					INT_VALUES[9] -= 1

					if INT_VALUES[9] == -1:

						INT_VALUES[9] = 1
				
				drawFight(INT_VALUES[12], INT_VALUES[13])
	
			elif keyboard.is_pressed("enter"):

				hit = False
				healed = False

				if INT_VALUES[13] == 0:

					if INT_VALUES[7] == 0:

						INT_VALUES[13] = 1

					elif INT_VALUES[7] == 1:

						INT_VALUES[13] = 2

					elif INT_VALUES[7] == 2:

						INT_VALUES[13] = 3

				elif INT_VALUES[13] == 1:

					if INT_VALUES[8] == 0:

						if randint(0,100) > 20:

							INT_VALUES[10] -= 35
							INT_VALUES[13] = 0

						else:

							hit = True
							INT_VALUES[0] -= 35
							INT_VALUES[13] = 0

					elif INT_VALUES[8] == 1:

						if randint(0,100) > 15:

							hit = True
							INT_VALUES[10] -= 25
							INT_VALUES[13] = 0

						else:

							INT_VALUES[0] -= 35
							INT_VALUES[13] = 0

				elif INT_VALUES[13] == 2:

					if INT_VALUES[9] == 0:

						if INT_VALUES[5] >0 and INT_VALUES[0] < 100:

							INT_VALUES[0] += 15
							INT_VALUES[5] -= 1
							healed = True

					elif INT_VALUES[9] == 1:

						if INT_VALUES[6] >0 and INT_VALUES[0] < 100:

							INT_VALUES[0] += 25
							INT_VALUES[6] -= 1
							healed = True

				elif INT_VALUES[13] == 3:

					if not fleed:

						fleed = True

						if randint(0,100) <= 0:

							fighting = False
							INT_VALUES = [100,     35,          25,            20,        15,           5,         5,          0,          0,               0,             100,        100,     0,           0]
							STR_VALUES = ["0","0","0","0","0","0","0"]
							drawMap(selection,lineend)
							break

				drawFight(INT_VALUES[12], INT_VALUES[13])

				if INT_VALUES[13] == 3 and fleed:

					print("You have already tried that")

				elif INT_VALUES[13] == 0 and hit:

					print("Missed! You've been hit!")

				elif INT_VALUES[13] == 2 and healed:

					print("You've been healed!")

			elif keyboard.is_pressed("escape"):

				INT_VALUES[13] = 0
				drawFight(INT_VALUES[12], INT_VALUES[13])

		if spacex == len(SCENES[selection])-1:
			
			clear()
			for i in END_SCREEN:

				print(i)
				time.sleep(0.125)

			time.sleep(0.125)
			print("Press Enter To Continue>")
			time.sleep(0.125)
			break
		
		if spacex+1 == chunk:

			chunk += 100

			if chunk >= len(SCENES[selection]):

				chunk = len(SCENES[selection])
		
			
		try:

			if not ("\n" in SCENES[selection][chunk]):

				chunk += 1	
				lineend += 1	

		except:

			pass

		if keyboard.is_pressed("escape"):

			break

		elif keyboard.is_pressed("right"):

			if spacex > chunk:

				spacex = chunk

			else:

				spacex +=1

			drawMap(selection, lineend)

		elif keyboard.is_pressed("left"):

			if not spacex < chunk - 100 - (lineend- 1):

				spacex -=1

			drawMap(selection, lineend)

		elif keyboard.is_pressed("down"):

			spacecount = []
			lentraveled = 0
			lenteleport = 0

			for i in range(spacex+1,spacex+21):

				if "\n" in SCENES[selection][i]:

					spacecount.append(i)

					for j in range(i+1,i+21):

						if not spacecount[0] == len(SCENES[selection])-1:

							if "\n" in SCENES[selection][j]:

								 spacecount.append(j)
								 break
					
					break
			
			if not spacecount[0] == chunk:

				for i in range(spacex,spacex-26, -1):

					if "\n" in SCENES[selection][i]:

						spacecount.append(i)
						break

					elif i == 0:

						spacecount.append(0)
						break				

				try:
					
					if spacecount[2] != 0:

						lentraveled += len(SCENES[selection][SCENES[selection][spacecount[2]].find("\n") + 1:len(SCENES[selection][spacecount[2]])])

					else:

						lentraveled += len(SCENES[selection][spacecount[2]])

					for i in range(spacecount[2]+1,spacex+1):

						lentraveled += len(SCENES[selection][i]) + 1

					
					lenteleport += len(SCENES[selection][SCENES[selection][spacecount[0]].find("\n") + 1:len(SCENES[selection][spacecount[0]])]) 
					
					for i in range(spacecount[0]+1,spacecount[1]+1):

						if lenteleport == lentraveled:

							spacex = i-1
							drawMap(selection, lineend)
							break

						elif lenteleport + 1 == lentraveled:

							spacex = i-1
							drawMap(selection, lineend)
							break

						elif lenteleport - 1 == lentraveled:

							spacex = i-1
							drawMap(selection, lineend)
							break

						lenteleport += len(SCENES[selection][i]) + 1

				except:

					pass