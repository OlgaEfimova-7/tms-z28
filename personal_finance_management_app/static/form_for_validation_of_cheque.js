function add() {
  var new_chq_no = parseInt($('#total_chq').val()) + 1;
  var new_input = "<input type='text' id='new_" + new_chq_no + "'>";
  $('#new_chq').html(new_input);
}

function remove() {
  var last_chq_no = $('#total_chq').val();
  if (last_chq_no > 1) {
    $('#new_' + last_chq_no).append('');
    $('#total_chq').val(last_chq_no - 1);
  }
}
var counter = 1;
function addInput(divName, nameOfClass, name){
          var newdiv = document.createElement('div');
          newdiv.innerHTML = "<input type='text' name="+name+" class=" +nameOfClass+">";
          document.getElementById(divName).appendChild(newdiv);
          counter++;

}
function removeInput(removeLink) {
    var allChilds = document.getElementById(removeLink);
    allChilds.removeChild(allChilds.lastChild);
}