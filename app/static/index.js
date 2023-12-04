let Workflows = function () {

    let firstEmail = document.getElementById("firstEmail").value;
    let secondEmail = document.getElementById("secondEmail").value;
    
    var data = new FormData();
    data.append("firstEmail", firstEmail);
    data.append("secondEmail", secondEmail);

    fetch("/subscribe", {
        method: "POST",
        body: data,
    })
        .then((response) => response.json())
        .then((json) => {
            if (json.error) {
                let e = document.getElementById("output");
                e.innerHTML =
                    `<div class="alert alert-danger mb-3" role="alert"><h3>Error</h3>${json.error}</div>`
                    + e.innerHTML;
            }
        });
};

let Unsubscribe = function () {

    let firstEmail = document.getElementById("firstEmail").value;
    let secondEmail = document.getElementById("secondEmail").value;
    
    var data = new FormData();
    data.append("firstEmail", firstEmail);
    data.append("secondEmail", secondEmail);

    fetch("/unsubscribe", {
        method: "DELETE",
        body: data,
    })
        .then((response) => response.json())
        .then((json) => {
            if (json.error) {
                let e = document.getElementById("output");
                e.innerHTML =
                    `<div class="alert alert-danger mb-3" role="alert"><h3>Error</h3>${json.error}</div>`
                    + e.innerHTML;
            }
        });
};