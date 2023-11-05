class main {
    
}

const value = document.querySelector("#value");
const input = document.querySelector("#radius");

input.addEventListener("input", (event) => {
  value.textContent = event.target.value;
});

function setDestinationVar() 
{
    // saves users input into intial and destination variables
    const nameInitial = document.getElementById("initial");
    const nameDestination = document.getElementById("destination");

}


function setFilterVar() 
{
    // saves users optional filters

    // PRICE
    price = document.getElementById("price");
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
    radius = document.getElementById("radius");
    // convert miles to meters
    radius = radius * 1609.34;

    // KEYWORD
    let keyword = document.getElementById("keyword");
    // if keyword is empty, default to "food"
    if(keyword == false)
    {
        keyword = "food";
    }

}
