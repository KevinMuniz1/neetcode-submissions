CREATE TYPE account_type AS ENUM ('checking', 'savings', 'cd', 'money_market');

CREATE TABLE bank_accounts (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    account_type account_type,
    balance INTEGER
);
-- Do not modify above this line --


INSERT INTO bank_accounts(account_type, balance)
    VALUES (account_type('checking'),1000),
    (account_type('savings'), 2000),
    (account_type('cd'),3000),
    (account_type('money_market'),4000);







-- Do not modify below this line --
SELECT * FROM bank_accounts;
