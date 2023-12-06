import React, { useContext } from 'react';
import { Text, View } from 'react-native';

import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import { AuthContext } from './context/AuthContext';
import SplashScreen from './screens/SplashScreen';
import Login from './screens/auth/login';
import Signup from './screens/auth/SignUp';
import FeedScreen from './screens/FeedScreen';
import ProfileScreen from './screens/ProfileScreen';
import OpenCamera from './screens/auth/openCamera';
import SearchHomeScreen from './screens/search';

const Stack = createNativeStackNavigator();

const Navigation = () => {
  const { log, splashLoading } = useContext(AuthContext);
  return (
    <NavigationContainer>
      <Stack.Navigator>
        {splashLoading ? (
          <Stack.Screen
            name="Splash Screen"
            component={SplashScreen}
            options={{ headerShown: false }}
          />
        ) : log  ? (
        <>
            <Stack.Screen options={{ headerShown: false }} name="FeedScreen" component={FeedScreen} />
            <Stack.Screen options={{ headerShown: false }} name="Profile" component={ProfileScreen} />
            <Stack.Screen options={{ headerShown: false }} name="Search" component={SearchHomeScreen} />
          </>) : (
          <>
            <Stack.Screen options={{ headerShown: false }} name="Login" component={Login} />
            <Stack.Screen options={{ headerShown: false }} name="signup" component={Signup} />
            <Stack.Screen options={{ headerShown: false }} name="openCamera" component={OpenCamera} />

          </>
        )}
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default Navigation;
