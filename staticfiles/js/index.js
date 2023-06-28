async function getStats(endpoint, id) {
    URL = 'http://127.0.0.1:8000/api/'+endpoint;
    const response = await fetch(URL);
    const data = await response.json();
    console.log(data);
    document.getElementById(id).innerHTML = JSON.stringify(data, null, 2);
}
window.onload = function(){
    document.getElementById('searchButton').click();
    }

async function copyToClipboard() {
    var _searchField = document.getElementById("searchField");
    var copiedURL = 'http://127.0.0.1:8000/api/'+_searchField.value;
    navigator.clipboard.writeText(copiedURL);
    alert("Copied text: " + copiedURL.toString());
}

//  function that dynamically escapes the search field
function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}
