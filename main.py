from pyscript import display, document

def clubcheck (e):
    firstnames = ["Jericho", "Jericho2", "Jericho3", "Jericho4", "Jericho5"]
    lastnames = ["Magsalin", "Magsalin2", "Magsalin3", "Magsalin4", "Magsalin5"]

    document.getElementById("output").innerHTML = "" # clears previous output
    fname = document.getElementById('firstname').value
    lname = document.getElementById('lastname').value

    check = "Jericho" in document.getElementById('firstname').value
    display(check)