<script>
function LoadRoom(roomname) {

    
           OBJECTGLOBAL = roomname;
          
           if (GameObjects[OBJECTGLOBAL][OBJECTMOVIE][1] != ''){
 
           document.getElementById("StartRoomLoad").innerHTML = '<video id="mainvid" onerror="hidevideo(OBJECTGLOBAL);" onended="hidevideo(OBJECTGLOBAL);" width="100%" height="" autoplay>' + '<source src="' + GameObjects[OBJECTGLOBAL][OBJECTMOVIE][1] + '" type="video/mp4"></video>';
           } else if (GameObjects[OBJECTGLOBAL][ROOMIMAGE][1] != ''){
           document.getElementById("StartRoomLoad").innerHTML = "<img src='" + GameObjects[OBJECTGLOBAL][ROOMIMAGE][1] + "' id='RoomBackground' width='" + GameObjects[OBJECTGLOBAL][OBJECTXSIZE][1] + "' height='" + GameObjects[OBJECTGLOBAL][OBJECTYSIZE][1] + "'></image>";
           }
                    document.getElementById("StartRoomText").innerHTML = GameObjects[OBJECTGLOBAL][OBJECTDESCFIRSTTIME][1];
                 
                 
                 
                            }

                            

function hidevideo(roomname) {

  var x = document.getElementById("mainvid");
  var y = document.getElementById("RoomBackground");

    x.style.display = "none";

if (GameObjects[OBJECTGLOBAL][ROOMIMAGE][1] != ''){
           document.getElementById("StartRoomLoad").innerHTML = "<img src='" + GameObjects[OBJECTGLOBAL][ROOMIMAGE][1] + "' id='RoomBackground' width='" + GameObjects[OBJECTGLOBAL][OBJECTXSIZE][1] + "' height='" + GameObjects[OBJECTGLOBAL][OBJECTYSIZE][1] + "'></image>";
           }
           
}

  function executeObjectCmd(object, pos = 1) {
            
            
            eval(GameObjectsCommands[OBJECTGLOBAL][object][pos]);
            
        }

function changeObjectValue(object, field, value, pos = 1){
           
            
            GameObjects[room][field][pos] = value;
                        
        }


</script>
