\c indoor_location_estimation;

CREATE TABLE gyroscopes (
    id VARCHAR(26) PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    walking_information_id VARCHAR(26) REFERENCES walking_information(id)
);

CREATE TABLE accelerometers (
    id VARCHAR(26) PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    walking_information_id VARCHAR(26) REFERENCES walking_information(id)
);

CREATE TABLE atmospheric_pressures (
    id VARCHAR(26) PRIMARY KEY,
    pressure DECIMAL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    walking_information_id VARCHAR(26) REFERENCES walking_information(id)
);

CREATE TABLE ratio_waves (
    id VARCHAR(26) PRIMARY KEY,
    rssi DECIMAL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    walking_information_id VARCHAR(26) REFERENCES walking_information(id)
);