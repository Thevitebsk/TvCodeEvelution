function main(){
  var code=document.getElementById("program")
  url=location.origin + location.pathname;
  if ( url!=location.href ) { code.value=decodeURIComponent(location.href.split("#")[1]) }
  var input=document.getElementById("input").value.split("\n")
  url=""
  code=code.value
  p=0; output=''; s=[]; ts=[]; /* m=0;*/
  num=["0","1","2","3","4","5","6","7","8","9"]
  while (code.length>p){
    //i will focus on the strings later
    //if (codev[p]=='"'){ m=1 ; p++ };
    //while (m==1){ ts.push(codev[p]) ; p++ ; if (codev[p+1]!=='"'){ break } }
    if (code[p]in num /*&& m==0*/){ s.push(code[p]) }
    else if (code[p]=="."){ if (s.length>0){ output += s.pop() } else { break } }
    else if (code[p]=="-"){if (s.length>0){ s.pop()} else { break } }
    //else if (code[p]=="\n"){ break }
    p++
  }
  if (code!=""){url="\nhttps://thevitebsk-github-io.vercel.app/true/ti.html#"+encodeURIComponent(code)}
  document.getElementById("console").innerHTML = output + '\nSTACK: [' + s + ']\nTEMPSTACK: [' + ts + ']\nBYTES: ' + code.length + url
}
