function handleSubmit(event)
{
    event.preventDefault();

    let initialLocation = setDestinationVar()[0];
    let destination = setDestinationVar()[1];
    let price = setFilterVar()[0];
    let radius = setFilterVar()[1];
    let keyword = setFilterVar()[2];

    const data = {initialLocation, destination, price, radius, keyword};

    console.log('/?' + new URLSearchParams(data));
    
    
}

const form = document.getElementById("form");
form.addEventListener("submit", handleSubmit);

const value = document.querySelector("#value");
const input = document.querySelector("#radius");

input.addEventListener("input", (event) => {
  value.textContent = event.target.value;
});

function setDestinationVar() 
{
    // saves users input into intial and destination variables
    const nameInitial = document.getElementById("initial").value;
    const nameDestination = document.getElementById("destination").value;
    return [nameInitial, nameDestination];
}


function setFilterVar() 
{
    // saves users optional filters

    // PRICE
    let price = document.getElementById("price").value;
    // convert $$ into int
    if(price == "$")
    {
        price = 1;
    }
    else if(price == "$$")
    {
        price = 2;
    }
    else if(price == "$$$")
    {
        price = 3;
    }
    else
    {
        price = 4;
    }

    // RADIUS
    let radius = document.getElementById("radius").value;
    // convert miles to meters
    radius = radius * 1609.34;

    // KEYWORD
    let keyword = document.getElementById("keyword").value;
    // if keyword is empty, default to "food"
    if(keyword == false)
    {
        keyword = "food";
    }
    
    return [price, radius, keyword]; 

}
