import React, {Component} from 'react';
import {Text, View, StyleSheet, TextInput} from 'react-native';

import Icon from 'react-native-vector-icons/FontAwesome';
import { AppColor } from "../utils/appColors";
export class PhoneInputForm extends Component {
  render() {
    return (
      <View style={styles.container}>
        <View style={styles.countryWrapper}>
          <Text style={styles.country}>IN +91</Text>
        </View>
        <View style={styles.inputNumber}>
          <TextInput value={'8086502009'} />
        </View>
        <View style={styles.closeBtnWrapper}>
          <Icon
            size={25}
            style={styles.icon}
            color={AppColor.gray}
            name={'times'}
          />
        </View>
      </View>
    );
  }
}

export default PhoneInputForm;

const styles = StyleSheet.create({
  container: {
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'center',
    borderWidth: 1,
    paddingLeft: 5,
    paddingRight: 5,
    borderRadius: 5,
    borderColor: AppColor.gray,
    backgroundColor: AppColor.gray1,
  },
  countryWrapper: {
    display: 'flex',
    borderRightWidth: 1,
    borderRightColor: AppColor.gray,
    paddingRight: 15,
  },
  country: {
    fontWeight: '700',
    color: AppColor.gray,
  },
  inputNumber: {
    display: 'flex',
    flex: 1,
    paddingLeft: 15,
  },
  closeBtnWrapper: {
    display: 'flex',
    flex: 1,
  },
  icon: {
    textAlign: 'right',
  },
});
