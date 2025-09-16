function localxml(filename){
    const xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", filename, false );
    xmlhttp.send();
    return xmlhttp.responseXML;
}


const xmlContent = xmlhttp.responseXML;


function gamerateTableRows(xml){
    let tablerows = "<tr><th>Title</th><th>Price</th></tr>";
    gamesElements = xml.getElementByTagName("games");

    for (let i = 0; i < gamesElements.length; i++) {
        const element = gamesElements[i];
        tablerows += 
        `
        <tr>
            <td>
                ${element.getElementByTagName("title")[0].childNodes[0].nodeValue}
            </td>
            <td>
                ${element.getElementByTagName("price")[0].childNodes[0].nodel}
            </td>
            <td>
                ${element.getElementByTagName("platform")[0].childNodes[0].nodel}
            </td>
        </tr>
        `   
    }
    return tablerows
}

document.getElementById("app").innerHTML = `<table id="xmlTable"></table>`;
document.getElementById("xmlTable").innerHTML = gamerateTableRows("scr/games.xml");
