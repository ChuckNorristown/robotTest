
function TheLogin() {

var password = 'roboCop';

if (this.document.login.password.value == password) {
  top.location.href="index.html";
}
if (this.document.login.password.value == "") {
   alert("Please enter your password.");
   this.document.password.focus();
   return false;
  }
if (this.document.login.password.value != "pacia1986") {
   alert("Invalid password.");
   this.document.password.focus();
   return false;
  }
}
