import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:hello_world/main.dart';
import 'package:hello_world/utils/notificationHelper.dart';
import 'package:hello_world/store/store.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:hello_world/actions/actions.dart';

const String custom = "test notification";
const reminderIcons = {
  custom: Icons.notifications_active,
};

bool swapper = false;

class TestBuilder extends StatefulWidget {
  TestBuilder({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _TestBuilderState createState() => _TestBuilderState();
}

class _TestBuilderState extends State<TestBuilder> {
  double margin = Platform.isIOS ? 10 : 5;

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          RaisedButton(
            child: Text('Test'),
            color: Colors.black45,
            onPressed: _TestBuilderButton,
            textColor: Colors.white,
          ),
        ],
      ),
    );
  }


  _TestBuilderButton() {
    if(swapper){
      getStore().dispatch(RemoveReminderAction(custom));
      turnOffNotificationById(flutterLocalNotificationsPlugin, 3);
      swapper = false;
    }
    else {
      swapper = true;
      var now = new DateTime.now();
      var notificationTime = new DateTime(now.year,
          now.month, now.day,
          now.hour, now.minute);

      getStore().dispatch(SetReminderAction(
          time: notificationTime.toIso8601String(),
          name: custom,
          repeat: RepeatInterval.Daily));

      scheduleNotification(
          flutterLocalNotificationsPlugin, '3', custom, notificationTime);
      new Future.delayed(const Duration(seconds: 4), () =>
          pubnub.publish('Trash-Client', {"requester": "App", "trigger": "trashDay",
            "status": 1}));
    }
  }
}