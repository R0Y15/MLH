<script>
//Global Variables for game settings
var GAMENAME = '';
var OBJECTGLOBAL = '';  //Indicates the current OBJECT loaded.
var GAMECURPLAYER = ''; //Indicates the current player you control.
var GAMESCORE = '0';
var GLOBALSETCLS = false;
var GAMEEAST = ['e', 'east', 'go e', 'go east', 'head east', 'head e', 'explore east', 'explore e', 'go eastbound', 'head eastbound', 'go east bound', 'head east bound', 'travel e', 'travel east'];
var GAMEWEST = ['w', 'west', 'go w', 'go west', 'head west', 'head w', 'explore west', 'explore w', 'go westbound', 'head westbound', 'go west bound', 'head west bound', 'travel w', 'travel west'];
var GAMESOUTH = ['s', 'south', 'go s', 'go south', 'head south', 'head s', 'explore south', 'explore s', 'go southbound', 'head southbound', 'go south bound', 'head south bound', 'travel s', 'travel south'];
var GAMENORTH = ['n', 'north', 'go n', 'go north', 'head north', 'head n', 'explore north', 'explore n', 'go northbound', 'head northbound', 'go north bound', 'head north bound', 'travel n', 'travel north'];
var GAMESOUTHEAST = ['se', 'southeast', 'south east', 'go se', 'go southeast', 'go south east', 'head southeast', 'head se', 'explore southeast', 'explore se', 'go southeastbound', 'head southeastbound', 'go southeast bound', 'head southeast bound', 'travel se', 'travel southeast'];
var GAMENORTHEAST = ['ne', 'northeast', 'north east', 'go ne', 'go northeast', 'go north east', 'head northeast', 'head ne', 'explore northeast', 'explore ne', 'go northeastbound', 'head northeastbound', 'go northeast bound', 'head northeast bound', 'travel ne', 'travel northeast'];
var GAMENORTHWEST = ['nw', 'northwest', 'north west', 'go nw', 'go northwest', 'go north west', 'head northwest', 'head nw', 'explore northwest', 'explore nw', 'go northwestbound', 'head northwestbound', 'go northwest bound', 'head northwest bound', 'travel nw', 'travel northwest'];
var GAMESOUTHWEST = ['sw', 'southwest', 'south west', 'go sw', 'go southwest', 'go south west', 'head southwest', 'head sw', 'explore southwest', 'explore sw', 'go southwestbound', 'head southwestbound', 'go southwest bound', 'head southwest bound', 'travel sw', 'travel southwest'];
var GAMEUP = ['u', 'up', 'go u', 'go up', 'head up', 'head u', 'explore up', 'explore u', 'go upbound', 'head upbound', 'go upward', 'head upward', 'travel u', 'travel upward', 'climb up', 'climb u', 'climb upward'];
var GAMEDOWN = ['d', 'down', 'go d', 'go down', 'head down', 'head d', 'explore down', 'explore d', 'go downbound', 'head downbound', 'go downward', 'head downward', 'travel d', 'travel downward', 'climb down', 'climb d', 'climb downward'];



//Global constiables for Game Object details
const OBJECTNAME = 0;
const OBJECTID = 1;
const OBJECTTYPE = 2 ;
const OBJECTDESCFIRSTTIME = 3;
const OBJECTDESC = 4;
const OBJECTSHORTDESC = 5;
const OBJECTALTNAMES = 6;
const OBJECTXSIZE = 7;
const OBJECTYSIZE = 8;
const OBJECTIMAGE = 9;
const OBJECTMOVIE = 10;
const OBJECTPLAYERSTATUS = 11;
const OBJECTAMOUNT = 12; //How much of the object exists.
const OBJECTSCORE = 13;
const OBJECTTICKER = 14; //Ticks off each time the object was entered.
const OBJECTTICKERUSE = 15; //How many times the object was used.


