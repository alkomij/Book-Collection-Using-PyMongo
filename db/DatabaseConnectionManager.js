require('dotenv').config();
const { MongoClient } = require('mongodb');

class DatabaseConnectionManager {
  constructor() {
    this.uri = process.env.MONGODB_URI;
    this.client = new MongoClient(this.uri, { useNewUrlParser: true, useUnifiedTopology: true });
  }

  async connect() {
    try {
      await this.client.connect();
      console.log("Connected successfully to MongoDB");
      return this.client;
    } catch (err) {
      console.error(`Failed to connect to MongoDB: ${err}`);
      throw err;
    }
  }

  async disconnect() {
    try {
      await this.client.close();
      console.log("Disconnected from MongoDB");
    } catch (err) {
      console.error(`Failed to disconnect from MongoDB: ${err}`);
      throw err;
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
