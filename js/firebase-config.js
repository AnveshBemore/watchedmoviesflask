// firebase-config.js
import firebase from "firebase/app";
import "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyCng2oD2_aSt18pmUa_LHKow_NpHDx5reY",
  authDomain: "watchedmovies-4e47c.firebaseapp.com",
  databaseURL: "https://watchedmovies-4e47c-default-rtdb.firebaseio.com",
  projectId: "watchedmovies-4e47c",
  storageBucket: "watchedmovies-4e47c.firebasestorage.app",
  messagingSenderId: "796319630373",
  appId: "1:796319630373:web:86385b893380d585cdabcc",
  measurementId: "G-64SLDWWTCG"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();

// Export the db variable so you can use it in other files
export { db };