//Global Const to be used with GameObjectContainer for containing inventory and equiping items.
const OBJECTCONTAINER = 1;
const OBJECTEQUIPHEAD = 2;
const OBJECTEQUIPEYES = 3;
const OBJECTEQUIPEARS = 4;
const OBJECTEQUIPMOUTH = 5;
const OBJECTEQUIPLEFTHAND = 6;
const OBJECTEQUIPRIGHTHAND = 7;
const OBJECTEQUIPLEFTFOOT = 8;
const OBJECTEQUIPRIGHTFOOT = 9;
const OBJECTEQUIPFRONTTORSO = 10;


//Global constiables for Game Object direction details for obect: GameObjectTravel
const OBJECTGOEAST = 1;
const OBJECTGOWEST = 2;
const OBJECTGONORTH = 3;
const OBJECTGOSOUTH = 4;
const OBJECTGOUP = 5;
const OBJECTGODOWN = 6;
const OBJECTGONORTHWEST = 7;
const OBJECTGONORTHEAST = 8;
const OBJECTGOSOUTHWEST = 9;
const OBJECTGOSOUTHEAST = 10;


//Global constiables for Game Object Blocked or locked Locations. Used with GameObjectTravel
const OBJECTGOEASTBLOCK = 11;
const OBJECTGOWESTBLOCK = 12;
const OBJECTGONORTHBLOCK = 13;
const OBJECTGOSOUTHBLOCK = 14;
const OBJECTGOUPBLOCK = 15;
const OBJECTGODOWNBLOCK = 16;
const OBJECTGONORTHWESTBLOCK = 17;
const OBJECTGONORTHEASTBLOCK = 18;
const OBJECTGOSOUTHWESTBLOCK = 19;
const OBJECTGOSOUTHEASTBLOCK = 20;


//Global constiables for Game Object Description to specify why the location is locked. Used with GameObjectTravel
const OBJECTGOEASTBLOCKDESC = 21;
const OBJECTGOWESTBLOCKDESC = 22;
const OBJECTGONORTHBLOCKDESC = 23;
const OBJECTGOSOUTHBLOCKDESC = 24;
const OBJECTGOUPBLOCKDESC = 25;
const OBJECTGODOWNBLOCKDESC = 26;
const OBJECTGONORTHWESTBLOCKDESC = 27;
const OBJECTGONORTHEASTBLOCKDESC = 28;
const OBJECTGOSOUTHWESTBLOCKDESC = 29;
const OBJECTGOSOUTHEASTBLOCKDESC = 30;


//Global constiables for GameObjectTravel Description when looking at OBJECT from constious directions(EG: Look from southwest at OBJECT)
const OBJECTFROMEASTLOOK = 31;
const OBJECTFROMWESTLOOK = 32;
const OBJECTFROMNORTHLOOK = 33;
const OBJECTFROMSOUTHLOOK = 34;
const OBJECTFROMUPLOOK = 35;
const OBJECTFROMDOWNLOOK = 36;
const OBJECTFROMNORTHWESTLOOK = 37;
const OBJECTFROMNORTHEASTLOOK = 38;
const OBJECTFROMSOUTHWESTLOOK = 39;
const OBJECTFROMSOUTHEASTLOOK = 40;


//Global for Object events in GameObjectEvents
const OBJECTONENTER = 1;
const OBJECTONENTERTIMES = 2;


