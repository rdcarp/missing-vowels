import logo from './logo.svg';
import './App.css';
import ReactHtml from 'raw-html-react'
import React from "react";


const CorrectAnswer = () => (
    <p>This is an answer</p>
)

const AnswerSubmit = () => (
  <input type={"test"} />
)

const Clue = () => (
  <p>HR S CL</p>
)

const Question = ({answered}) => (
    <div>
        <Clue />
        { !answered && <AnswerSubmit /> }
        { answered && <CorrectAnswer /> }
    </div>
)

const Category = ({title, answered}) => (
    <React.Fragment>
        <h2>{title}</h2>
        <h4>{answered ? "True":"False"}</h4>
        <Question answered={answered}/>
    </React.Fragment>
)

function App() {
  return (
    <div className="App">
      <header className="App-header">
          <h2>Page header.</h2>
      </header>
        <input type={"checkbox"} id={"answeredDebug"} />
      <Category title={"My missing vowels test."} answered={false}/>
    </div>
  );
}

export default App;
