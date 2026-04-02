function test(log: string) : void {
    console.log(log);
}

function validate(log: string, actual: any, expectation: any): void {
    const result = actual === expectation ? "PASSED" : "FAILED";
    const message = ` [${log}] Result : ${result}, actual: ${actual}, expected: ${expectation}`;
    console.log(message);
}

// Question 1:
//     Implement a simple in-memory cloud storage system that maps files to their meta information in TypeScript. This cloud storage system should support operations below

        // Level 1
//     add_file(name: string, size: number) -> boolean : should add new file name to the storage. size is the amount of moemory required in bytes. this operation failes if a file with the same name exists. return true if added successfully, false otherwise.

//     copy_file(name_from: string, name_to: string) -> boolean : should copy the file at name_from to name_to. this operation failes if name_from points to a file that does not exists or points to a directory. The operation failes if specifed file alredy exists at name_to. Returns True if the file was copied successfully, false otherwise.

//     get_file_size(name: string) -> number | null : should return the size of the file name if exists, null otherwise.

        // Level 2
//     find_file(prefix: string, suffix: string) -> string[] : search for files with names starting with prefix and ending with suffix. Returns a list of strings representing all matching files in this format: ["<name_1>(<size_1>)", "<name_2>(<size_2>)", ......] . The output should be sorted in descending order of file sizes, in the case of ties, lexicographically. if no files match the required properties, should return an empty list

        // Level 3
//     add_user(user_id: string, capacity: int) -> bool : should add a new user to the system, with capacity as their storage limit in bytes. The total size of all files owned by user_id cannot exceed capacity. The operation fails if a user user_id already exists. Returns true if a user successfully created, false otherwise.

//     add_file_by(user_id: string, name: string, size: number) -> number | null : should behave the same way as add_file. but added file should be owned by the user with user_id. A new file cannot be added to the storage if doing so will exceed the user's capacity limit. Returns the remaining storage capacity for user_id if the file is successfully added or null if otherwise

//     update_capacity(user_id: string, capacity: number) -> number | null : should change maximum storage capacity for the user with user_id. if the total size of all user's file exceeds the new capacity, the largest file (sorted lexicohgraphically in case of a tie) should be removed from the storage until the total size of all remaining files will no longer exceed the new capacity. Returns the number of removed files, or null if user with user_id does not exists

interface fileMetadata {
    name: string;
    size: number;
    username?: string;
}

interface userMetadata {
    name: string;
    capacity: number;
}


class CloudStorage {
    private fileStorage: Map<string, fileMetadata>;
    private userStorage: Map<string, userMetadata>;

    constructor() {
        this.fileStorage = new Map();
        this.userStorage = new Map();
    }

    private get_file(filename: string) : fileMetadata | null {
        const metadata = this.fileStorage.get(filename);
        return metadata ? metadata : null;
    }
    private set_file(filename: string, size: number, username?: string) : void {
        this.fileStorage.set(filename, this.create_metadata(filename, size, username))
    }
    private delete_file(filename: string) : fileMetadata | null {
        const metadata = this.get_file(filename);
        if (metadata == null) { return null }
        this.fileStorage.delete(metadata.name)
        return metadata
    }
    // define metadata type here
    private create_metadata(name: string, size: number, username?: string) : fileMetadata {
        return {
            name,
            size,
            username
        }
    }
    
    private get_user(username: string) : userMetadata | null {
        const metadata = this.userStorage.get(username);
        return metadata ? metadata : null;
    }
    private set_user(username: string, size: number) : void {
        this.userStorage.set(username, this.create_user_metadata(username, size))
    }
    // define user metadata type here
    private create_user_metadata(name: string, capacity: number) : userMetadata {
        return {
            name,
            capacity
        }
    }
    private get_files_by_username(username: string): fileMetadata[] {
        const userMetadata = this.get_user(username);
        const res: fileMetadata[] = [];
        if (userMetadata == null) {
            return res;
        }

        this.fileStorage.forEach((fileMetadata, filename) => {
            if (fileMetadata.username && fileMetadata.username == userMetadata.name) {
                res.push(fileMetadata)
            }
        })

        return res;
    }

    // Level 1
    add_file(filename: string, size: number) {
        if (this.get_file(filename) != null) {
            return false
        }
        this.set_file(filename, size)
        return true
    }

