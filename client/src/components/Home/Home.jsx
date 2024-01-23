import React from 'react'
import './Home.css'
import Image from "./Image"
import Carousel from "react-multi-carousel";
import "react-multi-carousel/lib/styles.css";
import { productData, responsive } from "./data";
import Product from "./Product";

function Home() {
  const product = productData.map((item) => (
    <Product
      name={item.name}
      url={item.imageurl}
      price={item.price}
      description={item.description}
    />
  ));



  return (
    <div className="home">
      <h1>
        <marquee>
          {" "}
          <span className='span--1'> "Welcome To Keja Yangu ,</span> Your Comfort Our Priority"
        </marquee>
      </h1>

      <Carousel showDots={true} responsive={responsive}>
        {product}
      </Carousel>
    </div>
  );
}

export default Home
