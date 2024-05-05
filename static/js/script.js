function showDiv(opt) {
  test = ["test1", "test2", "test3", "test4"];
  ex = ["ex1", "ex2", "ex3", "ex4"];
  for (i = 0; i < test.length; i++) {
    if (opt == test[i]) {
      document.getElementById(ex[i]).style.display = "block";
    } else {
      document.getElementById(ex[i]).style.display = "none";
      document.getElementById("result").style.display = "none";
    }
  }
}
function checkout() {
  v = new XMLHttpRequest();
  v.open("POST", "/checkout", true);
  v.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  abc = "123";
  v.send("id=" + abc);
  v.onload = function () {
    if (v.status === 200) {
      window.location.reload();
    }
  };
}
setTimeout(function () {
  document.getElementById("message").style.display = "none";
}, 2000);

function add() {
  v = new XMLHttpRequest();
  v.open("POST", "/add", true);
  v.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  add = "123";
  v.send("id=" + add);
  v.onload = function () {
    if (v.status === 200) {
      window.location.reload();
    }
  };
}
function changeBox() {
  let opt = document.getElementById("list").value;
  if (opt == "add") {
    document.getElementById("listItem").style.display = "none";
  } else if (opt == "delete") {
    document.getElementById("textInput").style.display = "none";
    document.getElementById("listItem").style.display = "none";
  } else if (opt == "deleteitem") {
    document.getElementById("textInput").style.display = "none";
    document.getElementById("listItem").style.display = "block";
  } else if (opt == "") {
    alert("select something")
  } else {
    document.getElementById("textInput").style.display = "block";
    document.getElementById("listItem").style.display = "block";
  }
  
}
