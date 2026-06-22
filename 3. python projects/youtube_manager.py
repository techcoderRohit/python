import json

def load_data():
    """Load videos from JSON file"""
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    """Save videos to JSON file"""
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file, indent=2)

def list_all_videos(videos):
    """Display all videos with index, name and time"""
    if not videos:
        print("\n" + "*" * 50)
        print("*** No videos in your list yet! ***")
        print("*" * 50)
        return
    
    print("\n" + "*" * 50)
    print("*** YouTube Videos Library ***")
    print("*" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} - ({video['time']} mins)")
    print("*" * 50)

def add_video(videos):
    """Add a new video to the list"""
    name = input("Enter video name: ").strip()
    if not name:
        print(" Video name cannot be empty!")
        return
    
    time = input("Enter video duration (in minutes): ").strip()
    if not time or not time.isdigit():
        print(" Please enter a valid duration in minutes!")
        return
    
    video = {'name': name, 'time': int(time)}
    videos.append(video)
    save_data_helper(videos)
    print(f" Video '{name}' added successfully!")

def update_video(videos):
    """Update an existing video's details"""
    if not videos:
        print("\n No videos to update!")
        return
    
    list_all_videos(videos)
    
    try:
        video_index = int(input("Enter video number to update: ")) - 1
        
        if video_index < 0 or video_index >= len(videos):
            print(" Invalid video number!")
            return
        
        name = input("Enter new video name (or press Enter to skip): ").strip()
        if name:
            videos[video_index]['name'] = name
        
        time = input("Enter new video duration in minutes (or press Enter to skip): ").strip()
        if time:
            if not time.isdigit():
                print(" Please enter a valid duration!")
                return
            videos[video_index]['time'] = int(time)
        
        save_data_helper(videos)
        print(" Video updated successfully!")
    
    except ValueError:
        print(" Please enter a valid number!")

def delete_video(videos):
    """Delete a video from the list"""
    if not videos:
        print("\n No videos to delete!")
        return
    
    list_all_videos(videos)
    
    try:
        video_index = int(input("Enter video number to delete: ")) - 1
        
        if video_index < 0 or video_index >= len(videos):
            print(" Invalid video number!")
            return
        
        deleted_video = videos.pop(video_index)
        save_data_helper(videos)
        print(f" Video '{deleted_video['name']}' deleted successfully!")
    
    except ValueError:
        print(" Please enter a valid number!")

def main():
    """Main function to run the YouTube Manager application"""
    videos = load_data()
    
    print("\n" + "*" * 50)
    print(" Welcome to YouTube Manager! ")
    print("*" * 50)
    
    while True:
        print("\n Choose an option:")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        
        choice = input("\nEnter your choice (1-5): ").strip()

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("\n Thank you for using YouTube Manager! Goodbye!")
                break
            case _:
                print(" Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()