// var Workflows = function () {
//   let DescriptionId = document.getElementById("DescriptionId").value;

//   var data = new FormData();

//   data.append("DescriptionId", DescriptionId);

//   fetch(`/crimeDescription/${DescriptionId}`, {
//     method: "GET",
//   })
//     .then((response) => response.json())
//     .then((json) => {
//       if (json.error) {
//         let e = document.getElementById("output");
//         e.innerHTML =
//           `<div class="alert alert-danger mb-3" role="alert"><h3>Error</h3>${json.error}</div>` +
//           e.innerHTML;
//       }
//     });
// };

var Workflows = function () {
    let DescriptionId = document.getElementById("DescriptionId").value;
  
    var data = new FormData();
  
    data.append("DescriptionId", DescriptionId);
  
    fetch(`/crimeDescription`, {
      method: "GET",
    })
      .then((response) => response.json())
      .then((json) => {
        if (json.error) {
          let e = document.getElementById("output");
          e.innerHTML =
            `<div class="alert alert-danger mb-3" role="alert"><h3>Error</h3>${json.error}</div>` +
            e.innerHTML;
        }
        else {
            for (var each in json) {
                var item = json[each]
                var html = `<tr><td>${item.CrimeCode}</td><td>${item.CrimeCodeDescription}</td></tr>`
                document.getElementById("CrimeDescription").innerHTML += html
            }
        }
      });

  };

var Deleting = function () {
  let DescriptionId = document.getElementById("DescriptionIdDeletion").value;

  var data = new FormData();

  data.append("DescriptionIdDeletion", DescriptionId);

  fetch(`/crimeDescription/delete/${DescriptionIdDeletion}`, {
    method: "DELETE",
    body: data,
  })
    .then((response) => response.json())
    .then((json) => {
      if (json.error) {
        let e = document.getElementById("output");
        e.innerHTML =
          `<div class="alert alert-danger mb-3" role="alert"><h3>Error</h3>${json.error}</div>` +
          e.innerHTML;
      }
    });
};

var Posting = function () {
  fetch("/subscribe", {
    method: "POST",
    body: data,
  })
    .then((response) => response.json())
    .then((json) => {
      if (json.error) {
        let e = document.getElementById("output");
        e.innerHTML =
          `<div class="alert alert-danger mb-3" role="alert"><h3>Error</h3>${json.error}</div>` +
          e.innerHTML;
      }
    });
};