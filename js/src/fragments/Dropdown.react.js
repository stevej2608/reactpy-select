import React from 'react'
import Select from 'react-select'

// https://react-select.com/props

export function Dropdown(props) {
    const local_props = { ...props };

    console.log('Dropdown()')

    // https://github.com/JedWatson/react-select/blob/master/packages/react-select/src/theme.ts

    if (local_props.theme) {
        local_props.theme = function (base_theme) {
            return {
                ...base_theme,
                ...props.theme,
                colors: {
                    ...base_theme.colors,
                    ...props.theme.colors,
                },
                spacing: {
                    ...base_theme.spacing,
                    ...props.theme.spacing,
                }
            }
        }
    }


    return (
        <Select {...local_props} />
    );
};
