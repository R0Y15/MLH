<script>	
     {

//create array for delimeterWords and ignored words
var coldel_words = new Array();
var colig_words = new Array();


//make all input lowercase so all cases match
		var UselessWords = IgnoredWords;
	
			UselessWords = UselessWords.toLowerCase();
			UselessWords = UselessWords.split(",");
	
		var consoleString = consoleString;
			consoleString = consoleString.toLowerCase();
	    var phrasedirect = '';
	    var onewordcmd = consoleString.split(' ').slice(0,1).join('');
        var twowordcmd = consoleString.split(' ').slice(0,2).join('');
        var threewordcmd = consoleString.split(' ').slice(0,3).join('');
		
		var textcmd = '';
		var firstObj = '';

//Find the command
	for( let syn in synonyms ){
    if (syn == onewordcmd){
        textcmd = synonyms[syn][0];
        phrasedirect = syn;
        break;
    
} else if (syn == twowordcmd){
        textcmd = synonyms[syn][0];
        phrasedirect = syn;
        break;
        
} else if (syn == threewordcmd){
        textcmd = synonyms[syn][0];
        phrasedirect = syn;
        break;	
} else {
	
	textcmd = CMDERROR;

}
									}
//

if(textcmd)
{
//this removes the command word "textcmd" from the input string
consoleString = consoleString.replace(phrasedirect, "");

}


for (i = 0; i < a.length; i++) {
var replacedWord = " " + a[i] + " ";
coligwords.push(replacedWord.trim());
    consoleString = replaceAll(consoleString, replacedWord, " ");
  
    
}

//This will replace delimeter words such as on/and/with or whatever is described with a comma to make it into an array
delimeterWords = delimeterWords.toLowerCase();
var a = delimeterWords.split(","),
    i;

for (i = 0; i < a.length; i++) {
var replacedWord = " " + a[i] + " ";

    consoleString = replaceAll(consoleString, replacedWord, ",");
   // consoleString = replaceAll(consoleString, replacedWord, "");
    
  //Deprecated: coldelwords.push(replacedWord.trim());
    
}


firstObj = consoleString.split(",", 2);

if (texcmd = CMDERROR) {
   
	errMsg('nocmd'); //if No synonym or command is found in the synonym list, it will throw an error. Otherwise will continue processing
	
}
else {
	
	var executeParse = firstObj[0] + "_" + textcmd; //eg: desk_look
	
	if (typeof window[executeParse] === 'function') { 
  		//if no command was defined in the code, it will throw an error and run one of the customized error messages
		
		executeParse = executeParse  + "()";
		eval(executeParse);
		
} else {
	
	errMsg('nocmd');
	
}




</script>
