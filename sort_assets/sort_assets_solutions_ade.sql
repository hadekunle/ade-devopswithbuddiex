DROP TABLE sort_assets;

CREATE TABLE sort_assets (
    model            varchar(5),
    created          date,
    assignee         varchar(10)
);

INSERT INTO sort_assets VALUES
('A1208','10/11/2019','Tom'),
('A1209','10/9/2019','John'),
('A1209','10/10/2019','Cat'),
('A1210','10/11/2019','Kim'),
('A1210','10/11/2019','Jim'),
('A1208','10/8/2019','Tim'),
('A1210','10/9/2019','Cam'),
('A1209','10/8/2019','Ken'),
('A1209','10/9/2019','Jack'),
('A1208','10/9/2019','Mary'); 


WITH cte AS 
  (
  SELECT model, created, assignee, 
      LPAD(CAST(ROW_NUMBER() OVER (ORDER BY model, created) AS TEXT), 6, '0') 
      AS asset_no
  FROM sort_assets
  )

select asset_no, model, created, assignee from cte;

-- https://sqliteonline.com/

-- TODO: add trigger to resort when new entry is added to table. 
