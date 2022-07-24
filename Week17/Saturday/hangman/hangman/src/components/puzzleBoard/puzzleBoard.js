import React from "react";

const PuzzleBoard = (props) => {
  


  const SetBoard = (word) => { 
    return word.split('').map((letter) =>  props.guesses.includes(letter.toLowerCase()) ? letter :' _ ')
  }

  return (
    <div>
    {SetBoard(props.puzzle)}
    </div>
  )
}

export default PuzzleBoard