    copy_file(name_from: string, name_to: string) {
        const fileFrom = this.get_file(name_from)
        if (fileFrom == null) {
            return false
        }
        if (this.get_file(name_to) != null) {
            return false
        } 
        this.set_file(name_to, fileFrom.size)
        return true
    }

    get_file_size(filename: string) : number | null {
        return this.get_file(filename)?.size ?? null;
    }

    // Level 2
    find_file(prefix: string, suffix: string): string[] {
        const res: fileMetadata[] = []

        this.fileStorage.forEach((metadata, _) => {
            if (metadata.name.startsWith(prefix) && metadata.name.endsWith(suffix)) {
                res.push(metadata)
            }
        })
        res.sort(this.sort_by_size_then_filename)
        return res.map((metadata) => metadata.name)
    }

    private sort_by_size_then_filename(a: any, b: any) {
        const filenameComparison = a.name.localeCompare(b.name);
        const sizeComparison = b.size - a.size;
        return sizeComparison != 0 ? sizeComparison : filenameComparison
    }

    // Level 3
    // should add a new user to the system, with capacity as their storage limit in bytes. The total size of all files owned by user_id cannot exceed capacity. The operation fails if a user user_id already exists. Returns true if a user successfully created, false otherwise
    add_user(username: string, capacity: number) {
        if (this.get_user(username) != null) {
            return false
        }
        this.set_user(username, capacity)
        return true}


    // should behave the same way as add_file. but added file should be owned by the user with user_id. A new file cannot be added to the storage if doing so will exceed the user's capacity limit. Returns the remaining storage capacity for user_id if the file is successfully added or null if otherwise
    add_file_by(username: string, filename: string, size: number) : number | null {
        const remainingCapacity = this.getRemainingCapacity(username);
        if (remainingCapacity == null || remainingCapacity < size) { return null }

        // we have more space here, add file with user information
        this.set_file(filename, size, username);
        return remainingCapacity - size;

    }

    private getRemainingCapacity(username: string) : number | null {
        const userMetadata = this.get_user(username);
        if (userMetadata == null) { return null }

        const userFiles : fileMetadata[] = this.get_files_by_username(userMetadata.name);
        let remainingUsage = 0;
        userFiles.forEach((fileMetadata) => {
            remainingUsage += fileMetadata.size;
        })
        return userMetadata.capacity - remainingUsage;
    }

    
    // should change maximum storage capacity for the user with user_id. if the total size of all user's file exceeds the new capacity, the largest file (sorted lexicohgraphically in case of a tie) should be removed from the storage until the total size of all remaining files will no longer exceed the new capacity. Returns the number of removed files, or null if user with user_id does not exists
    update_capacity(username: string, newCapacity: number) {
        let remainingCapacity = this.getRemainingCapacity(username);
        // if user does not exists
        if (remainingCapacity == null) { return null }

        // of mew capacity is larger, we can update immediate without removing anything
        const userFiles : fileMetadata[] = this.get_files_by_username(username);
        userFiles.sort(this.sort_by_size_then_filename);

        // console.log(userFiles)

        let removedFile = 0;
        let currentUsage = this.get_user(username)!.capacity - remainingCapacity;
        while (newCapacity < currentUsage && userFiles.length > 0) {
            
            // console.log(newCapacity, currentUsage)
            const metadataToDelete = userFiles.shift();
            const deletedMetadata = this.delete_file(metadataToDelete!.name);
            currentUsage -= deletedMetadata!.size;
            removedFile += 1
        }
        this.set_user(username, newCapacity)
        return removedFile
    }

    // Level 4 potential
}

const cloudStorage = new CloudStorage();

console.log("\n\n --- Level 1 ---")
validate("Test Level 1 add file 2                      ", cloudStorage.add_file("/dir1/dir2/file.txt", 10), true);
validate("Test Level 1 copy non existent file          ", cloudStorage.copy_file("/non-existent-file.txt", "/dir1/file.txt"), false);
validate("Test Level 1 copy existent file              ", cloudStorage.copy_file("/dir1/dir2/file.txt", "/dir1/file.txt"), true);
validate("Test Level 1 add file 1                      ", cloudStorage.add_file("/dir1/file.txt", 15), false);
validate("Test Level 1 copy file to existing location  ", cloudStorage.copy_file("/dir1/file.txt", "/dir1/dir2/file.txt"), false);
validate("Test Level 1 get existing file size          ", cloudStorage.get_file_size("/dir1/file.txt"), 10);
validate("Test Level 1 get non existing file size      ", cloudStorage.get_file_size("/non-existent-file.txt"), null);

