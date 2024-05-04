from FinanceApp import FinanceApp

if __name__ == "__main__":
    """
    Main entry point of the application.
    
    If this script is run directly (not imported), it creates an instance of the FinanceApp class and starts the main 
    loop."""
    app = FinanceApp()  # Create an instance of the FinanceApp class
    app.main_loop()  # Start the main loop of the application
