# What's New in 4.2

## Overview

This page shows a curated selection of features we’ve released in XMPro version 4.2. For more details on what's in the latest version, please read the [Release Notes](../../release-notes/archived/v4.2.0.md).

## Application Designer

### Recommendation and Alert Scoring

When setting up a Recommendation, authors are now able to fine-tune the Alert Recommendation priority by changing its score. By contrast, Alert Ranking only has options for High, Medium, and Low.

Alert Scores are calculated based on these factors:

* [**Recommendation**](../../how-to-guides/recommendations/manage-recommendations.md#create-a-recommendation) [ ](../../how-to-guides/recommendations/manage-recommendations.md#create-a-recommendation)-  The importance of the recommendation itself
* [**Recommendation Category**](../../how-to-guides/manage-categories.md#adding-a-new-category)  - The importance of the recommendation's category
* [**Recommendation Rule**](../../how-to-guides/recommendations/create-rules.md#create-rules) -  The importance of the specific rule
* [**Recommendation Optional**](../../how-to-guides/recommendations/create-rules.md#create-rules)- Additional Rule Factor value retrieved from the Data Stream.&#x20;

As a recommendation creator, assigning a score to an alert lets you control its importance level more precisely. This Score helps the alert recipient to understand its relative importance.

### Viewing the Alerts

You can view the order of alerts in the Recommendation Alerts list.

<figure><img src="../../.gitbook/assets/Fig 1. Recommendation Alerts list (1).PNG" alt=""><figcaption><p>Fig 1. Recommendation Alerts list</p></figcaption></figure>

You can also view the Scores using the Score Factor Matrix. Follow the steps mentioned [here](../../concepts/recommendation/recommendation-scoring.md#viewing-the-recommendation-scoring).

<figure><img src="../../.gitbook/assets/Fig 2. Score Factor Matrix.PNG" alt=""><figcaption><p>Fig 2. Score Factor Matrix</p></figcaption></figure>

### Auto-Assigning of an Escalated Recommendation Alert

This enhancement automatically assigns an escalated recommendation alert to the previous owner of the original alert. 

To use this, simply check "enable execution order" and "auto-escalate" with the specified rules. 

<figure><img src="../../.gitbook/assets/Fig 3. Auto-Assigning of an Escalated Recommendation Alert.PNG" alt=""><figcaption><p>Fig 3. Auto-Assigning of an Escalated Recommendation Alert</p></figcaption></figure>

You can view this as a timeline entry that creates an audit trail.

### Query Optimization for AD

Experience faster performance and quicker AD queries through optimized Entity Framework settings for database queries.

<figure><img src="../../.gitbook/assets/Fig 4. Query Optimization for AD.PNG" alt=""><figcaption><p>Fig 4. Query Optimization for AD</p></figcaption></figure>

## Subscription Manager

### New Permission - Hide Users Outside of Business Roles

This new permission prevents users’ information from being exposed to users who are not in the same business role group or any of the parent business role groups, enhancing privacy and security.

<figure><img src="../../.gitbook/assets/Fig 5. New Permission - Hide Users Outside of Business Roles.PNG" alt=""><figcaption><p>Fig 5. New Permission - Hide Users Outside of Business Roles</p></figcaption></figure>

## Data Stream Designer

### Agent Category Visual Indicator

Introduced color palettes as visual cues for agent categories. As a user, you can now quickly distinguish between listeners, context providers, transformations, etc.

<figure><img src="../../.gitbook/assets/Fig 6. Agent Category Visual Indicator (1).PNG" alt=""><figcaption><p>Fig 6. Agent Category Visual Indicator</p></figcaption></figure>
