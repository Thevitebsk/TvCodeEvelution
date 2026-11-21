function psm() {
  a = b = 0
    while (p<c.length){
      if (c[p] == "+") { a++ }
      else if (c[p] == "*") { [b,a]=[a,b] }
      else if (c[p] == "-") {
      if (a==0) { p=-1 } else { a-- }
      }
      else if (c[p] == "a") { o += a + " " }
      else if (c[p] == "b") { o += b + " " }
      p++; execs++
    }
  }
function gaia() {
    o=`Filename "${c}" doesn't seem to be a valid filename/commmand!`
}