
function theLogin() {

var password = 'roboCop';

if (this.document.login.password.value == password) {
  top.location.href="home.html";
}
if (this.document.login.password.value == "") {
   alert("Please enter your password.");
   this.document.password.focus();
   return false;
  }
if (this.document.login.password.value != "roboCop") {
   alert("Invalid password.");
   this.document.password.focus();
   return false;
  }
}
