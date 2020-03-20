function clearMiddle(){
    ml.innerHTML = ""
    mr.innerHTML = ""
}

function renderValidate(){
    clearMiddle()
    string = `
    <img src="${rootKontext + "/api/v1/camera/stream"}" id="image-left"> </img>
    
    <button onclick="validate()" class="btn btn-primary float-right middle-controls">Verify</button>
    <button onclick="renderValidate()" class="btn btn-warning float-right middle-controls">Retry</button>
    `
    ml.innerHTML = string;
    $("#middle-right").removeClass("border-danger").removeClass("border-success")
}

function renderChange(){
    clearMiddle()
    $("#middle-right").removeClass("border-danger").removeClass("border-success")
    console.log("change")

}
function renderEnrole(){
    clearMiddle()
    string = `
    <img src="${rootKontext + "/api/v1/camera/stream"}" id="image-left"> </img>
    
    <button onclick="snapShot()" class="btn btn-primary float-right middle-controls">Snap</button>
    <button onclick="renderEnrole()" class="btn btn-warning float-right middle-controls">Retry</button>
    `
    ml.innerHTML = string;

    string2 = `
    <form id="personform">
        <input type="text" class="form-control" name="fname" placeholder="First Name" ><br>
        <input type="text" class="form-control" name="lname" placeholder="Last Name" ><br>
        <select class="form-control" id="gender" name="gender">
            <option>male</option>
            <option>female</option>
            <option>other</option>
        </select><br>
        <input type="text" class="form-control" name="yob" placeholder="YoB"><br>
        
    </form>
    <button type="button" class="btn btn-success float-right" onclick="enrole()">Enrole</button>
    `
    mr.innerHTML = string2;
    $("#middle-right").removeClass("border-danger").removeClass("border-success")
}
function renderIdentify(){
    clearMiddle()
    string = `
    <img src="${rootKontext + "/api/v1/camera/stream"}" id="image-left"> </img>
    
    <button onclick="identify()" class="btn btn-primary float-right middle-controls">Identify</button>
    <button onclick="renderIdentify()" class="btn btn-warning float-right middle-controls">Retry</button>
    `
    ml.innerHTML = string;
    $("#middle-right").removeClass("border-danger").removeClass("border-success")
}