import React from "react";

const Guess = (props) => { 

  const {guesses, handler} = props

  const Validator = (event) => { 
    if (event.target.value.match( /[^a-z]/i) ){
      alert("Please enter a letter")
      event.preventDefault()
      return event.target.value = ''
    } 
    else if (guesses.includes(event.target.value.toLowerCase())) {
      alert(`${event.target.value} has already been guessed`)
      event.preventDefault()
      return event.target.value = ''
    }
  }
  
  return (
    <div>
      <form onSubmit={handler}>
        <label>
        Guess a letter
          <input type='text' size='1' maxLength={1} onChange={Validator}></input>
          <input type='submit' value='submit'></input>
        </label>
      </form>
    </div>
  )
}

export default Guess
