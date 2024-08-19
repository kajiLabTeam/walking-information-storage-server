\c indoor_location_estimation;


INSERT INTO pedestrians (id)
VALUES
    ('01F8VYXK67BGC1F9RP1E4S9YAK');

INSERT INTO buildings (id, name, latitude, longitude)
VALUES
    ('01F8VYXK67BGC1F9RP1E4S9YAK', '14号館', 35.1847559, 137.1110031);

INSERT INTO floors (id, level, name)
VALUES
    ('01F8VYXK67BGC1F9RP1E4S9YTV', 5, '14号館5階');

INSERT INTO floor_maps (id, floor_id)
VALUES
    ('01J41536W3YYS9KAJC2TVC9JD7', '01F8VYXK67BGC1F9RP1E4S9YTV');
