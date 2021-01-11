let calculate = document.getElementById("calculation");
let qaunt = document.getElementById("quantity");
let count = document.getElementById("buttonCountNumber");
calculation = document.getElementById("calculation").innerHTML;

document.getElementById("buttonCountPlus").onclick = function() {
  let countPlus = count.innerHTML;
  if(+countPlus <= 10){
    count.innerHTML++;
    qaunt.value = Number.parseInt(qaunt.value) + 1;
    let countPlus = count.innerHTML;
    
    // calculate.innerHTML = calculations(countPlus) ;
  }
}

document.getElementById("buttonCountMinus").onclick = function() {
  let countMinus = count.innerHTML;
  if(+countMinus >= 2){
    count.innerHTML--;
    qaunt.value = Number.parseInt(qaunt.value) - 1;
    let countMinus = count.innerHTML;
    // calculate.innerHTML = calculations(countMinus) ;
  }
}

calculations = (count) => {
  return calculation+` * ${count} = ` + (+count)*(+calculation);
}