import { Select } from '../fragments/Select.react'

const options = [
  { value: 'chocolate', label: 'Chocolate' },
  { value: 'strawberry', label: 'Strawberry' },
  { value: 'vanilla', label: 'Vanilla' }
]

// https://blog.logrocket.com/getting-started-react-select/#adding-custom-styles-react-select-components

const customStyles = {
  option: (defaultStyles, state) => ({
    ...defaultStyles,
    color: state.isSelected ? "#212529" : "#fff",
    backgroundColor: state.isSelected ? "#a0a0a0" : "#212529",
  }),

  control: (defaultStyles) => ({
    ...defaultStyles,
    backgroundColor: "#212529",
    padding: "10px",
    border: "none",
    boxShadow: "none",
  }),
  singleValue: (defaultStyles) => ({ ...defaultStyles, color: "#fff" }),
};


function App() {
  return (
    <Select options={options} styles={customStyles}/>
  )
}

export default App
