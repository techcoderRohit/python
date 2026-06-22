import sqlite3

# Database connection
conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS VIDEOS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time INTEGER NOT NULL
    )    
''')


def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    conn.commit()

def main():
    """Main function to run the YouTube Manager application"""
    print("\n" + "*" * 50)
    print("*** Welcome to YouTube Manager! ***")
    print("*" * 50)
    
    while True:
        print("Choose an option: ")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            list_all_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ") 
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id = input("Enter video ID to delete: ") 
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
    conn.close()

if __name__ == "__main__":
    main()



