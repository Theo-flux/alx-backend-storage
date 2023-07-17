-- create an index on the first letter of name  col
DROP INDEX idx_name_first ON names;
CREATE INDEX idx_name_first
ON `names` (name(1));

