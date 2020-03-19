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

function postJSON(url, data, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url, true);
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