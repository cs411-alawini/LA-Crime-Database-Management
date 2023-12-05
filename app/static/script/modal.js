let Workflows = function () {

    let DescriptionId = document.getElementById("DescriptionId").value;
    print(DescriptionId)
    
    var data = new FormData();

    data.append("DescriptionId", DescriptionId);

    fetch("/crimeDescription/${DescriptionId}", {
        method: "GET",
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




//     fetch("/subscribe", {
//         method: "POST",
//         body: data,
//     })
//         .then((response) => response.json())
//         .then((json) => {
//             if (json.error) {
//                 let e = document.getElementById("output");
//                 e.innerHTML =
//                     `<div class="alert alert-danger mb-3" role="alert"><h3>Error</h3>${json.error}</div>`
//                     + e.innerHTML;
//             }
//         });
// };

// let Unsubscribe = function () {

//     let firstEmail = document.getElementById("firstEmail").value;
//     let secondEmail = document.getElementById("secondEmail").value;
    
//     var data = new FormData();
//     data.append("firstEmail", firstEmail);
//     data.append("secondEmail", secondEmail);

//     fetch("/unsubscribe", {
//         method: "DELETE",
//         body: data,
//     })
//         .then((response) => response.json())
//         .then((json) => {
//             if (json.error) {
//                 let e = document.getElementById("output");
//                 e.innerHTML =
//                     `<div class="alert alert-danger mb-3" role="alert"><h3>Error</h3>${json.error}</div>`
//                     + e.innerHTML;
//             }
//         });
// };