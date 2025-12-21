"""
ReactPy v1 compatible run() function for ReactPy v2

This module provides a run() function that mimics the ReactPy v1 behavior,
making it easy to run simple examples without manual server setup.
"""

import sys
from typing import Any, Callable, Optional

import uvicorn
from reactpy import html
from reactpy.core.component import Component
from reactpy.types import VdomDict
from reactpy.executors.asgi import ReactPy


def run(
    app_main: Callable[[], Component],
    host: str = "127.0.0.1",
    port: int = 8000,
    title: str = "ReactPy App",
    head: Optional[VdomDict] = None,
    **kwargs: Any,
) -> None:
    """Run a ReactPy component with automatic server setup.

    This function reproduces the ReactPy v1 run() behavior by automatically
    creating and configuring an ASGI server to run your ReactPy component.

    Args:
        app_main: A ReactPy component function decorated with @component
        host: Server host address (default: "127.0.0.1")
        port: Server port (default: 8000)
        title: Page title (default: "ReactPy App")
        head: Optional HTML head VdomDict element with additional head content
        **kwargs: Additional arguments passed to uvicorn.run()

    Example:
        ```python
        from reactpy import component, html
        from examples.runner import run

        @component
        def AppMain():
            return html.h1("Hello ReactPy!")

        if __name__ == "__main__":
            run(AppMain)
        ```
    """

    # Build head element
    if head is None:
        head = html.head(html.title(title))
    elif "children" in head:
        # Add title to existing head if not present
        children = head.get("children", [])  # type: ignore[misc]
        has_title = any(
            isinstance(child, dict) and child.get("tagName") == "title"  # type: ignore[union-attr]
            for child in children  # type: ignore[union-attr]
        )
        if not has_title:
            # Convert to list to enable insert operation
            children_list = list(children)  # type: ignore[arg-type]
            children_list.insert(0, html.title(title))  # type: ignore[union-attr]
            head["children"] = children_list  # type: ignore[typeddict-item]
    else:
        head["children"] = [html.title(title)]  # type: ignore[typeddict-item]

    # Create ReactPy ASGI app
    app = ReactPy(app_main, html_head=head)

    # Display startup message
    print(f"Starting ReactPy server at http://{host}:{port}")
    print("Press CTRL+C to quit")

    try:
        # Run the server
        uvicorn.run(app, host=host, port=port, **kwargs)
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as ex:
        print(f"Server error: {ex}")
    finally:
        sys.exit(0)
