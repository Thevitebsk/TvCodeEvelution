function langs() {
  p = 0;  o = ""
  l = document.getElementById("l").value
  c = document.getElementById("c").value
  if (l == "+*-") { paml() }
  else {ti()}
  document.getElementById("o").innerHTML = "output:<br>" + o
}
function ti() {
  o = `Hello, ${l} anitisipators!<br>
    Unfortunatly this language isn't allowrd to be used right now,
    i need to finish implementing ${l}
    <br><br>-ga`
}
function paml() {
  a = b = tv = 0
  for (x in c) {
    console.log(x)
         if (c[x] == "+") { a++ }
    else if (c[x] == "*") { [b,a]=[a,b] }
    else if (c[x] == "-") { a-- }
    else if (c[x] == "a") { o += a + " " }
    else if (c[x] == "b") { o += b + " " }
    p++
  }
}
function bool1() {
  s=[]
}
function len() { document.getElementById("b").innerHTML = document.getElementById("c").value.length + " bytes" }
