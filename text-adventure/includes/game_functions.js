<script>

function replaceAll(str, find, replace) {
  return str.replace(new RegExp(find, 'g'), replace);
}   //end function ParsePlayerInput


function errMsg(errorglobal) {
 //Whenever the player wants to go in a direction that does not exist at the current location, the exit message will throw out a random
 //exit message from the global list.
  rndMsgLngth = globalmsg[errorglobal].length;
  rndMsgRst = Math.floor(Math.random() * rndMsgLngth);
  return globalmsg[errorglobal][rndMsgRst]);
}


function scrnDisplay($text2dis) {
 //Function that writes to the screen. 
  
  roomText = document.getElementById("StartRoomText");
  
  if (GLOBALSETCLS = true) {
   //if globally set to clear the screen for every new text inputted. 
    roomText.innerHTML = $text2dis;
  } 
  else {
    roomText.innerHTML += $text2dis;
  }
}

function findBetween(text, firststring, secondstring){
  //Function to text between two strings.
    var firstvariable = firststring;
    var secondvariable = secondstring;
    var text = text;   
   
          var regExString = new RegExp("(?:"+firstvariable+")((.[\\s\\S]*))(?:"+secondvariable+")", "ig"); //set ig flag for global search and case insensitive

              var strResult = regExString.exec(text);
  
  return strResult[1];
  
}

function strDelimiterCnt(text, delimiter){
 //Function to enter a string and divide it using a delimiter and return the count
  var textsep = text;
         textsep.split(delimiter);
  
  return textsep.length;
  
}

function strDelimiter(text, delimiter, pos){
 //Function to enter a string and divide it using a delimiter and return the string at the split position
  var textsep = text;
         textsep.split(delimiter);
  
  return textsep[pos];
  
}

function rtnStringInstances(string, searchinstance) {
//returns the number of times the search appears in the string.
  
eval("var regex = /" + searchinstance + "/gi, result, indices = [];");
while ( (result = regex.exec(string)) ) {
    indices.push(result);
    
}

return indices.length;
  
}

<script>
