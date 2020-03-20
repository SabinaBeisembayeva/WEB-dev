var input = document.getElementById('input');
var list = document.getElementById('list');
var tasks = [];
var i = -1;

window.onload = function() {

   document.getElementById('button').onclick = function() {
     if(input.value != '') {
       tasks.push(input.value);
       i++;
       list.innerHTML += item();
       input.value = '';

     }
   }
}

function item() {
  return `<div class="item" id='${i}'>
            <div class="inputBox">
              <input id = '${i}' type="checkbox" name="" value="" onclick = "toggleCross(${i})">
              <p id="input_name_${i}">${input.value}</p>
            </div>
            <img class="trash" id='${i}' src="./img.png" alt="trash" onclick="remove(${i})">
          </div>`
}

function remove(index) {
  var current = document.getElementById(index);
  current.style.display = "none";
}

function toggleCross(index) {
  var temp = document.getElementById('input_name_' + index);
  if(temp.classList.length == 0)
    temp.classList.add('cross');
  else
    temp.classList.remove('cross');
}
