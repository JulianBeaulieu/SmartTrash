import 'package:flutter/material.dart';
import 'package:hello_world/main.dart';
import 'package:hello_world/models/index.dart';

import 'ReminderAlertBuilder.dart';

class RemindersList extends StatelessWidget {
  final List<Reminder> reminders;
  RemindersList({this.reminders});

  @override
  Widget build(BuildContext context) {
    return ListView.separated(
        separatorBuilder: (context, index) {
          return Divider();
        },
        itemCount: reminders.length,
        itemBuilder: (context, index) {
          final item = reminders[index];
          return ListTile(
              title: Row(
                children: <Widget>[
                  Icon(
                    remindersIcons[item.name],
                    color: Colors.white,
                    size: 30.0,
                  ),
                  Text(item.name, style: TextStyle(color: Colors.white),)
                ],
              ),
              subtitle: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: <Widget>[
                    Padding(
                        padding: EdgeInsets.only(top: 10),
                        child: Row(
                          children: <Widget>[
                            Text(
                              "Start time: ",
                              style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white),
                            ),
                            Text(df.format(DateTime.parse(item.time)), style: TextStyle(color: Colors.white),),
                          ],
                        )),
                    Text(Reminder.parseRepeatIntervalToString(item.repeat), style: TextStyle(color: Colors.white),)
                  ]));
        });
    ;
  }
}
