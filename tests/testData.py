from collections import OrderedDict

rawTimetableData = {'new': False, 'showModal': False, 'showSpaceConstraintModal': False, 'key': '-LoKHh_LxFPCe8aA-h-N', 'step': 7, 'name': 'test 4', 'days':['Monday', 'Tuesday', 'Wednesday', 'Thursday'], 'numberOfPeriodsPerDay': 6, 'periods': {'period1': '8', 'period2': '9', 'period3': '10', 'period4': '11', 'period5': '12', 'period6': '13'}, 'numberOfSubjects': 1, 'subjects': {'data': [{'key': 1, 'room': 'B101', 'subject': 'maths'}, {'key': 11, 'room': 'A101', 'subject': 'physics'}, {'key': 21, 'room': 'B101', 'subject': 'chemistry'}], 'keyList': [1, 11, 21]}, 'teachers': {'data': [{'key': 1, 'targetNumberOfHours': 0, 'teacher': 'teacher1'}, {'key': 11, 'targetNumberOfHours': 0, 'teacher': 'teacher2'}], 'keyList': [1, 11]}, 'students': {'data': [{'key': 1, 'number': '50', 'students': '2019'}, {'key': 11, 'number': '50', 'students': '2020'}], 'keyList': [1, 11]}, 'tags': {'data': [{'key': 1, 'tag': 'tag1'}], 'keyList': [1]}, 'newActivity': {'error': None, 'split': 1, 'active': True, 'selectedSubject': '', 'selectedTeachers': [], 'selectedTags': [], 'selectedStudents': [], 'durations': {'duration_1': 1}}, 'activities': {'data': [{'active': 'true', 'children': [{'active': 'true', 'duration': '1', 'durations': {'duration_1': 1}, 'key': 2, 'students': [{'key': 11, 'number': '50', 'students': '2020'}], 'subject': 'maths', 'tags': [{'key': 1, 'tag': 'tag1'}], 'teachers': [{'key': 11, 'targetNumberOfHours': 0, 'teacher': 'teacher2'}]}], 'durations': {'duration_1': 1}, 'key': 1, 'students': [{'key': 11, 'number': '50', 'students': '2020'}], 'subject': 'maths', 'tags': [{'key': 1, 'tag': 'tag1'}], 'teachers': [{'key': 11, 'targetNumberOfHours': 0, 'teacher': 'teacher2'}], 'totalDuration': '1'}, {'active': 'true', 'children': [{'active': 'true', 'duration': '1', 'durations': {'duration_1': 1, 'duration_2': 1}, 'key': 4, 'students': [{'key': 11, 'number': '50', 'students': '2020'}], 'subject': 'physics', 'tags': [{'key': 1, 'tag': 'tag1'}], 'teachers': [{'key': 11, 'targetNumberOfHours': 0, 'teacher': 'teacher2'}]}, {'active': 'true', 'duration': '1', 'durations': {'duration_1': 1, 'duration_2': 1}, 'key': 5, 'students': [{'key': 11, 'number': '50', 'students': '2020'}], 'subject': 'physics', 'tags': [{'key': 1, 'tag': 'tag1'}], 'teachers': [{'key': 11, 'targetNumberOfHours': 0, 'teacher': 'teacher2'}]}], 'durations': {'duration_1': 1, 'duration_2': 1}, 'key': 3, 'students': [{'key': 11, 'number': '50', 'students': '2020'}], 'subject': 'physics', 'tags': [{'key': 1, 'tag': 'tag1'}], 'teachers': [{'key': 11, 'targetNumberOfHours': 0, 'teacher': 'teacher2'}], 'totalDuration': '2'}, {'active': 'true', 'children': [{'active': 'true', 'duration': '1', 'durations': {'duration_1': 1, 'duration_2': 1}, 'key': 7, 'students': [{'key': 1, 'number': '50', 'students': '2019'}], 'subject': 'physics', 'tags': [{'key': 1, 'tag': 'tag1'}], 'teachers': [{'key': 11, 'targetNumberOfHours': 0, 'teacher': 'teacher2'}]}, {'active': 'true', 'duration': '1', 'durations': {'duration_1': 1, 'duration_2': 1}, 'key': 8, 'students': [{'key': 1, 'number': '50', 'students': '2019'}], 'subject': 'physics', 'tags': [{'key': 1, 'tag': 'tag1'}], 'teachers': [{'key': 11, 'targetNumberOfHours': 0, 'teacher': 'teacher2'}]}], 'durations': {'duration_1': 1, 'duration_2': 1}, 'key': 6, 'students': [{'key': 1, 'number': '50', 'students': '2019'}], 'subject': 'physics', 'tags': [{'key': 1, 'tag': 'tag1'}], 'teachers': [{'key': 11, 'targetNumberOfHours': 0, 'teacher': 'teacher2'}], 'totalDuration': '2'}, {'active': 'true', 'children': [{'active': 'true', 'duration': '1', 'durations': {'duration_1': 1, 'duration_2': 1}, 'key': 10, 'students': [{'key': 1, 'number': '50', 'students': '2019'}], 'subject': 'maths', 'tags': [{'key': 1, 'tag': 'tag1'}], 'teachers': [{'key': 11, 'targetNumberOfHours': 0, 'teacher': 'teacher2'}]}, {'active': 'true', 'duration': '1', 'durations': {'duration_1': 1, 'duration_2': 1}, 'key': 11, 'students': [{'key': 1, 'number': '50', 'students': '2019'}], 'subject': 'maths', 'tags': [{'key': 1, 'tag': 'tag1'}], 'teachers': [{'key': 11, 'targetNumberOfHours': 0, 'teacher': 'teacher2'}]}], 'durations': {'duration_1': 1, 'duration_2': 1}, 'key': 9, 'students': [{'key': 1, 'number': '50', 'students': '2019'}], 'subject': 'maths', 'tags': [{'key': 1, 'tag': 'tag1'}], 'teachers': [{'key': 11, 'targetNumberOfHours': 0, 'teacher': 'teacher2'}], 'totalDuration': '2'}, {'active': 'true', 'children': [{'active': 'true', 'duration': '1', 'durations': {'duration_1': 1, 'duration_2': 1}, 'key': 13, 'students': [{'key': 1, 'number': '50', 'students': '2019'}], 'subject': 'chemistry', 'tags': [{'key': 1, 'tag': 'tag1'}], 'teachers': [{'key': 1, 'targetNumberOfHours': 0, 'teacher': 'teacher1'}]}, {'active': 'true', 'duration': '1', 'durations': {'duration_1': 1, 'duration_2': 1}, 'key': 14, 'students': [{'key': 1, 'number': '50', 'students': '2019'}], 'subject': 'chemistry', 'tags': [{'key': 1, 'tag': 'tag1'}], 'teachers': [{'key': 1, 'targetNumberOfHours': 0, 'teacher': 'teacher1'}]}], 'durations': {'duration_1': 1, 'duration_2': 1}, 'key': 12, 'students': [{'key': 1, 'number': '50', 'students': '2019'}], 'subject': 'chemistry', 'tags': [{'key': 1, 'tag': 'tag1'}], 'teachers': [{'key': 1, 'targetNumberOfHours': 0, 'teacher': 'teacher1'}], 'totalDuration': '2'}, {'active': 'true', 'children': [{'active': 'true', 'duration': '1', 'durations': {'duration_1': 1, 'duration_2': 1}, 'key': 16, 'students': [{'key': 11, 'number': '50', 'students': '2020'}], 'subject': 'chemistry', 'tags': [{'key': 1, 'tag': 'tag1'}], 'teachers': [{'key': 1, 'targetNumberOfHours': 0, 'teacher': 'teacher1'}]}, {'active': 'true', 'duration': '1', 'durations': {'duration_1': 1, 'duration_2': 1}, 'key': 17, 'students': [{'key': 11, 'number': '50', 'students': '2020'}], 'subject': 'chemistry', 'tags': [{'key': 1, 'tag': 'tag1'}], 'teachers': [{'key': 1, 'targetNumberOfHours': 0, 'teacher': 'teacher1'}]}], 'durations': {'duration_1': 1, 'duration_2': 1}, 'key': 15, 'students': [{'key': 11, 'number': '50', 'students': '2020'}], 'subject': 'chemistry', 'tags': [{'key': 1, 'tag': 'tag1'}], 'teachers': [{'key': 1, 'targetNumberOfHours': 0, 'teacher': 'teacher1'}], 'totalDuration': '2'}], 'error': '', 'keyList': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]}, 'buildings': {'data': [{'building': 'A', 'capacity': 100, 'key': 1}, {'building': 'B', 'capacity': 100, 'key': 11}], 'keyList': [1, 11]}, 'rooms': {'data': [{'building': 'A', 'capacity': '100', 'key': 1, 'room': 'A101'}, {'building': 'B', 'capacity': '100', 'key': 11, 'room': 'B101'}], 'keyList': [1, 11]}, 'finalTimetables': {'subgroups': [{'days': [{'hours': [{'activity_tag': [{'name': 'tag1'}], 'name': 8, 'subject': 'chemistry', 'teachers': [{'name': 'teacher1'}]}, {'empty': 'true', 'name': 9}, {'empty': 'true', 'name': 10}, {'empty': 'true', 'name': 11}, {'empty': 'true', 'name': 12}, {'activity_tag': [{'name': 'tag1'}], 'name': 13, 'subject': 'chemistry', 'teachers': [{'name': 'teacher1'}]}], 'name': 'Monday'}, {'hours': [{'activity_tag': [{'name': 'tag1'}], 'name': 8, 'subject': 'physics', 'teachers': [{'name': 'teacher2'}]}, {'empty': 'true', 'name': 9}, {'empty': 'true', 'name': 10}, {'empty': 'true', 'name': 11}, {'empty': 'true', 'name': 12}, {'activity_tag': [{'name': 'tag1'}], 'name': 13, 'subject': 'physics', 'teachers': [{'name': 'teacher2'}]}], 'name': 'Tuesday'}, {'hours': [{'empty': 'true', 'name': 8}, {'activity_tag': [{'name': 'tag1'}], 'name': 9, 'subject': 'maths', 'teachers': [{'name': 'teacher2'}]}, {'empty': 'true', 'name': 10}, {'empty': 'true', 'name': 11}, {'empty': 'true', 'name': 12}, {'empty': 'true', 'name': 13}], 'name': 'Wednesday'}, {'hours': [{'empty': 'true', 'name': 8}, {'empty': 'true', 'name': 9}, {'activity_tag': [{'name': 'tag1'}], 'name': 10, 'subject': 'maths', 'teachers': [{'name': 'teacher2'}]}, {'empty': 'true', 'name': 11}, {'empty': 'true', 'name': 12}, {'empty': 'true', 'name': 13}], 'name': 'Thursday'}], 'name': '2019 Automatic Group Automatic Subgroup'}, {'days': [{'hours': [{'activity_tag': [{'name': 'tag1'}], 'name': 8, 'subject': 'maths', 'teachers': [{'name': 'teacher2'}]}, {'activity_tag': [{'name': 'tag1'}], 'name': 9, 'subject': 'chemistry', 'teachers': [{'name': 'teacher1'}]}, {'empty': 'true', 'name': 10}, {'empty': 'true', 'name': 11}, {'empty': 'true', 'name': 12}, {'empty': 'true', 'name': 13}], 'name': 'Monday'}, {'hours': [{'empty': 'true', 'name': 8}, {'empty': 'true', 'name': 9}, {'activity_tag': [{'name': 'tag1'}], 'name': 10, 'subject': 'physics', 'teachers': [{'name': 'teacher2'}]}, {'empty': 'true', 'name': 11}, {'empty': 'true', 'name': 12}, {'empty': 'true', 'name': 13}], 'name': 'Tuesday'}, {'hours': [{'empty': 'true', 'name': 8}, {'empty': 'true', 'name': 9}, {'empty': 'true', 'name': 10}, {'empty': 'true', 'name': 11}, {'empty': 'true', 'name': 12}, {'empty': 'true', 'name': 13}], 'name': 'Wednesday'}, {'hours': [{'activity_tag': [{'name': 'tag1'}], 'name': 8, 'subject': 'physics', 'teachers': [{'name': 'teacher2'}]}, {'empty': 'true', 'name': 9}, {'empty': 'true', 'name': 10}, {'activity_tag': [{'name': 'tag1'}], 'name': 11, 'subject': 'chemistry', 'teachers': [{'name': 'teacher1'}]}, {'empty': 'true', 'name': 12}, {'empty': 'true', 'name': 13}], 'name': 'Thursday'}], 'name': '2020 Automatic Group Automatic Subgroup'}], 'teachers': [{'days': [{'hours': [{'activity_tag': [{'name': 'tag1'}], 'name': 8, 'students': [{'name': 2019}], 'subject': 'chemistry'}, {'activity_tag': [{'name': 'tag1'}], 'name': 9, 'students': [{'name': 2020}], 'subject': 'chemistry'}, {'empty': 'true', 'name': 10}, {'empty': 'true', 'name': 11}, {'empty': 'true', 'name': 12}, {'activity_tag': [{'name': 'tag1'}], 'name': 13, 'students': [{'name': 2019}], 'subject': 'chemistry'}], 'name': 'Monday'}, {'hours': [{'empty': 'true', 'name': 8}, {'empty': 'true', 'name': 9}, {'empty': 'true', 'name': 10}, {'empty': 'true', 'name': 11}, {'empty': 'true', 'name': 12}, {'empty': 'true', 'name': 13}], 'name': 'Tuesday'}, {'hours': [{'empty': 'true', 'name': 8}, {'empty': 'true', 'name': 9}, {'empty': 'true', 'name': 10}, {'empty': 'true', 'name': 11}, {'empty': 'true', 'name': 12}, {'empty': 'true', 'name': 13}], 'name': 'Wednesday'}, {'hours': [{'empty': 'true', 'name': 8}, {'empty': 'true', 'name': 9}, {'empty': 'true', 'name': 10}, {'activity_tag': [{'name': 'tag1'}], 'name': 11, 'students': [{'name': 2020}], 'subject': 'chemistry'}, {'empty': 'true', 'name': 12}, {'empty': 'true', 'name': 13}], 'name': 'Thursday'}], 'name': 'teacher1'}, {'days': [{'hours': [{'activity_tag': [{'name': 'tag1'}], 'name': 8, 'students': [{'name': 2020}], 'subject': 'maths'}, {'empty': 'true', 'name': 9}, {'empty': 'true', 'name': 10}, {'empty': 'true', 'name': 11}, {'empty': 'true', 'name': 12}, {'empty': 'true', 'name': 13}], 'name': 'Monday'}, {'hours': [{'activity_tag': [{'name': 'tag1'}], 'name': 8, 'students': [{'name': 2019}], 'subject': 'physics'}, {'empty': 'true', 'name': 9}, {'activity_tag': [{'name': 'tag1'}], 'name': 10, 'students': [{'name': 2020}], 'subject': 'physics'}, {'empty': 'true', 'name': 11}, {'empty': 'true', 'name': 12}, {'activity_tag': [{'name': 'tag1'}], 'name': 13, 'students': [{'name': 2019}], 'subject': 'physics'}], 'name': 'Tuesday'}, {'hours': [{'empty': 'true', 'name': 8}, {'activity_tag': [{'name': 'tag1'}], 'name': 9, 'students': [{'name': 2019}], 'subject': 'maths'}, {'empty': 'true', 'name': 10}, {'empty': 'true', 'name': 11}, {'empty': 'true', 'name': 12}, {'empty': 'true', 'name': 13}], 'name': 'Wednesday'}, {'hours': [{'activity_tag': [{'name': 'tag1'}], 'name': 8, 'students': [{'name': 2020}], 'subject': 'physics'}, {'empty': 'true', 'name': 9}, {'activity_tag': [{'name': 'tag1'}], 'name': 10, 'students': [{'name': 2019}], 'subject': 'maths'}, {'empty': 'true', 'name': 11}, {'empty': 'true', 'name': 12}, {'empty': 'true', 'name': 13}], 'name': 'Thursday'}], 'name': 'teacher2'}]}, 'finalTimetablesDataMap': {'subgroups': {'2019 Automatic Group Automatic Subgroup': {'Monday_10': 'NA', 'Monday_11': 'NA', 'Monday_12': 'NA', 'Monday_13': 'chemistry by teacher1 ', 'Monday_8': 'chemistry by teacher1 ', 'Monday_9': 'NA', 'Thursday_10': 'maths by teacher2 ', 'Thursday_11': 'NA', 'Thursday_12': 'NA', 'Thursday_13': 'NA', 'Thursday_8': 'NA', 'Thursday_9': 'NA', 'Tuesday_10': 'NA', 'Tuesday_11': 'NA', 'Tuesday_12': 'NA', 'Tuesday_13': 'physics by teacher2 ', 'Tuesday_8': 'physics by teacher2 ', 'Tuesday_9': 'NA', 'Wednesday_10': 'NA', 'Wednesday_11': 'NA', 'Wednesday_12': 'NA', 'Wednesday_13': 'NA', 'Wednesday_8': 'NA', 'Wednesday_9': 'maths by teacher2 '}, '2020 Automatic Group Automatic Subgroup': {'Monday_10': 'NA', 'Monday_11': 'NA', 'Monday_12': 'NA', 'Monday_13': 'NA', 'Monday_8': 'maths by teacher2 ', 'Monday_9': 'chemistry by teacher1 ', 'Thursday_10': 'NA', 'Thursday_11': 'chemistry by teacher1 ', 'Thursday_12': 'NA', 'Thursday_13': 'NA', 'Thursday_8': 'physics by teacher2 ', 'Thursday_9': 'NA', 'Tuesday_10': 'physics by teacher2 ', 'Tuesday_11': 'NA', 'Tuesday_12': 'NA', 'Tuesday_13': 'NA', 'Tuesday_8': 'NA', 'Tuesday_9': 'NA', 'Wednesday_10': 'NA', 'Wednesday_11': 'NA', 'Wednesday_12': 'NA', 'Wednesday_13': 'NA', 'Wednesday_8': 'NA', 'Wednesday_9': 'NA'}}, 'teachers': {'teacher1': {'Monday_10': 'NA', 'Monday_11': 'NA', 'Monday_12': 'NA', 'Monday_13': 'chemistry by 2019 ', 'Monday_8': 'chemistry by 2019 ', 'Monday_9': 'chemistry by 2020 ', 'Thursday_10': 'NA', 'Thursday_11': 'chemistry by 2020 ', 'Thursday_12': 'NA', 'Thursday_13': 'NA', 'Thursday_8': 'NA', 'Thursday_9': 'NA', 'Tuesday_10': 'NA', 'Tuesday_11': 'NA', 'Tuesday_12': 'NA', 'Tuesday_13': 'NA', 'Tuesday_8': 'NA', 'Tuesday_9': 'NA', 'Wednesday_10': 'NA', 'Wednesday_11': 'NA', 'Wednesday_12': 'NA', 'Wednesday_13': 'NA', 'Wednesday_8': 'NA', 'Wednesday_9': 'NA'}, 'teacher2': {'Monday_10': 'NA', 'Monday_11': 'NA', 'Monday_12': 'NA', 'Monday_13': 'NA', 'Monday_8': 'maths by 2020 ', 'Monday_9': 'NA', 'Thursday_10': 'maths by 2019 ', 'Thursday_11': 'NA', 'Thursday_12': 'NA', 'Thursday_13': 'NA', 'Thursday_8': 'physics by 2020 ', 'Thursday_9': 'NA', 'Tuesday_10': 'physics by 2020 ', 'Tuesday_11': 'NA', 'Tuesday_12': 'NA', 'Tuesday_13': 'physics by 2019 ', 'Tuesday_8': 'physics by 2019 ', 'Tuesday_9': 'NA', 'Wednesday_10': 'NA', 'Wednesday_11': 'NA', 'Wednesday_12': 'NA', 'Wednesday_13': 'NA', 'Wednesday_8': 'NA', 'Wednesday_9': 'maths by 2019 '}}}, 'finalTimetablesOrders': {'subgroups': {'2019 Automatic Group Automatic Subgroup': ['Monday_8', 'Tuesday_8', 'Wednesday_8', 'Thursday_8', 'Monday_9', 'Tuesday_9', 'Wednesday_9', 'Thursday_9', 'Monday_10', 'Tuesday_10', 'Wednesday_10', 'Thursday_10', 'Monday_11', 'Tuesday_11', 'Wednesday_11', 'Thursday_11', 'Monday_12', 'Tuesday_12', 'Wednesday_12', 'Thursday_12', 'Monday_13', 'Tuesday_13', 'Wednesday_13', 'Thursday_13'], '2020 Automatic Group Automatic Subgroup': ['Monday_8', 'Tuesday_8', 'Wednesday_8', 'Thursday_8', 'Monday_9', 'Tuesday_9', 'Wednesday_9', 'Thursday_9', 'Monday_10', 'Tuesday_10', 'Wednesday_10', 'Thursday_10', 'Monday_11', 'Tuesday_11', 'Wednesday_11', 'Thursday_11', 'Monday_12', 'Tuesday_12', 'Wednesday_12', 'Thursday_12', 'Monday_13', 'Tuesday_13', 'Wednesday_13', 'Thursday_13']}, 'teachers': {'teacher1': ['Monday_8', 'Tuesday_8', 'Wednesday_8', 'Thursday_8', 'Monday_9', 'Tuesday_9', 'Wednesday_9', 'Thursday_9', 'Monday_10', 'Tuesday_10', 'Wednesday_10', 'Thursday_10', 'Monday_11', 'Tuesday_11', 'Wednesday_11', 'Thursday_11', 'Monday_12', 'Tuesday_12', 'Wednesday_12', 'Thursday_12', 'Monday_13', 'Tuesday_13', 'Wednesday_13', 'Thursday_13'], 'teacher2': ['Monday_8', 'Tuesday_8', 'Wednesday_8', 'Thursday_8', 'Monday_9', 'Tuesday_9', 'Wednesday_9', 'Thursday_9', 'Monday_10', 'Tuesday_10', 'Wednesday_10', 'Thursday_10', 'Monday_11', 'Tuesday_11', 'Wednesday_11', 'Thursday_11', 'Monday_12', 'Tuesday_12', 'Wednesday_12', 'Thursday_12', 'Monday_13', 'Tuesday_13', 'Wednesday_13', 'Thursday_13']}}, 'lastModifiedTime': '9/18/2019, 4:19:55 PM', 'showGeneratedTimetable': 'subgroups', 'showSubgroupTimetable': '2019 Automatic Group Automatic Subgroup'}

