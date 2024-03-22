const { MongoClient } = require('mongodb');

class DatabaseConnectionManager {
  constructor(uri) {
    this.uri = uri; // MongoDB URI
    this.client = new MongoClient(this.uri, { useNewUrlParser: true, useUnifiedTopology: true });
  }

  async connect() {
    try {
      await this.client.connect();
      console.log("Connected successfully to MongoDB");
      return this.client;
    } catch (err) {
      console.error(`Failed to connect to MongoDB: ${err}`);
      throw err; // Rethrow the error for handling by the caller
    }
  }

  async disconnect() {
    try {
      await this.client.close();
      console.log("Disconnected from MongoDB");
    } catch (err) {
      console.error(`Failed to disconnect from MongoDB: ${err}`);
      throw err; // Rethrow the error for handling by the caller
    }
  }

  // Utility function to get the database connection
  getDb(dbName) {
    if (!this.client.isConnected()) {
      throw new Error("Not connected to MongoDB");
    }
    return this.client.db(dbName);
  }
}

module.exports = DatabaseConnectionManager;
