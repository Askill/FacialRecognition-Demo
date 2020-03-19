function clearMiddle(){
    ml.innerHTML = ""
    mr.innerHTML = ""
}

function renderValidate(){
    clearMiddle()
    string = `
    <img src="${rootKontext + "/api/v1/camera/stream"}" id="image-left"> </img>
    
    <button onclick="validate()" class="btn btn-primary float-right middle-controls">Validate</button>
    <button onclick="renderValidate()" class="btn btn-warning float-right middle-controls">Retry</button>
    `
    ml.innerHTML = string;
}

function renderChange(){
    clearMiddle()
    console.log("change")
}
function renderEnrole(){
    clearMiddle()
    console.log("enrole")
}
function renderIdentify(){
    clearMiddle()
    string = `
    <img src="${rootKontext + "/api/v1/camera/stream"}" id="image-left"> </img>
    
    <button onclick="identify()" class="btn btn-primary float-right middle-controls">Identify</button>
    <button onclick="renderIdentify()" class="btn btn-warning float-right middle-controls">Retry</button>
    `
    ml.innerHTML = string;
}