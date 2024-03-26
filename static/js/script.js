function showDiv(opt) {
  console.log("hi");

  test = ["test1", "test2", "test3", "test4"];
  ex = ["ex1", "ex2", "ex3", "ex4"];
  for (i = 0; i < test.length; i++) {
    if (opt == test[i]) {
     document.getElementById(ex[i]).style.display = "block"; 
    } else {
      document.getElementById(ex[i]).style.display = "none";
    }
  }
}
