async function predictTime() {

    const garment = document.getElementById("garment_type").value;
    const quantity = document.getElementById("order_quantity").value;
    const operations = document.getElementById("operations").value;

    const prediction = document.getElementById("prediction");

    if (
        garment === "" ||
        quantity === "" ||
        operations === ""
    ){
        prediction.innerHTML =
        "<span class='error'>Please fill all fields.</span>";
        return;
    }

    prediction.innerHTML =
    "<span class='loading'>Predicting...</span>";

    try{

        const response = await fetch("/predict",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                garment_type:garment,
                order_quantity:Number(quantity),
                num_stitch_operations:Number(operations)

            })

        });

        const data = await response.json();

        prediction.innerHTML = `
            Estimated Sewing Time<br><br>
            <strong>${data.predicted_time} Minutes</strong>
        `;

    }

    catch(error){

        prediction.innerHTML =
        "<span class='error'>Prediction Failed!</span>";

        console.log(error);

    }

}