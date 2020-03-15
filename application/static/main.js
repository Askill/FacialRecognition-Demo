var rootKontext = "/od1";
//var rootKontext = "";
var customeStyle = false;

function loadOD1(){
    try{
        let ksession = $.cookie("KSESSIONID");
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open( "GET", rootKontext, false );
        xmlHttp.send();
        document.getElementById("od1").innerHTML = xmlHttp.responseText;

        $('link[title="custom"]').prop('disabled', true);

        loadData();
    }
    catch(e){
        document.getElementById("od1").innerHTML = "Ein Fehler ist beim Laden des Dienstes aufgetreten, bitte versuchen Sie es später erneut.";
    }
}

function nextTab(){
    $('#navMenu1 a').removeClass("disabled");
    $('#navMenu1 a').tab('show');
}

function getJSON (url, callback) {
    let ksession = $.cookie("KSESSIONID");

    var xhr = new XMLHttpRequest();
    xhr.open('GET', url + "?session_id=" + ksession, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
      var status = xhr.status;
      if (status < 400) {
        callback(null, xhr.response);
      } else {
        console.log("failed getting");
        console.log(status);
      }
    };
    xhr.send();
};

function putJSON (url, data, callback) {
    let ksession = $.cookie("KSESSIONID");

    var xhr = new XMLHttpRequest();
    xhr.open('PUT', url + "?session_id=" + ksession, true);
    xhr.responseType = 'json';
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
      var status = xhr.status;
      if (status < 400) {
        callback(null, xhr.response);
      } else {
        console.log("failed posting");
        console.log(status);
      }
    };
    xhr.send(data);
};

function sendVorhaben(){
    let data = document.getElementById("form1");

    data = {};
    data["name"] = document.getElementById("form1")["name"].value;
    data["reason"] = document.getElementById("form1")["reason"].value;
    data["note"] = document.getElementById("form1")["note"].value;
    data["partial_application_id"] = document.getElementById("form1")["partial_application_id"].value;

    putJSON(rootKontext + "/api/v1/vorhaben/" + data["partial_application_id"],  JSON.stringify(data), function(error, data){
        document.getElementById("status").innerHTML = "Daten erfolgreich erneuert";
        loadData();
        nextTab();
    });

}

function queryString(string)
{
    let queryString = window.location.search;
    let varArray = queryString.split("&");
    for (let i=0;i<varArray.length;i++) {
      let param = varArray[i].split("=");
        if(param[0] == string ){
            return param[1]
        }
    }
}

function loadData(){
    let encodedID = queryString("?partialApplicationId");
    //encodedID = "d05e6d3a-1774-46a0-abb0-89abfe2ff5a3";
   getJSON(rootKontext + "/api/v1/vorhaben/" + encodedID, 
        function(error, data){
            console.log(data)
            populateForm(data["data"], "form1")
            populateForm(data["data"], "form2")
        }
    );
}

function populateForm(data, formId){
    console.log(data)
    inputs = document.forms[formId];

    for(var i = 0; i < 8; i++){   
        if(inputs[i] !== undefined && data[inputs[i].name] !== undefined){
            inputs[i].value = data[inputs[i].name];
        }
        else{
            console.log(inputs);
        }
    }
}

function loadNewStyle(){
    customeStyle = !customeStyle; 

    if(customeStyle){
        $('link[title="custom"]').prop('disabled', false);
        $('link[title="default"]').prop('disabled', true);

        console.log("StyleSheet: Custom");
        alert("StyleSheet: Custom");
    }
    else{
        $('link[title="default"]').prop('disabled', false);
        $('link[title="custom"]').prop('disabled', true);

        console.log("StyleSheet: Default");
        alert("StyleSheet: Default");
    }

}