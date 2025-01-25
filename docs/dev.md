# Development

To set up a virtual environment and manage dependencies for this project, follow these steps:

### Setting Up the Virtual Environment

1. **Create the virtual environment**:
   
   Navigate to your project directory and run the following command to create a virtual environment named `venv`:

   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment**:
   
   Activation varies by operating system:

   - On **Windows**, execute:

     ```bash
     venv\Scripts\activate
     ```

   - On **macOS and Linux**, use:

     ```bash
     source venv/bin/activate
     ```

   You will see `(venv)` in your command prompt which indicates that the virtual environment is now active.

3. **Install project dependencies**:

   With the virtual environment activated, install all required dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

### Additional Development Notes

- Ensure to deactivate the virtual environment when you're done working on the project by executing `deactivate`.
- Always activate the virtual environment before running any project-related commands to avoid installing packages globally.

This setup ensures that all dependencies are contained within an isolated environment, minimizing conflicts and maintaining consistency across development setups.