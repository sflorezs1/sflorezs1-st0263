import mongoose from 'mongoose';
import colors from 'colors';

const connectDB = async () => {

    try {
        const conn = await mongoose.connect(process.env.URL_DB_CONNECTION, {
            useUnifiedTopology: true,
            useNewUrlParser: true,
            useCreateIndex: true,
            replset: {
                auto_reconnect: true,
                ssl: false,
                sslValidate: false,
                socketOptions: {
                    keepAlive: 1000,
                    connectTimeoutMS: 30000
                },
                poolSize: 10
            },
            server: {
                poolSize: 5,
                socketOptions: {
                    keepAlive: 1000,
                    connectTimeoutMS: 30000
                }
            }
        })

        console.log(`MongoDB is connected:${conn.connection.host}`.yellow)
        console.log('MongoDB_URL=', process.env.URL_DB_CONNECTION)
    } catch (error) {
        console.log(`Error to conect to MongoDB: ${error.message}`.red.bold)
        process.exit(1)
    }
}

export default connectDB