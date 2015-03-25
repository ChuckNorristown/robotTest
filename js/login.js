
function Login() {

var password = 'robo-cop';

if (this.document.login.password.value == password) {
  top.location.href="index.html";
}
if (this.document.login.password.value == "") {
   alert("Please enter your password.");
   this.document.password.focus();
   return false;
  }
if (this.document.login.password.value != "robo-cop") {
   alert("Invalid password.");
   this.document.password.focus();
   return false;
  }
}
