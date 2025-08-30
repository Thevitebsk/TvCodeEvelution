function langs() {
  o = "" ; p = 0
  l = document.getElementById("l").value
  c = document.getElementById("c").value
  if (l == "true") { bool1() }
  if (l == "+*-") { paml() }
  else if (l == "6") { six() }
  document.getElementById("o").innerHTML = "output:<br>" + o
}
function ti() {
  if (c == "ti!") { o = "Hello, world!\n" } 
  else { o = "[]\n" }
}
function paml() {
  a = b = tv = 0
  while (p<c.length) {
         if (c[p]=="+") { a++ }
    else if (c[p]=="*") { tv=a ; a=b ; b=tv ; tv=0 }
    else if (c[p]=="-") { a-- }
    else if (c[p]=="a") { o += a + " " }
    else if (c[p]=="b") { o += b + " " }
    p++
  }
}
function bool1() {
  s=[]
}
function six() { o = "6\n" }
function len() { document.getElementById("b").innerHTML = " " + document.getElementById("c").value.length + " bytes" }
