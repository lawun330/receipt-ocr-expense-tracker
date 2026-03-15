# Rules

## README.md Rules
- Maintain a simple writing style
- Avoid excessive bullet points
- The README should follow this structure:
  1. Project Structure
  2. Dependencies Installation
  3. Deployment Tips
  4. Notes

## Comment Rules

### Comment Types
There are two types of comments:

1. Special Comments  
   - A comment placed directly above a function
   - Must start with a capital letter

2. Normal Comments  
   - Comments inside functions or beside standalone code
   - Must start with a lowercase letter

### Comment Style
- Do not use periods at the end of comments
- Use hierarchical comment levels when needed:
  - `#` explanation
  - `##` detailed explanation
  - `###` deeper explanation or examples

## Docstring Rules
- Follow the same structure as comment rules
- Sentences must end with periods
- Do not use periods in section labels such as:
  - args:
  - returns:
  - output:

## Code Structure Rules

### Section Definition

A section is one logical block of code. A section may be:
- A group of global variable declarations
- A function (including its comment if present)
- Any top-level code block

If a function has a comment above it, the section starts from the comment.

Example:
  ```python
  # calculate total price
  def calculate_total():
      pass
  ```
  The section begins from the comment line.

If no comment exists:
  ```python
  def calculate_total():
      pass
  ```
  The section begins from the function definition.

### Section Spacing

- There must be two blank lines between sections
- The spacing is measured from the last line of the previous section to the first line of the next section

Example:
  ```python
  API_URL = "example"
  TIMEOUT = 30


  # fetch user data
  def fetch_user():
      pass


  def save_user():
      pass
  ```

### Section Transitions

These transitions count as section-to-section transitions:
- Global variables → Function
- Function → Function

These transitions do NOT count as section transitions:
- Code blocks inside a function
- Loops inside functions
- Conditional statements inside functions

Example:
  ```python
  def process():
      for item in items:
          if item:
              print(item)
  ```
No extra spacing is required inside functions.

### Function Spacing

- Always ensure two blank lines after each function
- This applies to all top-level functions

### Variable Declaration Rules

- Consecutive variable declarations must not contain blank lines
- Keep them grouped together

Example:
  ```python
  API_URL = "example"
  TIMEOUT = 30
  RETRY_COUNT = 3
  variable1 = 40.4
  ```

## Import Rules

- Do not use wildcard imports
- Prefer explicit imports
- Keep all imports at the top of the file
- All imports must be sorted alphabetically, similar to the behavior enforced by Ruff
- Imports must be grouped in the following order:
  1. Standard library
  2. Third-party packages
  3. Local project imports
- Each group must be alphabetically sorted.
- Two blank lines must separate the import section from the next code section

Correct Example:
  ```python
  import os
  import sys

  import requests
  from dotenv import load_dotenv

  from services.auth import AuthService
  from utils.helpers import format_date


  # Load environment variables
  load_dotenv()
  ```

Incorrect Example (not alphabetical, incorrect grouping):
  ```python
  import requests
  import os
  from utils.helpers import format_date
  import sys
  ```