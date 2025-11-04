## ADDED Requirements
### Requirement: Classify User-Provided Text
The system SHALL provide an interface for a user to input a piece of text.

#### Scenario: User enters text
- **GIVEN** a user is on the main application page
- **WHEN** the user enters text into the designated text area
- **AND** clicks the "Classify" button
- **THEN** the system SHALL process the text for classification.

### Requirement: Display Classification Result
The system SHALL classify the input text and display the result to the user.

#### Scenario: Spam classification
- **GIVEN** the system has processed a piece of text
- **WHEN** the text is determined to be spam
- **THEN** the system SHALL display a "Spam" result.

#### Scenario: Not Spam (Ham) classification
- **GIVEN** the system has processed a piece of text
- **WHEN** the text is determined not to be spam
- **THEN** a "Not Spam" (or "Ham") result SHALL be displayed.
