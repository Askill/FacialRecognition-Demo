
rootKontext = ""
selected = null
var ml = document.getElementById('middle-left');
var mr = document.getElementById('middle-right');
personData = {}


function focusNav(id) {
    focusedID = id;
    $(id).addClass('btn-primary').siblings().removeClass('btn-primary')
    //$(id).removeClass('active').siblings().removeClass('active')
}

function focusPerson(id) {
    selected = id;
    $("#person" + id).removeClass('border-light').siblings().addClass('border-light')
    $("#person" + id).addClass('border-success').siblings().removeClass('border-success')
    renderPersonRight()
}

function loadPersonList(data) {
    console.log(data)
    data = data["data"]
    let el = document.getElementById('list');
    data.forEach(function (item) {
        string = `
        <div class="card border-light"  onclick="focusPerson(${item["person_id"]})" id="person${item["person_id"]}">
            <div class="card-body">
                <h4 class="card-title">${item["fname"]} ${item["lname"]}</h4>
                <h6 class="card-subtitle mb-2 text-muted">${item["timestamp"]}</h6>

                <p class="card-text">
                    <img class="listImg" src="${item["face"]}"></img>
                    <div class="personalInfo">
                        Gender: ${item["gender"]} <br>
                        YoB: ${item["yob"]} <br>
                        Available FP: ${item["fingerprints"].length} <br>
                        
                    </div>
                    
                </p>
            </div>
        </div>
        `
        el.innerHTML += string;
    })
}

function snapShot(){
    postJSON(rootKontext + "/api/v1/camera/", {},         
        function (error, data) {
            document.getElementById('image-left').src = rootKontext + "/api/v1/camera/still";
        }
    );
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

function identify(){
    snapShot()
    getJSON(rootKontext + "/api/v1/person/?useFace=True",
        function (error, data) {
            data = data["data"]
            renderPersonRight(data)
        }
    );
}

function validate(){
    snapShot()
    getJSON(rootKontext + "/api/v1/person/" + selected + "?useFace=True",
        function (error, data) {
            data = data["data"]
            renderPersonRight(data)
        }
    );
}

function loadStream() {
    string = `
    <img src="${rootKontext + "/api/v1/camera/stream"}" id="image-left"> </img>
    `
    ml.innerHTML += string;

    string = `
    <img src="${rootKontext + "/api/v1/camera/still"}" id="image-right"> </img>
    `
    mr.innerHTML += string;
}

function loadData() {
    getJSON(rootKontext + "/api/v1/person/",
        function (error, data) {
            ml = document.getElementById('middle-left');
            mr = document.getElementById('middle-right');
            personData = data
            loadPersonList(data)
            renderIdentify()
        }
    );
}