//Global constiables for GameObjectCommands
const OBJECTLOOK = 1;
const OBJECTTALK = 2;
const OBJECTTAKE = 3;
const OBJECTKICK = 4;
const OBJECTLICK = 5;
const OBJECTPUNCH = 6;
const OBJECTPUSH = 7;
const OBJECTPULL = 8;
const OBJECTTASTE = 9;
const OBJECTSMELL = 10;
const OBJECTLISTEN = 11;
const OBJECTTURNON = 12;
const OBJECTTURNOFF = 13;
const OBJECTTHINK = 14;
const OBJECTSMILE = 15;
const OBJECTCRY = 16;
const OBJECTTHROW = 17;
const OBJECTSHOOT = 18;
const OBJECTOPEN = 19;
const OBJECTCLOSE = 20;
const OBJECTFIGHT = 21;
const OBJECTUSE = 22;
const OBJECTPUTON = 23;
const OBJECTTAKEOFF = 24;
const OBJECTPICKUP = 25;
const OBJECTLOCK = 26;
const OBJECTUNLOCK = 27;
const OBJECTREAD = 28;
const OBJECTFIX = 29;
const OBJECTCLIMB = 30;
const OBJECTMOVE = 31;
const OBJECTDROP = 32;
const OBJECTATTACK = 33;
const OBJECTHIT = 34;
const OBJECTBITE = 35;
const OBJECTLAUGH = 36;
const OBJECTSWITCH = 37;
const OBJECTFLICK = 38;
const OBJECTTRIGGER = 39;
const OBJECTTRANSFORM = 40;
const OBJECTASK = 41;
const OBJECTBLOW = 42;
const OBJECTYELL = 43;
const OBJECTKNOCK = 44;
const OBJECTMOUNT = 45;
const OBJECTDISMOUNT = 46;
const OBJECTEAT = 47;
const OBJECTSWALLOW = 48;
const OBJECTSIT = 49;
const OBJECTSTEP = 50;
const OBJECTSTAND = 51;
const OBJECTDROPKICK = 52;
const OBJECTMOCK = 53;
const OBJECTSEAL = 54;
const OBJECTUNSEAL = 55;
const OBJECTCUT = 56;
const OBJECTSTAB = 57;
const OBJECTRIP = 58;
const OBJECTSLICE = 59;
const OBJECTLAND = 60;
const OBJECTTHANK = 61;
const OBJECTSWEAR = 62;
const OBJECTTEASE = 63;
const OBJECTPOINT = 64;
const OBJECTKISS = 65;
const OBJECTHUG = 66;
const OBJECTTOUCH = 67;
const OBJECTGIVE = 68;
const OBJECTTAKE = 69;
const OBJECTSLAP = 70;
const OBJECTCHALLENGE = 71;
const OBJECTSING = 72;
const OBJECTCALL = 73;
const OBJECTSPARE = 74;
const OBJECTHELP = 75;
const OBJECTHEAL = 76;
const OBJECTKILL = 77;
const OBJECTPUT = 78;
const OBJECTSALUTE = 79;
const OBJECTGREET = 80;
const OBJECTFALL = 81;
const OBJECTJUMP = 82;
const OBJECTSHOUT = 83;
const OBJECTWHISPER = 84;
const OBJECTRUN = 85;
const OBJECTWALK = 86;
const OBJECTDEFEND = 87;
const OBJECTTIE = 88;
const OBJECTUNTIE = 89;
const OBJECTBREAK = 90;
const OBJECTSNORT = 91;
const OBJECTDRINK = 92;
const OBJECTPRAY = 93;
const OBJECTWINK = 94;
const OBJECTSMOKE = 95;
const OBJECTLIGHT = 96;
const OBJECTACTIVATE = 97;
const OBJECTDEACTIVATE = 98;
const OBJECTOPERATE = 99;
const OBJECTSING = 100;
const OBJECTANSWER = 101;
const OBJECTBURN = 102;
const OBJECTCOUNT = 103;
const OBJECTINFLATE = 104;
const OBJECTDEFLATE = 105;
const OBJECTCROSS = 106;
const OBJECTDIG = 107;
const OBJECTBURY = 108;
const OBJECTENTER = 109;
const OBJECTEXIT = 110;
const OBJECTEMPTY = 111;
const OBJECTFILL = 112;
const OBJECTEXTINGUISH = 113;
const OBJECTFOLLOW = 114;
const OBJECTKNOCK = 115;
const OBJECTTRANSFER = 116;
const OBJECTMOVE = 117;
const OBJECTRAISE = 118;
const OBJECTLOWER = 119;
const OBJECTSEARCH = 120;
const OBJECTSHAKE = 121;
const OBJECTSLIDE = 122;
const OBJECTSTAY = 123;
const OBJECTSTRIKE = 124;
const OBJECTFIRE = 125;
const OBJECTSWIM = 126;
const OBJECTTELL = 127;
const OBJECTWAKE = 128;
const OBJECTCHARM = 129;
const OBJECTWAVE = 130;
const OBJECTWIND = 131;
const OBJECTDRILL = 132;
const OBJECTHAMMER = 133;
const OBJECTSCREW = 134;
const OBJECTPOUND = 135;


</script>
