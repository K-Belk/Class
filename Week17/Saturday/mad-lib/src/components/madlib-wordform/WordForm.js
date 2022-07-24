import React, { Component } from 'react'
import './WordForm.css'

class WordForm extends Component {
  onInputChange(key, index, event) {
    this.props.onInputChange(key, event.currentTarget.value, index)
  }

  handleWord = () => {
    const words = this.props.words
    const wordArr = words.map((word,index) => (
      <div key={index}>
      <label >
        {word.label}
        <input type="text"  name={word.key} onChange={(e) => this.onInputChange(word.key, index, e)}></input>
      </label>
      </div>
    ))
    return wordArr
  }

  render() {
    // console.log(this.props.words)
    return (
  
        <form onSubmit={}>
        {this.handleWord()}
        </form>
      
    )
  }
}

export default WordForm
