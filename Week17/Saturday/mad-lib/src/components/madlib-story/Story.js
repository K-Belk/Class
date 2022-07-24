import React, { Component } from 'react'
import './Story.css'

class Story extends Component {
  render() {
    return (
      <for>
        <p>{this.props.text}</p>
      </for>
    )
  }
}

export default Story
