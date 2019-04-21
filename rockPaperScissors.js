
const getUserChoice = (userInput) => {
  userInput = userInput.toLowerCase()

  if (userInput === 'rock') {
		return 'rock'
  } else if (userInput === 'paper') {
		return 'paper'
  } else if (userInput === 'scissors') {
    return 'scissors'
  } else {
    return 'Error'
  }
}

const getComputerChoice = () => {
	let compChoice = Math.floor(Math.random() * 3) + 1

  if (compChoice === 1) {
    return 'rock'
  } else if (compChoice === 2) {
		return 'paper'
  } else if (compChoice === 3) {
    return 'scissors'
  }
}

const determineWinner = (userChoice, computerChoice) => {
  if (userChoice === computerChoice) {
      return 'It is a tie';
  }
  if (userChoice === 'rock') {
    if (computerChoice === 'paper') {
      return 'The Computer Won'
    } else {
      return 'The Human Won'
    }
  }
  if (userChoice === 'scissors') {
    if (computerChoice === 'rock') {
      return 'The Computer Won'
    } else {
      return 'The Human Won'
    }
  }
  if (userChoice === 'paper') {
    if (computerChoice === 'rock') {
      return 'The Human Won'
    } else {
      return 'The Computer Won'
    }
  }
}

const playGame = (choice) => {
  if (choice === 'bomb') {
    console.log('The Human Won')
  } else {
	let human = getUserChoice(choice)
	let computer = getComputerChoice()
  console.log(determineWinner(human, computer))
	}
}

playGame('Rock')
