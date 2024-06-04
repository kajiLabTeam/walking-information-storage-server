CREATE DATABASE trajectory;

\c trajectory;

CREATE TABLE pedestrians (
    id VARCHAR(26) PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    deleted_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE floor_maps (
    id VARCHAR(26) PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    deleted_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE floor_map_images (
    id VARCHAR(26) PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    deleted_at TIMESTAMP WITH TIME ZONE,
    floor_map_id VARCHAR(26) REFERENCES floor_maps(id)
);

CREATE TABLE trajectories (
    id VARCHAR(26) PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    deleted_at TIMESTAMP WITH TIME ZONE,
    pedestrian_id VARCHAR(26) REFERENCES pedestrians(id),
    floor_map_id VARCHAR(26) REFERENCES floor_maps(id)
);

CREATE TABLE walking_samples (
    id VARCHAR(26) PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    trajectory_id VARCHAR(26) REFERENCES trajectories(id)
);

CREATE TABLE coordinates (
    id VARCHAR(26) PRIMARY KEY,
    x DECIMAL(10, 2) NOT NULL,
    y DECIMAL(10, 2) NOT NULL,
    walking_sample_id VARCHAR(26) REFERENCES walking_samples(id)
);

CREATE TABLE access_points (
    id VARCHAR(26) PRIMARY KEY,
    address VARCHAR(17) NOT NULL CHECK (
        address ~* '([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})'
    ) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE finger_prints (
    id VARCHAR(26) PRIMARY KEY,
    rssi DECIMAL(5, 2),
    walking_sample_id VARCHAR(26) REFERENCES walking_samples(id),
    access_point_id VARCHAR(26) REFERENCES access_points(id)
);

CREATE TABLE raw_data (
    id VARCHAR(26) PRIMARY KEY,
    walking_sample_id VARCHAR(26) REFERENCES walking_samples(id)
);