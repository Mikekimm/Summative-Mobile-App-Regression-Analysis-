// This is a basic Flutter widget test.
//
// To perform an interaction with a widget in your test, use the WidgetTester
// utility in the flutter_test package. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.

import 'package:flutter_test/flutter_test.dart';

import 'package:linear_regression_app/main.dart';

void main() {
  testWidgets('Insurance App loads home page', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const InsuranceApp());

    // Verify that the home page loads with title
    expect(find.text('Insurance Charges'), findsOneWidget);
    expect(find.text('Predictor'), findsOneWidget);
    expect(find.text('Get Started'), findsOneWidget);
  });

  testWidgets('Navigate to prediction page', (WidgetTester tester) async {
    // Build our app
    await tester.pumpWidget(const InsuranceApp());

    // Tap the Get Started button
    await tester.tap(find.text('Get Started'));
    await tester.pumpAndSettle();

    // Verify prediction page loaded
    expect(find.text('Insurance Prediction'), findsOneWidget);
    expect(find.text('Age'), findsOneWidget);
    expect(find.text('Predict'), findsOneWidget);
  });
}
