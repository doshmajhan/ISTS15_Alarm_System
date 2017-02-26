function loadStat(url) {
  var xhttp;
  xhttp=new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      var div = document.getElementById("box");
      if (xhttp.responseText.trim() === 'NULL') {
        document.getElementById("stat").innerHTML = "Unable to connect to sensor...";
        div.style.backgroundColor="orange";
      }
      else if (xhttp.responseText.trim() == 0) {
        document.getElementById("stat").innerHTML = "Powered Off.";
        div.style.backgroundColor="red";
      }
      else {
        document.getElementById("stat").innerHTML = "Powered On";
        div.style.backgroundColor="green";
      }
    }
  };
  xhttp.open("GET", url, true);
  xhttp.send();
}

function loadLog(url) {
  var xhttp;
  xhttp=new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
        var logTable = document.getElementById("logTable");
        var file = xhttp.responseText;
        file = file.split('\n');
        for(var line = 0; line < file.length; line ++){
            var row = logTable.insertRow(0);
            var cell = row.insertCell(0);
            cell.innerHTML = file[line];
        }
    }
  };
  xhttp.open("GET", url, true);
  xhttp.send();
}
