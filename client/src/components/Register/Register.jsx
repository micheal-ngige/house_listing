import React from 'react'
import "./Register.css"

function Register() {
  return (
    <div className="register--container">
      <form className="register--form">
        <label>Username</label>
        <br />
        <input className="input--field" type="text" placeholder="username" />
        <br />
        <label>Password</label>
        <br />
        <input
          className="input--field"
          type="password"
          placeholder="password"
        />
        <br />
        <label>Confirm password</label>
        <br />
        <input
          className="input--field"
          type="password"
          placeholder="confirm password"
        />
        <br />
        <button className="submit--field" type="submit">
          Submit
        </button>
      </form>
    </div>
  );
}

export default Register
