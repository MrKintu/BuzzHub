import React, {Component} from 'react';
import {Text, View, TouchableOpacity, StyleSheet} from 'react-native';
import { AppColor } from "../utils/appColors";

export class PrimaryButton extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    const {buttonBg, text, label} = this.props;

    const buttonBackground = buttonBg || AppColor.primary;
    const textColor = text || AppColor.secondary;
    const textLabel = label;

    return (
      <View style={styles.container}>
        <TouchableOpacity
          style={[styles.button, {backgroundColor: buttonBackground}]}>
          <Text style={[styles.text, {color: textColor}]}>{textLabel}</Text>
        </TouchableOpacity>
      </View>
    );
  }
}

export default PrimaryButton;

export const styles = StyleSheet.create({
  container: {
    width: '100%',
  },
  button: {
    backgroundColor: AppColor.primary,
    padding: 15,
    borderRadius: 5,
  },
  text: {
    color: AppColor.secondary,
    textAlign: 'center',
  },
});
