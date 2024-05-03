document.addEventListener("keydown", handleKeyPress);

  function handleKeyPress(event) {
    if (event.key === '1') {
        event.preventDefault();
        window.location.href = "ListFicheros.html";
    } else if (event.key === '2') {
        event.preventDefault();
        window.location.href = "ComMatPr.html";
    } else if (event.key === '3') {
        event.preventDefault();
        window.location.href = "EntMatPr.html";
    } else if (event.key === '4') {
        event.preventDefault();
        window.location.href = "Fabricacion.html";
    } else if (event.key === '5') {
        event.preventDefault();
        window.location.href = "Facturacion.html";
    } else if (event.key === '6') {
        event.preventDefault();
        window.location.href = "EntInvent.html";
    } else if (event.key === '7') {
        event.preventDefault();
        window.location.href = "EscandalloForm.html";
    } else if (event.key === '8') {
        event.preventDefault();
        window.location.href = "MPaFijar.html";
    } else if (event.key === '9') {
        event.preventDefault();
        window.location.href = "MantFicheros.html";
    }
  } 