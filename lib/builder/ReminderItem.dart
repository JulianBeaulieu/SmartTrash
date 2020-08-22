import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

import 'ReminderAlertBuilder.dart';

class ReminderItem extends StatelessWidget {
  final bool checkBoxValue;
  final void Function(bool) onChanged;
  final String iconName;

  ReminderItem({this.checkBoxValue, this.onChanged, this.iconName});

  Widget build(BuildContext context) {
    double margin = Platform.isIOS ? 10 : 5;

    return Card(
        margin: new EdgeInsets.only(left: 0, right: 0, top: margin),
        color: Colors.black45,
        child: CheckboxListTile(
            value: checkBoxValue,
            onChanged: onChanged,
            checkColor: Colors.black,
            activeColor: Colors.white,
            title: Row(children: <Widget>[
              Row(
                children: <Widget>[
                  Icon(
                    remindersIcons[iconName],
                    color: Colors.white,
                    size: 30.0,
                  ),
                  Padding(
                      padding: new EdgeInsets.only(left: margin),
                      child: Text(
                        iconName,
                        style: TextStyle(
                            fontSize: 16,
                            color: Colors.white,
                            decoration: TextDecoration.none,
                            fontWeight: FontWeight.normal),
                      ))
                ],
              )
            ])));
  }
}
