console.log("test")
var x=false;
  function exchange1(e)  {
    console.log(e);
  x=true;
  let start = document.getElementById("start");
  let end = document.getElementById("end");
  let val1=start.value;
  let val2=end.value;
  sessionStorage.setItem("val1",val1)
  sessionStorage.setItem("val2",val2)
}
    let b = document.getElementById("bt_ch");
    b.addEventListener("click",exchange1);
if(x)
{
  sessionStorage.setItem("val1",val1)
  sessionStorage.setItem("val2",val2)
  value1 = sessionStorage.getItem("val1")
  value2 = sessionStorage.getItem("val2")
  console.log(value1)
  console.log(value2)
 let f = document.querySelector("form");
 let bet = document.createElement("h3");
 let inp1 = document.createElement("start");
 let inp2 = document.createElement("end");
  bet.innerHTML="<center>"+value1+" between "+value2+"</center>"
  f.replaceChild(bet,inp1);
  inp2.parentNode.removeChild(inp2);
}