async function GetProducts() {
    let Data = await axios.get("http://127.0.0.1:8000/Products/List/");
    let List = Data.data.List;
    Display(List);
}


function BuyNow(Id)
{
    alert(Id)
}




function Display(List) {
    let Main = document.getElementsByTagName("main")[0];
    Main.innerHTML = "";
    for (let i = 0; i < List.length; i++) {
        Main.innerHTML += `
        <div class="ProductCard">
            <img src="media/${List[i].Image}" class="card-img-top" alt="${List[i].Name}">
            <div class="card-body">
                <h5 class="card-title">${List[i].Name}</h5>
                    <a href="ProductDetail/${List[i].id}">
                            <button class="btn btn-primary">View Details</button>
                        </a>                <p class="card-text">${List[i].Description}</p>
                <p class="card-text"><strong>Price:</strong> ${List[i].Price}</p>
                <p class="card-text"><strong>Category:</strong> ${List[i].Category}</p>
            </div>
        </div>
        `;
    }
}

function Delete(id) {
    // Implement the delete functionality
    console.log(`Deleting product with id: ${id}`);
}

function Edit(id) {
    // Implement the edit functionality
    console.log(`Editing product with id: ${id}`);
}

GetProducts();