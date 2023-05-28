//search Function
function myFunction() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue,choose;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  choose = document.getElementById("choice")

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    if(choose.value == "id"){td = tr[i].getElementsByTagName("td")[0];}
    else if (choose.value == "DP") {td = tr[i].getElementsByTagName("td")[5];}
    else if (choose.value == "db") {td = tr[i].getElementsByTagName("td")[2];}

    else {td = tr[i].getElementsByTagName("td")[1];}

    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

function Active() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue,choose,status;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  choose = document.getElementById("choice")

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      status = tr[i].getElementsByTagName("td")[6].innerHTML;
      if(choose.value.toUpperCase() == status.toUpperCase()){
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
      } else {
          tr[i].style.display = "none";
      }
    }
    else{
      tr[i].style.display = "none";
    }
  }
  }
}


var statusName = "false";


//check while typing
//name-->Student , course
function nmValidation(){
  var name = document.getElementById("Name");
  if(name.value == "") {
    document.getElementById("nm-message").style.display = "block";
    statusName = "false";
  }
  else {
    document.getElementById("nm-message").style.display = "none";
    statusName = "true";
  }
}

//id
function idValidation(){
  var id = document.getElementById("id");
  if(id.value.length < 8 || isNaN(id.value)) {
    document.getElementById("id-message").style.display = "block";
  }
  else {
    document.getElementById("id-message").style.display = "none";
  }
}

//hall no. for course
function hallValidation(){
  var hall = document.getElementById("hall");
  if(hall.value.length < 1 || isNaN(hall.value)) {
    document.getElementById("hall-message").style.display = "block";

}
else {
  document.getElementById("hall-message").style.display = "none";
 }
}

//Birth Check > 18
function birthValidation(){
  var birth = document.getElementById("Birth");
  var now =new Date();                            //getting current date
     var currentY= now.getFullYear();                //extracting year from the date
     var dobget = birth.value;                          //getting user input
     var dob = new Date(dobget);                             //formatting input as date
     var prevY = dob.getFullYear();                          //extracting year from input date
     var ageY =currentY - prevY;
if (birth.value == "" || ageY < 18) {
  document.getElementById("birth-message").style.display = "block";

}
else {
  document.getElementById("birth-message").style.display = "none";
}
}

//universty name check
function uniValidation(){
  var universty = document.getElementById("universty");
if(universty.value == "") {
  document.getElementById("un-message").style.display = "block";
}
else {
  document.getElementById("un-message").style.display = "none";
}
}

//email check
// function emailValidation(){
//   var email = document.getElementById("email");
//   var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

//   if(email.value.match(mailformat)) {
//     document.getElementById("e-message").style.display = "none";
//     statusEmail = "true";
//   }
//   else {
//     document.getElementById("e-message").style.display = "block";
//     statusEmail = "false";
//   }
// }

//psw check
function pswValidation(){
  var psw = document.getElementById("psw");
     if(psw.value.length < 6) {
       document.getElementById("psw-message").style.display = "block";
       statusPsw = "false";
     }
     else {
       document.getElementById("psw-message").style.display = "none";
       statusPsw = "true";
     }
   }


// login Validation
function loginValidation() {
     if (statusPsw == "true" && statusName == "true"){
       return true;
    }
     else {
       document.getElementById("e-message").style.display = "block";
       document.getElementById("psw-message").style.display = "block";
       return false;
     }
   }



//Validate -> add Student or edit
function Add(){  
  var name = document.getElementById("Name").value;
  var id = document.getElementById("id").value;
  var birth = document.getElementById("Birth").value;
  var uni = document.getElementById("universty").value;
  var course1 = document.getElementById("course1");
  var course2 = document.getElementById("course2");
  var course3 = document.getElementById("course3");

  if(name!=""&&id!=""&&birth!=""&&uni!=""){

      if(course1.value != course2.value && course1.value != course3.value && course2.value != course3.value){
        alert("Done Successfully");
        return true
      }
      else{
        alert("Please choose uniqe course in each field");
        return false
      }
    }
    else{
        alert("Please Fill the Form");
        return false
      }
    }

// register course
function register(){
  var name = document.getElementById("Name").value;
  var id = document.getElementById("id").value;
  var course1 = document.getElementById("course1");
  var course2 = document.getElementById("course2");
  var course3 = document.getElementById("course3");
  if(name!=""&&id!=""){
    if(course1.value != course2.value && course1.value != course3.value && course2.value != course3.value){
      alert("Done Successfully");
      return true
    }
    else{
      alert("Please choose uniqe course in each field");
      return false
    }
  }
  else{
      alert("Please Fill the Form");
      return false
    }
}



//Add,edit course
function validate(){
  var name = document.getElementById("Name").value;
  var id = document.getElementById("id").value;
  var hall = document.getElementById("hall").value;

  if(name != "" && id != "" &&hall != ""){
    let x = confirm('Are you sure?');
    if(x == true){
      alert("Done Successfully");
      return true
  }
  else{
    return false
  }
  }
  else{
    alert("Please Fill the Form");
    return false
  }
}


//delet row
function deleteRow(rowID) {
  let x = confirm("Are you sure you want to delet the row?");
  if(x == true){
    return true;
  }
}

$(document).ready(function(){
$(document).on("click",'#delete',function(e){
  e.preventDefault();
  var $this = $(this);
  x = confirm("Are you sure you want to delet this student?")
  if(x){
    $.ajax({
      url: $this.attr('href'),
      type: 'POST',
      datdaType: 'json',
      data:{csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
      success: function(resp) {
          $this.parents('.record').fadeOut("slow",function(){
            $this.parents('.record').remove();
          });
      },
      });
  }
})
})

$(document).ready(function(){
$(document).on("click",'#deleteCourse',function(e){
  e.preventDefault();
  var $this = $(this);
  x = confirm("Are you sure you want to delet this course?")
  if(x){
    $.ajax({
      url: $this.attr('href'),
      type: 'POST',
      datdaType: 'json',
      data:{csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
      success: function(resp) {
        if(resp.messages === "success"){
          $this.parents('.record').fadeOut("slow",function(){
            $this.parents('.record').remove();
          });
        }
      },
      });
  }
})
})