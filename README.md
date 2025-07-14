# Document360-API---Kovai.co
Document360 API CRUD Operations
This project demonstrates how to interact with the Document360 API to perform CRUD (Create, Read, Update, Delete) operations on drive folders.
📋 Task Overview
This console application implements 4 main API operations:

GET - Fetch all drive folders
POST - Create a new drive folder
PUT - Update folder name
DELETE - Remove folder

🛠️ Language and Tools Used

Language: Python 3.x
Libraries:

requests - For HTTP API calls
json - For JSON data handling
datetime - For timestamps


🚀 Setup and Installation
Prerequisites

Python 3.6 or higher
pip (Python package manager)

Installation Steps

Clone the repository:

bashgit clone <your-repository-url>
cd document360-api-crud

Install required packages:

bashpip install requests

Get your credentials:

API Key: Document360 API key
User ID: Document360 user ID

Configure your credentials:

Open document360_api.py
Replace the placeholder values with your actual credentials:

pythonAPI_TOKEN = "your_actual_api_key_here"    # Replace with your API key
USER_ID = "your_actual_user_id_here"      # Replace with your user ID


📁 Project Structure
document360-api-crud/
├── document360_api.py      # Main application file
├── README.md              # This file
└── requirements.txt       # Python dependencies
🏃‍♂️ How to Run

Run the main program:

bashpython document360_api.py

The program will automatically:

Fetch all existing folders (GET)
Create a new test folder (POST)
Rename the created folder (PUT)
Delete the folder (DELETE)
📊 Expected Output
The program will display detailed logs for each operation:
================================================================================
DOCUMENT360 API CRUD OPERATIONS DEMO
================================================================================

************************************************************
TASK #1: FETCHING ALL DRIVE FOLDERS
************************************************************

==================================================
REQUEST LOG - 2024-01-15 10:30:45
==================================================
Method: GET
URL: https://apihub.document360.io/v2/Drive/Folders
Headers: {
  "api_token": "your_api_key",
  "user_id": "your_user_id",
  "Content-Type": "application/json"
}

==================================================
RESPONSE LOG - 2024-01-15 10:30:46
==================================================
Status Code: 200
Status: SUCCESS
Response Body: [
  {
    "id": "folder_id_123",
    "name": "Sample Folder",
    "created_at": "2024-01-15T10:30:45Z"
  }
]

✅ SUCCESS: Found 1 folders
🔧 Features Implemented
Core Requirements

✅ Console application in Python
✅ Individual methods for each CRUD operation
✅ Standard naming conventions
✅ Proper request headers with api_token
✅ Detailed logging of requests and responses
✅ Dynamic folder ID storage and reuse
✅ Modular and readable code with comments

Bonus Features

✅ Response validation
✅ Comprehensive error handling
✅ HTTP status code validation
✅ JSON response structure validation
✅ Request timeout handling
✅ Detailed documentation

🔐 Security Notes

Never commit your actual API key or user ID to version control
These credentials should be stored in environment variables in production
Current implementation is for demonstration purposes only.

🔐 Security Notes

Never commit your actual API key or user ID to version control
These credentials should be stored in environment variables in production
Current implementation is for demonstration purposes only

📝 API Endpoints Used
MethodEndpointDescriptionGET/v2/Drive/FoldersFetch all foldersPOST/v2/Drive/FoldersCreate new folderPUT/v2/Drive/Folders/{id}Update folder nameDELETE/v2/Drive/Folders/{id}Delete folder
🐛 Error Handling
The application handles various error scenarios:

Network connectivity issues
Invalid API tokens
Invalid folder IDs
API rate limiting
Invalid JSON responses
HTTP timeout errors

🎯 Key Implementation Details

Dynamic Folder ID Management: The application stores the created folder ID and reuses it for update and delete operations.
Comprehensive Logging: Every request and response is logged with timestamps, headers, and full body content.
Modular Design: Each CRUD operation is implemented as a separate method in the Document360API class.
Error Resilience: Proper try-catch blocks and status code validation ensure the application handles errors gracefully.

📈 Sample Test Flow

GET: Retrieves existing folders to understand current state
POST: Creates a new folder with timestamp-based name
PUT: Updates the folder name by appending "Updated" prefix
DELETE: Removes the created folder to clean up

📞 Support
If you encounter any issues:

Check your API token is correct
Verify your internet connection
Ensure you have the required Python packages installed
Check the Document360 API documentation for any updates

🏆 Achievement Summary
This implementation successfully demonstrates:

REST API integration skills
Error handling and logging
Clean code structure
Documentation skills
Understanding of HTTP methods and status codes
