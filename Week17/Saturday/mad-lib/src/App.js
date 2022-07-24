import React, { Component } from 'react'
import './App.css'
import WordForm from './components/madlib-wordform/WordForm.js'
import Story from './components/madlib-story/Story.js'
import MadLibs from './madlibs/MadLibs.js'

class App extends Component {
  state = {
    madlibs: MadLibs,
    selectedMadLib: MadLibs[0]
  }

  onWordInputChange = (key, value, index) => {
    const newState = {
      ...this.state
    }
    newState.selectedMadLib.words[index] = {
      ...newState.selectedMadLib.words[index],
      value: value
    }
    this.setState(newState)
  }

  madLibSelections = () => {
    const madLibsArr = this.state.madlibs.map((lib, index) => (
      <option key={index} value={index}>{lib.title}</option>
    ) )
    return madLibsArr
  }

  changeMadLib = (e) => {
    const index = (e.currentTarget.value)
    this.setState({selectedMadLib: MadLibs[index]})
    
  }

  render() {
    console.log(this.madLibSelections())
    console.log(this.state.selectedMadLib)
    return (
      <div className="App">
        <h1>MADLIBS!</h1>
        <select onChange={this.changeMadLib}>
          {this.madLibSelections()}
        </select>
        <WordForm words={this.state.selectedMadLib.words} onInputChange={this.onWordInputChange} />
        <Story text={this.state.selectedMadLib.getText()} />
      </div>
    )
  }
}

export default App
