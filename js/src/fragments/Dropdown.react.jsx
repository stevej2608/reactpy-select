import React from 'react'
import chroma from 'chroma-js';
import Select from 'react-select'

// https://react-select.com/props

export function Dropdown(props) {
    const local_props = { ...props };

    console.log('Dropdown(styles)')

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

    if (local_props.styles) {

        /**
         * https://react-select.com/components#adjusting-the-styling
         * 
         *     clearIndicator
         *     container
         *     control
         *     dropdownIndicator
         *     group
         *     groupHeading
         *     indicatorsContainer
         *     indicatorSeparator
         *     input
         *     loadingIndicator
         *     loadingMessage
         *     menu
         *     menuList
         *     menuPortal
         *     multiValue
         *     multiValueLabel
         *     multiValueRemove
         *     noOptionsMessage
         *     option
         *     placeholder
         *     singleValue
         *     valueContainer
         */

        const customStyles = {}

        for (const [key, code] of Object.entries(local_props.styles)) {
            try {  
                customStyles[key] =  eval(code)
             } catch ( e ) { 
                console.log('eval error key=%s, error=%s', key, e)
             }
        }

        local_props.styles = customStyles

    }


    return (
        <Select {...local_props} />
    );
};
