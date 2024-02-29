## Flask Application Design for Coffee Booking App

### HTML Files
- **index.html**
  - **Purpose:** The landing page of the application, displaying a form to book a coffee order.
  - **Content:**
    - Form with input fields for name, email, coffee type, and quantity.
    - Submit button to send the order.

### Routes

- **[/]**
  - **HTTP Method:** GET
  - **Purpose:** Directs the user to the index.html page.

- **[/order]**
  - **HTTP Method:** POST
  - **Purpose:** Processes the coffee order submitted from index.html.
  - **Functionality:**
    - Retrieves order details from the request form.
    - Validates the order (e.g., checking if the email is valid, coffee type is supported, etc.).
    - Stores the order in a database or sends it to a fulfillment system.
    - Redirects to a success page or displays an error message if validation fails.

- **[/success]**
  - **HTTP Method:** GET
  - **Purpose:** Confirms a successful order.
  - **Content:**
    - Confirmation message and order details.