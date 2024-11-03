Ip Scanner scripts 01 and 02 are for the same purpose.
the second was improved with some great feauters:

Improvements
Error Handling: Add error handling for invalid IP addresses or hostname resolution failures.
Socket Creation: Move the socket creation inside the loop to ensure it’s done fresh for each connection attempt.
Resource Management: Use a context manager (with statement) to automatically close the socket.
User Input Validation: Check that the input is valid before proceeding with the scan.
Port Range: Allow users to specify the range of ports to scan.
Output Clarity: Format the output for better readability.
