import { Dropdown } from '../fragments/Dropdown.react'

const options = [
  { value: 'chocolate', label: 'Chocolate' },
  { value: 'strawberry', label: 'Strawberry' },
  { value: 'vanilla', label: 'Vanilla' }
]

function App() {

  return (
    <Dropdown options={options}/>
  )
}

export default App
