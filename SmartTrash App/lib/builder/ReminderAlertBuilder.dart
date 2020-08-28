import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:hello_world/actions/actions.dart';
import 'package:hello_world/main.dart';
import 'package:hello_world/models/index.dart';
import 'package:hello_world/store/store.dart';
import 'package:hello_world/utils/notificationHelper.dart';

import 'ReminderCustomItem.dart';
import 'ReminderItem.dart';

const String everyday = 'Take trash out every day';
const String weekly = 'Take trash out weekly';
const String custom = 'Custom time to take out';

const remindersIcons = {
  everyday: Icons.restore_from_trash,
  weekly: Icons.restore,
  custom: Icons.event_note,
};

class ReminderAlertBuilder extends StatefulWidget {
  ReminderAlertBuilder({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _ReminderAlertBuilderState createState() => _ReminderAlertBuilderState();
}

class _ReminderAlertBuilderState extends State<ReminderAlertBuilder> {
  bool everyDayReminder = false;
  bool everyWeekReminder = false;
  bool customReminder = false;
  double margin = Platform.isIOS ? 10 : 5;

  TimeOfDay customNotificationTime;
  DateTime customNotificationDate;

  @override
  Widget build(BuildContext context) {
    _prepareState();
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          RaisedButton(
            child: Text('Trash reminders'),
            color: Colors.black45,
            onPressed: _showMaterialDialog,
            textColor: Colors.white,
          ),
        ],
      ),
    );
  }

  _showMaterialDialog() {
    showDialog(
        context: context,
        barrierDismissible: true,
        builder: (BuildContext context) {
          return AlertDialog(
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.all(Radius.circular(10.0))),
              contentPadding: EdgeInsets.all(0.0),
              backgroundColor: Colors.grey,
              content: StatefulBuilder(
                  builder: (BuildContext context, StateSetter setState) {
                return Center(
                  child: Container(
                    width: MediaQuery.of(context).size.width - 10,
                    height: MediaQuery.of(context).size.height - 80,
                    padding: EdgeInsets.all(20),
                    color: Colors.grey,
                    child: Column(
                      children: [
                        Padding(
                            padding: new EdgeInsets.only(bottom: margin),
                            child: Text(
                              'Remind me every day',
                              style: TextStyle(
                                  fontSize: 20,
                                  color: Colors.black,
                                  decoration: TextDecoration.none,
                                  fontWeight: FontWeight.w500),
                            )),
                        ReminderItem(
                          onChanged: (value) {
                            setState(() {
                              everyDayReminder = value;
                            });
                            _configureEveryDayReminder(value);
                          },
                          checkBoxValue: everyDayReminder,
                          iconName: everyday,
                        ),
                        Padding(
                            padding: new EdgeInsets.only(
                                bottom: margin, top: margin),
                            child: Text(
                              'Remind me every week',
                              style: TextStyle(
                                  fontSize: 20,
                                  color: Colors.black,
                                  decoration: TextDecoration.none,
                                  fontWeight: FontWeight.w500),
                            )),
                        ReminderItem(
                          onChanged: (value) {
                            setState(() {
                              everyWeekReminder = value;
                            });
                            _configureEveryWeekReminder(value);
                          },
                          checkBoxValue: everyWeekReminder,
                          iconName: weekly,
                        ),
                        Padding(
                            padding: new EdgeInsets.only(
                                bottom: margin, top: margin),
                            child: Text(
                              'Custom',
                              style: TextStyle(
                                  fontSize: 20,
                                  color: Colors.black,
                                  decoration: TextDecoration.none,
                                  fontWeight: FontWeight.w500),
                            )),
                        ReminderCustomItem(
                          checkBoxValue: customReminder,
                          iconName: custom,
                          onChanged: (value) {
                            setState(() {
                              customReminder = value;
                            });
                            _configureCustomReminder(value);
                          },
                          showTimeDialog: () {
                            _showTimeDialog(setState);
                          },
                        ),
                        Padding(
                          padding: new EdgeInsets.only(
                              top: margin * 2, bottom: margin),
                          child: RaisedButton(
                              color: Colors.black45,
                              onPressed: () {
                                Navigator.of(context).pop();
                              },
                              child: Text(
                                "SAVE",
                                style: TextStyle(color: Colors.white),
                              )),
                        )
                      ],
                    ),
                  ),
                );
              }));
        });
  }

  _showTimeDialog(StateSetter setState) async {
    DateTime selectedDate = await showDatePicker(
        context: context,
        initialDate: DateTime.now(),
        firstDate: DateTime.utc(DateTime.now().year),
        lastDate: DateTime.utc(2021)
    );
    TimeOfDay selectedTime = await showTimePicker(
      initialTime: TimeOfDay.now(),
      context: context,
    );

    setState(() {
      customNotificationDate = selectedDate;
      customNotificationTime = selectedTime;
      customReminder = true;
    });

    _configureCustomReminder(true);
  }

  _prepareState() {
    List<Reminder> list = getStore().state.remindersState.reminders;

    list.forEach((item) {
      switch (item.name) {
        case everyday:
          everyDayReminder = true;
          break;
        case weekly:
          everyWeekReminder = true;
          break;
        case custom:
          customReminder = true;
          break;
        default:
          return;
      }
    });
  }

  void _configureEveryDayReminder(bool value) {
    if (value) {
      getStore().dispatch(SetReminderAction(
          time: new DateTime(DateTime.now().year, DateTime.now().month,
              DateTime.now().day, 12, 30).toIso8601String(),
          name: everyday,
          repeat: RepeatInterval.Daily));

      scheduleNotificationPeriodically(flutterLocalNotificationsPlugin, '0',
          everyday, RepeatInterval.Daily);
    } else {
      turnOffNotificationById(flutterLocalNotificationsPlugin, 0);
      getStore().dispatch(RemoveReminderAction(everyday));
    }
  }

  void _configureEveryWeekReminder(bool value) {
    if (value) {
      getStore().dispatch(SetReminderAction(
          time: new DateTime(DateTime.now().year, DateTime.now().month,
              DateTime.now().day, 12, 30).toIso8601String(),
          name: weekly,
          repeat: RepeatInterval.Weekly));
      scheduleNotificationPeriodically(flutterLocalNotificationsPlugin, '1',
          weekly, RepeatInterval.Weekly);
    } else {
      getStore().dispatch(RemoveReminderAction(weekly));
      turnOffNotificationById(flutterLocalNotificationsPlugin, 1);
    }
  }

  void _configureCustomReminder(bool value) {
    if (customNotificationTime != null && customNotificationDate != null) {
      if (value) {
        var now = new DateTime.now();
        var notificationTime = new DateTime(customNotificationDate.year,
            customNotificationDate.month, customNotificationDate.day,
            customNotificationTime.hour , customNotificationTime.minute);

        getStore().dispatch(SetReminderAction(
            time: notificationTime.toIso8601String(),
            name: custom,
            repeat: RepeatInterval.Weekly));

        scheduleNotification(
            flutterLocalNotificationsPlugin, '2', custom, notificationTime);
      } else {
        getStore().dispatch(RemoveReminderAction(custom));
        turnOffNotificationById(flutterLocalNotificationsPlugin, 2);
      }
    }
  }
}
