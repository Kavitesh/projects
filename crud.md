# MongoDB CRUD Tutorial with Hello World Example

This tutorial walks through basic **CRUD (Create, Read, Update, Delete)** operations in MongoDB using the `mongosh` (MongoDB Shell). We will work with a simple "Hello, World!" message and perform database operations on it.

---

## 📦 Prerequisites

- MongoDB installed locally or accessible remotely.
- `mongosh` command line shell installed.
- Basic familiarity with command line.

---

## 🔹 Step 1: Connect to MongoDB

Open your terminal and start the MongoDB shell:

```bash
mongosh
```

---

## 🛠️ Step 2: Use or Create a Database

We’ll use a database called `helloWorldDB`. If it doesn’t exist, MongoDB will create it automatically when we insert data.

```javascript
use helloWorldDB;
```

---

## 🟢 Step 3: Create (Insert) a Document

Create a new collection called `messages` and insert a document with the message "Hello, World!".

```javascript
db.messages.insertOne({
  message: "Hello, World!",
  author: "User",
  createdAt: new Date()
});
```

### ✅ Output:

```
{
  acknowledged: true,
  insertedId: ObjectId("...")
}
```

---

## 🔍 Step 4: Read (Find) Documents

### 🔸 Find a Single Document:

```javascript
db.messages.findOne({ author: "User" });
```

### 🔸 Find All Documents:

```javascript
db.messages.find().pretty();
```

This will display all documents in the `messages` collection in a readable format.

---

## ✏️ Step 5: Update a Document

Let’s update the message for the author `User`:

```javascript
db.messages.updateOne(
  { author: "User" }, // Filter condition
  { $set: { message: "Hello, MongoDB World!" } } // Update action
);
```

### ♻️ Verify the Update:

```javascript
db.messages.findOne({ author: "User" });
```

---

## 🗑️ Step 6: Delete a Document

Remove the message we inserted earlier:

```javascript
db.messages.deleteOne({ author: "User" });
```

### ♻️ Confirm Deletion:

```javascript
db.messages.find({ author: "User" });
```

This should return no results.

---

## 📚 Summary of Commands

| Operation | Command |
|----------|---------|
| Create   | `insertOne()` |
| Read     | `find()`, `findOne()` |
| Update   | `updateOne()` |
| Delete   | `deleteOne()` |

---