console.log("\n\n --- Level 2 ---")
validate("Test Level 2 add mp3 file 1                  ", cloudStorage.add_file("/root/dir/another_dir/file.mp3", 10), true);
validate("Test Level 2 add mp3 file 2                  ", cloudStorage.add_file("/root/file.mp3", 5), true);
validate("Test Level 2 add mp3 file 3                  ", cloudStorage.add_file("/root/music/file.mp3", 7), true);
validate("Test Level 2 copy file 3 to new location     ", cloudStorage.copy_file("/root/music/file.mp3", "/root/dir/file.mp3"), true);
validate("Test Level 2 find existing file              ", cloudStorage.find_file("/root", ".mp3").join(""), ["/root/dir/another_dir/file.mp3", "/root/dir/file.mp3", "/root/music/file.mp3", "/root/file.mp3"].join(""));
validate("Test Level 2 find non existing suffix        ", cloudStorage.find_file("/root", "file.txt").join(""), [].join(""));
validate("Test Level 2 find non existing               ", cloudStorage.find_file("/dir", "file.mp3").join(""), [].join(""));

console.log("\n\n --- Level 3 ---")
// Test: User Creation
validate("L3: Add user1                                 ", cloudStorage.add_user("user1", 100), true);
validate("L3: Add duplicate user1                       ", cloudStorage.add_user("user1", 50), false);
validate("L3: Add user2                                 ", cloudStorage.add_user("user2", 50), true);
// Test: Adding files with capacity limits
// user1 starts with 100 capacity
validate("L3: User1 adds file1 (60)                     ", cloudStorage.add_file_by("user1", "file1.txt", 60), 40); 
validate("L3: User1 adds file2 (50) - fails (exceeds)   ", cloudStorage.add_file_by("user1", "file2.txt", 50), null); 
validate("L3: Non-existent user adds file               ", cloudStorage.add_file_by("ghost", "file3.txt", 10), null);
validate("L3: User2 adds file (30)                      ", cloudStorage.add_file_by("user2", "file_u2.txt", 30), 20);
// Test: Capacity Update (No eviction needed)
validate("L3: Increase user1 capacity                   ", cloudStorage.update_capacity("user1", 150), 0);
validate("L3: Update non-existent user                  ", cloudStorage.update_capacity("ghost", 100), null);
// Test: Capacity Update (Eviction logic)
// Setup: user1 current total is 60 (file1.txt). Add more to test eviction order.
validate("L3: User1 adds abc.txt (20)                   ", cloudStorage.add_file_by("user1", "abc.txt", 20), 70); // 150 - 80 = 70
validate("L3: User1 adds xyz.txt (20)                   ", cloudStorage.add_file_by("user1", "xyz.txt", 20), 50); // 150 - 100 = 50
// Current user1: file1.txt(60), abc.txt(20), xyz.txt(20). Total = 100.
// Shrink user1 to 50:
// 1. file1.txt (60) is the largest. It must be removed.
// 2. New total is 40 (20+20). 40 <= 50. Stop. Result = 1 file removed.
validate("L3: Shrink user1 to 50 (evict 1)              ", cloudStorage.update_capacity("user1", 50), 1);
validate("L3: Verify file1 is gone                      ", cloudStorage.get_file_size("file1.txt"), null);
// Test: Tie-break Eviction (Largest size, then Lexicographical)
// Current user1: abc.txt(20), xyz.txt(20). Total = 40.
// Shrink user1 to 10:
// 1. Sizes are tied (20 vs 20). Lexicographically "xyz.txt" > "abc.txt". Remove xyz.txt.
// 2. Remaining total is 20. Still > 10. Remove abc.txt.
// Total removed: 2.
validate("L3: Shrink user1 to 10 (evict 2 via tie-break)", cloudStorage.update_capacity("user1", 10), 2);
validate("L3: Verify abc is gone                        ", cloudStorage.get_file_size("abc.txt"), null);
validate("L3: Verify xyz is gone                        ", cloudStorage.get_file_size("xyz.txt"), null);
