import * as React from 'react';
import { View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import Login from './src/screens/auth/login';
import Signup from './src/screens/auth/SignUp';
import FeedScreen from './src/screens/FeedScreen';
import ProfileScreen from './src/screens/ProfileScreen';
import OpenCamera from './src/screens/auth/openCamera';
import SearchHomeScreen from './src/screens/search';



const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator screenOptions={{ headerShown: false }}>
        <Stack.Screen name="Login" component={Login} />
        <Stack.Screen name="signup" component={OpenCamera} />
        <Stack.Screen name="FeedScreen" component={FeedScreen} />
        <Stack.Screen name="Profile" component={ProfileScreen} />
        <Stack.Screen name="Search" component={SearchHomeScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;