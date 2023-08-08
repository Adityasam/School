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

function format_date(date, short = "S") {
  if (date.includes("T")) {
    date = date.split("T")[0];
  }
  if (date.includes(" ")) {
    date = date.split(" ")[0];
  }
  if (date != null && date != "") {
    var spl = date.split("-");
    if (spl.length > 0) {
      var year = spl[0];
      var month = spl[1];
      var day = spl[2];

      year = year.toString();
      if (short == "S") {
        return (
          ("0" + day).slice(-2) +
          "/" +
          ("0" + month).slice(-2) +
          "/" +
          year.substring(year.length - 2)
        );
      } else {
        return (
          ("0" + day).slice(-2) + "/" + ("0" + month).slice(-2) + "/" + year
        );
      }
    } else {
      return "";
    }
  } else {
    return "--/--/----";
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

function get_bank_name(code) {
  var name = "";
  for (var i = 0; i < bankname.length; i++) {
    if (bankcode[i] == code) {
      name = bankname[i];
    }
  }

  return name;
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
  } else {
    return "0";
  }
}

function AMPM(time) {
  var hour = parseInt(time.substr(0, 2));
  var minute = time.substr(3, 2);
  var ampm = hour >= 12 ? "PM" : "AM";
  hour = hour % 12;
  hour = hour ? hour : 12;
  return ("0" + hour).slice(-2) + ":" + ("0" + minute).slice(-2) + " " + ampm;
}

// Function to compress an image file
function compressImage(
  file,
  maxWidth,
  maxHeight,
  quality,
  callback,
  usercode = ""
) {
  var img = new Image();
  var reader = new FileReader();

  // When the image is loaded, perform the compression
  img.onload = function () {
    var canvas = document.createElement("canvas");
    var ctx = canvas.getContext("2d");

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
    var dataURL = canvas.toDataURL("image/jpeg", quality / 100);
    callback(dataURL);
  };

  // Read the image file and load it into the image object
  reader.onload = function (event) {
    img.src = event.target.result;
  };
  reader.readAsDataURL(file);
}

// Function to convert a data URL to a file object
function dataURLtoFile(dataURL, fileName) {
  var arr = dataURL.split(",");
  var mime = arr[0].match(/:(.*?);/)[1];
  var bstr = atob(arr[1]);
  var n = bstr.length;
  var u8arr = new Uint8Array(n);
  while (n--) {
    u8arr[n] = bstr.charCodeAt(n);
  }
  var blob = new Blob([u8arr], { type: mime });
  return new File([blob], fileName, { type: mime });
}

function delete_item(id, table, permanent = "0") {
  var data = new FormData();
  data.append("id", id);
  data.append("table", table);
  if (permanent == "0") {
    send_ajax_data("delete_item", data);
  } else {
    send_ajax_data("permanent_delete", data);
  }
}

function add_commas(num) {
  var formattedNumber = "";
  num = parseFloat(num);
  try {
    var options = { style: "decimal", maximumFractionDigits: 2 };
    formattedNumber = num.toLocaleString("en-US", options);
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

function getDayOnDate(date) {
  var ndate = new Date(date);
  var weekday = ndate.getDay();

  var days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
  return days[weekday];
}

function response_to_url(response_data, filename) {
  // Decode the Base64-encoded content to a byte array
  var byteCharacters = atob(response_data);

  // Convert the byte array to a typed array
  var byteNumbers = new Array(byteCharacters.length);
  for (var i = 0; i < byteCharacters.length; i++) {
    byteNumbers[i] = byteCharacters.charCodeAt(i);
  }
  var byteArray = new Uint8Array(byteNumbers);

  // Create a Blob from the byte array and the MIME type
  var blob = new Blob([byteArray], { type: "application/pdf" });
  const file = new File([blob], filename, { type: "application/pdf" });

  if (document.getElementById(filename.replace(".pdf", "")) === null) {
    var newfile = document.createElement("input");
    newfile.type = "file";
    newfile.hidden = true;
    var dt = new DataTransfer();
    dt.items.add(file);
    newfile.files = dt.files;
    document.getElementById("offercontainer").appendChild(newfile);
    newfile.id = filename.replace(".pdf", "");
  } else {
    var newfile = document.getElementById(filename.replace(".pdf", ""));
    newfile.remove();

    var newfile = document.createElement("input");
    newfile.type = "file";
    newfile.hidden = true;
    var dt = new DataTransfer();
    dt.items.add(file);
    newfile.files = dt.files;
    document.getElementById("offercontainer").appendChild(newfile);
    newfile.id = filename.replace(".pdf", "");
  }

  // Create a download link and click it to download the file
  return window.URL.createObjectURL(blob);
}

function towords(number) {
  const words = [
    "",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen",
  ];
  const tensWords = [
    "",
    "",
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety",
  ];

  let rupee = Math.floor(number);
  let paisa = Math.round((number - rupee) * 100);

  let rupeeWords = "";
  if (rupee >= 1000) {
    rupeeWords += words[Math.floor(rupee / 1000)] + " Thousand ";
    rupee %= 1000;
  }
  if (rupee >= 100) {
    rupeeWords += words[Math.floor(rupee / 100)] + " Hundred ";
    rupee %= 100;
  }
  if (rupee >= 20) {
    rupeeWords += tensWords[Math.floor(rupee / 10)] + " ";
    rupee %= 10;
  }
  if (rupee > 0) {
    rupeeWords += words[rupee] + " ";
  }
  rupeeWords += "Rupees ";

  let paisaWords = "";
  if (paisa > 0) {
    paisaWords += "and " + words[paisa] + " Paisa";
  } else {
    paisaWords = "and Zero Paisa";
  }

  return rupeeWords + paisaWords;
}

function convert_monthyear(monthyear) {
  var split = monthyear.split("-");
  if (split.length > 1) {
    var months = [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ];
    var month = parseInt(split[1]);
    return months[month - 1] + "-" + split[0];
  } else {
    return "";
  }
}

function get_principal(){
  var data = new FormData();
  var list = load_ajax_data("/get_principal", data);
  return list;
}

function get_section(classid, drop, fun="") {
  var data = new FormData();
  data.append("classid", classid);
  var list = load_ajax_data("get_class_section", data);

  var parent = drop.parentElement;
  if (list.length == 0) {
    parent.getElementsByClassName("search_input")[0].value = "N/A";
    parent.getElementsByClassName("search_input")[0].classList.add("p-n");
  } else {
    parent.getElementsByClassName("search_input")[0].value = "";
    parent.getElementsByClassName("search_input")[0].classList.remove("p-n");
  }

  parent.getElementsByClassName("search_input")[0].setAttribute("data-id", "");

  drop.innerHTML = "";
  for (var i = 0; i < list.length; i++) {
    var div = document.createElement("div");
    div.className = "option_item";
    div.innerHTML = list[i]["title"];
    div.setAttribute("data-id", list[i]["id"]);
    if(fun!=""){
      div.setAttribute("data-fun", fun);
    }else{
      div.setAttribute("data-fun", "change_section");
    }
    div.onclick = function () {
      click_drop();
    };

    drop.appendChild(div);
  }
}

function makeid(length) {
  var result = "";
  var characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  var charactersLength = characters.length;
  for (var i = 0; i < length; i++) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
}

var MNTH = [
  "Jan",
  "Feb",
  "Mar",
  "Apr",
  "May",
  "Jun",
  "Jul",
  "Aug",
  "Sep",
  "Oct",
  "Nov",
  "Dec",
];
function convert_month(month) {
  var spl = month.split("-");
  if (spl.length <= 1) {
    return "";
  }
  var year = spl[0];
  var mo = parseInt(spl[1]);

  return MNTH[mo] + "-" + year;
}

function calculateDistance(lat1, lon1, lat2, lon2) {
  const earthRadius = 6371; // in kilometers

  // Convert latitude and longitude to radians
  const lat1Rad = toRadians(lat1);
  const lon1Rad = toRadians(lon1);
  const lat2Rad = toRadians(lat2);
  const lon2Rad = toRadians(lon2);

  // Calculate the differences between coordinates
  const latDiff = lat2Rad - lat1Rad;
  const lonDiff = lon2Rad - lon1Rad;

  // Apply Haversine formula
  const a =
    Math.sin(latDiff / 2) ** 2 +
    Math.cos(lat1Rad) *
      Math.cos(lat2Rad) *
      Math.sin(lonDiff / 2) ** 2;

  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  const distance = earthRadius * c *1000;

  return distance;
}

// Helper function to convert degrees to radians
function toRadians(degrees) {
  return (degrees * Math.PI) / 180;
}
