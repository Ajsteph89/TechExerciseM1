# Adam Stephens Technical Exercise

This is a technical exercise provided by Members 1st.  For exposing a daily data file over http(s) for further processing and searching.


## How to Run

Navigate to the project directory:

```bash
    cd Members1st
```

Set up a virtual environment for the project using pipenv. If you don't have pipenv installed, you can install it using pip:

```bash
	pip install pipenv
```

Then, activate the virtual environment by running:

```bash
   pipenv shell
```

Install the project dependencies:

```bash
	pipenv install
```

Set up the database by running the migrations:

```bash
   python manage.py migrate
```

Start the development server:

```bash
  python manage.py runserver
```

The app should now be running at http://localhost:8000/
## API Reference

### Search by Id

```http
  GET http://127.0.0.1:8000/entries/id/?search={Id}
```
#### Request Sample:

```
GET     /entries/id/?search=5
Content-Type: json
Authorization: N/A
Host: http://127.0.0.1:8000 

{
""
}

```

#### Response Example (200 OK)

```
{
	"Id": "5",
    "AccountNumber": "0000874494",
    "IdType": 0,
    "CommentCode": 0,
    "TransferCode": 0,
    "AdjustmentCode": 0,
    "RegECode": 0,
    "RegDCheckCode": 0,
    "RegDTransferCode": 0,
    "VoidCode": 0,
    "SubActionCode": "P",
    "SequenceNumber": 684882,
    "EffectiveDate": "2022-04-14T00:00:00Z",
    "PostDate": "2022-04-14T00:00:00Z",
    "PostTime": 1217,
    "PreviousAvailableBalance": "376.44",
    "UserNumber": 0,
    "UserOverride": 0,
    "SecurityLevels": 0,
    "Description": "Laborum minus voluptatibus sequi pariatur necessitatibus minus rerum doloribus.",
    "ActionCode": "D",
    "SourceCode": "E",
    "BalanceChange": "0.00",
    "InterestPenalty": "0.00",
    "NewBalance": "455.53",
    "FeeAmount": "0.00",
    "EscrowAmount": "0.00",
    "LastTranDate": "2022-04-14T00:00:00Z",
    "MaturityLoanDueDate": null,
    "Comment": "Velit earum sed quia et ex doloremque omnis sit.",
    "Branch": 9,
    "ConsoleNumber": 0,
    "BatchSequence": 0,
    "SalesTaxAmount": "0.00",
    "ActivityDate": "2022-04-14T00:00:00Z",
    "BilledFeeAmount": "0.00",
    "ProcessorUser": 0,
    "MemberBranch": "",
    "SubSourceCode": 2,
    "ConfirmationSequence": 0,
    "MicrAccountNumber": "888800000000874494",
    "MicrRtNumber": "",
    "Recurring": 0,
    "FeeExemptCourtesyAmount": "0.00",
    "BalSeg001SegmentId": "",
    "BalSeg001PmtChangeDate": null,
    "InterestEffectiveDate": null,
    "BalSeg001PrevFirstPmtDate": null,
    "DraftNumber": "",
    "TracerNumber": "0000684882",
    "SubSourceDescription": "",
    "TransactionAmount": "266.09",
    "ConfirmationNumber": "0000000005"
}

```

---


### Search by AccountNumber

```http
  GET http://127.0.0.1:8000/entries/account/?search={AccountNumber}
```
#### Request Sample:

```
GET     /entries/account/?search=463562
Content-Type: json
Authorization: N/A
Host: http://127.0.0.1:8000 

{
""
}

```

#### Response Example (200 OK)

