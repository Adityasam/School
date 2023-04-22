var INR = "&#8377";

function send_ajax_data(path, data) {
  var returndata = null;
  $.ajax({
    url: path,
    type: "POST",
    processData: false,
    contentType: false,
    data: data,
    async: false,
    dataType: "json",
    success: (data) => {
      returndata = data;
    },
    error: (error) => {
      console.log(error);
    },
  });

  return returndata;
}

function load_ajax_data(path, data = null) {
  returndata = null;
  $.ajax({
    url: path,
    type: "POST",
    processData: false,
    contentType: false,
    data: data,
    async: false,
    dataType: "json",
    success: (data) => {
      returndata = data;
    },
    error: (error) => {
      console.log(error);
    },
  });

  return returndata;
}

function format_date(date, short="S") {
  if (date != null) {
    var spl = date.split("-");
    if (spl.length > 0) {
      var year = spl[0];
      var month = spl[1];
      var day = spl[2];

      year = year.toString()
      if(short == "S"){
      return ("0" + day).slice(-2) + "/" + ("0" + month).slice(-2) + "/" + year.substring(year.length-2);
      }else{
        return ("0" + day).slice(-2) + "/" + ("0" + month).slice(-2) + "/" + year;
      }
    } else {
      return "";
    }
  } else {
    return "";
  }
}

function clean_temp(temp) {
  var clone = temp.cloneNode(true);
  clone.removeAttribute("id");
  clone.hidden = false;
  return clone;
}

function save_file(file) {
  var data = new FormData();
  data.append("myfile", file);
  var name = send_ajax_data("save_file", data);
  return name;
}

function url_to_file(url, inp, fun = null, fileName = "") {
  var spl = url.split(".");
  var ext = spl[spl.length - 1];

  if (fileName == "") {
    fileName = "defaultFile";
  }
  fileName = fileName + "." + ext;

  fetch(url)
    .then(async (response) => {
      const contentType = response.headers.get("content-type");
      const blob = await response.blob();
      const file = new File([blob], fileName, { contentType });

      var data = new DataTransfer();
      data.items.add(file);
      inp.files = data.files;

      if (fun != null) {
        window[fun]();
      }
    })
    .catch((err) => console.log(err));
}

function set_banks(block) {
  block.innerHTML = "";
  for (var i = 0; i < bankname.length; i++) {
    var div = document.createElement("div");
    div.classList.add("option_item");
    div.setAttribute("data-id", bankcode[i]);
    div.innerHTML = bankname[i];
    block.appendChild(div);

    div.onclick = function () {
      click_drop();
    };
  }
}

function change_status() {
  var parent = event.target.parentElement;
  $(parent).find(".status_btn").removeClass("active");
  event.target.classList.add("active");
  load_local();
}

function get_age(dob) {
  if (dob != "") {
    // specify the two dates as strings
    const date1Str = dob;

    // create Date objects from the strings
    const date1 = new Date(date1Str);
    const date2 = new Date();

    // calculate the difference in years
    const yearDiff = date2.getFullYear() - date1.getFullYear();
    return yearDiff;
  }else{
    return "0";
  }
}

function AMPM(time) {
  var hour = parseInt(time.substr(0, 2));
  var minute = time.substr(3, 2);
  var ampm = hour >= 12 ? 'PM' : 'AM';
  hour = hour % 12;
  hour = hour ? hour : 12;
  return ("0"+hour).slice(-2) + ':' + ("0"+minute).slice(-2) + ' ' + ampm;
}


// Function to compress an image file
function compressImage(file, maxWidth, maxHeight, quality, callback) {
  var img = new Image();
  var reader = new FileReader();

  // When the image is loaded, perform the compression
  img.onload = function() {
    var canvas = document.createElement('canvas');
    var ctx = canvas.getContext('2d');

    // Determine the new dimensions of the image
    var width = img.width;
    var height = img.height;
    if (width > maxWidth) {
      height *= maxWidth / width;
      width = maxWidth;
    }
    if (height > maxHeight) {
      width *= maxHeight / height;
      height = maxHeight;
    }

    // Set the dimensions of the canvas
    canvas.width = width;
    canvas.height = height;

    // Draw the image onto the canvas
    ctx.drawImage(img, 0, 0, width, height);

    // Convert the canvas to a data URL and call the callback function
    var dataURL = canvas.toDataURL('image/jpeg', quality / 100);
    callback(dataURL);
  };

  // Read the image file and load it into the image object
  reader.onload = function(event) {
    img.src = event.target.result;
  };
  reader.readAsDataURL(file);
}

// Function to convert a data URL to a file object
function dataURLtoFile(dataURL, fileName) {
  var arr = dataURL.split(',');
  var mime = arr[0].match(/:(.*?);/)[1];
  var bstr = atob(arr[1]);
  var n = bstr.length;
  var u8arr = new Uint8Array(n);
  while(n--) {
    u8arr[n] = bstr.charCodeAt(n);
  }
  var blob = new Blob([u8arr], {type: mime});
  return new File([blob], fileName, {type: mime});
}

function delete_item(id, table, permanent="0"){
  var data = new FormData();
  data.append("id", id);
  data.append("table", table);
  if(permanent == "0"){
    send_ajax_data("delete_item", data);
  }else{
    send_ajax_data("permanent_delete", data);
  }
}

function add_commas(num) {
  var formattedNumber = "";
  num = parseFloat(num);
  try {
      var options = { style: 'decimal', maximumFractionDigits: 2 };
      formattedNumber = num.toLocaleString('en-US', options);
  } catch (err) {
      console.log(err);
  }
  if (formattedNumber == "NaN") {
      formattedNumber = "0.00";
  }
  return formattedNumber;
}

function getDaysInMonth(year, month) {
  return new Date(year, month, 0).getDate();
}