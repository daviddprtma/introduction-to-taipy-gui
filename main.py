from taipy.gui import Gui
import taipy.gui.builder as tgb

# Define the root page with navigation
with tgb.Page() as root_page:
    tgb.navbar()  # Default navigation bar
    tgb.text("# Welcome to the Multi-Page Application", mode="md")

# Define Page 1
with tgb.Page() as page_1:
    tgb.text("## This is Page 1", mode="md")

# Define Page 2
with tgb.Page() as page_2:
    tgb.text("## This is Page 2", mode="md")

# Combine all pages
pages = {
    "/": root_page,
    "page1": page_1,
    "page2": page_2
}

# Run the application
Gui(pages=pages).run()