import React, { useState } from 'react'
import './App.css';

function App() {
  const [input , setInput] = useState('')
  const [palBool, setPalBool] = useState(false)

  const handleChange = (evt) => {
    evt.preventDefault()
    setInput(evt.target.value)
  }

  const isPalindrome = (evt) => {
    evt.preventDefault()
    const palindrome = evt.target.palindrome.value
    return reverseWord(palindrome.toLowerCase())
  }

  const reverseWord = (word) => {
    word = word.replace(/\s/g, '')
    if (!word.length) {
      return setPalBool(false)
    }
    let left = 0
    let right = word.length -1
    while (left < right) {
      
    }
  }

  return (
    <div className="App">
      what
    </div>
  );
}

export default App;
