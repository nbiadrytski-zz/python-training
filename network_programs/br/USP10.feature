Feature: PowerUp and Initialize My Ethernet Bridge
 	TestID: f1716b42-324a-4fff-9a07-e75b6a423435
 	Author: biadrytm
 	CreationDate: 10.02.2019
 	Reviewer: biadrytm_reviwe
 	ReviewDate: 10.03.2019
 	TestType: Normal Case
 	Specifications: 10799


Scenario: PowerUp and Initialize My Ethernet Bridge
	GIVEN TSCS has sent the ApplicationStateChanged message with device state DEVICE_STATE_CONFIGURATION to TMS
	WHEN TSCS receives the UpdateConfiguration message from TMS containing the information that N Ethernet Bridges will connect
	AND TSCS receives the Connect message from TSIS for the Nth Ethernet Bridge
	THEN TSCS shall send the PowerUp message to all Ethernet Bridges
	AND TSCS shall send the Initialize message to all Ethernet Bridges with an ID to identify the Ethernet Bridges