
rootKontext = ""

function getJSON(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    xhr.onload = function () {
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

function putJSON(url, data, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('PUT', url, true);
    xhr.responseType = 'json';
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function () {
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


function loadData() {
    getJSON(rootKontext + "/api/v1/person/",
        function (error, data) {
            console.log(data)
            data = data["data"]
            let el = document.getElementById('list');
            data.forEach(function (item) {
                string = `
                <div class="card border-light">
                    <div class="card-body">
                        <h4 class="card-title">${item["fname"]} ${item["lname"]}</h4>
                        <h6 class="card-subtitle mb-2 text-muted">${item["timestamp"]}</h6>

                        <p class="card-text container">
                            <img class="listImg" src="${item["face"]}"></img>
                            <div class="personalInfo">
                                ${item["gender"]} <br>
                                ${item["yob"]} <br>
                                ${item["fingerprints"].length} <br>
                            </div>
                            
                        </p>
                    </div>
                </div>
                `
                el.innerHTML += string;
            })



        }
    );
}