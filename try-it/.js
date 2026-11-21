function run() {
  execs = p = 0; o = ""
  l = document.getElementById("l").value
  c = document.getElementById("c").value+" "
  max = Number(document.getElementById("max").value)
  document.getElementById("o").innerHTML = "output:<br>" + o
  funcs={
    "+*-":"psm()"
  }
  eval(funcs[l])
}
function bool1() {
  s=[]
}
function len() {
  document.getElementById("b").innerHTML = document.getElementById("c").value.length + " bytes"
}
/*
just relised that there is no "con" function in this site...
i'll add this function later
if (L=window.location.href.split("?")[1]){ con(L) }
*/
len()