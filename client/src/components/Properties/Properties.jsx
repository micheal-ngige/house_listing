import React from 'react'
import { useEffect, useState } from 'react'

function Properties() {
const[properties, setProperties]=useState([])

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("http://127.0.0.1:5000/house");
      const data = await response.json();
      console.log(data)
      console.log("yes")
      setProperties(data);
    };
    fetchData();
  }, []);


  return (
    <div>
      <h1>Properties</h1>
      <div className="properties--1">
        {properties.map((property) => (
          <div className="item" key={property.housetype}>
            {/* <img
              src="../src/assets/img/e-commerce/product/product-3.jpg"
              className="image"
            /> */}
            <h4>Location: {property.location}</h4>
            <h4>Price: {property.price}</h4>
            <h4>Description: {property.description}</h4>           
            <button className='seemore--btn'>
              see more
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Properties
