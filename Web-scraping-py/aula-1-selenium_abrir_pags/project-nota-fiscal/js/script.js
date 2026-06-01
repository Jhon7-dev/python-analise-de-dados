function getXml() {
  var elements = document.forms.formulario.elements;
  var xmlTemplate = '<?xml version="1.0"?> <formData>';
  for (var i = 0; i < elements.length; i++) {
    var element = elements[i];
    if (element.tagName == "INPUT") {
      xmlTemplate =
        xmlTemplate +
        "<" +
        element.name +
        ">" +
        element.value +
        "</" +
        element.name +
        ">";
    }
    if (element.tagName == "SELECT") {
      xmlTemplate =
        xmlTemplate +
        "<" +
        element.name +
        ">" +
        element.value +
        "</" +
        element.name +
        ">";
    }
  }
  xmlTemplate = xmlTemplate + "</formData>";
  return xmlTemplate;
}

function download() {
  var element = document.createElement("a");
  text = getXml();
  element.setAttribute(
    "href",
    "data:text/plain;charset=utf-8," + encodeURIComponent(text),
  );
  element.setAttribute("download", "nota.xml");

  element.style.display = "none";
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}
