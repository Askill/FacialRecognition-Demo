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

function renderPersonIdentify(data){
    console.log(data)
    data.forEach(function (item) {
        string = `
        <div class="card border-light"  onclick="focusPerson(${item["person_id"]})" id="person${item["person_id"]}">
            <div class="card-body">
                <p class="card-text">
                    <img class="listImg" src="${item["face"]}"></img>
                    <div class="personalInfo">
                        Name: ${item["fname"]} ${item["lname"]} <br>
                        Gender: ${item["gender"]} <br>
                        YoB: ${item["yob"]} <br>
                        <h4>${item["matching_score"]}</h4>
                    </div>
                </p>
            </div>
        </div>
        `
        mr.innerHTML += string;
    })
}

function renderPersonRight(data){
    string = `
        <img src="${data["face"]}" id="image-right"> </img>

        <h4 class="heroInfo">
            Gender: ${data["gender"]} <br>
            YoB: ${data["yob"]} <br>
            Available FP: ${data["fingerprints"].length} <br>
            <h3>Score: ${data["matching_score"]} </h3>
        </h4>
        
    `
    mr.innerHTML = string;
}
