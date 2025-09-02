function r(n, k) {
  return Array.from({length:k-n}, (_,i)=>n+i)
}
function fact(n) {
  let t = 1;
  for (let t2 = n; t2 > 1; t2--) { t *= t2 }
  return t;
}
function jive() {
  //code execution
  out = "" ; s = [] ; p = 0
  i = document.getElementById("i").value.split("\n")
  code = document.getElementById("c").value
  while (p != code.length) {
           if (code[p] == "*") { s.push(i.shift())
    } else if (code[p] == "↓") { out += s.pop() + "\n"
    } else if (code[p] in "0123456789") { s.push(Number(code[p]))
    } else if (code[p] == "↑") { out += "["+s+"]"
    } else if (code[p] == ":") { while (code[p] !== ":" ) { p++ }
    } else if (code[p] == "!") { s.push(fact(s.pop()))
    } else if (code[p] == "[") { s.push( r( 1, Number( s.pop() + 1) ) ) }
    p++
  }
    document.getElementById("o").innerHTML = out //output the out variable
}
