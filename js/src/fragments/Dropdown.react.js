import React from 'react'
import Select from 'react-select'

// https://react-select.com/props
// https://dash.plotly.com/dash-core-components/dropdown#examples

const Dropdown = props => {
    const {options, multi} = props;
    return (
        <Select {...props}/>
    );
};


export default Dropdown;
