import React from 'react'
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

    // https://github.com/JedWatson/react-select/blob/master/packages/react-select/src/styles.ts#L52
    //
    // https://www.regextester.com/
    // /(\w+):\s\(defaultStyles[\s\S]*?\}\)/g

    if (local_props.styles) {

        /**
         * 
         *     clearIndicator: ClearIndicatorProps<Option, IsMulti, Group>;
         *     container: ContainerProps<Option, IsMulti, Group>;
         *     control: ControlProps<Option, IsMulti, Group>;
         *     dropdownIndicator: DropdownIndicatorProps<Option, IsMulti, Group>;
         *     group: GroupProps<Option, IsMulti, Group>;
         *     groupHeading: GroupHeadingProps<Option, IsMulti, Group>;
         *     indicatorsContainer: IndicatorsContainerProps<Option, IsMulti, Group>;
         *     indicatorSeparator: IndicatorSeparatorProps<Option, IsMulti, Group>;
         *     input: InputProps<Option, IsMulti, Group>;
         *     loadingIndicator: LoadingIndicatorProps<Option, IsMulti, Group>;
         *     loadingMessage: NoticeProps<Option, IsMulti, Group>;
         *     menu: MenuProps<Option, IsMulti, Group>;
         *     menuList: MenuListProps<Option, IsMulti, Group>;
         *     menuPortal: PortalStyleArgs;
         *     multiValue: MultiValueProps<Option, IsMulti, Group>;
         *     multiValueLabel: MultiValueProps<Option, IsMulti, Group>;
         *     multiValueRemove: MultiValueProps<Option, IsMulti, Group>;
         *     noOptionsMessage: NoticeProps<Option, IsMulti, Group>;
         *     option: OptionProps<Option, IsMulti, Group>;
         *     placeholder: PlaceholderProps<Option, IsMulti, Group>;
         *     singleValue: SingleValueProps<Option, IsMulti, Group>;
         *     valueContainer: ValueContainerProps<Option, IsMulti, Group>;
         */

        const customStyles = {
            option: (defaultStyles, state) => ({
              ...defaultStyles,
              ...props.styles.option
            }),
        
            control: (defaultStyles) => ({
              ...defaultStyles,
              ...props.styles.control

            }),

            singleValue: (defaultStyles) => ({
              ...defaultStyles,
              ...props.styles.singleValue 
            }),
          };

        local_props.styles = customStyles 
    }


    return (
        <Select {...local_props} />
    );
};
