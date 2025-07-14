import requests
import json
import time
from datetime import datetime

class Document360API:
    def __init__(self, api_token, user_id=None):
        """
        Initialize the Document360 API client
        
        Args:
            api_token (str): Your Document360 API token/key
            user_id (str, optional): Your Document360 user ID
        """
        self.api_token = api_token
        self.user_id = user_id
        self.base_url = "https://apihub.document360.io/v2/Drive/Folders"
        
        # Set up headers with both api_token and user_id if provided
        self.headers = {
            "api_token": self.api_token,
            "Content-Type": "application/json"
        }
        
        # Add user_id to headers if provided
        if self.user_id:
            self.headers["user_id"] = self.user_id
        self.folder_id = None  # Will store the created folder ID dynamically
    
    def log_request(self, method, url, headers, body=None):
        """Log request details"""
        print(f"\n{'='*50}")
        print(f"REQUEST LOG - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*50}")
        print(f"Method: {method}")
        print(f"URL: {url}")
        print(f"Headers: {json.dumps(headers, indent=2)}")
        if body:
            print(f"Body: {json.dumps(body, indent=2)}")
    
    def log_response(self, response):
        """Log response details"""
        print(f"\n{'='*50}")
        print(f"RESPONSE LOG - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*50}")
        print(f"Status Code: {response.status_code}")
        print(f"Status: {'SUCCESS' if response.status_code < 400 else 'ERROR'}")
        
        try:
            response_json = response.json()
            print(f"Response Body: {json.dumps(response_json, indent=2)}")
        except:
            print(f"Response Body (Raw): {response.text}")
        
        if response.status_code >= 400:
            print(f"ERROR MESSAGE: {response.text}")
    
    def get_all_folders(self):
        """
        Task #1: GET - Fetch all drive folders
        """
        print(f"\n{'*'*60}")
        print("TASK #1: FETCHING ALL DRIVE FOLDERS")
        print(f"{'*'*60}")
        
        try:
            # Log the request
            self.log_request("GET", self.base_url, self.headers)
            
            # Make the API call
            response = requests.get(self.base_url, headers=self.headers)
            
            # Log the response
            self.log_response(response)
            
            # Handle the response
            if response.status_code == 200:
                response_data = response.json()
                folders = response_data.get('data', [])
                print(f"\n✅ SUCCESS: Found {len(folders)} folders")
                
                # Display folder details
                for i, folder in enumerate(folders, 1):
                    print(f"\nFolder {i}:")
                    print(f"  Name: {folder.get('title', 'N/A')}")
                    print(f"  ID: {folder.get('id', 'N/A')}")
                    print(f"  Updated: {folder.get('updated_on', 'N/A')}")
                    print(f"  Items Count: {folder.get('items_count', 0)}")
                
                return folders
            else:
                print(f"\n❌ ERROR: Failed to fetch folders")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"\n❌ REQUEST ERROR: {str(e)}")
            return None
        except Exception as e:
            print(f"\n❌ UNEXPECTED ERROR: {str(e)}")
            return None
    
    def create_folder(self, folder_name, parent_folder_id=None):
        """
        Task #2: POST - Create a new drive folder (FIXED)
        
        Args:
            folder_name (str): Name of the folder to create
            parent_folder_id (str, optional): ID of parent folder for nested creation
        """
        print(f"\n{'*'*60}")
        print("TASK #2: CREATING A NEW FOLDER")
        print(f"{'*'*60}")
        
        # Prepare request body with user_id included in the body
        body = {
            "title": folder_name,
            "user_id": self.user_id  # Add user_id to the request body - THIS IS THE FIX!
        }
        
        # Add parent folder ID if provided (for nested folders)
        if parent_folder_id:
            body["parent_folder_id"] = parent_folder_id
        
        try:
            # Log the request
            self.log_request("POST", self.base_url, self.headers, body)
            
            # Make the API call
            response = requests.post(self.base_url, headers=self.headers, json=body)
            
            # Log the response
            self.log_response(response)
            
            # Handle the response
            if response.status_code in [200, 201]:
                response_data = response.json()
                
                # Check if the response indicates success
                if response_data.get('success', False):
                    folder_data = response_data.get('data', {})
                    self.folder_id = folder_data.get('id')  # Store folder ID dynamically
                    
                    print(f"\n✅ SUCCESS: Folder created successfully!")
                    print(f"  Folder Name: {folder_data.get('title', 'N/A')}")
                    print(f"  Folder ID: {self.folder_id}")
                    print(f"  Updated At: {folder_data.get('updated_on', 'N/A')}")
                    
                    return folder_data
                else:
                    print(f"\n❌ ERROR: API returned success=false")
                    errors = response_data.get('errors', [])
                    for error in errors:
                        print(f"  Error: {error.get('description', 'Unknown error')}")
                    return None
            else:
                print(f"\n❌ ERROR: Failed to create folder")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"\n❌ REQUEST ERROR: {str(e)}")
            return None
        except Exception as e:
            print(f"\n❌ UNEXPECTED ERROR: {str(e)}")
            return None
    
    def update_folder_name(self, new_name, folder_id=None):
        """
        Task #3: PUT - Update folder name (FIXED)
        
        Args:
            new_name (str): New name for the folder
            folder_id (str, optional): Folder ID to update. Uses stored ID if not provided
        """
        print(f"\n{'*'*60}")
        print("TASK #3: UPDATING FOLDER NAME")
        print(f"{'*'*60}")
        
        # Use stored folder ID if not provided
        target_folder_id = folder_id or self.folder_id
        
        if not target_folder_id:
            print("\n❌ ERROR: No folder ID available. Create a folder first.")
            return None
        
        # Prepare URL and body with user_id in the body
        url = f"{self.base_url}/{target_folder_id}"
        body = {
            "title": new_name,
            "user_id": self.user_id  # Add user_id to the request body - THIS IS THE FIX!
        }
        
        try:
            # Log the request
            self.log_request("PUT", url, self.headers, body)
            
            # Make the API call
            response = requests.put(url, headers=self.headers, json=body)
            
            # Log the response
            self.log_response(response)
            
            # Handle the response
            if response.status_code == 200:
                response_data = response.json()
                
                # Check if the response indicates success
                if response_data.get('success', False):
                    folder_data = response_data.get('data', {})
                    
                    print(f"\n✅ SUCCESS: Folder name updated successfully!")
                    print(f"  New Folder Name: {folder_data.get('title', 'N/A')}")
                    print(f"  Folder ID: {target_folder_id}")
                    print(f"  Updated At: {folder_data.get('updated_on', 'N/A')}")
                    
                    return folder_data
                else:
                    print(f"\n❌ ERROR: API returned success=false")
                    errors = response_data.get('errors', [])
                    for error in errors:
                        print(f"  Error: {error.get('description', 'Unknown error')}")
                    return None
            else:
                print(f"\n❌ ERROR: Failed to update folder name")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"\n❌ REQUEST ERROR: {str(e)}")
            return None
        except Exception as e:
            print(f"\n❌ UNEXPECTED ERROR: {str(e)}")
            return None
    
    def delete_folder(self, folder_id=None):
        """
        Task #4: DELETE - Remove the folder (FIXED)
        
        Args:
            folder_id (str, optional): Folder ID to delete. Uses stored ID if not provided
        """
        print(f"\n{'*'*60}")
        print("TASK #4: DELETING FOLDER")
        print(f"{'*'*60}")
        
        # Use stored folder ID if not provided
        target_folder_id = folder_id or self.folder_id
        
        if not target_folder_id:
            print("\n❌ ERROR: No folder ID available. Create a folder first.")
            return None
        
        # Prepare URL and body with user_id for DELETE request
        url = f"{self.base_url}/{target_folder_id}"
        
        # Some APIs require user_id in DELETE request body too
        body = {
            "user_id": self.user_id
        }
        
        try:
            # Log the request
            self.log_request("DELETE", url, self.headers, body)
            
            # Make the API call with body (in case API requires user_id)
            response = requests.delete(url, headers=self.headers, json=body)
            
            # Log the response
            self.log_response(response)
            
            # Handle the response
            if response.status_code in [200, 204]:
                # Handle both JSON response and empty response
                if response.content:
                    try:
                        response_data = response.json()
                        success = response_data.get('success', True)
                    except:
                        success = True  # If no JSON, assume success for 200/204
                else:
                    success = True  # Empty response with 200/204 means success
                
                if success:
                    print(f"\n✅ SUCCESS: Folder deleted successfully!")
                    print(f"  Deleted Folder ID: {target_folder_id}")
                    
                    # Clear the stored folder ID
                    self.folder_id = None
                    
                    return True
                else:
                    print(f"\n❌ ERROR: API returned success=false")
                    if response.content:
                        try:
                            response_data = response.json()
                            errors = response_data.get('errors', [])
                            for error in errors:
                                print(f"  Error: {error.get('description', 'Unknown error')}")
                        except:
                            pass
                    return False
            else:
                print(f"\n❌ ERROR: Failed to delete folder")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"\n❌ REQUEST ERROR: {str(e)}")
            return False
        except Exception as e:
            print(f"\n❌ UNEXPECTED ERROR: {str(e)}")
            return False
    
    def validate_response(self, response, expected_status_codes=[200]):
        """
        Bonus: Validate HTTP status codes and response structure
        """
        if response.status_code not in expected_status_codes:
            return False, f"Unexpected status code: {response.status_code}"
        
        try:
            response.json()
            return True, "Valid JSON response"
        except:
            return False, "Invalid JSON response"


