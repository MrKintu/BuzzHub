import * as React from 'react';
import {StatusBar, Text, View} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import Navigation from './src/Navigation';
import {AuthProvider} from './src/context/AuthContext';




const Stack = createNativeStackNavigator();

function App() {
  return (
    <AuthProvider>
    <StatusBar backgroundColor="#06bcee" />
    <Navigation />
  </AuthProvider>
  );
}

export default App;