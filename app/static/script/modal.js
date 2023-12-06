var Workflows = function () {
  let divisionRecordsNumber = document.getElementById("divisionRecordsNumber").value;
  let crimeCode = document.getElementById("crimeCode").value;
  let area = document.getElementById("area").value;

  // var data = new FormData();

  // data.append("divisionRecordsNumber", divisionRecordsNumber);
  // data.append("crimeCode", crimeCode);
  // data.append("area", area);
  // timeOccured = document.getElementById("timeOccured").value;
  // let lat = document.getElementById("lat").value;
  // let lon = document.getElementById("lon").value;
  // let crimeCode = document.getElementById("crimeCode").value;
  // let weaponUsedCode = document.getElementById("weaponUsedCode").value;
  // let moCodes = document.getElementById("moCodes").value;
  // let area = document.getElementById("area").value;
  // let premisesCode = document.getElementById("premisesCode").value;
  fetch(`/crimeDescription/${divisionRecordsNumber}/${crimeCode}/${area}`, {
    method: "GET",
  })
    .then((response) => response.json())
    .then((json) => {
      if (json.error) {
        let e = document.getElementById("output");
        e.innerHTML =
          `<div class="alert alert-danger mb-3" role="alert"><h3>Error</h3>${json.error}</div>` +
          e.innerHTML;
      } else {
        document
          .getElementById("CrimeDescription")
          .getElementsByTagName("tbody")[0].innerHTML = "";

        var tableRow = `<thead></thead><tr><td>divisionRecordsNumber</td><td>dateReported</td><td>dateOccurred</td>><td>timeOccured</td><td>lat</td><td>lon</td>><td>crimeCode</td><td>weaponUsedCode</td><td>area</td><td>premisesCode</td></tr></thead>`;
        document
            .getElementById("CrimeDescription")
            .getElementsByTagName("tbody")[0].innerHTML += tableRow;

        // Append rows to the tbody
        for (var each in json) {
          var item = json[each];
          var tableRow = `<tr><td>${item.divisionRecordsNumber}</td><td>${item.dateReported}</td><td>${item.dateOccurred}</td>><td>${item.timeOccured}</td><td>${item.lat}</td><td>${item.lon}</td>><td>${item.crimeCode}</td><td>${item.weaponUsedCode}</td><td>${item.area}</td><td>${item.premisesCode}</td></tr>`;
          document
            .getElementById("CrimeDescription")
            .getElementsByTagName("tbody")[0].innerHTML += tableRow;
        }
      }
    });
};

var Deleting = function () {
  let DescriptionIdDeletion = document.getElementById(
    "DescriptionIdDeletion"
  ).value;

  var data = new FormData();

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
  let divisionRecordsNumber = document.getElementById("divisionRecordsNumber").value;
  let dateReported = document.getElementById("dateReported").value;
  let dateOccurred = document.getElementById("dateOccurred").value;
  let timeOccured = document.getElementById("timeOccured").value;
  let lat = document.getElementById("lat").value;
  let lon = document.getElementById("lon").value;
  let crimeCode = document.getElementById("crimeCode").value;
  let weaponUsedCode = document.getElementById("weaponUsedCode").value;
  let moCodes = document.getElementById("moCodes").value;
  let area = document.getElementById("area").value;
  let premisesCode = document.getElementById("premisesCode").value;
  
  var data = new FormData();

  data.append("divisionRecordsNumber", divisionRecordsNumber);
  data.append("dateReported", dateReported);
  data.append("dateOccurred", dateOccurred);
  data.append("timeOccured", timeOccured);
  data.append("lat", lat);
  data.append("lon", lon);
  data.append("crimeCode", crimeCode);
  data.append("weaponUsedCode", weaponUsedCode);
  data.append("moCodes", moCodes);
  data.append("area", area);
  data.append("premisesCode", premisesCode);


  fetch(`/crimeDescription/insert`, {
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

var Updating = function () {
  let divisionRecordsNumber = document.getElementById(
    "divisionRecordsNumber"
  ).value;

  let lat2 = document.getElementById("lat2").value;
  let lon2 = document.getElementById("lon2").value;

  var data = new FormData();
  data.append("divisionRecordsNumber", divisionRecordsNumber);

  data.append("lat2", lat2);
  data.append("lon2", lon2);

  fetch(`/crimeDescription/update`, {
    method: "PUT",
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

function submitForm() {
  // Get values from input fields
  var crimeCode = document.getElementById('crimeCodemap').value;
  var area = document.getElementById('areamap').value;
  var limit = document.getElementById('limitmap').value;

  // Construct the URL
  var url = `/generateMap/${crimeCode}/${area}/${limit}`;

  // Redirect the user to the constructed URL
  window.location.href = url;
};