$(".opbtn").on("click", function () {
  var value = "";
  var parent = event.target.parentElement;
  if (parent.classList.contains("multi")) {
    $(event.target).toggleClass("active");
    var options = parent.getElementsByClassName("opbtn");
    for (var i = 0; i < options.length; i++) {
      value += options[i].getAttribute("data-id") + "^";
    }
  } else {
    $(parent).find(".opbtn").removeClass("active");
    $(event.target).addClass("active");
    value = event.target.getAttribute("data-id");
  }

  parent.setAttribute("data-id", value);
});

$(".search_input").on("focus", function () {
  $(".custom_dropdown").removeClass("active");
  var parent = event.target.parentElement;
  $(parent).addClass("active");
});

$(".search_input").on("focusout", function () {
  if (event.target.getAttribute("data-id") == "") {
    event.target.value = "";
  }
  if (event.target.value == "") {
    event.target.setAttribute("data-id", "");
  }
});

$(document).on("click", function () {
  if (
    !event.target.classList.contains("custom_dropdown") &&
    !event.target.classList.contains("optionblock") &&
    !event.target.classList.contains("search_input")
  ) {
    if (!event.target.parentElement.classList.contains("multi")) {
      $(".custom_dropdown").removeClass("active");
    }
  }
});

function search_drop() {
  var value = event.target.value.trim().toLowerCase();
  var parent = event.target.parentElement;
  var ops = parent.getElementsByClassName("option_item");
  for (var i = 0; i < ops.length; i++) {
    var v = ops[i].innerHTML.trim().toLowerCase();
    if (v.includes(value)) {
      ops[i].hidden = false;
    } else {
      ops[i].hidden = true;
    }
  }
}

$(".search_input").on("keyup", function () {
  search_drop();
});

function click_drop() {
  var parent = event.target.parentElement.parentElement;
  var opblock = parent.getElementsByClassName("optionblock")[0];

  if (!opblock.classList.contains("multi")) {
    $(opblock).find(".option_item").removeClass("active");
    event.target.classList.add("active");
  } else {
    if (event.target.classList.contains("active")) {
      event.target.classList.remove("active");
    } else {
      event.target.classList.add("active");
    }
  }

  var items = opblock.getElementsByClassName("option_item");
  var val = "";
  var name = "";
  for (var i = 0; i < items.length; i++) {
    if (items[i].classList.contains("active")) {
      var show_val = items[i].getAttribute("data-show");
      if (show_val != "undefined" && show_val != null) {
        name = show_val.trim();
      } else {
        name = items[i].innerHTML.trim();
      }
      val += items[i].getAttribute("data-id") + "^";
    }
  }

  var spl = val.split("^");
  spl = spl.slice(0, -1);
  if (spl.length == 0) {
    parent
      .getElementsByClassName("search_input")[0]
      .setAttribute("data-id", "");
    parent.getElementsByClassName("search_input")[0].value = "";
  } else if (spl.length == 1) {
    parent
      .getElementsByClassName("search_input")[0]
      .setAttribute("data-id", spl[0]);
    parent.getElementsByClassName("search_input")[0].value = name;
  } else if (spl.length > 1) {
    parent
      .getElementsByClassName("search_input")[0]
      .setAttribute("data-id", val);
    parent.getElementsByClassName("search_input")[0].value =
      spl.length + " items selected";
  }

  var fun = event.target.getAttribute("data-fun");
  if (fun != "undefined" && fun != null) {
    window[fun]();
  }
}

$(".option_item").on("click", function () {
  click_drop();
});

function set_drop_default() {
  var drops = document.getElementsByClassName("custom_dropdown");
  for (var i = 0; i < drops.length; i++) {
	$(drops[i]).find(".option_item").removeClass("active");
    var defvalue = drops[i]
      .getElementsByClassName("search_input")[0]
      .getAttribute("data-id");

    var spl = defvalue.split("^");
    spl = spl.slice(0, -1);
    var options = drops[i].getElementsByClassName("option_item");
    for (var j = 0; j < options.length; j++) {
      if (
        defvalue.includes(options[j].getAttribute("data-id")) &&
        !drops[i]
          .getElementsByClassName("search_input")[0]
          .classList.contains("EXC")
      ) {
        options[j].click();
      }
    }
  }

  var ops = document.getElementsByClassName("opbtn");
  for (var i = 0; i < ops.length; i++) {
    var defvalue = ops[i].parentElement.getAttribute("data-id");
    var options = ops[i].parentElement.getElementsByClassName("opbtn");
    for (var j = 0; j < options.length; j++) {
      if (options[j].getAttribute("data-id") == defvalue) {
        options[j].click();
      }
    }
  }
}

$(".custom_dropdown").append('<i class="fas fa-caret-down drop_caret"></i>');
$(".search_input").attr("autocomplete", "off");

function click_toggle(){
  $(event.target).toggleClass("active");
  if(event.target.classList.contains("active")){
    event.target.setAttribute("data-id", "1");
  }else{
    event.target.setAttribute("data-id", "0");
  }

  var fun = event.target.getAttribute("data-fun");
  if(fun !="undefined" && fun != null){
    window[fun]();
  }
}