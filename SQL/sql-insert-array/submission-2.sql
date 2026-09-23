CREATE TABLE stocks (
  id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name TEXT,
  transaction_dates DATE[]
);

-- Do not modify above this line --

INSERT INTO stocks(name, transaction_dates)
  VALUES('AAPL', ARRAY['2007-02-09', '2007-02-10', '2007-02-11']::DATE[]),
  ('GOOG', ARRAY['2004-12-15', '2004-12-16']::DATE[]);





-- Do not modify below this line --
SELECT * FROM stocks;
