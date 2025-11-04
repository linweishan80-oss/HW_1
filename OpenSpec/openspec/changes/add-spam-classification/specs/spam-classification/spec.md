## ADDED Requirements
### Requirement: Spam Classification
The system SHALL be able to classify a given text as either "Spam" or "Not Spam".

#### Scenario: Classifying a spam message
- **GIVEN** a trained Naive Bayes model and a TF-IDF vectorizer
- **WHEN** the user provides a text message that is clearly spam (e.g., "Congratulations! You've won a million dollars!")
- **THEN** the system SHALL classify the message as "Spam".

#### Scenario: Classifying a non-spam message
- **GIVEN** a trained Naive Bayes model and a TF-IDF vectorizer
- **WHEN** the user provides a text message that is clearly not spam (e.g., "Hi, are we still on for the meeting tomorrow?")
- **THEN** the system SHALL classify the message as "Not Spam".

### Requirement: User Interface
The system SHALL provide a user interface for spam classification.

#### Scenario: User enters text and gets a classification
- **GIVEN** the Streamlit application is running
- **WHEN** the user enters a text message into a text area and clicks a "Classify" button
- **THEN** the system SHALL display the classification result ("Spam" or "Not Spam") to the user.
