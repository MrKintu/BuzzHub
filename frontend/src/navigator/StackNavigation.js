import React from 'react';
import Login from '../screens/auth/login';
import Signup from '../screens/auth/SignUp';
import { createStackNavigator } from '@react-navigation/stack';
import { NavigationContainer } from '@react-navigation/native';


const Stack = createStackNavigator();

function StackNav() {
    return (
        <NavigationContainer>
            <Stack.Navigator initialroutename="Login">
                <Stack.Screen  name="Login" component={Login} options={{title:"lll"}} />
                <Stack.Screen name="SignUp" component={Signup} />
            </Stack.Navigator>
        </NavigationContainer>

    );
}

export default StackNav;


