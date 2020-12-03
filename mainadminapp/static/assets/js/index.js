let country_id = selector.value;
 //sending ajax request to the view with id of selected country. Function is defined below.
 ajax_request(country_id);
 });


function ajax_request(id){
//creating new xhttp request.
 var xhttp = new XMLHttpRequest();
 xhttp.onreadystatechange = function() {
 if (this.readyState == 4 && this.status == 200) {
 //converting the response text to a javascript object.
 res = JSON.parse(this.responseText)
 cities = res.cities;
//Deleting all children of the City Selector, so that we only get the cities of selected country.
 removeChilds(document.getElementById('city'));
 for(const prop in cities){
 add_option(prop,cities[prop]);
 }
 }
 };
//sending ajax GET request to server with id of selected city.
 xhttp.open("GET", `/ajax_handler/${id}`, true);
 xhttp.send();
}


function add_option(val,text){
 var sel = document.getElementById('city');

 // create new option element
var opt = document.createElement('option');

// create text node to add to option element (opt)
opt.appendChild( document.createTextNode(text) );

// set value property of opt
opt.value = val;

 // add opt to end of select box (sel)
sel.appendChild(opt);
 }

}

var removeChilds = function (node) {
 var last;
//Delete every lastChild of the City Selector------- Delete all children
 while (last = node.lastChild) node.removeChild(last);
};
