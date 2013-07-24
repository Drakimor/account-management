function validateForm()
{
var x=document.forms["provisionie"]["firstName"].value;
if (x==null || x=="")
  {
  alert("First name must be filled out");
  return false;
  }
var x=document.forms["provisionie"]["lastName"].value;
if (x==null || x=="")
  {
  alert("Last name must be filled out");
  return false;
  }
var x=document.forms["provisionie"]["personalEmail"].value;
var atpos=x.indexOf("@");
var dotpos=x.lastIndexOf(".");
if (atpos<1 || dotpos<atpos+2 || dotpos+2>=x.length)
  {
  alert("Not a valid e-mail address");
  return false;
  }
}