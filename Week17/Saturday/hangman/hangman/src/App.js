import React, {useEffect, useState} from 'react'
import './App.css';
import Guess from './components/guess/guess';
import PuzzleBoard from './components/puzzleBoard/puzzleBoard';
import words from './wordList';

function App() {
  
  useEffect(() => {
    chosePuzzle()
  }, [])
  
  const puzzles = words
  
  const [puzzle, setPuzzle] = useState('word')
  const [guessedLetters, setGuessedLetters] = useState([])
  
  const chosePuzzle = () => {
    setPuzzle(puzzles[Math.floor(Math.random()*puzzles.length)])
  }

  const handleGuess = (event) => { 
    event.preventDefault()
    if(event.target[0].value != '' ){
      const updated = [...guessedLetters]
    updated.push(event.target[0].value.toLowerCase())
    setGuessedLetters(updated)
    }
    return event.target.reset() 
  }

  return (
    <div >
      <PuzzleBoard puzzle={puzzle} guesses={guessedLetters} />
      <Guess handler={handleGuess} guesses={guessedLetters}  />
    </div>
  );
}

export default App;
