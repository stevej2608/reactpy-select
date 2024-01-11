import React from 'react'
import Select from 'react-select'

const Dropdown = props => {
    const {options, multi} = props;
    return (
        <Select {...props}/>
    );
};


export default Dropdown;
