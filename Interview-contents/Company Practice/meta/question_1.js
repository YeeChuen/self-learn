// function ValidityState(log, actual, expectation) {
//     const result = actual == expectation ? "PASSED" : "FAILED";
//     const message = ` [${log}] Result : ${result}, actual: ${actual}, expected: ${expectation}`;
//     console.log(message);
// }

// // Question 1:
// //     Implement a simple in-memory cloud storage system that maps files to their meta information in TypeScript. This cloud storage system should support operations below

// //     add_file(name: string, size: number) -> boolean : should add new file name to the storage. size is the amount of moemory required in bytes. this operation failes if a file with the same name exists. return true if added successfully, false otherwise.

// //     copy_file(name_from: string, name_to: string) -> boolean : should copy the file at name_from to name_to. this operation failes if name_from points to a file that does not exists or points to a directory. The operation failes if specifed file alredy exists at name_to. Returns True if the file was copied successfully, false otherwise.

// //     get_file_size(name: string) -> number | null : should return the size of the file name if exists, null otherwise.

// //     find_file(prefix: string, suffix: string) -> string[] : search for files with names starting with prefix and ending with suffix. Returns a list of strings representing all matching files in this format: ["<name_1>(<size_1>)", "<name_2>(<size_2>)", ......] . The output should be sorted in descending order of file sizes, in the case of ties, lexicographically. if no files match the required properties, should return an empty list

// //     add_user(user_id: string, capacity: int) -> bool : should add a new user to the system, with capacity as their storage limit in bytes. The total size of all files owned by user_id cannot exceed capacity. The operation fails if a user user_id already exists. Returns true if a user successfully created, false otherwise.

// //     add_file_by(user_id: string, name: string, size: number) -> number | null : should behave the same way as add_file. but added file should be owned by the user with user_id. A new file cannot be added to the storage if doing so will exceed the user's capacity limit. Returns the remaining storage capacityt for user_id if the file is successfully added or null if otherwise

// //     update_capacity(user_id: string, capacity: number) -> number | null : should change maximum storage capacity for the user with user_id. if the total size of all user's file exceeds the new capacity, the largest file (sorted lexicohgraphically in case of a tie) should be removed from the storage until the total size of all remaining files will no longer exceed the new capacity. Returns the number of removed files, or null if user with user_id does not exists

// class CloudStorage {
//     constructor() {
//         this.fileStorage = new Map();
//     }

//     #get_file(filename) {
//         return this.fileStorage.has(filename) ? this.fileStorage.get(filename) : null;
//     }
//     #set_file(filename, metadata) {
//         this.fileStorage.set(filename, metadata)
//     }

//     // define metadata type here
//     #create_metadata(filename, size) {
//         return {
//             name: filename,
//             size: size
//         }
//     }

//     // Level 1
//     add_file(filename, size) {
//         if (this.#get_file(filename) != null) {
//             return false
//         }
//         this.#set_file(filename, this.#create_metadata(filename, size))
//         return true
//     }

//     copy_file(name_from, name_to) {
//         if (this.#get_file(name_from) == null) {
//             return false
//         }
//         if (this.#get_file(name_to) != null) {
//             return false
//         }
//         this.#set_file(name_to, this.#create_metadata(name_to, this.#get_file(name_from).size))
//         return true
//     }

//     get_file_size(filename) {
//         return this.#get_file(filename)?.size ?? null;
//     }

//     // Level 2
//     find_file(prefix, suffix) {
//         const res = []
//         const metadatas = this.fileStorage.values();

//         metadatas.forEach((metadata) => {
//             if (metadata.name.startsWith(prefix) && metadata.name.endsWith(suffix)) {
//                 res.push(metadata)
//             }
//         })
//         res.sort((a, b) => {
//             const filenameComparison = a.name.localeCompare(b.name);
//             const sizeComparison = b.size - a.size;
//             return sizeComparison != 0 ? sizeComparison : filenameComparison
//         })
//         return res.map((metadata) => metadata.name)
//     }

//     // Level 3
//     add_user() {}

//     add_file_by() {}

//     update_capacity() {}

//     // Level 4 potential
// }

// const cloudStorage = new CloudStorage();

// ValidityState("Test Level 1", cloudStorage.add_file("/dir1/dir2/file.txt", 10), true);
// ValidityState("Test Level 1", cloudStorage.copy_file("/non-existent-file.txt", "/dir1/file.txt"), false);
// ValidityState("Test Level 1", cloudStorage.copy_file("/dir1/dir2/file.txt", "/dir1/file.txt"), true);
// ValidityState("Test Level 1", cloudStorage.add_file("/dir1/file.txt", 15), false);
// ValidityState("Test Level 1", cloudStorage.copy_file("/dir1/file.txt", "/dir1/dir2/file.txt"), false);
// ValidityState("Test Level 1", cloudStorage.get_file_size("/dir1/file.txt"), 10);
// ValidityState("Test Level 1", cloudStorage.get_file_size("/non-existent-file.txt"), null);

// ValidityState("Test Level 2", cloudStorage.add_file("/root/dir/another_dir/file.mp3", 10), true);
// ValidityState("Test Level 2", cloudStorage.add_file("/root/file.mp3", 5), true);
// ValidityState("Test Level 2", cloudStorage.add_file("/root/music/file.mp3", 7), true);
// ValidityState("Test Level 2", cloudStorage.copy_file("/root/music/file.mp3", "/root/dir/file.mp3"), true);
// ValidityState("Test Level 2", cloudStorage.find_file("/root", ".mp3").join(""), ["/root/dir/another_dir/file.mp3", "/root/dir/file.mp3", "/root/music/file.mp3", "/root/file.mp3"].join(""));
// ValidityState("Test Level 2", cloudStorage.find_file("/root", "file.txt").join(""), [].join(""));
// ValidityState("Test Level 2", cloudStorage.find_file("/dir", "file.mp3").join(""), [].join(""));