```
{
	"Id": "1",
    "AccountNumber": "0000463562",
    "IdType": 1,
    "CommentCode": 0,
    "TransferCode": 0,
    "AdjustmentCode": 0,
    "RegECode": 0,
    "RegDCheckCode": 0,
    "RegDTransferCode": 0,
    "VoidCode": 0,
    "SubActionCode": "5",
    "SequenceNumber": 936633,
    "EffectiveDate": "2022-03-27T00:00:00Z",
    "PostDate": "2022-03-27T00:00:00Z",
    "PostTime": 2326,
    "PreviousAvailableBalance": "-413.98",
    "UserNumber": 0,
    "UserOverride": 0,
    "SecurityLevels": 0,
    "Description": "Delectus et consequatur vero aliquam hic sed.",
    "ActionCode": "W",
    "SourceCode": "C",
    "BalanceChange": "0.00",
    "InterestPenalty": "0.00",
    "NewBalance": "-2.55",
    "FeeAmount": "0.00",
    "EscrowAmount": "0.00",
    "LastTranDate": "2022-03-27T00:00:00Z",
    "MaturityLoanDueDate": null,
    "Comment": "Reprehenderit enim suscipit voluptatem at aut temporibus cum quod est.",
    "Branch": 5,
    "ConsoleNumber": 0,
    "BatchSequence": 0,
    "SalesTaxAmount": "0.00",
    "ActivityDate": "2022-03-27T00:00:00Z",
    "BilledFeeAmount": "0.00",
    "ProcessorUser": 0,
    "MemberBranch": "",
    "SubSourceCode": 0,
    "ConfirmationSequence": 0,
    "MicrAccountNumber": "888800000000463562",
    "MicrRtNumber": "",
    "Recurring": 0,
    "FeeExemptCourtesyAmount": "0.00",
    "BalSeg001SegmentId": "",
    "BalSeg001PmtChangeDate": null,
    "InterestEffectiveDate": null,
    "BalSeg001PrevFirstPmtDate": null,
    "DraftNumber": "",
    "TracerNumber": "0000936633",
    "SubSourceDescription": "",
    "TransactionAmount": "-376.17",
    "ConfirmationNumber": "0000000001"
}

```

---


### Search by Date

```http
  GET http://127.0.0.1:8000/entries/dates/?search={YYYY-MM-DD}
```
#### Request Sample:

```
GET     /entries/dates/?search=2021-07-17
Content-Type: json
Authorization: N/A
Host: http://127.0.0.1:8000 

{
""
}

```

#### Response Example (200 OK)

```
{
	"Id": "45",
    "AccountNumber": "0000656527",
    "IdType": 0,
    "CommentCode": 0,
    "TransferCode": 0,
    "AdjustmentCode": 0,
    "RegECode": 0,
    "RegDCheckCode": 0,
    "RegDTransferCode": 0,
    "VoidCode": 0,
    "SubActionCode": "7",
    "SequenceNumber": 110077,
    "EffectiveDate": "2021-07-17T00:00:00Z",
    "PostDate": "2021-07-17T00:00:00Z",
    "PostTime": 820,
    "PreviousAvailableBalance": "-632.77",
    "UserNumber": 0,
    "UserOverride": 0,
    "SecurityLevels": 0,
    "Description": "Perspiciatis doloribus ex sint minus dolorum.",
    "ActionCode": "W",
    "SourceCode": "S",
    "BalanceChange": "0.00",
    "InterestPenalty": "0.00",
    "NewBalance": "-73.57",
    "FeeAmount": "0.00",
    "EscrowAmount": "0.00",
    "LastTranDate": "2021-07-17T00:00:00Z",
    "MaturityLoanDueDate": null,
    "Comment": "Similique non quae mollitia ut libero ut impedit.",
    "Branch": 1,
    "ConsoleNumber": 0,
    "BatchSequence": 0,
    "SalesTaxAmount": "0.00",
    "ActivityDate": "2021-07-17T00:00:00Z",
    "BilledFeeAmount": "0.00",
    "ProcessorUser": 0,
    "MemberBranch": "",
    "SubSourceCode": 4,
    "ConfirmationSequence": 0,
    "MicrAccountNumber": "888800000000656527",
    "MicrRtNumber": "",
    "Recurring": 0,
    "FeeExemptCourtesyAmount": "0.00",
    "BalSeg001SegmentId": "",
    "BalSeg001PmtChangeDate": null,
    "InterestEffectiveDate": null,
    "BalSeg001PrevFirstPmtDate": null,
    "DraftNumber": "",
    "TracerNumber": "0000110077",
    "SubSourceDescription": "",
    "TransactionAmount": "-307.93",
    "ConfirmationNumber": "0000000045"
}

```
## Notes/Comments

HTTPS
- Not included due to time constraints.
- Planned to follow this [tutorial](https://realpython.com/django-nginx-gunicorn/)

Date Search
- This enpoint currently searchers for a single date and not a range.
- Planned to create custom search filter in views to allow for date range search. 

Search any property/multiple properties
- Began working with dynamic search filter in views.
- Search was not working for all fields, need additional research.
## Authors

- [@Ajsteph89](https://www.github.com/Ajsteph89)
- [LinkedIn](https://www.linkedin.com/in/adam-stephens-802365241)

