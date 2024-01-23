import React from "react";
import ReactDOM from "react-dom";
import htm from "htm";

import { Dropdown, chroma } from './fragments/Dropdown.react'
import { ExampleCounter } from "./fragments/ExampleCounter.react";


const html = htm.bind(React.createElement);

export function bind(node, config) {
  return {

    create: (type, props, children) => {
      console.log('create %s', type)
      return React.createElement(type, props, ...children)
    },

    render: (element) => ReactDOM.render(element, node),
    unmount: () => ReactDOM.unmountComponentAtNode(node),
  }
}

export { Dropdown, ExampleCounter, chroma }
