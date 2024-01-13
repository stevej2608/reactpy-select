import React from 'react'
import Select from 'react-select'

// https://react-select.com/props
// https://dash.plotly.com/dash-core-components/dropdown#examples

export function Dropdown(props) {
    const local_props  = {...props};

    console.log('Dropdown()')

    if ('theme' in local_props) {
        const tcb = function(default_theme) {
            const custom_theme =  {
                ...default_theme,
                ...props.theme,
                colors: {
                    ...default_theme.colors,
                    ...props.theme.colors,
                }
            }
            return custom_theme
          }

          local_props.theme = tcb
    }


    return (
        <Select {...local_props}/>
    );
};