# subgroup for student data
subgroupTeacher = [OrderedDict([('@name', 'teacher1'), ('Day', [OrderedDict([('@name', 'Monday'), ('Hour', [OrderedDict([('@name', 8)]), OrderedDict([('@name', 9), ('Subject', OrderedDict([('@name', 'chemistry')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Students', OrderedDict([('@name', 2019)])), ('Room', OrderedDict([('@name', 'B101')]))]), OrderedDict([('@name', 10)]), OrderedDict([('@name', 11)]), OrderedDict([('@name', 12)]), OrderedDict([('@name', 13)])])]), OrderedDict([('@name', 'Tuesday'), ('Hour', [OrderedDict([('@name', 8)]), OrderedDict([('@name', 9)]), OrderedDict([('@name', 10), ('Subject', OrderedDict([('@name', 'chemistry')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Students', OrderedDict([('@name', 2020)])), ('Room', OrderedDict([('@name', 'B101')]))]), OrderedDict([('@name', 11)]), OrderedDict([('@name', 12)]), OrderedDict([('@name', 13)])])]), OrderedDict([('@name', 'Wednesday'), ('Hour', [OrderedDict([('@name', 8)]), OrderedDict([('@name', 9)]), OrderedDict([('@name', 10)]), OrderedDict([('@name', 11)]), OrderedDict([('@name', 12)]), OrderedDict([('@name', 13)])])]), OrderedDict([('@name', 'Thursday'), ('Hour', [OrderedDict([('@name', 8)]), OrderedDict([('@name', 9)]), OrderedDict([('@name', 10)]), OrderedDict([('@name', 11)]), OrderedDict([('@name', 12), ('Subject', OrderedDict([('@name', 'chemistry')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Students', OrderedDict([('@name', 2019)])), ('Room', OrderedDict([('@name', 'B101')]))]), OrderedDict([('@name', 13), ('Subject', OrderedDict([('@name', 'chemistry')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Students', OrderedDict([('@name', 2020)])), ('Room', OrderedDict([('@name', 'B101')]))])])])])]), OrderedDict([('@name', 'teacher2'), ('Day', [OrderedDict([('@name', 'Monday'), ('Hour', [OrderedDict([('@name', 8)]), OrderedDict([('@name', 9)]), OrderedDict([('@name', 10), ('Subject', OrderedDict([('@name', 'maths')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Students', OrderedDict([('@name', 2020)])), ('Room', OrderedDict([('@name', 'B101')]))]), OrderedDict([('@name', 11), ('Subject', OrderedDict([('@name', 'maths')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Students', OrderedDict([('@name', 2019)])), ('Room', OrderedDict([('@name', 'B101')]))]), OrderedDict([('@name', 12)]), OrderedDict([('@name', 13), ('Subject', OrderedDict([('@name', 'physics')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Students', OrderedDict([('@name', 2020)])), ('Room', OrderedDict([('@name', 'A101')]))])])]), OrderedDict([('@name', 'Tuesday'), ('Hour', [OrderedDict([('@name', 8)]), OrderedDict([('@name', 9)]), OrderedDict([('@name', 10)]), OrderedDict([('@name', 11), ('Subject', OrderedDict([('@name', 'physics')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Students', OrderedDict([('@name', 2020)])), ('Room', OrderedDict([('@name', 'A101')]))]), OrderedDict([('@name', 12)]), OrderedDict([('@name', 13)])])]), OrderedDict([('@name', 'Wednesday'), ('Hour', [OrderedDict([('@name', 8)]), OrderedDict([('@name', 9)]), OrderedDict([('@name', 10), ('Subject', OrderedDict([('@name', 'physics')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Students', OrderedDict([('@name', 2019)])), ('Room', OrderedDict([('@name', 'A101')]))]), OrderedDict([('@name', 11)]), OrderedDict([('@name', 12)]), OrderedDict([('@name', 13), ('Subject', OrderedDict([('@name', 'maths')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Students', OrderedDict([('@name', 2019)])), ('Room', OrderedDict([('@name', 'B101')]))])])]), OrderedDict([('@name', 'Thursday'), ('Hour', [OrderedDict([('@name', 8), ('Subject', OrderedDict([('@name', 'physics')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Students', OrderedDict([('@name', 2019)])), ('Room', OrderedDict([('@name', 'A101')]))]), OrderedDict([('@name', 9)]), OrderedDict([('@name', 10)]), OrderedDict([('@name', 11)]), OrderedDict([('@name', 12)]), OrderedDict([('@name', 13)])])])])])]

# subgroup for teacher data
subgroupStudent = [OrderedDict([('@name', '2019 Automatic Group Automatic Subgroup'), ('Day', [OrderedDict([('@name', 'Monday'), ('Hour', [OrderedDict([('@name', 8)]), OrderedDict([('@name', 9), ('Teacher', OrderedDict([('@name', 'teacher1')])), ('Subject', OrderedDict([('@name', 'chemistry')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Room', OrderedDict([('@name', 'B101')]))]), OrderedDict([('@name', 10)]), OrderedDict([('@name', 11), ('Teacher', OrderedDict([('@name', 'teacher2')])), ('Subject', OrderedDict([('@name', 'maths')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Room', OrderedDict([('@name', 'B101')]))]), OrderedDict([('@name', 12)]), OrderedDict([('@name', 13)])])]), OrderedDict([('@name', 'Tuesday'), ('Hour', [OrderedDict([('@name', 8)]), OrderedDict([('@name', 9)]), OrderedDict([('@name', 10)]), OrderedDict([('@name', 11)]), OrderedDict([('@name', 12)]), OrderedDict([('@name', 13)])])]), OrderedDict([('@name', 'Wednesday'), ('Hour', [OrderedDict([('@name', 8)]), OrderedDict([('@name', 9)]), OrderedDict([('@name', 10), ('Teacher', OrderedDict([('@name', 'teacher2')])), ('Subject', OrderedDict([('@name', 'physics')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Room', OrderedDict([('@name', 'A101')]))]), OrderedDict([('@name', 11)]), OrderedDict([('@name', 12)]), OrderedDict([('@name', 13), ('Teacher', OrderedDict([('@name', 'teacher2')])), ('Subject', OrderedDict([('@name', 'maths')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Room', OrderedDict([('@name', 'B101')]))])])]), OrderedDict([('@name', 'Thursday'), ('Hour', [OrderedDict([('@name', 8), ('Teacher', OrderedDict([('@name', 'teacher2')])), ('Subject', OrderedDict([('@name', 'physics')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Room', OrderedDict([('@name', 'A101')]))]), OrderedDict([('@name', 9)]), OrderedDict([('@name', 10)]), OrderedDict([('@name', 11)]), OrderedDict([('@name', 12), ('Teacher', OrderedDict([('@name', 'teacher1')])), ('Subject', OrderedDict([('@name', 'chemistry')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Room', OrderedDict([('@name', 'B101')]))]), OrderedDict([('@name', 13)])])])])]), OrderedDict([('@name', '2020 Automatic Group Automatic Subgroup'), ('Day', [OrderedDict([('@name', 'Monday'), ('Hour', [OrderedDict([('@name', 8)]), OrderedDict([('@name', 9)]), OrderedDict([('@name', 10), ('Teacher', OrderedDict([('@name', 'teacher2')])), ('Subject', OrderedDict([('@name', 'maths')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Room', OrderedDict([('@name', 'B101')]))]), OrderedDict([('@name', 11)]), OrderedDict([('@name', 12)]), OrderedDict([('@name', 13), ('Teacher', OrderedDict([('@name', 'teacher2')])), ('Subject', OrderedDict([('@name', 'physics')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Room', OrderedDict([('@name', 'A101')]))])])]), OrderedDict([('@name', 'Tuesday'), ('Hour', [OrderedDict([('@name', 8)]), OrderedDict([('@name', 9)]), OrderedDict([('@name', 10), ('Teacher', OrderedDict([('@name', 'teacher1')])), ('Subject', OrderedDict([('@name', 'chemistry')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Room', OrderedDict([('@name', 'B101')]))]), OrderedDict([('@name', 11), ('Teacher', OrderedDict([('@name', 'teacher2')])), ('Subject', OrderedDict([('@name', 'physics')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Room', OrderedDict([('@name', 'A101')]))]), OrderedDict([('@name', 12)]), OrderedDict([('@name', 13)])])]), OrderedDict([('@name', 'Wednesday'), ('Hour', [OrderedDict([('@name', 8)]), OrderedDict([('@name', 9)]), OrderedDict([('@name', 10)]), OrderedDict([('@name', 11)]), OrderedDict([('@name', 12)]), OrderedDict([('@name', 13)])])]), OrderedDict([('@name', 'Thursday'), ('Hour', [OrderedDict([('@name', 8)]), OrderedDict([('@name', 9)]), OrderedDict([('@name', 10)]), OrderedDict([('@name', 11)]), OrderedDict([('@name', 12)]), OrderedDict([('@name', 13), ('Teacher', OrderedDict([('@name', 'teacher1')])), ('Subject', OrderedDict([('@name', 'chemistry')])), ('Activity_Tag', OrderedDict([('@name', 'tag1')])), ('Room', OrderedDict([('@name', 'B101')]))])])])])])]

fitOrderToDataTestData = {'fileType': 'html', 'data': {'name': '2019 Automatic Group Automatic Subgroup', 'days': [{'name': 'Monday', 'hours': [{'name': 8, 'empty': 'true'}, {'name': 9, 'subject': 'maths', 'activity_tag': [{'name': 'tag1'}], 'teachers': [{'name': 'teacher2'}], 'room': [{'name': 'B101'}]}, {'name': 10, 'empty': 'true'}, {'name': 11, 'subject': 'maths', 'activity_tag': [{'name': 'tag1'}], 'teachers': [{'name': 'teacher2'}], 'room': [{'name': 'B101'}]}, {'name': 12, 'empty': 'true'}, {'name': 13, 'empty': 'true'}]}, {'name': 'Tuesday', 'hours': [{'name': 8, 'subject': 'physics', 'activity_tag': [{'name': 'tag1'}], 'teachers': [{'name': 'teacher2'}], 'room': [{'name': 'A101'}]}, {'name': 9, 'subject': 'chemistry', 'activity_tag': [{'name': 'tag1'}], 'teachers': [{'name': 'teacher1'}], 'room': [{'name': 'B101'}]}, {'name': 10, 'empty': 'true'}, {'name': 11, 'subject': 'physics', 'activity_tag': [{'name': 'tag1'}], 'teachers': [{'name': 'teacher2'}], 'room': [{'name': 'A101'}]}, {'name': 12, 'empty': 'true'}, {'name': 13, 'empty': 'true'}]}, {'name': 'Wednesday', 'hours': [{'name': 8, 'empty': 'true'}, {'name': 9, 'empty': 'true'}, {'name': 10, 'subject': 'chemistry', 'activity_tag': [{'name': 'tag1'}], 'teachers': [{'name': 'teacher1'}], 'room': [{'name': 'B101'}]}, {'name': 11, 'empty': 'true'}, {'name': 12, 'empty': 'true'}, {'name': 13, 'empty': 'true'}]}, {'name': 'Thursday', 'hours': [{'name': 8, 'empty': 'true'}, {'name': 9, 'empty': 'true'}, {'name': 10, 'empty': 'true'}, {'name': 11, 'empty': 'true'}, {'name': 12, 'empty': 'true'}, {'name': 13, 'empty': 'true'}]}]}, 'order': ['Monday_8', 'Tuesday_8', 'Wednesday_8', 'Thursday_8', 'Monday_9', 'Tuesday_9', 'Wednesday_9', 'Thursday_9', 'Monday_10', 'Tuesday_10', 'Wednesday_10', 'Thursday_10', 'Monday_11', 'Tuesday_11', 'Wednesday_11', 'Thursday_11', 'Monday_12', 'Tuesday_12', 'Wednesday_12', 'Thursday_12', 'Monday_13', 'Tuesday_13', 'Wednesday_13', 'Thursday_13'], 'key': '-LoKHh_LxFPCe8aA-h-N'}

fitDataToHtmlTestData  = {'days': [{'name': 'Monday', 'hours': [{'name': 8, 'empty': 'true'}, {'name': 9, 'subject': 'maths', 'activity_tag': [{'name': 'tag1'}], 'teachers': [{'name': 'teacher2'}], 'room': [{'name': 'B101'}]}, {'name': 10, 'empty': 'true'}, {'name': 11, 'subject': 'maths', 'activity_tag': [{'name': 'tag1'}], 'teachers': [{'name': 'teacher2'}], 'room': [{'name': 'B101'}]}, {'name': 12, 'empty': 'true'}, {'name': 13, 'empty': 'true'}]}, {'name': 'Tuesday', 'hours': [{'name': 8, 'subject': 'physics', 'activity_tag': [{'name': 'tag1'}], 'teachers': [{'name': 'teacher2'}], 'room': [{'name': 'A101'}]}, {'name': 9, 'subject': 'chemistry', 'activity_tag': [{'name': 'tag1'}], 'teachers': [{'name': 'teacher1'}], 'room': [{'name': 'B101'}]}, {'name': 10, 'empty': 'true'}, {'name': 11, 'subject': 'physics', 'activity_tag': [{'name': 'tag1'}], 'teachers': [{'name': 'teacher2'}], 'room': [{'name': 'A101'}]}, {'name': 12, 'empty': 'true'}, {'name': 13, 'empty': 'true'}]}, {'name': 'Wednesday', 'hours': [{'name': 8, 'empty': 'true'}, {'name': 9, 'empty': 'true'}, {'name': 10, 'subject': 'chemistry', 'activity_tag': [{'name': 'tag1'}], 'teachers': [{'name': 'teacher1'}], 'room': [{'name': 'B101'}]}, {'name': 11, 'empty': 'true'}, {'name': 12, 'empty': 'true'}, {'name': 13, 'empty': 'true'}]}, {'name': 'Thursday', 'hours': [{'name': 8, 'empty': 'true'}, {'name': 9, 'empty': 'true'}, {'name': 10, 'empty': 'true'}, {'name': 11, 'empty': 'true'}, {'name': 12, 'empty': 'true'}, {'name': 13, 'empty': 'true'}]}], 'name': '2019 Automatic Group Automatic Subgroup'}
