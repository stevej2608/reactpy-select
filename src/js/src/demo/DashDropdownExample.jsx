import { Select } from '../fragments/Select.react'

// Mimic the style of the classic Plotly/Dash Stock Tickers Demo App
//
// See https://github.com/plotly/dash-stock-tickers-demo-app

const TICKERS = [
  {'label': 'AAPL', 'value': 'AAPL'}, 
  {'label': 'TSLA', 'value': 'TSLA'}, 
  {'label': 'COKE', 'value': 'COKE'}, 
  {'label': 'YHOO', 'value': 'YHOO'}, 
  {'label': 'GOOGL', 'value': 'GOOGL'}
  ]

const colourStyles = {

  multiValueLabel: `(styles, { data }) => ({
    ...styles,
    color: '#5ca3ff',
  })`,

  multiValue: `(styles, { data }) => {
    return {
      ...styles,
      backgroundColor: '#ebf5ff',
      border: '1px solid #c2e0ff'
    }
  }`,

  multiValueRemove: `(styles, { data }) => ({
    ...styles,
    color: '#5ca3ff',
    ':hover': {
      backgroundColor: '#d9ebfd',
    },
  })`,

};

function App() {
  return (
    <Select
      isMulti
      options={TICKERS}
      styles={colourStyles}
    />
  )
}

export default App