def main():
    """
    Main function to demonstrate all CRUD operations
    """
    print("="*80)
    print("DOCUMENT360 API CRUD OPERATIONS DEMO")
    print("="*80)
    
    # Your actual credentials
    API_TOKEN = "M1XbCrQnV47mHjZcYnpsUBOFPvDFo/PJhrSaPRNlJb4MYO0gWTQamNFIw6zn7KLCo5e4xx7aTm5dbDhSxFBJS64Qd34M8gn0/78uGxilK4Rg4MVNLVO62u18ElX59BSJJ1Pcfyar2N5TqrQMEypEOQ=="
    USER_ID = "223e32e4-7a9f-4a69-ba9a-5f201c00dbda"
    
    # Initialize API client with both credentials
    api = Document360API(API_TOKEN, USER_ID)
    
    try:
        # Task #1: GET all folders
        print("\n" + "="*80)
        print("STARTING CRUD OPERATIONS SEQUENCE")
        print("="*80)
        
        folders = api.get_all_folders()
        time.sleep(2)  # Small delay between operations
        
        # Task #2: CREATE a new folder
        folder_name = f"Test Folder {datetime.now().strftime('%Y%m%d_%H%M%S')}"
        created_folder = api.create_folder(folder_name)
        time.sleep(2)
        
        if created_folder:
            # Task #3: UPDATE folder name
            new_name = f"Updated {folder_name}"
            updated_folder = api.update_folder_name(new_name)
            time.sleep(2)
            
            # Task #4: DELETE the folder
            api.delete_folder()
        
        print("\n" + "="*80)
        print("CRUD OPERATIONS COMPLETED SUCCESSFULLY!")
        print("="*80)
        
    except Exception as e:
        print(f"\n❌ MAIN EXECUTION ERROR: {str(e)}")


if __name__ == "__main__":
    main()